# API collectivity index

This index restores the short collectivity labels that appear immediately after the synopsis on official PETSc manual pages but are omitted by paragraph-length filtering in Skill Seekers 3.9.1. Use the linked full entry for qualifiers and argument semantics.

- Manual-page URLs inspected: 8,378
- Entries with an explicit collectivity label: 6,131
- Pages without a synopsis collectivity label (primarily types, constants, and indexes): 2,247
- Fetch failures after retries: 0

## AO

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `AOApplicationToPetsc` | Collective | <https://petsc.org/release/manualpages/AO/AOApplicationToPetsc/> |
| `AOApplicationToPetscIS` | Collective | <https://petsc.org/release/manualpages/AO/AOApplicationToPetscIS/> |
| `AOApplicationToPetscPermuteInt` | Collective | <https://petsc.org/release/manualpages/AO/AOApplicationToPetscPermuteInt/> |
| `AOApplicationToPetscPermuteReal` | Collective | <https://petsc.org/release/manualpages/AO/AOApplicationToPetscPermuteReal/> |
| `AOCreate` | Collective | <https://petsc.org/release/manualpages/AO/AOCreate/> |
| `AOCreateBasic` | Collective | <https://petsc.org/release/manualpages/AO/AOCreateBasic/> |
| `AOCreateBasicIS` | Collective | <https://petsc.org/release/manualpages/AO/AOCreateBasicIS/> |
| `AOCreateMemoryScalable` | Collective | <https://petsc.org/release/manualpages/AO/AOCreateMemoryScalable/> |
| `AOCreateMemoryScalableIS` | Collective | <https://petsc.org/release/manualpages/AO/AOCreateMemoryScalableIS/> |
| `AODestroy` | Collective | <https://petsc.org/release/manualpages/AO/AODestroy/> |
| `AOGetType` | Not Collective | <https://petsc.org/release/manualpages/AO/AOGetType/> |
| `AOMappingHasApplicationIndex` | Not Collective | <https://petsc.org/release/manualpages/AO/AOMappingHasApplicationIndex/> |
| `AOMappingHasPetscIndex` | Not Collective | <https://petsc.org/release/manualpages/AO/AOMappingHasPetscIndex/> |
| `AOPetscToApplication` | Collective | <https://petsc.org/release/manualpages/AO/AOPetscToApplication/> |
| `AOPetscToApplicationIS` | Collective | <https://petsc.org/release/manualpages/AO/AOPetscToApplicationIS/> |
| `AOPetscToApplicationPermuteInt` | Collective | <https://petsc.org/release/manualpages/AO/AOPetscToApplicationPermuteInt/> |
| `AOPetscToApplicationPermuteReal` | Collective | <https://petsc.org/release/manualpages/AO/AOPetscToApplicationPermuteReal/> |
| `AORegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/AO/AORegister/> |
| `AORegisterAll` | Not Collective | <https://petsc.org/release/manualpages/AO/AORegisterAll/> |
| `AOSetFromOptions` | Collective | <https://petsc.org/release/manualpages/AO/AOSetFromOptions/> |
| `AOSetIS` | Collective | <https://petsc.org/release/manualpages/AO/AOSetIS/> |
| `AOSetType` | Collective | <https://petsc.org/release/manualpages/AO/AOSetType/> |
| `AOView` | Collective | <https://petsc.org/release/manualpages/AO/AOView/> |
| `AOViewFromOptions` | Collective | <https://petsc.org/release/manualpages/AO/AOViewFromOptions/> |

## Bag

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscBagCreate` | Collective | <https://petsc.org/release/manualpages/Bag/PetscBagCreate/> |
| `PetscBagDestroy` | Collective | <https://petsc.org/release/manualpages/Bag/PetscBagDestroy/> |
| `PetscBagGetData` | Not Collective | <https://petsc.org/release/manualpages/Bag/PetscBagGetData/> |
| `PetscBagGetName` | Not Collective | <https://petsc.org/release/manualpages/Bag/PetscBagGetName/> |
| `PetscBagGetNames` | Not Collective | <https://petsc.org/release/manualpages/Bag/PetscBagGetNames/> |
| `PetscBagLoad` | Collective | <https://petsc.org/release/manualpages/Bag/PetscBagLoad/> |
| `PetscBagRegisterBool` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterBool/> |
| `PetscBagRegisterBoolArray` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterBoolArray/> |
| `PetscBagRegisterEnum` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterEnum/> |
| `PetscBagRegisterInt` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterInt/> |
| `PetscBagRegisterInt64` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterInt64/> |
| `PetscBagRegisterIntArray` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterIntArray/> |
| `PetscBagRegisterReal` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterReal/> |
| `PetscBagRegisterRealArray` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterRealArray/> |
| `PetscBagRegisterScalar` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterScalar/> |
| `PetscBagRegisterString` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagRegisterString/> |
| `PetscBagSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Bag/PetscBagSetFromOptions/> |
| `PetscBagSetName` | Not Collective | <https://petsc.org/release/manualpages/Bag/PetscBagSetName/> |
| `PetscBagSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Bag/PetscBagSetOptionsPrefix/> |
| `PetscBagView` | Collective | <https://petsc.org/release/manualpages/Bag/PetscBagView/> |
| `PetscBagViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Bag/PetscBagViewFromOptions/> |

## BM

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscBenchCreate` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchCreate/> |
| `PetscBenchDestroy` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchDestroy/> |
| `PetscBenchGetSize` | Logically Collective | <https://petsc.org/release/manualpages/BM/PetscBenchGetSize/> |
| `PetscBenchGetType` | Not Collective | <https://petsc.org/release/manualpages/BM/PetscBenchGetType/> |
| `PetscBenchRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/BM/PetscBenchRegister/> |
| `PetscBenchReset` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchReset/> |
| `PetscBenchRun` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchRun/> |
| `PetscBenchSetFromOptions` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchSetFromOptions/> |
| `PetscBenchSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/BM/PetscBenchSetOptionsPrefix/> |
| `PetscBenchSetSize` | Logically Collective | <https://petsc.org/release/manualpages/BM/PetscBenchSetSize/> |
| `PetscBenchSetType` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchSetType/> |
| `PetscBenchSetUp` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchSetUp/> |
| `PetscBenchView` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchView/> |
| `PetscBenchViewFromOptions` | Collective | <https://petsc.org/release/manualpages/BM/PetscBenchViewFromOptions/> |

## Characteristic

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `CharacteristicCreate` | Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicCreate/> |
| `CharacteristicDestroy` | Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicDestroy/> |
| `CharacteristicRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Characteristic/CharacteristicRegister/> |
| `CharacteristicRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicRegisterAll/> |
| `CharacteristicSetFieldInterpolation` | Not Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicSetFieldInterpolation/> |
| `CharacteristicSetFieldInterpolationLocal` | Not Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicSetFieldInterpolationLocal/> |
| `CharacteristicSetType` | Logically Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicSetType/> |
| `CharacteristicSetUp` | Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicSetUp/> |
| `CharacteristicSetVelocityInterpolation` | Not Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicSetVelocityInterpolation/> |
| `CharacteristicSetVelocityInterpolationLocal` | Not Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicSetVelocityInterpolationLocal/> |
| `CharacteristicSolve` | Collective | <https://petsc.org/release/manualpages/Characteristic/CharacteristicSolve/> |
| `DMDAMapCoordsToPeriodicDomain` | Not Collective | <https://petsc.org/release/manualpages/Characteristic/DMDAMapCoordsToPeriodicDomain/> |

## Device

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PETSC_DEVICE_DEFAULT` | Not Collective | <https://petsc.org/release/manualpages/Device/PETSC_DEVICE_DEFAULT/> |
| `PetscDeviceArrayCopy` | Not Collective, Asynchronous, Auto-dependency aware | <https://petsc.org/release/manualpages/Device/PetscDeviceArrayCopy/> |
| `PetscDeviceArrayZero` | Not Collective, Asynchronous, Auto-dependency aware | <https://petsc.org/release/manualpages/Device/PetscDeviceArrayZero/> |
| `PetscDeviceCalloc` | Not Collective, Asynchronous, Auto-dependency aware | <https://petsc.org/release/manualpages/Device/PetscDeviceCalloc/> |
| `PetscDeviceConfigure` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceConfigure/> |
| `PetscDeviceContextCreate` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextCreate/> |
| `PetscDeviceContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextDestroy/> |
| `PetscDeviceContextDuplicate` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextDuplicate/> |
| `PetscDeviceContextFork` | Not Collective, Asynchronous | <https://petsc.org/release/manualpages/Device/PetscDeviceContextFork/> |
| `PetscDeviceContextForkWithStreamType` | Not Collective, Asynchronous | <https://petsc.org/release/manualpages/Device/PetscDeviceContextForkWithStreamType/> |
| `PetscDeviceContextGetCurrentContext` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextGetCurrentContext/> |
| `PetscDeviceContextGetDevice` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextGetDevice/> |
| `PetscDeviceContextGetDeviceType` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextGetDeviceType/> |
| `PetscDeviceContextGetStreamType` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextGetStreamType/> |
| `PetscDeviceContextJoin` | Not Collective, Asynchronous | <https://petsc.org/release/manualpages/Device/PetscDeviceContextJoin/> |
| `PetscDeviceContextMarkIntentFromID` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextMarkIntentFromID/> |
| `PetscDeviceContextQueryIdle` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextQueryIdle/> |
| `PetscDeviceContextSetCurrentContext` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextSetCurrentContext/> |
| `PetscDeviceContextSetDevice` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextSetDevice/> |
| `PetscDeviceContextSetFromOptions` | Collective on comm or dctx | <https://petsc.org/release/manualpages/Device/PetscDeviceContextSetFromOptions/> |
| `PetscDeviceContextSetStreamType` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextSetStreamType/> |
| `PetscDeviceContextSetUp` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextSetUp/> |
| `PetscDeviceContextSynchronize` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextSynchronize/> |
| `PetscDeviceContextView` | Collective on viewer | <https://petsc.org/release/manualpages/Device/PetscDeviceContextView/> |
| `PetscDeviceContextWaitForContext` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceContextWaitForContext/> |
| `PetscDeviceCreate` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceCreate/> |
| `PetscDeviceDestroy` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceDestroy/> |
| `PetscDeviceFree` | Not Collective, Asynchronous, Auto-dependency aware | <https://petsc.org/release/manualpages/Device/PetscDeviceFree/> |
| `PetscDeviceGetAttribute` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceGetAttribute/> |
| `PetscDeviceGetDeviceId` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceGetDeviceId/> |
| `PetscDeviceGetType` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceGetType/> |
| `PetscDeviceInitialize` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceInitialize/> |
| `PetscDeviceInitialized` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceInitialized/> |
| `PetscDeviceMalloc` | Not Collective, Asynchronous, Auto-dependency aware | <https://petsc.org/release/manualpages/Device/PetscDeviceMalloc/> |
| `PetscDeviceMemcpy` | Not Collective, Asynchronous, Auto-dependency aware | <https://petsc.org/release/manualpages/Device/PetscDeviceMemcpy/> |
| `PetscDeviceMemset` | Not Collective, Asynchronous, Auto-dependency aware | <https://petsc.org/release/manualpages/Device/PetscDeviceMemset/> |
| `PetscDeviceRegisterMemory` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceRegisterMemory/> |
| `PetscDeviceSetDefaultDeviceType` | Not Collective | <https://petsc.org/release/manualpages/Device/PetscDeviceSetDefaultDeviceType/> |
| `PetscDeviceView` | Collective on viewer | <https://petsc.org/release/manualpages/Device/PetscDeviceView/> |
| `WaitForHIP` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Device/WaitForHIP/> |

## DM

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMAdaptInterpolator` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptInterpolator/> |
| `DMAdaptLabel` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptLabel/> |
| `DMAdaptorAdapt` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorAdapt/> |
| `DMAdaptorCreate` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorCreate/> |
| `DMAdaptorDestroy` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorDestroy/> |
| `DMAdaptorGetCriterion` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorGetCriterion/> |
| `DMAdaptorGetMixedSetupFunction` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorGetMixedSetupFunction/> |
| `DMAdaptorGetSequenceLength` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorGetSequenceLength/> |
| `DMAdaptorGetSolver` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorGetSolver/> |
| `DMAdaptorGetTransferFunction` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorGetTransferFunction/> |
| `DMAdaptorGetType` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorGetType/> |
| `DMAdaptorMonitor` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitor/> |
| `DMAdaptorMonitorCancel` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorCancel/> |
| `DMAdaptorMonitorError` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorError/> |
| `DMAdaptorMonitorErrorDraw` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorErrorDraw/> |
| `DMAdaptorMonitorErrorDrawLG` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorErrorDrawLG/> |
| `DMAdaptorMonitorErrorDrawLGCreate` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorErrorDrawLGCreate/> |
| `DMAdaptorMonitorRegister` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorRegister/> |
| `DMAdaptorMonitorRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorRegisterAll/> |
| `DMAdaptorMonitorRegisterDestroy` | Not collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorRegisterDestroy/> |
| `DMAdaptorMonitorSet` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorSet/> |
| `DMAdaptorMonitorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorSetFromOptions/> |
| `DMAdaptorMonitorSize` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorMonitorSize/> |
| `DMAdaptorRegister` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorRegister/> |
| `DMAdaptorRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorRegisterAll/> |
| `DMAdaptorRegisterDestroy` | Not collective | <https://petsc.org/release/manualpages/DM/DMAdaptorRegisterDestroy/> |
| `DMAdaptorSetCriterion` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetCriterion/> |
| `DMAdaptorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetFromOptions/> |
| `DMAdaptorSetMixedSetupFunction` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetMixedSetupFunction/> |
| `DMAdaptorSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetOptionsPrefix/> |
| `DMAdaptorSetSequenceLength` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetSequenceLength/> |
| `DMAdaptorSetSolver` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetSolver/> |
| `DMAdaptorSetTransferFunction` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetTransferFunction/> |
| `DMAdaptorSetType` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetType/> |
| `DMAdaptorSetUp` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorSetUp/> |
| `DMAdaptorView` | Collective | <https://petsc.org/release/manualpages/DM/DMAdaptorView/> |
| `DMAddBoundary` | Collective | <https://petsc.org/release/manualpages/DM/DMAddBoundary/> |
| `DMAddField` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMAddField/> |
| `DMAddLabel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMAddLabel/> |
| `DMAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMAppendOptionsPrefix/> |
| `DMCheckInterpolator` | Collective | <https://petsc.org/release/manualpages/DM/DMCheckInterpolator/> |
| `DMClearAuxiliaryVec` | Not Collective | <https://petsc.org/release/manualpages/DM/DMClearAuxiliaryVec/> |
| `DMClearDS` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMClearDS/> |
| `DMClearFields` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMClearFields/> |
| `DMClearGlobalVectors` | Collective | <https://petsc.org/release/manualpages/DM/DMClearGlobalVectors/> |
| `DMClearLabelStratum` | Not Collective | <https://petsc.org/release/manualpages/DM/DMClearLabelStratum/> |
| `DMClearLabelValue` | Not Collective | <https://petsc.org/release/manualpages/DM/DMClearLabelValue/> |
| `DMClearLocalVectors` | Collective | <https://petsc.org/release/manualpages/DM/DMClearLocalVectors/> |
| `DMClearNamedGlobalVectors` | Collective | <https://petsc.org/release/manualpages/DM/DMClearNamedGlobalVectors/> |
| `DMClearNamedLocalVectors` | Collective | <https://petsc.org/release/manualpages/DM/DMClearNamedLocalVectors/> |
| `DMClone` | Collective | <https://petsc.org/release/manualpages/DM/DMClone/> |
| `DMCoarsen` | Collective | <https://petsc.org/release/manualpages/DM/DMCoarsen/> |
| `DMCoarsenHierarchy` | Collective | <https://petsc.org/release/manualpages/DM/DMCoarsenHierarchy/> |
| `DMCoarsenHookAdd` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMCoarsenHookAdd/> |
| `DMCoarsenHookRemove` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMCoarsenHookRemove/> |
| `DMCompareLabels` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMCompareLabels/> |
| `DMComputeError` | Collective | <https://petsc.org/release/manualpages/DM/DMComputeError/> |
| `DMComputeExactSolution` | Collective | <https://petsc.org/release/manualpages/DM/DMComputeExactSolution/> |
| `DMComputeL2Diff` | Collective | <https://petsc.org/release/manualpages/DM/DMComputeL2Diff/> |
| `DMComputeL2FieldDiff` | Collective | <https://petsc.org/release/manualpages/DM/DMComputeL2FieldDiff/> |
| `DMComputeL2GradientDiff` | Collective | <https://petsc.org/release/manualpages/DM/DMComputeL2GradientDiff/> |
| `DMComputeVariableBounds` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMComputeVariableBounds/> |
| `DMConvert` | Collective | <https://petsc.org/release/manualpages/DM/DMConvert/> |
| `DMCopyAuxiliaryVec` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCopyAuxiliaryVec/> |
| `DMCopyDisc` | Collective | <https://petsc.org/release/manualpages/DM/DMCopyDisc/> |
| `DMCopyDS` | Collective | <https://petsc.org/release/manualpages/DM/DMCopyDS/> |
| `DMCopyFields` | Collective | <https://petsc.org/release/manualpages/DM/DMCopyFields/> |
| `DMCopyLabels` | Collective | <https://petsc.org/release/manualpages/DM/DMCopyLabels/> |
| `DMCopyTransform` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCopyTransform/> |
| `DMCreate` | Collective | <https://petsc.org/release/manualpages/DM/DMCreate/> |
| `DMCreateColoring` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateColoring/> |
| `DMCreateDomainDecomposition` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCreateDomainDecomposition/> |
| `DMCreateDomainDecompositionScatters` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCreateDomainDecompositionScatters/> |
| `DMCreateDS` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateDS/> |
| `DMCreateFEDefault` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCreateFEDefault/> |
| `DMCreateFieldDecomposition` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMCreateFieldDecomposition/> |
| `DMCreateFieldIS` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMCreateFieldIS/> |
| `DMCreateGlobalVector` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateGlobalVector/> |
| `DMCreateGradientMatrix` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateGradientMatrix/> |
| `DMCreateInjection` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateInjection/> |
| `DMCreateInterpolation` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateInterpolation/> |
| `DMCreateLabel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCreateLabel/> |
| `DMCreateLabelAtIndex` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCreateLabelAtIndex/> |
| `DMCreateLocalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCreateLocalVector/> |
| `DMCreateMassMatrix` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateMassMatrix/> |
| `DMCreateMassMatrixLumped` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateMassMatrixLumped/> |
| `DMCreateMatrix` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateMatrix/> |
| `DMCreateRestriction` | Collective | <https://petsc.org/release/manualpages/DM/DMCreateRestriction/> |
| `DMCreateSectionSubDM` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCreateSectionSubDM/> |
| `DMCreateSectionSuperDM` | Not Collective | <https://petsc.org/release/manualpages/DM/DMCreateSectionSuperDM/> |
| `DMCreateSubDM` | Not collective | <https://petsc.org/release/manualpages/DM/DMCreateSubDM/> |
| `DMCreateSuperDM` | Not collective | <https://petsc.org/release/manualpages/DM/DMCreateSuperDM/> |
| `DMDestroy` | Collective | <https://petsc.org/release/manualpages/DM/DMDestroy/> |
| `DMExtrude` | Collective | <https://petsc.org/release/manualpages/DM/DMExtrude/> |
| `DMFieldCreateDA` | Collective | <https://petsc.org/release/manualpages/DM/DMFieldCreateDA/> |
| `DMFieldCreateDefaultFaceQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldCreateDefaultFaceQuadrature/> |
| `DMFieldCreateDefaultQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldCreateDefaultQuadrature/> |
| `DMFieldCreateDS` | Collective | <https://petsc.org/release/manualpages/DM/DMFieldCreateDS/> |
| `DMFieldCreateDSWithDG` | Collective | <https://petsc.org/release/manualpages/DM/DMFieldCreateDSWithDG/> |
| `DMFieldCreateFEGeom` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldCreateFEGeom/> |
| `DMFieldCreateShell` | Collective | <https://petsc.org/release/manualpages/DM/DMFieldCreateShell/> |
| `DMFieldDestroy` | Collective | <https://petsc.org/release/manualpages/DM/DMFieldDestroy/> |
| `DMFieldEvaluate` | Collective | <https://petsc.org/release/manualpages/DM/DMFieldEvaluate/> |
| `DMFieldEvaluateFE` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldEvaluateFE/> |
| `DMFieldEvaluateFV` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldEvaluateFV/> |
| `DMFieldFinalizePackage` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMFieldFinalizePackage/> |
| `DMFieldGetDegree` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldGetDegree/> |
| `DMFieldGetDM` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldGetDM/> |
| `DMFieldGetNumComponents` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldGetNumComponents/> |
| `DMFieldGetType` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldGetType/> |
| `DMFieldInitializePackage` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMFieldInitializePackage/> |
| `DMFieldRegister` | Not collective, No Fortran Support | <https://petsc.org/release/manualpages/DM/DMFieldRegister/> |
| `DMFieldRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldRegisterAll/> |
| `DMFieldSetType` | Collective | <https://petsc.org/release/manualpages/DM/DMFieldSetType/> |
| `DMFieldShellEvaluateFEDefault` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellEvaluateFEDefault/> |
| `DMFieldShellEvaluateFVDefault` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellEvaluateFVDefault/> |
| `DMFieldShellGetContext` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellGetContext/> |
| `DMFieldShellSetCreateDefaultQuadrature` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellSetCreateDefaultQuadrature/> |
| `DMFieldShellSetDestroy` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellSetDestroy/> |
| `DMFieldShellSetEvaluate` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellSetEvaluate/> |
| `DMFieldShellSetEvaluateFE` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellSetEvaluateFE/> |
| `DMFieldShellSetEvaluateFV` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellSetEvaluateFV/> |
| `DMFieldShellSetGetDegree` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMFieldShellSetGetDegree/> |
| `DMFieldView` | Collective | <https://petsc.org/release/manualpages/DM/DMFieldView/> |
| `DMFindRegionNum` | Not Collective | <https://petsc.org/release/manualpages/DM/DMFindRegionNum/> |
| `DMGenerateRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/DM/DMGenerateRegister/> |
| `DMGenerateRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGenerateRegisterAll/> |
| `DMGenerateRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGenerateRegisterDestroy/> |
| `DMGeomModelRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/DM/DMGeomModelRegister/> |
| `DMGeomModelRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGeomModelRegisterAll/> |
| `DMGeomModelRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGeomModelRegisterDestroy/> |
| `DMGetAdjacency` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetAdjacency/> |
| `DMGetApplicationContext` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetApplicationContext/> |
| `DMGetAuxiliaryLabels` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetAuxiliaryLabels/> |
| `DMGetAuxiliaryVec` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetAuxiliaryVec/> |
| `DMGetBasicAdjacency` | Not collective | <https://petsc.org/release/manualpages/DM/DMGetBasicAdjacency/> |
| `DMGetBlockingType` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetBlockingType/> |
| `DMGetBlockSize` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetBlockSize/> |
| `DMGetBoundingBox` | Collective | <https://petsc.org/release/manualpages/DM/DMGetBoundingBox/> |
| `DMGetCeed` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCeed/> |
| `DMGetCellCoordinateDM` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCellCoordinateDM/> |
| `DMGetCellCoordinates` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCellCoordinates/> |
| `DMGetCellCoordinateSection` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCellCoordinateSection/> |
| `DMGetCellCoordinatesLocal` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCellCoordinatesLocal/> |
| `DMGetCellCoordinatesLocalNoncollective` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCellCoordinatesLocalNoncollective/> |
| `DMGetCellCoordinatesLocalSetUp` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCellCoordinatesLocalSetUp/> |
| `DMGetCellDS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCellDS/> |
| `DMGetCoarseDM` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCoarseDM/> |
| `DMGetCoarsenLevel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCoarsenLevel/> |
| `DMGetCompatibility` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCompatibility/> |
| `DMGetCoordinateDim` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinateDim/> |
| `DMGetCoordinateDM` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinateDM/> |
| `DMGetCoordinateField` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinateField/> |
| `DMGetCoordinates` | Collective if the global vector with coordinates has not been set yet but the local vector with coordinates has been set | <https://petsc.org/release/manualpages/DM/DMGetCoordinates/> |
| `DMGetCoordinateSection` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinateSection/> |
| `DMGetCoordinatesLocal` | Collective the first time it is called | <https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocal/> |
| `DMGetCoordinatesLocalized` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalized/> |
| `DMGetCoordinatesLocalizedLocal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalizedLocal/> |
| `DMGetCoordinatesLocalNoncollective` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalNoncollective/> |
| `DMGetCoordinatesLocalSetUp` | Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalSetUp/> |
| `DMGetCoordinatesLocalTuple` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalTuple/> |
| `DMGetDefaultConstraints` | not Collective | <https://petsc.org/release/manualpages/DM/DMGetDefaultConstraints/> |
| `DMGetDimension` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetDimension/> |
| `DMGetDimPoints` | Collective | <https://petsc.org/release/manualpages/DM/DMGetDimPoints/> |
| `DMGetDS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetDS/> |
| `DMGetField` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetField/> |
| `DMGetFieldAvoidTensor` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetFieldAvoidTensor/> |
| `DMGetGlobalSection` | Collective | <https://petsc.org/release/manualpages/DM/DMGetGlobalSection/> |
| `DMGetGlobalVector` | Collective | <https://petsc.org/release/manualpages/DM/DMGetGlobalVector/> |
| `DMGetISColoringType` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMGetISColoringType/> |
| `DMGetLabel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLabel/> |
| `DMGetLabelByNum` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLabelByNum/> |
| `DMGetLabelIdIS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLabelIdIS/> |
| `DMGetLabelName` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLabelName/> |
| `DMGetLabelOutput` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLabelOutput/> |
| `DMGetLabelSize` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLabelSize/> |
| `DMGetLabelValue` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLabelValue/> |
| `DMGetLocalBoundingBox` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLocalBoundingBox/> |
| `DMGetLocalToGlobalMapping` | Collective | <https://petsc.org/release/manualpages/DM/DMGetLocalToGlobalMapping/> |
| `DMGetLocalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetLocalVector/> |
| `DMGetMatType` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMGetMatType/> |
| `DMGetNamedGlobalVector` | Collective | <https://petsc.org/release/manualpages/DM/DMGetNamedGlobalVector/> |
| `DMGetNamedLocalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetNamedLocalVector/> |
| `DMGetNearNullSpaceConstructor` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMGetNearNullSpaceConstructor/> |
| `DMGetNeighbors` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetNeighbors/> |
| `DMGetNullSpaceConstructor` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMGetNullSpaceConstructor/> |
| `DMGetNumAuxiliaryVec` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetNumAuxiliaryVec/> |
| `DMGetNumDS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetNumDS/> |
| `DMGetNumFields` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetNumFields/> |
| `DMGetNumLabels` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetNumLabels/> |
| `DMGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetOptionsPrefix/> |
| `DMGetOutputDM` | Collective | <https://petsc.org/release/manualpages/DM/DMGetOutputDM/> |
| `DMGetPeriodicity` | Not collective | <https://petsc.org/release/manualpages/DM/DMGetPeriodicity/> |
| `DMGetPointSF` | Not collective but the resulting PetscSF is collective | <https://petsc.org/release/manualpages/DM/DMGetPointSF/> |
| `DMGetRefineLevel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetRefineLevel/> |
| `DMGetRegionDS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetRegionDS/> |
| `DMGetRegionNumDS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetRegionNumDS/> |
| `DMGetSparseLocalize` | Not collective | <https://petsc.org/release/manualpages/DM/DMGetSparseLocalize/> |
| `DMGetStratumIS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetStratumIS/> |
| `DMGetStratumSize` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetStratumSize/> |
| `DMGetType` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetType/> |
| `DMGetUseNatural` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetUseNatural/> |
| `DMGetVecType` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMGetVecType/> |
| `DMGetWorkArray` | Not Collective | <https://petsc.org/release/manualpages/DM/DMGetWorkArray/> |
| `DMGlobalToLocal` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DM/DMGlobalToLocal/> |
| `DMGlobalToLocalBegin` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DM/DMGlobalToLocalBegin/> |
| `DMGlobalToLocalBeginDefaultShell` | Collective | <https://petsc.org/release/manualpages/DM/DMGlobalToLocalBeginDefaultShell/> |
| `DMGlobalToLocalEnd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DM/DMGlobalToLocalEnd/> |
| `DMGlobalToLocalHookAdd` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMGlobalToLocalHookAdd/> |
| `DMGlobalToLocalSolve` | Collective | <https://petsc.org/release/manualpages/DM/DMGlobalToLocalSolve/> |
| `DMHasBound` | Logically collective | <https://petsc.org/release/manualpages/DM/DMHasBound/> |
| `DMHasColoring` | Not Collective | <https://petsc.org/release/manualpages/DM/DMHasColoring/> |
| `DMHasCreateInjection` | Not Collective | <https://petsc.org/release/manualpages/DM/DMHasCreateInjection/> |
| `DMHasCreateRestriction` | Not Collective | <https://petsc.org/release/manualpages/DM/DMHasCreateRestriction/> |
| `DMHasLabel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMHasLabel/> |
| `DMHasNamedGlobalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMHasNamedGlobalVector/> |
| `DMHasNamedLocalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMHasNamedLocalVector/> |
| `DMHasVariableBounds` | Not Collective | <https://petsc.org/release/manualpages/DM/DMHasVariableBounds/> |
| `DMInterpolate` | Collective if any hooks are | <https://petsc.org/release/manualpages/DM/DMInterpolate/> |
| `DMInterpolateSolution` | Collective | <https://petsc.org/release/manualpages/DM/DMInterpolateSolution/> |
| `DMInterpolationAddPoints` | Not Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationAddPoints/> |
| `DMInterpolationCreate` | Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationCreate/> |
| `DMInterpolationDestroy` | Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationDestroy/> |
| `DMInterpolationGetCoordinates` | Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationGetCoordinates/> |
| `DMInterpolationGetDim` | Not Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationGetDim/> |
| `DMInterpolationGetDof` | Not Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationGetDof/> |
| `DMInterpolationGetVector` | Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationGetVector/> |
| `DMInterpolationRestoreVector` | Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationRestoreVector/> |
| `DMInterpolationSetDim` | Not Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationSetDim/> |
| `DMInterpolationSetDof` | Not Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationSetDof/> |
| `DMInterpolationSetUp` | Collective | <https://petsc.org/release/manualpages/DM/DMInterpolationSetUp/> |
| `DMIsBoundaryPoint` | Not Collective | <https://petsc.org/release/manualpages/DM/DMIsBoundaryPoint/> |
| `DMLoad` | Collective | <https://petsc.org/release/manualpages/DM/DMLoad/> |
| `DMLocalizeCoordinates` | Collective | <https://petsc.org/release/manualpages/DM/DMLocalizeCoordinates/> |
| `DMLocalToGlobal` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DM/DMLocalToGlobal/> |
| `DMLocalToGlobalBegin` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DM/DMLocalToGlobalBegin/> |
| `DMLocalToGlobalEnd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DM/DMLocalToGlobalEnd/> |
| `DMLocalToGlobalHookAdd` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMLocalToGlobalHookAdd/> |
| `DMLocalToLocalBegin` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DM/DMLocalToLocalBegin/> |
| `DMLocalToLocalEnd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DM/DMLocalToLocalEnd/> |
| `DMLocatePoints` | Collective | <https://petsc.org/release/manualpages/DM/DMLocatePoints/> |
| `DMMonitor` | Collective | <https://petsc.org/release/manualpages/DM/DMMonitor/> |
| `DMMonitorCancel` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMMonitorCancel/> |
| `DMMonitorSet` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMMonitorSet/> |
| `DMMonitorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/DM/DMMonitorSetFromOptions/> |
| `DMPolytopeGetOrientation` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPolytopeGetOrientation/> |
| `DMPolytopeGetVertexOrientation` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPolytopeGetVertexOrientation/> |
| `DMPolytopeInCellTest` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPolytopeInCellTest/> |
| `DMPolytopeMatchOrientation` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPolytopeMatchOrientation/> |
| `DMPolytopeMatchVertexOrientation` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPolytopeMatchVertexOrientation/> |
| `DMPrintCellIndices` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPrintCellIndices/> |
| `DMPrintCellMatrix` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPrintCellMatrix/> |
| `DMPrintCellVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPrintCellVector/> |
| `DMPrintCellVectorReal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMPrintCellVectorReal/> |
| `DMPrintLocalVec` | Collective | <https://petsc.org/release/manualpages/DM/DMPrintLocalVec/> |
| `DMProjectBdFieldLabelLocal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMProjectBdFieldLabelLocal/> |
| `DMProjectField` | Collective | <https://petsc.org/release/manualpages/DM/DMProjectField/> |
| `DMProjectFieldLabel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMProjectFieldLabel/> |
| `DMProjectFieldLabelLocal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMProjectFieldLabelLocal/> |
| `DMProjectFieldLocal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMProjectFieldLocal/> |
| `DMProjectFunction` | Collective | <https://petsc.org/release/manualpages/DM/DMProjectFunction/> |
| `DMProjectFunctionLabel` | Collective | <https://petsc.org/release/manualpages/DM/DMProjectFunctionLabel/> |
| `DMProjectFunctionLabelLocal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMProjectFunctionLabelLocal/> |
| `DMProjectFunctionLocal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMProjectFunctionLocal/> |
| `DMRedundantCreate` | Collective | <https://petsc.org/release/manualpages/DM/DMRedundantCreate/> |
| `DMRedundantGetSize` | Not Collective | <https://petsc.org/release/manualpages/DM/DMRedundantGetSize/> |
| `DMRedundantSetSize` | Collective | <https://petsc.org/release/manualpages/DM/DMRedundantSetSize/> |
| `DMRefine` | Collective | <https://petsc.org/release/manualpages/DM/DMRefine/> |
| `DMRefineHierarchy` | Collective | <https://petsc.org/release/manualpages/DM/DMRefineHierarchy/> |
| `DMRefineHookAdd` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMRefineHookAdd/> |
| `DMRefineHookRemove` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMRefineHookRemove/> |
| `DMRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/DM/DMRegister/> |
| `DMRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/DMRegisterAll/> |
| `DMRemoveLabel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMRemoveLabel/> |
| `DMRemoveLabelBySelf` | Not Collective | <https://petsc.org/release/manualpages/DM/DMRemoveLabelBySelf/> |
| `DMReorderSectionGetDefault` | Not collective | <https://petsc.org/release/manualpages/DM/DMReorderSectionGetDefault/> |
| `DMReorderSectionGetType` | Not collective | <https://petsc.org/release/manualpages/DM/DMReorderSectionGetType/> |
| `DMReorderSectionSetDefault` | Logically collective | <https://petsc.org/release/manualpages/DM/DMReorderSectionSetDefault/> |
| `DMReorderSectionSetType` | Logically collective | <https://petsc.org/release/manualpages/DM/DMReorderSectionSetType/> |
| `DMRestoreGlobalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMRestoreGlobalVector/> |
| `DMRestoreLocalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMRestoreLocalVector/> |
| `DMRestoreNamedGlobalVector` | Collective | <https://petsc.org/release/manualpages/DM/DMRestoreNamedGlobalVector/> |
| `DMRestoreNamedLocalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMRestoreNamedLocalVector/> |
| `DMRestoreWorkArray` | Not Collective | <https://petsc.org/release/manualpages/DM/DMRestoreWorkArray/> |
| `DMRestrict` | Collective if any hooks are | <https://petsc.org/release/manualpages/DM/DMRestrict/> |
| `DMSetAdjacency` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetAdjacency/> |
| `DMSetApplicationContext` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetApplicationContext/> |
| `DMSetApplicationContextDestroy` | Logically Collective if the function is collective | <https://petsc.org/release/manualpages/DM/DMSetApplicationContextDestroy/> |
| `DMSetAuxiliaryVec` | Not Collective because auxiliary vectors are not parallel | <https://petsc.org/release/manualpages/DM/DMSetAuxiliaryVec/> |
| `DMSetBasicAdjacency` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetBasicAdjacency/> |
| `DMSetBlockingType` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetBlockingType/> |
| `DMSetCellCoordinateDM` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetCellCoordinateDM/> |
| `DMSetCellCoordinateField` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetCellCoordinateField/> |
| `DMSetCellCoordinates` | Collective | <https://petsc.org/release/manualpages/DM/DMSetCellCoordinates/> |
| `DMSetCellCoordinateSection` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetCellCoordinateSection/> |
| `DMSetCellCoordinatesLocal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetCellCoordinatesLocal/> |
| `DMSetCoarsenLevel` | Collective | <https://petsc.org/release/manualpages/DM/DMSetCoarsenLevel/> |
| `DMSetCoordinateDim` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetCoordinateDim/> |
| `DMSetCoordinateDM` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetCoordinateDM/> |
| `DMSetCoordinateField` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetCoordinateField/> |
| `DMSetCoordinates` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetCoordinates/> |
| `DMSetCoordinateSection` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetCoordinateSection/> |
| `DMSetCoordinatesLocal` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetCoordinatesLocal/> |
| `DMSetDefaultConstraints` | Collective | <https://petsc.org/release/manualpages/DM/DMSetDefaultConstraints/> |
| `DMSetDimension` | Collective | <https://petsc.org/release/manualpages/DM/DMSetDimension/> |
| `DMSetField` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetField/> |
| `DMSetFieldAvoidTensor` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetFieldAvoidTensor/> |
| `DMSetFromOptions` | Collective | <https://petsc.org/release/manualpages/DM/DMSetFromOptions/> |
| `DMSetISColoringType` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetISColoringType/> |
| `DMSetLabel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetLabel/> |
| `DMSetLabelOutput` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetLabelOutput/> |
| `DMSetLabelValue` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetLabelValue/> |
| `DMSetMatrixPreallocateOnly` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetMatrixPreallocateOnly/> |
| `DMSetMatrixPreallocateSkip` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetMatrixPreallocateSkip/> |
| `DMSetMatrixStructureOnly` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetMatrixStructureOnly/> |
| `DMSetMatType` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetMatType/> |
| `DMSetNearNullSpaceConstructor` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMSetNearNullSpaceConstructor/> |
| `DMSetNullSpaceConstructor` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMSetNullSpaceConstructor/> |
| `DMSetNumFields` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetNumFields/> |
| `DMSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetOptionsPrefix/> |
| `DMSetPeriodicity` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetPeriodicity/> |
| `DMSetPointSF` | Collective | <https://petsc.org/release/manualpages/DM/DMSetPointSF/> |
| `DMSetRefineLevel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetRefineLevel/> |
| `DMSetRegionDS` | Collective | <https://petsc.org/release/manualpages/DM/DMSetRegionDS/> |
| `DMSetRegionNumDS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetRegionNumDS/> |
| `DMSetSnapToGeomModel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetSnapToGeomModel/> |
| `DMSetSparseLocalize` | Collective | <https://petsc.org/release/manualpages/DM/DMSetSparseLocalize/> |
| `DMSetStratumIS` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSetStratumIS/> |
| `DMSetType` | Collective | <https://petsc.org/release/manualpages/DM/DMSetType/> |
| `DMSetUp` | Collective | <https://petsc.org/release/manualpages/DM/DMSetUp/> |
| `DMSetUseNatural` | Collective | <https://petsc.org/release/manualpages/DM/DMSetUseNatural/> |
| `DMSetVariableBounds` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetVariableBounds/> |
| `DMSetVecType` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSetVecType/> |
| `DMShellCreate` | Collective | <https://petsc.org/release/manualpages/DM/DMShellCreate/> |
| `DMShellGetCoarsen` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellGetCoarsen/> |
| `DMShellGetContext` | Collective | <https://petsc.org/release/manualpages/DM/DMShellGetContext/> |
| `DMShellGetCreateInjection` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellGetCreateInjection/> |
| `DMShellGetCreateInterpolation` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellGetCreateInterpolation/> |
| `DMShellGetCreateRestriction` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellGetCreateRestriction/> |
| `DMShellGetCreateSubDM` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellGetCreateSubDM/> |
| `DMShellGetGlobalVector` | Not Collective | <https://petsc.org/release/manualpages/DM/DMShellGetGlobalVector/> |
| `DMShellGetRefine` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellGetRefine/> |
| `DMShellSetCoarsen` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCoarsen/> |
| `DMShellSetContext` | Collective | <https://petsc.org/release/manualpages/DM/DMShellSetContext/> |
| `DMShellSetCreateDomainDecomposition` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateDomainDecomposition/> |
| `DMShellSetCreateDomainDecompositionScatters` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateDomainDecompositionScatters/> |
| `DMShellSetCreateFieldDecomposition` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateFieldDecomposition/> |
| `DMShellSetCreateGlobalVector` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateGlobalVector/> |
| `DMShellSetCreateInjection` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateInjection/> |
| `DMShellSetCreateInterpolation` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateInterpolation/> |
| `DMShellSetCreateLocalVector` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateLocalVector/> |
| `DMShellSetCreateMatrix` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateMatrix/> |
| `DMShellSetCreateRestriction` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateRestriction/> |
| `DMShellSetCreateSubDM` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetCreateSubDM/> |
| `DMShellSetDestroyContext` | Collective | <https://petsc.org/release/manualpages/DM/DMShellSetDestroyContext/> |
| `DMShellSetGlobalToLocal` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetGlobalToLocal/> |
| `DMShellSetGlobalToLocalVecScatter` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetGlobalToLocalVecScatter/> |
| `DMShellSetGlobalVector` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetGlobalVector/> |
| `DMShellSetLocalToGlobal` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetLocalToGlobal/> |
| `DMShellSetLocalToGlobalVecScatter` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetLocalToGlobalVecScatter/> |
| `DMShellSetLocalToLocal` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetLocalToLocal/> |
| `DMShellSetLocalToLocalVecScatter` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetLocalToLocalVecScatter/> |
| `DMShellSetLocalVector` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetLocalVector/> |
| `DMShellSetMatrix` | Collective | <https://petsc.org/release/manualpages/DM/DMShellSetMatrix/> |
| `DMShellSetRefine` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMShellSetRefine/> |
| `DMSlicedCreate` | Collective | <https://petsc.org/release/manualpages/DM/DMSlicedCreate/> |
| `DMSlicedSetBlockFills` | Logically Collective | <https://petsc.org/release/manualpages/DM/DMSlicedSetBlockFills/> |
| `DMSlicedSetGhosts` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSlicedSetGhosts/> |
| `DMSlicedSetPreallocation` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSlicedSetPreallocation/> |
| `DMSnapToGeomModel` | Not Collective | <https://petsc.org/release/manualpages/DM/DMSnapToGeomModel/> |
| `DMSubDomainHookAdd` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMSubDomainHookAdd/> |
| `DMSubDomainHookRemove` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DM/DMSubDomainHookRemove/> |
| `DMSubDomainRestrict` | Collective if any hooks are | <https://petsc.org/release/manualpages/DM/DMSubDomainRestrict/> |
| `DMSwarmProjectFields` | Collective | <https://petsc.org/release/manualpages/DM/DMSwarmProjectFields/> |
| `DMSwarmProjectGradientFields` | Collective | <https://petsc.org/release/manualpages/DM/DMSwarmProjectGradientFields/> |
| `DMSwarmRemap` | Collective | <https://petsc.org/release/manualpages/DM/DMSwarmRemap/> |
| `DMView` | Collective | <https://petsc.org/release/manualpages/DM/DMView/> |
| `DMViewFromOptions` | Collective | <https://petsc.org/release/manualpages/DM/DMViewFromOptions/> |
| `MatGetDM` | Not Collective | <https://petsc.org/release/manualpages/DM/MatGetDM/> |
| `MatSetDM` | Not Collective | <https://petsc.org/release/manualpages/DM/MatSetDM/> |
| `PetscDSRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/PetscDSRegisterAll/> |
| `PetscDualSpaceRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/PetscDualSpaceRegisterAll/> |
| `PetscFERegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/PetscFERegisterAll/> |
| `PetscFVRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/PetscFVRegisterAll/> |
| `PetscLimiterRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/PetscLimiterRegisterAll/> |
| `PetscSpaceRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DM/PetscSpaceRegisterAll/> |
| `VecGetDM` | Not Collective | <https://petsc.org/release/manualpages/DM/VecGetDM/> |
| `VecSetDM` | Not Collective | <https://petsc.org/release/manualpages/DM/VecSetDM/> |

## DMComposite

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMCompositeAddDM` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeAddDM/> |
| `DMCompositeCreate` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeCreate/> |
| `DMCompositeGather` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGather/> |
| `DMCompositeGatherArray` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGatherArray/> |
| `DMCompositeGetAccess` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetAccess/> |
| `DMCompositeGetAccessArray` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetAccessArray/> |
| `DMCompositeGetEntries` | Not Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetEntries/> |
| `DMCompositeGetEntriesArray` | Not Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetEntriesArray/> |
| `DMCompositeGetGlobalISs` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetGlobalISs/> |
| `DMCompositeGetISLocalToGlobalMappings` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetISLocalToGlobalMappings/> |
| `DMCompositeGetLocalAccessArray` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetLocalAccessArray/> |
| `DMCompositeGetLocalISs` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetLocalISs/> |
| `DMCompositeGetLocalVectors` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetLocalVectors/> |
| `DMCompositeGetNumberDM` | Not Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeGetNumberDM/> |
| `DMCompositeRestoreAccess` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeRestoreAccess/> |
| `DMCompositeRestoreAccessArray` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeRestoreAccessArray/> |
| `DMCompositeRestoreLocalAccessArray` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeRestoreLocalAccessArray/> |
| `DMCompositeRestoreLocalVectors` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMComposite/DMCompositeRestoreLocalVectors/> |
| `DMCompositeScatter` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeScatter/> |
| `DMCompositeScatterArray` | Collective | <https://petsc.org/release/manualpages/DMComposite/DMCompositeScatterArray/> |
| `DMCompositeSetCoupling` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMComposite/DMCompositeSetCoupling/> |

## DMDA

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMDAConvertToCell` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAConvertToCell/> |
| `DMDACreate` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDACreate/> |
| `DMDACreate1d` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDACreate1d/> |
| `DMDACreate2d` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDACreate2d/> |
| `DMDACreate3d` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDACreate3d/> |
| `DMDACreateAggregates` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDACreateAggregates/> |
| `DMDACreateCompatibleDMDA` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDACreateCompatibleDMDA/> |
| `DMDACreateNaturalVector` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDACreateNaturalVector/> |
| `DMDACreatePatchIS` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDACreatePatchIS/> |
| `DMDACreatePF` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDACreatePF/> |
| `DMDAGetAO` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetAO/> |
| `DMDAGetBoundaryType` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetBoundaryType/> |
| `DMDAGetCoordinateArray` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDAGetCoordinateArray/> |
| `DMDAGetCoordinateName` | Not Collective; name will contain a common value; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDAGetCoordinateName/> |
| `DMDAGetCorners` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetCorners/> |
| `DMDAGetDepthStratum` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetDepthStratum/> |
| `DMDAGetDof` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetDof/> |
| `DMDAGetElements` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetElements/> |
| `DMDAGetElementsCorners` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetElementsCorners/> |
| `DMDAGetElementsSizes` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetElementsSizes/> |
| `DMDAGetElementType` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetElementType/> |
| `DMDAGetFieldName` | Not Collective; name will contain a common value | <https://petsc.org/release/manualpages/DMDA/DMDAGetFieldName/> |
| `DMDAGetFieldNames` | Not Collective; names will contain a common value; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDAGetFieldNames/> |
| `DMDAGetGhostCorners` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetGhostCorners/> |
| `DMDAGetHeightStratum` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetHeightStratum/> |
| `DMDAGetInfo` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetInfo/> |
| `DMDAGetInterpolationType` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetInterpolationType/> |
| `DMDAGetLocalInfo` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetLocalInfo/> |
| `DMDAGetLogicalCoordinate` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetLogicalCoordinate/> |
| `DMDAGetNeighbors` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetNeighbors/> |
| `DMDAGetNonOverlappingRegion` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetNonOverlappingRegion/> |
| `DMDAGetNumFaces` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetNumFaces/> |
| `DMDAGetNumLocalSubDomains` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetNumLocalSubDomains/> |
| `DMDAGetNumVertices` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetNumVertices/> |
| `DMDAGetOffset` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetOffset/> |
| `DMDAGetOverlap` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetOverlap/> |
| `DMDAGetOwnershipRanges` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetOwnershipRanges/> |
| `DMDAGetProcessorSubset` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDAGetProcessorSubset/> |
| `DMDAGetProcessorSubsets` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDAGetProcessorSubsets/> |
| `DMDAGetRay` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetRay/> |
| `DMDAGetRefinementFactor` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetRefinementFactor/> |
| `DMDAGetScatter` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetScatter/> |
| `DMDAGetStencilType` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetStencilType/> |
| `DMDAGetStencilWidth` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetStencilWidth/> |
| `DMDAGetSubdomainCornersIS` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGetSubdomainCornersIS/> |
| `DMDAGlobalToNaturalAllCreate` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGlobalToNaturalAllCreate/> |
| `DMDAGlobalToNaturalBegin` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGlobalToNaturalBegin/> |
| `DMDAGlobalToNaturalEnd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DMDA/DMDAGlobalToNaturalEnd/> |
| `DMDAMapMatStencilToGlobal` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAMapMatStencilToGlobal/> |
| `DMDANaturalAllToGlobalCreate` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDANaturalAllToGlobalCreate/> |
| `DMDANaturalToGlobalBegin` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DMDA/DMDANaturalToGlobalBegin/> |
| `DMDANaturalToGlobalEnd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/DMDA/DMDANaturalToGlobalEnd/> |
| `DMDARestoreCoordinateArray` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDARestoreCoordinateArray/> |
| `DMDARestoreElements` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDARestoreElements/> |
| `DMDARestoreSubdomainCornersIS` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDARestoreSubdomainCornersIS/> |
| `DMDASetAOType` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetAOType/> |
| `DMDASetBlockFills` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetBlockFills/> |
| `DMDASetBlockFillsSparse` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetBlockFillsSparse/> |
| `DMDASetBoundaryType` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetBoundaryType/> |
| `DMDASetCoordinateName` | Logically Collective; name must contain a common value; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDASetCoordinateName/> |
| `DMDASetDof` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetDof/> |
| `DMDASetElementType` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetElementType/> |
| `DMDASetFieldName` | Logically Collective; name must contain a common value | <https://petsc.org/release/manualpages/DMDA/DMDASetFieldName/> |
| `DMDASetFieldNames` | Logically Collective; names must contain a common value; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDASetFieldNames/> |
| `DMDASetGetMatrix` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMDA/DMDASetGetMatrix/> |
| `DMDASetGLLCoordinates` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetGLLCoordinates/> |
| `DMDASetInterpolationType` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetInterpolationType/> |
| `DMDASetNonOverlappingRegion` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetNonOverlappingRegion/> |
| `DMDASetNumLocalSubDomains` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetNumLocalSubDomains/> |
| `DMDASetNumProcs` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetNumProcs/> |
| `DMDASetOffset` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetOffset/> |
| `DMDASetOverlap` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetOverlap/> |
| `DMDASetOwnershipRanges` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetOwnershipRanges/> |
| `DMDASetRefinementFactor` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetRefinementFactor/> |
| `DMDASetSizes` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetSizes/> |
| `DMDASetStencilType` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetStencilType/> |
| `DMDASetStencilWidth` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetStencilWidth/> |
| `DMDASetUniformCoordinates` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetUniformCoordinates/> |
| `DMDASetVertexCoordinates` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDASetVertexCoordinates/> |
| `DMDAVecGetArray` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecGetArray/> |
| `DMDAVecGetArrayDOF` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayDOF/> |
| `DMDAVecGetArrayDOFRead` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayDOFRead/> |
| `DMDAVecGetArrayDOFWrite` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayDOFWrite/> |
| `DMDAVecGetArrayRead` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayRead/> |
| `DMDAVecGetArrayWrite` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayWrite/> |
| `DMDAVecRestoreArray` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArray/> |
| `DMDAVecRestoreArrayDOF` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayDOF/> |
| `DMDAVecRestoreArrayDOFRead` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayDOFRead/> |
| `DMDAVecRestoreArrayDOFWrite` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayDOFWrite/> |
| `DMDAVecRestoreArrayRead` | Not Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayRead/> |
| `DMDAVecRestoreArrayWrite` | Logically Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayWrite/> |
| `DMDAVTKWriteAll` | Collective | <https://petsc.org/release/manualpages/DMDA/DMDAVTKWriteAll/> |

## DMForest

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMForestGetAdaptivityForest` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetAdaptivityForest/> |
| `DMForestGetAdaptivityLabel` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetAdaptivityLabel/> |
| `DMForestGetAdaptivityPurpose` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetAdaptivityPurpose/> |
| `DMForestGetAdaptivitySF` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetAdaptivitySF/> |
| `DMForestGetAdaptivityStrategy` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetAdaptivityStrategy/> |
| `DMForestGetAdaptivitySuccess` | Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetAdaptivitySuccess/> |
| `DMForestGetAdjacencyCodimension` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetAdjacencyCodimension/> |
| `DMForestGetAdjacencyDimension` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetAdjacencyDimension/> |
| `DMForestGetBaseCoordinateMapping` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetBaseCoordinateMapping/> |
| `DMForestGetBaseDM` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetBaseDM/> |
| `DMForestGetCellChart` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetCellChart/> |
| `DMForestGetCellSF` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetCellSF/> |
| `DMForestGetCellWeightFactor` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetCellWeightFactor/> |
| `DMForestGetCellWeights` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetCellWeights/> |
| `DMForestGetComputeAdaptivitySF` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetComputeAdaptivitySF/> |
| `DMForestGetGradeFactor` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetGradeFactor/> |
| `DMForestGetInitialRefinement` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetInitialRefinement/> |
| `DMForestGetMaximumRefinement` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetMaximumRefinement/> |
| `DMForestGetMinimumRefinement` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetMinimumRefinement/> |
| `DMForestGetPartitionOverlap` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetPartitionOverlap/> |
| `DMForestGetTopology` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetTopology/> |
| `DMForestGetWeightCapacity` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestGetWeightCapacity/> |
| `DMForestRegisterType` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMForestRegisterType/> |
| `DMForestSetAdaptivityForest` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetAdaptivityForest/> |
| `DMForestSetAdaptivityLabel` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetAdaptivityLabel/> |
| `DMForestSetAdaptivityPurpose` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetAdaptivityPurpose/> |
| `DMForestSetAdaptivityStrategy` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetAdaptivityStrategy/> |
| `DMForestSetAdjacencyCodimension` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetAdjacencyCodimension/> |
| `DMForestSetAdjacencyDimension` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetAdjacencyDimension/> |
| `DMForestSetBaseCoordinateMapping` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetBaseCoordinateMapping/> |
| `DMForestSetBaseDM` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetBaseDM/> |
| `DMForestSetCellWeightFactor` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetCellWeightFactor/> |
| `DMForestSetCellWeights` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetCellWeights/> |
| `DMForestSetComputeAdaptivitySF` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetComputeAdaptivitySF/> |
| `DMForestSetGradeFactor` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetGradeFactor/> |
| `DMForestSetInitialRefinement` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetInitialRefinement/> |
| `DMForestSetMaximumRefinement` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetMaximumRefinement/> |
| `DMForestSetMinimumRefinement` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetMinimumRefinement/> |
| `DMForestSetPartitionOverlap` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetPartitionOverlap/> |
| `DMForestSetWeightCapacity` | Logically Collective | <https://petsc.org/release/manualpages/DMForest/DMForestSetWeightCapacity/> |
| `DMForestTemplate` | Collective | <https://petsc.org/release/manualpages/DMForest/DMForestTemplate/> |
| `DMForestTransferVec` | Collective | <https://petsc.org/release/manualpages/DMForest/DMForestTransferVec/> |
| `DMForestTransferVecFromBase` | Collective | <https://petsc.org/release/manualpages/DMForest/DMForestTransferVecFromBase/> |
| `DMIsForest` | Not Collective | <https://petsc.org/release/manualpages/DMForest/DMIsForest/> |

## DMLabel

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMLabelAddStrata` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelAddStrata/> |
| `DMLabelAddStrataIS` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelAddStrataIS/> |
| `DMLabelClearStratum` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelClearStratum/> |
| `DMLabelClearValue` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelClearValue/> |
| `DMLabelCompare` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMLabel/DMLabelCompare/> |
| `DMLabelComputeIndex` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelComputeIndex/> |
| `DMLabelConvertToSection` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelConvertToSection/> |
| `DMLabelCreate` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelCreate/> |
| `DMLabelCreateIndex` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelCreateIndex/> |
| `DMLabelDestroy` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelDestroy/> |
| `DMLabelDestroyIndex` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelDestroyIndex/> |
| `DMLabelDistribute` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelDistribute/> |
| `DMLabelDuplicate` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelDuplicate/> |
| `DMLabelEphemeralGetLabel` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelEphemeralGetLabel/> |
| `DMLabelEphemeralGetTransform` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelEphemeralGetTransform/> |
| `DMLabelEphemeralSetLabel` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelEphemeralSetLabel/> |
| `DMLabelEphemeralSetTransform` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelEphemeralSetTransform/> |
| `DMLabelFilter` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelFilter/> |
| `DMLabelGather` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGather/> |
| `DMLabelGetBounds` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetBounds/> |
| `DMLabelGetDefaultValue` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetDefaultValue/> |
| `DMLabelGetNonEmptyStratumValuesIS` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetNonEmptyStratumValuesIS/> |
| `DMLabelGetNumValues` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetNumValues/> |
| `DMLabelGetStratumBounds` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetStratumBounds/> |
| `DMLabelGetStratumIS` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetStratumIS/> |
| `DMLabelGetStratumPointIndex` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetStratumPointIndex/> |
| `DMLabelGetStratumSize` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetStratumSize/> |
| `DMLabelGetType` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetType/> |
| `DMLabelGetValue` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetValue/> |
| `DMLabelGetValueBounds` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetValueBounds/> |
| `DMLabelGetValueIndex` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetValueIndex/> |
| `DMLabelGetValueIS` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetValueIS/> |
| `DMLabelGetValueISGlobal` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelGetValueISGlobal/> |
| `DMLabelHasPoint` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelHasPoint/> |
| `DMLabelHasStratum` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelHasStratum/> |
| `DMLabelHasValue` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelHasValue/> |
| `DMLabelInsertIS` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelInsertIS/> |
| `DMLabelPermute` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelPermute/> |
| `DMLabelPermuteValues` | Not collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelPermuteValues/> |
| `DMLabelPropagateBegin` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelPropagateBegin/> |
| `DMLabelPropagateEnd` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelPropagateEnd/> |
| `DMLabelPropagatePush` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelPropagatePush/> |
| `DMLabelRegister` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelRegister/> |
| `DMLabelRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelRegisterAll/> |
| `DMLabelReset` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelReset/> |
| `DMLabelRewriteValues` | Not collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelRewriteValues/> |
| `DMLabelSetDefaultValue` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelSetDefaultValue/> |
| `DMLabelSetStratumBounds` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelSetStratumBounds/> |
| `DMLabelSetStratumIS` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelSetStratumIS/> |
| `DMLabelSetType` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelSetType/> |
| `DMLabelSetUp` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelSetUp/> |
| `DMLabelSetValue` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelSetValue/> |
| `DMLabelStratumHasPoint` | Not Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelStratumHasPoint/> |
| `DMLabelView` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelView/> |
| `DMLabelViewFromOptions` | Collective | <https://petsc.org/release/manualpages/DMLabel/DMLabelViewFromOptions/> |
| `PetscSectionCreateGlobalSectionLabel` | Collective | <https://petsc.org/release/manualpages/DMLabel/PetscSectionCreateGlobalSectionLabel/> |
| `PetscSectionSymCreateLabel` | Collective | <https://petsc.org/release/manualpages/DMLabel/PetscSectionSymCreateLabel/> |
| `PetscSectionSymLabelGetStratum` | Logically Collective | <https://petsc.org/release/manualpages/DMLabel/PetscSectionSymLabelGetStratum/> |

## DMMOAB

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMMoabCreate` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabCreate/> |
| `DMMoabCreateBoxMesh` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabCreateBoxMesh/> |
| `DMMoabCreateElement` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabCreateElement/> |
| `DMMoabCreateMoab` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabCreateMoab/> |
| `DMMoabCreateSubmesh` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabCreateSubmesh/> |
| `DMMoabCreateVector` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabCreateVector/> |
| `DMMoabCreateVertices` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabCreateVertices/> |
| `DMMoabGenerateHierarchy` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGenerateHierarchy/> |
| `DMMoabGetAllVertices` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetAllVertices/> |
| `DMMoabGetBlockSize` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetBlockSize/> |
| `DMMoabGetDimension` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetDimension/> |
| `DMMoabGetDofs` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetDofs/> |
| `DMMoabGetDofsBlocked` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetDofsBlocked/> |
| `DMMoabGetDofsBlockedLocal` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetDofsBlockedLocal/> |
| `DMMoabGetDofsLocal` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetDofsLocal/> |
| `DMMoabGetElementConnectivity` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetElementConnectivity/> |
| `DMMoabGetFieldDof` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetFieldDof/> |
| `DMMoabGetFieldDofs` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetFieldDofs/> |
| `DMMoabGetFieldDofsLocal` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetFieldDofsLocal/> |
| `DMMoabGetFieldName` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetFieldName/> |
| `DMMoabGetHierarchyLevel` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetHierarchyLevel/> |
| `DMMoabGetInterface` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetInterface/> |
| `DMMoabGetLocalElements` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetLocalElements/> |
| `DMMoabGetLocalSize` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetLocalSize/> |
| `DMMoabGetLocalToGlobalTag` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetLocalToGlobalTag/> |
| `DMMoabGetLocalVertices` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetLocalVertices/> |
| `DMMoabGetMaterialBlock` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetMaterialBlock/> |
| `DMMoabGetOffset` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetOffset/> |
| `DMMoabGetParallelComm` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetParallelComm/> |
| `DMMoabGetSize` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetSize/> |
| `DMMoabGetVertexConnectivity` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetVertexConnectivity/> |
| `DMMoabGetVertexCoordinates` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetVertexCoordinates/> |
| `DMMoabGetVertexDofsBlocked` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetVertexDofsBlocked/> |
| `DMMoabGetVertexDofsBlockedLocal` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabGetVertexDofsBlockedLocal/> |
| `DMMoabIsEntityOnBoundary` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabIsEntityOnBoundary/> |
| `DMMoabLoadFromFile` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabLoadFromFile/> |
| `DMMoabOutput` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabOutput/> |
| `DMMoabRenumberMeshEntities` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabRenumberMeshEntities/> |
| `DMMoabRestoreVertexConnectivity` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabRestoreVertexConnectivity/> |
| `DMMoabSetBlockFills` | Logically Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetBlockFills/> |
| `DMMoabSetBlockSize` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetBlockSize/> |
| `DMMoabSetFieldName` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetFieldName/> |
| `DMMoabSetFieldNames` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetFieldNames/> |
| `DMMoabSetFieldVector` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetFieldVector/> |
| `DMMoabSetGlobalFieldVector` | Not Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetGlobalFieldVector/> |
| `DMMoabSetInterface` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetInterface/> |
| `DMMoabSetLocalElements` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetLocalElements/> |
| `DMMoabSetLocalToGlobalTag` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetLocalToGlobalTag/> |
| `DMMoabSetLocalVertices` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabSetLocalVertices/> |
| `DMMoabVecGetArray` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabVecGetArray/> |
| `DMMoabVecGetArrayRead` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabVecGetArrayRead/> |
| `DMMoabVecRestoreArray` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabVecRestoreArray/> |
| `DMMoabVecRestoreArrayRead` | Collective | <https://petsc.org/release/manualpages/DMMOAB/DMMoabVecRestoreArrayRead/> |

## DMNetwork

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMNetworkAddComponent` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkAddComponent/> |
| `DMNetworkAddSharedVertices` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkAddSharedVertices/> |
| `DMNetworkAddSubnetwork` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkAddSubnetwork/> |
| `DMNetworkAssembleGraphStructures` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkAssembleGraphStructures/> |
| `DMNetworkCreate` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkCreate/> |
| `DMNetworkCreateIS` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkCreateIS/> |
| `DMNetworkCreateLocalIS` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkCreateLocalIS/> |
| `DMNetworkDistribute` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkDistribute/> |
| `DMNetworkEdgeSetMatrix` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkEdgeSetMatrix/> |
| `DMNetworkFinalizeComponents` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkFinalizeComponents/> |
| `DMNetworkGetComponent` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetComponent/> |
| `DMNetworkGetConnectedVertices` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetConnectedVertices/> |
| `DMNetworkGetEdgeOffset` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetEdgeOffset/> |
| `DMNetworkGetEdgeRange` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetEdgeRange/> |
| `DMNetworkGetGlobalEdgeIndex` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetGlobalEdgeIndex/> |
| `DMNetworkGetGlobalVecOffset` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetGlobalVecOffset/> |
| `DMNetworkGetGlobalVertexIndex` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetGlobalVertexIndex/> |
| `DMNetworkGetLocalVecOffset` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetLocalVecOffset/> |
| `DMNetworkGetNumComponents` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetNumComponents/> |
| `DMNetworkGetNumEdges` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetNumEdges/> |
| `DMNetworkGetNumSubNetworks` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetNumSubNetworks/> |
| `DMNetworkGetNumVertices` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetNumVertices/> |
| `DMNetworkGetPlex` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetPlex/> |
| `DMNetworkGetSharedVertices` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetSharedVertices/> |
| `DMNetworkGetSubnetwork` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetSubnetwork/> |
| `DMNetworkGetSupportingEdges` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetSupportingEdges/> |
| `DMNetworkGetVertexLocalToGlobalOrdering` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetVertexLocalToGlobalOrdering/> |
| `DMNetworkGetVertexOffset` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetVertexOffset/> |
| `DMNetworkGetVertexRange` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkGetVertexRange/> |
| `DMNetworkHasJacobian` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkHasJacobian/> |
| `DMNetworkIsGhostVertex` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkIsGhostVertex/> |
| `DMNetworkIsSharedVertex` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkIsSharedVertex/> |
| `DMNetworkLayoutSetUp` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkLayoutSetUp/> |
| `DMNetworkMonitorAdd` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkMonitorAdd/> |
| `DMNetworkMonitorCreate` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkMonitorCreate/> |
| `DMNetworkMonitorDestroy` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkMonitorDestroy/> |
| `DMNetworkMonitorPop` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkMonitorPop/> |
| `DMNetworkMonitorView` | Collective, No Fortran support | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkMonitorView/> |
| `DMNetworkRegisterComponent` | Logically Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkRegisterComponent/> |
| `DMNetworkSetNumSubNetworks` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkSetNumSubNetworks/> |
| `DMNetworkSetVertexLocalToGlobalOrdering` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkSetVertexLocalToGlobalOrdering/> |
| `DMNetworkSharedVertexGetInfo` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkSharedVertexGetInfo/> |
| `DMNetworkVertexSetMatrix` | Not Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkVertexSetMatrix/> |
| `DMNetworkViewSetShowGlobal` | Logically Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkViewSetShowGlobal/> |
| `DMNetworkViewSetShowNumbering` | Logically Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkViewSetShowNumbering/> |
| `DMNetworkViewSetShowRanks` | Logically Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkViewSetShowRanks/> |
| `DMNetworkViewSetShowVertices` | Logically Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkViewSetShowVertices/> |
| `DMNetworkViewSetViewRanks` | Collective | <https://petsc.org/release/manualpages/DMNetwork/DMNetworkViewSetViewRanks/> |
| `PetscSFGetSubSF` | Collective | <https://petsc.org/release/manualpages/DMNetwork/PetscSFGetSubSF/> |

## DMPatch

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMPatchCreate` | Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchCreate/> |
| `DMPatchCreateGrid` | Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchCreateGrid/> |
| `DMPatchGetCoarse` | Not Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchGetCoarse/> |
| `DMPatchGetCommSize` | Not Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchGetCommSize/> |
| `DMPatchGetPatchSize` | Not Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchGetPatchSize/> |
| `DMPatchSetCommSize` | Logically Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchSetCommSize/> |
| `DMPatchSetPatchSize` | Logically Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchSetPatchSize/> |
| `DMPatchSolve` | Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchSolve/> |
| `DMPatchZoom` | Collective | <https://petsc.org/release/manualpages/DMPatch/DMPatchZoom/> |

## DMPlex

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMPlex_Surface_Grad` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlex_Surface_Grad/> |
| `DMPlexBuildCoordinatesFromCellList` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexBuildCoordinatesFromCellList/> |
| `DMPlexBuildCoordinatesFromCellListParallel` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/DMPlexBuildCoordinatesFromCellListParallel/> |
| `DMPlexBuildFromCellList` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/DMPlexBuildFromCellList/> |
| `DMPlexBuildFromCellListParallel` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/DMPlexBuildFromCellListParallel/> |
| `DMPlexBuildFromCellSectionParallel` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/DMPlexBuildFromCellSectionParallel/> |
| `DMPlexCheckCellShape` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCheckCellShape/> |
| `DMPlexCheckFaces` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCheckFaces/> |
| `DMPlexCheckOrphanVertices` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCheckOrphanVertices/> |
| `DMPlexCheckPointSF` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCheckPointSF/> |
| `DMPlexComputeBdJacobianSingle` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeBdJacobianSingle/> |
| `DMPlexComputeBdJacobianSingleByLabel` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeBdJacobianSingleByLabel/> |
| `DMPlexComputeBdResidualSingle` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeBdResidualSingle/> |
| `DMPlexComputeBdResidualSingleByKey` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeBdResidualSingleByKey/> |
| `DMPlexComputeCellGeometryAffineFEM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeCellGeometryAffineFEM/> |
| `DMPlexComputeCellGeometryFEM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeCellGeometryFEM/> |
| `DMPlexComputeCellGeometryFVM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeCellGeometryFVM/> |
| `DMPlexComputeCellTypes` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeCellTypes/> |
| `DMPlexComputeClementInterpolant` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeClementInterpolant/> |
| `DMPlexComputeGradientClementInterpolant` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeGradientClementInterpolant/> |
| `DMPlexComputeGradientFVM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeGradientFVM/> |
| `DMPlexComputeInjectorReferenceTree` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeInjectorReferenceTree/> |
| `DMPlexComputeJacobianActionByKey` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeJacobianActionByKey/> |
| `DMPlexComputeJacobianByKey` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeJacobianByKey/> |
| `DMPlexComputeJacobianByKeyGeneral` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeJacobianByKeyGeneral/> |
| `DMPlexComputeJacobianHybridByKey` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeJacobianHybridByKey/> |
| `DMPlexComputeL2DiffLocal` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeL2DiffLocal/> |
| `DMPlexComputeL2DiffVec` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeL2DiffVec/> |
| `DMPlexComputeL2FluxDiffVec` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeL2FluxDiffVec/> |
| `DMPlexComputeL2FluxDiffVecLocal` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeL2FluxDiffVecLocal/> |
| `DMPlexComputeMassMatrixNested` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeMassMatrixNested/> |
| `DMPlexComputeOrthogonalQuality` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeOrthogonalQuality/> |
| `DMPlexComputeProjection2Dto1D` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeProjection2Dto1D/> |
| `DMPlexComputeProjection3Dto1D` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeProjection3Dto1D/> |
| `DMPlexComputeProjection3Dto2D` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeProjection3Dto2D/> |
| `DMPlexComputeResidualByKey` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeResidualByKey/> |
| `DMPlexComputeResidualHybridByKey` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexComputeResidualHybridByKey/> |
| `DMPlexConstructCohesiveCells` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexConstructCohesiveCells/> |
| `DMPlexConstructGhostCells` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexConstructGhostCells/> |
| `DMPlexCoordinatesLoad` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCoordinatesLoad/> |
| `DMPlexCoordinatesToReference` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCoordinatesToReference/> |
| `DMPlexCoordinatesView` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCoordinatesView/> |
| `DMPlexCopyCoordinates` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCopyCoordinates/> |
| `DMPlexCreate` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreate/> |
| `DMPlexCreateBallMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateBallMesh/> |
| `DMPlexCreateBoxMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateBoxMesh/> |
| `DMPlexCreateBoxSurfaceMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateBoxSurfaceMesh/> |
| `DMPlexCreateCGNS` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateCGNS/> |
| `DMPlexCreateCGNSFromFile` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateCGNSFromFile/> |
| `DMPlexCreateClosureIndex` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateClosureIndex/> |
| `DMPlexCreateCoarsePointIS` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateCoarsePointIS/> |
| `DMPlexCreateColoring` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateColoring/> |
| `DMPlexCreateCoordinateSpace` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateCoordinateSpace/> |
| `DMPlexCreateDefaultReferenceTree` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateDefaultReferenceTree/> |
| `DMPlexCreateDoublet` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateDoublet/> |
| `DMPlexCreateEdgeNumbering` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateEdgeNumbering/> |
| `DMPlexCreateExodus` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateExodus/> |
| `DMPlexCreateExodusFromFile` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateExodusFromFile/> |
| `DMPlexCreateFluent` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateFluent/> |
| `DMPlexCreateFluentFromFile` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateFluentFromFile/> |
| `DMPlexCreateFromCellListParallelPetsc` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateFromCellListParallelPetsc/> |
| `DMPlexCreateFromCellListPetsc` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateFromCellListPetsc/> |
| `DMPlexCreateFromCellSectionParallel` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateFromCellSectionParallel/> |
| `DMPlexCreateFromFile` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateFromFile/> |
| `DMPlexCreateGeomFromFile` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateGeomFromFile/> |
| `DMPlexCreateGmsh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateGmsh/> |
| `DMPlexCreateHexCylinderMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateHexCylinderMesh/> |
| `DMPlexCreateHybridMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateHybridMesh/> |
| `DMPlexCreateHypercubicMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateHypercubicMesh/> |
| `DMPlexCreateNaturalVector` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateNaturalVector/> |
| `DMPlexCreateNeighborCSR` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateNeighborCSR/> |
| `DMPlexCreateOverlapLabel` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateOverlapLabel/> |
| `DMPlexCreateOverlapLabelFromLabels` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateOverlapLabelFromLabels/> |
| `DMPlexCreateOverlapMigrationSF` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateOverlapMigrationSF/> |
| `DMPlexCreatePartitionerGraph` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreatePartitionerGraph/> |
| `DMPlexCreatePointNumbering` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreatePointNumbering/> |
| `DMPlexCreateProcessSF` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateProcessSF/> |
| `DMPlexCreateReferenceCell` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateReferenceCell/> |
| `DMPlexCreateRigidBodies` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateRigidBodies/> |
| `DMPlexCreateRigidBody` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateRigidBody/> |
| `DMPlexCreateSection` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateSection/> |
| `DMPlexCreateSphereMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateSphereMesh/> |
| `DMPlexCreateTPSMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateTPSMesh/> |
| `DMPlexCreateTwoSidedProcessSF` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateTwoSidedProcessSF/> |
| `DMPlexCreateWedgeBoxMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateWedgeBoxMesh/> |
| `DMPlexCreateWedgeCylinderMesh` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexCreateWedgeCylinderMesh/> |
| `DMPlexDistribute` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexDistribute/> |
| `DMPlexDistributeData` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexDistributeData/> |
| `DMPlexDistributeField` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexDistributeField/> |
| `DMPlexDistributeFieldIS` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexDistributeFieldIS/> |
| `DMPlexDistributeGetDefault` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexDistributeGetDefault/> |
| `DMPlexDistributeOverlap` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexDistributeOverlap/> |
| `DMPlexDistributeOwnership` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexDistributeOwnership/> |
| `DMPlexDistributeSetDefault` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexDistributeSetDefault/> |
| `DMPlexEqual` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexEqual/> |
| `DMPlexFindVertices` | Not Collective (provided DMGetCoordinatesLocalSetUp () has been already called) | <https://petsc.org/release/manualpages/DMPlex/DMPlexFindVertices/> |
| `DMPlexFreeGeomObject` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexFreeGeomObject/> |
| `DMPlexGenerate` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGenerate/> |
| `DMPlexGeomDataAndGrads` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGeomDataAndGrads/> |
| `DMPlexGetActivePoint` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetActivePoint/> |
| `DMPlexGetAnchors` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetAnchors/> |
| `DMPlexGetCellCoordinates` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetCellCoordinates/> |
| `DMPlexGetCellType` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetCellType/> |
| `DMPlexGetCellTypeLabel` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetCellTypeLabel/> |
| `DMPlexGetChart` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetChart/> |
| `DMPlexGetClosureIndices` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetClosureIndices/> |
| `DMPlexGetCompressedClosure` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetCompressedClosure/> |
| `DMPlexGetCone` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetCone/> |
| `DMPlexGetConeOrientation` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetConeOrientation/> |
| `DMPlexGetConeOrientations` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetConeOrientations/> |
| `DMPlexGetConeRecursive` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetConeRecursive/> |
| `DMPlexGetConeRecursiveVertices` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetConeRecursiveVertices/> |
| `DMPlexGetCones` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetCones/> |
| `DMPlexGetConeSection` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetConeSection/> |
| `DMPlexGetConeSize` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetConeSize/> |
| `DMPlexGetConeTuple` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetConeTuple/> |
| `DMPlexGetCoordinateMap` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetCoordinateMap/> |
| `DMPlexGetDataFVM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetDataFVM/> |
| `DMPlexGetDepth` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetDepth/> |
| `DMPlexGetDepthLabel` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetDepthLabel/> |
| `DMPlexGetDepthStratum` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetDepthStratum/> |
| `DMPlexGetFullJoin` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetFullJoin/> |
| `DMPlexGetFullMeet` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetFullMeet/> |
| `DMPlexGetGatherDM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGatherDM/> |
| `DMPlexGetGeomBodyMassProperties` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomBodyMassProperties/> |
| `DMPlexGetGeomCntrlPntAndWeightData` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomCntrlPntAndWeightData/> |
| `DMPlexGetGeomCntrlPntMaps` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomCntrlPntMaps/> |
| `DMPlexGetGeometryFVM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeometryFVM/> |
| `DMPlexGetGeomFaceNumOfControlPoints` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomFaceNumOfControlPoints/> |
| `DMPlexGetGeomGradData` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomGradData/> |
| `DMPlexGetGeomID` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomID/> |
| `DMPlexGetGeomModelBodies` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelBodies/> |
| `DMPlexGetGeomModelBodyEdges` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelBodyEdges/> |
| `DMPlexGetGeomModelBodyFaces` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelBodyFaces/> |
| `DMPlexGetGeomModelBodyLoops` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelBodyLoops/> |
| `DMPlexGetGeomModelBodyNodes` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelBodyNodes/> |
| `DMPlexGetGeomModelBodyShells` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelBodyShells/> |
| `DMPlexGetGeomModelEdgeNodes` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelEdgeNodes/> |
| `DMPlexGetGeomModelFaceEdges` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelFaceEdges/> |
| `DMPlexGetGeomModelFaceLoops` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelFaceLoops/> |
| `DMPlexGetGeomModelShellFaces` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelShellFaces/> |
| `DMPlexGetGeomModelTUV` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomModelTUV/> |
| `DMPlexGetGeomObject` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGeomObject/> |
| `DMPlexGetGradientDM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetGradientDM/> |
| `DMPlexGetHeightStratum` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetHeightStratum/> |
| `DMPlexGetInterpolatePreferTensor` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetInterpolatePreferTensor/> |
| `DMPlexGetIsoperiodicFaceSF` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetIsoperiodicFaceSF/> |
| `DMPlexGetJoin` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetJoin/> |
| `DMPlexGetLocalOffsets` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetLocalOffsets/> |
| `DMPlexGetLocalOffsetsSupport` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetLocalOffsetsSupport/> |
| `DMPlexGetMaxSizes` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetMaxSizes/> |
| `DMPlexGetMeet` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetMeet/> |
| `DMPlexGetMigrationSF` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetMigrationSF/> |
| `DMPlexGetMinRadius` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetMinRadius/> |
| `DMPlexGetNumFaceVertices` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetNumFaceVertices/> |
| `DMPlexGetOrdering` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetOrdering/> |
| `DMPlexGetOrdering1D` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetOrdering1D/> |
| `DMPlexGetOrientedCone` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetOrientedCone/> |
| `DMPlexGetOrientedFace` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetOrientedFace/> |
| `DMPlexGetOverlap` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetOverlap/> |
| `DMPlexGetPartitioner` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetPartitioner/> |
| `DMPlexGetPointDepth` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetPointDepth/> |
| `DMPlexGetPointGlobal` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetPointGlobal/> |
| `DMPlexGetPointGlobalField` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetPointGlobalField/> |
| `DMPlexGetPointHeight` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetPointHeight/> |
| `DMPlexGetPointLocal` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetPointLocal/> |
| `DMPlexGetPointLocalField` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetPointLocalField/> |
| `DMPlexGetRedundantDM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetRedundantDM/> |
| `DMPlexGetReferenceTree` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetReferenceTree/> |
| `DMPlexGetSaveTransform` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetSaveTransform/> |
| `DMPlexGetScale` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetScale/> |
| `DMPlexGetSubdomainSection` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetSubdomainSection/> |
| `DMPlexGetSupport` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetSupport/> |
| `DMPlexGetSupportSection` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetSupportSection/> |
| `DMPlexGetSupportSize` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetSupportSize/> |
| `DMPlexGetTransform` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetTransform/> |
| `DMPlexGetTransitiveClosure` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetTransitiveClosure/> |
| `DMPlexGetUseCeed` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetUseCeed/> |
| `DMPlexGetUseMatClosurePermutation` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGetUseMatClosurePermutation/> |
| `DMPlexGlobalToNaturalBegin` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGlobalToNaturalBegin/> |
| `DMPlexGlobalToNaturalEnd` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGlobalToNaturalEnd/> |
| `DMPlexGlobalVectorLoad` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGlobalVectorLoad/> |
| `DMPlexGlobalVectorView` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexGlobalVectorView/> |
| `DMPlexInflateToGeomModel` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInflateToGeomModel/> |
| `DMPlexInflateToGeomModelUseTUV` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInflateToGeomModelUseTUV/> |
| `DMPlexInflateToGeomModelUseXYZ` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInflateToGeomModelUseXYZ/> |
| `DMPlexInsertBoundaryValues` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInsertBoundaryValues/> |
| `DMPlexInsertBoundaryValuesEssentialBdField` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInsertBoundaryValuesEssentialBdField/> |
| `DMPlexInsertBoundaryValuesFVM` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInsertBoundaryValuesFVM/> |
| `DMPlexInsertBounds` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInsertBounds/> |
| `DMPlexInsertCone` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInsertCone/> |
| `DMPlexInsertConeOrientation` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInsertConeOrientation/> |
| `DMPlexInsertSupport` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInsertSupport/> |
| `DMPlexInterpolate` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInterpolate/> |
| `DMPlexInterpolatedFlag` | collective property depending on whether it is returned by DMPlexIsInterpolated () or DMPlexIsInterpolatedCollective () . | <https://petsc.org/release/manualpages/DMPlex/DMPlexInterpolatedFlag/> |
| `DMPlexInterpolatePointSF` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexInterpolatePointSF/> |
| `DMPlexIsDistributed` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexIsDistributed/> |
| `DMPlexIsInterpolated` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexIsInterpolated/> |
| `DMPlexIsInterpolatedCollective` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexIsInterpolatedCollective/> |
| `DMPlexLabelsLoad` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexLabelsLoad/> |
| `DMPlexLabelsView` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexLabelsView/> |
| `DMPlexLocalVectorLoad` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexLocalVectorLoad/> |
| `DMPlexLocalVectorView` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexLocalVectorView/> |
| `DMPlexMarkBoundaryFaces` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexMarkBoundaryFaces/> |
| `DMPlexMatGetClosureIndicesRefined` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexMatGetClosureIndicesRefined/> |
| `DMPlexMatSetClosure` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexMatSetClosure/> |
| `DMPlexMatSetClosureGeneral` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexMatSetClosureGeneral/> |
| `DMPlexMatSetClosureRefined` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexMatSetClosureRefined/> |
| `DMPlexMetricSetFromOptions` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexMetricSetFromOptions/> |
| `DMPlexMigrate` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexMigrate/> |
| `DMPlexModifyGeomModel` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexModifyGeomModel/> |
| `DMPlexNaturalToGlobalBegin` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexNaturalToGlobalBegin/> |
| `DMPlexNaturalToGlobalEnd` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexNaturalToGlobalEnd/> |
| `DMPlexOrientLabel` | Collective on dm | <https://petsc.org/release/manualpages/DMPlex/DMPlexOrientLabel/> |
| `DMPlexOrientPoint` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexOrientPoint/> |
| `DMPlexPermute` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPermute/> |
| `DMPlexPointGlobalFieldRead` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointGlobalFieldRead/> |
| `DMPlexPointGlobalFieldRef` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointGlobalFieldRef/> |
| `DMPlexPointGlobalRead` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointGlobalRead/> |
| `DMPlexPointGlobalRef` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointGlobalRef/> |
| `DMPlexPointLocalFieldRead` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointLocalFieldRead/> |
| `DMPlexPointLocalFieldRef` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointLocalFieldRef/> |
| `DMPlexPointLocalRead` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointLocalRead/> |
| `DMPlexPointLocalRef` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointLocalRef/> |
| `DMPlexPointQueueBack` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointQueueBack/> |
| `DMPlexPointQueueCreate` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointQueueCreate/> |
| `DMPlexPointQueueDequeue` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointQueueDequeue/> |
| `DMPlexPointQueueDestroy` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointQueueDestroy/> |
| `DMPlexPointQueueEmptyCollective` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointQueueEmptyCollective/> |
| `DMPlexPointQueueEnqueue` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointQueueEnqueue/> |
| `DMPlexPointQueueEnsureSize` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointQueueEnsureSize/> |
| `DMPlexPointQueueFront` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPointQueueFront/> |
| `DMPlexPreallocateOperator` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexPreallocateOperator/> |
| `DMPlexReferenceToCoordinates` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexReferenceToCoordinates/> |
| `DMPlexRefineToSimplexGetReflect` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRefineToSimplexGetReflect/> |
| `DMPlexRefineToSimplexSetReflect` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRefineToSimplexSetReflect/> |
| `DMPlexRemapGeometry` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRemapGeometry/> |
| `DMPlexRemapMigrationSF` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRemapMigrationSF/> |
| `DMPlexReorderCohesiveSupports` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexReorderCohesiveSupports/> |
| `DMPlexReorderGetDefault` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexReorderGetDefault/> |
| `DMPlexReorderSetDefault` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexReorderSetDefault/> |
| `DMPlexRestoreCellCoordinates` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreCellCoordinates/> |
| `DMPlexRestoreClosureIndices` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreClosureIndices/> |
| `DMPlexRestoreCompressedClosure` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreCompressedClosure/> |
| `DMPlexRestoreConeRecursive` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreConeRecursive/> |
| `DMPlexRestoreGeomBodyMassProperties` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreGeomBodyMassProperties/> |
| `DMPlexRestoreGeomCntrlPntAndWeightData` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreGeomCntrlPntAndWeightData/> |
| `DMPlexRestoreGeomGradData` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreGeomGradData/> |
| `DMPlexRestoreJoin` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreJoin/> |
| `DMPlexRestoreMeet` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreMeet/> |
| `DMPlexRestoreOrientedCone` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreOrientedCone/> |
| `DMPlexRestoreTransitiveClosure` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexRestoreTransitiveClosure/> |
| `DMPlexSectionLoad` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSectionLoad/> |
| `DMPlexSectionView` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSectionView/> |
| `DMPlexSetActivePoint` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetActivePoint/> |
| `DMPlexSetAnchors` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetAnchors/> |
| `DMPlexSetCellType` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetCellType/> |
| `DMPlexSetChart` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetChart/> |
| `DMPlexSetCone` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetCone/> |
| `DMPlexSetConeOrientation` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetConeOrientation/> |
| `DMPlexSetConeSize` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetConeSize/> |
| `DMPlexSetCoordinateMap` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetCoordinateMap/> |
| `DMPlexSetInterpolatePreferTensor` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetInterpolatePreferTensor/> |
| `DMPlexSetIsoperiodicFaceSF` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetIsoperiodicFaceSF/> |
| `DMPlexSetIsoperiodicFaceTransform` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetIsoperiodicFaceTransform/> |
| `DMPlexSetMigrationSF` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetMigrationSF/> |
| `DMPlexSetMinRadius` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetMinRadius/> |
| `DMPlexSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetOptionsPrefix/> |
| `DMPlexSetOverlap` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetOverlap/> |
| `DMPlexSetPartitioner` | logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetPartitioner/> |
| `DMPlexSetReferenceTree` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetReferenceTree/> |
| `DMPlexSetSaveTransform` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetSaveTransform/> |
| `DMPlexSetScale` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetScale/> |
| `DMPlexSetSupport` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetSupport/> |
| `DMPlexSetSupportSize` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetSupportSize/> |
| `DMPlexSetTransform` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetTransform/> |
| `DMPlexSetTree` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetTree/> |
| `DMPlexSetUseCeed` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetUseCeed/> |
| `DMPlexSetUseMatClosurePermutation` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSetUseMatClosurePermutation/> |
| `DMPlexShearGeometry` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexShearGeometry/> |
| `DMPlexStratify` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexStratify/> |
| `DMPlexSymmetrize` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexSymmetrize/> |
| `DMPlexTetgenSetOptions` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTetgenSetOptions/> |
| `DMPlexTopologyLoad` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTopologyLoad/> |
| `DMPlexTopologyView` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTopologyView/> |
| `DMPlexTransferVecTree` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransferVecTree/> |
| `DMPlexTransformAdaptLabel` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformAdaptLabel/> |
| `DMPlexTransformApply` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformApply/> |
| `DMPlexTransformCellTransformIdentity` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformCellTransformIdentity/> |
| `DMPlexTransformCohesiveExtrudeGetTensor` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformCohesiveExtrudeGetTensor/> |
| `DMPlexTransformCohesiveExtrudeGetUnsplit` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformCohesiveExtrudeGetUnsplit/> |
| `DMPlexTransformCohesiveExtrudeGetWidth` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformCohesiveExtrudeGetWidth/> |
| `DMPlexTransformCohesiveExtrudeSetTensor` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformCohesiveExtrudeSetTensor/> |
| `DMPlexTransformCohesiveExtrudeSetWidth` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformCohesiveExtrudeSetWidth/> |
| `DMPlexTransformCreate` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformCreate/> |
| `DMPlexTransformCreateDiscLabels` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformCreateDiscLabels/> |
| `DMPlexTransformDestroy` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformDestroy/> |
| `DMPlexTransformExtrudeGetLayers` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeGetLayers/> |
| `DMPlexTransformExtrudeGetNormal` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeGetNormal/> |
| `DMPlexTransformExtrudeGetPeriodic` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeGetPeriodic/> |
| `DMPlexTransformExtrudeGetSymmetric` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeGetSymmetric/> |
| `DMPlexTransformExtrudeGetTensor` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeGetTensor/> |
| `DMPlexTransformExtrudeGetThickness` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeGetThickness/> |
| `DMPlexTransformExtrudeSetLayers` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeSetLayers/> |
| `DMPlexTransformExtrudeSetNormal` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeSetNormal/> |
| `DMPlexTransformExtrudeSetNormalFunction` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeSetNormalFunction/> |
| `DMPlexTransformExtrudeSetPeriodic` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeSetPeriodic/> |
| `DMPlexTransformExtrudeSetSymmetric` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeSetSymmetric/> |
| `DMPlexTransformExtrudeSetTensor` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeSetTensor/> |
| `DMPlexTransformExtrudeSetThickness` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeSetThickness/> |
| `DMPlexTransformExtrudeSetThicknesses` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformExtrudeSetThicknesses/> |
| `DMPlexTransformGetCellType` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetCellType/> |
| `DMPlexTransformGetCellTypeStratum` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetCellTypeStratum/> |
| `DMPlexTransformGetChart` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetChart/> |
| `DMPlexTransformGetCone` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetCone/> |
| `DMPlexTransformGetConeOriented` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetConeOriented/> |
| `DMPlexTransformGetConeSize` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetConeSize/> |
| `DMPlexTransformGetDepth` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetDepth/> |
| `DMPlexTransformGetDepthStratum` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetDepthStratum/> |
| `DMPlexTransformGetMatchStrata` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetMatchStrata/> |
| `DMPlexTransformGetSourcePoint` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetSourcePoint/> |
| `DMPlexTransformGetSubcellOrientation` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetSubcellOrientation/> |
| `DMPlexTransformGetSubcellOrientationIdentity` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetSubcellOrientationIdentity/> |
| `DMPlexTransformGetTargetPoint` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetTargetPoint/> |
| `DMPlexTransformGetType` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformGetType/> |
| `DMPlexTransformMapCoordinates` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformMapCoordinates/> |
| `DMPlexTransformRegister` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformRegister/> |
| `DMPlexTransformRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformRegisterAll/> |
| `DMPlexTransformRegisterDestroy` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformRegisterDestroy/> |
| `DMPlexTransformRestoreCone` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformRestoreCone/> |
| `DMPlexTransformSetFromOptions` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformSetFromOptions/> |
| `DMPlexTransformSetMatchStrata` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformSetMatchStrata/> |
| `DMPlexTransformSetType` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformSetType/> |
| `DMPlexTransformView` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTransformView/> |
| `DMPlexTreeRefineCell` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTreeRefineCell/> |
| `DMPlexTriangleSetOptions` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexTriangleSetOptions/> |
| `DMPlexUninterpolate` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexUninterpolate/> |
| `DMPlexVecGetClosure` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexVecGetClosure/> |
| `DMPlexVecGetClosureAtDepth` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexVecGetClosureAtDepth/> |
| `DMPlexVecGetOrientedClosure` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexVecGetOrientedClosure/> |
| `DMPlexVecRestoreClosure` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexVecRestoreClosure/> |
| `DMPlexVecSetClosure` | Not collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexVecSetClosure/> |
| `DMPlexVecView1D` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexVecView1D/> |
| `DMPlexVTKWriteAll` | Collective | <https://petsc.org/release/manualpages/DMPlex/DMPlexVTKWriteAll/> |
| `PETSC_VIEWER_EXODUSII_` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/PETSC_VIEWER_EXODUSII_/> |
| `PetscCallEGADS` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/PetscCallEGADS/> |
| `PetscGridHashCreate` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscGridHashCreate/> |
| `PetscGridHashDestroy` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscGridHashDestroy/> |
| `PetscGridHashEnlarge` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/PetscGridHashEnlarge/> |
| `PetscGridHashGetEnclosingBox` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/PetscGridHashGetEnclosingBox/> |
| `PetscGridHashSetGrid` | Not Collective | <https://petsc.org/release/manualpages/DMPlex/PetscGridHashSetGrid/> |
| `PetscPartitionerDMPlexPartition` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscPartitionerDMPlexPartition/> |
| `PetscViewerExodusIIGetId` | Logically Collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetId/> |
| `PetscViewerExodusIIGetNodalVariable` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetNodalVariable/> |
| `PetscViewerExodusIIGetNodalVariableIndex` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetNodalVariableIndex/> |
| `PetscViewerExodusIIGetNodalVariableName` | Collective; | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetNodalVariableName/> |
| `PetscViewerExodusIIGetNodalVariableNames` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetNodalVariableNames/> |
| `PetscViewerExodusIIGetOrder` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetOrder/> |
| `PetscViewerExodusIIGetZonalVariable` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetZonalVariable/> |
| `PetscViewerExodusIIGetZonalVariableIndex` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetZonalVariableIndex/> |
| `PetscViewerExodusIIGetZonalVariableName` | Collective; | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetZonalVariableName/> |
| `PetscViewerExodusIIGetZonalVariableNames` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIGetZonalVariableNames/> |
| `PetscViewerExodusIIOpen` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIIOpen/> |
| `PetscViewerExodusIISetNodalVariable` | Collective; | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIISetNodalVariable/> |
| `PetscViewerExodusIISetNodalVariableName` | Collective; | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIISetNodalVariableName/> |
| `PetscViewerExodusIISetNodalVariableNames` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIISetNodalVariableNames/> |
| `PetscViewerExodusIISetOrder` | Collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIISetOrder/> |
| `PetscViewerExodusIISetZonalVariable` | Collective; | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIISetZonalVariable/> |
| `PetscViewerExodusIISetZonalVariableName` | Collective; | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIISetZonalVariableName/> |
| `PetscViewerExodusIISetZonalVariableNames` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DMPlex/PetscViewerExodusIISetZonalVariableNames/> |
| `PetscViewerHDF5GetDMPlexStorageVersionReading` | Logically collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerHDF5GetDMPlexStorageVersionReading/> |
| `PetscViewerHDF5GetDMPlexStorageVersionWriting` | Logically collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerHDF5GetDMPlexStorageVersionWriting/> |
| `PetscViewerHDF5SetDMPlexStorageVersionReading` | Logically collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerHDF5SetDMPlexStorageVersionReading/> |
| `PetscViewerHDF5SetDMPlexStorageVersionWriting` | Logically collective | <https://petsc.org/release/manualpages/DMPlex/PetscViewerHDF5SetDMPlexStorageVersionWriting/> |

## DMPRODUCT

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMProductGetDimensionIndex` | Not Collective | <https://petsc.org/release/manualpages/DMPRODUCT/DMProductGetDimensionIndex/> |
| `DMProductGetDM` | Not Collective | <https://petsc.org/release/manualpages/DMPRODUCT/DMProductGetDM/> |
| `DMProductSetDimensionIndex` | Not Collective | <https://petsc.org/release/manualpages/DMPRODUCT/DMProductSetDimensionIndex/> |
| `DMProductSetDM` | Not Collective | <https://petsc.org/release/manualpages/DMPRODUCT/DMProductSetDM/> |

## DMStag

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMStagCreate1d` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagCreate1d/> |
| `DMStagCreate2d` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagCreate2d/> |
| `DMStagCreate3d` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagCreate3d/> |
| `DMStagCreateCompatibleDMStag` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagCreateCompatibleDMStag/> |
| `DMStagCreateISFromStencils` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagCreateISFromStencils/> |
| `DMStagGetBoundaryTypes` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetBoundaryTypes/> |
| `DMStagGetCorners` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetCorners/> |
| `DMStagGetDOF` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetDOF/> |
| `DMStagGetEntries` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetEntries/> |
| `DMStagGetEntriesLocal` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetEntriesLocal/> |
| `DMStagGetEntriesPerElement` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetEntriesPerElement/> |
| `DMStagGetGhostCorners` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetGhostCorners/> |
| `DMStagGetGlobalSizes` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetGlobalSizes/> |
| `DMStagGetIsFirstRank` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetIsFirstRank/> |
| `DMStagGetIsLastRank` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetIsLastRank/> |
| `DMStagGetLocalSizes` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetLocalSizes/> |
| `DMStagGetLocationDOF` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetLocationDOF/> |
| `DMStagGetLocationSlot` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetLocationSlot/> |
| `DMStagGetNumRanks` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetNumRanks/> |
| `DMStagGetOwnershipRanges` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetOwnershipRanges/> |
| `DMStagGetProductCoordinateArrays` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetProductCoordinateArrays/> |
| `DMStagGetProductCoordinateArraysRead` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetProductCoordinateArraysRead/> |
| `DMStagGetProductCoordinateLocationSlot` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetProductCoordinateLocationSlot/> |
| `DMStagGetRefinementFactor` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetRefinementFactor/> |
| `DMStagGetStencilType` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetStencilType/> |
| `DMStagGetStencilWidth` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagGetStencilWidth/> |
| `DMStagMatGetValuesStencil` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagMatGetValuesStencil/> |
| `DMStagMatSetValuesStencil` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagMatSetValuesStencil/> |
| `DMStagMigrateVec` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagMigrateVec/> |
| `DMStagPopulateLocalToGlobalInjective` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagPopulateLocalToGlobalInjective/> |
| `DMStagRestoreProductCoordinateArrays` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagRestoreProductCoordinateArrays/> |
| `DMStagRestoreProductCoordinateArraysRead` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagRestoreProductCoordinateArraysRead/> |
| `DMStagSetBoundaryTypes` | Logically Collective; boundaryType0, boundaryType1, and boundaryType2 must contain common values | <https://petsc.org/release/manualpages/DMStag/DMStagSetBoundaryTypes/> |
| `DMStagSetCoordinateDMType` | Logically Collective; dmtype must contain common value | <https://petsc.org/release/manualpages/DMStag/DMStagSetCoordinateDMType/> |
| `DMStagSetDOF` | Logically Collective; dof0 , dof1 , dof2 , and dof3 must contain common values | <https://petsc.org/release/manualpages/DMStag/DMStagSetDOF/> |
| `DMStagSetGlobalSizes` | Logically Collective; N0 , N1 , and N2 must contain common values | <https://petsc.org/release/manualpages/DMStag/DMStagSetGlobalSizes/> |
| `DMStagSetNumRanks` | Logically Collective; nRanks0 , nRanks1 , and nRanks2 must contain common values | <https://petsc.org/release/manualpages/DMStag/DMStagSetNumRanks/> |
| `DMStagSetOwnershipRanges` | Logically Collective; lx , ly , and lz must contain common values | <https://petsc.org/release/manualpages/DMStag/DMStagSetOwnershipRanges/> |
| `DMStagSetRefinementFactor` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagSetRefinementFactor/> |
| `DMStagSetStencilType` | Logically Collective; stencilType must contain common value | <https://petsc.org/release/manualpages/DMStag/DMStagSetStencilType/> |
| `DMStagSetStencilWidth` | Logically Collective; stencilWidth must contain common value | <https://petsc.org/release/manualpages/DMStag/DMStagSetStencilWidth/> |
| `DMStagSetUniformCoordinates` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagSetUniformCoordinates/> |
| `DMStagSetUniformCoordinatesExplicit` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagSetUniformCoordinatesExplicit/> |
| `DMStagSetUniformCoordinatesProduct` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagSetUniformCoordinatesProduct/> |
| `DMStagStencilToIndexLocal` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagStencilToIndexLocal/> |
| `DMStagVecGetArray` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagVecGetArray/> |
| `DMStagVecGetArrayRead` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagVecGetArrayRead/> |
| `DMStagVecGetValuesStencil` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagVecGetValuesStencil/> |
| `DMStagVecRestoreArray` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagVecRestoreArray/> |
| `DMStagVecRestoreArrayRead` | Logically Collective | <https://petsc.org/release/manualpages/DMStag/DMStagVecRestoreArrayRead/> |
| `DMStagVecSetValuesStencil` | Not Collective | <https://petsc.org/release/manualpages/DMStag/DMStagVecSetValuesStencil/> |
| `DMStagVecSplitToDMDA` | Collective | <https://petsc.org/release/manualpages/DMStag/DMStagVecSplitToDMDA/> |

## DMSwarm

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMSwarmAddCellDM` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmAddCellDM/> |
| `DMSwarmAddNPoints` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmAddNPoints/> |
| `DMSwarmAddPoint` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmAddPoint/> |
| `DMSwarmCellDMCreate` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMCreate/> |
| `DMSwarmCellDMDestroy` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMDestroy/> |
| `DMSwarmCellDMGetBlockSize` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMGetBlockSize/> |
| `DMSwarmCellDMGetCellID` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMGetCellID/> |
| `DMSwarmCellDMGetCoordinateFields` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMGetCoordinateFields/> |
| `DMSwarmCellDMGetDM` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMGetDM/> |
| `DMSwarmCellDMGetFields` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMGetFields/> |
| `DMSwarmCellDMGetSort` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMGetSort/> |
| `DMSwarmCellDMSetSort` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMSetSort/> |
| `DMSwarmCellDMView` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCellDMView/> |
| `DMSwarmCollectViewCreate` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCollectViewCreate/> |
| `DMSwarmCollectViewDestroy` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCollectViewDestroy/> |
| `DMSwarmComputeLocalSize` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmComputeLocalSize/> |
| `DMSwarmComputeLocalSizeFromOptions` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmComputeLocalSizeFromOptions/> |
| `DMSwarmCopyPoint` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCopyPoint/> |
| `DMSwarmCreateGlobalVectorFromField` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCreateGlobalVectorFromField/> |
| `DMSwarmCreateGlobalVectorFromFields` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCreateGlobalVectorFromFields/> |
| `DMSwarmCreateLocalVectorFromField` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCreateLocalVectorFromField/> |
| `DMSwarmCreateLocalVectorFromFields` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCreateLocalVectorFromFields/> |
| `DMSwarmCreateMassMatrixSquare` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCreateMassMatrixSquare/> |
| `DMSwarmCreatePointPerCellCount` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmCreatePointPerCellCount/> |
| `DMSwarmDataBucketGetDMSwarmDataFieldByName` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDataBucketGetDMSwarmDataFieldByName/> |
| `DMSwarmDataBucketGetDMSwarmDataFieldIdByName` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDataBucketGetDMSwarmDataFieldIdByName/> |
| `DMSwarmDataBucketQueryDMSwarmDataFieldByName` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDataBucketQueryDMSwarmDataFieldByName/> |
| `DMSwarmDataFieldGetEntries` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDataFieldGetEntries/> |
| `DMSwarmDataFieldRestoreEntries` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDataFieldRestoreEntries/> |
| `DMSwarmDestroyGlobalVectorFromField` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDestroyGlobalVectorFromField/> |
| `DMSwarmDestroyGlobalVectorFromFields` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDestroyGlobalVectorFromFields/> |
| `DMSwarmDestroyLocalVectorFromField` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDestroyLocalVectorFromField/> |
| `DMSwarmDestroyLocalVectorFromFields` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDestroyLocalVectorFromFields/> |
| `DMSwarmDuplicate` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmDuplicate/> |
| `DMSwarmFinalizeFieldRegister` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmFinalizeFieldRegister/> |
| `DMSwarmGetCellDM` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetCellDM/> |
| `DMSwarmGetCellDMActive` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetCellDMActive/> |
| `DMSwarmGetCellDMByName` | Not collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetCellDMByName/> |
| `DMSwarmGetCellDMNames` | Not collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetCellDMNames/> |
| `DMSwarmGetCoordinateFunction` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetCoordinateFunction/> |
| `DMSwarmGetField` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetField/> |
| `DMSwarmGetFieldInfo` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetFieldInfo/> |
| `DMSwarmGetLocalSize` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetLocalSize/> |
| `DMSwarmGetMigrateType` | Logically Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetMigrateType/> |
| `DMSwarmGetNumSpecies` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetNumSpecies/> |
| `DMSwarmGetSize` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetSize/> |
| `DMSwarmGetType` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetType/> |
| `DMSwarmGetVelocityFunction` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmGetVelocityFunction/> |
| `DMSwarmInitializeCoordinates` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmInitializeCoordinates/> |
| `DMSwarmInitializeFieldRegister` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmInitializeFieldRegister/> |
| `DMSwarmInitializeVelocities` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmInitializeVelocities/> |
| `DMSwarmInitializeVelocitiesFromOptions` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmInitializeVelocitiesFromOptions/> |
| `DMSwarmInsertPointsUsingCellDM` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmInsertPointsUsingCellDM/> |
| `DMSwarmMigrate` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmMigrate/> |
| `DMSwarmRegisterPetscDatatypeField` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmRegisterPetscDatatypeField/> |
| `DMSwarmRegisterUserDatatypeField` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmRegisterUserDatatypeField/> |
| `DMSwarmRegisterUserStructField` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmRegisterUserStructField/> |
| `DMSwarmRemovePoint` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmRemovePoint/> |
| `DMSwarmRemovePointAtIndex` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmRemovePointAtIndex/> |
| `DMSwarmReplace` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmReplace/> |
| `DMSwarmRestoreField` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmRestoreField/> |
| `DMSwarmSetCellDM` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetCellDM/> |
| `DMSwarmSetCellDMActive` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetCellDMActive/> |
| `DMSwarmSetCoordinateFunction` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetCoordinateFunction/> |
| `DMSwarmSetLocalSizes` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetLocalSizes/> |
| `DMSwarmSetMigrateType` | Logically Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetMigrateType/> |
| `DMSwarmSetNumSpecies` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetNumSpecies/> |
| `DMSwarmSetPointCoordinates` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetPointCoordinates/> |
| `DMSwarmSetPointCoordinatesCellwise` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetPointCoordinatesCellwise/> |
| `DMSwarmSetPointCoordinatesRandom` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetPointCoordinatesRandom/> |
| `DMSwarmSetPointsUniformCoordinates` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetPointsUniformCoordinates/> |
| `DMSwarmSetType` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetType/> |
| `DMSwarmSetVelocityFunction` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSetVelocityFunction/> |
| `DMSwarmSortGetAccess` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSortGetAccess/> |
| `DMSwarmSortGetIsValid` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSortGetIsValid/> |
| `DMSwarmSortGetNumberOfPointsPerCell` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSortGetNumberOfPointsPerCell/> |
| `DMSwarmSortGetPointsPerCell` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSortGetPointsPerCell/> |
| `DMSwarmSortGetSizes` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSortGetSizes/> |
| `DMSwarmSortRestoreAccess` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSortRestoreAccess/> |
| `DMSwarmSortRestorePointsPerCell` | Not Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmSortRestorePointsPerCell/> |
| `DMSwarmVectorDefineField` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmVectorDefineField/> |
| `DMSwarmVectorDefineFields` | Collective, No Fortran support | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmVectorDefineFields/> |
| `DMSwarmVectorGetField` | Not collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmVectorGetField/> |
| `DMSwarmViewFieldsXDMF` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmViewFieldsXDMF/> |
| `DMSwarmViewXDMF` | Collective | <https://petsc.org/release/manualpages/DMSwarm/DMSwarmViewXDMF/> |

## Draw

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscDrawAppendTitle` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAppendTitle/> |
| `PetscDrawArrow` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawArrow/> |
| `PetscDrawAxisCreate` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAxisCreate/> |
| `PetscDrawAxisDestroy` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAxisDestroy/> |
| `PetscDrawAxisDraw` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAxisDraw/> |
| `PetscDrawAxisGetLimits` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAxisGetLimits/> |
| `PetscDrawAxisSetColors` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAxisSetColors/> |
| `PetscDrawAxisSetHoldLimits` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAxisSetHoldLimits/> |
| `PetscDrawAxisSetLabels` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAxisSetLabels/> |
| `PetscDrawAxisSetLimits` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawAxisSetLimits/> |
| `PetscDrawBarCreate` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarCreate/> |
| `PetscDrawBarDestroy` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarDestroy/> |
| `PetscDrawBarDraw` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarDraw/> |
| `PetscDrawBarGetAxis` | Not Collective, axis is parallel if bar is parallel | <https://petsc.org/release/manualpages/Draw/PetscDrawBarGetAxis/> |
| `PetscDrawBarGetDraw` | Not Collective, draw is parallel if bar is parallel | <https://petsc.org/release/manualpages/Draw/PetscDrawBarGetDraw/> |
| `PetscDrawBarSave` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarSave/> |
| `PetscDrawBarSetColor` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarSetColor/> |
| `PetscDrawBarSetData` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarSetData/> |
| `PetscDrawBarSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarSetFromOptions/> |
| `PetscDrawBarSetLimits` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarSetLimits/> |
| `PetscDrawBarSort` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBarSort/> |
| `PetscDrawBOP` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawBOP/> |
| `PetscDrawCheckResizedWindow` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawCheckResizedWindow/> |
| `PetscDrawClear` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawClear/> |
| `PetscDrawCollectiveBegin` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawCollectiveBegin/> |
| `PetscDrawCollectiveEnd` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawCollectiveEnd/> |
| `PetscDrawCoordinateToPixel` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawCoordinateToPixel/> |
| `PetscDrawCreate` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawCreate/> |
| `PetscDrawDestroy` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawDestroy/> |
| `PetscDrawEllipse` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawEllipse/> |
| `PetscDrawEOP` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawEOP/> |
| `PetscDrawFlush` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawFlush/> |
| `PetscDrawGetBoundingBox` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetBoundingBox/> |
| `PetscDrawGetCoordinates` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetCoordinates/> |
| `PetscDrawGetCurrentPoint` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetCurrentPoint/> |
| `PetscDrawGetMarkerType` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetMarkerType/> |
| `PetscDrawGetMouseButton` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetMouseButton/> |
| `PetscDrawGetPause` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetPause/> |
| `PetscDrawGetPopup` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetPopup/> |
| `PetscDrawGetSingleton` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetSingleton/> |
| `PetscDrawGetTitle` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetTitle/> |
| `PetscDrawGetType` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetType/> |
| `PetscDrawGetViewPort` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetViewPort/> |
| `PetscDrawGetWindowSize` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawGetWindowSize/> |
| `PetscDrawHGAddValue` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGAddValue/> |
| `PetscDrawHGAddWeightedValue` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGAddWeightedValue/> |
| `PetscDrawHGCalcStats` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGCalcStats/> |
| `PetscDrawHGCreate` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGCreate/> |
| `PetscDrawHGDestroy` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGDestroy/> |
| `PetscDrawHGDraw` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGDraw/> |
| `PetscDrawHGGetAxis` | Not Collective, axis is parallel if hist is parallel | <https://petsc.org/release/manualpages/Draw/PetscDrawHGGetAxis/> |
| `PetscDrawHGGetDraw` | Not Collective, draw is parallel if hist is parallel | <https://petsc.org/release/manualpages/Draw/PetscDrawHGGetDraw/> |
| `PetscDrawHGIntegerBins` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGIntegerBins/> |
| `PetscDrawHGReset` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGReset/> |
| `PetscDrawHGSave` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGSave/> |
| `PetscDrawHGSetColor` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGSetColor/> |
| `PetscDrawHGSetLimits` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGSetLimits/> |
| `PetscDrawHGSetNumberBins` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGSetNumberBins/> |
| `PetscDrawHGView` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawHGView/> |
| `PetscDrawIndicatorFunction` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawIndicatorFunction/> |
| `PetscDrawIsNull` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawIsNull/> |
| `PetscDrawLGAddCommonPoint` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGAddCommonPoint/> |
| `PetscDrawLGAddPoint` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGAddPoint/> |
| `PetscDrawLGAddPoints` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGAddPoints/> |
| `PetscDrawLGCreate` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGCreate/> |
| `PetscDrawLGDestroy` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGDestroy/> |
| `PetscDrawLGDraw` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGDraw/> |
| `PetscDrawLGGetAxis` | Not Collective, if lg is parallel then axis is parallel | <https://petsc.org/release/manualpages/Draw/PetscDrawLGGetAxis/> |
| `PetscDrawLGGetData` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGGetData/> |
| `PetscDrawLGGetDimension` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGGetDimension/> |
| `PetscDrawLGGetDraw` | Not Collective, if lg is parallel then draw is parallel | <https://petsc.org/release/manualpages/Draw/PetscDrawLGGetDraw/> |
| `PetscDrawLGReset` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGReset/> |
| `PetscDrawLGSave` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSave/> |
| `PetscDrawLGSetColors` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSetColors/> |
| `PetscDrawLGSetDimension` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSetDimension/> |
| `PetscDrawLGSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSetFromOptions/> |
| `PetscDrawLGSetLegend` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSetLegend/> |
| `PetscDrawLGSetLimits` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSetLimits/> |
| `PetscDrawLGSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSetOptionsPrefix/> |
| `PetscDrawLGSetUseMarkers` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSetUseMarkers/> |
| `PetscDrawLGSPDraw` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGSPDraw/> |
| `PetscDrawLGView` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLGView/> |
| `PetscDrawLine` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLine/> |
| `PetscDrawLineGetWidth` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLineGetWidth/> |
| `PetscDrawLineSetWidth` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawLineSetWidth/> |
| `PetscDrawMarker` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawMarker/> |
| `PetscDrawOpenImage` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawOpenImage/> |
| `PetscDrawOpenX` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawOpenX/> |
| `PetscDrawPause` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawPause/> |
| `PetscDrawPixelToCoordinate` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawPixelToCoordinate/> |
| `PetscDrawPoint` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawPoint/> |
| `PetscDrawPointPixel` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawPointPixel/> |
| `PetscDrawPointSetSize` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawPointSetSize/> |
| `PetscDrawPopCurrentPoint` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawPopCurrentPoint/> |
| `PetscDrawPushCurrentPoint` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawPushCurrentPoint/> |
| `PetscDrawRealToColor` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawRealToColor/> |
| `PetscDrawRectangle` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawRectangle/> |
| `PetscDrawRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Draw/PetscDrawRegister/> |
| `PetscDrawRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawRegisterAll/> |
| `PetscDrawResizeWindow` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawResizeWindow/> |
| `PetscDrawRestoreSingleton` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawRestoreSingleton/> |
| `PetscDrawSave` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSave/> |
| `PetscDrawSaveMovie` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSaveMovie/> |
| `PetscDrawScalePopup` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawScalePopup/> |
| `PetscDrawSetCoordinates` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetCoordinates/> |
| `PetscDrawSetCurrentPoint` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetCurrentPoint/> |
| `PetscDrawSetDoubleBuffer` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetDoubleBuffer/> |
| `PetscDrawSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetFromOptions/> |
| `PetscDrawSetMarkerType` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetMarkerType/> |
| `PetscDrawSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetOptionsPrefix/> |
| `PetscDrawSetPause` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetPause/> |
| `PetscDrawSetSave` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetSave/> |
| `PetscDrawSetSaveFinalImage` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetSaveFinalImage/> |
| `PetscDrawSetSaveMovie` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetSaveMovie/> |
| `PetscDrawSetTitle` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetTitle/> |
| `PetscDrawSetType` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetType/> |
| `PetscDrawSetViewPort` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSetViewPort/> |
| `PetscDrawSPAddPoint` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPAddPoint/> |
| `PetscDrawSPAddPointColorized` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPAddPointColorized/> |
| `PetscDrawSPAddPoints` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPAddPoints/> |
| `PetscDrawSPCreate` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPCreate/> |
| `PetscDrawSPDestroy` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPDestroy/> |
| `PetscDrawSPDraw` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPDraw/> |
| `PetscDrawSPGetAxis` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPGetAxis/> |
| `PetscDrawSPGetDimension` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPGetDimension/> |
| `PetscDrawSPGetDraw` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPGetDraw/> |
| `PetscDrawSplitViewPort` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSplitViewPort/> |
| `PetscDrawSPReset` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPReset/> |
| `PetscDrawSPSave` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPSave/> |
| `PetscDrawSPSetDimension` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPSetDimension/> |
| `PetscDrawSPSetLimits` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawSPSetLimits/> |
| `PetscDrawString` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawString/> |
| `PetscDrawStringBoxed` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawStringBoxed/> |
| `PetscDrawStringCentered` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawStringCentered/> |
| `PetscDrawStringGetSize` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawStringGetSize/> |
| `PetscDrawStringSetSize` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawStringSetSize/> |
| `PetscDrawStringVertical` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawStringVertical/> |
| `PetscDrawTensorContour` | Collective, but draw must be sequential | <https://petsc.org/release/manualpages/Draw/PetscDrawTensorContour/> |
| `PetscDrawTensorContourPatch` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawTensorContourPatch/> |
| `PetscDrawTriangle` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawTriangle/> |
| `PetscDrawUtilitySetCmap` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawUtilitySetCmap/> |
| `PetscDrawUtilitySetGamma` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawUtilitySetGamma/> |
| `PetscDrawView` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawView/> |
| `PetscDrawViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawViewFromOptions/> |
| `PetscDrawViewPortsCreate` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawViewPortsCreate/> |
| `PetscDrawViewPortsCreateRect` | Collective | <https://petsc.org/release/manualpages/Draw/PetscDrawViewPortsCreateRect/> |
| `PetscDrawViewPortsDestroy` | Collective on the PetscDraw inside ports | <https://petsc.org/release/manualpages/Draw/PetscDrawViewPortsDestroy/> |
| `PetscDrawViewPortsSet` | Logically Collective on the PetscDraw inside ports | <https://petsc.org/release/manualpages/Draw/PetscDrawViewPortsSet/> |
| `PetscDrawZoom` | Collective draw | <https://petsc.org/release/manualpages/Draw/PetscDrawZoom/> |
| `PetscViewerDrawGetDraw` | Collective | <https://petsc.org/release/manualpages/Draw/PetscViewerDrawGetDraw/> |
| `PetscViewerDrawGetDrawAxis` | Collective | <https://petsc.org/release/manualpages/Draw/PetscViewerDrawGetDrawAxis/> |
| `PetscViewerDrawGetDrawLG` | Collective | <https://petsc.org/release/manualpages/Draw/PetscViewerDrawGetDrawLG/> |
| `PetscViewerDrawGetDrawType` | Not Collective | <https://petsc.org/release/manualpages/Draw/PetscViewerDrawGetDrawType/> |
| `PetscViewerDrawSetDrawType` | Logically Collective | <https://petsc.org/release/manualpages/Draw/PetscViewerDrawSetDrawType/> |

## DT

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscCDFConstant1D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscCDFConstant1D/> |
| `PetscCDFConstant2D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscCDFConstant2D/> |
| `PetscCDFConstant3D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscCDFConstant3D/> |
| `PetscCDFMaxwellBoltzmann1D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscCDFMaxwellBoltzmann1D/> |
| `PetscCDFMaxwellBoltzmann2D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscCDFMaxwellBoltzmann2D/> |
| `PetscCDFMaxwellBoltzmann3D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscCDFMaxwellBoltzmann3D/> |
| `PetscDSAddBoundary` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSAddBoundary/> |
| `PetscDSAddBoundaryByName` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSAddBoundaryByName/> |
| `PetscDSAddDiscretization` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSAddDiscretization/> |
| `PetscDSCopy` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSCopy/> |
| `PetscDSCopyBoundary` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSCopyBoundary/> |
| `PetscDSCopyBounds` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSCopyBounds/> |
| `PetscDSCopyConstants` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSCopyConstants/> |
| `PetscDSCopyEquations` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSCopyEquations/> |
| `PetscDSCopyExactSolutions` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSCopyExactSolutions/> |
| `PetscDSCreate` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSCreate/> |
| `PetscDSDestroy` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSDestroy/> |
| `PetscDSDestroyBoundary` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSDestroyBoundary/> |
| `PetscDSGetBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetBdJacobian/> |
| `PetscDSGetBdJacobianPreconditioner` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscDSGetBdJacobianPreconditioner/> |
| `PetscDSGetBdResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetBdResidual/> |
| `PetscDSGetCohesive` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetCohesive/> |
| `PetscDSGetComponentDerivativeOffsets` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetComponentDerivativeOffsets/> |
| `PetscDSGetComponentDerivativeOffsetsCohesive` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetComponentDerivativeOffsetsCohesive/> |
| `PetscDSGetComponentOffset` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetComponentOffset/> |
| `PetscDSGetComponentOffsets` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetComponentOffsets/> |
| `PetscDSGetComponentOffsetsCohesive` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetComponentOffsetsCohesive/> |
| `PetscDSGetComponents` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetComponents/> |
| `PetscDSGetConstants` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetConstants/> |
| `PetscDSGetContext` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetContext/> |
| `PetscDSGetCoordinateDimension` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetCoordinateDimension/> |
| `PetscDSGetDimensions` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetDimensions/> |
| `PetscDSGetDiscretization` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetDiscretization/> |
| `PetscDSGetDynamicJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetDynamicJacobian/> |
| `PetscDSGetEvaluationArrays` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetEvaluationArrays/> |
| `PetscDSGetExactSolution` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetExactSolution/> |
| `PetscDSGetExactSolutionTimeDerivative` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetExactSolutionTimeDerivative/> |
| `PetscDSGetFaceTabulation` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetFaceTabulation/> |
| `PetscDSGetFieldIndex` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetFieldIndex/> |
| `PetscDSGetFieldOffset` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetFieldOffset/> |
| `PetscDSGetFieldOffsetCohesive` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetFieldOffsetCohesive/> |
| `PetscDSGetFieldSize` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetFieldSize/> |
| `PetscDSGetForceQuad` | Not collective | <https://petsc.org/release/manualpages/DT/PetscDSGetForceQuad/> |
| `PetscDSGetHeightSubspace` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetHeightSubspace/> |
| `PetscDSGetImplicit` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetImplicit/> |
| `PetscDSGetJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetJacobian/> |
| `PetscDSGetJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetJacobianPreconditioner/> |
| `PetscDSGetJetDegree` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetJetDegree/> |
| `PetscDSGetLowerBound` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetLowerBound/> |
| `PetscDSGetNumCohesive` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetNumCohesive/> |
| `PetscDSGetNumFields` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetNumFields/> |
| `PetscDSGetObjective` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetObjective/> |
| `PetscDSGetQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetQuadrature/> |
| `PetscDSGetResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetResidual/> |
| `PetscDSGetRHSResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetRHSResidual/> |
| `PetscDSGetRiemannSolver` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetRiemannSolver/> |
| `PetscDSGetSpatialDimension` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetSpatialDimension/> |
| `PetscDSGetTabulation` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetTabulation/> |
| `PetscDSGetTotalComponents` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetTotalComponents/> |
| `PetscDSGetTotalDimension` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetTotalDimension/> |
| `PetscDSGetType` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscDSGetType/> |
| `PetscDSGetUpdate` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetUpdate/> |
| `PetscDSGetUpperBound` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetUpperBound/> |
| `PetscDSGetWeakForm` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetWeakForm/> |
| `PetscDSGetWorkspace` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSGetWorkspace/> |
| `PetscDSHasBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSHasBdJacobian/> |
| `PetscDSHasBdJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSHasBdJacobianPreconditioner/> |
| `PetscDSHasDynamicJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSHasDynamicJacobian/> |
| `PetscDSHasJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSHasJacobian/> |
| `PetscDSHasJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSHasJacobianPreconditioner/> |
| `PetscDSIsCohesive` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSIsCohesive/> |
| `PetscDSPermuteQuadPoint` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSPermuteQuadPoint/> |
| `PetscDSRegister` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscDSRegister/> |
| `PetscDSSelectDiscretizations` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSelectDiscretizations/> |
| `PetscDSSelectEquations` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSelectEquations/> |
| `PetscDSSetBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetBdJacobian/> |
| `PetscDSSetBdJacobianPreconditioner` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscDSSetBdJacobianPreconditioner/> |
| `PetscDSSetBdResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetBdResidual/> |
| `PetscDSSetCellParameters` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetCellParameters/> |
| `PetscDSSetCohesive` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetCohesive/> |
| `PetscDSSetConstants` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetConstants/> |
| `PetscDSSetContext` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetContext/> |
| `PetscDSSetCoordinateDimension` | Logically Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetCoordinateDimension/> |
| `PetscDSSetDiscretization` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetDiscretization/> |
| `PetscDSSetDynamicJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetDynamicJacobian/> |
| `PetscDSSetExactSolution` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetExactSolution/> |
| `PetscDSSetExactSolutionTimeDerivative` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetExactSolutionTimeDerivative/> |
| `PetscDSSetForceQuad` | Logically collective on ds | <https://petsc.org/release/manualpages/DT/PetscDSSetForceQuad/> |
| `PetscDSSetFromOptions` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetFromOptions/> |
| `PetscDSSetImplicit` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetImplicit/> |
| `PetscDSSetIntegrationParameters` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetIntegrationParameters/> |
| `PetscDSSetJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetJacobian/> |
| `PetscDSSetJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetJacobianPreconditioner/> |
| `PetscDSSetJetDegree` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetJetDegree/> |
| `PetscDSSetLowerBound` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetLowerBound/> |
| `PetscDSSetObjective` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetObjective/> |
| `PetscDSSetResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetResidual/> |
| `PetscDSSetRHSResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetRHSResidual/> |
| `PetscDSSetRiemannSolver` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetRiemannSolver/> |
| `PetscDSSetType` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscDSSetType/> |
| `PetscDSSetUp` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetUp/> |
| `PetscDSSetUpdate` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetUpdate/> |
| `PetscDSSetUpperBound` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetUpperBound/> |
| `PetscDSSetWeakForm` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSSetWeakForm/> |
| `PetscDSUpdateBoundaryLabels` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSUpdateBoundaryLabels/> |
| `PetscDSUseJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDSUseJacobianPreconditioner/> |
| `PetscDSView` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSView/> |
| `PetscDSViewFromOptions` | Collective | <https://petsc.org/release/manualpages/DT/PetscDSViewFromOptions/> |
| `PetscDTCreateDefaultQuadrature` | Not collective | <https://petsc.org/release/manualpages/DT/PetscDTCreateDefaultQuadrature/> |
| `PetscDTCreateQuadratureByCell` | Not collective | <https://petsc.org/release/manualpages/DT/PetscDTCreateQuadratureByCell/> |
| `PetscDTGaussJacobiQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTGaussJacobiQuadrature/> |
| `PetscDTGaussLobattoJacobiQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTGaussLobattoJacobiQuadrature/> |
| `PetscDTGaussLobattoLegendreQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTGaussLobattoLegendreQuadrature/> |
| `PetscDTGaussQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTGaussQuadrature/> |
| `PetscDTGaussTensorQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTGaussTensorQuadrature/> |
| `PetscDTJacobiEval` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTJacobiEval/> |
| `PetscDTLegendreEval` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTLegendreEval/> |
| `PetscDTReconstructPoly` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTReconstructPoly/> |
| `PetscDTSimplexQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTSimplexQuadrature/> |
| `PetscDTStroudConicalQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTStroudConicalQuadrature/> |
| `PetscDTTanhSinhIntegrate` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscDTTanhSinhIntegrate/> |
| `PetscDTTanhSinhIntegrateMPFR` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscDTTanhSinhIntegrateMPFR/> |
| `PetscDTTanhSinhTensorQuadrature` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTTanhSinhTensorQuadrature/> |
| `PetscDTTensorQuadratureCreate` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscDTTensorQuadratureCreate/> |
| `PetscFormKeySort` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscFormKeySort/> |
| `PetscGaussLobattoLegendreElementAdvectionCreate` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementAdvectionCreate/> |
| `PetscGaussLobattoLegendreElementAdvectionDestroy` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementAdvectionDestroy/> |
| `PetscGaussLobattoLegendreElementGradientCreate` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementGradientCreate/> |
| `PetscGaussLobattoLegendreElementGradientDestroy` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementGradientDestroy/> |
| `PetscGaussLobattoLegendreElementLaplacianCreate` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementLaplacianCreate/> |
| `PetscGaussLobattoLegendreElementLaplacianDestroy` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementLaplacianDestroy/> |
| `PetscGaussLobattoLegendreElementMassCreate` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementMassCreate/> |
| `PetscGaussLobattoLegendreElementMassDestroy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementMassDestroy/> |
| `PetscGaussLobattoLegendreIntegrate` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreIntegrate/> |
| `PetscPDFConstant1D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFConstant1D/> |
| `PetscPDFConstant2D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFConstant2D/> |
| `PetscPDFConstant3D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFConstant3D/> |
| `PetscPDFGaussian1D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFGaussian1D/> |
| `PetscPDFGaussian2D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFGaussian2D/> |
| `PetscPDFGaussian3D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFGaussian3D/> |
| `PetscPDFMaxwellBoltzmann1D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFMaxwellBoltzmann1D/> |
| `PetscPDFMaxwellBoltzmann2D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFMaxwellBoltzmann2D/> |
| `PetscPDFMaxwellBoltzmann3D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFMaxwellBoltzmann3D/> |
| `PetscPDFSampleConstant1D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFSampleConstant1D/> |
| `PetscPDFSampleConstant2D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFSampleConstant2D/> |
| `PetscPDFSampleConstant3D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFSampleConstant3D/> |
| `PetscPDFSampleGaussian1D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFSampleGaussian1D/> |
| `PetscPDFSampleGaussian2D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFSampleGaussian2D/> |
| `PetscPDFSampleGaussian3D` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscPDFSampleGaussian3D/> |
| `PetscProbComputeKSStatistic` | Collective | <https://petsc.org/release/manualpages/DT/PetscProbComputeKSStatistic/> |
| `PetscProbComputeKSStatisticMagnitude` | Collective | <https://petsc.org/release/manualpages/DT/PetscProbComputeKSStatisticMagnitude/> |
| `PetscProbComputeKSStatisticWeighted` | Collective | <https://petsc.org/release/manualpages/DT/PetscProbComputeKSStatisticWeighted/> |
| `PetscProbCreateFromOptions` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscProbCreateFromOptions/> |
| `PetscQuadratureCreate` | Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureCreate/> |
| `PetscQuadratureDestroy` | Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureDestroy/> |
| `PetscQuadratureDuplicate` | Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureDuplicate/> |
| `PetscQuadratureExpandComposite` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/DT/PetscQuadratureExpandComposite/> |
| `PetscQuadratureGetCellType` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureGetCellType/> |
| `PetscQuadratureGetData` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureGetData/> |
| `PetscQuadratureGetNumComponents` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureGetNumComponents/> |
| `PetscQuadratureGetOrder` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureGetOrder/> |
| `PetscQuadraturePushForward` | Collective | <https://petsc.org/release/manualpages/DT/PetscQuadraturePushForward/> |
| `PetscQuadratureSetCellType` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureSetCellType/> |
| `PetscQuadratureSetData` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureSetData/> |
| `PetscQuadratureSetNumComponents` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureSetNumComponents/> |
| `PetscQuadratureSetOrder` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureSetOrder/> |
| `PetscQuadratureView` | Collective | <https://petsc.org/release/manualpages/DT/PetscQuadratureView/> |
| `PetscWeakFormAddBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormAddBdJacobian/> |
| `PetscWeakFormAddBdJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormAddBdJacobianPreconditioner/> |
| `PetscWeakFormAddBdResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormAddBdResidual/> |
| `PetscWeakFormAddDynamicJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormAddDynamicJacobian/> |
| `PetscWeakFormAddJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormAddJacobian/> |
| `PetscWeakFormAddJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormAddJacobianPreconditioner/> |
| `PetscWeakFormAddObjective` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormAddObjective/> |
| `PetscWeakFormAddResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormAddResidual/> |
| `PetscWeakFormClear` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormClear/> |
| `PetscWeakFormClearIndex` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormClearIndex/> |
| `PetscWeakFormCopy` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormCopy/> |
| `PetscWeakFormCreate` | Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormCreate/> |
| `PetscWeakFormDestroy` | Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormDestroy/> |
| `PetscWeakFormGetBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetBdJacobian/> |
| `PetscWeakFormGetBdJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetBdJacobianPreconditioner/> |
| `PetscWeakFormGetBdResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetBdResidual/> |
| `PetscWeakFormGetDynamicJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetDynamicJacobian/> |
| `PetscWeakFormGetIndexObjective` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetIndexObjective/> |
| `PetscWeakFormGetJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetJacobian/> |
| `PetscWeakFormGetJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetJacobianPreconditioner/> |
| `PetscWeakFormGetNumFields` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetNumFields/> |
| `PetscWeakFormGetObjective` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetObjective/> |
| `PetscWeakFormGetResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetResidual/> |
| `PetscWeakFormGetRiemannSolver` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormGetRiemannSolver/> |
| `PetscWeakFormHasBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormHasBdJacobian/> |
| `PetscWeakFormHasBdJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormHasBdJacobianPreconditioner/> |
| `PetscWeakFormHasDynamicJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormHasDynamicJacobian/> |
| `PetscWeakFormHasJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormHasJacobian/> |
| `PetscWeakFormHasJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormHasJacobianPreconditioner/> |
| `PetscWeakFormReplaceLabel` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormReplaceLabel/> |
| `PetscWeakFormRewriteKeys` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormRewriteKeys/> |
| `PetscWeakFormSetBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetBdJacobian/> |
| `PetscWeakFormSetBdJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetBdJacobianPreconditioner/> |
| `PetscWeakFormSetBdResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetBdResidual/> |
| `PetscWeakFormSetDynamicJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetDynamicJacobian/> |
| `PetscWeakFormSetIndexBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexBdJacobian/> |
| `PetscWeakFormSetIndexBdJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexBdJacobianPreconditioner/> |
| `PetscWeakFormSetIndexBdResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexBdResidual/> |
| `PetscWeakFormSetIndexDynamicJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexDynamicJacobian/> |
| `PetscWeakFormSetIndexJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexJacobian/> |
| `PetscWeakFormSetIndexJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexJacobianPreconditioner/> |
| `PetscWeakFormSetIndexObjective` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexObjective/> |
| `PetscWeakFormSetIndexResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexResidual/> |
| `PetscWeakFormSetIndexRiemannSolver` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexRiemannSolver/> |
| `PetscWeakFormSetJacobian` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetJacobian/> |
| `PetscWeakFormSetJacobianPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetJacobianPreconditioner/> |
| `PetscWeakFormSetNumFields` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetNumFields/> |
| `PetscWeakFormSetObjective` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetObjective/> |
| `PetscWeakFormSetResidual` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetResidual/> |
| `PetscWeakFormSetRiemannSolver` | Not Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormSetRiemannSolver/> |
| `PetscWeakFormView` | Collective | <https://petsc.org/release/manualpages/DT/PetscWeakFormView/> |

## DUALSPACE

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscDualSpaceCreate` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceCreate/> |
| `PetscDualSpaceCreateSum` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceCreateSum/> |
| `PetscDualSpaceDestroy` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceDestroy/> |
| `PetscDualSpaceDuplicate` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceDuplicate/> |
| `PetscDualSpaceGetDimension` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetDimension/> |
| `PetscDualSpaceGetDM` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetDM/> |
| `PetscDualSpaceGetFunctional` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetFunctional/> |
| `PetscDualSpaceGetHeightSubspace` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetHeightSubspace/> |
| `PetscDualSpaceGetInteriorDimension` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetInteriorDimension/> |
| `PetscDualSpaceGetInteriorSection` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetInteriorSection/> |
| `PetscDualSpaceGetNumDof` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetNumDof/> |
| `PetscDualSpaceGetOrder` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetOrder/> |
| `PetscDualSpaceGetPointSubspace` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetPointSubspace/> |
| `PetscDualSpaceGetSection` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetSection/> |
| `PetscDualSpaceGetSymmetries` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetSymmetries/> |
| `PetscDualSpaceGetType` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetType/> |
| `PetscDualSpaceGetUniform` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetUniform/> |
| `PetscDualSpaceLagrangeGetContinuity` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetContinuity/> |
| `PetscDualSpaceLagrangeGetMomentOrder` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetMomentOrder/> |
| `PetscDualSpaceLagrangeGetNodeType` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetNodeType/> |
| `PetscDualSpaceLagrangeGetTensor` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetTensor/> |
| `PetscDualSpaceLagrangeGetTrimmed` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetTrimmed/> |
| `PetscDualSpaceLagrangeGetUseMoments` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetUseMoments/> |
| `PetscDualSpaceLagrangeSetContinuity` | Logically Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetContinuity/> |
| `PetscDualSpaceLagrangeSetMomentOrder` | Logically Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetMomentOrder/> |
| `PetscDualSpaceLagrangeSetNodeType` | Logically Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetNodeType/> |
| `PetscDualSpaceLagrangeSetTensor` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetTensor/> |
| `PetscDualSpaceLagrangeSetTrimmed` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetTrimmed/> |
| `PetscDualSpaceLagrangeSetUseMoments` | Logically Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetUseMoments/> |
| `PetscDualSpaceRefinedSetCellSpaces` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceRefinedSetCellSpaces/> |
| `PetscDualSpaceRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceRegister/> |
| `PetscDualSpaceSetDM` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetDM/> |
| `PetscDualSpaceSetFromOptions` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetFromOptions/> |
| `PetscDualSpaceSetOrder` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetOrder/> |
| `PetscDualSpaceSetType` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetType/> |
| `PetscDualSpaceSetUp` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetUp/> |
| `PetscDualSpaceSimpleSetDimension` | Logically Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSimpleSetDimension/> |
| `PetscDualSpaceSimpleSetFunctional` | Not Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSimpleSetFunctional/> |
| `PetscDualSpaceSumGetInterleave` | Logically collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumGetInterleave/> |
| `PetscDualSpaceSumSetInterleave` | Logically collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumSetInterleave/> |
| `PetscDualSpaceView` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceView/> |
| `PetscDualSpaceViewFromOptions` | Collective | <https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceViewFromOptions/> |

## FE

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscFECompositeGetMapping` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFECompositeGetMapping/> |
| `PetscFEComputeTabulation` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEComputeTabulation/> |
| `PetscFECopyQuadrature` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFECopyQuadrature/> |
| `PetscFECreate` | Collective | <https://petsc.org/release/manualpages/FE/PetscFECreate/> |
| `PetscFECreateBrokenElement` | Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateBrokenElement/> |
| `PetscFECreateByCell` | Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateByCell/> |
| `PetscFECreateCellGeometry` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateCellGeometry/> |
| `PetscFECreateDefault` | Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateDefault/> |
| `PetscFECreateFromSpaces` | Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateFromSpaces/> |
| `PetscFECreateHeightTrace` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateHeightTrace/> |
| `PetscFECreateLagrange` | Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateLagrange/> |
| `PetscFECreateLagrangeByCell` | Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateLagrangeByCell/> |
| `PetscFECreateTabulation` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateTabulation/> |
| `PetscFECreateVector` | Collective | <https://petsc.org/release/manualpages/FE/PetscFECreateVector/> |
| `PetscFEDestroy` | Collective | <https://petsc.org/release/manualpages/FE/PetscFEDestroy/> |
| `PetscFEDestroyCellGeometry` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEDestroyCellGeometry/> |
| `PetscFEExpandFaceQuadrature` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEExpandFaceQuadrature/> |
| `PetscFEGetBasisSpace` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetBasisSpace/> |
| `PetscFEGetCeedBasis` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetCeedBasis/> |
| `PetscFEGetCellTabulation` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetCellTabulation/> |
| `PetscFEGetDimension` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetDimension/> |
| `PetscFEGetDualSpace` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetDualSpace/> |
| `PetscFEGetFaceCentroidTabulation` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetFaceCentroidTabulation/> |
| `PetscFEGetFaceQuadrature` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetFaceQuadrature/> |
| `PetscFEGetFaceTabulation` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetFaceTabulation/> |
| `PetscFEGetNumComponents` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetNumComponents/> |
| `PetscFEGetNumDof` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetNumDof/> |
| `PetscFEGetQuadrature` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetQuadrature/> |
| `PetscFEGetSpatialDimension` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetSpatialDimension/> |
| `PetscFEGetTileSizes` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetTileSizes/> |
| `PetscFEGetType` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEGetType/> |
| `PetscFEIntegrate` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEIntegrate/> |
| `PetscFEIntegrateBd` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEIntegrateBd/> |
| `PetscFEIntegrateBdJacobian` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEIntegrateBdJacobian/> |
| `PetscFEIntegrateBdResidual` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEIntegrateBdResidual/> |
| `PetscFEIntegrateHybridJacobian` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEIntegrateHybridJacobian/> |
| `PetscFEIntegrateHybridResidual` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEIntegrateHybridResidual/> |
| `PetscFEIntegrateJacobian` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEIntegrateJacobian/> |
| `PetscFEIntegrateResidual` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFEIntegrateResidual/> |
| `PetscFELimitDegree` | Collective | <https://petsc.org/release/manualpages/FE/PetscFELimitDegree/> |
| `PetscFERefine` | Collective | <https://petsc.org/release/manualpages/FE/PetscFERefine/> |
| `PetscFERegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/FE/PetscFERegister/> |
| `PetscFESetBasisSpace` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFESetBasisSpace/> |
| `PetscFESetCeed` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFESetCeed/> |
| `PetscFESetDualSpace` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFESetDualSpace/> |
| `PetscFESetFaceQuadrature` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFESetFaceQuadrature/> |
| `PetscFESetFromOptions` | Collective | <https://petsc.org/release/manualpages/FE/PetscFESetFromOptions/> |
| `PetscFESetName` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFESetName/> |
| `PetscFESetNumComponents` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFESetNumComponents/> |
| `PetscFESetQuadrature` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFESetQuadrature/> |
| `PetscFESetTileSizes` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscFESetTileSizes/> |
| `PetscFESetType` | Collective | <https://petsc.org/release/manualpages/FE/PetscFESetType/> |
| `PetscFESetUp` | Collective | <https://petsc.org/release/manualpages/FE/PetscFESetUp/> |
| `PetscFEView` | Collective | <https://petsc.org/release/manualpages/FE/PetscFEView/> |
| `PetscFEViewFromOptions` | Collective | <https://petsc.org/release/manualpages/FE/PetscFEViewFromOptions/> |
| `PetscTabulationDestroy` | Not Collective | <https://petsc.org/release/manualpages/FE/PetscTabulationDestroy/> |

## FV

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscFVCreate` | Collective | <https://petsc.org/release/manualpages/FV/PetscFVCreate/> |
| `PetscFVCreateDualSpace` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVCreateDualSpace/> |
| `PetscFVCreateTabulation` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVCreateTabulation/> |
| `PetscFVDestroy` | Collective | <https://petsc.org/release/manualpages/FV/PetscFVDestroy/> |
| `PetscFVGetCeedBasis` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetCeedBasis/> |
| `PetscFVGetCellTabulation` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetCellTabulation/> |
| `PetscFVGetComponentName` | Logically Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetComponentName/> |
| `PetscFVGetComputeGradients` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetComputeGradients/> |
| `PetscFVGetDualSpace` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetDualSpace/> |
| `PetscFVGetLimiter` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetLimiter/> |
| `PetscFVGetNumComponents` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetNumComponents/> |
| `PetscFVGetQuadrature` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetQuadrature/> |
| `PetscFVGetSpatialDimension` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetSpatialDimension/> |
| `PetscFVGetType` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVGetType/> |
| `PetscFVIntegrateRHSFunction` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVIntegrateRHSFunction/> |
| `PetscFVLeastSquaresSetMaxFaces` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVLeastSquaresSetMaxFaces/> |
| `PetscFVRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/FV/PetscFVRegister/> |
| `PetscFVSetCeed` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetCeed/> |
| `PetscFVSetComponentName` | Logically Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetComponentName/> |
| `PetscFVSetComputeGradients` | Logically Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetComputeGradients/> |
| `PetscFVSetDualSpace` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetDualSpace/> |
| `PetscFVSetFromOptions` | Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetFromOptions/> |
| `PetscFVSetLimiter` | Logically Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetLimiter/> |
| `PetscFVSetNumComponents` | Logically Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetNumComponents/> |
| `PetscFVSetQuadrature` | Logically Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetQuadrature/> |
| `PetscFVSetSpatialDimension` | Logically Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetSpatialDimension/> |
| `PetscFVSetType` | Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetType/> |
| `PetscFVSetUp` | Collective | <https://petsc.org/release/manualpages/FV/PetscFVSetUp/> |
| `PetscFVView` | Collective | <https://petsc.org/release/manualpages/FV/PetscFVView/> |
| `PetscFVViewFromOptions` | Collective | <https://petsc.org/release/manualpages/FV/PetscFVViewFromOptions/> |
| `PetscLimiterCreate` | Collective | <https://petsc.org/release/manualpages/FV/PetscLimiterCreate/> |
| `PetscLimiterDestroy` | Collective | <https://petsc.org/release/manualpages/FV/PetscLimiterDestroy/> |
| `PetscLimiterGetType` | Not Collective | <https://petsc.org/release/manualpages/FV/PetscLimiterGetType/> |
| `PetscLimiterRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/FV/PetscLimiterRegister/> |
| `PetscLimiterSetFromOptions` | Collective | <https://petsc.org/release/manualpages/FV/PetscLimiterSetFromOptions/> |
| `PetscLimiterSetType` | Collective | <https://petsc.org/release/manualpages/FV/PetscLimiterSetType/> |
| `PetscLimiterSetUp` | Collective | <https://petsc.org/release/manualpages/FV/PetscLimiterSetUp/> |
| `PetscLimiterView` | Collective | <https://petsc.org/release/manualpages/FV/PetscLimiterView/> |
| `PetscLimiterViewFromOptions` | Collective | <https://petsc.org/release/manualpages/FV/PetscLimiterViewFromOptions/> |

## IS

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `ISAllGather` | Collective | <https://petsc.org/release/manualpages/IS/ISAllGather/> |
| `ISAllGatherColors` | Collective | <https://petsc.org/release/manualpages/IS/ISAllGatherColors/> |
| `ISBlockGetIndices` | Not Collective | <https://petsc.org/release/manualpages/IS/ISBlockGetIndices/> |
| `ISBlockGetLocalSize` | Not Collective | <https://petsc.org/release/manualpages/IS/ISBlockGetLocalSize/> |
| `ISBlockGetSize` | Not Collective | <https://petsc.org/release/manualpages/IS/ISBlockGetSize/> |
| `ISBlockRestoreIndices` | Not Collective | <https://petsc.org/release/manualpages/IS/ISBlockRestoreIndices/> |
| `ISBlockSetIndices` | Collective | <https://petsc.org/release/manualpages/IS/ISBlockSetIndices/> |
| `ISBuildTwoSided` | Collective | <https://petsc.org/release/manualpages/IS/ISBuildTwoSided/> |
| `ISClearInfoCache` | Not Collective | <https://petsc.org/release/manualpages/IS/ISClearInfoCache/> |
| `ISColoringCreate` | Collective | <https://petsc.org/release/manualpages/IS/ISColoringCreate/> |
| `ISColoringDestroy` | Collective | <https://petsc.org/release/manualpages/IS/ISColoringDestroy/> |
| `ISColoringGetColors` | Not Collective | <https://petsc.org/release/manualpages/IS/ISColoringGetColors/> |
| `ISColoringGetIS` | Collective | <https://petsc.org/release/manualpages/IS/ISColoringGetIS/> |
| `ISColoringGetType` | Collective | <https://petsc.org/release/manualpages/IS/ISColoringGetType/> |
| `ISColoringReference` | Logically collective | <https://petsc.org/release/manualpages/IS/ISColoringReference/> |
| `ISColoringRestoreIS` | Collective | <https://petsc.org/release/manualpages/IS/ISColoringRestoreIS/> |
| `ISColoringSetType` | Collective | <https://petsc.org/release/manualpages/IS/ISColoringSetType/> |
| `ISColoringValueCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/IS/ISColoringValueCast/> |
| `ISColoringView` | Collective | <https://petsc.org/release/manualpages/IS/ISColoringView/> |
| `ISColoringViewFromOptions` | Collective | <https://petsc.org/release/manualpages/IS/ISColoringViewFromOptions/> |
| `ISComplement` | Collective | <https://petsc.org/release/manualpages/IS/ISComplement/> |
| `ISConcatenate` | Collective | <https://petsc.org/release/manualpages/IS/ISConcatenate/> |
| `ISContiguousLocal` | Not Collective | <https://petsc.org/release/manualpages/IS/ISContiguousLocal/> |
| `ISCopy` | Collective | <https://petsc.org/release/manualpages/IS/ISCopy/> |
| `ISCreate` | Collective | <https://petsc.org/release/manualpages/IS/ISCreate/> |
| `ISCreateBlock` | Collective | <https://petsc.org/release/manualpages/IS/ISCreateBlock/> |
| `ISCreateGeneral` | Collective | <https://petsc.org/release/manualpages/IS/ISCreateGeneral/> |
| `ISCreateStride` | Collective | <https://petsc.org/release/manualpages/IS/ISCreateStride/> |
| `ISCreateSubIS` | Collective | <https://petsc.org/release/manualpages/IS/ISCreateSubIS/> |
| `ISDestroy` | Collective | <https://petsc.org/release/manualpages/IS/ISDestroy/> |
| `ISDifference` | Collective | <https://petsc.org/release/manualpages/IS/ISDifference/> |
| `ISDuplicate` | Collective | <https://petsc.org/release/manualpages/IS/ISDuplicate/> |
| `ISEmbed` | Not Collective | <https://petsc.org/release/manualpages/IS/ISEmbed/> |
| `ISEqual` | Collective | <https://petsc.org/release/manualpages/IS/ISEqual/> |
| `ISEqualUnsorted` | Collective | <https://petsc.org/release/manualpages/IS/ISEqualUnsorted/> |
| `ISExpand` | Collective | <https://petsc.org/release/manualpages/IS/ISExpand/> |
| `ISGeneralFilter` | Collective | <https://petsc.org/release/manualpages/IS/ISGeneralFilter/> |
| `ISGeneralSetIndices` | Logically Collective | <https://petsc.org/release/manualpages/IS/ISGeneralSetIndices/> |
| `ISGeneralSetIndicesFromMask` | Collective | <https://petsc.org/release/manualpages/IS/ISGeneralSetIndicesFromMask/> |
| `ISGetBlockSize` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetBlockSize/> |
| `ISGetCompressOutput` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetCompressOutput/> |
| `ISGetIndices` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetIndices/> |
| `ISGetInfo` | Collective or Logically Collective if the type is IS_GLOBAL (logically collective if the value of the property has been permanently set with ISSetInfo () ) | <https://petsc.org/release/manualpages/IS/ISGetInfo/> |
| `ISGetLayout` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetLayout/> |
| `ISGetLocalSize` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetLocalSize/> |
| `ISGetMinMax` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetMinMax/> |
| `ISGetNonlocalIndices` | Collective | <https://petsc.org/release/manualpages/IS/ISGetNonlocalIndices/> |
| `ISGetNonlocalIS` | Collective | <https://petsc.org/release/manualpages/IS/ISGetNonlocalIS/> |
| `ISGetPointRange` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetPointRange/> |
| `ISGetPointSubrange` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetPointSubrange/> |
| `ISGetSize` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetSize/> |
| `ISGetTotalIndices` | Collective | <https://petsc.org/release/manualpages/IS/ISGetTotalIndices/> |
| `ISGetType` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGetType/> |
| `ISGlobalToLocalMappingApply` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGlobalToLocalMappingApply/> |
| `ISGlobalToLocalMappingApplyBlock` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGlobalToLocalMappingApplyBlock/> |
| `ISGlobalToLocalMappingApplyIS` | Not Collective | <https://petsc.org/release/manualpages/IS/ISGlobalToLocalMappingApplyIS/> |
| `ISIdentity` | Collective | <https://petsc.org/release/manualpages/IS/ISIdentity/> |
| `ISIntersect` | Collective | <https://petsc.org/release/manualpages/IS/ISIntersect/> |
| `ISInvertPermutation` | Collective | <https://petsc.org/release/manualpages/IS/ISInvertPermutation/> |
| `ISListToPair` | Collective | <https://petsc.org/release/manualpages/IS/ISListToPair/> |
| `ISLoad` | Collective | <https://petsc.org/release/manualpages/IS/ISLoad/> |
| `ISLocalToGlobalMappingApply` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingApply/> |
| `ISLocalToGlobalMappingApplyBlock` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingApplyBlock/> |
| `ISLocalToGlobalMappingApplyIS` | Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingApplyIS/> |
| `ISLocalToGlobalMappingConcatenate` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingConcatenate/> |
| `ISLocalToGlobalMappingCreate` | Not Collective, but communicator may have more than one process | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingCreate/> |
| `ISLocalToGlobalMappingCreateIS` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingCreateIS/> |
| `ISLocalToGlobalMappingCreateSF` | Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingCreateSF/> |
| `ISLocalToGlobalMappingDestroy` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingDestroy/> |
| `ISLocalToGlobalMappingDuplicate` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingDuplicate/> |
| `ISLocalToGlobalMappingGetBlockIndices` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockIndices/> |
| `ISLocalToGlobalMappingGetBlockInfo` | Collective the first time it is called | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockInfo/> |
| `ISLocalToGlobalMappingGetBlockMultiLeavesSF` | Collective the first time it is called | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockMultiLeavesSF/> |
| `ISLocalToGlobalMappingGetBlockNodeInfo` | Collective the first time it is called | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockNodeInfo/> |
| `ISLocalToGlobalMappingGetBlockSize` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockSize/> |
| `ISLocalToGlobalMappingGetIndices` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetIndices/> |
| `ISLocalToGlobalMappingGetInfo` | Collective the first time it is called | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetInfo/> |
| `ISLocalToGlobalMappingGetNodeInfo` | Collective the first time it is called | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetNodeInfo/> |
| `ISLocalToGlobalMappingGetSize` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetSize/> |
| `ISLocalToGlobalMappingGetType` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetType/> |
| `ISLocalToGlobalMappingLoad` | Collective on viewer | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingLoad/> |
| `ISLocalToGlobalMappingRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRegister/> |
| `ISLocalToGlobalMappingRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRegisterAll/> |
| `ISLocalToGlobalMappingRestoreBlockIndices` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreBlockIndices/> |
| `ISLocalToGlobalMappingRestoreBlockInfo` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreBlockInfo/> |
| `ISLocalToGlobalMappingRestoreBlockNodeInfo` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreBlockNodeInfo/> |
| `ISLocalToGlobalMappingRestoreIndices` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreIndices/> |
| `ISLocalToGlobalMappingRestoreInfo` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreInfo/> |
| `ISLocalToGlobalMappingRestoreNodeInfo` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreNodeInfo/> |
| `ISLocalToGlobalMappingSetBlockSize` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingSetBlockSize/> |
| `ISLocalToGlobalMappingSetFromOptions` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingSetFromOptions/> |
| `ISLocalToGlobalMappingSetType` | Logically Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingSetType/> |
| `ISLocalToGlobalMappingView` | Collective on viewer | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingView/> |
| `ISLocalToGlobalMappingViewFromOptions` | Collective | <https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingViewFromOptions/> |
| `ISLocate` | Not Collective | <https://petsc.org/release/manualpages/IS/ISLocate/> |
| `ISOnComm` | Collective | <https://petsc.org/release/manualpages/IS/ISOnComm/> |
| `ISPairToList` | Collective | <https://petsc.org/release/manualpages/IS/ISPairToList/> |
| `ISPartitioningCount` | Collective | <https://petsc.org/release/manualpages/IS/ISPartitioningCount/> |
| `ISPartitioningToNumbering` | Collective | <https://petsc.org/release/manualpages/IS/ISPartitioningToNumbering/> |
| `ISPermutation` | Logically Collective | <https://petsc.org/release/manualpages/IS/ISPermutation/> |
| `ISRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/IS/ISRegister/> |
| `ISRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/IS/ISRegisterAll/> |
| `ISRenumber` | Collective | <https://petsc.org/release/manualpages/IS/ISRenumber/> |
| `ISRestoreIndices` | Not Collective | <https://petsc.org/release/manualpages/IS/ISRestoreIndices/> |
| `ISRestoreNonlocalIndices` | Not Collective. | <https://petsc.org/release/manualpages/IS/ISRestoreNonlocalIndices/> |
| `ISRestoreNonlocalIS` | Not collective. | <https://petsc.org/release/manualpages/IS/ISRestoreNonlocalIS/> |
| `ISRestorePointRange` | Not Collective | <https://petsc.org/release/manualpages/IS/ISRestorePointRange/> |
| `ISRestoreTotalIndices` | Not Collective. | <https://petsc.org/release/manualpages/IS/ISRestoreTotalIndices/> |
| `ISSetBlockSize` | Collective | <https://petsc.org/release/manualpages/IS/ISSetBlockSize/> |
| `ISSetCompressOutput` | Collective | <https://petsc.org/release/manualpages/IS/ISSetCompressOutput/> |
| `ISSetIdentity` | Logically Collective | <https://petsc.org/release/manualpages/IS/ISSetIdentity/> |
| `ISSetInfo` | Logically Collective if ISInfoType is IS_GLOBAL | <https://petsc.org/release/manualpages/IS/ISSetInfo/> |
| `ISSetLayout` | Collective | <https://petsc.org/release/manualpages/IS/ISSetLayout/> |
| `ISSetPermutation` | Logically Collective | <https://petsc.org/release/manualpages/IS/ISSetPermutation/> |
| `ISSetType` | Collective | <https://petsc.org/release/manualpages/IS/ISSetType/> |
| `ISShift` | Collective | <https://petsc.org/release/manualpages/IS/ISShift/> |
| `ISSort` | Collective | <https://petsc.org/release/manualpages/IS/ISSort/> |
| `ISSorted` | Not Collective | <https://petsc.org/release/manualpages/IS/ISSorted/> |
| `ISSortPermutation` | Not Collective | <https://petsc.org/release/manualpages/IS/ISSortPermutation/> |
| `ISSortRemoveDups` | Collective | <https://petsc.org/release/manualpages/IS/ISSortRemoveDups/> |
| `ISStrideGetInfo` | Not Collective | <https://petsc.org/release/manualpages/IS/ISStrideGetInfo/> |
| `ISStrideSetStride` | Logically Collective | <https://petsc.org/release/manualpages/IS/ISStrideSetStride/> |
| `ISToGeneral` | Collective | <https://petsc.org/release/manualpages/IS/ISToGeneral/> |
| `ISView` | Collective | <https://petsc.org/release/manualpages/IS/ISView/> |
| `ISViewFromOptions` | Collective | <https://petsc.org/release/manualpages/IS/ISViewFromOptions/> |
| `PetscKDTreeCreate` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/IS/PetscKDTreeCreate/> |
| `PetscKDTreeDestroy` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/IS/PetscKDTreeDestroy/> |
| `PetscKDTreeQueryPointsNearestNeighbor` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/IS/PetscKDTreeQueryPointsNearestNeighbor/> |
| `PetscKDTreeView` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/IS/PetscKDTreeView/> |
| `PetscLayoutCompare` | Not Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutCompare/> |
| `PetscLayoutCreate` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutCreate/> |
| `PetscLayoutCreateFromRanges` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutCreateFromRanges/> |
| `PetscLayoutCreateFromSizes` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutCreateFromSizes/> |
| `PetscLayoutDestroy` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutDestroy/> |
| `PetscLayoutDuplicate` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutDuplicate/> |
| `PetscLayoutFindOwner` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/IS/PetscLayoutFindOwner/> |
| `PetscLayoutFindOwnerIndex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/IS/PetscLayoutFindOwnerIndex/> |
| `PetscLayoutGetBlockSize` | Not Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutGetBlockSize/> |
| `PetscLayoutGetLocalSize` | Not Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutGetLocalSize/> |
| `PetscLayoutGetRange` | Not Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutGetRange/> |
| `PetscLayoutGetRanges` | Not Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutGetRanges/> |
| `PetscLayoutGetSize` | Not Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutGetSize/> |
| `PetscLayoutReference` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutReference/> |
| `PetscLayoutSetBlockSize` | Logically Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutSetBlockSize/> |
| `PetscLayoutSetISLocalToGlobalMapping` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutSetISLocalToGlobalMapping/> |
| `PetscLayoutSetLocalSize` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutSetLocalSize/> |
| `PetscLayoutSetSize` | Logically Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutSetSize/> |
| `PetscLayoutSetUp` | Collective | <https://petsc.org/release/manualpages/IS/PetscLayoutSetUp/> |
| `PetscParallelSortInt` | Collective | <https://petsc.org/release/manualpages/IS/PetscParallelSortInt/> |

## KSP

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMCopyDMKSP` | Logically Collective | <https://petsc.org/release/manualpages/KSP/DMCopyDMKSP/> |
| `DMGetDMKSP` | Logically Collective | <https://petsc.org/release/manualpages/KSP/DMGetDMKSP/> |
| `DMGetDMKSPWrite` | Logically Collective | <https://petsc.org/release/manualpages/KSP/DMGetDMKSPWrite/> |
| `DMKSPGetComputeInitialGuess` | Not Collective | <https://petsc.org/release/manualpages/KSP/DMKSPGetComputeInitialGuess/> |
| `DMKSPGetComputeOperators` | Not Collective | <https://petsc.org/release/manualpages/KSP/DMKSPGetComputeOperators/> |
| `DMKSPGetComputeRHS` | Not Collective | <https://petsc.org/release/manualpages/KSP/DMKSPGetComputeRHS/> |
| `DMKSPSetComputeInitialGuess` | Not Collective | <https://petsc.org/release/manualpages/KSP/DMKSPSetComputeInitialGuess/> |
| `DMKSPSetComputeOperators` | Not Collective | <https://petsc.org/release/manualpages/KSP/DMKSPSetComputeOperators/> |
| `DMKSPSetComputeRHS` | Not Collective | <https://petsc.org/release/manualpages/KSP/DMKSPSetComputeRHS/> |
| `KSPAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPAppendOptionsPrefix/> |
| `KSPBCGSLSetEll` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPBCGSLSetEll/> |
| `KSPBCGSLSetPol` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPBCGSLSetPol/> |
| `KSPBCGSLSetUsePseudoinverse` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPBCGSLSetUsePseudoinverse/> |
| `KSPBCGSLSetXRes` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPBCGSLSetXRes/> |
| `KSPBuildResidual` | Collective | <https://petsc.org/release/manualpages/KSP/KSPBuildResidual/> |
| `KSPBuildSolution` | Collective | <https://petsc.org/release/manualpages/KSP/KSPBuildSolution/> |
| `KSPBuildSolutionDefault` | Collective | <https://petsc.org/release/manualpages/KSP/KSPBuildSolutionDefault/> |
| `KSPCGGetNormD` | Not collective | <https://petsc.org/release/manualpages/KSP/KSPCGGetNormD/> |
| `KSPCGGetObjFcn` | Not collective | <https://petsc.org/release/manualpages/KSP/KSPCGGetObjFcn/> |
| `KSPCGSetObjectiveTarget` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPCGSetObjectiveTarget/> |
| `KSPCGSetRadius` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPCGSetRadius/> |
| `KSPCGSetType` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPCGSetType/> |
| `KSPCGUseSingleReduction` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPCGUseSingleReduction/> |
| `KSPChebyshevEstEigSet` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPChebyshevEstEigSet/> |
| `KSPChebyshevEstEigSetUseNoisy` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPChebyshevEstEigSetUseNoisy/> |
| `KSPChebyshevGetKind` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPChebyshevGetKind/> |
| `KSPChebyshevSetEigenvalues` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPChebyshevSetEigenvalues/> |
| `KSPChebyshevSetKind` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPChebyshevSetKind/> |
| `KSPCheckPCMPI` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/KSP/KSPCheckPCMPI/> |
| `KSPCheckSolve` | Collective | <https://petsc.org/release/manualpages/KSP/KSPCheckSolve/> |
| `KSPComputeConvergenceRate` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPComputeConvergenceRate/> |
| `KSPComputeEigenvalues` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPComputeEigenvalues/> |
| `KSPComputeEigenvaluesExplicitly` | Collective | <https://petsc.org/release/manualpages/KSP/KSPComputeEigenvaluesExplicitly/> |
| `KSPComputeExtremeSingularValues` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPComputeExtremeSingularValues/> |
| `KSPComputeOperator` | Collective | <https://petsc.org/release/manualpages/KSP/KSPComputeOperator/> |
| `KSPComputeRitz` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPComputeRitz/> |
| `KSPConvergedDefault` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedDefault/> |
| `KSPConvergedDefaultCreate` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedDefaultCreate/> |
| `KSPConvergedDefaultDestroy` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedDefaultDestroy/> |
| `KSPConvergedDefaultSetConvergedMaxits` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedDefaultSetConvergedMaxits/> |
| `KSPConvergedDefaultSetUIRNorm` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedDefaultSetUIRNorm/> |
| `KSPConvergedDefaultSetUMIRNorm` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedDefaultSetUMIRNorm/> |
| `KSPConvergedRateView` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedRateView/> |
| `KSPConvergedReasonView` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedReasonView/> |
| `KSPConvergedReasonViewCancel` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedReasonViewCancel/> |
| `KSPConvergedReasonViewFromOptions` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedReasonViewFromOptions/> |
| `KSPConvergedReasonViewSet` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedReasonViewSet/> |
| `KSPConvergedSkip` | Collective | <https://petsc.org/release/manualpages/KSP/KSPConvergedSkip/> |
| `KSPCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPCreate/> |
| `KSPCreateVecs` | Collective | <https://petsc.org/release/manualpages/KSP/KSPCreateVecs/> |
| `KSPDestroy` | Collective | <https://petsc.org/release/manualpages/KSP/KSPDestroy/> |
| `KSPDestroyDefault` | Collective | <https://petsc.org/release/manualpages/KSP/KSPDestroyDefault/> |
| `KSPFCGGetMmax` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPFCGGetMmax/> |
| `KSPFCGGetNprealloc` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPFCGGetNprealloc/> |
| `KSPFCGGetTruncationType` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPFCGGetTruncationType/> |
| `KSPFCGSetMmax` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPFCGSetMmax/> |
| `KSPFCGSetNprealloc` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPFCGSetNprealloc/> |
| `KSPFCGSetTruncationType` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPFCGSetTruncationType/> |
| `KSPFETIDPSetInnerBDDC` | Collective | <https://petsc.org/release/manualpages/KSP/KSPFETIDPSetInnerBDDC/> |
| `KSPFETIDPSetPressureOperator` | Collective | <https://petsc.org/release/manualpages/KSP/KSPFETIDPSetPressureOperator/> |
| `KSPFlexibleSetModifyPC` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPFlexibleSetModifyPC/> |
| `KSPGCRGetRestart` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGCRGetRestart/> |
| `KSPGCRSetRestart` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGCRSetRestart/> |
| `KSPGetAndClearConvergenceTest` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGetAndClearConvergenceTest/> |
| `KSPGetApplicationContext` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetApplicationContext/> |
| `KSPGetComputeEigenvalues` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetComputeEigenvalues/> |
| `KSPGetComputeSingularValues` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetComputeSingularValues/> |
| `KSPGetConvergedNegativeCurvature` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGetConvergedNegativeCurvature/> |
| `KSPGetConvergedReason` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetConvergedReason/> |
| `KSPGetConvergedReasonString` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetConvergedReasonString/> |
| `KSPGetConvergenceContext` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetConvergenceContext/> |
| `KSPGetConvergenceTest` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGetConvergenceTest/> |
| `KSPGetDiagonalScale` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetDiagonalScale/> |
| `KSPGetDiagonalScaleFix` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetDiagonalScaleFix/> |
| `KSPGetDM` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetDM/> |
| `KSPGetErrorHistory` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetErrorHistory/> |
| `KSPGetErrorIfNotConverged` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetErrorIfNotConverged/> |
| `KSPGetGuess` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetGuess/> |
| `KSPGetInitialGuessKnoll` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetInitialGuessKnoll/> |
| `KSPGetInitialGuessNonzero` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetInitialGuessNonzero/> |
| `KSPGetIterationNumber` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetIterationNumber/> |
| `KSPGetMinimumIterations` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetMinimumIterations/> |
| `KSPGetMonitorContext` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetMonitorContext/> |
| `KSPGetNestLevel` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetNestLevel/> |
| `KSPGetNormType` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetNormType/> |
| `KSPGetOperators` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGetOperators/> |
| `KSPGetOperatorsSet` | Not Collective, though the results on all processes will be the same | <https://petsc.org/release/manualpages/KSP/KSPGetOperatorsSet/> |
| `KSPGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetOptionsPrefix/> |
| `KSPGetPC` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetPC/> |
| `KSPGetPCSide` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetPCSide/> |
| `KSPGetResidualHistory` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetResidualHistory/> |
| `KSPGetResidualNorm` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetResidualNorm/> |
| `KSPGetReusePreconditioner` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGetReusePreconditioner/> |
| `KSPGetRhs` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetRhs/> |
| `KSPGetSolution` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetSolution/> |
| `KSPGetTolerances` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetTolerances/> |
| `KSPGetTotalIterations` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetTotalIterations/> |
| `KSPGetType` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGetType/> |
| `KSPGLTRGetLambda` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGLTRGetLambda/> |
| `KSPGLTRGetMinEig` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGLTRGetMinEig/> |
| `KSPGMRESClassicalGramSchmidtOrthogonalization` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/KSP/KSPGMRESClassicalGramSchmidtOrthogonalization/> |
| `KSPGMRESGetCGSRefinementType` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESGetCGSRefinementType/> |
| `KSPGMRESGetOrthogonalization` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESGetOrthogonalization/> |
| `KSPGMRESGetRestart` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESGetRestart/> |
| `KSPGMRESModifiedGramSchmidtOrthogonalization` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/KSP/KSPGMRESModifiedGramSchmidtOrthogonalization/> |
| `KSPGMRESMonitorKrylov` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESMonitorKrylov/> |
| `KSPGMRESSetBreakdownTolerance` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESSetBreakdownTolerance/> |
| `KSPGMRESSetCGSRefinementType` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESSetCGSRefinementType/> |
| `KSPGMRESSetHapTol` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESSetHapTol/> |
| `KSPGMRESSetOrthogonalization` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESSetOrthogonalization/> |
| `KSPGMRESSetPreAllocateVectors` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESSetPreAllocateVectors/> |
| `KSPGMRESSetRestart` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGMRESSetRestart/> |
| `KSPGuessCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessCreate/> |
| `KSPGuessDestroy` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessDestroy/> |
| `KSPGuessFischerSetModel` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessFischerSetModel/> |
| `KSPGuessFormGuess` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessFormGuess/> |
| `KSPGuessGetType` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessGetType/> |
| `KSPGuessRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/KSP/KSPGuessRegister/> |
| `KSPGuessRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessRegisterAll/> |
| `KSPGuessSetFromOptions` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessSetFromOptions/> |
| `KSPGuessSetTolerance` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessSetTolerance/> |
| `KSPGuessSetType` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessSetType/> |
| `KSPGuessSetUp` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessSetUp/> |
| `KSPGuessUpdate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessUpdate/> |
| `KSPGuessView` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPGuessView/> |
| `KSPHPDDMSetType` | Collective | <https://petsc.org/release/manualpages/KSP/KSPHPDDMSetType/> |
| `KSPInitialResidual` | Collective | <https://petsc.org/release/manualpages/KSP/KSPInitialResidual/> |
| `KSPLGMRESSetAugDim` | Collective | <https://petsc.org/release/manualpages/KSP/KSPLGMRESSetAugDim/> |
| `KSPLGMRESSetConstant` | Collective | <https://petsc.org/release/manualpages/KSP/KSPLGMRESSetConstant/> |
| `KSPLoad` | Collective | <https://petsc.org/release/manualpages/KSP/KSPLoad/> |
| `KSPLSQRConvergedDefault` | Collective | <https://petsc.org/release/manualpages/KSP/KSPLSQRConvergedDefault/> |
| `KSPLSQRGetNorms` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPLSQRGetNorms/> |
| `KSPLSQRGetStandardErrorVec` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPLSQRGetStandardErrorVec/> |
| `KSPLSQRMonitorResidual` | Collective | <https://petsc.org/release/manualpages/KSP/KSPLSQRMonitorResidual/> |
| `KSPLSQRMonitorResidualDrawLG` | Collective | <https://petsc.org/release/manualpages/KSP/KSPLSQRMonitorResidualDrawLG/> |
| `KSPLSQRMonitorResidualDrawLGCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPLSQRMonitorResidualDrawLGCreate/> |
| `KSPLSQRSetComputeStandardErrorVec` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPLSQRSetComputeStandardErrorVec/> |
| `KSPLSQRSetExactMatNorm` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPLSQRSetExactMatNorm/> |
| `KSPMatRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPMatRegisterAll/> |
| `KSPMINRESGetUseQLP` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMINRESGetUseQLP/> |
| `KSPMINRESSetRadius` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMINRESSetRadius/> |
| `KSPMINRESSetUseQLP` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMINRESSetUseQLP/> |
| `KSPMonitor` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitor/> |
| `KSPMonitorCancel` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorCancel/> |
| `KSPMonitorDynamicTolerance` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorDynamicTolerance/> |
| `KSPMonitorDynamicToleranceCreate` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorDynamicToleranceCreate/> |
| `KSPMonitorDynamicToleranceSetCoefficient` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorDynamicToleranceSetCoefficient/> |
| `KSPMonitorError` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorError/> |
| `KSPMonitorErrorDraw` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorErrorDraw/> |
| `KSPMonitorErrorDrawLG` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorErrorDrawLG/> |
| `KSPMonitorErrorDrawLGCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorErrorDrawLGCreate/> |
| `KSPMonitorLGRange` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorLGRange/> |
| `KSPMonitorRegister` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorRegister/> |
| `KSPMonitorRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorRegisterAll/> |
| `KSPMonitorResidual` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorResidual/> |
| `KSPMonitorResidualDrawLG` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorResidualDrawLG/> |
| `KSPMonitorResidualDrawLGCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorResidualDrawLGCreate/> |
| `KSPMonitorResidualRange` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorResidualRange/> |
| `KSPMonitorResidualView` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorResidualView/> |
| `KSPMonitorSAWs` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSAWs/> |
| `KSPMonitorSAWsCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSAWsCreate/> |
| `KSPMonitorSAWsDestroy` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSAWsDestroy/> |
| `KSPMonitorSet` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSet/> |
| `KSPMonitorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSetFromOptions/> |
| `KSPMonitorSingularValue` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSingularValue/> |
| `KSPMonitorSingularValueCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSingularValueCreate/> |
| `KSPMonitorSolution` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSolution/> |
| `KSPMonitorSolutionDraw` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSolutionDraw/> |
| `KSPMonitorSolutionDrawLG` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSolutionDrawLG/> |
| `KSPMonitorSolutionDrawLGCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorSolutionDrawLGCreate/> |
| `KSPMonitorTrueResidual` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorTrueResidual/> |
| `KSPMonitorTrueResidualDrawLG` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorTrueResidualDrawLG/> |
| `KSPMonitorTrueResidualDrawLGCreate` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorTrueResidualDrawLGCreate/> |
| `KSPMonitorTrueResidualMax` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorTrueResidualMax/> |
| `KSPMonitorTrueResidualView` | Collective | <https://petsc.org/release/manualpages/KSP/KSPMonitorTrueResidualView/> |
| `KSPPIPEFCGGetMmax` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEFCGGetMmax/> |
| `KSPPIPEFCGGetNprealloc` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEFCGGetNprealloc/> |
| `KSPPIPEFCGGetTruncationType` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEFCGGetTruncationType/> |
| `KSPPIPEFCGSetMmax` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEFCGSetMmax/> |
| `KSPPIPEFCGSetNprealloc` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEFCGSetNprealloc/> |
| `KSPPIPEFCGSetTruncationType` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEFCGSetTruncationType/> |
| `KSPPIPEFGMRESSetShift` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEFGMRESSetShift/> |
| `KSPPIPEGCRGetMmax` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEGCRGetMmax/> |
| `KSPPIPEGCRGetNprealloc` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEGCRGetNprealloc/> |
| `KSPPIPEGCRGetTruncationType` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEGCRGetTruncationType/> |
| `KSPPIPEGCRGetUnrollW` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEGCRGetUnrollW/> |
| `KSPPIPEGCRSetMmax` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEGCRSetMmax/> |
| `KSPPIPEGCRSetNprealloc` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEGCRSetNprealloc/> |
| `KSPPIPEGCRSetTruncationType` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEGCRSetTruncationType/> |
| `KSPPIPEGCRSetUnrollW` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPPIPEGCRSetUnrollW/> |
| `KSPPythonGetType` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPPythonGetType/> |
| `KSPPythonSetType` | Collective | <https://petsc.org/release/manualpages/KSP/KSPPythonSetType/> |
| `KSPQCGGetQuadratic` | Collective | <https://petsc.org/release/manualpages/KSP/KSPQCGGetQuadratic/> |
| `KSPQCGGetTrialStepNorm` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPQCGGetTrialStepNorm/> |
| `KSPQCGSetTrustRegionRadius` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPQCGSetTrustRegionRadius/> |
| `KSPRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/KSP/KSPRegister/> |
| `KSPRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPRegisterAll/> |
| `KSPReset` | Collective | <https://petsc.org/release/manualpages/KSP/KSPReset/> |
| `KSPResetFromOptions` | Collective | <https://petsc.org/release/manualpages/KSP/KSPResetFromOptions/> |
| `KSPResetViewers` | Collective | <https://petsc.org/release/manualpages/KSP/KSPResetViewers/> |
| `KSPRichardsonSetScale` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPRichardsonSetScale/> |
| `KSPRichardsonSetSelfScale` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPRichardsonSetSelfScale/> |
| `KSPSetApplicationContext` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetApplicationContext/> |
| `KSPSetCheckNormIteration` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetCheckNormIteration/> |
| `KSPSetComputeEigenvalues` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetComputeEigenvalues/> |
| `KSPSetComputeInitialGuess` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetComputeInitialGuess/> |
| `KSPSetComputeOperators` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetComputeOperators/> |
| `KSPSetComputeRHS` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetComputeRHS/> |
| `KSPSetComputeRitz` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetComputeRitz/> |
| `KSPSetComputeSingularValues` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetComputeSingularValues/> |
| `KSPSetConvergedNegativeCurvature` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetConvergedNegativeCurvature/> |
| `KSPSetConvergenceTest` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetConvergenceTest/> |
| `KSPSetDiagonalScale` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetDiagonalScale/> |
| `KSPSetDiagonalScaleFix` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetDiagonalScaleFix/> |
| `KSPSetDM` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetDM/> |
| `KSPSetDMActive` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetDMActive/> |
| `KSPSetErrorHistory` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPSetErrorHistory/> |
| `KSPSetErrorIfNotConverged` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetErrorIfNotConverged/> |
| `KSPSetFromOptions` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetFromOptions/> |
| `KSPSetGuess` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetGuess/> |
| `KSPSetInitialGuessKnoll` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetInitialGuessKnoll/> |
| `KSPSetInitialGuessNonzero` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetInitialGuessNonzero/> |
| `KSPSetLagNorm` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetLagNorm/> |
| `KSPSetMatSolveBatchSize` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetMatSolveBatchSize/> |
| `KSPSetMinimumIterations` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetMinimumIterations/> |
| `KSPSetNestLevel` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetNestLevel/> |
| `KSPSetNormType` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetNormType/> |
| `KSPSetOperators` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetOperators/> |
| `KSPSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetOptionsPrefix/> |
| `KSPSetPC` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetPC/> |
| `KSPSetPCSide` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetPCSide/> |
| `KSPSetPostSolve` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetPostSolve/> |
| `KSPSetPreSolve` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetPreSolve/> |
| `KSPSetResidualHistory` | Not Collective | <https://petsc.org/release/manualpages/KSP/KSPSetResidualHistory/> |
| `KSPSetReusePreconditioner` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetReusePreconditioner/> |
| `KSPSetSkipPCSetFromOptions` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetSkipPCSetFromOptions/> |
| `KSPSetSupportedNorm` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetSupportedNorm/> |
| `KSPSetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetTolerances/> |
| `KSPSetType` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetType/> |
| `KSPSetUp` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetUp/> |
| `KSPSetUpOnBlocks` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetUpOnBlocks/> |
| `KSPSetUseExplicitTranspose` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetUseExplicitTranspose/> |
| `KSPSetUseFischerGuess` | Logically Collective | <https://petsc.org/release/manualpages/KSP/KSPSetUseFischerGuess/> |
| `KSPSetWorkVecs` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSetWorkVecs/> |
| `KSPSolve` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSolve/> |
| `KSPSolveTranspose` | Collective | <https://petsc.org/release/manualpages/KSP/KSPSolveTranspose/> |
| `KSPUnwindPreconditioner` | Collective | <https://petsc.org/release/manualpages/KSP/KSPUnwindPreconditioner/> |
| `KSPView` | Collective | <https://petsc.org/release/manualpages/KSP/KSPView/> |
| `KSPViewFromOptions` | Collective | <https://petsc.org/release/manualpages/KSP/KSPViewFromOptions/> |
| `MatCreateLMVMBadBroyden` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMBadBroyden/> |
| `MatCreateLMVMBFGS` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMBFGS/> |
| `MatCreateLMVMBroyden` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMBroyden/> |
| `MatCreateLMVMDBFGS` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMDBFGS/> |
| `MatCreateLMVMDDFP` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMDDFP/> |
| `MatCreateLMVMDFP` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMDFP/> |
| `MatCreateLMVMDiagBroyden` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMDiagBroyden/> |
| `MatCreateLMVMDQN` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMDQN/> |
| `MatCreateLMVMSR1` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMSR1/> |
| `MatCreateLMVMSymBadBroyden` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMSymBadBroyden/> |
| `MatCreateLMVMSymBroyden` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateLMVMSymBroyden/> |
| `MatCreateSchurComplement` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateSchurComplement/> |
| `MatCreateSchurComplementPmat` | Collective | <https://petsc.org/release/manualpages/KSP/MatCreateSchurComplementPmat/> |
| `MatGetSchurComplement` | Collective | <https://petsc.org/release/manualpages/KSP/MatGetSchurComplement/> |
| `MatLMVMGetHistorySize` | Not Collective | <https://petsc.org/release/manualpages/KSP/MatLMVMGetHistorySize/> |
| `MatLMVMGetLastUpdate` | Not collective | <https://petsc.org/release/manualpages/KSP/MatLMVMGetLastUpdate/> |
| `MatLMVMGetMultAlgorithm` | Not collective | <https://petsc.org/release/manualpages/KSP/MatLMVMGetMultAlgorithm/> |
| `MatLMVMSetMultAlgorithm` | Logically collective | <https://petsc.org/release/manualpages/KSP/MatLMVMSetMultAlgorithm/> |
| `MatSchurComplementComputeExplicitOperator` | Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementComputeExplicitOperator/> |
| `MatSchurComplementGetAinvType` | Not Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementGetAinvType/> |
| `MatSchurComplementGetKSP` | Not Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementGetKSP/> |
| `MatSchurComplementGetPmat` | Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementGetPmat/> |
| `MatSchurComplementGetSubMatrices` | Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementGetSubMatrices/> |
| `MatSchurComplementSetAinvType` | Not Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementSetAinvType/> |
| `MatSchurComplementSetKSP` | Not Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementSetKSP/> |
| `MatSchurComplementSetSubMatrices` | Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementSetSubMatrices/> |
| `MatSchurComplementUpdateSubMatrices` | Collective | <https://petsc.org/release/manualpages/KSP/MatSchurComplementUpdateSubMatrices/> |

## LANDAU

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMPlexLandauAccess` | Collective | <https://petsc.org/release/manualpages/LANDAU/DMPlexLandauAccess/> |
| `DMPlexLandauAddMaxwellians` | Collective | <https://petsc.org/release/manualpages/LANDAU/DMPlexLandauAddMaxwellians/> |
| `DMPlexLandauCreateMassMatrix` | Collective | <https://petsc.org/release/manualpages/LANDAU/DMPlexLandauCreateMassMatrix/> |
| `DMPlexLandauCreateVelocitySpace` | Collective | <https://petsc.org/release/manualpages/LANDAU/DMPlexLandauCreateVelocitySpace/> |
| `DMPlexLandauDestroyVelocitySpace` | Collective | <https://petsc.org/release/manualpages/LANDAU/DMPlexLandauDestroyVelocitySpace/> |
| `DMPlexLandauIFunction` | Collective | <https://petsc.org/release/manualpages/LANDAU/DMPlexLandauIFunction/> |
| `DMPlexLandauIJacobian` | Collective | <https://petsc.org/release/manualpages/LANDAU/DMPlexLandauIJacobian/> |
| `DMPlexLandauPrintNorms` | Collective | <https://petsc.org/release/manualpages/LANDAU/DMPlexLandauPrintNorms/> |
| `LandauKokkosCreateMatMaps` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/LANDAU/LandauKokkosCreateMatMaps/> |
| `LandauKokkosDestroyMatMaps` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/LANDAU/LandauKokkosDestroyMatMaps/> |
| `LandauKokkosJacobian` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/LANDAU/LandauKokkosJacobian/> |
| `LandauKokkosStaticDataClear` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/LANDAU/LandauKokkosStaticDataClear/> |
| `LandauKokkosStaticDataSet` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/LANDAU/LandauKokkosStaticDataSet/> |

## Log

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscAddLogDouble` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscAddLogDouble/> |
| `PetscAddLogDoubleCnt` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscAddLogDoubleCnt/> |
| `PetscClassIdRegister` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscClassIdRegister/> |
| `PetscGetFlops` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscGetFlops/> |
| `PetscInfo` | Collective | <https://petsc.org/release/manualpages/Log/PetscInfo/> |
| `PetscInfoActivateClass` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoActivateClass/> |
| `PetscInfoAllow` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoAllow/> |
| `PetscInfoDeactivateClass` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoDeactivateClass/> |
| `PetscInfoDestroy` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoDestroy/> |
| `PetscInfoEnabled` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoEnabled/> |
| `PetscInfoGetClass` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoGetClass/> |
| `PetscInfoGetFile` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscInfoGetFile/> |
| `PetscInfoGetInfo` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoGetInfo/> |
| `PetscInfoProcessClass` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoProcessClass/> |
| `PetscInfoSetClasses` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscInfoSetClasses/> |
| `PetscInfoSetFile` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoSetFile/> |
| `PetscInfoSetFilterCommSelf` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoSetFilterCommSelf/> |
| `PetscInfoSetFromOptions` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscInfoSetFromOptions/> |
| `PetscIntStackCreate` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscIntStackCreate/> |
| `PetscIntStackDestroy` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscIntStackDestroy/> |
| `PetscIntStackEmpty` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscIntStackEmpty/> |
| `PetscIntStackPop` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscIntStackPop/> |
| `PetscIntStackPush` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscIntStackPush/> |
| `PetscIntStackTop` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscIntStackTop/> |
| `PetscLogActions` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogActions/> |
| `PetscLogAllBegin` | Logically Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogAllBegin/> |
| `PetscLogClassGetClassId` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogClassGetClassId/> |
| `PetscLogClassIdGetName` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogClassIdGetName/> |
| `PetscLogCpuToGpu` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogCpuToGpu/> |
| `PetscLogCpuToGpuScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogCpuToGpuScalar/> |
| `PetscLogDefaultBegin` | Logically Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogDefaultBegin/> |
| `PetscLogDump` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogDump/> |
| `PetscLogEventActivate` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventActivate/> |
| `PetscLogEventActivateClass` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventActivateClass/> |
| `PetscLogEventBegin` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventBegin/> |
| `PetscLogEventDeactivate` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventDeactivate/> |
| `PetscLogEventDeactivateClass` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventDeactivateClass/> |
| `PetscLogEventDeactivatePop` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventDeactivatePop/> |
| `PetscLogEventDeactivatePush` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventDeactivatePush/> |
| `PetscLogEventEnd` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventEnd/> |
| `PetscLogEventExcludeClass` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventExcludeClass/> |
| `PetscLogEventGetId` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventGetId/> |
| `PetscLogEventGetName` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventGetName/> |
| `PetscLogEventIncludeClass` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventIncludeClass/> |
| `PetscLogEventRegister` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventRegister/> |
| `PetscLogEventSetActiveAll` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventSetActiveAll/> |
| `PetscLogEventSetCollective` | collective ) Logically Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventSetCollective/> |
| `PetscLogEventSetDof` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventSetDof/> |
| `PetscLogEventSetError` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventSetError/> |
| `PetscLogEventsPause` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogEventsPause/> |
| `PetscLogEventsResume` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogEventsResume/> |
| `PetscLogEventSync` | Collective | <https://petsc.org/release/manualpages/Log/PetscLogEventSync/> |
| `PetscLogFlops` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogFlops/> |
| `PetscLogGetDefaultHandler` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogGetDefaultHandler/> |
| `PetscLogGetState` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogGetState/> |
| `PetscLogGpuTimeAdd` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogGpuTimeAdd/> |
| `PetscLogGpuToCpu` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogGpuToCpu/> |
| `PetscLogGpuToCpuScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogGpuToCpuScalar/> |
| `PetscLogHandlerCreate` | Collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerCreate/> |
| `PetscLogHandlerCreateLegacy` | Collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerCreateLegacy/> |
| `PetscLogHandlerCreateTrace` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogHandlerCreateTrace/> |
| `PetscLogHandlerDestroy` | Logically collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerDestroy/> |
| `PetscLogHandlerDump` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerDump/> |
| `PetscLogHandlerEventBegin` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerEventBegin/> |
| `PetscLogHandlerEventDeactivatePop` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerEventDeactivatePop/> |
| `PetscLogHandlerEventDeactivatePush` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerEventDeactivatePush/> |
| `PetscLogHandlerEventEnd` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerEventEnd/> |
| `PetscLogHandlerEventsPause` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerEventsPause/> |
| `PetscLogHandlerEventsResume` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerEventsResume/> |
| `PetscLogHandlerEventSync` | Collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerEventSync/> |
| `PetscLogHandlerGetEventPerfInfo` | Not collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogHandlerGetEventPerfInfo/> |
| `PetscLogHandlerGetNumObjects` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerGetNumObjects/> |
| `PetscLogHandlerGetStagePerfInfo` | Not collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogHandlerGetStagePerfInfo/> |
| `PetscLogHandlerGetState` | Logically collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerGetState/> |
| `PetscLogHandlerGetType` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerGetType/> |
| `PetscLogHandlerLogObjectState` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogHandlerLogObjectState/> |
| `PetscLogHandlerObjectCreate` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerObjectCreate/> |
| `PetscLogHandlerObjectDestroy` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerObjectDestroy/> |
| `PetscLogHandlerRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogHandlerRegister/> |
| `PetscLogHandlerSetLogActions` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerSetLogActions/> |
| `PetscLogHandlerSetLogObjects` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerSetLogObjects/> |
| `PetscLogHandlerSetState` | Logically collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerSetState/> |
| `PetscLogHandlerStageGetVisible` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerStageGetVisible/> |
| `PetscLogHandlerStagePop` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerStagePop/> |
| `PetscLogHandlerStagePush` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerStagePush/> |
| `PetscLogHandlerStageSetVisible` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerStageSetVisible/> |
| `PetscLogHandlerStart` | Logically collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerStart/> |
| `PetscLogHandlerStop` | Logically collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerStop/> |
| `PetscLogHandlerView` | Collective | <https://petsc.org/release/manualpages/Log/PetscLogHandlerView/> |
| `PetscLogIsActive` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogIsActive/> |
| `PetscLogLegacyCallbacksBegin` | Logically Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogLegacyCallbacksBegin/> |
| `PetscLogMPEBegin` | Collective on PETSC_COMM_WORLD , No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogMPEBegin/> |
| `PetscLogMPEDump` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogMPEDump/> |
| `PetscLogNestedBegin` | Logically Collective on PETSC_COMM_WORLD , No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogNestedBegin/> |
| `PetscLogObjectCreate` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogObjectCreate/> |
| `PetscLogObjectDestroy` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogObjectDestroy/> |
| `PetscLogObjectParents` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogObjectParents/> |
| `PetscLogObjects` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogObjects/> |
| `PetscLogObjectState` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogObjectState/> |
| `PetscLogPerfstubsBegin` | Collective on PETSC_COMM_WORLD , No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogPerfstubsBegin/> |
| `PetscLogSetThreshold` | Logically Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogSetThreshold/> |
| `PetscLogStageGetActive` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStageGetActive/> |
| `PetscLogStageGetId` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStageGetId/> |
| `PetscLogStageGetName` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStageGetName/> |
| `PetscLogStageGetVisible` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStageGetVisible/> |
| `PetscLogStagePop` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStagePop/> |
| `PetscLogStagePush` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStagePush/> |
| `PetscLogStageRegister` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStageRegister/> |
| `PetscLogStageSetActive` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStageSetActive/> |
| `PetscLogStageSetVisible` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscLogStageSetVisible/> |
| `PetscLogStateClassGetInfo` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateClassGetInfo/> |
| `PetscLogStateClassRegister` | Logically collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogStateClassRegister/> |
| `PetscLogStateClassSetActive` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateClassSetActive/> |
| `PetscLogStateClassSetActiveAll` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateClassSetActiveAll/> |
| `PetscLogStateCreate` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateCreate/> |
| `PetscLogStateDestroy` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateDestroy/> |
| `PetscLogStateEventCurrentlyActive` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogStateEventCurrentlyActive/> |
| `PetscLogStateEventGetActive` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateEventGetActive/> |
| `PetscLogStateEventGetInfo` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateEventGetInfo/> |
| `PetscLogStateEventRegister` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateEventRegister/> |
| `PetscLogStateEventSetActive` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateEventSetActive/> |
| `PetscLogStateEventSetActiveAll` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateEventSetActiveAll/> |
| `PetscLogStateEventSetCollective` | collective ) Logically collective | <https://petsc.org/release/manualpages/Log/PetscLogStateEventSetCollective/> |
| `PetscLogStateGetClassFromClassId` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateGetClassFromClassId/> |
| `PetscLogStateGetClassFromName` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateGetClassFromName/> |
| `PetscLogStateGetCurrentStage` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateGetCurrentStage/> |
| `PetscLogStateGetEventFromName` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateGetEventFromName/> |
| `PetscLogStateGetNumClasses` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateGetNumClasses/> |
| `PetscLogStateGetNumEvents` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateGetNumEvents/> |
| `PetscLogStateGetNumStages` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateGetNumStages/> |
| `PetscLogStateGetStageFromName` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateGetStageFromName/> |
| `PetscLogStateStageEventIsActive` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogStateStageEventIsActive/> |
| `PetscLogStateStageGetActive` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateStageGetActive/> |
| `PetscLogStateStageGetInfo` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateStageGetInfo/> |
| `PetscLogStateStagePop` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateStagePop/> |
| `PetscLogStateStagePush` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateStagePush/> |
| `PetscLogStateStageRegister` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateStageRegister/> |
| `PetscLogStateStageSetActive` | Not collective | <https://petsc.org/release/manualpages/Log/PetscLogStateStageSetActive/> |
| `PetscLogTraceBegin` | Logically Collective on PETSC_COMM_WORLD , No Fortran Support | <https://petsc.org/release/manualpages/Log/PetscLogTraceBegin/> |
| `PetscLogView` | Collective | <https://petsc.org/release/manualpages/Log/PetscLogView/> |
| `PetscLogViewFromOptions` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Log/PetscLogViewFromOptions/> |
| `PetscPreLoadBegin` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscPreLoadBegin/> |
| `PetscPreLoadEnd` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscPreLoadEnd/> |
| `PetscPreLoadStage` | Not Collective | <https://petsc.org/release/manualpages/Log/PetscPreLoadStage/> |

## Mat

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `MatADot` | Collective | <https://petsc.org/release/manualpages/Mat/MatADot/> |
| `MatAIJGetLocalMat` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatAIJGetLocalMat/> |
| `MatANorm` | Collective | <https://petsc.org/release/manualpages/Mat/MatANorm/> |
| `MatAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatAppendOptionsPrefix/> |
| `MatAppendOptionsPrefixFactor` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatAppendOptionsPrefixFactor/> |
| `MatAssembled` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatAssembled/> |
| `MatAssemblyBegin` | Collective | <https://petsc.org/release/manualpages/Mat/MatAssemblyBegin/> |
| `MatAssemblyEnd` | Collective | <https://petsc.org/release/manualpages/Mat/MatAssemblyEnd/> |
| `MatAXPY` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatAXPY/> |
| `MatAYPX` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatAYPX/> |
| `MatBackwardSolve` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatBackwardSolve/> |
| `MatBindToCPU` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatBindToCPU/> |
| `MatBlockMatSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatBlockMatSetPreallocation/> |
| `MatCheckCompressedRow` | Collective | <https://petsc.org/release/manualpages/Mat/MatCheckCompressedRow/> |
| `MatCholeskyFactor` | Collective | <https://petsc.org/release/manualpages/Mat/MatCholeskyFactor/> |
| `MatCholeskyFactorNumeric` | Collective | <https://petsc.org/release/manualpages/Mat/MatCholeskyFactorNumeric/> |
| `MatCholeskyFactorSymbolic` | Collective | <https://petsc.org/release/manualpages/Mat/MatCholeskyFactorSymbolic/> |
| `MatColoringPatch` | Collective | <https://petsc.org/release/manualpages/Mat/MatColoringPatch/> |
| `MatCompositeAddMat` | Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeAddMat/> |
| `MatCompositeGetMat` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeGetMat/> |
| `MatCompositeGetMatStructure` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeGetMatStructure/> |
| `MatCompositeGetNumberMat` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeGetNumberMat/> |
| `MatCompositeGetType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeGetType/> |
| `MatCompositeMerge` | Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeMerge/> |
| `MatCompositeSetMatStructure` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeSetMatStructure/> |
| `MatCompositeSetMergeType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeSetMergeType/> |
| `MatCompositeSetScalings` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeSetScalings/> |
| `MatCompositeSetType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatCompositeSetType/> |
| `MatComputeBandwidth` | Collective | <https://petsc.org/release/manualpages/Mat/MatComputeBandwidth/> |
| `MatComputeOperator` | Collective | <https://petsc.org/release/manualpages/Mat/MatComputeOperator/> |
| `MatComputeOperatorTranspose` | Collective | <https://petsc.org/release/manualpages/Mat/MatComputeOperatorTranspose/> |
| `MatComputeVariableBlockEnvelope` | Collective | <https://petsc.org/release/manualpages/Mat/MatComputeVariableBlockEnvelope/> |
| `MatConjugate` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatConjugate/> |
| `MatConstantDiagonalGetConstant` | Not collective | <https://petsc.org/release/manualpages/Mat/MatConstantDiagonalGetConstant/> |
| `MatConvert` | Collective | <https://petsc.org/release/manualpages/Mat/MatConvert/> |
| `MatCopy` | Collective | <https://petsc.org/release/manualpages/Mat/MatCopy/> |
| `MatCopyHashToXAIJ` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatCopyHashToXAIJ/> |
| `MatCreate` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreate/> |
| `MatCreateAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateAIJ/> |
| `MatCreateAIJCUSPARSE` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateAIJCUSPARSE/> |
| `MatCreateAIJHIPSPARSE` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateAIJHIPSPARSE/> |
| `MatCreateAIJKokkos` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateAIJKokkos/> |
| `MatCreateAIJViennaCL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateAIJViennaCL/> |
| `MatCreateBAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateBAIJ/> |
| `MatCreateBAIJMKL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateBAIJMKL/> |
| `MatCreateBlockMat` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateBlockMat/> |
| `MatCreateCentering` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateCentering/> |
| `MatCreateComposite` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateComposite/> |
| `MatCreateConstantDiagonal` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateConstantDiagonal/> |
| `MatCreateDense` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateDense/> |
| `MatCreateDenseCUDA` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateDenseCUDA/> |
| `MatCreateDenseFromVecType` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateDenseFromVecType/> |
| `MatCreateDenseHIP` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateDenseHIP/> |
| `MatCreateDenseWithMemType` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateDenseWithMemType/> |
| `MatCreateDiagonal` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateDiagonal/> |
| `MatCreateFFT` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateFFT/> |
| `MatCreateFromOptions` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateFromOptions/> |
| `MatCreateFromParCSR` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateFromParCSR/> |
| `MatCreateGraph` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateGraph/> |
| `MatCreateHermitianTranspose` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateHermitianTranspose/> |
| `MatCreateHtoolFromKernel` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatCreateHtoolFromKernel/> |
| `MatCreateIS` | Collective. | <https://petsc.org/release/manualpages/Mat/MatCreateIS/> |
| `MatCreateKAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateKAIJ/> |
| `MatCreateLocalRef` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatCreateLocalRef/> |
| `MatCreateLRC` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateLRC/> |
| `MatCreateMAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMAIJ/> |
| `MatCreateMFFD` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMFFD/> |
| `MatCreateMPIAdj` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAdj/> |
| `MatCreateMPIAIJCRL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJCRL/> |
| `MatCreateMPIAIJMKL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJMKL/> |
| `MatCreateMPIAIJPERM` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJPERM/> |
| `MatCreateMPIAIJSELL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJSELL/> |
| `MatCreateMPIAIJSumSeqAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJSumSeqAIJ/> |
| `MatCreateMPIAIJSumSeqAIJNumeric` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJSumSeqAIJNumeric/> |
| `MatCreateMPIAIJSumSeqAIJSymbolic` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJSumSeqAIJSymbolic/> |
| `MatCreateMPIAIJWithArrays` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJWithArrays/> |
| `MatCreateMPIAIJWithSeqAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJWithSeqAIJ/> |
| `MatCreateMPIAIJWithSplitArrays` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIAIJWithSplitArrays/> |
| `MatCreateMPIBAIJWithArrays` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIBAIJWithArrays/> |
| `MatCreateMPIMatConcatenateSeqMat` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPIMatConcatenateSeqMat/> |
| `MatCreateMPISBAIJWithArrays` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateMPISBAIJWithArrays/> |
| `MatCreateNest` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateNest/> |
| `MatCreateNormal` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateNormal/> |
| `MatCreateNormalHermitian` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateNormalHermitian/> |
| `MatCreateRedundantMatrix` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateRedundantMatrix/> |
| `MatCreateSBAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSBAIJ/> |
| `MatCreateScaLAPACK` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateScaLAPACK/> |
| `MatCreateScatter` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateScatter/> |
| `MatCreateSELL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSELL/> |
| `MatCreateSELLCUDA` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSELLCUDA/> |
| `MatCreateSELLHIP` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSELLHIP/> |
| `MatCreateSeqAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJ/> |
| `MatCreateSeqAIJCRL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJCRL/> |
| `MatCreateSeqAIJCUSPARSE` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJCUSPARSE/> |
| `MatCreateSeqAIJFromTriple` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJFromTriple/> |
| `MatCreateSeqAIJHIPSPARSE` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJHIPSPARSE/> |
| `MatCreateSeqAIJKokkos` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJKokkos/> |
| `MatCreateSeqAIJMKL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJMKL/> |
| `MatCreateSeqAIJPERM` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJPERM/> |
| `MatCreateSeqAIJSELL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJSELL/> |
| `MatCreateSeqAIJViennaCL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJViennaCL/> |
| `MatCreateSeqAIJWithArrays` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqAIJWithArrays/> |
| `MatCreateSeqBAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqBAIJ/> |
| `MatCreateSeqBAIJWithArrays` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqBAIJWithArrays/> |
| `MatCreateSeqCUFFT` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqCUFFT/> |
| `MatCreateSeqDense` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqDense/> |
| `MatCreateSeqDenseCUDA` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqDenseCUDA/> |
| `MatCreateSeqDenseHIP` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqDenseHIP/> |
| `MatCreateSeqSBAIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqSBAIJ/> |
| `MatCreateSeqSBAIJWithArrays` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqSBAIJWithArrays/> |
| `MatCreateSeqSELL` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSeqSELL/> |
| `MatCreateShell` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateShell/> |
| `MatCreateSubMatrices` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSubMatrices/> |
| `MatCreateSubMatricesMPI` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSubMatricesMPI/> |
| `MatCreateSubMatrix` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSubMatrix/> |
| `MatCreateSubMatrixVirtual` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateSubMatrixVirtual/> |
| `MatCreateTranspose` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateTranspose/> |
| `MatCreateVecs` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateVecs/> |
| `MatCreateVecsFFTW` | Collective | <https://petsc.org/release/manualpages/Mat/MatCreateVecsFFTW/> |
| `MatCUSPARSESetFormat` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatCUSPARSESetFormat/> |
| `MatDenseCUDAGetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDAGetArray/> |
| `MatDenseCUDAGetArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDAGetArrayRead/> |
| `MatDenseCUDAGetArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDAGetArrayWrite/> |
| `MatDenseCUDAPlaceArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDAPlaceArray/> |
| `MatDenseCUDAReplaceArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDAReplaceArray/> |
| `MatDenseCUDAResetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDAResetArray/> |
| `MatDenseCUDARestoreArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDARestoreArray/> |
| `MatDenseCUDARestoreArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDARestoreArrayRead/> |
| `MatDenseCUDARestoreArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDARestoreArrayWrite/> |
| `MatDenseCUDASetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseCUDASetPreallocation/> |
| `MatDenseGetArray` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetArray/> |
| `MatDenseGetArrayAndMemType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetArrayAndMemType/> |
| `MatDenseGetArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetArrayRead/> |
| `MatDenseGetArrayReadAndMemType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetArrayReadAndMemType/> |
| `MatDenseGetArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetArrayWrite/> |
| `MatDenseGetArrayWriteAndMemType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetArrayWriteAndMemType/> |
| `MatDenseGetColumn` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetColumn/> |
| `MatDenseGetColumnVec` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetColumnVec/> |
| `MatDenseGetColumnVecRead` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetColumnVecRead/> |
| `MatDenseGetColumnVecWrite` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetColumnVecWrite/> |
| `MatDenseGetLDA` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetLDA/> |
| `MatDenseGetSubMatrix` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseGetSubMatrix/> |
| `MatDenseHIPGetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPGetArray/> |
| `MatDenseHIPGetArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPGetArrayRead/> |
| `MatDenseHIPGetArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPGetArrayWrite/> |
| `MatDenseHIPPlaceArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPPlaceArray/> |
| `MatDenseHIPReplaceArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPReplaceArray/> |
| `MatDenseHIPResetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPResetArray/> |
| `MatDenseHIPRestoreArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPRestoreArray/> |
| `MatDenseHIPRestoreArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPRestoreArrayRead/> |
| `MatDenseHIPRestoreArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPRestoreArrayWrite/> |
| `MatDenseHIPSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseHIPSetPreallocation/> |
| `MatDensePlaceArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDensePlaceArray/> |
| `MatDenseReplaceArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseReplaceArray/> |
| `MatDenseReplaceArrayWithMemType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseReplaceArrayWithMemType/> |
| `MatDenseResetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseResetArray/> |
| `MatDenseRestoreArray` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreArray/> |
| `MatDenseRestoreArrayAndMemType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreArrayAndMemType/> |
| `MatDenseRestoreArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreArrayRead/> |
| `MatDenseRestoreArrayReadAndMemType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreArrayReadAndMemType/> |
| `MatDenseRestoreArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreArrayWrite/> |
| `MatDenseRestoreArrayWriteAndMemType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreArrayWriteAndMemType/> |
| `MatDenseRestoreColumn` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreColumn/> |
| `MatDenseRestoreColumnVec` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreColumnVec/> |
| `MatDenseRestoreColumnVecRead` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreColumnVecRead/> |
| `MatDenseRestoreColumnVecWrite` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreColumnVecWrite/> |
| `MatDenseRestoreSubMatrix` | Collective | <https://petsc.org/release/manualpages/Mat/MatDenseRestoreSubMatrix/> |
| `MatDenseSetLDA` | Collective if the matrix layouts have not yet been setup | <https://petsc.org/release/manualpages/Mat/MatDenseSetLDA/> |
| `MatDestroy` | Collective | <https://petsc.org/release/manualpages/Mat/MatDestroy/> |
| `MatDestroyMatrices` | Collective | <https://petsc.org/release/manualpages/Mat/MatDestroyMatrices/> |
| `MatDestroySeqNonzeroStructure` | Collective | <https://petsc.org/release/manualpages/Mat/MatDestroySeqNonzeroStructure/> |
| `MatDestroySubMatrices` | Collective | <https://petsc.org/release/manualpages/Mat/MatDestroySubMatrices/> |
| `MatDiagonalScale` | Collective | <https://petsc.org/release/manualpages/Mat/MatDiagonalScale/> |
| `MatDiagonalScaleLocal` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatDiagonalScaleLocal/> |
| `MatDiagonalSet` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatDiagonalSet/> |
| `MatDiagonalSetDiagonal` | Collective | <https://petsc.org/release/manualpages/Mat/MatDiagonalSetDiagonal/> |
| `MatDuplicate` | Collective | <https://petsc.org/release/manualpages/Mat/MatDuplicate/> |
| `MatEliminateZeros` | Collective | <https://petsc.org/release/manualpages/Mat/MatEliminateZeros/> |
| `MatEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatEqual/> |
| `MatFactorClearError` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorClearError/> |
| `MatFactorCreateSchurComplement` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorCreateSchurComplement/> |
| `MatFactorFactorizeSchurComplement` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorFactorizeSchurComplement/> |
| `MatFactorGetCanUseOrdering` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorGetCanUseOrdering/> |
| `MatFactorGetError` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorGetError/> |
| `MatFactorGetErrorZeroPivot` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorGetErrorZeroPivot/> |
| `MatFactorGetPreferredOrdering` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorGetPreferredOrdering/> |
| `MatFactorGetSchurComplement` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorGetSchurComplement/> |
| `MatFactorGetSolverType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatFactorGetSolverType/> |
| `MatFactorInfoInitialize` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatFactorInfoInitialize/> |
| `MatFactorInvertSchurComplement` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorInvertSchurComplement/> |
| `MatFactorRestoreSchurComplement` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorRestoreSchurComplement/> |
| `MatFactorSetSchurIS` | Collective | <https://petsc.org/release/manualpages/Mat/MatFactorSetSchurIS/> |
| `MatFactorSolveSchurComplement` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorSolveSchurComplement/> |
| `MatFactorSolveSchurComplementTranspose` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatFactorSolveSchurComplementTranspose/> |
| `MatFDColoringSetValues` | Collective | <https://petsc.org/release/manualpages/Mat/MatFDColoringSetValues/> |
| `MatFindOffBlockDiagonalEntries` | Collective | <https://petsc.org/release/manualpages/Mat/MatFindOffBlockDiagonalEntries/> |
| `MatFindZeroDiagonals` | Collective | <https://petsc.org/release/manualpages/Mat/MatFindZeroDiagonals/> |
| `MatForwardSolve` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatForwardSolve/> |
| `MatGetBlockSize` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetBlockSize/> |
| `MatGetBlockSizes` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetBlockSizes/> |
| `MatGetBrowsOfAcols` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetBrowsOfAcols/> |
| `MatGetColumnIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetColumnIJ/> |
| `MatGetColumnVector` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetColumnVector/> |
| `MatGetCurrentMemType` | Not Collective, but the result will be the same on all MPI processes | <https://petsc.org/release/manualpages/Mat/MatGetCurrentMemType/> |
| `MatGetDiagonal` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetDiagonal/> |
| `MatGetDiagonalBlock` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetDiagonalBlock/> |
| `MatGetFactor` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetFactor/> |
| `MatGetFactorAvailable` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetFactorAvailable/> |
| `MatGetFactorType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetFactorType/> |
| `MatGetGhosts` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetGhosts/> |
| `MatGetInertia` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetInertia/> |
| `MatGetInfo` | Collective if MAT_GLOBAL_MAX or MAT_GLOBAL_SUM is used as the flag | <https://petsc.org/release/manualpages/Mat/MatGetInfo/> |
| `MatGetLayouts` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetLayouts/> |
| `MatGetLocalSize` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetLocalSize/> |
| `MatGetLocalSubMatrix` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetLocalSubMatrix/> |
| `MatGetLocalToGlobalMapping` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetLocalToGlobalMapping/> |
| `MatGetMultiProcBlock` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetMultiProcBlock/> |
| `MatGetNearNullSpace` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetNearNullSpace/> |
| `MatGetNonzeroState` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetNonzeroState/> |
| `MatGetNullSpace` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetNullSpace/> |
| `MatGetNullSpaces` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetNullSpaces/> |
| `MatGetOperation` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetOperation/> |
| `MatGetOption` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetOption/> |
| `MatGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetOptionsPrefix/> |
| `MatGetOwnershipIS` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetOwnershipIS/> |
| `MatGetOwnershipRange` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetOwnershipRange/> |
| `MatGetOwnershipRangeColumn` | Not Collective, unless matrix has not been allocated, then collective | <https://petsc.org/release/manualpages/Mat/MatGetOwnershipRangeColumn/> |
| `MatGetOwnershipRanges` | Not Collective, unless matrix has not been allocated | <https://petsc.org/release/manualpages/Mat/MatGetOwnershipRanges/> |
| `MatGetOwnershipRangesColumn` | Not Collective, unless matrix has not been allocated | <https://petsc.org/release/manualpages/Mat/MatGetOwnershipRangesColumn/> |
| `MatGetRow` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetRow/> |
| `MatGetRowIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetRowIJ/> |
| `MatGetRowMax` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetRowMax/> |
| `MatGetRowMaxAbs` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetRowMaxAbs/> |
| `MatGetRowMin` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetRowMin/> |
| `MatGetRowMinAbs` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetRowMinAbs/> |
| `MatGetRowSum` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetRowSum/> |
| `MatGetRowSumAbs` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetRowSumAbs/> |
| `MatGetRowUpperTriangular` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetRowUpperTriangular/> |
| `MatGetSeqNonzeroStructure` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetSeqNonzeroStructure/> |
| `MatGetSize` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetSize/> |
| `MatGetState` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetState/> |
| `MatGetTrace` | Collective | <https://petsc.org/release/manualpages/Mat/MatGetTrace/> |
| `MatGetTransposeNullSpace` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatGetTransposeNullSpace/> |
| `MatGetType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetType/> |
| `MatGetValue` | Not Collective; can only return a value owned by the given process | <https://petsc.org/release/manualpages/Mat/MatGetValue/> |
| `MatGetValues` | Not Collective; can only return values that are owned by the give process | <https://petsc.org/release/manualpages/Mat/MatGetValues/> |
| `MatGetValuesLocal` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetValuesLocal/> |
| `MatGetVariableBlockSizes` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatGetVariableBlockSizes/> |
| `MatGetVecType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatGetVecType/> |
| `MatH2OpusGetNativeMult` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatH2OpusGetNativeMult/> |
| `MatH2OpusSetNativeMult` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatH2OpusSetNativeMult/> |
| `MatHasCongruentLayouts` | Collective | <https://petsc.org/release/manualpages/Mat/MatHasCongruentLayouts/> |
| `MatHasOperation` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatHasOperation/> |
| `MatHeaderMerge` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatHeaderMerge/> |
| `MatHermitianTranspose` | Collective | <https://petsc.org/release/manualpages/Mat/MatHermitianTranspose/> |
| `MatHermitianTransposeGetMat` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatHermitianTransposeGetMat/> |
| `MatHIPSPARSESetFormat` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatHIPSPARSESetFormat/> |
| `MatHtoolSetKernel` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatHtoolSetKernel/> |
| `MatHYPREGetParCSR` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatHYPREGetParCSR/> |
| `MatHYPRESetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatHYPRESetPreallocation/> |
| `MatICCFactor` | Collective | <https://petsc.org/release/manualpages/Mat/MatICCFactor/> |
| `MatICCFactorSymbolic` | Collective | <https://petsc.org/release/manualpages/Mat/MatICCFactorSymbolic/> |
| `MatILUFactor` | Collective | <https://petsc.org/release/manualpages/Mat/MatILUFactor/> |
| `MatILUFactorSymbolic` | Collective | <https://petsc.org/release/manualpages/Mat/MatILUFactorSymbolic/> |
| `MatImaginaryPart` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatImaginaryPart/> |
| `MatIncreaseOverlap` | Collective | <https://petsc.org/release/manualpages/Mat/MatIncreaseOverlap/> |
| `MatIncreaseOverlapSplit` | Collective | <https://petsc.org/release/manualpages/Mat/MatIncreaseOverlapSplit/> |
| `MatInodeAdjustForInodes` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatInodeAdjustForInodes/> |
| `MatInodeGetInodeSizes` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatInodeGetInodeSizes/> |
| `MatInterpolate` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatInterpolate/> |
| `MatInterpolateAdd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatInterpolateAdd/> |
| `MatInvertBlockDiagonal` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatInvertBlockDiagonal/> |
| `MatInvertBlockDiagonalMat` | Collective | <https://petsc.org/release/manualpages/Mat/MatInvertBlockDiagonalMat/> |
| `MatInvertVariableBlockDiagonal` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatInvertVariableBlockDiagonal/> |
| `MatInvertVariableBlockEnvelope` | Collective | <https://petsc.org/release/manualpages/Mat/MatInvertVariableBlockEnvelope/> |
| `MatISFixLocalEmpty` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatISFixLocalEmpty/> |
| `MatISGetAllowRepeated` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatISGetAllowRepeated/> |
| `MatISGetLocalMat` | Not Collective. | <https://petsc.org/release/manualpages/Mat/MatISGetLocalMat/> |
| `MatISGetLocalToGlobalMapping` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatISGetLocalToGlobalMapping/> |
| `MatIsHermitian` | Collective | <https://petsc.org/release/manualpages/Mat/MatIsHermitian/> |
| `MatIsHermitianKnown` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatIsHermitianKnown/> |
| `MatIsHermitianTranspose` | Collective | <https://petsc.org/release/manualpages/Mat/MatIsHermitianTranspose/> |
| `MatIsLinear` | Collective | <https://petsc.org/release/manualpages/Mat/MatIsLinear/> |
| `MatISRestoreLocalMat` | Not Collective. | <https://petsc.org/release/manualpages/Mat/MatISRestoreLocalMat/> |
| `MatISSetAllowRepeated` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatISSetAllowRepeated/> |
| `MatISSetLocalMat` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatISSetLocalMat/> |
| `MatISSetLocalMatType` | Logically Collective. | <https://petsc.org/release/manualpages/Mat/MatISSetLocalMatType/> |
| `MatISSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatISSetPreallocation/> |
| `MatIsSPDKnown` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatIsSPDKnown/> |
| `MatISStoreL2L` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatISStoreL2L/> |
| `MatIsStructurallySymmetric` | Collective | <https://petsc.org/release/manualpages/Mat/MatIsStructurallySymmetric/> |
| `MatIsStructurallySymmetricKnown` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatIsStructurallySymmetricKnown/> |
| `MatIsSymmetric` | Collective | <https://petsc.org/release/manualpages/Mat/MatIsSymmetric/> |
| `MatIsSymmetricKnown` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatIsSymmetricKnown/> |
| `MatIsTranspose` | Collective | <https://petsc.org/release/manualpages/Mat/MatIsTranspose/> |
| `MatKAIJGetAIJ` | Not Collective, but if the MATKAIJ matrix is parallel, the MATAIJ matrix is also parallel | <https://petsc.org/release/manualpages/Mat/MatKAIJGetAIJ/> |
| `MatKAIJGetS` | Not Collective; the entire S is stored and returned independently on all processes. | <https://petsc.org/release/manualpages/Mat/MatKAIJGetS/> |
| `MatKAIJGetScaledIdentity` | Logically Collective. | <https://petsc.org/release/manualpages/Mat/MatKAIJGetScaledIdentity/> |
| `MatKAIJGetSRead` | Not Collective; the entire S is stored and returned independently on all processes. | <https://petsc.org/release/manualpages/Mat/MatKAIJGetSRead/> |
| `MatKAIJGetT` | Not Collective; the entire T is stored and returned independently on all processes | <https://petsc.org/release/manualpages/Mat/MatKAIJGetT/> |
| `MatKAIJGetTRead` | Not Collective; the entire T is stored and returned independently on all processes | <https://petsc.org/release/manualpages/Mat/MatKAIJGetTRead/> |
| `MatKAIJRestoreS` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatKAIJRestoreS/> |
| `MatKAIJRestoreSRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatKAIJRestoreSRead/> |
| `MatKAIJRestoreT` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatKAIJRestoreT/> |
| `MatKAIJRestoreTRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatKAIJRestoreTRead/> |
| `MatKAIJSetAIJ` | Logically Collective; if the MATAIJ matrix is parallel, the MATKAIJ matrix is also parallel | <https://petsc.org/release/manualpages/Mat/MatKAIJSetAIJ/> |
| `MatKAIJSetS` | Logically Collective; the entire S is stored independently on all processes. | <https://petsc.org/release/manualpages/Mat/MatKAIJSetS/> |
| `MatKAIJSetT` | Logically Collective; the entire T is stored independently on all processes. | <https://petsc.org/release/manualpages/Mat/MatKAIJSetT/> |
| `MatLoad` | Collective | <https://petsc.org/release/manualpages/Mat/MatLoad/> |
| `MatLRCGetMats` | Not collective | <https://petsc.org/release/manualpages/Mat/MatLRCGetMats/> |
| `MatLRCSetMats` | Logically collective | <https://petsc.org/release/manualpages/Mat/MatLRCSetMats/> |
| `MatLUFactor` | Collective | <https://petsc.org/release/manualpages/Mat/MatLUFactor/> |
| `MatLUFactorNumeric` | Collective | <https://petsc.org/release/manualpages/Mat/MatLUFactorNumeric/> |
| `MatLUFactorSymbolic` | Collective | <https://petsc.org/release/manualpages/Mat/MatLUFactorSymbolic/> |
| `MatMAIJGetAIJ` | Not Collective, but if the MATMAIJ matrix is parallel, the MATAIJ matrix is also parallel | <https://petsc.org/release/manualpages/Mat/MatMAIJGetAIJ/> |
| `MatMAIJRedimension` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMAIJRedimension/> |
| `MatMatInterpolate` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatInterpolate/> |
| `MatMatInterpolateAdd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatInterpolateAdd/> |
| `MatMatMatMult` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatMatMult/> |
| `MatMatMult` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatMult/> |
| `MatMatMultEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatMatMultEqual/> |
| `MatMatRestrict` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatRestrict/> |
| `MatMatSolve` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatSolve/> |
| `MatMatSolveTranspose` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatSolveTranspose/> |
| `MatMatTransposeMult` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatTransposeMult/> |
| `MatMatTransposeMultEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatMatTransposeMultEqual/> |
| `MatMatTransposeSolve` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMatTransposeSolve/> |
| `MatMFFDCheckPositivity` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDCheckPositivity/> |
| `MatMFFDGetH` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDGetH/> |
| `MatMFFDRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatMFFDRegister/> |
| `MatMFFDRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDRegisterAll/> |
| `MatMFFDResetHHistory` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDResetHHistory/> |
| `MatMFFDSetBase` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetBase/> |
| `MatMFFDSetCheckh` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetCheckh/> |
| `MatMFFDSetFunction` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetFunction/> |
| `MatMFFDSetFunctionError` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetFunctionError/> |
| `MatMFFDSetFunctioni` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetFunctioni/> |
| `MatMFFDSetFunctioniBase` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetFunctioniBase/> |
| `MatMFFDSetHHistory` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetHHistory/> |
| `MatMFFDSetOptionsPrefix` | Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetOptionsPrefix/> |
| `MatMFFDSetPeriod` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMFFDSetPeriod/> |
| `MatMkl_CPardisoSetCntl` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMkl_CPardisoSetCntl/> |
| `MatMkl_PardisoSetCntl` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMkl_PardisoSetCntl/> |
| `MatMPIAdjCreateNonemptySubcommMat` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAdjCreateNonemptySubcommMat/> |
| `MatMPIAdjSetPreallocation` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAdjSetPreallocation/> |
| `MatMPIAdjToSeq` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAdjToSeq/> |
| `MatMPIAdjToSeqRankZero` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAdjToSeqRankZero/> |
| `MatMPIAIJGetLocalMat` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAIJGetLocalMat/> |
| `MatMPIAIJGetLocalMatCondensed` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAIJGetLocalMatCondensed/> |
| `MatMPIAIJGetLocalMatMerge` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAIJGetLocalMatMerge/> |
| `MatMPIAIJGetNumberNonzeros` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAIJGetNumberNonzeros/> |
| `MatMPIAIJGetSeqAIJ` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAIJGetSeqAIJ/> |
| `MatMPIAIJSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAIJSetPreallocation/> |
| `MatMPIAIJSetPreallocationCSR` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAIJSetPreallocationCSR/> |
| `MatMPIAIJSetUseScalableIncreaseOverlap` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPIAIJSetUseScalableIncreaseOverlap/> |
| `MatMPIBAIJGetSeqBAIJ` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMPIBAIJGetSeqBAIJ/> |
| `MatMPIBAIJSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPIBAIJSetPreallocation/> |
| `MatMPIBAIJSetPreallocationCSR` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPIBAIJSetPreallocationCSR/> |
| `MatMPIBAIJSetValuesBlocked` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPIBAIJSetValuesBlocked/> |
| `MatMPIDenseSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPIDenseSetPreallocation/> |
| `MatMPISBAIJSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPISBAIJSetPreallocation/> |
| `MatMPISBAIJSetPreallocationCSR` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPISBAIJSetPreallocationCSR/> |
| `MatMPISELLGetLocalMatCondensed` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMPISELLGetLocalMatCondensed/> |
| `MatMPISELLGetSeqSELL` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatMPISELLGetSeqSELL/> |
| `MatMPISELLSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatMPISELLSetPreallocation/> |
| `MatMult` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMult/> |
| `MatMultAdd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMultAdd/> |
| `MatMultAddEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatMultAddEqual/> |
| `MatMultDiagonalBlock` | Collective | <https://petsc.org/release/manualpages/Mat/MatMultDiagonalBlock/> |
| `MatMultEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatMultEqual/> |
| `MatMultHermitianTranspose` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMultHermitianTranspose/> |
| `MatMultHermitianTransposeAdd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMultHermitianTransposeAdd/> |
| `MatMultHermitianTransposeAddEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatMultHermitianTransposeAddEqual/> |
| `MatMultHermitianTransposeEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatMultHermitianTransposeEqual/> |
| `MatMultTranspose` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMultTranspose/> |
| `MatMultTransposeAdd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatMultTransposeAdd/> |
| `MatMultTransposeAddEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatMultTransposeAddEqual/> |
| `MatMultTransposeEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatMultTransposeEqual/> |
| `MatMumpsGetCntl` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetCntl/> |
| `MatMumpsGetIcntl` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetIcntl/> |
| `MatMumpsGetInfo` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetInfo/> |
| `MatMumpsGetInfog` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetInfog/> |
| `MatMumpsGetInverse` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetInverse/> |
| `MatMumpsGetInverseTranspose` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetInverseTranspose/> |
| `MatMumpsGetNullPivots` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetNullPivots/> |
| `MatMumpsGetOocTmpDir` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetOocTmpDir/> |
| `MatMumpsGetRinfo` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetRinfo/> |
| `MatMumpsGetRinfog` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsGetRinfog/> |
| `MatMumpsSetBlk` | Not collective, only relevant on the first process of the MPI communicator | <https://petsc.org/release/manualpages/Mat/MatMumpsSetBlk/> |
| `MatMumpsSetCntl` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsSetCntl/> |
| `MatMumpsSetIcntl` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsSetIcntl/> |
| `MatMumpsSetOocTmpDir` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatMumpsSetOocTmpDir/> |
| `MatNestGetISs` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatNestGetISs/> |
| `MatNestGetLocalISs` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatNestGetLocalISs/> |
| `MatNestGetSize` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatNestGetSize/> |
| `MatNestGetSubMat` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatNestGetSubMat/> |
| `MatNestGetSubMats` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatNestGetSubMats/> |
| `MatNestSetSubMat` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatNestSetSubMat/> |
| `MatNestSetSubMats` | Collective | <https://petsc.org/release/manualpages/Mat/MatNestSetSubMats/> |
| `MatNestSetVecType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatNestSetVecType/> |
| `MatNorm` | Collective | <https://petsc.org/release/manualpages/Mat/MatNorm/> |
| `MatNormalGetMat` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatNormalGetMat/> |
| `MatNormalHermitianGetMat` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatNormalHermitianGetMat/> |
| `MatNullSpaceCreate` | Collective | <https://petsc.org/release/manualpages/Mat/MatNullSpaceCreate/> |
| `MatNullSpaceCreateRigidBody` | Collective | <https://petsc.org/release/manualpages/Mat/MatNullSpaceCreateRigidBody/> |
| `MatNullSpaceDestroy` | Collective | <https://petsc.org/release/manualpages/Mat/MatNullSpaceDestroy/> |
| `MatNullSpaceGetVecs` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatNullSpaceGetVecs/> |
| `MatNullSpaceRemove` | Collective | <https://petsc.org/release/manualpages/Mat/MatNullSpaceRemove/> |
| `MatNullSpaceSetFunction` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatNullSpaceSetFunction/> |
| `MatNullSpaceTest` | Collective | <https://petsc.org/release/manualpages/Mat/MatNullSpaceTest/> |
| `MatNullSpaceView` | Collective | <https://petsc.org/release/manualpages/Mat/MatNullSpaceView/> |
| `MatPermute` | Collective | <https://petsc.org/release/manualpages/Mat/MatPermute/> |
| `MatPreallocateBegin` | Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateBegin/> |
| `MatPreallocateEnd` | Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateEnd/> |
| `MatPreallocateLocation` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateLocation/> |
| `MatPreallocateSet` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateSet/> |
| `MatPreallocateSetLocal` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateSetLocal/> |
| `MatPreallocateSetLocalBlock` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateSetLocalBlock/> |
| `MatPreallocateSetLocalRemoveDups` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateSetLocalRemoveDups/> |
| `MatPreallocateSymmetricSetBlock` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateSymmetricSetBlock/> |
| `MatPreallocateSymmetricSetLocalBlock` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPreallocateSymmetricSetLocalBlock/> |
| `MatProductClear` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductClear/> |
| `MatProductCreate` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductCreate/> |
| `MatProductCreateWithMat` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductCreateWithMat/> |
| `MatProductGetAlgorithm` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatProductGetAlgorithm/> |
| `MatProductGetMats` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatProductGetMats/> |
| `MatProductGetType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatProductGetType/> |
| `MatProductNumeric` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductNumeric/> |
| `MatProductReplaceMats` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductReplaceMats/> |
| `MatProductSetAlgorithm` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductSetAlgorithm/> |
| `MatProductSetFill` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductSetFill/> |
| `MatProductSetFromOptions` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatProductSetFromOptions/> |
| `MatProductSetType` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductSetType/> |
| `MatProductSymbolic` | Collective | <https://petsc.org/release/manualpages/Mat/MatProductSymbolic/> |
| `MatProductView` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatProductView/> |
| `MatPropagateSymmetryOptions` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPropagateSymmetryOptions/> |
| `MatPtAP` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatPtAP/> |
| `MatPtAPMultEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatPtAPMultEqual/> |
| `MatPythonCreate` | Collective | <https://petsc.org/release/manualpages/Mat/MatPythonCreate/> |
| `MatPythonGetType` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatPythonGetType/> |
| `MatPythonSetType` | Collective | <https://petsc.org/release/manualpages/Mat/MatPythonSetType/> |
| `MatQRFactor` | Collective | <https://petsc.org/release/manualpages/Mat/MatQRFactor/> |
| `MatQRFactorNumeric` | Collective | <https://petsc.org/release/manualpages/Mat/MatQRFactorNumeric/> |
| `MatQRFactorSymbolic` | Collective | <https://petsc.org/release/manualpages/Mat/MatQRFactorSymbolic/> |
| `MatRARt` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatRARt/> |
| `MatRARtMultEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatRARtMultEqual/> |
| `MatRealPart` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatRealPart/> |
| `MatRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatRegister/> |
| `MatRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatRegisterAll/> |
| `MatReorderForNonzeroDiagonal` | Collective | <https://petsc.org/release/manualpages/Mat/MatReorderForNonzeroDiagonal/> |
| `MatReorderingSeqSBAIJ` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatReorderingSeqSBAIJ/> |
| `MatResetHash` | Collective | <https://petsc.org/release/manualpages/Mat/MatResetHash/> |
| `MatResetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatResetPreallocation/> |
| `MatResidual` | Collective | <https://petsc.org/release/manualpages/Mat/MatResidual/> |
| `MatRestoreColumnIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatRestoreColumnIJ/> |
| `MatRestoreLocalSubMatrix` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatRestoreLocalSubMatrix/> |
| `MatRestoreNullSpaces` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatRestoreNullSpaces/> |
| `MatRestoreRow` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatRestoreRow/> |
| `MatRestoreRowIJ` | Collective | <https://petsc.org/release/manualpages/Mat/MatRestoreRowIJ/> |
| `MatRestoreRowUpperTriangular` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatRestoreRowUpperTriangular/> |
| `MatRestrict` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatRestrict/> |
| `MatScaLAPACKGetBlockSizes` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatScaLAPACKGetBlockSizes/> |
| `MatScaLAPACKSetBlockSizes` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatScaLAPACKSetBlockSizes/> |
| `MatScale` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatScale/> |
| `MatScatterGetVecScatter` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatScatterGetVecScatter/> |
| `MatScatterSetVecScatter` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatScatterSetVecScatter/> |
| `MatSelectVariableBlockSizes` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSelectVariableBlockSizes/> |
| `MatSeqAIJCUSPARSEGetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJCUSPARSEGetArray/> |
| `MatSeqAIJCUSPARSEGetArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJCUSPARSEGetArrayRead/> |
| `MatSeqAIJCUSPARSEGetArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJCUSPARSEGetArrayWrite/> |
| `MatSeqAIJCUSPARSEGetIJ` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJCUSPARSEGetIJ/> |
| `MatSeqAIJCUSPARSERestoreArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJCUSPARSERestoreArray/> |
| `MatSeqAIJCUSPARSERestoreArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJCUSPARSERestoreArrayRead/> |
| `MatSeqAIJCUSPARSERestoreArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJCUSPARSERestoreArrayWrite/> |
| `MatSeqAIJCUSPARSERestoreIJ` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJCUSPARSERestoreIJ/> |
| `MatSeqAIJGetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJGetArray/> |
| `MatSeqAIJGetArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJGetArrayRead/> |
| `MatSeqAIJGetArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJGetArrayWrite/> |
| `MatSeqAIJGetCSRAndMemType` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatSeqAIJGetCSRAndMemType/> |
| `MatSeqAIJGetMaxRowNonzeros` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJGetMaxRowNonzeros/> |
| `MatSeqAIJHIPSPARSEGetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJHIPSPARSEGetArray/> |
| `MatSeqAIJHIPSPARSEGetArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJHIPSPARSEGetArrayRead/> |
| `MatSeqAIJHIPSPARSEGetArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJHIPSPARSEGetArrayWrite/> |
| `MatSeqAIJHIPSPARSEGetIJ` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJHIPSPARSEGetIJ/> |
| `MatSeqAIJHIPSPARSERestoreArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJHIPSPARSERestoreArray/> |
| `MatSeqAIJHIPSPARSERestoreArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJHIPSPARSERestoreArrayRead/> |
| `MatSeqAIJHIPSPARSERestoreArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJHIPSPARSERestoreArrayWrite/> |
| `MatSeqAIJHIPSPARSERestoreIJ` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJHIPSPARSERestoreIJ/> |
| `MatSeqAIJRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatSeqAIJRegister/> |
| `MatSeqAIJRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJRegisterAll/> |
| `MatSeqAIJRestoreArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJRestoreArray/> |
| `MatSeqAIJRestoreArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJRestoreArrayRead/> |
| `MatSeqAIJRestoreArrayWrite` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJRestoreArrayWrite/> |
| `MatSeqAIJSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJSetPreallocation/> |
| `MatSeqAIJSetType` | Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJSetType/> |
| `MatSeqAIJSetValuesLocalFast` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqAIJSetValuesLocalFast/> |
| `MatSeqBAIJGetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqBAIJGetArray/> |
| `MatSeqBAIJRestoreArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqBAIJRestoreArray/> |
| `MatSeqBAIJSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatSeqBAIJSetPreallocation/> |
| `MatSeqBAIJSetPreallocationCSR` | Collective | <https://petsc.org/release/manualpages/Mat/MatSeqBAIJSetPreallocationCSR/> |
| `MatSeqDenseInvert` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqDenseInvert/> |
| `MatSeqDenseSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatSeqDenseSetPreallocation/> |
| `MatSeqSBAIJGetArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSBAIJGetArray/> |
| `MatSeqSBAIJRestoreArray` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSBAIJRestoreArray/> |
| `MatSeqSBAIJSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSBAIJSetPreallocation/> |
| `MatSeqSELLGetAvgSliceWidth` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSELLGetAvgSliceWidth/> |
| `MatSeqSELLGetFillRatio` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSELLGetFillRatio/> |
| `MatSeqSELLGetMaxSliceWidth` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSELLGetMaxSliceWidth/> |
| `MatSeqSELLGetVarSliceSize` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSELLGetVarSliceSize/> |
| `MatSeqSELLSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSELLSetPreallocation/> |
| `MatSeqSELLSetSliceHeight` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSeqSELLSetSliceHeight/> |
| `MatSetBlockSize` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetBlockSize/> |
| `MatSetBlockSizes` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetBlockSizes/> |
| `MatSetBlockSizesFromMats` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetBlockSizesFromMats/> |
| `MatSetErrorIfFailure` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetErrorIfFailure/> |
| `MatSetFactorType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetFactorType/> |
| `MatSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetFromOptions/> |
| `MatSetHPL` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetHPL/> |
| `MatSetInf` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetInf/> |
| `MatSetLayouts` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetLayouts/> |
| `MatSetLocalToGlobalMapping` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetLocalToGlobalMapping/> |
| `MatSetNearNullSpace` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetNearNullSpace/> |
| `MatSetNullSpace` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetNullSpace/> |
| `MatSetOperation` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetOperation/> |
| `MatSetOption` | Logically Collective for certain operations, such as MAT_SPD , not collective for MAT_ROW_ORIENTED , see MatOption | <https://petsc.org/release/manualpages/Mat/MatSetOption/> |
| `MatSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetOptionsPrefix/> |
| `MatSetOptionsPrefixFactor` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetOptionsPrefixFactor/> |
| `MatSetPreallocationCOO` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetPreallocationCOO/> |
| `MatSetPreallocationCOOLocal` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetPreallocationCOOLocal/> |
| `MatSetRandom` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetRandom/> |
| `MatSetSizes` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetSizes/> |
| `MatSetStencil` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetStencil/> |
| `MatSetTransposeNullSpace` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetTransposeNullSpace/> |
| `MatSetType` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetType/> |
| `MatSetUnfactored` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSetUnfactored/> |
| `MatSetUp` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetUp/> |
| `MatSetValue` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValue/> |
| `MatSetValueLocal` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValueLocal/> |
| `MatSetValues` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValues/> |
| `MatSetValuesBatch` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesBatch/> |
| `MatSetValuesBlocked` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesBlocked/> |
| `MatSetValuesBlockedLocal` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesBlockedLocal/> |
| `MatSetValuesBlockedStencil` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesBlockedStencil/> |
| `MatSetValuesCOO` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesCOO/> |
| `MatSetValuesIS` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesIS/> |
| `MatSetValuesLocal` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesLocal/> |
| `MatSetValuesRow` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesRow/> |
| `MatSetValuesRowLocal` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesRowLocal/> |
| `MatSetValuesStencil` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetValuesStencil/> |
| `MatSetVariableBlockSizes` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatSetVariableBlockSizes/> |
| `MatSetVecType` | Collective | <https://petsc.org/release/manualpages/Mat/MatSetVecType/> |
| `MatShellGetContext` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatShellGetContext/> |
| `MatShellGetOperation` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatShellGetOperation/> |
| `MatShellGetScalingShifts` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatShellGetScalingShifts/> |
| `MatShellSetContext` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatShellSetContext/> |
| `MatShellSetContextDestroy` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatShellSetContextDestroy/> |
| `MatShellSetManageScalingShifts` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatShellSetManageScalingShifts/> |
| `MatShellSetMatProductOperation` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatShellSetMatProductOperation/> |
| `MatShellSetOperation` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatShellSetOperation/> |
| `MatShellSetVecType` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatShellSetVecType/> |
| `MatShellTestMult` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatShellTestMult/> |
| `MatShellTestMultTranspose` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatShellTestMultTranspose/> |
| `MatShift` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatShift/> |
| `MatSolve` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatSolve/> |
| `MatSolveAdd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatSolveAdd/> |
| `MatSolverTypeRegister` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Mat/MatSolverTypeRegister/> |
| `MatSolves` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatSolves/> |
| `MatSolveTranspose` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatSolveTranspose/> |
| `MatSolveTransposeAdd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatSolveTransposeAdd/> |
| `MatSOR` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatSOR/> |
| `MatStashGetInfo` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatStashGetInfo/> |
| `MatStashSetInitialSize` | Not Collective | <https://petsc.org/release/manualpages/Mat/MatStashSetInitialSize/> |
| `MatSTRUMPACKGetColPerm` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetColPerm/> |
| `MatSTRUMPACKGetCompAbsTol` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetCompAbsTol/> |
| `MatSTRUMPACKGetCompButterflyLevels` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetCompButterflyLevels/> |
| `MatSTRUMPACKGetCompLeafSize` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetCompLeafSize/> |
| `MatSTRUMPACKGetCompLossyPrecision` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetCompLossyPrecision/> |
| `MatSTRUMPACKGetCompMinSepSize` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetCompMinSepSize/> |
| `MatSTRUMPACKGetCompRelTol` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetCompRelTol/> |
| `MatSTRUMPACKGetGPU` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetGPU/> |
| `MatSTRUMPACKGetReordering` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKGetReordering/> |
| `MatSTRUMPACKSetColPerm` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetColPerm/> |
| `MatSTRUMPACKSetCompAbsTol` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetCompAbsTol/> |
| `MatSTRUMPACKSetCompButterflyLevels` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetCompButterflyLevels/> |
| `MatSTRUMPACKSetCompLeafSize` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetCompLeafSize/> |
| `MatSTRUMPACKSetCompLossyPrecision` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetCompLossyPrecision/> |
| `MatSTRUMPACKSetCompMinSepSize` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetCompMinSepSize/> |
| `MatSTRUMPACKSetCompRelTol` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetCompRelTol/> |
| `MatSTRUMPACKSetGeometricComponents` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetGeometricComponents/> |
| `MatSTRUMPACKSetGeometricNxyz` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetGeometricNxyz/> |
| `MatSTRUMPACKSetGeometricWidth` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetGeometricWidth/> |
| `MatSTRUMPACKSetGPU` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetGPU/> |
| `MatSTRUMPACKSetReordering` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSTRUMPACKSetReordering/> |
| `MatSubdomainsCreateCoalesce` | Collective | <https://petsc.org/release/manualpages/Mat/MatSubdomainsCreateCoalesce/> |
| `MatSubMatrixVirtualUpdate` | Collective | <https://petsc.org/release/manualpages/Mat/MatSubMatrixVirtualUpdate/> |
| `MatSuperluDistGetDiagU` | Collective | <https://petsc.org/release/manualpages/Mat/MatSuperluDistGetDiagU/> |
| `MatSuperluSetILUDropTol` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatSuperluSetILUDropTol/> |
| `MatTransColoringApplyDenToSp` | Collective | <https://petsc.org/release/manualpages/Mat/MatTransColoringApplyDenToSp/> |
| `MatTransColoringApplySpToDen` | Collective | <https://petsc.org/release/manualpages/Mat/MatTransColoringApplySpToDen/> |
| `MatTranspose` | Collective | <https://petsc.org/release/manualpages/Mat/MatTranspose/> |
| `MatTransposeColoringCreate` | Collective | <https://petsc.org/release/manualpages/Mat/MatTransposeColoringCreate/> |
| `MatTransposeColoringDestroy` | Collective | <https://petsc.org/release/manualpages/Mat/MatTransposeColoringDestroy/> |
| `MatTransposeGetMat` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatTransposeGetMat/> |
| `MatTransposeMatMult` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Mat/MatTransposeMatMult/> |
| `MatTransposeMatMultEqual` | Collective | <https://petsc.org/release/manualpages/Mat/MatTransposeMatMultEqual/> |
| `MatTransposeSetPrecursor` | Collective | <https://petsc.org/release/manualpages/Mat/MatTransposeSetPrecursor/> |
| `MatTransposeSymbolic` | Collective | <https://petsc.org/release/manualpages/Mat/MatTransposeSymbolic/> |
| `MatUpdateMPIAIJWithArray` | Collective | <https://petsc.org/release/manualpages/Mat/MatUpdateMPIAIJWithArray/> |
| `MatUpdateMPIAIJWithArrays` | Collective | <https://petsc.org/release/manualpages/Mat/MatUpdateMPIAIJWithArrays/> |
| `MatView` | Collective on viewer | <https://petsc.org/release/manualpages/Mat/MatView/> |
| `MatViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Mat/MatViewFromOptions/> |
| `MatXAIJSetPreallocation` | Collective | <https://petsc.org/release/manualpages/Mat/MatXAIJSetPreallocation/> |
| `MatZeroEntries` | Logically Collective | <https://petsc.org/release/manualpages/Mat/MatZeroEntries/> |
| `MatZeroRows` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRows/> |
| `MatZeroRowsColumns` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsColumns/> |
| `MatZeroRowsColumnsIS` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsColumnsIS/> |
| `MatZeroRowsColumnsLocal` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsColumnsLocal/> |
| `MatZeroRowsColumnsLocalIS` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsColumnsLocalIS/> |
| `MatZeroRowsColumnsStencil` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsColumnsStencil/> |
| `MatZeroRowsIS` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsIS/> |
| `MatZeroRowsLocal` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsLocal/> |
| `MatZeroRowsLocalIS` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsLocalIS/> |
| `MatZeroRowsStencil` | Collective | <https://petsc.org/release/manualpages/Mat/MatZeroRowsStencil/> |
| `PetscHeapAdd` | Not Collective | <https://petsc.org/release/manualpages/Mat/PetscHeapAdd/> |
| `PetscHeapCreate` | Not Collective | <https://petsc.org/release/manualpages/Mat/PetscHeapCreate/> |
| `PetscHeapDestroy` | Not Collective | <https://petsc.org/release/manualpages/Mat/PetscHeapDestroy/> |
| `PetscHeapPeek` | Not Collective | <https://petsc.org/release/manualpages/Mat/PetscHeapPeek/> |
| `PetscHeapPop` | Not Collective | <https://petsc.org/release/manualpages/Mat/PetscHeapPop/> |
| `PetscHeapStash` | Not Collective | <https://petsc.org/release/manualpages/Mat/PetscHeapStash/> |
| `PetscHeapUnstash` | Not Collective | <https://petsc.org/release/manualpages/Mat/PetscHeapUnstash/> |
| `PetscHeapView` | Not Collective | <https://petsc.org/release/manualpages/Mat/PetscHeapView/> |
| `VecScatterFFTWToPetsc` | Collective | <https://petsc.org/release/manualpages/Mat/VecScatterFFTWToPetsc/> |
| `VecScatterPetscToFFTW` | Collective | <https://petsc.org/release/manualpages/Mat/VecScatterPetscToFFTW/> |

## MatFD

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `MatFDColoringApply` | Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringApply/> |
| `MatFDColoringCreate` | Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringCreate/> |
| `MatFDColoringDestroy` | Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringDestroy/> |
| `MatFDColoringGetFunction` | Not Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringGetFunction/> |
| `MatFDColoringGetPerturbedColumns` | Not Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringGetPerturbedColumns/> |
| `MatFDColoringSetBlockSize` | Logically Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringSetBlockSize/> |
| `MatFDColoringSetF` | Logically Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringSetF/> |
| `MatFDColoringSetFromOptions` | Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringSetFromOptions/> |
| `MatFDColoringSetFunction` | Logically Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringSetFunction/> |
| `MatFDColoringSetParameters` | Logically Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringSetParameters/> |
| `MatFDColoringSetType` | Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringSetType/> |
| `MatFDColoringSetUp` | Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringSetUp/> |
| `MatFDColoringView` | Collective | <https://petsc.org/release/manualpages/MatFD/MatFDColoringView/> |

## MatGraphOperations

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `MatCoarsenApply` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenApply/> |
| `MatCoarsenCreate` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenCreate/> |
| `MatCoarsenDestroy` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenDestroy/> |
| `MatCoarsenGetData` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenGetData/> |
| `MatCoarsenGetType` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenGetType/> |
| `MatCoarsenMISKGetDistance` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenMISKGetDistance/> |
| `MatCoarsenMISKSetDistance` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenMISKSetDistance/> |
| `MatCoarsenRegister` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenRegister/> |
| `MatCoarsenRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenRegisterAll/> |
| `MatCoarsenSetAdjacency` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenSetAdjacency/> |
| `MatCoarsenSetFromOptions` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenSetFromOptions/> |
| `MatCoarsenSetGreedyOrdering` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenSetGreedyOrdering/> |
| `MatCoarsenSetMaximumIterations` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenSetMaximumIterations/> |
| `MatCoarsenSetStrengthIndex` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenSetStrengthIndex/> |
| `MatCoarsenSetStrictAggs` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenSetStrictAggs/> |
| `MatCoarsenSetThreshold` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenSetThreshold/> |
| `MatCoarsenSetType` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenSetType/> |
| `MatCoarsenView` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenView/> |
| `MatCoarsenViewFromOptions` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatCoarsenViewFromOptions/> |
| `MatColoringApply` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringApply/> |
| `MatColoringCreate` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringCreate/> |
| `MatColoringCreateWeights` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringCreateWeights/> |
| `MatColoringDestroy` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringDestroy/> |
| `MatColoringGetDegrees` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringGetDegrees/> |
| `MatColoringGetDistance` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringGetDistance/> |
| `MatColoringGetMaxColors` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringGetMaxColors/> |
| `MatColoringRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringRegister/> |
| `MatColoringRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringRegisterAll/> |
| `MatColoringSetDistance` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringSetDistance/> |
| `MatColoringSetFromOptions` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringSetFromOptions/> |
| `MatColoringSetMaxColors` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringSetMaxColors/> |
| `MatColoringSetType` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringSetType/> |
| `MatColoringSetWeights` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringSetWeights/> |
| `MatColoringSetWeightType` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringSetWeightType/> |
| `MatColoringView` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatColoringView/> |
| `MatGetOrdering` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatGetOrdering/> |
| `MatGetOrderingList` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatGetOrderingList/> |
| `MatMeshToCellGraph` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatMeshToCellGraph/> |
| `MatOrderingRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/MatGraphOperations/MatOrderingRegister/> |
| `MatOrderingRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatOrderingRegisterAll/> |
| `MatPartitioningApply` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningApply/> |
| `MatPartitioningApplyND` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningApplyND/> |
| `MatPartitioningChacoGetEigenNumber` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoGetEigenNumber/> |
| `MatPartitioningChacoGetEigenSolver` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoGetEigenSolver/> |
| `MatPartitioningChacoGetEigenTol` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoGetEigenTol/> |
| `MatPartitioningChacoGetGlobal` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoGetGlobal/> |
| `MatPartitioningChacoGetLocal` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoGetLocal/> |
| `MatPartitioningChacoSetCoarseLevel` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoSetCoarseLevel/> |
| `MatPartitioningChacoSetEigenNumber` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoSetEigenNumber/> |
| `MatPartitioningChacoSetEigenSolver` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoSetEigenSolver/> |
| `MatPartitioningChacoSetEigenTol` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoSetEigenTol/> |
| `MatPartitioningChacoSetGlobal` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoSetGlobal/> |
| `MatPartitioningChacoSetLocal` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningChacoSetLocal/> |
| `MatPartitioningCreate` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningCreate/> |
| `MatPartitioningDestroy` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningDestroy/> |
| `MatPartitioningGetType` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningGetType/> |
| `MatPartitioningGetUseEdgeWeights` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningGetUseEdgeWeights/> |
| `MatPartitioningHierarchicalGetCoarseparts` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningHierarchicalGetCoarseparts/> |
| `MatPartitioningHierarchicalGetFineparts` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningHierarchicalGetFineparts/> |
| `MatPartitioningHierarchicalSetNcoarseparts` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningHierarchicalSetNcoarseparts/> |
| `MatPartitioningHierarchicalSetNfineparts` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningHierarchicalSetNfineparts/> |
| `MatPartitioningImprove` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningImprove/> |
| `MatPartitioningParmetisSetCoarseSequential` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningParmetisSetCoarseSequential/> |
| `MatPartitioningParmetisSetRepartition` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningParmetisSetRepartition/> |
| `MatPartitioningPartySetBipart` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPartySetBipart/> |
| `MatPartitioningPartySetCoarseLevel` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPartySetCoarseLevel/> |
| `MatPartitioningPartySetGlobal` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPartySetGlobal/> |
| `MatPartitioningPartySetLocal` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPartySetLocal/> |
| `MatPartitioningPartySetMatchOptimization` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPartySetMatchOptimization/> |
| `MatPartitioningPTScotchGetImbalance` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPTScotchGetImbalance/> |
| `MatPartitioningPTScotchGetStrategy` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPTScotchGetStrategy/> |
| `MatPartitioningPTScotchSetImbalance` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPTScotchSetImbalance/> |
| `MatPartitioningPTScotchSetStrategy` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningPTScotchSetStrategy/> |
| `MatPartitioningRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningRegister/> |
| `MatPartitioningRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningRegisterAll/> |
| `MatPartitioningSetAdjacency` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningSetAdjacency/> |
| `MatPartitioningSetFromOptions` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningSetFromOptions/> |
| `MatPartitioningSetNParts` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningSetNParts/> |
| `MatPartitioningSetNumberVertexWeights` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningSetNumberVertexWeights/> |
| `MatPartitioningSetPartitionWeights` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningSetPartitionWeights/> |
| `MatPartitioningSetType` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningSetType/> |
| `MatPartitioningSetUseEdgeWeights` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningSetUseEdgeWeights/> |
| `MatPartitioningSetVertexWeights` | Logically Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningSetVertexWeights/> |
| `MatPartitioningView` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningView/> |
| `MatPartitioningViewFromOptions` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningViewFromOptions/> |
| `MatPartitioningViewImbalance` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/MatPartitioningViewImbalance/> |
| `PetscPartitionerCreate` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerCreate/> |
| `PetscPartitionerDestroy` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerDestroy/> |
| `PetscPartitionerGetType` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerGetType/> |
| `PetscPartitionerMatPartitioningGetMatPartitioning` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerMatPartitioningGetMatPartitioning/> |
| `PetscPartitionerMultistageSetStages` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerMultistageSetStages/> |
| `PetscPartitionerPartition` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerPartition/> |
| `PetscPartitionerRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerRegister/> |
| `PetscPartitionerRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerRegisterAll/> |
| `PetscPartitionerReset` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerReset/> |
| `PetscPartitionerSetFromOptions` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerSetFromOptions/> |
| `PetscPartitionerSetType` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerSetType/> |
| `PetscPartitionerSetUp` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerSetUp/> |
| `PetscPartitionerShellGetRandom` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerShellGetRandom/> |
| `PetscPartitionerShellSetPartition` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerShellSetPartition/> |
| `PetscPartitionerShellSetRandom` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerShellSetRandom/> |
| `PetscPartitionerView` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerView/> |
| `PetscPartitionerViewFromOptions` | Collective | <https://petsc.org/release/manualpages/MatGraphOperations/PetscPartitionerViewFromOptions/> |

## Matlab

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PETSC_MATLAB_ENGINE_` | Not Collective | <https://petsc.org/release/manualpages/Matlab/PETSC_MATLAB_ENGINE_/> |
| `PetscMatlabEngineCreate` | Not Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineCreate/> |
| `PetscMatlabEngineDestroy` | Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineDestroy/> |
| `PetscMatlabEngineEvaluate` | Not Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineEvaluate/> |
| `PetscMatlabEngineGet` | Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineGet/> |
| `PetscMatlabEngineGetArray` | Not Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineGetArray/> |
| `PetscMatlabEngineGetOutput` | Not Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineGetOutput/> |
| `PetscMatlabEnginePrintOutput` | Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEnginePrintOutput/> |
| `PetscMatlabEnginePut` | Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEnginePut/> |
| `PetscMatlabEnginePutArray` | Collective | <https://petsc.org/release/manualpages/Matlab/PetscMatlabEnginePutArray/> |

## PC

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PCAmgXGetResources` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/PC/PCAmgXGetResources/> |
| `PCAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCAppendOptionsPrefix/> |
| `PCApply` | Collective | <https://petsc.org/release/manualpages/PC/PCApply/> |
| `PCApplyBAorAB` | Collective | <https://petsc.org/release/manualpages/PC/PCApplyBAorAB/> |
| `PCApplyBAorABTranspose` | Collective | <https://petsc.org/release/manualpages/PC/PCApplyBAorABTranspose/> |
| `PCApplyRichardson` | Collective | <https://petsc.org/release/manualpages/PC/PCApplyRichardson/> |
| `PCApplyRichardsonExists` | Not Collective | <https://petsc.org/release/manualpages/PC/PCApplyRichardsonExists/> |
| `PCApplySymmetricLeft` | Collective | <https://petsc.org/release/manualpages/PC/PCApplySymmetricLeft/> |
| `PCApplySymmetricRight` | Collective | <https://petsc.org/release/manualpages/PC/PCApplySymmetricRight/> |
| `PCApplyTranspose` | Collective | <https://petsc.org/release/manualpages/PC/PCApplyTranspose/> |
| `PCApplyTransposeExists` | Collective | <https://petsc.org/release/manualpages/PC/PCApplyTransposeExists/> |
| `PCASMCreateSubdomains` | Collective | <https://petsc.org/release/manualpages/PC/PCASMCreateSubdomains/> |
| `PCASMCreateSubdomains2D` | Not Collective | <https://petsc.org/release/manualpages/PC/PCASMCreateSubdomains2D/> |
| `PCASMDestroySubdomains` | Collective | <https://petsc.org/release/manualpages/PC/PCASMDestroySubdomains/> |
| `PCASMGetDMSubdomains` | Not Collective | <https://petsc.org/release/manualpages/PC/PCASMGetDMSubdomains/> |
| `PCASMGetLocalSubdomains` | Not Collective | <https://petsc.org/release/manualpages/PC/PCASMGetLocalSubdomains/> |
| `PCASMGetLocalSubmatrices` | Not Collective | <https://petsc.org/release/manualpages/PC/PCASMGetLocalSubmatrices/> |
| `PCASMGetLocalType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCASMGetLocalType/> |
| `PCASMGetSubKSP` | Collective iff first_local is requested | <https://petsc.org/release/manualpages/PC/PCASMGetSubKSP/> |
| `PCASMGetSubMatType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCASMGetSubMatType/> |
| `PCASMGetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCASMGetType/> |
| `PCASMSetDMSubdomains` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCASMSetDMSubdomains/> |
| `PCASMSetLocalSubdomains` | Collective | <https://petsc.org/release/manualpages/PC/PCASMSetLocalSubdomains/> |
| `PCASMSetLocalType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCASMSetLocalType/> |
| `PCASMSetOverlap` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCASMSetOverlap/> |
| `PCASMSetSortIndices` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCASMSetSortIndices/> |
| `PCASMSetSubMatType` | Collective | <https://petsc.org/release/manualpages/PC/PCASMSetSubMatType/> |
| `PCASMSetTotalSubdomains` | Collective, all MPI ranks must pass in the same array of IS | <https://petsc.org/release/manualpages/PC/PCASMSetTotalSubdomains/> |
| `PCASMSetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCASMSetType/> |
| `PCBDDCCreateFETIDPOperators` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCCreateFETIDPOperators/> |
| `PCBDDCGetDirichletBoundaries` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCGetDirichletBoundaries/> |
| `PCBDDCGetDirichletBoundariesLocal` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCGetDirichletBoundariesLocal/> |
| `PCBDDCGetNeumannBoundaries` | Not Collective | <https://petsc.org/release/manualpages/PC/PCBDDCGetNeumannBoundaries/> |
| `PCBDDCGetNeumannBoundariesLocal` | Not Collective | <https://petsc.org/release/manualpages/PC/PCBDDCGetNeumannBoundariesLocal/> |
| `PCBDDCGetPrimalVerticesIS` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCGetPrimalVerticesIS/> |
| `PCBDDCGetPrimalVerticesLocalIS` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCGetPrimalVerticesLocalIS/> |
| `PCBDDCMatFETIDPGetRHS` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCMatFETIDPGetRHS/> |
| `PCBDDCMatFETIDPGetSolution` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCMatFETIDPGetSolution/> |
| `PCBDDCSetChangeOfBasisMat` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetChangeOfBasisMat/> |
| `PCBDDCSetCoarseningRatio` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetCoarseningRatio/> |
| `PCBDDCSetDirichletBoundaries` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetDirichletBoundaries/> |
| `PCBDDCSetDirichletBoundariesLocal` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetDirichletBoundariesLocal/> |
| `PCBDDCSetDiscreteGradient` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetDiscreteGradient/> |
| `PCBDDCSetDivergenceMat` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetDivergenceMat/> |
| `PCBDDCSetDofsSplitting` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetDofsSplitting/> |
| `PCBDDCSetDofsSplittingLocal` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetDofsSplittingLocal/> |
| `PCBDDCSetLevels` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetLevels/> |
| `PCBDDCSetLocalAdjacencyGraph` | Not collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetLocalAdjacencyGraph/> |
| `PCBDDCSetNeumannBoundaries` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetNeumannBoundaries/> |
| `PCBDDCSetNeumannBoundariesLocal` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetNeumannBoundariesLocal/> |
| `PCBDDCSetPrimalVerticesIS` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetPrimalVerticesIS/> |
| `PCBDDCSetPrimalVerticesLocalIS` | Collective | <https://petsc.org/release/manualpages/PC/PCBDDCSetPrimalVerticesLocalIS/> |
| `PCBJacobiGetLocalBlocks` | Not Collective | <https://petsc.org/release/manualpages/PC/PCBJacobiGetLocalBlocks/> |
| `PCBJacobiGetSubKSP` | Not Collective | <https://petsc.org/release/manualpages/PC/PCBJacobiGetSubKSP/> |
| `PCBJacobiGetTotalBlocks` | Not Collective | <https://petsc.org/release/manualpages/PC/PCBJacobiGetTotalBlocks/> |
| `PCBJacobiSetLocalBlocks` | Not Collective | <https://petsc.org/release/manualpages/PC/PCBJacobiSetLocalBlocks/> |
| `PCBJacobiSetTotalBlocks` | Collective | <https://petsc.org/release/manualpages/PC/PCBJacobiSetTotalBlocks/> |
| `PCBJKOKKOSGetKSP` | Not Collective but KSP returned is parallel if PC was parallel | <https://petsc.org/release/manualpages/PC/PCBJKOKKOSGetKSP/> |
| `PCBJKOKKOSSetKSP` | Collective | <https://petsc.org/release/manualpages/PC/PCBJKOKKOSSetKSP/> |
| `PCCompositeAddPC` | Collective | <https://petsc.org/release/manualpages/PC/PCCompositeAddPC/> |
| `PCCompositeAddPCType` | Collective | <https://petsc.org/release/manualpages/PC/PCCompositeAddPCType/> |
| `PCCompositeGetNumberPC` | Not Collective | <https://petsc.org/release/manualpages/PC/PCCompositeGetNumberPC/> |
| `PCCompositeGetPC` | Not Collective | <https://petsc.org/release/manualpages/PC/PCCompositeGetPC/> |
| `PCCompositeGetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCCompositeGetType/> |
| `PCCompositeSetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCCompositeSetType/> |
| `PCCompositeSpecialSetAlpha` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCCompositeSpecialSetAlpha/> |
| `PCCompositeSpecialSetAlphaMat` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCCompositeSpecialSetAlphaMat/> |
| `PCComputeOperator` | Collective | <https://petsc.org/release/manualpages/PC/PCComputeOperator/> |
| `PCCreate` | Collective | <https://petsc.org/release/manualpages/PC/PCCreate/> |
| `PCDeflationGetCoarseKSP` | Not Collective | <https://petsc.org/release/manualpages/PC/PCDeflationGetCoarseKSP/> |
| `PCDeflationGetPC` | Not Collective | <https://petsc.org/release/manualpages/PC/PCDeflationGetPC/> |
| `PCDeflationSetCoarseMat` | Collective | <https://petsc.org/release/manualpages/PC/PCDeflationSetCoarseMat/> |
| `PCDeflationSetCorrectionFactor` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCDeflationSetCorrectionFactor/> |
| `PCDeflationSetInitOnly` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCDeflationSetInitOnly/> |
| `PCDeflationSetLevels` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCDeflationSetLevels/> |
| `PCDeflationSetProjectionNullSpaceMat` | Collective | <https://petsc.org/release/manualpages/PC/PCDeflationSetProjectionNullSpaceMat/> |
| `PCDeflationSetReductionFactor` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCDeflationSetReductionFactor/> |
| `PCDeflationSetSpace` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCDeflationSetSpace/> |
| `PCDeflationSetSpaceToCompute` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCDeflationSetSpaceToCompute/> |
| `PCDestroy` | Collective | <https://petsc.org/release/manualpages/PC/PCDestroy/> |
| `PCDiagonalScaleLeft` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCDiagonalScaleLeft/> |
| `PCDiagonalScaleRight` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCDiagonalScaleRight/> |
| `PCEisenstatGetNoDiagonalScaling` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCEisenstatGetNoDiagonalScaling/> |
| `PCEisenstatGetOmega` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCEisenstatGetOmega/> |
| `PCEisenstatSetNoDiagonalScaling` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCEisenstatSetNoDiagonalScaling/> |
| `PCEisenstatSetOmega` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCEisenstatSetOmega/> |
| `PCExoticSetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCExoticSetType/> |
| `PCFactorGetAllowDiagonalFill` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorGetAllowDiagonalFill/> |
| `PCFactorGetLevels` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorGetLevels/> |
| `PCFactorGetMatrix` | Not Collective though mat is parallel if pc is parallel | <https://petsc.org/release/manualpages/PC/PCFactorGetMatrix/> |
| `PCFactorGetMatSolverType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCFactorGetMatSolverType/> |
| `PCFactorGetShiftAmount` | Not Collective | <https://petsc.org/release/manualpages/PC/PCFactorGetShiftAmount/> |
| `PCFactorGetShiftType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCFactorGetShiftType/> |
| `PCFactorGetUseInPlace` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorGetUseInPlace/> |
| `PCFactorGetZeroPivot` | Not Collective | <https://petsc.org/release/manualpages/PC/PCFactorGetZeroPivot/> |
| `PCFactorReorderForNonzeroDiagonal` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorReorderForNonzeroDiagonal/> |
| `PCFactorSetAllowDiagonalFill` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetAllowDiagonalFill/> |
| `PCFactorSetColumnPivot` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetColumnPivot/> |
| `PCFactorSetDropTolerance` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetDropTolerance/> |
| `PCFactorSetFill` | Not Collective, each process can expect a different amount of fill | <https://petsc.org/release/manualpages/PC/PCFactorSetFill/> |
| `PCFactorSetLevels` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetLevels/> |
| `PCFactorSetMatOrderingType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetMatOrderingType/> |
| `PCFactorSetMatSolverType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetMatSolverType/> |
| `PCFactorSetPivotInBlocks` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetPivotInBlocks/> |
| `PCFactorSetReuseFill` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetReuseFill/> |
| `PCFactorSetReuseOrdering` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetReuseOrdering/> |
| `PCFactorSetShiftAmount` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetShiftAmount/> |
| `PCFactorSetShiftType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetShiftType/> |
| `PCFactorSetUseInPlace` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetUseInPlace/> |
| `PCFactorSetZeroPivot` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFactorSetZeroPivot/> |
| `PCFieldSplitGetDetectSaddlePoint` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetDetectSaddlePoint/> |
| `PCFieldSplitGetDiagUseAmat` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetDiagUseAmat/> |
| `PCFieldSplitGetDMSplits` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetDMSplits/> |
| `PCFieldSplitGetIS` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetIS/> |
| `PCFieldSplitGetISByIndex` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetISByIndex/> |
| `PCFieldSplitGetOffDiagUseAmat` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetOffDiagUseAmat/> |
| `PCFieldSplitGetSchurBlocks` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetSchurBlocks/> |
| `PCFieldSplitGetSchurPre` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetSchurPre/> |
| `PCFieldSplitGetSubKSP` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetSubKSP/> |
| `PCFieldSplitGetType` | Not collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitGetType/> |
| `PCFieldSplitSchurGetS` | Not Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSchurGetS/> |
| `PCFieldSplitSchurGetSubKSP` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSchurGetSubKSP/> |
| `PCFieldSplitSchurRestoreS` | Not Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSchurRestoreS/> |
| `PCFieldSplitSetBlockSize` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetBlockSize/> |
| `PCFieldSplitSetDetectSaddlePoint` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetDetectSaddlePoint/> |
| `PCFieldSplitSetDiagUseAmat` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetDiagUseAmat/> |
| `PCFieldSplitSetDMSplits` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetDMSplits/> |
| `PCFieldSplitSetFields` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetFields/> |
| `PCFieldSplitSetGKBDelay` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetGKBDelay/> |
| `PCFieldSplitSetGKBMaxit` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetGKBMaxit/> |
| `PCFieldSplitSetGKBNu` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetGKBNu/> |
| `PCFieldSplitSetGKBTol` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetGKBTol/> |
| `PCFieldSplitSetIS` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetIS/> |
| `PCFieldSplitSetOffDiagUseAmat` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetOffDiagUseAmat/> |
| `PCFieldSplitSetSchurFactType` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetSchurFactType/> |
| `PCFieldSplitSetSchurPre` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetSchurPre/> |
| `PCFieldSplitSetSchurScale` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetSchurScale/> |
| `PCFieldSplitSetType` | Collective | <https://petsc.org/release/manualpages/PC/PCFieldSplitSetType/> |
| `PCGalerkinGetKSP` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGalerkinGetKSP/> |
| `PCGalerkinSetComputeSubmatrix` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGalerkinSetComputeSubmatrix/> |
| `PCGalerkinSetInterpolation` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGalerkinSetInterpolation/> |
| `PCGalerkinSetRestriction` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGalerkinSetRestriction/> |
| `PCGAMGASMSetHEM` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGASMSetHEM/> |
| `PCGAMGASMSetUseAggs` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGASMSetUseAggs/> |
| `PCGAMGClassicalGetType` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGClassicalGetType/> |
| `PCGAMGClassicalSetType` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGClassicalSetType/> |
| `PCGAMGGetType` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGGetType/> |
| `PCGAMGMISkSetAggressive` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGMISkSetAggressive/> |
| `PCGAMGMISkSetMinDegreeOrdering` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGMISkSetMinDegreeOrdering/> |
| `PCGAMGSetAggressiveLevels` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetAggressiveLevels/> |
| `PCGAMGSetAggressiveSquareGraph` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetAggressiveSquareGraph/> |
| `PCGAMGSetCoarseEqLim` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetCoarseEqLim/> |
| `PCGAMGSetCoarseGridLayoutType` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetCoarseGridLayoutType/> |
| `PCGAMGSetCpuPinCoarseGrids` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetCpuPinCoarseGrids/> |
| `PCGAMGSetEigenvalues` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetEigenvalues/> |
| `PCGAMGSetGraphSymmetrize` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetGraphSymmetrize/> |
| `PCGAMGSetInjectionIndex` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetInjectionIndex/> |
| `PCGAMGSetLowMemoryFilter` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetLowMemoryFilter/> |
| `PCGAMGSetNlevels` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetNlevels/> |
| `PCGAMGSetNSmooths` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetNSmooths/> |
| `PCGAMGSetParallelCoarseGridSolve` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetParallelCoarseGridSolve/> |
| `PCGAMGSetProcEqLim` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetProcEqLim/> |
| `PCGAMGSetRankReductionFactors` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetRankReductionFactors/> |
| `PCGAMGSetRecomputeEstEig` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetRecomputeEstEig/> |
| `PCGAMGSetRepartition` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetRepartition/> |
| `PCGAMGSetReuseInterpolation` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetReuseInterpolation/> |
| `PCGAMGSetThreshold` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetThreshold/> |
| `PCGAMGSetThresholdScale` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetThresholdScale/> |
| `PCGAMGSetType` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetType/> |
| `PCGAMGSetUseSAEstEig` | Collective | <https://petsc.org/release/manualpages/PC/PCGAMGSetUseSAEstEig/> |
| `PCGASMCreateSubdomains` | Collective | <https://petsc.org/release/manualpages/PC/PCGASMCreateSubdomains/> |
| `PCGASMCreateSubdomains2D` | Collective | <https://petsc.org/release/manualpages/PC/PCGASMCreateSubdomains2D/> |
| `PCGASMDestroySubdomains` | Collective | <https://petsc.org/release/manualpages/PC/PCGASMDestroySubdomains/> |
| `PCGASMGetSubdomains` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGASMGetSubdomains/> |
| `PCGASMGetSubKSP` | Collective iff first_local is requested | <https://petsc.org/release/manualpages/PC/PCGASMGetSubKSP/> |
| `PCGASMGetSubmatrices` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGASMGetSubmatrices/> |
| `PCGASMGetUseDMSubdomains` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGASMGetUseDMSubdomains/> |
| `PCGASMSetOverlap` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGASMSetOverlap/> |
| `PCGASMSetSortIndices` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGASMSetSortIndices/> |
| `PCGASMSetSubdomains` | Collective | <https://petsc.org/release/manualpages/PC/PCGASMSetSubdomains/> |
| `PCGASMSetTotalSubdomains` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGASMSetTotalSubdomains/> |
| `PCGASMSetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGASMSetType/> |
| `PCGASMSetUseDMSubdomains` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGASMSetUseDMSubdomains/> |
| `PCGetApplicationContext` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGetApplicationContext/> |
| `PCGetCoarseOperators` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGetCoarseOperators/> |
| `PCGetDiagonalScale` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGetDiagonalScale/> |
| `PCGetDM` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGetDM/> |
| `PCGetFailedReason` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGetFailedReason/> |
| `PCGetInterpolations` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGetInterpolations/> |
| `PCGetKSPNestLevel` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGetKSPNestLevel/> |
| `PCGetOperators` | Not Collective, though parallel Mat s are returned if pc is parallel | <https://petsc.org/release/manualpages/PC/PCGetOperators/> |
| `PCGetOperatorsSet` | Not Collective, though the results on all processes should be the same | <https://petsc.org/release/manualpages/PC/PCGetOperatorsSet/> |
| `PCGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGetOptionsPrefix/> |
| `PCGetReusePreconditioner` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGetReusePreconditioner/> |
| `PCGetType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCGetType/> |
| `PCGetUseAmat` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCGetUseAmat/> |
| `PCHMGSetCoarseningComponent` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCHMGSetCoarseningComponent/> |
| `PCHMGSetInnerPCType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCHMGSetInnerPCType/> |
| `PCHMGSetReuseInterpolation` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCHMGSetReuseInterpolation/> |
| `PCHMGSetUseSubspaceCoarsening` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCHMGSetUseSubspaceCoarsening/> |
| `PCHMGUseMatMAIJ` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCHMGUseMatMAIJ/> |
| `PCHPDDMGetComplexities` | Collective | <https://petsc.org/release/manualpages/PC/PCHPDDMGetComplexities/> |
| `PCHPDDMSetCoarseCorrectionType` | Collective | <https://petsc.org/release/manualpages/PC/PCHPDDMSetCoarseCorrectionType/> |
| `PCHYPREAMSSetInteriorNodes` | Collective | <https://petsc.org/release/manualpages/PC/PCHYPREAMSSetInteriorNodes/> |
| `PCHYPREGetCFMarkers` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCHYPREGetCFMarkers/> |
| `PCHYPRESetAlphaPoissonMatrix` | Collective | <https://petsc.org/release/manualpages/PC/PCHYPRESetAlphaPoissonMatrix/> |
| `PCHYPRESetBetaPoissonMatrix` | Collective | <https://petsc.org/release/manualpages/PC/PCHYPRESetBetaPoissonMatrix/> |
| `PCHYPRESetDiscreteCurl` | Collective | <https://petsc.org/release/manualpages/PC/PCHYPRESetDiscreteCurl/> |
| `PCHYPRESetDiscreteGradient` | Collective | <https://petsc.org/release/manualpages/PC/PCHYPRESetDiscreteGradient/> |
| `PCHYPRESetEdgeConstantVectors` | Collective | <https://petsc.org/release/manualpages/PC/PCHYPRESetEdgeConstantVectors/> |
| `PCHYPRESetInterpolations` | Collective | <https://petsc.org/release/manualpages/PC/PCHYPRESetInterpolations/> |
| `PCISSetSubdomainDiagonalScaling` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCISSetSubdomainDiagonalScaling/> |
| `PCISSetSubdomainScalingFactor` | Not Collective | <https://petsc.org/release/manualpages/PC/PCISSetSubdomainScalingFactor/> |
| `PCISSetUseStiffnessScaling` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCISSetUseStiffnessScaling/> |
| `PCJacobiGetDiagonal` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCJacobiGetDiagonal/> |
| `PCJacobiGetFixDiagonal` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCJacobiGetFixDiagonal/> |
| `PCJacobiGetRowl1Scale` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCJacobiGetRowl1Scale/> |
| `PCJacobiGetType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCJacobiGetType/> |
| `PCJacobiGetUseAbs` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCJacobiGetUseAbs/> |
| `PCJacobiSetFixDiagonal` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCJacobiSetFixDiagonal/> |
| `PCJacobiSetRowl1Scale` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCJacobiSetRowl1Scale/> |
| `PCJacobiSetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCJacobiSetType/> |
| `PCJacobiSetUseAbs` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCJacobiSetUseAbs/> |
| `PCKSPGetKSP` | Not Collective but ksp returned is parallel if pc was parallel | <https://petsc.org/release/manualpages/PC/PCKSPGetKSP/> |
| `PCKSPSetKSP` | Collective | <https://petsc.org/release/manualpages/PC/PCKSPSetKSP/> |
| `PCLoad` | Collective | <https://petsc.org/release/manualpages/PC/PCLoad/> |
| `PCMatApply` | Collective | <https://petsc.org/release/manualpages/PC/PCMatApply/> |
| `PCMatApplyTranspose` | Collective | <https://petsc.org/release/manualpages/PC/PCMatApplyTranspose/> |
| `PCMatGetApplyOperation` | Logically collective | <https://petsc.org/release/manualpages/PC/PCMatGetApplyOperation/> |
| `PCMatSetApplyOperation` | Logically collective | <https://petsc.org/release/manualpages/PC/PCMatSetApplyOperation/> |
| `PCMGGalerkinGetMatProductAlgorithm` | Not Collective | <https://petsc.org/release/manualpages/PC/PCMGGalerkinGetMatProductAlgorithm/> |
| `PCMGGalerkinSetMatProductAlgorithm` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGGalerkinSetMatProductAlgorithm/> |
| `PCMGGetAdaptCoarseSpaceType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCMGGetAdaptCoarseSpaceType/> |
| `PCMGGetAdaptCR` | Not Collective | <https://petsc.org/release/manualpages/PC/PCMGGetAdaptCR/> |
| `PCMGGetAdaptInterpolation` | Not Collective | <https://petsc.org/release/manualpages/PC/PCMGGetAdaptInterpolation/> |
| `PCMGGetCoarseSolve` | Not Collective | <https://petsc.org/release/manualpages/PC/PCMGGetCoarseSolve/> |
| `PCMGGetCoarseSpaceConstructor` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/PC/PCMGGetCoarseSpaceConstructor/> |
| `PCMGGetGalerkin` | Not Collective | <https://petsc.org/release/manualpages/PC/PCMGGetGalerkin/> |
| `PCMGGetInjection` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGGetInjection/> |
| `PCMGGetInterpolation` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGGetInterpolation/> |
| `PCMGGetLevels` | Not Collective | <https://petsc.org/release/manualpages/PC/PCMGGetLevels/> |
| `PCMGGetRestriction` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGGetRestriction/> |
| `PCMGGetRScale` | Collective | <https://petsc.org/release/manualpages/PC/PCMGGetRScale/> |
| `PCMGGetSmoother` | Not Collective, ksp returned is parallel if pc is | <https://petsc.org/release/manualpages/PC/PCMGGetSmoother/> |
| `PCMGGetSmootherDown` | Not Collective, ksp returned is parallel if pc is | <https://petsc.org/release/manualpages/PC/PCMGGetSmootherDown/> |
| `PCMGGetSmootherUp` | Not Collective, ksp returned is parallel if pc is | <https://petsc.org/release/manualpages/PC/PCMGGetSmootherUp/> |
| `PCMGGetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGGetType/> |
| `PCMGMatResidualDefault` | Collective | <https://petsc.org/release/manualpages/PC/PCMGMatResidualDefault/> |
| `PCMGMatResidualTransposeDefault` | Collective | <https://petsc.org/release/manualpages/PC/PCMGMatResidualTransposeDefault/> |
| `PCMGMultiplicativeSetCycles` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGMultiplicativeSetCycles/> |
| `PCMGRegisterCoarseSpaceConstructor` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/PC/PCMGRegisterCoarseSpaceConstructor/> |
| `PCMGResidualDefault` | Collective | <https://petsc.org/release/manualpages/PC/PCMGResidualDefault/> |
| `PCMGResidualTransposeDefault` | Collective | <https://petsc.org/release/manualpages/PC/PCMGResidualTransposeDefault/> |
| `PCMGSetAdaptCoarseSpaceType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetAdaptCoarseSpaceType/> |
| `PCMGSetAdaptCR` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetAdaptCR/> |
| `PCMGSetAdaptInterpolation` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetAdaptInterpolation/> |
| `PCMGSetCycleType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetCycleType/> |
| `PCMGSetCycleTypeOnLevel` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetCycleTypeOnLevel/> |
| `PCMGSetDistinctSmoothUp` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetDistinctSmoothUp/> |
| `PCMGSetGalerkin` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetGalerkin/> |
| `PCMGSetInjection` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetInjection/> |
| `PCMGSetInterpolation` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetInterpolation/> |
| `PCMGSetLevels` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetLevels/> |
| `PCMGSetNumberSmooth` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetNumberSmooth/> |
| `PCMGSetOperators` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetOperators/> |
| `PCMGSetR` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetR/> |
| `PCMGSetResidual` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetResidual/> |
| `PCMGSetResidualTranspose` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetResidualTranspose/> |
| `PCMGSetRestriction` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetRestriction/> |
| `PCMGSetRhs` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetRhs/> |
| `PCMGSetRScale` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetRScale/> |
| `PCMGSetType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetType/> |
| `PCMGSetX` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCMGSetX/> |
| `PCModifySubMatrices` | Collective | <https://petsc.org/release/manualpages/PC/PCModifySubMatrices/> |
| `PCMPIGetKSP` | Not Collective | <https://petsc.org/release/manualpages/PC/PCMPIGetKSP/> |
| `PCMPIServerBegin` | Logically Collective on all MPI processes except rank 0 | <https://petsc.org/release/manualpages/PC/PCMPIServerBegin/> |
| `PCMPIServerEnd` | Logically Collective on all MPI ranks except 0 | <https://petsc.org/release/manualpages/PC/PCMPIServerEnd/> |
| `PCPARMSSetFill` | Collective | <https://petsc.org/release/manualpages/PC/PCPARMSSetFill/> |
| `PCPARMSSetGlobal` | Collective | <https://petsc.org/release/manualpages/PC/PCPARMSSetGlobal/> |
| `PCPARMSSetLocal` | Collective | <https://petsc.org/release/manualpages/PC/PCPARMSSetLocal/> |
| `PCPARMSSetNonsymPerm` | Collective | <https://petsc.org/release/manualpages/PC/PCPARMSSetNonsymPerm/> |
| `PCPARMSSetSolveRestart` | Collective | <https://petsc.org/release/manualpages/PC/PCPARMSSetSolveRestart/> |
| `PCPARMSSetSolveTolerances` | Collective | <https://petsc.org/release/manualpages/PC/PCPARMSSetSolveTolerances/> |
| `PCPatchGetCellNumbering` | Not Collective | <https://petsc.org/release/manualpages/PC/PCPatchGetCellNumbering/> |
| `PCPatchGetConstructType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCPatchGetConstructType/> |
| `PCPatchGetPartitionOfUnity` | Not Collective | <https://petsc.org/release/manualpages/PC/PCPatchGetPartitionOfUnity/> |
| `PCPatchGetPrecomputeElementTensors` | Not Collective | <https://petsc.org/release/manualpages/PC/PCPatchGetPrecomputeElementTensors/> |
| `PCPatchGetSaveOperators` | Not Collective | <https://petsc.org/release/manualpages/PC/PCPatchGetSaveOperators/> |
| `PCPatchGetSubKSP` | Not Collective | <https://petsc.org/release/manualpages/PC/PCPatchGetSubKSP/> |
| `PCPatchGetSubMatType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCPatchGetSubMatType/> |
| `PCPatchSetCellNumbering` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetCellNumbering/> |
| `PCPatchSetComputeFunction` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetComputeFunction/> |
| `PCPatchSetComputeFunctionExteriorFacets` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetComputeFunctionExteriorFacets/> |
| `PCPatchSetComputeFunctionInteriorFacets` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetComputeFunctionInteriorFacets/> |
| `PCPatchSetComputeOperator` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetComputeOperator/> |
| `PCPatchSetComputeOperatorExteriorFacets` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetComputeOperatorExteriorFacets/> |
| `PCPatchSetComputeOperatorInteriorFacets` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetComputeOperatorInteriorFacets/> |
| `PCPatchSetConstructType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetConstructType/> |
| `PCPatchSetDiscretisationInfo` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetDiscretisationInfo/> |
| `PCPatchSetPartitionOfUnity` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetPartitionOfUnity/> |
| `PCPatchSetPrecomputeElementTensors` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetPrecomputeElementTensors/> |
| `PCPatchSetSaveOperators` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetSaveOperators/> |
| `PCPatchSetSubMatType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCPatchSetSubMatType/> |
| `PCPostSolve` | Collective | <https://petsc.org/release/manualpages/PC/PCPostSolve/> |
| `PCPreSolve` | Collective | <https://petsc.org/release/manualpages/PC/PCPreSolve/> |
| `PCPythonGetType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCPythonGetType/> |
| `PCPythonSetType` | Collective | <https://petsc.org/release/manualpages/PC/PCPythonSetType/> |
| `PCRedistributeGetKSP` | Not Collective | <https://petsc.org/release/manualpages/PC/PCRedistributeGetKSP/> |
| `PCReduceFailedReason` | Collective | <https://petsc.org/release/manualpages/PC/PCReduceFailedReason/> |
| `PCRedundantGetKSP` | Not Collective | <https://petsc.org/release/manualpages/PC/PCRedundantGetKSP/> |
| `PCRedundantGetOperators` | Not Collective | <https://petsc.org/release/manualpages/PC/PCRedundantGetOperators/> |
| `PCRedundantSetNumber` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCRedundantSetNumber/> |
| `PCRedundantSetScatter` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCRedundantSetScatter/> |
| `PCRegister` | Not collective. No Fortran Support | <https://petsc.org/release/manualpages/PC/PCRegister/> |
| `PCRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/PC/PCRegisterAll/> |
| `PCReset` | Collective | <https://petsc.org/release/manualpages/PC/PCReset/> |
| `PCSetApplicationContext` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetApplicationContext/> |
| `PCSetCoordinates` | Collective | <https://petsc.org/release/manualpages/PC/PCSetCoordinates/> |
| `PCSetDiagonalScale` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetDiagonalScale/> |
| `PCSetDM` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetDM/> |
| `PCSetErrorIfFailure` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetErrorIfFailure/> |
| `PCSetFailedReason` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetFailedReason/> |
| `PCSetFromOptions` | Collective | <https://petsc.org/release/manualpages/PC/PCSetFromOptions/> |
| `PCSetKSPNestLevel` | Collective | <https://petsc.org/release/manualpages/PC/PCSetKSPNestLevel/> |
| `PCSetModifySubMatrices` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetModifySubMatrices/> |
| `PCSetOperators` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetOperators/> |
| `PCSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetOptionsPrefix/> |
| `PCSetPostSetUp` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetPostSetUp/> |
| `PCSetReusePreconditioner` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetReusePreconditioner/> |
| `PCSetType` | Collective | <https://petsc.org/release/manualpages/PC/PCSetType/> |
| `PCSetUp` | Collective | <https://petsc.org/release/manualpages/PC/PCSetUp/> |
| `PCSetUpOnBlocks` | Collective | <https://petsc.org/release/manualpages/PC/PCSetUpOnBlocks/> |
| `PCSetUseAmat` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSetUseAmat/> |
| `PCShellGetContext` | Not Collective | <https://petsc.org/release/manualpages/PC/PCShellGetContext/> |
| `PCShellGetName` | Not Collective | <https://petsc.org/release/manualpages/PC/PCShellGetName/> |
| `PCShellSetApply` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetApply/> |
| `PCShellSetApplyBA` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetApplyBA/> |
| `PCShellSetApplyRichardson` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetApplyRichardson/> |
| `PCShellSetApplySymmetricLeft` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetApplySymmetricLeft/> |
| `PCShellSetApplySymmetricRight` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetApplySymmetricRight/> |
| `PCShellSetApplyTranspose` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetApplyTranspose/> |
| `PCShellSetContext` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetContext/> |
| `PCShellSetDestroy` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetDestroy/> |
| `PCShellSetMatApply` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetMatApply/> |
| `PCShellSetMatApplyTranspose` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetMatApplyTranspose/> |
| `PCShellSetName` | Not Collective | <https://petsc.org/release/manualpages/PC/PCShellSetName/> |
| `PCShellSetPostSolve` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetPostSolve/> |
| `PCShellSetPreSolve` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetPreSolve/> |
| `PCShellSetSetUp` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetSetUp/> |
| `PCShellSetView` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCShellSetView/> |
| `PCSORGetIterations` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSORGetIterations/> |
| `PCSORGetOmega` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSORGetOmega/> |
| `PCSORGetSymmetric` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSORGetSymmetric/> |
| `PCSORSetIterations` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSORSetIterations/> |
| `PCSORSetOmega` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSORSetOmega/> |
| `PCSORSetSymmetric` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCSORSetSymmetric/> |
| `PCTelescopeGetDM` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeGetDM/> |
| `PCTelescopeGetIgnoreDM` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeGetIgnoreDM/> |
| `PCTelescopeGetIgnoreKSPComputeOperators` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeGetIgnoreKSPComputeOperators/> |
| `PCTelescopeGetKSP` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeGetKSP/> |
| `PCTelescopeGetReductionFactor` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeGetReductionFactor/> |
| `PCTelescopeGetSubcommType` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeGetSubcommType/> |
| `PCTelescopeGetUseCoarseDM` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeGetUseCoarseDM/> |
| `PCTelescopeSetIgnoreDM` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeSetIgnoreDM/> |
| `PCTelescopeSetIgnoreKSPComputeOperators` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeSetIgnoreKSPComputeOperators/> |
| `PCTelescopeSetReductionFactor` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeSetReductionFactor/> |
| `PCTelescopeSetSubcommType` | Logically Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeSetSubcommType/> |
| `PCTelescopeSetUseCoarseDM` | Not Collective | <https://petsc.org/release/manualpages/PC/PCTelescopeSetUseCoarseDM/> |
| `PCView` | Collective | <https://petsc.org/release/manualpages/PC/PCView/> |
| `PCViewFromOptions` | Collective | <https://petsc.org/release/manualpages/PC/PCViewFromOptions/> |

## PetscDA

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscDAAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAAppendOptionsPrefix/> |
| `PetscDACreate` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDACreate/> |
| `PetscDADestroy` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDADestroy/> |
| `PetscDAEnsembleAnalysis` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleAnalysis/> |
| `PetscDAEnsembleApplySqrtTInverse` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleApplySqrtTInverse/> |
| `PetscDAEnsembleApplyTInverse` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleApplyTInverse/> |
| `PetscDAEnsembleComputeAnomalies` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleComputeAnomalies/> |
| `PetscDAEnsembleComputeMean` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleComputeMean/> |
| `PetscDAEnsembleComputeNormalizedInnovationMatrix` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleComputeNormalizedInnovationMatrix/> |
| `PetscDAEnsembleForecast` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleForecast/> |
| `PetscDAEnsembleGetInflation` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleGetInflation/> |
| `PetscDAEnsembleGetMember` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleGetMember/> |
| `PetscDAEnsembleGetSize` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleGetSize/> |
| `PetscDAEnsembleGetSqrtType` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleGetSqrtType/> |
| `PetscDAEnsembleRestoreMember` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleRestoreMember/> |
| `PetscDAEnsembleSetInflation` | Logically Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleSetInflation/> |
| `PetscDAEnsembleSetMember` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleSetMember/> |
| `PetscDAEnsembleSetSize` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleSetSize/> |
| `PetscDAEnsembleSetSqrtType` | Logically Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleSetSqrtType/> |
| `PetscDAEnsembleTFactor` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleTFactor/> |
| `PetscDAFinalizePackage` | Logically Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAFinalizePackage/> |
| `PetscDAGetNDOF` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAGetNDOF/> |
| `PetscDAGetObsErrorVariance` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAGetObsErrorVariance/> |
| `PetscDAGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAGetOptionsPrefix/> |
| `PetscDAGetSizes` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAGetSizes/> |
| `PetscDAGetType` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAGetType/> |
| `PetscDAInitializePackage` | Logically Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAInitializePackage/> |
| `PetscDALETKFGetLocalizationMatrix` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDALETKFGetLocalizationMatrix/> |
| `PetscDALETKFGetObsPerVertex` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDALETKFGetObsPerVertex/> |
| `PetscDALETKFSetLocalization` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDALETKFSetLocalization/> |
| `PetscDALETKFSetObsPerVertex` | Logically Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDALETKFSetObsPerVertex/> |
| `PetscDARegister` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDARegister/> |
| `PetscDARegisterAll` | Not Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDARegisterAll/> |
| `PetscDASetFromOptions` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDASetFromOptions/> |
| `PetscDASetLocalSizes` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDASetLocalSizes/> |
| `PetscDASetNDOF` | Logically Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDASetNDOF/> |
| `PetscDASetObsErrorVariance` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDASetObsErrorVariance/> |
| `PetscDASetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDASetOptionsPrefix/> |
| `PetscDASetSizes` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDASetSizes/> |
| `PetscDASetType` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDASetType/> |
| `PetscDASetUp` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDASetUp/> |
| `PetscDAView` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAView/> |
| `PetscDAViewFromOptions` | Collective | <https://petsc.org/release/manualpages/PetscDA/PetscDAViewFromOptions/> |

## PetscRegressor

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscRegressorAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorAppendOptionsPrefix/> |
| `PetscRegressorCreate` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorCreate/> |
| `PetscRegressorDestroy` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorDestroy/> |
| `PetscRegressorFinalizePackage` | Logically Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorFinalizePackage/> |
| `PetscRegressorFit` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorFit/> |
| `PetscRegressorGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorGetOptionsPrefix/> |
| `PetscRegressorGetTao` | Not Collective, but if the PetscRegressor is parallel, then the Tao object is parallel | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorGetTao/> |
| `PetscRegressorGetType` | Not Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorGetType/> |
| `PetscRegressorInitializePackage` | Logically Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorInitializePackage/> |
| `PetscRegressorLinearGetCoefficients` | Not Collective but the vector is parallel | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearGetCoefficients/> |
| `PetscRegressorLinearGetIntercept` | Not Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearGetIntercept/> |
| `PetscRegressorLinearGetKSP` | Not Collective, but if the PetscRegressor is parallel, then the KSP object is parallel | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearGetKSP/> |
| `PetscRegressorLinearSetFitIntercept` | Logically Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearSetFitIntercept/> |
| `PetscRegressorLinearSetType` | Logically Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearSetType/> |
| `PetscRegressorLinearSetUseKSP` | Logically Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearSetUseKSP/> |
| `PetscRegressorPredict` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorPredict/> |
| `PetscRegressorRegister` | Not collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorRegister/> |
| `PetscRegressorReset` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorReset/> |
| `PetscRegressorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetFromOptions/> |
| `PetscRegressorSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetOptionsPrefix/> |
| `PetscRegressorSetRegularizerWeight` | Logically Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetRegularizerWeight/> |
| `PetscRegressorSetType` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetType/> |
| `PetscRegressorSetUp` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetUp/> |
| `PetscRegressorView` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorView/> |
| `PetscRegressorViewFromOptions` | Collective | <https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorViewFromOptions/> |

## PetscSection

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscSectionAddConstraintDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionAddConstraintDof/> |
| `PetscSectionAddDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionAddDof/> |
| `PetscSectionAddFieldConstraintDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionAddFieldConstraintDof/> |
| `PetscSectionAddFieldDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionAddFieldDof/> |
| `PetscSectionArrayView` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionArrayView/> |
| `PetscSectionClone` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionClone/> |
| `PetscSectionCompare` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionCompare/> |
| `PetscSectionCopy` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionCopy/> |
| `PetscSectionCreate` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionCreate/> |
| `PetscSectionCreateComponentSubsection` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateComponentSubsection/> |
| `PetscSectionCreateSubdomainSection` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateSubdomainSection/> |
| `PetscSectionCreateSubmeshSection` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateSubmeshSection/> |
| `PetscSectionCreateSubsection` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateSubsection/> |
| `PetscSectionCreateSupersection` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateSupersection/> |
| `PetscSectionDestroy` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionDestroy/> |
| `PetscSectionExtractDofsFromArray` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionExtractDofsFromArray/> |
| `PetscSectionGetBlockStarts` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetBlockStarts/> |
| `PetscSectionGetChart` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetChart/> |
| `PetscSectionGetClosureIndex` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetClosureIndex/> |
| `PetscSectionGetClosureInversePermutation` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetClosureInversePermutation/> |
| `PetscSectionGetClosurePermutation` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetClosurePermutation/> |
| `PetscSectionGetComponentName` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetComponentName/> |
| `PetscSectionGetConstrainedStorageSize` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetConstrainedStorageSize/> |
| `PetscSectionGetConstraintDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetConstraintDof/> |
| `PetscSectionGetConstraintIndices` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetConstraintIndices/> |
| `PetscSectionGetDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetDof/> |
| `PetscSectionGetFieldComponents` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldComponents/> |
| `PetscSectionGetFieldConstraintDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldConstraintDof/> |
| `PetscSectionGetFieldConstraintIndices` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldConstraintIndices/> |
| `PetscSectionGetFieldDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldDof/> |
| `PetscSectionGetFieldName` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldName/> |
| `PetscSectionGetFieldOffset` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldOffset/> |
| `PetscSectionGetFieldPointOffset` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldPointOffset/> |
| `PetscSectionGetFieldPointSyms` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldPointSyms/> |
| `PetscSectionGetFieldSym` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldSym/> |
| `PetscSectionGetIncludesConstraints` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetIncludesConstraints/> |
| `PetscSectionGetMaxDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetMaxDof/> |
| `PetscSectionGetNumFields` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetNumFields/> |
| `PetscSectionGetOffset` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetOffset/> |
| `PetscSectionGetOffsetRange` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetOffsetRange/> |
| `PetscSectionGetPermutation` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetPermutation/> |
| `PetscSectionGetPointLayout` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetPointLayout/> |
| `PetscSectionGetPointMajor` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetPointMajor/> |
| `PetscSectionGetPointSyms` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetPointSyms/> |
| `PetscSectionGetStorageSize` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetStorageSize/> |
| `PetscSectionGetSym` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetSym/> |
| `PetscSectionGetUseFieldOffsets` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetUseFieldOffsets/> |
| `PetscSectionGetValueLayout` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionGetValueLayout/> |
| `PetscSectionHasConstraints` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionHasConstraints/> |
| `PetscSectionLoad` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionLoad/> |
| `PetscSectionMigrateData` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionMigrateData/> |
| `PetscSectionPermute` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionPermute/> |
| `PetscSectionReset` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionReset/> |
| `PetscSectionRestoreFieldPointSyms` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionRestoreFieldPointSyms/> |
| `PetscSectionRestorePointSyms` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionRestorePointSyms/> |
| `PetscSectionSetBlockStarts` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetBlockStarts/> |
| `PetscSectionSetChart` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetChart/> |
| `PetscSectionSetClosureIndex` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetClosureIndex/> |
| `PetscSectionSetClosurePermutation` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetClosurePermutation/> |
| `PetscSectionSetComponentName` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetComponentName/> |
| `PetscSectionSetConstraintDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetConstraintDof/> |
| `PetscSectionSetConstraintIndices` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetConstraintIndices/> |
| `PetscSectionSetDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetDof/> |
| `PetscSectionSetFieldComponents` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldComponents/> |
| `PetscSectionSetFieldConstraintDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldConstraintDof/> |
| `PetscSectionSetFieldConstraintIndices` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldConstraintIndices/> |
| `PetscSectionSetFieldDof` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldDof/> |
| `PetscSectionSetFieldName` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldName/> |
| `PetscSectionSetFieldOffset` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldOffset/> |
| `PetscSectionSetFieldSym` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldSym/> |
| `PetscSectionSetFromOptions` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFromOptions/> |
| `PetscSectionSetIncludesConstraints` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetIncludesConstraints/> |
| `PetscSectionSetNumFields` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetNumFields/> |
| `PetscSectionSetOffset` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetOffset/> |
| `PetscSectionSetPermutation` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetPermutation/> |
| `PetscSectionSetPointMajor` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetPointMajor/> |
| `PetscSectionSetSym` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetSym/> |
| `PetscSectionSetUp` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetUp/> |
| `PetscSectionSetUpBC` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetUpBC/> |
| `PetscSectionSetUseFieldOffsets` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSetUseFieldOffsets/> |
| `PetscSectionSymCopy` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSymCopy/> |
| `PetscSectionSymCreate` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSymCreate/> |
| `PetscSectionSymDestroy` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSymDestroy/> |
| `PetscSectionSymDistribute` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSymDistribute/> |
| `PetscSectionSymGetType` | Not Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSymGetType/> |
| `PetscSectionSymRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSymRegister/> |
| `PetscSectionSymSetType` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSymSetType/> |
| `PetscSectionSymView` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionSymView/> |
| `PetscSectionView` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionView/> |
| `PetscSectionViewFromOptions` | Collective | <https://petsc.org/release/manualpages/PetscSection/PetscSectionViewFromOptions/> |

## PetscSF

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscLayoutMapLocal` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscLayoutMapLocal/> |
| `PetscNvshmemFinalize` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscNvshmemFinalize/> |
| `PetscSFBcastBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFBcastBegin/> |
| `PetscSFBcastEnd` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFBcastEnd/> |
| `PetscSFBcastWithMemTypeBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFBcastWithMemTypeBegin/> |
| `PetscSFComputeDegreeBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFComputeDegreeBegin/> |
| `PetscSFComputeDegreeEnd` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFComputeDegreeEnd/> |
| `PetscSFComputeMultiRootOriginalNumbering` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFComputeMultiRootOriginalNumbering/> |
| `PetscSFCreate` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreate/> |
| `PetscSFCreateByMatchingIndices` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreateByMatchingIndices/> |
| `PetscSFCreateEmbeddedLeafSF` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreateEmbeddedLeafSF/> |
| `PetscSFCreateEmbeddedRootSF` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreateEmbeddedRootSF/> |
| `PetscSFCreateFromLayouts` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreateFromLayouts/> |
| `PetscSFCreateInverseSF` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreateInverseSF/> |
| `PetscSFCreateRemoteOffsets` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreateRemoteOffsets/> |
| `PetscSFCreateSectionSF` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreateSectionSF/> |
| `PetscSFCreateStridedSF` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFCreateStridedSF/> |
| `PetscSFDeregisterPersistent` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFDeregisterPersistent/> |
| `PetscSFDestroy` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFDestroy/> |
| `PetscSFDistributeSection` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFDistributeSection/> |
| `PetscSFDuplicate` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFDuplicate/> |
| `PetscSFFetchAndOpBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFFetchAndOpBegin/> |
| `PetscSFFetchAndOpEnd` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFFetchAndOpEnd/> |
| `PetscSFFetchAndOpWithMemTypeBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFFetchAndOpWithMemTypeBegin/> |
| `PetscSFFinalizePackage` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFFinalizePackage/> |
| `PetscSFGatherBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGatherBegin/> |
| `PetscSFGatherEnd` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGatherEnd/> |
| `PetscSFGetGraph` | Not Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetGraph/> |
| `PetscSFGetGraphLayout` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetGraphLayout/> |
| `PetscSFGetGroups` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetGroups/> |
| `PetscSFGetLeafRange` | Not Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetLeafRange/> |
| `PetscSFGetLeafRanks` | Not Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetLeafRanks/> |
| `PetscSFGetMultiSF` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetMultiSF/> |
| `PetscSFGetRanksSF` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetRanksSF/> |
| `PetscSFGetRootRanks` | Not Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetRootRanks/> |
| `PetscSFGetType` | Not Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFGetType/> |
| `PetscSFInitializePackage` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFInitializePackage/> |
| `PetscSFMerge` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFMerge/> |
| `PetscSFReduceBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFReduceBegin/> |
| `PetscSFReduceEnd` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFReduceEnd/> |
| `PetscSFReduceWithMemTypeBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFReduceWithMemTypeBegin/> |
| `PetscSFRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/PetscSF/PetscSFRegister/> |
| `PetscSFRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFRegisterAll/> |
| `PetscSFRegisterPersistent` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFRegisterPersistent/> |
| `PetscSFReset` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFReset/> |
| `PetscSFScatterBegin` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFScatterBegin/> |
| `PetscSFScatterEnd` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFScatterEnd/> |
| `PetscSFSetFromOptions` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetFromOptions/> |
| `PetscSFSetGraph` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraph/> |
| `PetscSFSetGraphFromCoordinates` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraphFromCoordinates/> |
| `PetscSFSetGraphLayout` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraphLayout/> |
| `PetscSFSetGraphWithPattern` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraphWithPattern/> |
| `PetscSFSetRankOrder` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetRankOrder/> |
| `PetscSFSetType` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetType/> |
| `PetscSFSetUp` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetUp/> |
| `PetscSFSetUpRanks` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFSetUpRanks/> |
| `PetscSFView` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFView/> |
| `PetscSFViewFromOptions` | Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFViewFromOptions/> |
| `PetscSFWindowGetFlavorType` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFWindowGetFlavorType/> |
| `PetscSFWindowGetInfo` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFWindowGetInfo/> |
| `PetscSFWindowGetSyncType` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFWindowGetSyncType/> |
| `PetscSFWindowSetFlavorType` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFWindowSetFlavorType/> |
| `PetscSFWindowSetInfo` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFWindowSetInfo/> |
| `PetscSFWindowSetSyncType` | Logically Collective | <https://petsc.org/release/manualpages/PetscSF/PetscSFWindowSetSyncType/> |

## PF

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PFAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/PF/PFAppendOptionsPrefix/> |
| `PFApply` | Collective | <https://petsc.org/release/manualpages/PF/PFApply/> |
| `PFApplyVec` | Collective | <https://petsc.org/release/manualpages/PF/PFApplyVec/> |
| `PFCreate` | Collective | <https://petsc.org/release/manualpages/PF/PFCreate/> |
| `PFDestroy` | Collective | <https://petsc.org/release/manualpages/PF/PFDestroy/> |
| `PFGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/PF/PFGetOptionsPrefix/> |
| `PFGetType` | Not Collective | <https://petsc.org/release/manualpages/PF/PFGetType/> |
| `PFRegister` | Not Collective | <https://petsc.org/release/manualpages/PF/PFRegister/> |
| `PFRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/PF/PFRegisterAll/> |
| `PFSet` | Collective | <https://petsc.org/release/manualpages/PF/PFSet/> |
| `PFSetFromOptions` | Collective | <https://petsc.org/release/manualpages/PF/PFSetFromOptions/> |
| `PFSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/PF/PFSetOptionsPrefix/> |
| `PFSetType` | Collective | <https://petsc.org/release/manualpages/PF/PFSetType/> |
| `PFStringSetFunction` | Collective | <https://petsc.org/release/manualpages/PF/PFStringSetFunction/> |
| `PFView` | Collective unless viewer is PETSC_VIEWER_STDOUT_SELF | <https://petsc.org/release/manualpages/PF/PFView/> |
| `PFViewFromOptions` | Collective | <https://petsc.org/release/manualpages/PF/PFViewFromOptions/> |

## Sensitivity

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `TSAdjointCostIntegral` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointCostIntegral/> |
| `TSAdjointMonitor` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitor/> |
| `TSAdjointMonitorCancel` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorCancel/> |
| `TSAdjointMonitorDrawSensi` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorDrawSensi/> |
| `TSAdjointMonitorSet` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorSet/> |
| `TSAdjointMonitorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorSetFromOptions/> |
| `TSAdjointReset` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointReset/> |
| `TSAdjointResetForward` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointResetForward/> |
| `TSAdjointSetForward` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetForward/> |
| `TSAdjointSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetFromOptions/> |
| `TSAdjointSetSteps` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetSteps/> |
| `TSAdjointSetUp` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetUp/> |
| `TSAdjointSolve` | Collective ` | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointSolve/> |
| `TSAdjointStep` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSAdjointStep/> |
| `TSComputeIHessianProductFunctionPP` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeIHessianProductFunctionPP/> |
| `TSComputeIHessianProductFunctionPU` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeIHessianProductFunctionPU/> |
| `TSComputeIHessianProductFunctionUP` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeIHessianProductFunctionUP/> |
| `TSComputeIHessianProductFunctionUU` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeIHessianProductFunctionUU/> |
| `TSComputeIJacobianP` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeIJacobianP/> |
| `TSComputeRHSHessianProductFunctionPP` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSHessianProductFunctionPP/> |
| `TSComputeRHSHessianProductFunctionPU` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSHessianProductFunctionPU/> |
| `TSComputeRHSHessianProductFunctionUP` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSHessianProductFunctionUP/> |
| `TSComputeRHSHessianProductFunctionUU` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSHessianProductFunctionUU/> |
| `TSComputeRHSJacobianP` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSJacobianP/> |
| `TSComputeSNESJacobian` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSComputeSNESJacobian/> |
| `TSForwardCostIntegral` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSForwardCostIntegral/> |
| `TSForwardGetSensitivities` | Not Collective, but Smat returned is parallel if ts is parallel | <https://petsc.org/release/manualpages/Sensitivity/TSForwardGetSensitivities/> |
| `TSForwardReset` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSForwardReset/> |
| `TSForwardSetInitialSensitivities` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSForwardSetInitialSensitivities/> |
| `TSForwardSetSensitivities` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSForwardSetSensitivities/> |
| `TSForwardSetUp` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSForwardSetUp/> |
| `TSForwardStep` | Collective | <https://petsc.org/release/manualpages/Sensitivity/TSForwardStep/> |
| `TSGetCostGradients` | Not Collective, but the vectors returned are parallel if TS is parallel | <https://petsc.org/release/manualpages/Sensitivity/TSGetCostGradients/> |
| `TSGetCostHessianProducts` | Not Collective, but vectors returned are parallel if TS is parallel | <https://petsc.org/release/manualpages/Sensitivity/TSGetCostHessianProducts/> |
| `TSGetCostIntegral` | Not Collective | <https://petsc.org/release/manualpages/Sensitivity/TSGetCostIntegral/> |
| `TSGetIJacobianP` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSGetIJacobianP/> |
| `TSGetRHSJacobianP` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSGetRHSJacobianP/> |
| `TSSetCostGradients` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSSetCostGradients/> |
| `TSSetCostHessianProducts` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSSetCostHessianProducts/> |
| `TSSetCostIntegrand` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSSetCostIntegrand/> |
| `TSSetIHessianProduct` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSSetIHessianProduct/> |
| `TSSetIJacobianP` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSSetIJacobianP/> |
| `TSSetRHSHessianProduct` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSSetRHSHessianProduct/> |
| `TSSetRHSJacobianP` | Logically Collective | <https://petsc.org/release/manualpages/Sensitivity/TSSetRHSJacobianP/> |

## SNES

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMCopyDMSNES` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMCopyDMSNES/> |
| `DMDASNESSetFunctionLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMDASNESSetFunctionLocal/> |
| `DMDASNESSetFunctionLocalVec` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMDASNESSetFunctionLocalVec/> |
| `DMDASNESSetJacobianLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMDASNESSetJacobianLocal/> |
| `DMDASNESSetJacobianLocalVec` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMDASNESSetJacobianLocalVec/> |
| `DMDASNESSetObjectiveLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMDASNESSetObjectiveLocal/> |
| `DMDASNESSetObjectiveLocalVec` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMDASNESSetObjectiveLocalVec/> |
| `DMDASNESSetPicardLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMDASNESSetPicardLocal/> |
| `DMDestroyVI` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMDestroyVI/> |
| `DMGetDMSNES` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMGetDMSNES/> |
| `DMGetDMSNESWrite` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMGetDMSNESWrite/> |
| `DMPlexSetSNESVariableBounds` | Collective | <https://petsc.org/release/manualpages/SNES/DMPlexSetSNESVariableBounds/> |
| `DMPlexSNESComputeResidualCEED` | Collective | <https://petsc.org/release/manualpages/SNES/DMPlexSNESComputeResidualCEED/> |
| `DMSetVI` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMSetVI/> |
| `DMSNESCreateJacobianMF` | Collective | <https://petsc.org/release/manualpages/SNES/DMSNESCreateJacobianMF/> |
| `DMSNESGetBoundaryLocal` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetBoundaryLocal/> |
| `DMSNESGetFunction` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetFunction/> |
| `DMSNESGetFunctionLocal` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetFunctionLocal/> |
| `DMSNESGetJacobian` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetJacobian/> |
| `DMSNESGetJacobianLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetJacobianLocal/> |
| `DMSNESGetNGS` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetNGS/> |
| `DMSNESGetObjective` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetObjective/> |
| `DMSNESGetObjectiveLocal` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetObjectiveLocal/> |
| `DMSNESGetPicard` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESGetPicard/> |
| `DMSNESSetBoundaryLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetBoundaryLocal/> |
| `DMSNESSetFunction` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetFunction/> |
| `DMSNESSetFunctionContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetFunctionContextDestroy/> |
| `DMSNESSetFunctionLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetFunctionLocal/> |
| `DMSNESSetJacobian` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetJacobian/> |
| `DMSNESSetJacobianContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetJacobianContextDestroy/> |
| `DMSNESSetJacobianLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetJacobianLocal/> |
| `DMSNESSetMFFunction` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetMFFunction/> |
| `DMSNESSetNGS` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetNGS/> |
| `DMSNESSetObjective` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetObjective/> |
| `DMSNESSetObjectiveLocal` | Logically Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetObjectiveLocal/> |
| `DMSNESSetPicard` | Not Collective | <https://petsc.org/release/manualpages/SNES/DMSNESSetPicard/> |
| `KSPMonitorSNESResidual` | Collective | <https://petsc.org/release/manualpages/SNES/KSPMonitorSNESResidual/> |
| `KSPMonitorSNESResidualDrawLG` | Collective | <https://petsc.org/release/manualpages/SNES/KSPMonitorSNESResidualDrawLG/> |
| `KSPMonitorSNESResidualDrawLGCreate` | Collective | <https://petsc.org/release/manualpages/SNES/KSPMonitorSNESResidualDrawLGCreate/> |
| `MatCreateSNESMF` | Collective | <https://petsc.org/release/manualpages/SNES/MatCreateSNESMF/> |
| `MatMFFDComputeJacobian` | Collective | <https://petsc.org/release/manualpages/SNES/MatMFFDComputeJacobian/> |
| `MatSNESMFGetReuseBase` | Logically Collective | <https://petsc.org/release/manualpages/SNES/MatSNESMFGetReuseBase/> |
| `MatSNESMFGetSNES` | Not Collective | <https://petsc.org/release/manualpages/SNES/MatSNESMFGetSNES/> |
| `MatSNESMFSetReuseBase` | Logically Collective | <https://petsc.org/release/manualpages/SNES/MatSNESMFSetReuseBase/> |
| `PetscConvEstComputeError` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstComputeError/> |
| `PetscConvEstComputeInitialGuess` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstComputeInitialGuess/> |
| `PetscConvEstCreate` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstCreate/> |
| `PetscConvEstDestroy` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstDestroy/> |
| `PetscConvEstGetConvRate` | Not Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstGetConvRate/> |
| `PetscConvEstGetSolver` | Not Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstGetSolver/> |
| `PetscConvEstMonitorDefault` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstMonitorDefault/> |
| `PetscConvEstRateView` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstRateView/> |
| `PetscConvEstSetFromOptions` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstSetFromOptions/> |
| `PetscConvEstSetSolver` | Not Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstSetSolver/> |
| `PetscConvEstSetUp` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstSetUp/> |
| `PetscConvEstView` | Collective | <https://petsc.org/release/manualpages/SNES/PetscConvEstView/> |
| `SNESAddOptionsChecker` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESAddOptionsChecker/> |
| `SNESAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESAppendOptionsPrefix/> |
| `SNESApplyNPC` | Collective | <https://petsc.org/release/manualpages/SNES/SNESApplyNPC/> |
| `SNESCheckFunctionDomainError` | Collective | <https://petsc.org/release/manualpages/SNES/SNESCheckFunctionDomainError/> |
| `SNESCompositeAddSNES` | Collective | <https://petsc.org/release/manualpages/SNES/SNESCompositeAddSNES/> |
| `SNESCompositeGetNumber` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESCompositeGetNumber/> |
| `SNESCompositeGetSNES` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESCompositeGetSNES/> |
| `SNESCompositeSetDamping` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESCompositeSetDamping/> |
| `SNESCompositeSetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESCompositeSetType/> |
| `SNESComputeFunction` | Collective | <https://petsc.org/release/manualpages/SNES/SNESComputeFunction/> |
| `SNESComputeFunctionDefaultNPC` | Collective | <https://petsc.org/release/manualpages/SNES/SNESComputeFunctionDefaultNPC/> |
| `SNESComputeJacobian` | Collective | <https://petsc.org/release/manualpages/SNES/SNESComputeJacobian/> |
| `SNESComputeJacobianDefault` | Collective | <https://petsc.org/release/manualpages/SNES/SNESComputeJacobianDefault/> |
| `SNESComputeJacobianDefaultColor` | Collective | <https://petsc.org/release/manualpages/SNES/SNESComputeJacobianDefaultColor/> |
| `SNESComputeMFFunction` | Collective | <https://petsc.org/release/manualpages/SNES/SNESComputeMFFunction/> |
| `SNESComputeNGS` | Collective | <https://petsc.org/release/manualpages/SNES/SNESComputeNGS/> |
| `SNESComputeObjective` | Collective | <https://petsc.org/release/manualpages/SNES/SNESComputeObjective/> |
| `SNESConverged` | Collective | <https://petsc.org/release/manualpages/SNES/SNESConverged/> |
| `SNESConvergedCorrectPressure` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESConvergedCorrectPressure/> |
| `SNESConvergedDefault` | Collective | <https://petsc.org/release/manualpages/SNES/SNESConvergedDefault/> |
| `SNESConvergedReasonView` | Collective | <https://petsc.org/release/manualpages/SNES/SNESConvergedReasonView/> |
| `SNESConvergedReasonViewCancel` | Collective | <https://petsc.org/release/manualpages/SNES/SNESConvergedReasonViewCancel/> |
| `SNESConvergedReasonViewFromOptions` | Collective | <https://petsc.org/release/manualpages/SNES/SNESConvergedReasonViewFromOptions/> |
| `SNESConvergedReasonViewSet` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESConvergedReasonViewSet/> |
| `SNESConvergedSkip` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESConvergedSkip/> |
| `SNESCreate` | Collective | <https://petsc.org/release/manualpages/SNES/SNESCreate/> |
| `SNESDestroy` | Collective | <https://petsc.org/release/manualpages/SNES/SNESDestroy/> |
| `SNESGetAlwaysComputesFinalResidual` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESGetAlwaysComputesFinalResidual/> |
| `SNESGetApplicationContext` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetApplicationContext/> |
| `SNESGetCheckJacobianDomainError` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESGetCheckJacobianDomainError/> |
| `SNESGetConvergedReason` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetConvergedReason/> |
| `SNESGetConvergedReasonString` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetConvergedReasonString/> |
| `SNESGetConvergenceHistory` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetConvergenceHistory/> |
| `SNESGetDivergenceTolerance` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetDivergenceTolerance/> |
| `SNESGetDM` | Not Collective but dm obtained is parallel on snes | <https://petsc.org/release/manualpages/SNES/SNESGetDM/> |
| `SNESGetErrorIfNotConverged` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetErrorIfNotConverged/> |
| `SNESGetForceIteration` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESGetForceIteration/> |
| `SNESGetFunction` | Not Collective, but r is parallel if snes is parallel. Collective if r is requested, but has not been created yet. | <https://petsc.org/release/manualpages/SNES/SNESGetFunction/> |
| `SNESGetFunctionNorm` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetFunctionNorm/> |
| `SNESGetFunctionType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESGetFunctionType/> |
| `SNESGetGridSequence` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESGetGridSequence/> |
| `SNESGetIterationNumber` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetIterationNumber/> |
| `SNESGetJacobian` | Not Collective, but Mat object will be parallel if SNES is | <https://petsc.org/release/manualpages/SNES/SNESGetJacobian/> |
| `SNESGetKSP` | Not Collective, but if snes is parallel, then ksp is parallel | <https://petsc.org/release/manualpages/SNES/SNESGetKSP/> |
| `SNESGetLagJacobian` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetLagJacobian/> |
| `SNESGetLagPreconditioner` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetLagPreconditioner/> |
| `SNESGetLinearSolveFailures` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetLinearSolveFailures/> |
| `SNESGetLinearSolveIterations` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetLinearSolveIterations/> |
| `SNESGetLineSearch` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetLineSearch/> |
| `SNESGetMaxLinearSolveFailures` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetMaxLinearSolveFailures/> |
| `SNESGetMaxNonlinearStepFailures` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetMaxNonlinearStepFailures/> |
| `SNESGetNonlinearStepFailures` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetNonlinearStepFailures/> |
| `SNESGetNormSchedule` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESGetNormSchedule/> |
| `SNESGetNPC` | Not Collective; but any changes to the obtained the pc object must be applied collectively | <https://petsc.org/release/manualpages/SNES/SNESGetNPC/> |
| `SNESGetNPCFunction` | Collective | <https://petsc.org/release/manualpages/SNES/SNESGetNPCFunction/> |
| `SNESGetNPCSide` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetNPCSide/> |
| `SNESGetNumberFunctionEvals` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetNumberFunctionEvals/> |
| `SNESGetObjective` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetObjective/> |
| `SNESGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetOptionsPrefix/> |
| `SNESGetPicard` | Not Collective, but Vec is parallel if SNES is parallel. Collective if Vec is requested, but has not been created yet. | <https://petsc.org/release/manualpages/SNES/SNESGetPicard/> |
| `SNESGetRhs` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESGetRhs/> |
| `SNESGetSolution` | Not Collective, but x is parallel if snes is parallel | <https://petsc.org/release/manualpages/SNES/SNESGetSolution/> |
| `SNESGetSolutionNorm` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetSolutionNorm/> |
| `SNESGetSolutionUpdate` | Not Collective, but x is parallel if snes is parallel | <https://petsc.org/release/manualpages/SNES/SNESGetSolutionUpdate/> |
| `SNESGetTolerances` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetTolerances/> |
| `SNESGetType` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetType/> |
| `SNESGetUpdateNorm` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESGetUpdateNorm/> |
| `SNESGetUseMatrixFree` | Not Collective, but the resulting flags will be the same on all MPI processes | <https://petsc.org/release/manualpages/SNES/SNESGetUseMatrixFree/> |
| `SNESHasNPC` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESHasNPC/> |
| `SNESKSPGetParametersEW` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESKSPGetParametersEW/> |
| `SNESKSPGetUseEW` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESKSPGetUseEW/> |
| `SNESKSPSetParametersEW` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESKSPSetParametersEW/> |
| `SNESKSPSetUseEW` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESKSPSetUseEW/> |
| `SNESLineSearchAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchAppendOptionsPrefix/> |
| `SNESLineSearchApply` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchApply/> |
| `SNESLineSearchCreate` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchCreate/> |
| `SNESLineSearchDestroy` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchDestroy/> |
| `SNESLineSearchGetDefaultMonitor` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetDefaultMonitor/> |
| `SNESLineSearchGetLambda` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetLambda/> |
| `SNESLineSearchGetNorms` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetNorms/> |
| `SNESLineSearchGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetOptionsPrefix/> |
| `SNESLineSearchGetSNES` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetSNES/> |
| `SNESLineSearchGetTolerances` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetTolerances/> |
| `SNESLineSearchGetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetType/> |
| `SNESLineSearchGetVecs` | Not Collective but the vectors are parallel | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetVecs/> |
| `SNESLineSearchGetVIFunctions` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchGetVIFunctions/> |
| `SNESLineSearchMonitor` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitor/> |
| `SNESLineSearchMonitorCancel` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitorCancel/> |
| `SNESLineSearchMonitorSet` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitorSet/> |
| `SNESLineSearchMonitorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitorSetFromOptions/> |
| `SNESLineSearchMonitorSolutionUpdate` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitorSolutionUpdate/> |
| `SNESLineSearchPostCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchPostCheck/> |
| `SNESLineSearchPreCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchPreCheck/> |
| `SNESLineSearchPreCheckPicard` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchPreCheckPicard/> |
| `SNESLineSearchRegister` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/SNES/SNESLineSearchRegister/> |
| `SNESLineSearchRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchRegisterAll/> |
| `SNESLineSearchReset` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchReset/> |
| `SNESLineSearchSetDefaultMonitor` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetDefaultMonitor/> |
| `SNESLineSearchSetFromOptions` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetFromOptions/> |
| `SNESLineSearchSetNorms` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetNorms/> |
| `SNESLineSearchSetPostCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetPostCheck/> |
| `SNESLineSearchSetPreCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetPreCheck/> |
| `SNESLineSearchSetReason` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetReason/> |
| `SNESLineSearchSetTolerances` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetTolerances/> |
| `SNESLineSearchSetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetType/> |
| `SNESLineSearchSetUp` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetUp/> |
| `SNESLineSearchSetVecs` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetVecs/> |
| `SNESLineSearchSetVIFunctions` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchSetVIFunctions/> |
| `SNESLineSearchShellGetApply` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchShellGetApply/> |
| `SNESLineSearchShellSetApply` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchShellSetApply/> |
| `SNESLineSearchView` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESLineSearchView/> |
| `SNESLoad` | Collective | <https://petsc.org/release/manualpages/SNES/SNESLoad/> |
| `SNESMonitor` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitor/> |
| `SNESMonitorCancel` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorCancel/> |
| `SNESMonitorDefault` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorDefault/> |
| `SNESMonitorDefaultField` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorDefaultField/> |
| `SNESMonitorDefaultSetUp` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorDefaultSetUp/> |
| `SNESMonitorFields` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorFields/> |
| `SNESMonitorFunction` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorFunction/> |
| `SNESMonitorJacUpdateSpectrum` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorJacUpdateSpectrum/> |
| `SNESMonitorLGRange` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorLGRange/> |
| `SNESMonitorRange` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorRange/> |
| `SNESMonitorRatio` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorRatio/> |
| `SNESMonitorRatioSetUp` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorRatioSetUp/> |
| `SNESMonitorResidual` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorResidual/> |
| `SNESMonitorSAWs` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorSAWs/> |
| `SNESMonitorSAWsCreate` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorSAWsCreate/> |
| `SNESMonitorSAWsDestroy` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorSAWsDestroy/> |
| `SNESMonitorScaling` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorScaling/> |
| `SNESMonitorSet` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorSet/> |
| `SNESMonitorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorSetFromOptions/> |
| `SNESMonitorSolution` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorSolution/> |
| `SNESMonitorSolutionUpdate` | Collective | <https://petsc.org/release/manualpages/SNES/SNESMonitorSolutionUpdate/> |
| `SNESMSGetDamping` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESMSGetDamping/> |
| `SNESMSGetType` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESMSGetType/> |
| `SNESMSRegister` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/SNES/SNESMSRegister/> |
| `SNESMSRegisterAll` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMSRegisterAll/> |
| `SNESMSRegisterDestroy` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMSRegisterDestroy/> |
| `SNESMSSetDamping` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMSSetDamping/> |
| `SNESMSSetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMSSetType/> |
| `SNESMultiblockGetSubSNES` | Not Collective but each SNES obtained is parallel | <https://petsc.org/release/manualpages/SNES/SNESMultiblockGetSubSNES/> |
| `SNESMultiblockSetBlockSize` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMultiblockSetBlockSize/> |
| `SNESMultiblockSetFields` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMultiblockSetFields/> |
| `SNESMultiblockSetIS` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMultiblockSetIS/> |
| `SNESMultiblockSetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESMultiblockSetType/> |
| `SNESNASMGetDamping` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMGetDamping/> |
| `SNESNASMGetNumber` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMGetNumber/> |
| `SNESNASMGetSNES` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMGetSNES/> |
| `SNESNASMGetSubdomains` | Not Collective but some of the objects returned will be parallel | <https://petsc.org/release/manualpages/SNES/SNESNASMGetSubdomains/> |
| `SNESNASMGetSubdomainVecs` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMGetSubdomainVecs/> |
| `SNESNASMGetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMGetType/> |
| `SNESNASMSetComputeFinalJacobian` | Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMSetComputeFinalJacobian/> |
| `SNESNASMSetDamping` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMSetDamping/> |
| `SNESNASMSetSubdomains` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMSetSubdomains/> |
| `SNESNASMSetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMSetType/> |
| `SNESNASMSetWeight` | Collective | <https://petsc.org/release/manualpages/SNES/SNESNASMSetWeight/> |
| `SNESNCGSetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNCGSetType/> |
| `SNESNewtonALComputeFunction` | Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonALComputeFunction/> |
| `SNESNewtonALGetFunction` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonALGetFunction/> |
| `SNESNewtonALGetLoadParameter` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonALGetLoadParameter/> |
| `SNESNewtonALSetCorrectionType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonALSetCorrectionType/> |
| `SNESNewtonALSetDiagonalScaling` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonALSetDiagonalScaling/> |
| `SNESNewtonALSetFunction` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonALSetFunction/> |
| `SNESNewtonTRDCGetPostCheck` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCGetPostCheck/> |
| `SNESNewtonTRDCGetPreCheck` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCGetPreCheck/> |
| `SNESNewtonTRDCGetRhoFlag` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCGetRhoFlag/> |
| `SNESNewtonTRDCPostCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCPostCheck/> |
| `SNESNewtonTRDCPreCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCPreCheck/> |
| `SNESNewtonTRDCSetPostCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCSetPostCheck/> |
| `SNESNewtonTRDCSetPreCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCSetPreCheck/> |
| `SNESNewtonTRGetPostCheck` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRGetPostCheck/> |
| `SNESNewtonTRGetPreCheck` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRGetPreCheck/> |
| `SNESNewtonTRGetTolerances` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRGetTolerances/> |
| `SNESNewtonTRGetUpdateParameters` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRGetUpdateParameters/> |
| `SNESNewtonTRPostCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRPostCheck/> |
| `SNESNewtonTRPreCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRPreCheck/> |
| `SNESNewtonTRSetPostCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetPostCheck/> |
| `SNESNewtonTRSetPreCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetPreCheck/> |
| `SNESNewtonTRSetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetTolerances/> |
| `SNESNewtonTRSetUpdateParameters` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetUpdateParameters/> |
| `SNESNGMRESGetRestartFmRise` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNGMRESGetRestartFmRise/> |
| `SNESNGMRESSetRestartType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNGMRESSetRestartType/> |
| `SNESNGMRESSetSelectType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNGMRESSetSelectType/> |
| `SNESNGSGetTolerances` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESNGSGetTolerances/> |
| `SNESNGSSetSweeps` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNGSSetSweeps/> |
| `SNESNGSSetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESNGSSetTolerances/> |
| `SNESObjectiveComputeFunctionDefaultFD` | Collective | <https://petsc.org/release/manualpages/SNES/SNESObjectiveComputeFunctionDefaultFD/> |
| `SNESParametersInitialize` | Collective | <https://petsc.org/release/manualpages/SNES/SNESParametersInitialize/> |
| `SNESPatchSetCellNumbering` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESPatchSetCellNumbering/> |
| `SNESPatchSetComputeFunction` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESPatchSetComputeFunction/> |
| `SNESPatchSetComputeOperator` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESPatchSetComputeOperator/> |
| `SNESPatchSetConstructType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESPatchSetConstructType/> |
| `SNESPatchSetDiscretisationInfo` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESPatchSetDiscretisationInfo/> |
| `SNESPicardComputeFunction` | Collective | <https://petsc.org/release/manualpages/SNES/SNESPicardComputeFunction/> |
| `SNESPicardComputeJacobian` | Collective | <https://petsc.org/release/manualpages/SNES/SNESPicardComputeJacobian/> |
| `SNESPicardComputeMFFunction` | Collective | <https://petsc.org/release/manualpages/SNES/SNESPicardComputeMFFunction/> |
| `SNESPruneJacobianColor` | Collective | <https://petsc.org/release/manualpages/SNES/SNESPruneJacobianColor/> |
| `SNESPythonGetType` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESPythonGetType/> |
| `SNESPythonSetType` | Collective | <https://petsc.org/release/manualpages/SNES/SNESPythonSetType/> |
| `SNESQNSetRestartType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESQNSetRestartType/> |
| `SNESQNSetScaleType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESQNSetScaleType/> |
| `SNESQNSetType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESQNSetType/> |
| `SNESRegister` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESRegister/> |
| `SNESRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESRegisterAll/> |
| `SNESReset` | Collective | <https://petsc.org/release/manualpages/SNES/SNESReset/> |
| `SNESResetCounters` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESResetCounters/> |
| `SNESResetFromOptions` | Collective | <https://petsc.org/release/manualpages/SNES/SNESResetFromOptions/> |
| `SNESSetAlwaysComputesFinalResidual` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetAlwaysComputesFinalResidual/> |
| `SNESSetApplicationContext` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetApplicationContext/> |
| `SNESSetCheckJacobianDomainError` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetCheckJacobianDomainError/> |
| `SNESSetComputeApplicationContext` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/SNES/SNESSetComputeApplicationContext/> |
| `SNESSetComputeInitialGuess` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetComputeInitialGuess/> |
| `SNESSetConvergedReason` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESSetConvergedReason/> |
| `SNESSetConvergenceHistory` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetConvergenceHistory/> |
| `SNESSetConvergenceTest` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetConvergenceTest/> |
| `SNESSetCountersReset` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetCountersReset/> |
| `SNESSetDivergenceTolerance` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetDivergenceTolerance/> |
| `SNESSetDM` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetDM/> |
| `SNESSetErrorIfNotConverged` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetErrorIfNotConverged/> |
| `SNESSetForceIteration` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetForceIteration/> |
| `SNESSetFromOptions` | Collective | <https://petsc.org/release/manualpages/SNES/SNESSetFromOptions/> |
| `SNESSetFunction` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetFunction/> |
| `SNESSetFunctionDomainError` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESSetFunctionDomainError/> |
| `SNESSetFunctionNorm` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetFunctionNorm/> |
| `SNESSetFunctionType` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetFunctionType/> |
| `SNESSetGridSequence` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetGridSequence/> |
| `SNESSetInitialFunction` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetInitialFunction/> |
| `SNESSetIterationNumber` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESSetIterationNumber/> |
| `SNESSetJacobian` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetJacobian/> |
| `SNESSetJacobianDomainError` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetJacobianDomainError/> |
| `SNESSetKSP` | Not Collective, but the SNES and KSP objects must live on the same MPI_Comm | <https://petsc.org/release/manualpages/SNES/SNESSetKSP/> |
| `SNESSetLagJacobian` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetLagJacobian/> |
| `SNESSetLagJacobianPersists` | Logically collective | <https://petsc.org/release/manualpages/SNES/SNESSetLagJacobianPersists/> |
| `SNESSetLagPreconditioner` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetLagPreconditioner/> |
| `SNESSetLagPreconditionerPersists` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetLagPreconditionerPersists/> |
| `SNESSetLineSearch` | Collective | <https://petsc.org/release/manualpages/SNES/SNESSetLineSearch/> |
| `SNESSetMaxLinearSolveFailures` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetMaxLinearSolveFailures/> |
| `SNESSetMaxNonlinearStepFailures` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESSetMaxNonlinearStepFailures/> |
| `SNESSetNormSchedule` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetNormSchedule/> |
| `SNESSetNPC` | Collective | <https://petsc.org/release/manualpages/SNES/SNESSetNPC/> |
| `SNESSetNPCSide` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetNPCSide/> |
| `SNESSetObjective` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetObjective/> |
| `SNESSetObjectiveDomainError` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESSetObjectiveDomainError/> |
| `SNESSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetOptionsPrefix/> |
| `SNESSetPicard` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetPicard/> |
| `SNESSetSolution` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetSolution/> |
| `SNESSetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetTolerances/> |
| `SNESSetTrustRegionTolerance` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetTrustRegionTolerance/> |
| `SNESSetType` | Collective | <https://petsc.org/release/manualpages/SNES/SNESSetType/> |
| `SNESSetUp` | Collective | <https://petsc.org/release/manualpages/SNES/SNESSetUp/> |
| `SNESSetUpdate` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetUpdate/> |
| `SNESSetUpMatrices` | Collective | <https://petsc.org/release/manualpages/SNES/SNESSetUpMatrices/> |
| `SNESSetUseMatrixFree` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESSetUseMatrixFree/> |
| `SNESShellGetContext` | Not Collective | <https://petsc.org/release/manualpages/SNES/SNESShellGetContext/> |
| `SNESShellSetContext` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESShellSetContext/> |
| `SNESShellSetSolve` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESShellSetSolve/> |
| `SNESSolve` | Collective | <https://petsc.org/release/manualpages/SNES/SNESSolve/> |
| `SNESTestFunction` | Collective | <https://petsc.org/release/manualpages/SNES/SNESTestFunction/> |
| `SNESTestJacobian` | Collective | <https://petsc.org/release/manualpages/SNES/SNESTestJacobian/> |
| `SNESTestLocalMin` | Collective | <https://petsc.org/release/manualpages/SNES/SNESTestLocalMin/> |
| `SNESView` | Collective | <https://petsc.org/release/manualpages/SNES/SNESView/> |
| `SNESViewFromOptions` | Collective | <https://petsc.org/release/manualpages/SNES/SNESViewFromOptions/> |
| `SNESVISetRedundancyCheck` | Logically Collective | <https://petsc.org/release/manualpages/SNES/SNESVISetRedundancyCheck/> |

## SNESFAS

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `SNESFASCreateCoarseVec` | Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCreateCoarseVec/> |
| `SNESFASCycleGetCorrection` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetCorrection/> |
| `SNESFASCycleGetInjection` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetInjection/> |
| `SNESFASCycleGetInterpolation` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetInterpolation/> |
| `SNESFASCycleGetRestriction` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetRestriction/> |
| `SNESFASCycleGetRScale` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetRScale/> |
| `SNESFASCycleGetSmoother` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetSmoother/> |
| `SNESFASCycleGetSmootherDown` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetSmootherDown/> |
| `SNESFASCycleGetSmootherUp` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetSmootherUp/> |
| `SNESFASCycleIsFine` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleIsFine/> |
| `SNESFASCycleSetCycles` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleSetCycles/> |
| `SNESFASFullGetTotal` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASFullGetTotal/> |
| `SNESFASFullSetDownSweep` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASFullSetDownSweep/> |
| `SNESFASFullSetTotal` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASFullSetTotal/> |
| `SNESFASGalerkinFunctionDefault` | Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASGalerkinFunctionDefault/> |
| `SNESFASGetGalerkin` | Not Collective but the result would be the same on all MPI processes | <https://petsc.org/release/manualpages/SNESFAS/SNESFASGetGalerkin/> |
| `SNESFASGetType` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASGetType/> |
| `SNESFASRestrict` | Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASRestrict/> |
| `SNESFASSetContinuation` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASSetContinuation/> |
| `SNESFASSetCycles` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASSetCycles/> |
| `SNESFASSetGalerkin` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASSetGalerkin/> |
| `SNESFASSetLog` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASSetLog/> |
| `SNESFASSetMonitor` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASSetMonitor/> |
| `SNESFASSetNumberSmoothDown` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASSetNumberSmoothDown/> |
| `SNESFASSetNumberSmoothUp` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASSetNumberSmoothUp/> |
| `SNESFASSetType` | Logically Collective | <https://petsc.org/release/manualpages/SNESFAS/SNESFASSetType/> |

## SPACE

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PetscSpaceCreate` | Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceCreate/> |
| `PetscSpaceDestroy` | Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceDestroy/> |
| `PetscSpaceGetHeightSubspace` | Not Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceGetHeightSubspace/> |
| `PetscSpaceGetType` | Not Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceGetType/> |
| `PetscSpacePointGetPoints` | Logically Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpacePointGetPoints/> |
| `PetscSpacePointSetPoints` | Logically Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpacePointSetPoints/> |
| `PetscSpaceRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/SPACE/PetscSpaceRegister/> |
| `PetscSpaceSetFromOptions` | Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceSetFromOptions/> |
| `PetscSpaceSetType` | Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceSetType/> |
| `PetscSpaceSetUp` | Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceSetUp/> |
| `PetscSpaceSumGetInterleave` | Logically collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceSumGetInterleave/> |
| `PetscSpaceSumSetInterleave` | Logically collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceSumSetInterleave/> |
| `PetscSpaceView` | Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceView/> |
| `PetscSpaceViewFromOptions` | Collective | <https://petsc.org/release/manualpages/SPACE/PetscSpaceViewFromOptions/> |

## Sys

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `CHKERRA` | Not Collective | <https://petsc.org/release/manualpages/Sys/CHKERRA/> |
| `CHKERRABORT` | Not Collective | <https://petsc.org/release/manualpages/Sys/CHKERRABORT/> |
| `CHKERRCXX` | Not Collective | <https://petsc.org/release/manualpages/Sys/CHKERRCXX/> |
| `CHKERRMPI` | Not Collective | <https://petsc.org/release/manualpages/Sys/CHKERRMPI/> |
| `CHKERRQ` | Not Collective | <https://petsc.org/release/manualpages/Sys/CHKERRQ/> |
| `CHKERRXX` | Not Collective | <https://petsc.org/release/manualpages/Sys/CHKERRXX/> |
| `CHKMEMQ` | Not Collective | <https://petsc.org/release/manualpages/Sys/CHKMEMQ/> |
| `MPIU_Allreduce` | Collective | <https://petsc.org/release/manualpages/Sys/MPIU_Allreduce/> |
| `MPIU_Scatterv` | Collective | <https://petsc.org/release/manualpages/Sys/MPIU_Scatterv/> |
| `PCMPIServerAddressesDestroy` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PCMPIServerAddressesDestroy/> |
| `PETSCABORT` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PETSCABORT/> |
| `PetscAbortErrorHandler` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAbortErrorHandler/> |
| `PetscAbs` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscAbs/> |
| `PetscAbsComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAbsComplex/> |
| `PetscAbsScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAbsScalar/> |
| `PetscAcosComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAcosComplex/> |
| `PetscAcoshComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAcoshComplex/> |
| `PetscAcoshReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAcoshReal/> |
| `PetscAcoshScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAcoshScalar/> |
| `PetscAcosReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAcosReal/> |
| `PetscAcosScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAcosScalar/> |
| `PetscAddrAlign` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscAddrAlign/> |
| `PetscApproximateGTE` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscApproximateGTE/> |
| `PetscApproximateLTE` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscApproximateLTE/> |
| `PetscArgComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscArgComplex/> |
| `PetscArgScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscArgScalar/> |
| `PetscArraycmp` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscArraycmp/> |
| `PetscArraycpy` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscArraycpy/> |
| `PetscArraymove` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscArraymove/> |
| `PetscArrayzero` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscArrayzero/> |
| `PetscAsinComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAsinComplex/> |
| `PetscAsinhComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAsinhComplex/> |
| `PetscAsinhReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAsinhReal/> |
| `PetscAsinhScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAsinhScalar/> |
| `PetscAsinReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAsinReal/> |
| `PetscAsinScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAsinScalar/> |
| `PetscAssert` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAssert/> |
| `PetscAssertAbort` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAssertAbort/> |
| `PetscAtan2Real` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAtan2Real/> |
| `PetscAtanComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAtanComplex/> |
| `PetscAtanhComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAtanhComplex/> |
| `PetscAtanhReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAtanhReal/> |
| `PetscAtanhScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAtanhScalar/> |
| `PetscAtanReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAtanReal/> |
| `PetscAtanScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAtanScalar/> |
| `PetscAttachDebugger` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscAttachDebugger/> |
| `PetscAttachDebuggerErrorHandler` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscAttachDebuggerErrorHandler/> |
| `PetscBasename` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBasename/> |
| `PetscBinaryClose` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscBinaryClose/> |
| `PetscBinaryOpen` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscBinaryOpen/> |
| `PetscBinaryRead` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscBinaryRead/> |
| `PetscBinarySeek` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBinarySeek/> |
| `PetscBinarySynchronizedRead` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBinarySynchronizedRead/> |
| `PetscBinarySynchronizedWrite` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBinarySynchronizedWrite/> |
| `PetscBinaryWrite` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscBinaryWrite/> |
| `PetscBLASIntCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBLASIntCast/> |
| `PetscBoxAuthorize` | Not Collective, only the first rank in MPI_Comm does anything | <https://petsc.org/release/manualpages/Sys/PetscBoxAuthorize/> |
| `PetscBoxRefresh` | Not Collective, only the first process in the MPI_Comm does anything | <https://petsc.org/release/manualpages/Sys/PetscBoxRefresh/> |
| `PetscBoxUpload` | Not collective, only the first process in the MPI_Comm uploads the file | <https://petsc.org/release/manualpages/Sys/PetscBoxUpload/> |
| `PetscBTClear` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTClear/> |
| `PetscBTCopy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTCopy/> |
| `PetscBTCountSet` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTCountSet/> |
| `PetscBTCreate` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTCreate/> |
| `PetscBTDestroy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTDestroy/> |
| `PetscBTLength` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTLength/> |
| `PetscBTLookup` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTLookup/> |
| `PetscBTLookupClear` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTLookupClear/> |
| `PetscBTLookupSet` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTLookupSet/> |
| `PetscBTMemzero` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTMemzero/> |
| `PetscBTNegate` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTNegate/> |
| `PetscBTSet` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscBTSet/> |
| `PetscByteSwap` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscByteSwap/> |
| `PetscCall` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCall/> |
| `PetscCallA` | Collective | <https://petsc.org/release/manualpages/Sys/PetscCallA/> |
| `PetscCallAbort` | Collective | <https://petsc.org/release/manualpages/Sys/PetscCallAbort/> |
| `PetscCallBack` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCallBack/> |
| `PetscCallBLAS` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCallBLAS/> |
| `PetscCallCXX` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCallCXX/> |
| `PetscCallCXXAbort` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCallCXXAbort/> |
| `PetscCallMPI` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCallMPI/> |
| `PetscCallMPIAbort` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCallMPIAbort/> |
| `PetscCallMPINull` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCallMPINull/> |
| `PetscCallMPIReturnMPI` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCallMPIReturnMPI/> |
| `PetscCallNull` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCallNull/> |
| `PetscCalloc` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCalloc/> |
| `PetscCalloc1` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCalloc1/> |
| `PetscCalloc2` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCalloc2/> |
| `PetscCalloc3` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCalloc3/> |
| `PetscCalloc4` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCalloc4/> |
| `PetscCalloc5` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCalloc5/> |
| `PetscCalloc6` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCalloc6/> |
| `PetscCalloc7` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCalloc7/> |
| `PetscCallReturnMPI` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCallReturnMPI/> |
| `PetscCallThrow` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCallThrow/> |
| `PetscCallVoid` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCallVoid/> |
| `PetscCbrtReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCbrtReal/> |
| `PetscCeilInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCeilInt/> |
| `PetscCeilInt64` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCeilInt64/> |
| `PetscCeilReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCeilReal/> |
| `PetscCheck` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCheck/> |
| `PetscCheckAbort` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCheckAbort/> |
| `PetscCheckDupsInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCheckDupsInt/> |
| `PetscCheckPointer` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCheckPointer/> |
| `PetscCheckPointerSetIntensity` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscCheckPointerSetIntensity/> |
| `PetscCheckReturnMPI` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCheckReturnMPI/> |
| `PetscCIFilename` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCIFilename/> |
| `PetscCILinenumber` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCILinenumber/> |
| `PetscCIntCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCIntCast/> |
| `PetscCitationsRegister` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCitationsRegister/> |
| `PetscClipInterval` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscClipInterval/> |
| `PetscCommBuildTwoSided` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCommBuildTwoSided/> |
| `PetscCommBuildTwoSidedF` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCommBuildTwoSidedF/> |
| `PetscCommBuildTwoSidedFReq` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCommBuildTwoSidedFReq/> |
| `PetscCommBuildTwoSidedGetType` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscCommBuildTwoSidedGetType/> |
| `PetscCommBuildTwoSidedSetType` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscCommBuildTwoSidedSetType/> |
| `PetscCommDestroy` | Collective | <https://petsc.org/release/manualpages/Sys/PetscCommDestroy/> |
| `PetscCommDuplicate` | Collective | <https://petsc.org/release/manualpages/Sys/PetscCommDuplicate/> |
| `PetscCommGetComm` | Collective | <https://petsc.org/release/manualpages/Sys/PetscCommGetComm/> |
| `PetscCommGetNewTag` | Collective | <https://petsc.org/release/manualpages/Sys/PetscCommGetNewTag/> |
| `PetscCommRestoreComm` | Collective | <https://petsc.org/release/manualpages/Sys/PetscCommRestoreComm/> |
| `PetscConj` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscConj/> |
| `PetscConjComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscConjComplex/> |
| `PetscContainerCreate` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscContainerCreate/> |
| `PetscContainerDestroy` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscContainerDestroy/> |
| `PetscContainerGetPointer` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscContainerGetPointer/> |
| `PetscContainerSetCtxDestroy` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscContainerSetCtxDestroy/> |
| `PetscContainerSetPointer` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscContainerSetPointer/> |
| `PetscContainerSetUserDestroy` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscContainerSetUserDestroy/> |
| `PetscCopysignReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCopysignReal/> |
| `PetscCosComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCosComplex/> |
| `PetscCoshComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCoshComplex/> |
| `PetscCoshReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCoshReal/> |
| `PetscCoshScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCoshScalar/> |
| `PetscCosReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCosReal/> |
| `PetscCosScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCosScalar/> |
| `PetscCUBLASGetHandle` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCUBLASGetHandle/> |
| `PetscCuBLASIntCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCuBLASIntCast/> |
| `PetscCUSOLVERDnGetHandle` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscCUSOLVERDnGetHandle/> |
| `PetscDataTypeFromString` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscDataTypeFromString/> |
| `PetscDataTypeGetSize` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscDataTypeGetSize/> |
| `PetscDataTypeToMPIDataType` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscDataTypeToMPIDataType/> |
| `PetscDemangleSymbol` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscDemangleSymbol/> |
| `PetscDetermineInitialFPTrap` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscDetermineInitialFPTrap/> |
| `PetscDLAddr` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLAddr/> |
| `PetscDLClose` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLClose/> |
| `PetscDLLibraryAppend` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLLibraryAppend/> |
| `PetscDLLibraryClose` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLLibraryClose/> |
| `PetscDLLibraryOpen` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLLibraryOpen/> |
| `PetscDLLibraryPrepend` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLLibraryPrepend/> |
| `PetscDLLibraryPrintPath` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscDLLibraryPrintPath/> |
| `PetscDLLibraryRetrieve` | Collective | <https://petsc.org/release/manualpages/Sys/PetscDLLibraryRetrieve/> |
| `PetscDLLibrarySym` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLLibrarySym/> |
| `PetscDLOpen` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLOpen/> |
| `PetscDLSym` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscDLSym/> |
| `PetscElementalFinalizePackage` | Collective on MPI_COMM_WORLD , not PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Sys/PetscElementalFinalizePackage/> |
| `PetscElementalInitialized` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscElementalInitialized/> |
| `PetscElementalInitializePackage` | Collective on MPI_COMM_WORLD , not PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Sys/PetscElementalInitializePackage/> |
| `PetscEListFind` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscEListFind/> |
| `PetscEmacsClientErrorHandler` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscEmacsClientErrorHandler/> |
| `PetscEnd` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Sys/PetscEnd/> |
| `PetscEnumFind` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscEnumFind/> |
| `PetscErfReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscErfReal/> |
| `PetscError` | Collective | <https://petsc.org/release/manualpages/Sys/PetscError/> |
| `PetscErrorMessage` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscErrorMessage/> |
| `PetscErrorPrintf` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscErrorPrintf/> |
| `PetscErrorPrintfInitialize` | Collective | <https://petsc.org/release/manualpages/Sys/PetscErrorPrintfInitialize/> |
| `PetscExpComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscExpComplex/> |
| `PetscExpReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscExpReal/> |
| `PetscExpScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscExpScalar/> |
| `PetscFClose` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscFClose/> |
| `PetscFileRetrieve` | Collective | <https://petsc.org/release/manualpages/Sys/PetscFileRetrieve/> |
| `PetscFinalize` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Sys/PetscFinalize/> |
| `PetscFindCount` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFindCount/> |
| `PetscFindInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFindInt/> |
| `PetscFindMPIInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFindMPIInt/> |
| `PetscFindReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFindReal/> |
| `PetscFixFilename` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFixFilename/> |
| `PetscFloorReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFloorReal/> |
| `PetscFmodReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFmodReal/> |
| `PetscFOpen` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscFOpen/> |
| `PetscFormatRealArray` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFormatRealArray/> |
| `PetscFortranCallbackGetSizes` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFortranCallbackGetSizes/> |
| `PetscFortranCallbackRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFortranCallbackRegister/> |
| `PetscFPrintf` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFPrintf/> |
| `PetscFPTrapPop` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFPTrapPop/> |
| `PetscFPTrapPush` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFPTrapPush/> |
| `PetscFree` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFree/> |
| `PetscFree2` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFree2/> |
| `PetscFree3` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFree3/> |
| `PetscFree4` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFree4/> |
| `PetscFree5` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFree5/> |
| `PetscFree6` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFree6/> |
| `PetscFree7` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFree7/> |
| `PetscFreeA` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFreeA/> |
| `PetscFreeArguments` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFreeArguments/> |
| `PetscFunctionBegin` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFunctionBegin/> |
| `PetscFunctionBeginHot` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFunctionBeginHot/> |
| `PetscFunctionBeginUser` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFunctionBeginUser/> |
| `PetscFunctionListAdd` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFunctionListAdd/> |
| `PetscFunctionListClear` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFunctionListClear/> |
| `PetscFunctionListFind` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFunctionListFind/> |
| `PetscFunctionListGet` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFunctionListGet/> |
| `PetscFunctionListPrintAll` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFunctionListPrintAll/> |
| `PetscFunctionListPrintNonEmpty` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFunctionListPrintNonEmpty/> |
| `PetscFunctionListPrintTypes` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFunctionListPrintTypes/> |
| `PetscFunctionListView` | Collective | <https://petsc.org/release/manualpages/Sys/PetscFunctionListView/> |
| `PetscFunctionReturn` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscFunctionReturn/> |
| `PetscFunctionReturnVoid` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscFunctionReturnVoid/> |
| `PetscGarbageCleanup` | Collective | <https://petsc.org/release/manualpages/Sys/PetscGarbageCleanup/> |
| `PetscGatherMessageLengths` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGatherMessageLengths/> |
| `PetscGatherMessageLengths2` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGatherMessageLengths2/> |
| `PetscGatherNumberOfMessages` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGatherNumberOfMessages/> |
| `PetscGCD` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGCD/> |
| `PetscGetArchType` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetArchType/> |
| `PetscGetArgs` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGetArgs/> |
| `PetscGetArguments` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGetArguments/> |
| `PetscGetCPUTime` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetCPUTime/> |
| `PetscGetCurrentCUDAStream` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGetCurrentCUDAStream/> |
| `PetscGetCurrentHIPStream` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGetCurrentHIPStream/> |
| `PetscGetDate` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetDate/> |
| `PetscGetFullPath` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetFullPath/> |
| `PetscGetHomeDirectory` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetHomeDirectory/> |
| `PetscGetHostName` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetHostName/> |
| `PetscGetMemType` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGetMemType/> |
| `PetscGetPetscDir` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGetPetscDir/> |
| `PetscGetProgramName` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetProgramName/> |
| `PetscGetRealPath` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetRealPath/> |
| `PetscGetRelativePath` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGetRelativePath/> |
| `PetscGetTmp` | Collective | <https://petsc.org/release/manualpages/Sys/PetscGetTmp/> |
| `PetscGetUserName` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetUserName/> |
| `PetscGetVersion` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscGetVersion/> |
| `PetscGetVersionNumber` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetVersionNumber/> |
| `PetscGetWorkingDirectory` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscGetWorkingDirectory/> |
| `PetscGlobalMinMaxInt` | Collective | <https://petsc.org/release/manualpages/Sys/PetscGlobalMinMaxInt/> |
| `PetscGlobalMinMaxReal` | Collective | <https://petsc.org/release/manualpages/Sys/PetscGlobalMinMaxReal/> |
| `PetscGlobusAuthorize` | Not Collective, only the first process in MPI_Comm does anything | <https://petsc.org/release/manualpages/Sys/PetscGlobusAuthorize/> |
| `PetscGlobusGetTransfers` | Not Collective, only the first process in MPI_Comm does anything | <https://petsc.org/release/manualpages/Sys/PetscGlobusGetTransfers/> |
| `PetscGlobusUpload` | Not Collective, only the first process in the MPI_Comm uploads the file | <https://petsc.org/release/manualpages/Sys/PetscGlobusUpload/> |
| `PetscGoogleDriveAuthorize` | Not Collective, only the first process in MPI_Comm does anything | <https://petsc.org/release/manualpages/Sys/PetscGoogleDriveAuthorize/> |
| `PetscGoogleDriveRefresh` | Not Collective, only the first process in the MPI_Comm does anything | <https://petsc.org/release/manualpages/Sys/PetscGoogleDriveRefresh/> |
| `PetscGoogleDriveUpload` | Not Collective, only the first process in the MPI_Comm uploads the file | <https://petsc.org/release/manualpages/Sys/PetscGoogleDriveUpload/> |
| `PetscHasExternalPackage` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscHasExternalPackage/> |
| `PetscHeaderCreate` | Collective | <https://petsc.org/release/manualpages/Sys/PetscHeaderCreate/> |
| `PetscHeaderDestroy` | Collective | <https://petsc.org/release/manualpages/Sys/PetscHeaderDestroy/> |
| `PetscHelpPrintf` | Not Collective, only applies on MPI rank 0; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscHelpPrintf/> |
| `PetscHIPBLASGetHandle` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscHIPBLASGetHandle/> |
| `PetscHipBLASIntCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscHipBLASIntCast/> |
| `PetscHIPSOLVERGetHandle` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscHIPSOLVERGetHandle/> |
| `PetscHypotReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscHypotReal/> |
| `PetscImaginaryPart` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscImaginaryPart/> |
| `PetscImaginaryPartComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscImaginaryPartComplex/> |
| `PetscInitialize` | Collective on MPI_COMM_WORLD or PETSC_COMM_WORLD if it has been set | <https://petsc.org/release/manualpages/Sys/PetscInitialize/> |
| `PetscInitializeFortran` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Sys/PetscInitializeFortran/> |
| `PetscInitializeNoArguments` | Collective | <https://petsc.org/release/manualpages/Sys/PetscInitializeNoArguments/> |
| `PetscInitializeNoPointers` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscInitializeNoPointers/> |
| `PetscIntCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscIntCast/> |
| `PetscIntMultError` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscIntMultError/> |
| `PetscIntMultTruncate` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscIntMultTruncate/> |
| `PetscIntSortSemiOrdered` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscIntSortSemiOrdered/> |
| `PetscIntSortSemiOrderedWithArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscIntSortSemiOrderedWithArray/> |
| `PetscIntSumError` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscIntSumError/> |
| `PetscIntSumTruncate` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscIntSumTruncate/> |
| `PetscIntView` | Collective | <https://petsc.org/release/manualpages/Sys/PetscIntView/> |
| `PetscIntViewNumColumns` | Collective | <https://petsc.org/release/manualpages/Sys/PetscIntViewNumColumns/> |
| `PetscKokkosInitializeCheck` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscKokkosInitializeCheck/> |
| `PetscLCM` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscLCM/> |
| `PetscLGamma` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscLGamma/> |
| `PetscLikely` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscLikely/> |
| `PetscLog10Real` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscLog10Real/> |
| `PetscLog2Real` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscLog2Real/> |
| `PetscLogComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscLogComplex/> |
| `PetscLogReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscLogReal/> |
| `PetscLogScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscLogScalar/> |
| `PetscLs` | Collective | <https://petsc.org/release/manualpages/Sys/PetscLs/> |
| `PetscMalloc` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMalloc/> |
| `PetscMalloc1` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMalloc1/> |
| `PetscMalloc2` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMalloc2/> |
| `PetscMalloc3` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMalloc3/> |
| `PetscMalloc4` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMalloc4/> |
| `PetscMalloc5` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMalloc5/> |
| `PetscMalloc6` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMalloc6/> |
| `PetscMalloc7` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMalloc7/> |
| `PetscMallocA` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMallocA/> |
| `PetscMallocClear` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocClear/> |
| `PetscMallocDump` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocDump/> |
| `PetscMallocGetCurrentUsage` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocGetCurrentUsage/> |
| `PetscMallocGetDebug` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocGetDebug/> |
| `PetscMallocGetMaximumUsage` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocGetMaximumUsage/> |
| `PetscMallocGetStack` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMallocGetStack/> |
| `PetscMallocLogRequestedSizeGet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocLogRequestedSizeGet/> |
| `PetscMallocLogRequestedSizeSet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocLogRequestedSizeSet/> |
| `PetscMallocPopMaximumUsage` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocPopMaximumUsage/> |
| `PetscMallocPushMaximumUsage` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocPushMaximumUsage/> |
| `PetscMallocResetCUDAHost` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocResetCUDAHost/> |
| `PetscMallocResetDRAM` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocResetDRAM/> |
| `PetscMallocResetHIPHost` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocResetHIPHost/> |
| `PetscMallocSet` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMallocSet/> |
| `PetscMallocSetCoalesce` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocSetCoalesce/> |
| `PetscMallocSetCUDAHost` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocSetCUDAHost/> |
| `PetscMallocSetDebug` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocSetDebug/> |
| `PetscMallocSetDRAM` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocSetDRAM/> |
| `PetscMallocSetHIPHost` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocSetHIPHost/> |
| `PetscMallocTraceGet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocTraceGet/> |
| `PetscMallocTraceSet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocTraceSet/> |
| `PetscMallocView` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocView/> |
| `PetscMallocViewGet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocViewGet/> |
| `PetscMallocViewSet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMallocViewSet/> |
| `PetscMax` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMax/> |
| `PetscMaxSum` | Collective | <https://petsc.org/release/manualpages/Sys/PetscMaxSum/> |
| `PetscMemcmp` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMemcmp/> |
| `PetscMemcpy` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemcpy/> |
| `PetscMemmove` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemmove/> |
| `PetscMemoryAccessRead` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemoryAccessRead/> |
| `PetscMemoryAccessWrite` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemoryAccessWrite/> |
| `PetscMemoryGetCurrentUsage` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMemoryGetCurrentUsage/> |
| `PetscMemoryGetMaximumUsage` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMemoryGetMaximumUsage/> |
| `PetscMemorySetGetMaximumUsage` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMemorySetGetMaximumUsage/> |
| `PetscMemoryTrace` | Collective on PETSC_COMM_WORLD ; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemoryTrace/> |
| `PetscMemoryView` | Collective | <https://petsc.org/release/manualpages/Sys/PetscMemoryView/> |
| `PetscMemTypeCUDA` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemTypeCUDA/> |
| `PetscMemTypeDevice` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemTypeDevice/> |
| `PetscMemTypeHIP` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemTypeHIP/> |
| `PetscMemTypeHost` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemTypeHost/> |
| `PetscMemTypeNVSHMEM` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemTypeNVSHMEM/> |
| `PetscMemTypeSYCL` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemTypeSYCL/> |
| `PetscMemzero` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMemzero/> |
| `PetscMergeIntArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMergeIntArray/> |
| `PetscMergeIntArrayPair` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMergeIntArrayPair/> |
| `PetscMergeMPIIntArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMergeMPIIntArray/> |
| `PetscMin` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMin/> |
| `PetscMkdir` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMkdir/> |
| `PetscMPIAbortErrorHandler` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMPIAbortErrorHandler/> |
| `PetscMPIDataTypeToPetscDataType` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMPIDataTypeToPetscDataType/> |
| `PetscMPIDump` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Sys/PetscMPIDump/> |
| `PetscMPIErrorString` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMPIErrorString/> |
| `PetscMPIIntCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscMPIIntCast/> |
| `PetscMPIIntSortSemiOrdered` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMPIIntSortSemiOrdered/> |
| `PetscMPIIntSortSemiOrderedWithArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscMPIIntSortSemiOrderedWithArray/> |
| `PetscNew` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscNew/> |
| `PetscNewLog` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscNewLog/> |
| `PetscObjectAddOptionsHandler` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectAddOptionsHandler/> |
| `PetscObjectBaseTypeCompare` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectBaseTypeCompare/> |
| `PetscObjectBaseTypeCompareAny` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectBaseTypeCompareAny/> |
| `PetscObjectChangeTypeName` | Logically collective | <https://petsc.org/release/manualpages/Sys/PetscObjectChangeTypeName/> |
| `PetscObjectComm` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscObjectComm/> |
| `PetscObjectCompareId` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectCompareId/> |
| `PetscObjectCompose` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectCompose/> |
| `PetscObjectComposedDataGetInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataGetInt/> |
| `PetscObjectComposedDataGetIntstar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataGetIntstar/> |
| `PetscObjectComposedDataGetReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataGetReal/> |
| `PetscObjectComposedDataGetRealstar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataGetRealstar/> |
| `PetscObjectComposedDataGetScalar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataGetScalar/> |
| `PetscObjectComposedDataGetScalarstar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataGetScalarstar/> |
| `PetscObjectComposedDataRegister` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataRegister/> |
| `PetscObjectComposedDataSetInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataSetInt/> |
| `PetscObjectComposedDataSetIntstar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataSetIntstar/> |
| `PetscObjectComposedDataSetReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataSetReal/> |
| `PetscObjectComposedDataSetRealstar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataSetRealstar/> |
| `PetscObjectComposedDataSetScalar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataSetScalar/> |
| `PetscObjectComposedDataSetScalarstar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposedDataSetScalarstar/> |
| `PetscObjectComposeFunction` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectComposeFunction/> |
| `PetscObjectContainerCompose` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectContainerCompose/> |
| `PetscObjectContainerQuery` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectContainerQuery/> |
| `PetscObjectCopyFortranFunctionPointers` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectCopyFortranFunctionPointers/> |
| `PetscObjectDelayedDestroy` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectDelayedDestroy/> |
| `PetscObjectDereference` | Collective on obj if reference reaches 0 otherwise Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectDereference/> |
| `PetscObjectDestroy` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectDestroy/> |
| `PetscObjectDestroyOptionsHandlers` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectDestroyOptionsHandlers/> |
| `PetscObjectGetClassId` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetClassId/> |
| `PetscObjectGetClassName` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetClassName/> |
| `PetscObjectGetComm` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetComm/> |
| `PetscObjectGetFortranCallback` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscObjectGetFortranCallback/> |
| `PetscObjectGetId` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetId/> |
| `PetscObjectGetName` | Not Collective unless obj has not yet been named | <https://petsc.org/release/manualpages/Sys/PetscObjectGetName/> |
| `PetscObjectGetNewTag` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetNewTag/> |
| `PetscObjectGetOptions` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetOptions/> |
| `PetscObjectGetReference` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetReference/> |
| `PetscObjectGetTabLevel` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetTabLevel/> |
| `PetscObjectGetType` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectGetType/> |
| `PetscObjectHasFunction` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectHasFunction/> |
| `PetscObjectIncrementTabLevel` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectIncrementTabLevel/> |
| `PetscObjectIsNull` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectIsNull/> |
| `PetscObjectName` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectName/> |
| `PetscObjectNullify` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectNullify/> |
| `PetscObjectObjectTypeCompare` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectObjectTypeCompare/> |
| `PetscObjectOptionsBegin` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectOptionsBegin/> |
| `PetscObjectProcessOptionsHandlers` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectProcessOptionsHandlers/> |
| `PetscObjectQuery` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectQuery/> |
| `PetscObjectQueryFunction` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectQueryFunction/> |
| `PetscObjectReference` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectReference/> |
| `PetscObjectRegisterDestroy` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectRegisterDestroy/> |
| `PetscObjectRegisterDestroyAll` | Logically Collective on the individual PetscObject s that are being processed | <https://petsc.org/release/manualpages/Sys/PetscObjectRegisterDestroyAll/> |
| `PetscObjectRemoveReference` | Logically collective | <https://petsc.org/release/manualpages/Sys/PetscObjectRemoveReference/> |
| `PetscObjectSAWsBlock` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSAWsBlock/> |
| `PetscObjectSAWsGrantAccess` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSAWsGrantAccess/> |
| `PetscObjectSAWsSetBlock` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSAWsSetBlock/> |
| `PetscObjectSAWsTakeAccess` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSAWsTakeAccess/> |
| `PetscObjectSAWsViewOff` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSAWsViewOff/> |
| `PetscObjectSetFortranCallback` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscObjectSetFortranCallback/> |
| `PetscObjectSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSetFromOptions/> |
| `PetscObjectSetName` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSetName/> |
| `PetscObjectSetOptions` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSetOptions/> |
| `PetscObjectSetOptionsPrefix` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSetOptionsPrefix/> |
| `PetscObjectSetTabLevel` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSetTabLevel/> |
| `PetscObjectSetUp` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectSetUp/> |
| `PetscObjectsGetObject` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectsGetObject/> |
| `PetscObjectsListGetGlobalNumbering` | Collective. | <https://petsc.org/release/manualpages/Sys/PetscObjectsListGetGlobalNumbering/> |
| `PetscObjectStateGet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectStateGet/> |
| `PetscObjectStateIncrease` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectStateIncrease/> |
| `PetscObjectStateSet` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectStateSet/> |
| `PetscObjectsView` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectsView/> |
| `PetscObjectTypeCompare` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectTypeCompare/> |
| `PetscObjectTypeCompareAny` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectTypeCompareAny/> |
| `PetscObjectView` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectView/> |
| `PetscObjectViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Sys/PetscObjectViewFromOptions/> |
| `PetscOffloadBoth` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscOffloadBoth/> |
| `PetscOffloadDevice` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscOffloadDevice/> |
| `PetscOffloadHost` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscOffloadHost/> |
| `PetscOffloadUnallocated` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscOffloadUnallocated/> |
| `PetscOptionsAllUsed` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsAllUsed/> |
| `PetscOptionsBegin` | Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsBegin/> |
| `PetscOptionsBool` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsBool/> |
| `PetscOptionsBool3` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsBool3/> |
| `PetscOptionsBoolArray` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsBoolArray/> |
| `PetscOptionsBoolGroup` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsBoolGroup/> |
| `PetscOptionsBoolGroupBegin` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsBoolGroupBegin/> |
| `PetscOptionsBoolGroupEnd` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsBoolGroupEnd/> |
| `PetscOptionsBoundedInt` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsBoundedInt/> |
| `PetscOptionsBoundedReal` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsBoundedReal/> |
| `PetscOptionsClear` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsClear/> |
| `PetscOptionsClearValue` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsClearValue/> |
| `PetscOptionsCreate` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsCreate/> |
| `PetscOptionsCreateDefault` | Logically collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsCreateDefault/> |
| `PetscOptionsDeprecated_Private` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsDeprecated_Private/> |
| `PetscOptionsDestroy` | Logically Collective on whatever communicator was associated with the call to PetscOptionsCreate () | <https://petsc.org/release/manualpages/Sys/PetscOptionsDestroy/> |
| `PetscOptionsDestroyDefault` | Logically collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsDestroyDefault/> |
| `PetscOptionsEList` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsEList/> |
| `PetscOptionsEnd` | Collective on the comm used in PetscOptionsBegin () or obj used in PetscObjectOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsEnd/> |
| `PetscOptionsEnum` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsEnum/> |
| `PetscOptionsEnumArray` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsEnumArray/> |
| `PetscOptionsFindPair` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsFindPair/> |
| `PetscOptionsFList` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsFList/> |
| `PetscOptionsGetAll` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetAll/> |
| `PetscOptionsGetBool` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetBool/> |
| `PetscOptionsGetBool3` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetBool3/> |
| `PetscOptionsGetBoolArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetBoolArray/> |
| `PetscOptionsGetEList` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetEList/> |
| `PetscOptionsGetEnum` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetEnum/> |
| `PetscOptionsGetEnumArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetEnumArray/> |
| `PetscOptionsGetenv` | Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetenv/> |
| `PetscOptionsGetInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetInt/> |
| `PetscOptionsGetIntArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetIntArray/> |
| `PetscOptionsGetMPIInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetMPIInt/> |
| `PetscOptionsGetReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetReal/> |
| `PetscOptionsGetRealArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetRealArray/> |
| `PetscOptionsGetScalar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetScalar/> |
| `PetscOptionsGetScalarArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetScalarArray/> |
| `PetscOptionsGetString` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetString/> |
| `PetscOptionsGetStringArray` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscOptionsGetStringArray/> |
| `PetscOptionsHasHelp` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsHasHelp/> |
| `PetscOptionsHasName` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsHasName/> |
| `PetscOptionsHeadEnd` | Collective on the comm used in PetscOptionsBegin () or obj used in PetscObjectOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsHeadEnd/> |
| `PetscOptionsInsert` | Collective on PETSC_COMM_WORLD | <https://petsc.org/release/manualpages/Sys/PetscOptionsInsert/> |
| `PetscOptionsInsertArgs` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsInsertArgs/> |
| `PetscOptionsInsertFile` | Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsInsertFile/> |
| `PetscOptionsInsertFileYAML` | Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsInsertFileYAML/> |
| `PetscOptionsInsertString` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsInsertString/> |
| `PetscOptionsInsertStringYAML` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsInsertStringYAML/> |
| `PetscOptionsInt` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsInt/> |
| `PetscOptionsIntArray` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsIntArray/> |
| `PetscOptionsLeft` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsLeft/> |
| `PetscOptionsLeftError` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsLeftError/> |
| `PetscOptionsLeftGet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsLeftGet/> |
| `PetscOptionsLeftRestore` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsLeftRestore/> |
| `PetscOptionsMonitorDefault` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsMonitorDefault/> |
| `PetscOptionsMonitorSet` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsMonitorSet/> |
| `PetscOptionsMPIInt` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsMPIInt/> |
| `PetscOptionsName` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsName/> |
| `PetscOptionsPop` | Logically Collective on whatever communicator was associated with the call to PetscOptionsCreate () | <https://petsc.org/release/manualpages/Sys/PetscOptionsPop/> |
| `PetscOptionsPrefixPop` | Logically Collective on the MPI_Comm used when called PetscOptionsPrefixPush () | <https://petsc.org/release/manualpages/Sys/PetscOptionsPrefixPop/> |
| `PetscOptionsPrefixPush` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsPrefixPush/> |
| `PetscOptionsPush` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsPush/> |
| `PetscOptionsRangeInt` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsRangeInt/> |
| `PetscOptionsRangeReal` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsRangeReal/> |
| `PetscOptionsReal` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsReal/> |
| `PetscOptionsRealArray` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsRealArray/> |
| `PetscOptionsReject` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsReject/> |
| `PetscOptionsScalar` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsScalar/> |
| `PetscOptionsScalarArray` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsScalarArray/> |
| `PetscOptionsSetAlias` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsSetAlias/> |
| `PetscOptionsSetValue` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsSetValue/> |
| `PetscOptionsString` | Logically Collective on the communicator passed in PetscOptionsBegin () | <https://petsc.org/release/manualpages/Sys/PetscOptionsString/> |
| `PetscOptionsStringArray` | Logically Collective on the communicator passed in PetscOptionsBegin () ; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscOptionsStringArray/> |
| `PetscOptionsStringToBool` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsStringToBool/> |
| `PetscOptionsStringToInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsStringToInt/> |
| `PetscOptionsStringToReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsStringToReal/> |
| `PetscOptionsStringToScalar` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsStringToScalar/> |
| `PetscOptionsUsed` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsUsed/> |
| `PetscOptionsValidKey` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscOptionsValidKey/> |
| `PetscOptionsView` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscOptionsView/> |
| `PetscParallelSortedInt` | Collective | <https://petsc.org/release/manualpages/Sys/PetscParallelSortedInt/> |
| `PetscPClose` | Collective, but only MPI rank 0 does anything | <https://petsc.org/release/manualpages/Sys/PetscPClose/> |
| `PetscPOpen` | Logically Collective, but only MPI rank 0 runs the command | <https://petsc.org/release/manualpages/Sys/PetscPOpen/> |
| `PetscPOpenSetMachine` | Logically Collective, but only the MPI process with rank 0 runs the command | <https://petsc.org/release/manualpages/Sys/PetscPOpenSetMachine/> |
| `PetscPopErrorHandler` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscPopErrorHandler/> |
| `PetscPopSignalHandler` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscPopSignalHandler/> |
| `PetscPostIrecvInt` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscPostIrecvInt/> |
| `PetscPostIrecvScalar` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscPostIrecvScalar/> |
| `PetscPowComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscPowComplex/> |
| `PetscPowReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscPowReal/> |
| `PetscPowScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscPowScalar/> |
| `PetscPrefetchBlock` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscPrefetchBlock/> |
| `PetscPrintf` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscPrintf/> |
| `PetscProcessTree` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscProcessTree/> |
| `PetscPushErrorHandler` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscPushErrorHandler/> |
| `PetscPushSignalHandler` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscPushSignalHandler/> |
| `PetscRandomCreate` | Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomCreate/> |
| `PetscRandomDestroy` | Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomDestroy/> |
| `PetscRandomGetInterval` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomGetInterval/> |
| `PetscRandomGetSeed` | Not collective | <https://petsc.org/release/manualpages/Sys/PetscRandomGetSeed/> |
| `PetscRandomGetType` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomGetType/> |
| `PetscRandomGetValue` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomGetValue/> |
| `PetscRandomGetValueReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomGetValueReal/> |
| `PetscRandomGetValues` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomGetValues/> |
| `PetscRandomGetValuesReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomGetValuesReal/> |
| `PetscRandomRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscRandomRegister/> |
| `PetscRandomRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomRegisterAll/> |
| `PetscRandomSeed` | Not collective | <https://petsc.org/release/manualpages/Sys/PetscRandomSeed/> |
| `PetscRandomSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomSetFromOptions/> |
| `PetscRandomSetInterval` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomSetInterval/> |
| `PetscRandomSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomSetOptionsPrefix/> |
| `PetscRandomSetSeed` | Not collective | <https://petsc.org/release/manualpages/Sys/PetscRandomSetSeed/> |
| `PetscRandomSetType` | Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomSetType/> |
| `PetscRandomView` | Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomView/> |
| `PetscRandomViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Sys/PetscRandomViewFromOptions/> |
| `PetscRealConstant` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRealConstant/> |
| `PetscRealIntMultTruncate` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscRealIntMultTruncate/> |
| `PetscRealloc` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRealloc/> |
| `PetscRealPart` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRealPart/> |
| `PetscRealPartComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscRealPartComplex/> |
| `PetscRealSortSemiOrdered` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRealSortSemiOrdered/> |
| `PetscRealSortSemiOrderedWithArrayInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRealSortSemiOrderedWithArrayInt/> |
| `PetscRealView` | Collective | <https://petsc.org/release/manualpages/Sys/PetscRealView/> |
| `PetscRealViewNumColumns` | Collective | <https://petsc.org/release/manualpages/Sys/PetscRealViewNumColumns/> |
| `PetscRegisterFinalize` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRegisterFinalize/> |
| `PetscRegisterFinalizeAll` | Not Collective except for registered functions that are collective | <https://petsc.org/release/manualpages/Sys/PetscRegisterFinalizeAll/> |
| `PetscReturnErrorHandler` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscReturnErrorHandler/> |
| `PetscRintReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscRintReal/> |
| `PetscRMTree` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscRMTree/> |
| `PetscSAWsBlock` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSAWsBlock/> |
| `PetscScalarView` | Collective | <https://petsc.org/release/manualpages/Sys/PetscScalarView/> |
| `PetscScalarViewNumColumns` | Collective | <https://petsc.org/release/manualpages/Sys/PetscScalarViewNumColumns/> |
| `PetscSegBufferCreate` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSegBufferCreate/> |
| `PetscSegBufferDestroy` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSegBufferDestroy/> |
| `PetscSegBufferExtractAlloc` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSegBufferExtractAlloc/> |
| `PetscSegBufferExtractInPlace` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSegBufferExtractInPlace/> |
| `PetscSegBufferExtractTo` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSegBufferExtractTo/> |
| `PetscSegBufferGet` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSegBufferGet/> |
| `PetscSegBufferGetSize` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSegBufferGetSize/> |
| `PetscSegBufferUnuse` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSegBufferUnuse/> |
| `PetscSequentialPhaseBegin` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSequentialPhaseBegin/> |
| `PetscSequentialPhaseEnd` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSequentialPhaseEnd/> |
| `PetscSetDebugger` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSetDebugger/> |
| `PetscSetDebuggerFromString` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSetDebuggerFromString/> |
| `PetscSetDebugTerminal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSetDebugTerminal/> |
| `PetscSetDefaultDebugger` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSetDefaultDebugger/> |
| `PetscSetDisplay` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSetDisplay/> |
| `PetscSetFPTrap` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSetFPTrap/> |
| `PetscSetProgramName` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSetProgramName/> |
| `PetscSharedTmp` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSharedTmp/> |
| `PetscSharedWorkingDirectory` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSharedWorkingDirectory/> |
| `PetscShmCommGet` | Collective. | <https://petsc.org/release/manualpages/Sys/PetscShmCommGet/> |
| `PetscShmgetAddressesFinalize` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscShmgetAddressesFinalize/> |
| `PetscShmgetAllocateArray` | Not Collective, only called on the first MPI process | <https://petsc.org/release/manualpages/Sys/PetscShmgetAllocateArray/> |
| `PetscShmgetDeallocateArray` | Not Collective, only called on the first MPI process | <https://petsc.org/release/manualpages/Sys/PetscShmgetDeallocateArray/> |
| `PetscShmgetMapAddresses` | Collective | <https://petsc.org/release/manualpages/Sys/PetscShmgetMapAddresses/> |
| `PetscShmgetUnmapAddresses` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscShmgetUnmapAddresses/> |
| `PetscSign` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSign/> |
| `PetscSignalHandlerDefault` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSignalHandlerDefault/> |
| `PetscSignalSegvCheckPointerOrMpi` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSignalSegvCheckPointerOrMpi/> |
| `PetscSinComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSinComplex/> |
| `PetscSinhComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSinhComplex/> |
| `PetscSinhReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSinhReal/> |
| `PetscSinhScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSinhScalar/> |
| `PetscSinReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSinReal/> |
| `PetscSinScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSinScalar/> |
| `PetscSleep` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSleep/> |
| `PetscSNPrintf` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSNPrintf/> |
| `PetscSNPrintfCount` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSNPrintfCount/> |
| `PetscSortCount` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortCount/> |
| `PetscSortedCheckDupsCount` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortedCheckDupsCount/> |
| `PetscSortedCheckDupsInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortedCheckDupsInt/> |
| `PetscSortedInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortedInt/> |
| `PetscSortedInt64` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortedInt64/> |
| `PetscSortedMPIInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortedMPIInt/> |
| `PetscSortedReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortedReal/> |
| `PetscSortedRemoveDupsInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortedRemoveDupsInt/> |
| `PetscSortInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortInt/> |
| `PetscSortInt64` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortInt64/> |
| `PetscSortIntWithArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortIntWithArray/> |
| `PetscSortIntWithArrayPair` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortIntWithArrayPair/> |
| `PetscSortIntWithCountArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortIntWithCountArray/> |
| `PetscSortIntWithDataArray` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSortIntWithDataArray/> |
| `PetscSortIntWithIntCountArrayPair` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortIntWithIntCountArrayPair/> |
| `PetscSortIntWithMPIIntArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortIntWithMPIIntArray/> |
| `PetscSortIntWithPermutation` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortIntWithPermutation/> |
| `PetscSortIntWithScalarArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortIntWithScalarArray/> |
| `PetscSortMPIInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortMPIInt/> |
| `PetscSortMPIIntWithArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortMPIIntWithArray/> |
| `PetscSortMPIIntWithIntArray` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortMPIIntWithIntArray/> |
| `PetscSortReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortReal/> |
| `PetscSortRealWithArrayInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortRealWithArrayInt/> |
| `PetscSortRealWithPermutation` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortRealWithPermutation/> |
| `PetscSortRemoveDupsInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortRemoveDupsInt/> |
| `PetscSortRemoveDupsMPIInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortRemoveDupsMPIInt/> |
| `PetscSortRemoveDupsReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortRemoveDupsReal/> |
| `PetscSortReverseInt` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortReverseInt/> |
| `PetscSortSplit` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortSplit/> |
| `PetscSortSplitReal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSortSplitReal/> |
| `PetscSortStrWithPermutation` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSortStrWithPermutation/> |
| `PetscSplitOwnership` | Collective (if n or N is PETSC_DECIDE or PETSC_DETERMINE ) | <https://petsc.org/release/manualpages/Sys/PetscSplitOwnership/> |
| `PetscSplitOwnershipBlock` | Collective (if N is PETSC_DECIDE ) | <https://petsc.org/release/manualpages/Sys/PetscSplitOwnershipBlock/> |
| `PetscSplitOwnershipEqual` | Collective (if n or N is PETSC_DECIDE ) | <https://petsc.org/release/manualpages/Sys/PetscSplitOwnershipEqual/> |
| `PetscSqr` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSqr/> |
| `PetscSqrtComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSqrtComplex/> |
| `PetscSqrtReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSqrtReal/> |
| `PetscSqrtScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscSqrtScalar/> |
| `PetscStackCopy` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStackCopy/> |
| `PetscStackPop` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStackPop/> |
| `PetscStackPopNoCheck` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStackPopNoCheck/> |
| `PetscStackPrint` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStackPrint/> |
| `PetscStackPush` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStackPush/> |
| `PetscStackPushExternal` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStackPushExternal/> |
| `PetscStackPushNoCheck` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStackPushNoCheck/> |
| `PetscStackSAWsGrantAccess` | Collective on PETSC_COMM_WORLD ? | <https://petsc.org/release/manualpages/Sys/PetscStackSAWsGrantAccess/> |
| `PetscStackSAWsTakeAccess` | Collective on PETSC_COMM_WORLD ? | <https://petsc.org/release/manualpages/Sys/PetscStackSAWsTakeAccess/> |
| `PetscStackSAWsViewOff` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscStackSAWsViewOff/> |
| `PetscStackUpdateLine` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStackUpdateLine/> |
| `PetscStackView` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStackView/> |
| `PetscStackViewSAWs` | Logically Collective on PETSC_COMM_WORLD ; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStackViewSAWs/> |
| `PetscStartMatlab` | Logically Collective, but only MPI rank 0 in the communicator does anything | <https://petsc.org/release/manualpages/Sys/PetscStartMatlab/> |
| `PetscStopForDebugger` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStopForDebugger/> |
| `PetscStrallocpy` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrallocpy/> |
| `PetscStrArrayallocpy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrArrayallocpy/> |
| `PetscStrArrayDestroy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrArrayDestroy/> |
| `PetscStrbeginswith` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrbeginswith/> |
| `PetscStrcasecmp` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrcasecmp/> |
| `PetscStrcat` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrcat/> |
| `PetscStrchr` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrchr/> |
| `PetscStrcmp` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrcmp/> |
| `PetscStrcmpAny` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrcmpAny/> |
| `PetscStrcpy` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrcpy/> |
| `PetscStrendswith` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrendswith/> |
| `PetscStrendswithwhich` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrendswithwhich/> |
| `PetscStrgrt` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrgrt/> |
| `PetscStrInList` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrInList/> |
| `PetscStrlcat` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrlcat/> |
| `PetscStrlen` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrlen/> |
| `PetscStrNArrayallocpy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrNArrayallocpy/> |
| `PetscStrNArrayDestroy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrNArrayDestroy/> |
| `PetscStrncmp` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrncmp/> |
| `PetscStrncpy` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscStrncpy/> |
| `PetscStrrchr` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrrchr/> |
| `PetscStrreplace` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrreplace/> |
| `PetscStrrstr` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrrstr/> |
| `PetscStrstr` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrstr/> |
| `PetscStrToArray` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrToArray/> |
| `PetscStrToArrayDestroy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrToArrayDestroy/> |
| `PetscStrtolower` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrtolower/> |
| `PetscStrtoupper` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscStrtoupper/> |
| `PetscSubcommCreate` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommCreate/> |
| `PetscSubcommDestroy` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommDestroy/> |
| `PetscSubcommGetChild` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommGetChild/> |
| `PetscSubcommGetContiguousParent` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommGetContiguousParent/> |
| `PetscSubcommGetParent` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommGetParent/> |
| `PetscSubcommSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommSetFromOptions/> |
| `PetscSubcommSetNumber` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommSetNumber/> |
| `PetscSubcommSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommSetOptionsPrefix/> |
| `PetscSubcommSetType` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommSetType/> |
| `PetscSubcommSetTypeGeneral` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommSetTypeGeneral/> |
| `PetscSubcommView` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSubcommView/> |
| `PetscSynchronizedFGets` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSynchronizedFGets/> |
| `PetscSynchronizedFlush` | Collective | <https://petsc.org/release/manualpages/Sys/PetscSynchronizedFlush/> |
| `PetscSynchronizedFPrintf` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSynchronizedFPrintf/> |
| `PetscSynchronizedPrintf` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscSynchronizedPrintf/> |
| `PetscTanComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTanComplex/> |
| `PetscTanhComplex` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTanhComplex/> |
| `PetscTanhReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTanhReal/> |
| `PetscTanhScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTanhScalar/> |
| `PetscTanReal` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTanReal/> |
| `PetscTanScalar` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTanScalar/> |
| `PetscTestDirectory` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscTestDirectory/> |
| `PetscTestFile` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscTestFile/> |
| `PetscTGamma` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTGamma/> |
| `PetscTime` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscTime/> |
| `PetscTimeAdd` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscTimeAdd/> |
| `PetscTimeSubtract` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscTimeSubtract/> |
| `PetscTimSort` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTimSort/> |
| `PetscTimSortWithArray` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTimSortWithArray/> |
| `PetscTokenCreate` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTokenCreate/> |
| `PetscTokenDestroy` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTokenDestroy/> |
| `PetscTokenFind` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTokenFind/> |
| `PetscTraceBackErrorHandler` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscTraceBackErrorHandler/> |
| `PetscUnlikely` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscUnlikely/> |
| `PetscUnlikelyDebug` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Sys/PetscUnlikelyDebug/> |
| `PetscWaitOnError` | Not Collective | <https://petsc.org/release/manualpages/Sys/PetscWaitOnError/> |
| `SETERRA` | Collective | <https://petsc.org/release/manualpages/Sys/SETERRA/> |
| `SETERRABORT` | Collective | <https://petsc.org/release/manualpages/Sys/SETERRABORT/> |
| `SETERRMPI` | Collective | <https://petsc.org/release/manualpages/Sys/SETERRMPI/> |
| `SETERRQ` | Collective | <https://petsc.org/release/manualpages/Sys/SETERRQ/> |

## Tao

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `MatCreateSubMatrixFree` | Collective | <https://petsc.org/release/manualpages/Tao/MatCreateSubMatrixFree/> |
| `MatDFischer` | Collective | <https://petsc.org/release/manualpages/Tao/MatDFischer/> |
| `MatDSFischer` | Collective | <https://petsc.org/release/manualpages/Tao/MatDSFischer/> |
| `TaoAddTerm` | Collective | <https://petsc.org/release/manualpages/Tao/TaoAddTerm/> |
| `TaoADMMGetDualVector` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMGetDualVector/> |
| `TaoADMMGetMisfitSubsolver` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMGetMisfitSubsolver/> |
| `TaoADMMGetRegularizationSubsolver` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMGetRegularizationSubsolver/> |
| `TaoADMMGetRegularizerCoefficient` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMGetRegularizerCoefficient/> |
| `TaoADMMGetRegularizerType` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMGetRegularizerType/> |
| `TaoADMMGetSpectralPenalty` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMGetSpectralPenalty/> |
| `TaoADMMGetUpdateType` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMGetUpdateType/> |
| `TaoADMMSetConstraintVectorRHS` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetConstraintVectorRHS/> |
| `TaoADMMSetMinimumSpectralPenalty` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetMinimumSpectralPenalty/> |
| `TaoADMMSetMisfitConstraintJacobian` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetMisfitConstraintJacobian/> |
| `TaoADMMSetMisfitHessianChangeStatus` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetMisfitHessianChangeStatus/> |
| `TaoADMMSetMisfitHessianRoutine` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetMisfitHessianRoutine/> |
| `TaoADMMSetMisfitObjectiveAndGradientRoutine` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetMisfitObjectiveAndGradientRoutine/> |
| `TaoADMMSetRegHessianChangeStatus` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetRegHessianChangeStatus/> |
| `TaoADMMSetRegularizerCoefficient` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerCoefficient/> |
| `TaoADMMSetRegularizerConstraintJacobian` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerConstraintJacobian/> |
| `TaoADMMSetRegularizerHessianRoutine` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerHessianRoutine/> |
| `TaoADMMSetRegularizerObjectiveAndGradientRoutine` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerObjectiveAndGradientRoutine/> |
| `TaoADMMSetRegularizerType` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerType/> |
| `TaoADMMSetSpectralPenalty` | Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetSpectralPenalty/> |
| `TaoADMMSetUpdateType` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoADMMSetUpdateType/> |
| `TaoAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoAppendOptionsPrefix/> |
| `TaoBoundSolution` | Collective | <https://petsc.org/release/manualpages/Tao/TaoBoundSolution/> |
| `TaoBRGNGetDampingVector` | Collective | <https://petsc.org/release/manualpages/Tao/TaoBRGNGetDampingVector/> |
| `TaoBRGNGetRegularizationType` | Not collective | <https://petsc.org/release/manualpages/Tao/TaoBRGNGetRegularizationType/> |
| `TaoBRGNGetSubsolver` | Collective | <https://petsc.org/release/manualpages/Tao/TaoBRGNGetSubsolver/> |
| `TaoBRGNSetL1SmoothEpsilon` | Collective | <https://petsc.org/release/manualpages/Tao/TaoBRGNSetL1SmoothEpsilon/> |
| `TaoBRGNSetRegularizationType` | Logically collective | <https://petsc.org/release/manualpages/Tao/TaoBRGNSetRegularizationType/> |
| `TaoBRGNSetRegularizerWeight` | Collective | <https://petsc.org/release/manualpages/Tao/TaoBRGNSetRegularizerWeight/> |
| `TaoComputeConstraints` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeConstraints/> |
| `TaoComputeDualVariables` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeDualVariables/> |
| `TaoComputeEqualityConstraints` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeEqualityConstraints/> |
| `TaoComputeGradient` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeGradient/> |
| `TaoComputeHessian` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeHessian/> |
| `TaoComputeInequalityConstraints` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeInequalityConstraints/> |
| `TaoComputeJacobian` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeJacobian/> |
| `TaoComputeJacobianDesign` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeJacobianDesign/> |
| `TaoComputeJacobianEquality` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeJacobianEquality/> |
| `TaoComputeJacobianInequality` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeJacobianInequality/> |
| `TaoComputeJacobianState` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeJacobianState/> |
| `TaoComputeObjective` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeObjective/> |
| `TaoComputeObjectiveAndGradient` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeObjectiveAndGradient/> |
| `TaoComputeResidual` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeResidual/> |
| `TaoComputeResidualJacobian` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeResidualJacobian/> |
| `TaoComputeVariableBounds` | Collective | <https://petsc.org/release/manualpages/Tao/TaoComputeVariableBounds/> |
| `TaoCreate` | Collective | <https://petsc.org/release/manualpages/Tao/TaoCreate/> |
| `TaoDefaultComputeGradient` | Collective | <https://petsc.org/release/manualpages/Tao/TaoDefaultComputeGradient/> |
| `TaoDefaultComputeHessian` | Collective | <https://petsc.org/release/manualpages/Tao/TaoDefaultComputeHessian/> |
| `TaoDefaultComputeHessianColor` | Collective | <https://petsc.org/release/manualpages/Tao/TaoDefaultComputeHessianColor/> |
| `TaoDefaultComputeHessianMFFD` | Collective | <https://petsc.org/release/manualpages/Tao/TaoDefaultComputeHessianMFFD/> |
| `TaoDefaultConvergenceTest` | Collective | <https://petsc.org/release/manualpages/Tao/TaoDefaultConvergenceTest/> |
| `TaoDestroy` | Collective | <https://petsc.org/release/manualpages/Tao/TaoDestroy/> |
| `TaoGetADMMParentTao` | Collective | <https://petsc.org/release/manualpages/Tao/TaoGetADMMParentTao/> |
| `TaoGetApplicationContext` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetApplicationContext/> |
| `TaoGetConstraintTolerances` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetConstraintTolerances/> |
| `TaoGetConvergedReason` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetConvergedReason/> |
| `TaoGetConvergenceHistory` | Collective | <https://petsc.org/release/manualpages/Tao/TaoGetConvergenceHistory/> |
| `TaoGetCurrentFunctionEvaluations` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetCurrentFunctionEvaluations/> |
| `TaoGetCurrentTrustRegionRadius` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetCurrentTrustRegionRadius/> |
| `TaoGetDualVariables` | Collective | <https://petsc.org/release/manualpages/Tao/TaoGetDualVariables/> |
| `TaoGetEqualityConstraintsRoutine` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetEqualityConstraintsRoutine/> |
| `TaoGetFunctionLowerBound` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetFunctionLowerBound/> |
| `TaoGetGradient` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetGradient/> |
| `TaoGetGradientNorm` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetGradientNorm/> |
| `TaoGetHessian` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetHessian/> |
| `TaoGetHessianMatrices` | Not collective | <https://petsc.org/release/manualpages/Tao/TaoGetHessianMatrices/> |
| `TaoGetInequalityBounds` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoGetInequalityBounds/> |
| `TaoGetInequalityConstraintsRoutine` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetInequalityConstraintsRoutine/> |
| `TaoGetInitialTrustRegionRadius` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetInitialTrustRegionRadius/> |
| `TaoGetIterationNumber` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetIterationNumber/> |
| `TaoGetJacobianEqualityRoutine` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetJacobianEqualityRoutine/> |
| `TaoGetJacobianInequalityRoutine` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetJacobianInequalityRoutine/> |
| `TaoGetKSP` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetKSP/> |
| `TaoGetLinearSolveIterations` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetLinearSolveIterations/> |
| `TaoGetLineSearch` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetLineSearch/> |
| `TaoGetMaximumFunctionEvaluations` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoGetMaximumFunctionEvaluations/> |
| `TaoGetMaximumIterations` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetMaximumIterations/> |
| `TaoGetObjective` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetObjective/> |
| `TaoGetObjectiveAndGradient` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetObjectiveAndGradient/> |
| `TaoGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetOptionsPrefix/> |
| `TaoGetRecycleHistory` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoGetRecycleHistory/> |
| `TaoGetResidualNorm` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetResidualNorm/> |
| `TaoGetSolution` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetSolution/> |
| `TaoGetSolutionStatus` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetSolutionStatus/> |
| `TaoGetTerm` | Not collective | <https://petsc.org/release/manualpages/Tao/TaoGetTerm/> |
| `TaoGetTolerances` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetTolerances/> |
| `TaoGetTotalIterationNumber` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetTotalIterationNumber/> |
| `TaoGetType` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetType/> |
| `TaoGetVariableBounds` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoGetVariableBounds/> |
| `TaoGradientNorm` | Collective | <https://petsc.org/release/manualpages/Tao/TaoGradientNorm/> |
| `TaoIsGradientDefined` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoIsGradientDefined/> |
| `TaoIsObjectiveAndGradientDefined` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoIsObjectiveAndGradientDefined/> |
| `TaoIsObjectiveDefined` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoIsObjectiveDefined/> |
| `TaoKSPSetUseEW` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoKSPSetUseEW/> |
| `TaoMonitorCancel` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorCancel/> |
| `TaoMonitorConstraintNorm` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorConstraintNorm/> |
| `TaoMonitorDefault` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorDefault/> |
| `TaoMonitorDefaultShort` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorDefaultShort/> |
| `TaoMonitorDrawCtxCreate` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorDrawCtxCreate/> |
| `TaoMonitorDrawCtxDestroy` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorDrawCtxDestroy/> |
| `TaoMonitorGlobalization` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorGlobalization/> |
| `TaoMonitorGradient` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorGradient/> |
| `TaoMonitorGradientDraw` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorGradientDraw/> |
| `TaoMonitorResidual` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorResidual/> |
| `TaoMonitorSet` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorSet/> |
| `TaoMonitorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorSetFromOptions/> |
| `TaoMonitorSolution` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorSolution/> |
| `TaoMonitorSolutionDraw` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorSolutionDraw/> |
| `TaoMonitorStep` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorStep/> |
| `TaoMonitorStepDraw` | Collective | <https://petsc.org/release/manualpages/Tao/TaoMonitorStepDraw/> |
| `TaoParametersInitialize` | Collective | <https://petsc.org/release/manualpages/Tao/TaoParametersInitialize/> |
| `TaoPythonGetType` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoPythonGetType/> |
| `TaoPythonSetType` | Collective | <https://petsc.org/release/manualpages/Tao/TaoPythonSetType/> |
| `TaoRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Tao/TaoRegister/> |
| `TaoRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoRegisterAll/> |
| `TaoRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoRegisterDestroy/> |
| `TaoResetStatistics` | Collective | <https://petsc.org/release/manualpages/Tao/TaoResetStatistics/> |
| `TaoSetApplicationContext` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetApplicationContext/> |
| `TaoSetConstraintsRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetConstraintsRoutine/> |
| `TaoSetConstraintTolerances` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetConstraintTolerances/> |
| `TaoSetConvergedReason` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetConvergedReason/> |
| `TaoSetConvergenceHistory` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetConvergenceHistory/> |
| `TaoSetConvergenceTest` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetConvergenceTest/> |
| `TaoSetEqualityConstraintsRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetEqualityConstraintsRoutine/> |
| `TaoSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Tao/TaoSetFromOptions/> |
| `TaoSetFunctionLowerBound` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetFunctionLowerBound/> |
| `TaoSetGradient` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetGradient/> |
| `TaoSetGradientNorm` | Collective | <https://petsc.org/release/manualpages/Tao/TaoSetGradientNorm/> |
| `TaoSetHessian` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetHessian/> |
| `TaoSetInequalityBounds` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetInequalityBounds/> |
| `TaoSetInequalityConstraintsRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetInequalityConstraintsRoutine/> |
| `TaoSetInitialTrustRegionRadius` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetInitialTrustRegionRadius/> |
| `TaoSetIterationNumber` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetIterationNumber/> |
| `TaoSetJacobianDesignRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetJacobianDesignRoutine/> |
| `TaoSetJacobianEqualityRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetJacobianEqualityRoutine/> |
| `TaoSetJacobianInequalityRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetJacobianInequalityRoutine/> |
| `TaoSetJacobianResidualRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetJacobianResidualRoutine/> |
| `TaoSetJacobianRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetJacobianRoutine/> |
| `TaoSetJacobianStateRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetJacobianStateRoutine/> |
| `TaoSetMaximumFunctionEvaluations` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetMaximumFunctionEvaluations/> |
| `TaoSetMaximumIterations` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetMaximumIterations/> |
| `TaoSetObjective` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetObjective/> |
| `TaoSetObjectiveAndGradient` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetObjectiveAndGradient/> |
| `TaoSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetOptionsPrefix/> |
| `TaoSetRecycleHistory` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetRecycleHistory/> |
| `TaoSetResidualRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetResidualRoutine/> |
| `TaoSetResidualWeights` | Collective | <https://petsc.org/release/manualpages/Tao/TaoSetResidualWeights/> |
| `TaoSetSolution` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetSolution/> |
| `TaoSetStateDesignIS` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetStateDesignIS/> |
| `TaoSetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetTolerances/> |
| `TaoSetTotalIterationNumber` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetTotalIterationNumber/> |
| `TaoSetType` | Collective | <https://petsc.org/release/manualpages/Tao/TaoSetType/> |
| `TaoSetUp` | Collective | <https://petsc.org/release/manualpages/Tao/TaoSetUp/> |
| `TaoSetUpdate` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetUpdate/> |
| `TaoSetVariableBounds` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetVariableBounds/> |
| `TaoSetVariableBoundsRoutine` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoSetVariableBoundsRoutine/> |
| `TaoShellGetContext` | Not Collective | <https://petsc.org/release/manualpages/Tao/TaoShellGetContext/> |
| `TaoShellSetContext` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoShellSetContext/> |
| `TaoShellSetSolve` | Logically Collective | <https://petsc.org/release/manualpages/Tao/TaoShellSetSolve/> |
| `TaoSoftThreshold` | Collective | <https://petsc.org/release/manualpages/Tao/TaoSoftThreshold/> |
| `TaoSolve` | Collective | <https://petsc.org/release/manualpages/Tao/TaoSolve/> |
| `TaoTestGradient` | Collective | <https://petsc.org/release/manualpages/Tao/TaoTestGradient/> |
| `TaoTestHessian` | Collective | <https://petsc.org/release/manualpages/Tao/TaoTestHessian/> |
| `TaoView` | Collective | <https://petsc.org/release/manualpages/Tao/TaoView/> |
| `TaoViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Tao/TaoViewFromOptions/> |
| `VecFischer` | Logically Collective | <https://petsc.org/release/manualpages/Tao/VecFischer/> |
| `VecSFischer` | Logically Collective | <https://petsc.org/release/manualpages/Tao/VecSFischer/> |

## TaoLineSearch

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `TaoLineSearchAppendOptionsPrefix` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchAppendOptionsPrefix/> |
| `TaoLineSearchApply` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchApply/> |
| `TaoLineSearchComputeGradient` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchComputeGradient/> |
| `TaoLineSearchComputeObjective` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchComputeObjective/> |
| `TaoLineSearchComputeObjectiveAndGradient` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchComputeObjectiveAndGradient/> |
| `TaoLineSearchComputeObjectiveAndGTS` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchComputeObjectiveAndGTS/> |
| `TaoLineSearchCreate` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchCreate/> |
| `TaoLineSearchDestroy` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchDestroy/> |
| `TaoLineSearchGetFullStepObjective` | Not Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetFullStepObjective/> |
| `TaoLineSearchGetNumberFunctionEvaluations` | Not Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetNumberFunctionEvaluations/> |
| `TaoLineSearchGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetOptionsPrefix/> |
| `TaoLineSearchGetSolution` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetSolution/> |
| `TaoLineSearchGetStartingVector` | Not Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetStartingVector/> |
| `TaoLineSearchGetStepDirection` | Not Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetStepDirection/> |
| `TaoLineSearchGetStepLength` | Not Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetStepLength/> |
| `TaoLineSearchGetType` | Not Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetType/> |
| `TaoLineSearchIsUsingTaoRoutines` | Not Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchIsUsingTaoRoutines/> |
| `TaoLineSearchRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchRegister/> |
| `TaoLineSearchReset` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchReset/> |
| `TaoLineSearchSetFromOptions` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetFromOptions/> |
| `TaoLineSearchSetGradientRoutine` | Logically Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetGradientRoutine/> |
| `TaoLineSearchSetInitialStepLength` | Logically Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetInitialStepLength/> |
| `TaoLineSearchSetObjectiveAndGradientRoutine` | Logically Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetObjectiveAndGradientRoutine/> |
| `TaoLineSearchSetObjectiveAndGTSRoutine` | Logically Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetObjectiveAndGTSRoutine/> |
| `TaoLineSearchSetObjectiveRoutine` | Logically Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetObjectiveRoutine/> |
| `TaoLineSearchSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetOptionsPrefix/> |
| `TaoLineSearchSetType` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetType/> |
| `TaoLineSearchSetUp` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetUp/> |
| `TaoLineSearchSetVariableBounds` | Logically Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetVariableBounds/> |
| `TaoLineSearchUseTaoRoutines` | Logically Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchUseTaoRoutines/> |
| `TaoLineSearchView` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchView/> |
| `TaoLineSearchViewFromOptions` | Collective | <https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchViewFromOptions/> |

## TaoTerm

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `TaoTermComputeGradient` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeGradient/> |
| `TaoTermComputeGradientFD` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeGradientFD/> |
| `TaoTermComputeGradientGetUseFD` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeGradientGetUseFD/> |
| `TaoTermComputeGradientSetUseFD` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeGradientSetUseFD/> |
| `TaoTermComputeHessian` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessian/> |
| `TaoTermComputeHessianFD` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessianFD/> |
| `TaoTermComputeHessianGetUseFD` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessianGetUseFD/> |
| `TaoTermComputeHessianMFFD` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessianMFFD/> |
| `TaoTermComputeHessianSetUseFD` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessianSetUseFD/> |
| `TaoTermComputeObjective` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeObjective/> |
| `TaoTermComputeObjectiveAndGradient` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeObjectiveAndGradient/> |
| `TaoTermCreate` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreate/> |
| `TaoTermCreateHalfL2Squared` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateHalfL2Squared/> |
| `TaoTermCreateHessianMatrices` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateHessianMatrices/> |
| `TaoTermCreateHessianMatricesDefault` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateHessianMatricesDefault/> |
| `TaoTermCreateHessianMFFD` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateHessianMFFD/> |
| `TaoTermCreateL1` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateL1/> |
| `TaoTermCreateParametersVec` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateParametersVec/> |
| `TaoTermCreateQuadratic` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateQuadratic/> |
| `TaoTermCreateShell` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateShell/> |
| `TaoTermCreateSolutionVec` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateSolutionVec/> |
| `TaoTermDestroy` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermDestroy/> |
| `TaoTermDuplicate` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermDuplicate/> |
| `TaoTermGetCreateHessianMode` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetCreateHessianMode/> |
| `TaoTermGetFDDelta` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetFDDelta/> |
| `TaoTermGetParametersLayout` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetParametersLayout/> |
| `TaoTermGetParametersMode` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetParametersMode/> |
| `TaoTermGetParametersSizes` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetParametersSizes/> |
| `TaoTermGetParametersVecType` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetParametersVecType/> |
| `TaoTermGetSolutionLayout` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetSolutionLayout/> |
| `TaoTermGetSolutionSizes` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetSolutionSizes/> |
| `TaoTermGetSolutionVecType` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetSolutionVecType/> |
| `TaoTermGetType` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermGetType/> |
| `TaoTermIsComputeHessianFDPossible` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermIsComputeHessianFDPossible/> |
| `TaoTermIsCreateHessianMatricesDefined` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermIsCreateHessianMatricesDefined/> |
| `TaoTermIsGradientDefined` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermIsGradientDefined/> |
| `TaoTermIsHessianDefined` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermIsHessianDefined/> |
| `TaoTermIsObjectiveAndGradientDefined` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermIsObjectiveAndGradientDefined/> |
| `TaoTermIsObjectiveDefined` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermIsObjectiveDefined/> |
| `TaoTermL1GetEpsilon` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermL1GetEpsilon/> |
| `TaoTermL1SetEpsilon` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermL1SetEpsilon/> |
| `TaoTermQuadraticGetMat` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermQuadraticGetMat/> |
| `TaoTermQuadraticSetMat` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermQuadraticSetMat/> |
| `TaoTermRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/TaoTerm/TaoTermRegister/> |
| `TaoTermSetCreateHessianMode` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetCreateHessianMode/> |
| `TaoTermSetFDDelta` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetFDDelta/> |
| `TaoTermSetFromOptions` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetFromOptions/> |
| `TaoTermSetParametersLayout` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersLayout/> |
| `TaoTermSetParametersMode` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersMode/> |
| `TaoTermSetParametersSizes` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersSizes/> |
| `TaoTermSetParametersTemplate` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersTemplate/> |
| `TaoTermSetParametersVecType` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersVecType/> |
| `TaoTermSetSolutionLayout` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetSolutionLayout/> |
| `TaoTermSetSolutionSizes` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetSolutionSizes/> |
| `TaoTermSetSolutionTemplate` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetSolutionTemplate/> |
| `TaoTermSetSolutionVecType` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetSolutionVecType/> |
| `TaoTermSetType` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetType/> |
| `TaoTermSetUp` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSetUp/> |
| `TaoTermShellGetContext` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellGetContext/> |
| `TaoTermShellSetContext` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetContext/> |
| `TaoTermShellSetContextDestroy` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetContextDestroy/> |
| `TaoTermShellSetCreateHessianMatrices` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetCreateHessianMatrices/> |
| `TaoTermShellSetCreateParametersVec` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetCreateParametersVec/> |
| `TaoTermShellSetCreateSolutionVec` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetCreateSolutionVec/> |
| `TaoTermShellSetGradient` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetGradient/> |
| `TaoTermShellSetHessian` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetHessian/> |
| `TaoTermShellSetIsComputeHessianFDPossible` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetIsComputeHessianFDPossible/> |
| `TaoTermShellSetObjective` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetObjective/> |
| `TaoTermShellSetObjectiveAndGradient` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetObjectiveAndGradient/> |
| `TaoTermShellSetView` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetView/> |
| `TaoTermSumAddTerm` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumAddTerm/> |
| `TaoTermSumGetLastTermObjectives` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetLastTermObjectives/> |
| `TaoTermSumGetNumberTerms` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetNumberTerms/> |
| `TaoTermSumGetTerm` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetTerm/> |
| `TaoTermSumGetTermHessianMatrices` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetTermHessianMatrices/> |
| `TaoTermSumGetTermMask` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetTermMask/> |
| `TaoTermSumParametersPack` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumParametersPack/> |
| `TaoTermSumParametersUnpack` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumParametersUnpack/> |
| `TaoTermSumSetNumberTerms` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumSetNumberTerms/> |
| `TaoTermSumSetTerm` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumSetTerm/> |
| `TaoTermSumSetTermHessianMatrices` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumSetTermHessianMatrices/> |
| `TaoTermSumSetTermMask` | Logically collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermSumSetTermMask/> |
| `TaoTermView` | Collective | <https://petsc.org/release/manualpages/TaoTerm/TaoTermView/> |
| `VecNestGetTaoTermSumParameters` | Not collective | <https://petsc.org/release/manualpages/TaoTerm/VecNestGetTaoTermSumParameters/> |

## TS

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `DMCopyDMTS` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMCopyDMTS/> |
| `DMDATSSetIFunctionLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMDATSSetIFunctionLocal/> |
| `DMDATSSetIJacobianLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMDATSSetIJacobianLocal/> |
| `DMDATSSetRHSFunctionLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMDATSSetRHSFunctionLocal/> |
| `DMDATSSetRHSJacobianLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMDATSSetRHSJacobianLocal/> |
| `DMGetDMTS` | Not Collective | <https://petsc.org/release/manualpages/TS/DMGetDMTS/> |
| `DMGetDMTSWrite` | Not Collective | <https://petsc.org/release/manualpages/TS/DMGetDMTSWrite/> |
| `DMPlexTSComputeRHSFunctionFVMCEED` | Collective | <https://petsc.org/release/manualpages/TS/DMPlexTSComputeRHSFunctionFVMCEED/> |
| `DMTSCopy` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSCopy/> |
| `DMTSCreateRHSMassMatrix` | Collective | <https://petsc.org/release/manualpages/TS/DMTSCreateRHSMassMatrix/> |
| `DMTSCreateRHSMassMatrixLumped` | Collective | <https://petsc.org/release/manualpages/TS/DMTSCreateRHSMassMatrixLumped/> |
| `DMTSDestroyRHSMassMatrix` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSDestroyRHSMassMatrix/> |
| `DMTSGetForcingFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSGetForcingFunction/> |
| `DMTSGetI2Function` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSGetI2Function/> |
| `DMTSGetI2Jacobian` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSGetI2Jacobian/> |
| `DMTSGetIFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSGetIFunction/> |
| `DMTSGetIFunctionLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSGetIFunctionLocal/> |
| `DMTSGetIJacobian` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSGetIJacobian/> |
| `DMTSGetIJacobianLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSGetIJacobianLocal/> |
| `DMTSGetRHSFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSGetRHSFunction/> |
| `DMTSGetRHSFunctionLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSGetRHSFunctionLocal/> |
| `DMTSGetRHSJacobian` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSGetRHSJacobian/> |
| `DMTSGetSolutionFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSGetSolutionFunction/> |
| `DMTSGetTransientVariable` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSGetTransientVariable/> |
| `DMTSSetBoundaryLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSSetBoundaryLocal/> |
| `DMTSSetForcingFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetForcingFunction/> |
| `DMTSSetI2Function` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetI2Function/> |
| `DMTSSetI2FunctionContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetI2FunctionContextDestroy/> |
| `DMTSSetI2Jacobian` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetI2Jacobian/> |
| `DMTSSetI2JacobianContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetI2JacobianContextDestroy/> |
| `DMTSSetIFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetIFunction/> |
| `DMTSSetIFunctionContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetIFunctionContextDestroy/> |
| `DMTSSetIFunctionLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSSetIFunctionLocal/> |
| `DMTSSetIFunctionSerialize` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetIFunctionSerialize/> |
| `DMTSSetIJacobian` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetIJacobian/> |
| `DMTSSetIJacobianContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetIJacobianContextDestroy/> |
| `DMTSSetIJacobianLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSSetIJacobianLocal/> |
| `DMTSSetIJacobianSerialize` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetIJacobianSerialize/> |
| `DMTSSetRHSFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetRHSFunction/> |
| `DMTSSetRHSFunctionContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetRHSFunctionContextDestroy/> |
| `DMTSSetRHSFunctionLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSSetRHSFunctionLocal/> |
| `DMTSSetRHSJacobian` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetRHSJacobian/> |
| `DMTSSetRHSJacobianContextDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetRHSJacobianContextDestroy/> |
| `DMTSSetSolutionFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/DMTSSetSolutionFunction/> |
| `DMTSSetTransientVariable` | Logically Collective | <https://petsc.org/release/manualpages/TS/DMTSSetTransientVariable/> |
| `PetscConvEstUseTS` | Not Collective | <https://petsc.org/release/manualpages/TS/PetscConvEstUseTS/> |
| `SNESTSFormFunction` | Logically Collective | <https://petsc.org/release/manualpages/TS/SNESTSFormFunction/> |
| `SNESTSFormJacobian` | Collective | <https://petsc.org/release/manualpages/TS/SNESTSFormJacobian/> |
| `TS2GetSolution` | Not Collective | <https://petsc.org/release/manualpages/TS/TS2GetSolution/> |
| `TS2SetSolution` | Logically Collective | <https://petsc.org/release/manualpages/TS/TS2SetSolution/> |
| `TSAdaptCandidateAdd` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/TS/TSAdaptCandidateAdd/> |
| `TSAdaptCandidatesClear` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptCandidatesClear/> |
| `TSAdaptCandidatesGet` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAdaptCandidatesGet/> |
| `TSAdaptCheckStage` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptCheckStage/> |
| `TSAdaptChoose` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptChoose/> |
| `TSAdaptCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptCreate/> |
| `TSAdaptDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptDestroy/> |
| `TSAdaptDSPSetFilter` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptDSPSetFilter/> |
| `TSAdaptGetClip` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAdaptGetClip/> |
| `TSAdaptGetMaxIgnore` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAdaptGetMaxIgnore/> |
| `TSAdaptGetSafety` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAdaptGetSafety/> |
| `TSAdaptGetScaleSolveFailed` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAdaptGetScaleSolveFailed/> |
| `TSAdaptGetStepLimits` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAdaptGetStepLimits/> |
| `TSAdaptGetType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAdaptGetType/> |
| `TSAdaptHistoryGetStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptHistoryGetStep/> |
| `TSAdaptHistorySetHistory` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptHistorySetHistory/> |
| `TSAdaptHistorySetTrajectory` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptHistorySetTrajectory/> |
| `TSAdaptLoad` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptLoad/> |
| `TSAdaptRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSAdaptRegister/> |
| `TSAdaptRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAdaptRegisterAll/> |
| `TSAdaptReset` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptReset/> |
| `TSAdaptSetAlwaysAccept` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetAlwaysAccept/> |
| `TSAdaptSetCheckStage` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetCheckStage/> |
| `TSAdaptSetClip` | Logically collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetClip/> |
| `TSAdaptSetFromOptions` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetFromOptions/> |
| `TSAdaptSetMaxIgnore` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetMaxIgnore/> |
| `TSAdaptSetMonitor` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetMonitor/> |
| `TSAdaptSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetOptionsPrefix/> |
| `TSAdaptSetSafety` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetSafety/> |
| `TSAdaptSetScaleSolveFailed` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetScaleSolveFailed/> |
| `TSAdaptSetStepLimits` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetStepLimits/> |
| `TSAdaptSetTimeStepIncreaseDelay` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetTimeStepIncreaseDelay/> |
| `TSAdaptSetType` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptSetType/> |
| `TSAdaptView` | Collective | <https://petsc.org/release/manualpages/TS/TSAdaptView/> |
| `TSAlpha2GetParams` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAlpha2GetParams/> |
| `TSAlpha2SetParams` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAlpha2SetParams/> |
| `TSAlpha2SetRadius` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAlpha2SetRadius/> |
| `TSAlphaGetParams` | Not Collective | <https://petsc.org/release/manualpages/TS/TSAlphaGetParams/> |
| `TSAlphaSetParams` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAlphaSetParams/> |
| `TSAlphaSetRadius` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAlphaSetRadius/> |
| `TSAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSAppendOptionsPrefix/> |
| `TSARKIMEXGetFastSlowSplit` | Not Collective | <https://petsc.org/release/manualpages/TS/TSARKIMEXGetFastSlowSplit/> |
| `TSARKIMEXGetFullyImplicit` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSARKIMEXGetFullyImplicit/> |
| `TSARKIMEXGetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSARKIMEXGetType/> |
| `TSARKIMEXRegister` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSARKIMEXRegister/> |
| `TSARKIMEXRegisterAll` | Not Collective, but should be called by all processes which will need the schemes to be registered | <https://petsc.org/release/manualpages/TS/TSARKIMEXRegisterAll/> |
| `TSARKIMEXRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSARKIMEXRegisterDestroy/> |
| `TSARKIMEXSetFastSlowSplit` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSARKIMEXSetFastSlowSplit/> |
| `TSARKIMEXSetFullyImplicit` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSARKIMEXSetFullyImplicit/> |
| `TSARKIMEXSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSARKIMEXSetType/> |
| `TSBasicSymplecticGetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSBasicSymplecticGetType/> |
| `TSBasicSymplecticRegister` | Not Collective, but the same schemes should be registered on all processes on which they will be used | <https://petsc.org/release/manualpages/TS/TSBasicSymplecticRegister/> |
| `TSBasicSymplecticRegisterAll` | Not Collective, but should be called by all processes which will need the schemes to be registered | <https://petsc.org/release/manualpages/TS/TSBasicSymplecticRegisterAll/> |
| `TSBasicSymplecticRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSBasicSymplecticRegisterDestroy/> |
| `TSBasicSymplecticSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSBasicSymplecticSetType/> |
| `TSBDFGetOrder` | Not Collective | <https://petsc.org/release/manualpages/TS/TSBDFGetOrder/> |
| `TSBDFSetOrder` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSBDFSetOrder/> |
| `TSClone` | Collective | <https://petsc.org/release/manualpages/TS/TSClone/> |
| `TSComputeExactError` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeExactError/> |
| `TSComputeForcingFunction` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeForcingFunction/> |
| `TSComputeI2Function` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeI2Function/> |
| `TSComputeI2Jacobian` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeI2Jacobian/> |
| `TSComputeIFunction` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeIFunction/> |
| `TSComputeIFunctionLinear` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeIFunctionLinear/> |
| `TSComputeIJacobian` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeIJacobian/> |
| `TSComputeIJacobianConstant` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeIJacobianConstant/> |
| `TSComputeIJacobianDefaultColor` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeIJacobianDefaultColor/> |
| `TSComputeInitialCondition` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeInitialCondition/> |
| `TSComputeLinearStability` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeLinearStability/> |
| `TSComputeRHSFunction` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeRHSFunction/> |
| `TSComputeRHSFunctionLinear` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeRHSFunctionLinear/> |
| `TSComputeRHSJacobian` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeRHSJacobian/> |
| `TSComputeRHSJacobianConstant` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeRHSJacobianConstant/> |
| `TSComputeSolutionFunction` | Collective | <https://petsc.org/release/manualpages/TS/TSComputeSolutionFunction/> |
| `TSComputeTransientVariable` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSComputeTransientVariable/> |
| `TSCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSCreate/> |
| `TSDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSDestroy/> |
| `TSDIRKGetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSDIRKGetType/> |
| `TSDIRKRegister` | Logically Collective. | <https://petsc.org/release/manualpages/TS/TSDIRKRegister/> |
| `TSDIRKSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSDIRKSetType/> |
| `TSDiscGradGetFormulation` | Not Collective | <https://petsc.org/release/manualpages/TS/TSDiscGradGetFormulation/> |
| `TSDiscGradGetType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSDiscGradGetType/> |
| `TSDiscGradSetFormulation` | Not Collective | <https://petsc.org/release/manualpages/TS/TSDiscGradSetFormulation/> |
| `TSDiscGradSetType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSDiscGradSetType/> |
| `TSDMSwarmMonitorMoments` | Not Collective | <https://petsc.org/release/manualpages/TS/TSDMSwarmMonitorMoments/> |
| `TSEIMEXSetMaxRows` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSEIMEXSetMaxRows/> |
| `TSEIMEXSetOrdAdapt` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSEIMEXSetOrdAdapt/> |
| `TSEIMEXSetRowCol` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSEIMEXSetRowCol/> |
| `TSErrorWeightedENorm` | Collective | <https://petsc.org/release/manualpages/TS/TSErrorWeightedENorm/> |
| `TSErrorWeightedNorm` | Collective | <https://petsc.org/release/manualpages/TS/TSErrorWeightedNorm/> |
| `TSEvaluateStep` | Collective | <https://petsc.org/release/manualpages/TS/TSEvaluateStep/> |
| `TSEvaluateWLTE` | Collective | <https://petsc.org/release/manualpages/TS/TSEvaluateWLTE/> |
| `TSFunctionDomainError` | Collective | <https://petsc.org/release/manualpages/TS/TSFunctionDomainError/> |
| `TSGetAdapt` | Collective if controller has not yet been created | <https://petsc.org/release/manualpages/TS/TSGetAdapt/> |
| `TSGetApplicationContext` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetApplicationContext/> |
| `TSGetAuxSolution` | Not Collective, but v returned is parallel if ts is parallel | <https://petsc.org/release/manualpages/TS/TSGetAuxSolution/> |
| `TSGetCFLTime` | Collective | <https://petsc.org/release/manualpages/TS/TSGetCFLTime/> |
| `TSGetComputeExactError` | Not collective | <https://petsc.org/release/manualpages/TS/TSGetComputeExactError/> |
| `TSGetComputeInitialCondition` | Not collective | <https://petsc.org/release/manualpages/TS/TSGetComputeInitialCondition/> |
| `TSGetConvergedReason` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetConvergedReason/> |
| `TSGetDM` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetDM/> |
| `TSGetEquationType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetEquationType/> |
| `TSGetEvaluationTimes` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetEvaluationTimes/> |
| `TSGetExactFinalTime` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetExactFinalTime/> |
| `TSGetI2Function` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetI2Function/> |
| `TSGetI2Jacobian` | Not Collective, but parallel objects are returned if TS is parallel | <https://petsc.org/release/manualpages/TS/TSGetI2Jacobian/> |
| `TSGetIFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetIFunction/> |
| `TSGetIJacobian` | Not Collective, but parallel objects are returned if ts is parallel | <https://petsc.org/release/manualpages/TS/TSGetIJacobian/> |
| `TSGetKSP` | Not Collective, but ksp is parallel if ts is parallel | <https://petsc.org/release/manualpages/TS/TSGetKSP/> |
| `TSGetKSPIterations` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetKSPIterations/> |
| `TSGetMaxSteps` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetMaxSteps/> |
| `TSGetMaxTime` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetMaxTime/> |
| `TSGetNumEvents` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSGetNumEvents/> |
| `TSGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetOptionsPrefix/> |
| `TSGetPrevTime` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetPrevTime/> |
| `TSGetProblemType` | Not collective | <https://petsc.org/release/manualpages/TS/TSGetProblemType/> |
| `TSGetRHSFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetRHSFunction/> |
| `TSGetRHSJacobian` | Not Collective, but parallel objects are returned if ts is parallel | <https://petsc.org/release/manualpages/TS/TSGetRHSJacobian/> |
| `TSGetRunSteps` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetRunSteps/> |
| `TSGetSNES` | Not Collective, but snes is parallel if ts is parallel | <https://petsc.org/release/manualpages/TS/TSGetSNES/> |
| `TSGetSNESFailures` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetSNESFailures/> |
| `TSGetSNESIterations` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetSNESIterations/> |
| `TSGetSolution` | Not Collective, but v returned is parallel if ts is parallel | <https://petsc.org/release/manualpages/TS/TSGetSolution/> |
| `TSGetSolutionComponents` | Not Collective, but v returned is parallel if ts is parallel | <https://petsc.org/release/manualpages/TS/TSGetSolutionComponents/> |
| `TSGetSolveTime` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetSolveTime/> |
| `TSGetStepNumber` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetStepNumber/> |
| `TSGetStepRejections` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetStepRejections/> |
| `TSGetStepResize` | Not collective | <https://petsc.org/release/manualpages/TS/TSGetStepResize/> |
| `TSGetStepRollBack` | Not collective | <https://petsc.org/release/manualpages/TS/TSGetStepRollBack/> |
| `TSGetTime` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetTime/> |
| `TSGetTimeError` | Not Collective, but v returned is parallel if ts is parallel | <https://petsc.org/release/manualpages/TS/TSGetTimeError/> |
| `TSGetTimeSpan` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetTimeSpan/> |
| `TSGetTimeStep` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetTimeStep/> |
| `TSGetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSGetTolerances/> |
| `TSGetTrajectory` | Collective | <https://petsc.org/release/manualpages/TS/TSGetTrajectory/> |
| `TSGetType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetType/> |
| `TSGetUseSplitRHSFunction` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGetUseSplitRHSFunction/> |
| `TSGLEEGetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSGLEEGetType/> |
| `TSGLEERegister` | Not Collective, but the same schemes should be registered on all processes on which they will be used, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSGLEERegister/> |
| `TSGLEERegisterAll` | Not Collective, but should be called by all processes which will need the schemes to be registered | <https://petsc.org/release/manualpages/TS/TSGLEERegisterAll/> |
| `TSGLEERegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGLEERegisterDestroy/> |
| `TSGLEESetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSGLEESetType/> |
| `TSGLLEAcceptRegister` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAcceptRegister/> |
| `TSGLLEAdaptChoose` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptChoose/> |
| `TSGLLEAdaptCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptCreate/> |
| `TSGLLEAdaptDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptDestroy/> |
| `TSGLLEAdaptRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptRegister/> |
| `TSGLLEAdaptRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptRegisterAll/> |
| `TSGLLEAdaptSetFromOptions` | Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptSetFromOptions/> |
| `TSGLLEAdaptSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptSetOptionsPrefix/> |
| `TSGLLEAdaptSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptSetType/> |
| `TSGLLEAdaptView` | Collective | <https://petsc.org/release/manualpages/TS/TSGLLEAdaptView/> |
| `TSGLLEGetAdapt` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGLLEGetAdapt/> |
| `TSGLLERegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSGLLERegister/> |
| `TSGLLERegisterAll` | Not Collective | <https://petsc.org/release/manualpages/TS/TSGLLERegisterAll/> |
| `TSGLLESetAcceptType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSGLLESetAcceptType/> |
| `TSGLLESetType` | Collective | <https://petsc.org/release/manualpages/TS/TSGLLESetType/> |
| `TSHasTransientVariable` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSHasTransientVariable/> |
| `TSInterpolate` | Collective | <https://petsc.org/release/manualpages/TS/TSInterpolate/> |
| `TSIRKGetNumStages` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSIRKGetNumStages/> |
| `TSIRKGetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSIRKGetType/> |
| `TSIRKRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSIRKRegister/> |
| `TSIRKRegisterAll` | Not Collective, but should be called by all processes which will need the schemes to be registered | <https://petsc.org/release/manualpages/TS/TSIRKRegisterAll/> |
| `TSIRKRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSIRKRegisterDestroy/> |
| `TSIRKSetNumStages` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSIRKSetNumStages/> |
| `TSIRKSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSIRKSetType/> |
| `TSIRKTableauCreate` | Not Collective | <https://petsc.org/release/manualpages/TS/TSIRKTableauCreate/> |
| `TSLoad` | Collective | <https://petsc.org/release/manualpages/TS/TSLoad/> |
| `TSMonitor` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitor/> |
| `TSMonitorCancel` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSMonitorCancel/> |
| `TSMonitorDMDARay` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorDMDARay/> |
| `TSMonitorDMDARayDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorDMDARayDestroy/> |
| `TSMonitorDrawCtxCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorDrawCtxCreate/> |
| `TSMonitorDrawCtxDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorDrawCtxDestroy/> |
| `TSMonitorDrawError` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorDrawError/> |
| `TSMonitorDrawSolution` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorDrawSolution/> |
| `TSMonitorDrawSolutionFunction` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorDrawSolutionFunction/> |
| `TSMonitorDrawSolutionPhase` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorDrawSolutionPhase/> |
| `TSMonitorEnvelope` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorEnvelope/> |
| `TSMonitorEnvelopeCtxCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorEnvelopeCtxCreate/> |
| `TSMonitorEnvelopeCtxDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorEnvelopeCtxDestroy/> |
| `TSMonitorEnvelopeGetBounds` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorEnvelopeGetBounds/> |
| `TSMonitorError` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorError/> |
| `TSMonitorHGCtxCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorHGCtxCreate/> |
| `TSMonitorHGCtxDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSMonitorHGCtxDestroy/> |
| `TSMonitorLGCtxCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGCtxCreate/> |
| `TSMonitorLGCtxDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGCtxDestroy/> |
| `TSMonitorLGCtxNetworkCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGCtxNetworkCreate/> |
| `TSMonitorLGCtxNetworkDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGCtxNetworkDestroy/> |
| `TSMonitorLGCtxNetworkSolution` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGCtxNetworkSolution/> |
| `TSMonitorLGCtxSetDisplayVariables` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGCtxSetDisplayVariables/> |
| `TSMonitorLGCtxSetTransform` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGCtxSetTransform/> |
| `TSMonitorLGCtxSetVariableNames` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGCtxSetVariableNames/> |
| `TSMonitorLGDMDARay` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGDMDARay/> |
| `TSMonitorLGError` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGError/> |
| `TSMonitorLGGetVariableNames` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGGetVariableNames/> |
| `TSMonitorLGKSPIterations` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGKSPIterations/> |
| `TSMonitorLGSetDisplayVariables` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGSetDisplayVariables/> |
| `TSMonitorLGSetTransform` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGSetTransform/> |
| `TSMonitorLGSetVariableNames` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGSetVariableNames/> |
| `TSMonitorLGSNESIterations` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGSNESIterations/> |
| `TSMonitorLGSolution` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGSolution/> |
| `TSMonitorLGTimeStep` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorLGTimeStep/> |
| `TSMonitorSet` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSet/> |
| `TSMonitorSetFromOptions` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSetFromOptions/> |
| `TSMonitorSolution` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSolution/> |
| `TSMonitorSolutionSetup` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSolutionSetup/> |
| `TSMonitorSolutionVTK` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSolutionVTK/> |
| `TSMonitorSolutionVTKCtxCreate` | Not collective | <https://petsc.org/release/manualpages/TS/TSMonitorSolutionVTKCtxCreate/> |
| `TSMonitorSolutionVTKDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSolutionVTKDestroy/> |
| `TSMonitorSPCtxCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSPCtxCreate/> |
| `TSMonitorSPCtxDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSPCtxDestroy/> |
| `TSMonitorSPEig` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSPEig/> |
| `TSMonitorSPEigCtxCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSPEigCtxCreate/> |
| `TSMonitorSPEigCtxDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSMonitorSPEigCtxDestroy/> |
| `TSMPRKGetType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSMPRKGetType/> |
| `TSMPRKRegister` | Not Collective, but the same schemes should be registered on all processes on which they will be used, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSMPRKRegister/> |
| `TSMPRKRegisterAll` | Not Collective, but should be called by all processes which will need the schemes to be registered | <https://petsc.org/release/manualpages/TS/TSMPRKRegisterAll/> |
| `TSMPRKRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSMPRKRegisterDestroy/> |
| `TSMPRKSetType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSMPRKSetType/> |
| `TSPostEvaluate` | Collective | <https://petsc.org/release/manualpages/TS/TSPostEvaluate/> |
| `TSPostStage` | Collective | <https://petsc.org/release/manualpages/TS/TSPostStage/> |
| `TSPostStep` | Collective | <https://petsc.org/release/manualpages/TS/TSPostStep/> |
| `TSPreStage` | Collective | <https://petsc.org/release/manualpages/TS/TSPreStage/> |
| `TSPreStep` | Collective | <https://petsc.org/release/manualpages/TS/TSPreStep/> |
| `TSPruneIJacobianColor` | Collective | <https://petsc.org/release/manualpages/TS/TSPruneIJacobianColor/> |
| `TSPseudoComputeFunction` | Collective | <https://petsc.org/release/manualpages/TS/TSPseudoComputeFunction/> |
| `TSPseudoIncrementDtFromInitialDt` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSPseudoIncrementDtFromInitialDt/> |
| `TSPseudoSetMaxTimeStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSPseudoSetMaxTimeStep/> |
| `TSPseudoSetTimeStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSPseudoSetTimeStep/> |
| `TSPseudoSetTimeStepIncrement` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSPseudoSetTimeStepIncrement/> |
| `TSPseudoSetVerifyTimeStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSPseudoSetVerifyTimeStep/> |
| `TSPseudoTimeStepDefault` | Collective, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSPseudoTimeStepDefault/> |
| `TSPythonGetType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSPythonGetType/> |
| `TSPythonSetType` | Collective | <https://petsc.org/release/manualpages/TS/TSPythonSetType/> |
| `TSRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSRegister/> |
| `TSRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/TS/TSRegisterAll/> |
| `TSRemoveTrajectory` | Collective | <https://petsc.org/release/manualpages/TS/TSRemoveTrajectory/> |
| `TSReset` | Collective | <https://petsc.org/release/manualpages/TS/TSReset/> |
| `TSResetTrajectory` | Collective | <https://petsc.org/release/manualpages/TS/TSResetTrajectory/> |
| `TSResize` | Collective | <https://petsc.org/release/manualpages/TS/TSResize/> |
| `TSResizeRegisterVec` | Collective | <https://petsc.org/release/manualpages/TS/TSResizeRegisterVec/> |
| `TSResizeRetrieveVec` | Collective | <https://petsc.org/release/manualpages/TS/TSResizeRetrieveVec/> |
| `TSRestartStep` | Collective | <https://petsc.org/release/manualpages/TS/TSRestartStep/> |
| `TSRHSJacobianSetReuse` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSJacobianSetReuse/> |
| `TSRHSJacobianTest` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSJacobianTest/> |
| `TSRHSJacobianTestTranspose` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSJacobianTestTranspose/> |
| `TSRHSSplitGetIS` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSSplitGetIS/> |
| `TSRHSSplitGetSNES` | Not Collective, but snes is parallel if ts is parallel | <https://petsc.org/release/manualpages/TS/TSRHSSplitGetSNES/> |
| `TSRHSSplitGetSubTS` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSSplitGetSubTS/> |
| `TSRHSSplitGetSubTSs` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSSplitGetSubTSs/> |
| `TSRHSSplitSetIFunction` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSSplitSetIFunction/> |
| `TSRHSSplitSetIJacobian` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSSplitSetIJacobian/> |
| `TSRHSSplitSetIS` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSSplitSetIS/> |
| `TSRHSSplitSetRHSFunction` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRHSSplitSetRHSFunction/> |
| `TSRHSSplitSetSNES` | Collective | <https://petsc.org/release/manualpages/TS/TSRHSSplitSetSNES/> |
| `TSRKGetMultirate` | Not Collective | <https://petsc.org/release/manualpages/TS/TSRKGetMultirate/> |
| `TSRKGetOrder` | Not Collective | <https://petsc.org/release/manualpages/TS/TSRKGetOrder/> |
| `TSRKGetTableau` | Not Collective | <https://petsc.org/release/manualpages/TS/TSRKGetTableau/> |
| `TSRKGetType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSRKGetType/> |
| `TSRKRegister` | Not Collective, but the same schemes should be registered on all processes on which they will be used, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSRKRegister/> |
| `TSRKRegisterAll` | Not Collective, but should be called by all processes which will need the schemes to be registered | <https://petsc.org/release/manualpages/TS/TSRKRegisterAll/> |
| `TSRKRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSRKRegisterDestroy/> |
| `TSRKSetMultirate` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRKSetMultirate/> |
| `TSRKSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRKSetType/> |
| `TSRollBack` | Collective | <https://petsc.org/release/manualpages/TS/TSRollBack/> |
| `TSRosWGetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRosWGetType/> |
| `TSRosWRegister` | Not Collective, but the same schemes should be registered on all processes on which they will be used | <https://petsc.org/release/manualpages/TS/TSRosWRegister/> |
| `TSRosWRegisterAll` | Not Collective, but should be called by all MPI processes which will need the schemes to be registered | <https://petsc.org/release/manualpages/TS/TSRosWRegisterAll/> |
| `TSRosWRegisterDestroy` | Not Collective | <https://petsc.org/release/manualpages/TS/TSRosWRegisterDestroy/> |
| `TSRosWRegisterRos4` | Not Collective, but the same schemes should be registered on all processes on which they will be used | <https://petsc.org/release/manualpages/TS/TSRosWRegisterRos4/> |
| `TSRosWSetRecomputeJacobian` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRosWSetRecomputeJacobian/> |
| `TSRosWSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSRosWSetType/> |
| `TSSetApplicationContext` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetApplicationContext/> |
| `TSSetCFLTimeLocal` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetCFLTimeLocal/> |
| `TSSetComputeExactError` | Logically collective | <https://petsc.org/release/manualpages/TS/TSSetComputeExactError/> |
| `TSSetComputeInitialCondition` | Logically collective | <https://petsc.org/release/manualpages/TS/TSSetComputeInitialCondition/> |
| `TSSetConvergedReason` | Logically Collective; reason must contain common value | <https://petsc.org/release/manualpages/TS/TSSetConvergedReason/> |
| `TSSetDM` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetDM/> |
| `TSSetEquationType` | Not Collective | <https://petsc.org/release/manualpages/TS/TSSetEquationType/> |
| `TSSetErrorIfStepFails` | Not Collective | <https://petsc.org/release/manualpages/TS/TSSetErrorIfStepFails/> |
| `TSSetEvaluationTimes` | Collective | <https://petsc.org/release/manualpages/TS/TSSetEvaluationTimes/> |
| `TSSetEventHandler` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetEventHandler/> |
| `TSSetEventTolerances` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetEventTolerances/> |
| `TSSetExactFinalTime` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetExactFinalTime/> |
| `TSSetForcingFunction` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetForcingFunction/> |
| `TSSetFromOptions` | Collective | <https://petsc.org/release/manualpages/TS/TSSetFromOptions/> |
| `TSSetFunctionDomainError` | Logically collective | <https://petsc.org/release/manualpages/TS/TSSetFunctionDomainError/> |
| `TSSetI2Function` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetI2Function/> |
| `TSSetI2Jacobian` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetI2Jacobian/> |
| `TSSetIFunction` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetIFunction/> |
| `TSSetIJacobian` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetIJacobian/> |
| `TSSetMatStructure` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetMatStructure/> |
| `TSSetMaxSNESFailures` | Not Collective | <https://petsc.org/release/manualpages/TS/TSSetMaxSNESFailures/> |
| `TSSetMaxStepRejections` | Not Collective | <https://petsc.org/release/manualpages/TS/TSSetMaxStepRejections/> |
| `TSSetMaxSteps` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetMaxSteps/> |
| `TSSetMaxTime` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetMaxTime/> |
| `TSSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetOptionsPrefix/> |
| `TSSetPostEvaluate` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetPostEvaluate/> |
| `TSSetPostEventSecondStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetPostEventSecondStep/> |
| `TSSetPostEventStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetPostEventStep/> |
| `TSSetPostStage` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetPostStage/> |
| `TSSetPostStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetPostStep/> |
| `TSSetPreStage` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetPreStage/> |
| `TSSetPreStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetPreStep/> |
| `TSSetProblemType` | Not collective | <https://petsc.org/release/manualpages/TS/TSSetProblemType/> |
| `TSSetResize` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetResize/> |
| `TSSetRHSFunction` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetRHSFunction/> |
| `TSSetRHSJacobian` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetRHSJacobian/> |
| `TSSetRunSteps` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetRunSteps/> |
| `TSSetSaveTrajectory` | Collective | <https://petsc.org/release/manualpages/TS/TSSetSaveTrajectory/> |
| `TSSetSNES` | Collective | <https://petsc.org/release/manualpages/TS/TSSetSNES/> |
| `TSSetSolution` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetSolution/> |
| `TSSetSolutionFunction` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetSolutionFunction/> |
| `TSSetStepNumber` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetStepNumber/> |
| `TSSetTime` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetTime/> |
| `TSSetTimeError` | Not Collective, but v returned is parallel if ts is parallel | <https://petsc.org/release/manualpages/TS/TSSetTimeError/> |
| `TSSetTimeSpan` | Collective | <https://petsc.org/release/manualpages/TS/TSSetTimeSpan/> |
| `TSSetTimeStep` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetTimeStep/> |
| `TSSetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetTolerances/> |
| `TSSetTransientVariable` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetTransientVariable/> |
| `TSSetType` | Collective | <https://petsc.org/release/manualpages/TS/TSSetType/> |
| `TSSetUp` | Collective | <https://petsc.org/release/manualpages/TS/TSSetUp/> |
| `TSSetUseSplitRHSFunction` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSetUseSplitRHSFunction/> |
| `TSSolve` | Collective | <https://petsc.org/release/manualpages/TS/TSSolve/> |
| `TSSSPGetNumStages` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSSPGetNumStages/> |
| `TSSSPGetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSSPGetType/> |
| `TSSSPSetNumStages` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSSPSetNumStages/> |
| `TSSSPSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSSPSetType/> |
| `TSStep` | Collective | <https://petsc.org/release/manualpages/TS/TSStep/> |
| `TSSundialsGetIterations` | Not Collective | <https://petsc.org/release/manualpages/TS/TSSundialsGetIterations/> |
| `TSSundialsSetGramSchmidtType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSundialsSetGramSchmidtType/> |
| `TSSundialsSetLinearTolerance` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSundialsSetLinearTolerance/> |
| `TSSundialsSetMaxl` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSundialsSetMaxl/> |
| `TSSundialsSetMaxord` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSundialsSetMaxord/> |
| `TSSundialsSetTolerance` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSundialsSetTolerance/> |
| `TSSundialsSetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSundialsSetType/> |
| `TSSundialsSetUseDense` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSSundialsSetUseDense/> |
| `TSThetaGetEndpoint` | Not Collective | <https://petsc.org/release/manualpages/TS/TSThetaGetEndpoint/> |
| `TSThetaGetTheta` | Not Collective | <https://petsc.org/release/manualpages/TS/TSThetaGetTheta/> |
| `TSThetaSetEndpoint` | Not Collective | <https://petsc.org/release/manualpages/TS/TSThetaSetEndpoint/> |
| `TSThetaSetTheta` | Not Collective | <https://petsc.org/release/manualpages/TS/TSThetaSetTheta/> |
| `TSTrajectoryCreate` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryCreate/> |
| `TSTrajectoryDestroy` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryDestroy/> |
| `TSTrajectoryGet` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryGet/> |
| `TSTrajectoryGetNumSteps` | Not Collective. | <https://petsc.org/release/manualpages/TS/TSTrajectoryGetNumSteps/> |
| `TSTrajectoryGetSolutionOnly` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryGetSolutionOnly/> |
| `TSTrajectoryGetType` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryGetType/> |
| `TSTrajectoryGetUpdatedHistoryVecs` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryGetUpdatedHistoryVecs/> |
| `TSTrajectoryGetVecs` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryGetVecs/> |
| `TSTrajectoryMemorySetType` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryMemorySetType/> |
| `TSTrajectoryRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/TS/TSTrajectoryRegister/> |
| `TSTrajectoryRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryRegisterAll/> |
| `TSTrajectoryReset` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryReset/> |
| `TSTrajectoryRestoreUpdatedHistoryVecs` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryRestoreUpdatedHistoryVecs/> |
| `TSTrajectorySet` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySet/> |
| `TSTrajectorySetDirname` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetDirname/> |
| `TSTrajectorySetFiletemplate` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetFiletemplate/> |
| `TSTrajectorySetFromOptions` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetFromOptions/> |
| `TSTrajectorySetKeepFiles` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetKeepFiles/> |
| `TSTrajectorySetMaxCpsDisk` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetMaxCpsDisk/> |
| `TSTrajectorySetMaxCpsRAM` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetMaxCpsRAM/> |
| `TSTrajectorySetMaxUnitsDisk` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetMaxUnitsDisk/> |
| `TSTrajectorySetMaxUnitsRAM` | Logically Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetMaxUnitsRAM/> |
| `TSTrajectorySetMonitor` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetMonitor/> |
| `TSTrajectorySetSolutionOnly` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetSolutionOnly/> |
| `TSTrajectorySetTransform` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetTransform/> |
| `TSTrajectorySetType` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetType/> |
| `TSTrajectorySetUp` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetUp/> |
| `TSTrajectorySetUseHistory` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetUseHistory/> |
| `TSTrajectorySetVariableNames` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectorySetVariableNames/> |
| `TSTrajectoryView` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryView/> |
| `TSTrajectoryViewFromOptions` | Collective | <https://petsc.org/release/manualpages/TS/TSTrajectoryViewFromOptions/> |
| `TSView` | Collective | <https://petsc.org/release/manualpages/TS/TSView/> |
| `TSViewFromOptions` | Collective | <https://petsc.org/release/manualpages/TS/TSViewFromOptions/> |

## Vec

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `ISComplementVec` | Collective | <https://petsc.org/release/manualpages/Vec/ISComplementVec/> |
| `PetscCommSplitReductionBegin` | Collective but not synchronizing | <https://petsc.org/release/manualpages/Vec/PetscCommSplitReductionBegin/> |
| `PetscOptionsGetVec` | Collective | <https://petsc.org/release/manualpages/Vec/PetscOptionsGetVec/> |
| `PetscSectionVecView` | Collective | <https://petsc.org/release/manualpages/Vec/PetscSectionVecView/> |
| `VecAbs` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecAbs/> |
| `VecAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecAppendOptionsPrefix/> |
| `VecAssemblyBegin` | Collective | <https://petsc.org/release/manualpages/Vec/VecAssemblyBegin/> |
| `VecAssemblyEnd` | Collective | <https://petsc.org/release/manualpages/Vec/VecAssemblyEnd/> |
| `VecAXPBY` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecAXPBY/> |
| `VecAXPBYPCZ` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecAXPBYPCZ/> |
| `VecAXPY` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecAXPY/> |
| `VecAYPX` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecAYPX/> |
| `VecBindToCPU` | Logically collective | <https://petsc.org/release/manualpages/Vec/VecBindToCPU/> |
| `VecBoundToCPU` | Not collective | <https://petsc.org/release/manualpages/Vec/VecBoundToCPU/> |
| `VecCheckAssembled` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecCheckAssembled/> |
| `VecConcatenate` | Collective | <https://petsc.org/release/manualpages/Vec/VecConcatenate/> |
| `VecConjugate` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecConjugate/> |
| `VecCopy` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecCopy/> |
| `VecCreate` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreate/> |
| `VecCreateFromOptions` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateFromOptions/> |
| `VecCreateGhost` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateGhost/> |
| `VecCreateGhostBlock` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateGhostBlock/> |
| `VecCreateGhostBlockWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateGhostBlockWithArray/> |
| `VecCreateGhostWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateGhostWithArray/> |
| `VecCreateLocalVector` | Not Collective. | <https://petsc.org/release/manualpages/Vec/VecCreateLocalVector/> |
| `VecCreateMPI` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateMPI/> |
| `VecCreateMPICUDA` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateMPICUDA/> |
| `VecCreateMPICUDAWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateMPICUDAWithArray/> |
| `VecCreateMPICUDAWithArrays` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateMPICUDAWithArrays/> |
| `VecCreateMPIHIP` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateMPIHIP/> |
| `VecCreateMPIHIPWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateMPIHIPWithArray/> |
| `VecCreateMPIHIPWithArrays` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateMPIHIPWithArrays/> |
| `VecCreateMPIKokkosWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateMPIKokkosWithArray/> |
| `VecCreateMPIViennaCLWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateMPIViennaCLWithArray/> |
| `VecCreateMPIViennaCLWithArrays` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateMPIViennaCLWithArrays/> |
| `VecCreateMPIWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateMPIWithArray/> |
| `VecCreateNest` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateNest/> |
| `VecCreateSeq` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateSeq/> |
| `VecCreateSeqCUDA` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateSeqCUDA/> |
| `VecCreateSeqCUDAWithArray` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateSeqCUDAWithArray/> |
| `VecCreateSeqCUDAWithArrays` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateSeqCUDAWithArrays/> |
| `VecCreateSeqHIP` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateSeqHIP/> |
| `VecCreateSeqHIPWithArray` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateSeqHIPWithArray/> |
| `VecCreateSeqHIPWithArrays` | Collective, Possibly Synchronous | <https://petsc.org/release/manualpages/Vec/VecCreateSeqHIPWithArrays/> |
| `VecCreateSeqKokkos` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateSeqKokkos/> |
| `VecCreateSeqKokkosWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateSeqKokkosWithArray/> |
| `VecCreateSeqViennaCL` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateSeqViennaCL/> |
| `VecCreateSeqViennaCLWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateSeqViennaCLWithArray/> |
| `VecCreateSeqViennaCLWithArrays` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateSeqViennaCLWithArrays/> |
| `VecCreateSeqWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateSeqWithArray/> |
| `VecCreateShared` | Collective | <https://petsc.org/release/manualpages/Vec/VecCreateShared/> |
| `VecCUDAGetArray` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecCUDAGetArray/> |
| `VecCUDAGetArrayRead` | Not Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecCUDAGetArrayRead/> |
| `VecCUDAGetArrayWrite` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecCUDAGetArrayWrite/> |
| `VecCUDAPlaceArray` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecCUDAPlaceArray/> |
| `VecCUDAReplaceArray` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecCUDAReplaceArray/> |
| `VecCUDAResetArray` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecCUDAResetArray/> |
| `VecCUDARestoreArrayRead` | Not Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecCUDARestoreArrayRead/> |
| `VecCUDARestoreArrayWrite` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecCUDARestoreArrayWrite/> |
| `VecDestroy` | Collective | <https://petsc.org/release/manualpages/Vec/VecDestroy/> |
| `VecDestroyVecs` | Collective | <https://petsc.org/release/manualpages/Vec/VecDestroyVecs/> |
| `VecDot` | Collective | <https://petsc.org/release/manualpages/Vec/VecDot/> |
| `VecDotNorm2` | Collective | <https://petsc.org/release/manualpages/Vec/VecDotNorm2/> |
| `VecDotRealPart` | Collective | <https://petsc.org/release/manualpages/Vec/VecDotRealPart/> |
| `VecDuplicate` | Collective | <https://petsc.org/release/manualpages/Vec/VecDuplicate/> |
| `VecDuplicateVecs` | Collective | <https://petsc.org/release/manualpages/Vec/VecDuplicateVecs/> |
| `VecEqual` | Collective | <https://petsc.org/release/manualpages/Vec/VecEqual/> |
| `VecErrorWeightedNorms` | Collective | <https://petsc.org/release/manualpages/Vec/VecErrorWeightedNorms/> |
| `VecExp` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecExp/> |
| `VecFlag` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecFlag/> |
| `VecGetArray` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray/> |
| `VecGetArray1d` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray1d/> |
| `VecGetArray1dRead` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray1dRead/> |
| `VecGetArray1dWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray1dWrite/> |
| `VecGetArray2d` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray2d/> |
| `VecGetArray2dRead` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray2dRead/> |
| `VecGetArray2dWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray2dWrite/> |
| `VecGetArray3d` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray3d/> |
| `VecGetArray3dRead` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray3dRead/> |
| `VecGetArray3dWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray3dWrite/> |
| `VecGetArray4d` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray4d/> |
| `VecGetArray4dRead` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray4dRead/> |
| `VecGetArray4dWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArray4dWrite/> |
| `VecGetArrayAndMemType` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecGetArrayAndMemType/> |
| `VecGetArrayPair` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecGetArrayPair/> |
| `VecGetArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetArrayRead/> |
| `VecGetArrayReadAndMemType` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecGetArrayReadAndMemType/> |
| `VecGetArrays` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecGetArrays/> |
| `VecGetArrayWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetArrayWrite/> |
| `VecGetArrayWriteAndMemType` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecGetArrayWriteAndMemType/> |
| `VecGetBlockSize` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetBlockSize/> |
| `VecGetLayout` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetLayout/> |
| `VecGetLocalSize` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetLocalSize/> |
| `VecGetLocalToGlobalMapping` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetLocalToGlobalMapping/> |
| `VecGetLocalVector` | Collective | <https://petsc.org/release/manualpages/Vec/VecGetLocalVector/> |
| `VecGetLocalVectorRead` | Not Collective. | <https://petsc.org/release/manualpages/Vec/VecGetLocalVectorRead/> |
| `VecGetOffloadMask` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetOffloadMask/> |
| `VecGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetOptionsPrefix/> |
| `VecGetOwnershipRange` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetOwnershipRange/> |
| `VecGetOwnershipRanges` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetOwnershipRanges/> |
| `VecGetPinnedMemoryMin` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGetPinnedMemoryMin/> |
| `VecGetSize` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetSize/> |
| `VecGetState` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetState/> |
| `VecGetSubVector` | Collective | <https://petsc.org/release/manualpages/Vec/VecGetSubVector/> |
| `VecGetType` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetType/> |
| `VecGetValues` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetValues/> |
| `VecGetValuesSection` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGetValuesSection/> |
| `VecGhostGetLocalForm` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGhostGetLocalForm/> |
| `VecGhostIsLocalForm` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecGhostIsLocalForm/> |
| `VecGhostRestoreLocalForm` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecGhostRestoreLocalForm/> |
| `VecGhostUpdateBegin` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Vec/VecGhostUpdateBegin/> |
| `VecGhostUpdateEnd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Vec/VecGhostUpdateEnd/> |
| `VecHIPGetArray` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPGetArray/> |
| `VecHIPGetArrayRead` | Not Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPGetArrayRead/> |
| `VecHIPGetArrayWrite` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPGetArrayWrite/> |
| `VecHIPPlaceArray` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPPlaceArray/> |
| `VecHIPReplaceArray` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPReplaceArray/> |
| `VecHIPResetArray` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPResetArray/> |
| `VecHIPRestoreArray` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPRestoreArray/> |
| `VecHIPRestoreArrayRead` | Not Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPRestoreArrayRead/> |
| `VecHIPRestoreArrayWrite` | Logically Collective; Asynchronous; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecHIPRestoreArrayWrite/> |
| `VecImaginaryPart` | Collective | <https://petsc.org/release/manualpages/Vec/VecImaginaryPart/> |
| `VecISAXPY` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecISAXPY/> |
| `VecISCopy` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecISCopy/> |
| `VecISSet` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecISSet/> |
| `VecISShift` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecISShift/> |
| `VecKokkosPlaceArray` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecKokkosPlaceArray/> |
| `VecKokkosResetArray` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecKokkosResetArray/> |
| `VecLoad` | Collective | <https://petsc.org/release/manualpages/Vec/VecLoad/> |
| `VecLocked` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecLocked/> |
| `VecLockGet` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecLockGet/> |
| `VecLockGetLocation` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecLockGetLocation/> |
| `VecLockReadPop` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecLockReadPop/> |
| `VecLockReadPush` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecLockReadPush/> |
| `VecLockWriteSet` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecLockWriteSet/> |
| `VecLog` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecLog/> |
| `VecMax` | Collective | <https://petsc.org/release/manualpages/Vec/VecMax/> |
| `VecMAXPBY` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecMAXPBY/> |
| `VecMaxPointwiseDivide` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecMaxPointwiseDivide/> |
| `VecMAXPY` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecMAXPY/> |
| `VecMDot` | Collective | <https://petsc.org/release/manualpages/Vec/VecMDot/> |
| `VecMean` | Collective | <https://petsc.org/release/manualpages/Vec/VecMean/> |
| `VecMedian` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecMedian/> |
| `VecMin` | Collective | <https://petsc.org/release/manualpages/Vec/VecMin/> |
| `VecMPISetGhost` | Collective | <https://petsc.org/release/manualpages/Vec/VecMPISetGhost/> |
| `VecMTDot` | Collective | <https://petsc.org/release/manualpages/Vec/VecMTDot/> |
| `VecNestGetSize` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecNestGetSize/> |
| `VecNestGetSubVec` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecNestGetSubVec/> |
| `VecNestGetSubVecs` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecNestGetSubVecs/> |
| `VecNestGetSubVecsRead` | Logically collective | <https://petsc.org/release/manualpages/Vec/VecNestGetSubVecsRead/> |
| `VecNestRestoreSubVecsRead` | Logically collective | <https://petsc.org/release/manualpages/Vec/VecNestRestoreSubVecsRead/> |
| `VecNestSetSubVec` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecNestSetSubVec/> |
| `VecNestSetSubVecs` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecNestSetSubVecs/> |
| `VecNorm` | Collective | <https://petsc.org/release/manualpages/Vec/VecNorm/> |
| `VecNormalize` | Collective | <https://petsc.org/release/manualpages/Vec/VecNormalize/> |
| `VecNormAvailable` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecNormAvailable/> |
| `VecPlaceArray` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecPlaceArray/> |
| `VecPointwiseDivide` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecPointwiseDivide/> |
| `VecPointwiseMax` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecPointwiseMax/> |
| `VecPointwiseMaxAbs` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecPointwiseMaxAbs/> |
| `VecPointwiseMin` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecPointwiseMin/> |
| `VecPointwiseMult` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecPointwiseMult/> |
| `VecPointwiseSign` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecPointwiseSign/> |
| `VecPow` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecPow/> |
| `VecRealPart` | Collective | <https://petsc.org/release/manualpages/Vec/VecRealPart/> |
| `VecReciprocal` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecReciprocal/> |
| `VecRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecRegister/> |
| `VecRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecRegisterAll/> |
| `VecReplaceArray` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecReplaceArray/> |
| `VecResetArray` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecResetArray/> |
| `VecRestoreArray` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray/> |
| `VecRestoreArray1d` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray1d/> |
| `VecRestoreArray1dRead` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray1dRead/> |
| `VecRestoreArray1dWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray1dWrite/> |
| `VecRestoreArray2d` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray2d/> |
| `VecRestoreArray2dRead` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray2dRead/> |
| `VecRestoreArray2dWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray2dWrite/> |
| `VecRestoreArray3d` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray3d/> |
| `VecRestoreArray3dRead` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray3dRead/> |
| `VecRestoreArray3dWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray3dWrite/> |
| `VecRestoreArray4d` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray4d/> |
| `VecRestoreArray4dRead` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray4dRead/> |
| `VecRestoreArray4dWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArray4dWrite/> |
| `VecRestoreArrayAndMemType` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecRestoreArrayAndMemType/> |
| `VecRestoreArrayPair` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecRestoreArrayPair/> |
| `VecRestoreArrayRead` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArrayRead/> |
| `VecRestoreArrayReadAndMemType` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecRestoreArrayReadAndMemType/> |
| `VecRestoreArrays` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecRestoreArrays/> |
| `VecRestoreArrayWrite` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreArrayWrite/> |
| `VecRestoreArrayWriteAndMemType` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecRestoreArrayWriteAndMemType/> |
| `VecRestoreLocalVector` | Logically Collective. | <https://petsc.org/release/manualpages/Vec/VecRestoreLocalVector/> |
| `VecRestoreLocalVectorRead` | Not Collective. | <https://petsc.org/release/manualpages/Vec/VecRestoreLocalVectorRead/> |
| `VecRestoreSubVector` | Collective | <https://petsc.org/release/manualpages/Vec/VecRestoreSubVector/> |
| `VecScale` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecScale/> |
| `VecScatterBegin` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Vec/VecScatterBegin/> |
| `VecScatterCopy` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterCopy/> |
| `VecScatterCreate` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterCreate/> |
| `VecScatterCreateToAll` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterCreateToAll/> |
| `VecScatterCreateToZero` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterCreateToZero/> |
| `VecScatterDestroy` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterDestroy/> |
| `VecScatterEnd` | Neighbor-wise Collective | <https://petsc.org/release/manualpages/Vec/VecScatterEnd/> |
| `VecScatterGetMerged` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecScatterGetMerged/> |
| `VecScatterGetType` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecScatterGetType/> |
| `VecScatterRegister` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecScatterRegister/> |
| `VecScatterRemap` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterRemap/> |
| `VecScatterSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterSetFromOptions/> |
| `VecScatterSetType` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterSetType/> |
| `VecScatterSetUp` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterSetUp/> |
| `VecScatterView` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterView/> |
| `VecScatterViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Vec/VecScatterViewFromOptions/> |
| `VecsCreateSeq` | Collective | <https://petsc.org/release/manualpages/Vec/VecsCreateSeq/> |
| `VecsCreateSeqWithArray` | Collective | <https://petsc.org/release/manualpages/Vec/VecsCreateSeqWithArray/> |
| `VecsDestroy` | Collective | <https://petsc.org/release/manualpages/Vec/VecsDestroy/> |
| `VecsDuplicate` | Collective | <https://petsc.org/release/manualpages/Vec/VecsDuplicate/> |
| `VecSet` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecSet/> |
| `VecSetBlockSize` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecSetBlockSize/> |
| `VecSetErrorIfLocked` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecSetErrorIfLocked/> |
| `VecSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetFromOptions/> |
| `VecSetInf` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetInf/> |
| `VecSetLayout` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetLayout/> |
| `VecSetLocalToGlobalMapping` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecSetLocalToGlobalMapping/> |
| `VecSetOperation` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecSetOperation/> |
| `VecSetOption` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetOption/> |
| `VecSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecSetOptionsPrefix/> |
| `VecSetPinnedMemoryMin` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecSetPinnedMemoryMin/> |
| `VecSetPreallocationCOO` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetPreallocationCOO/> |
| `VecSetPreallocationCOOLocal` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetPreallocationCOOLocal/> |
| `VecSetRandom` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecSetRandom/> |
| `VecSetRandomGaussian` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetRandomGaussian/> |
| `VecSetSizes` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetSizes/> |
| `VecSetType` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetType/> |
| `VecSetUp` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetUp/> |
| `VecSetValue` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetValue/> |
| `VecSetValueLocal` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetValueLocal/> |
| `VecSetValues` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetValues/> |
| `VecSetValuesBlocked` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetValuesBlocked/> |
| `VecSetValuesBlockedLocal` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetValuesBlockedLocal/> |
| `VecSetValuesCOO` | Collective | <https://petsc.org/release/manualpages/Vec/VecSetValuesCOO/> |
| `VecSetValuesLocal` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetValuesLocal/> |
| `VecSetValuesSection` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSetValuesSection/> |
| `VecShift` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecShift/> |
| `VecSqrtAbs` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecSqrtAbs/> |
| `VecStashGetInfo` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecStashGetInfo/> |
| `VecStashSetInitialSize` | Not Collective, different processes can have different size stashes | <https://petsc.org/release/manualpages/Vec/VecStashSetInitialSize/> |
| `VecStashView` | Collective | <https://petsc.org/release/manualpages/Vec/VecStashView/> |
| `VecStashViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Vec/VecStashViewFromOptions/> |
| `VecStepBoundInfo` | Collective | <https://petsc.org/release/manualpages/Vec/VecStepBoundInfo/> |
| `VecStepMax` | Collective | <https://petsc.org/release/manualpages/Vec/VecStepMax/> |
| `VecStepMaxBounded` | Collective | <https://petsc.org/release/manualpages/Vec/VecStepMaxBounded/> |
| `VecStrideGather` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideGather/> |
| `VecStrideGatherAll` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideGatherAll/> |
| `VecStrideMax` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideMax/> |
| `VecStrideMaxAll` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideMaxAll/> |
| `VecStrideMin` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideMin/> |
| `VecStrideMinAll` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideMinAll/> |
| `VecStrideNorm` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideNorm/> |
| `VecStrideNormAll` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideNormAll/> |
| `VecStrideScale` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecStrideScale/> |
| `VecStrideScaleAll` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecStrideScaleAll/> |
| `VecStrideScatter` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideScatter/> |
| `VecStrideScatterAll` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideScatterAll/> |
| `VecStrideSet` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecStrideSet/> |
| `VecStrideSubSetGather` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideSubSetGather/> |
| `VecStrideSubSetScatter` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideSubSetScatter/> |
| `VecStrideSum` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideSum/> |
| `VecStrideSumAll` | Collective | <https://petsc.org/release/manualpages/Vec/VecStrideSumAll/> |
| `VecSum` | Collective | <https://petsc.org/release/manualpages/Vec/VecSum/> |
| `VecSwap` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecSwap/> |
| `VecTaggerAbsoluteGetBox` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerAbsoluteGetBox/> |
| `VecTaggerAbsoluteSetBox` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerAbsoluteSetBox/> |
| `VecTaggerAndGetSubs` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerAndGetSubs/> |
| `VecTaggerAndSetSubs` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerAndSetSubs/> |
| `VecTaggerCDFGetBox` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerCDFGetBox/> |
| `VecTaggerCDFGetMethod` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerCDFGetMethod/> |
| `VecTaggerCDFIterativeGetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerCDFIterativeGetTolerances/> |
| `VecTaggerCDFIterativeSetTolerances` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerCDFIterativeSetTolerances/> |
| `VecTaggerCDFSetBox` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerCDFSetBox/> |
| `VecTaggerCDFSetMethod` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerCDFSetMethod/> |
| `VecTaggerComputeBoxes` | Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerComputeBoxes/> |
| `VecTaggerComputeIS` | Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerComputeIS/> |
| `VecTaggerCreate` | Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerCreate/> |
| `VecTaggerDestroy` | Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerDestroy/> |
| `VecTaggerFinalizePackage` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerFinalizePackage/> |
| `VecTaggerGetBlockSize` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerGetBlockSize/> |
| `VecTaggerGetInvert` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerGetInvert/> |
| `VecTaggerGetType` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerGetType/> |
| `VecTaggerInitializePackage` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerInitializePackage/> |
| `VecTaggerOrGetSubs` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerOrGetSubs/> |
| `VecTaggerOrSetSubs` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerOrSetSubs/> |
| `VecTaggerRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Vec/VecTaggerRegister/> |
| `VecTaggerRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerRegisterAll/> |
| `VecTaggerRelativeGetBox` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerRelativeGetBox/> |
| `VecTaggerRelativeSetBox` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerRelativeSetBox/> |
| `VecTaggerSetBlockSize` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerSetBlockSize/> |
| `VecTaggerSetFromOptions` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerSetFromOptions/> |
| `VecTaggerSetInvert` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerSetInvert/> |
| `VecTaggerSetType` | Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerSetType/> |
| `VecTaggerSetUp` | Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerSetUp/> |
| `VecTaggerView` | Collective | <https://petsc.org/release/manualpages/Vec/VecTaggerView/> |
| `VecTDot` | Collective | <https://petsc.org/release/manualpages/Vec/VecTDot/> |
| `VecUniqueEntries` | Collective | <https://petsc.org/release/manualpages/Vec/VecUniqueEntries/> |
| `VecViennaCLPlaceArray` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecViennaCLPlaceArray/> |
| `VecViennaCLResetArray` | Not Collective | <https://petsc.org/release/manualpages/Vec/VecViennaCLResetArray/> |
| `VecView` | Collective | <https://petsc.org/release/manualpages/Vec/VecView/> |
| `VecViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Vec/VecViewFromOptions/> |
| `VecViewNative` | Collective | <https://petsc.org/release/manualpages/Vec/VecViewNative/> |
| `VecWAXPY` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecWAXPY/> |
| `VecWhichBetween` | Collective | <https://petsc.org/release/manualpages/Vec/VecWhichBetween/> |
| `VecWhichBetweenOrEqual` | Collective | <https://petsc.org/release/manualpages/Vec/VecWhichBetweenOrEqual/> |
| `VecWhichEqual` | Collective | <https://petsc.org/release/manualpages/Vec/VecWhichEqual/> |
| `VecWhichGreaterThan` | Collective | <https://petsc.org/release/manualpages/Vec/VecWhichGreaterThan/> |
| `VecWhichInactive` | Collective | <https://petsc.org/release/manualpages/Vec/VecWhichInactive/> |
| `VecWhichLessThan` | Collective | <https://petsc.org/release/manualpages/Vec/VecWhichLessThan/> |
| `VecZeroEntries` | Logically Collective | <https://petsc.org/release/manualpages/Vec/VecZeroEntries/> |

## Viewer

| Symbol | Collectivity | Official manual page |
|---|---|---|
| `PETSC_VIEWER_BINARY_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_BINARY_/> |
| `PETSC_VIEWER_DRAW_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_DRAW_/> |
| `PETSC_VIEWER_GLVIS_` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_GLVIS_/> |
| `PETSC_VIEWER_HDF5_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_HDF5_/> |
| `PETSC_VIEWER_MATLAB_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_MATLAB_/> |
| `PETSC_VIEWER_PYTHON_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_PYTHON_/> |
| `PETSC_VIEWER_PYVISTA_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_PYVISTA_/> |
| `PETSC_VIEWER_SAWS_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_SAWS_/> |
| `PETSC_VIEWER_SOCKET_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_SOCKET_/> |
| `PETSC_VIEWER_STDERR_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_STDERR_/> |
| `PETSC_VIEWER_STDOUT_` | Collective | <https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_STDOUT_/> |
| `PetscBTView` | Collective on viewer ; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscBTView/> |
| `PetscDataTypeToHDF5DataType` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscDataTypeToHDF5DataType/> |
| `PetscHDF5DataTypeToPetscDataType` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscHDF5DataTypeToPetscDataType/> |
| `PetscHDF5IntCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscHDF5IntCast/> |
| `PetscMonitorCompare` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscMonitorCompare/> |
| `PetscObjectViewSAWs` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscObjectViewSAWs/> |
| `PetscOptionsCreateViewer` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscOptionsCreateViewer/> |
| `PetscOptionsCreateViewers` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscOptionsCreateViewers/> |
| `PetscOptionsGetCreateViewerOff` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscOptionsGetCreateViewerOff/> |
| `PetscOptionsHelpPrintedCheck` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscOptionsHelpPrintedCheck/> |
| `PetscOptionsHelpPrintedDestroy` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscOptionsHelpPrintedDestroy/> |
| `PetscOptionsPopCreateViewerOff` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscOptionsPopCreateViewerOff/> |
| `PetscOptionsPushCreateViewerOff` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscOptionsPushCreateViewerOff/> |
| `PetscOptionsViewer` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscOptionsViewer/> |
| `PetscViewerADIOSOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerADIOSOpen/> |
| `PetscViewerAndFormatCreate` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerAndFormatCreate/> |
| `PetscViewerAndFormatDestroy` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerAndFormatDestroy/> |
| `PetscViewerAppendOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerAppendOptionsPrefix/> |
| `PetscViewerASCIIAddTab` | Not Collective, but only first processor in set has any effect; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIAddTab/> |
| `PetscViewerASCIIGetPointer` | Not Collective, depending on the viewer the value may be meaningless except for process 0 of the viewer; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIGetPointer/> |
| `PetscViewerASCIIGetStderr` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIGetStderr/> |
| `PetscViewerASCIIGetStdout` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIGetStdout/> |
| `PetscViewerASCIIGetTab` | Not Collective, meaningful on first processor only; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIGetTab/> |
| `PetscViewerASCIIOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIOpen/> |
| `PetscViewerASCIIOpenWithFILE` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIOpenWithFILE/> |
| `PetscViewerASCIIPopSynchronized` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPopSynchronized/> |
| `PetscViewerASCIIPopTab` | Not Collective, but only first MPI rank in the viewer has any effect; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPopTab/> |
| `PetscViewerASCIIPrintf` | Not Collective, but only the first MPI rank in the viewer has any effect | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPrintf/> |
| `PetscViewerASCIIPushSynchronized` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPushSynchronized/> |
| `PetscViewerASCIIPushTab` | Not Collective, but only first MPI rank in the viewer has any effect; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPushTab/> |
| `PetscViewerASCIISetFILE` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISetFILE/> |
| `PetscViewerASCIISetTab` | Not Collective, but only first processor in set has any effect; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISetTab/> |
| `PetscViewerASCIISubtractTab` | Not Collective, but only first processor in set has any effect; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISubtractTab/> |
| `PetscViewerASCIISynchronizedPrintf` | Not Collective, must call collective PetscViewerFlush () to get the results flushed | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISynchronizedPrintf/> |
| `PetscViewerASCIIUseTabs` | Not Collective, but only first MPI rank in the viewer has any effect; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIUseTabs/> |
| `PetscViewerBinaryAddMPIIOOffset` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryAddMPIIOOffset/> |
| `PetscViewerBinaryGetDescriptor` | Collective because it may trigger a PetscViewerSetUp () call; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetDescriptor/> |
| `PetscViewerBinaryGetFlowControl` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetFlowControl/> |
| `PetscViewerBinaryGetInfoPointer` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetInfoPointer/> |
| `PetscViewerBinaryGetMPIIODescriptor` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetMPIIODescriptor/> |
| `PetscViewerBinaryGetMPIIOOffset` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetMPIIOOffset/> |
| `PetscViewerBinaryGetSkipHeader` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetSkipHeader/> |
| `PetscViewerBinaryGetSkipInfo` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetSkipInfo/> |
| `PetscViewerBinaryGetSkipOptions` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetSkipOptions/> |
| `PetscViewerBinaryGetUseMPIIO` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetUseMPIIO/> |
| `PetscViewerBinaryOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryOpen/> |
| `PetscViewerBinaryRead` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryRead/> |
| `PetscViewerBinaryReadAll` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryReadAll/> |
| `PetscViewerBinaryReadStringArray` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryReadStringArray/> |
| `PetscViewerBinarySetFlowControl` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetFlowControl/> |
| `PetscViewerBinarySetSkipHeader` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetSkipHeader/> |
| `PetscViewerBinarySetSkipInfo` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetSkipInfo/> |
| `PetscViewerBinarySetSkipOptions` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetSkipOptions/> |
| `PetscViewerBinarySetUseMPIIO` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetUseMPIIO/> |
| `PetscViewerBinarySkipInfo` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySkipInfo/> |
| `PetscViewerBinaryWrite` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryWrite/> |
| `PetscViewerBinaryWriteAll` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryWriteAll/> |
| `PetscViewerBinaryWriteStringArray` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryWriteStringArray/> |
| `PetscViewerCGNSGetSolutionIndex` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSGetSolutionIndex/> |
| `PetscViewerCGNSGetSolutionIteration` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSGetSolutionIteration/> |
| `PetscViewerCGNSGetSolutionName` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSGetSolutionName/> |
| `PetscViewerCGNSGetSolutionTime` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSGetSolutionTime/> |
| `PetscViewerCGNSOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSOpen/> |
| `PetscViewerCGNSSetSolutionIndex` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSSetSolutionIndex/> |
| `PetscViewerCheckReadable` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCheckReadable/> |
| `PetscViewerCheckWritable` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCheckWritable/> |
| `PetscViewerCreate` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerCreate/> |
| `PetscViewerDestroy` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDestroy/> |
| `PetscViewerDrawBaseAdd` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawBaseAdd/> |
| `PetscViewerDrawBaseSet` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawBaseSet/> |
| `PetscViewerDrawClear` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawClear/> |
| `PetscViewerDrawGetBounds` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawGetBounds/> |
| `PetscViewerDrawGetHold` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawGetHold/> |
| `PetscViewerDrawGetPause` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawGetPause/> |
| `PetscViewerDrawGetTitle` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawGetTitle/> |
| `PetscViewerDrawOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawOpen/> |
| `PetscViewerDrawResize` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawResize/> |
| `PetscViewerDrawSetBounds` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetBounds/> |
| `PetscViewerDrawSetHold` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetHold/> |
| `PetscViewerDrawSetInfo` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetInfo/> |
| `PetscViewerDrawSetPause` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetPause/> |
| `PetscViewerDrawSetTitle` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetTitle/> |
| `PetscViewerFileGetMode` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFileGetMode/> |
| `PetscViewerFileGetName` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFileGetName/> |
| `PetscViewerFileSetMode` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFileSetMode/> |
| `PetscViewerFileSetName` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFileSetName/> |
| `PetscViewerFlowControlEndMain` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlEndMain/> |
| `PetscViewerFlowControlEndWorker` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlEndWorker/> |
| `PetscViewerFlowControlStart` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlStart/> |
| `PetscViewerFlowControlStepMain` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlStepMain/> |
| `PetscViewerFlowControlStepWorker` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlStepWorker/> |
| `PetscViewerFlush` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerFlush/> |
| `PetscViewerGetFormat` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerGetFormat/> |
| `PetscViewerGetOptionsPrefix` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerGetOptionsPrefix/> |
| `PetscViewerGetSubViewer` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerGetSubViewer/> |
| `PetscViewerGetType` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerGetType/> |
| `PetscViewerGLVisOpen` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisOpen/> |
| `PetscViewerGLVisSetFields` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisSetFields/> |
| `PetscViewerGLVisSetPrecision` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisSetPrecision/> |
| `PetscViewerGLVisSetSnapId` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisSetSnapId/> |
| `PetscViewerHDF5GetBaseDimension2` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetBaseDimension2/> |
| `PetscViewerHDF5GetCollective` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetCollective/> |
| `PetscViewerHDF5GetCompress` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetCompress/> |
| `PetscViewerHDF5GetDefaultTimestepping` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetDefaultTimestepping/> |
| `PetscViewerHDF5GetFileId` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetFileId/> |
| `PetscViewerHDF5GetGroup` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetGroup/> |
| `PetscViewerHDF5GetSPOutput` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetSPOutput/> |
| `PetscViewerHDF5GetTimestep` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetTimestep/> |
| `PetscViewerHDF5HasAttribute` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasAttribute/> |
| `PetscViewerHDF5HasDataset` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasDataset/> |
| `PetscViewerHDF5HasGroup` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasGroup/> |
| `PetscViewerHDF5HasObject` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasObject/> |
| `PetscViewerHDF5HasObjectAttribute` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasObjectAttribute/> |
| `PetscViewerHDF5IncrementTimestep` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5IncrementTimestep/> |
| `PetscViewerHDF5IsTimestepping` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5IsTimestepping/> |
| `PetscViewerHDF5Load` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5Load/> |
| `PetscViewerHDF5Open` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5Open/> |
| `PetscViewerHDF5OpenGroup` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5OpenGroup/> |
| `PetscViewerHDF5PathIsRelative` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PathIsRelative/> |
| `PetscViewerHDF5PopGroup` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PopGroup/> |
| `PetscViewerHDF5PopTimestepping` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PopTimestepping/> |
| `PetscViewerHDF5PushGroup` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PushGroup/> |
| `PetscViewerHDF5PushTimestepping` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PushTimestepping/> |
| `PetscViewerHDF5ReadAttribute` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5ReadAttribute/> |
| `PetscViewerHDF5ReadObjectAttribute` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5ReadObjectAttribute/> |
| `PetscViewerHDF5SetBaseDimension2` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetBaseDimension2/> |
| `PetscViewerHDF5SetCollective` | Logically Collective; flg must contain common value | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetCollective/> |
| `PetscViewerHDF5SetCompress` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetCompress/> |
| `PetscViewerHDF5SetDefaultTimestepping` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetDefaultTimestepping/> |
| `PetscViewerHDF5SetSPOutput` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetSPOutput/> |
| `PetscViewerHDF5SetTimestep` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetTimestep/> |
| `PetscViewerHDF5WriteAttribute` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5WriteAttribute/> |
| `PetscViewerHDF5WriteGroup` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5WriteGroup/> |
| `PetscViewerHDF5WriteObjectAttribute` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5WriteObjectAttribute/> |
| `PetscViewerMathematicaOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaOpen/> |
| `PetscViewerMathematicaPutCSRMatrix` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaPutCSRMatrix/> |
| `PetscViewerMathematicaPutMatrix` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaPutMatrix/> |
| `PetscViewerMatlabGetArray` | Not Collective; only processor zero reads in the array | <https://petsc.org/release/manualpages/Viewer/PetscViewerMatlabGetArray/> |
| `PetscViewerMatlabOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerMatlabOpen/> |
| `PetscViewerMatlabPutArray` | Not Collective, only processor zero saves array | <https://petsc.org/release/manualpages/Viewer/PetscViewerMatlabPutArray/> |
| `PetscViewerMatlabPutVariable` | Not Collective; only processor zero writes the variable | <https://petsc.org/release/manualpages/Viewer/PetscViewerMatlabPutVariable/> |
| `PetscViewerMonitorLGSetUp` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerMonitorLGSetUp/> |
| `PetscViewerPopFormat` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerPopFormat/> |
| `PetscViewerPushFormat` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerPushFormat/> |
| `PetscViewerPythonCreate` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerPythonCreate/> |
| `PetscViewerPythonGetType` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerPythonGetType/> |
| `PetscViewerPythonSetType` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerPythonSetType/> |
| `PetscViewerPythonViewObject` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerPythonViewObject/> |
| `PetscViewerRead` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerRead/> |
| `PetscViewerReadable` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerReadable/> |
| `PetscViewerRegister` | Not Collective, No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerRegister/> |
| `PetscViewerRegisterAll` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerRegisterAll/> |
| `PetscViewerRestoreSubViewer` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerRestoreSubViewer/> |
| `PetscViewerSAWsOpen` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerSAWsOpen/> |
| `PetscViewersCreate` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewersCreate/> |
| `PetscViewersDestroy` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewersDestroy/> |
| `PetscViewerSetFormat` | Logically Collective, No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerSetFormat/> |
| `PetscViewerSetFromOptions` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerSetFromOptions/> |
| `PetscViewerSetOptionsPrefix` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerSetOptionsPrefix/> |
| `PetscViewerSetType` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerSetType/> |
| `PetscViewerSetUp` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerSetUp/> |
| `PetscViewersGetViewer` | Collective if the viewer has not previously be obtained. | <https://petsc.org/release/manualpages/Viewer/PetscViewersGetViewer/> |
| `PetscViewerSocketOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerSocketOpen/> |
| `PetscViewerSocketSetConnection` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerSocketSetConnection/> |
| `PetscViewerStringGetStringRead` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerStringGetStringRead/> |
| `PetscViewerStringOpen` | Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerStringOpen/> |
| `PetscViewerStringSetOwnString` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerStringSetOwnString/> |
| `PetscViewerStringSetString` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerStringSetString/> |
| `PetscViewerStringSPrintf` | Logically Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscViewerStringSPrintf/> |
| `PetscViewerView` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerView/> |
| `PetscViewerViewFromOptions` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerViewFromOptions/> |
| `PetscViewerVTKAddField` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVTKAddField/> |
| `PetscViewerVTKFWrite` | Logically Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVTKFWrite/> |
| `PetscViewerVTKGetDM` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVTKGetDM/> |
| `PetscViewerVTKOpen` | Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVTKOpen/> |
| `PetscViewerVUFlushDeferred` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVUFlushDeferred/> |
| `PetscViewerVUGetPointer` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVUGetPointer/> |
| `PetscViewerVUGetVecSeen` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVUGetVecSeen/> |
| `PetscViewerVUPrintDeferred` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVUPrintDeferred/> |
| `PetscViewerVUSetMode` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVUSetMode/> |
| `PetscViewerVUSetVecSeen` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerVUSetVecSeen/> |
| `PetscViewerWritable` | Not Collective | <https://petsc.org/release/manualpages/Viewer/PetscViewerWritable/> |
| `PetscVTKIntCast` | Not Collective; No Fortran Support | <https://petsc.org/release/manualpages/Viewer/PetscVTKIntCast/> |
