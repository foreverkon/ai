# Petsc-Docs-Full-Raw - Overview Orientation

**Pages:** 12

---

## GPU Support Roadmap#

**URL:** https://petsc.org/release/overview/gpu_roadmap/

**Contents:**
- GPU Support Roadmap#

PETSc algebraic solvers run on GPU systems from NVIDIA using CUDA, and AMD and Intel using OpenCL/ViennaCL and HIP. Effective GPU implementations of low-level linear algebra operations provide a highly performant alternative solution strategy for users, and is therefore a high priority for PETSc developers.

See FAQ topic which shows how to enable GPU backends.

PETSc uses a single source programming model where solver back-ends are selected as runtime options and configuration options with no changes to the API.

Users should (ideally) never have to change their source code to take advantage of new backend implementations.

PETSc code will include full implementations of vector and matrix operations (as well as other select operations) using each of:

NVIDIA, AMD, Intel GPUs

Kokkos and Kokkos-Kernels

NVIDIA, AMD, Intel GPUs

Basic linear algebra GPU implementations enable many solvers, including GAMG and BDDC, to run entirely on the GPU. PETSc is currently adding GPU support for residual and Jacobian creation and for matrix assembly extensions to MATAIJCUSPARSE and MATAIJKOKKOS. This is work in progress.

We could use your help in further developing PETSc for GPUs; see PETSc Developers documentation. The label GPU is used on our GitLab repository for all activity involving GPUs.

You should use PETSc main (Git branch) for GPUs, do not install the current release.

Summary of Vector Types Available In PETSc

**Examples:**

Example 1 (unknown):
```unknown
MATAIJCUSPARSE
```

Example 2 (unknown):
```unknown
MATAIJKOKKOS
```

---

## Overview#

**URL:** https://petsc.org/release/overview/

**Contents:**
- Overview#

PETSc, the Portable, Extensible Toolkit for Scientific Computation, includes a large suite of scalable parallel linear and nonlinear equation solvers, ODE integrators, and optimization algorithms for application codes written in C, C++, Fortran, and Python. In addition, PETSc includes support for managing parallel PDE discretizations including parallel matrix and vector assembly routines. Toolkits/libraries that use PETSc.

---

## PETSc in a nutshell#

**URL:** https://petsc.org/release/overview/nutshell/

**Contents:**
- PETSc in a nutshell#
- Algebraic objects#
- Solvers#
- Model/Discretization Interfaces to Solvers#
- Utilities for Simulations/Solvers#

See Tutorials, by Mathematical Problem to immediately jump in and run PETSc code.

PETSc/TAO is a tool for writing, analyzing, and optimizing large-scale numerical simulations.

Vectors - containers for simulation solutions, right-hand sides of linear systems, etc (Vec).

Matrices - contain Jacobians and operators that define linear systems (Mat).

Multiple sparse and dense matrix storage formats,

Limited memory variable metric representations,

block and nested representations,

Easy, efficient matrix assembly and interface.

Indices - used to access portions of vectors and matrix, for example {1,2,4} or 1:10 (IS).

Linear solvers based on preconditioners (PC) and Krylov subspace methods (KSP).

Nonlinear solvers (SNES).

Time integrators, (ODE/PDE), explicit, implicit, IMEX, (TS)

Local and global error estimators

Performing sensitivity analysis with the TS ODE Solvers.

Optimization with equality and inequality constraints, first and second order (Newton) methods (Tao).

PetscRegressor for regression and classification problems (PetscRegressor).

Eigenvalue/Eigenvectors and related algorithms in the package SLEPc.

PETSc data assimilation for data assimilation problems (PetscDA). Currently provides support for ensemble-based approaches.

Simple structured grids, DMDA.

Staggered grids, DMSTAG: Staggered, Structured Grid, DMSTAG.

Unstructured grids, DMPlex: Unstructured Grids, DMPLEX.

Networks/graphs, for example the power grid, river networks, the nervous system, Networks, DMNETWORK.

Quad or octree grids, DMFOREST.

For full feature list see:

Nonlinear solvers table

ODE integrators table

Model/discretization interfaces to solvers table

control of the simulation via runtime options

visualization of the solvers and simulation via viewers,

monitoring of solution progress,

profiling of the performance,

robust error handling.

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

---

## Summary of Discretization Management Systems#

**URL:** https://petsc.org/release/overview/discrete_table/

**Contents:**
- Summary of Discretization Management Systems#

Staggered structured grids

Support for finite elements and volumes

Summary of Tao Solvers

Summary of Unstructured Mesh Transformations

**Examples:**

Example 1 (unknown):
```unknown
DMDACreate3d()
```

Example 2 (unknown):
```unknown
DMStagCreate3d()
```

Example 3 (unknown):
```unknown
DMForestSetBaseDM()
```

Example 4 (unknown):
```unknown
DMNetworkCreate()
```

---

## Summary of Matrix Types Available In PETSc#

**URL:** https://petsc.org/release/overview/matrix_table/

**Contents:**
- Summary of Matrix Types Available In PETSc#

Compressed sparse row

MatCreateMPIAIJSELL()

MatCreateMPIAIJPERM()

MatCreateAIJCUSPARSE()

NVIDIA cuSPARSE library

NVIDIA GPU acceleration

Multiple applications of single MATAIJ

Commonly used for identical interpolations on each component of a multi-component vector

Kronecker product of sparse matrix \(A\); \(I \otimes S + A \otimes T\)

SIMD and GPU acceleration

Block compressed sparse row

Upper triangular compressed sparse row

Elemental by Jack Poulson

NVIDIA GPU Acceleration

MatMult() via finite differencing of a function

MATMFFD, see Matrix-Free Methods

MatCreateMFFD(), see also MatCreateSNESMF()

Provides only matrix-vector products

User-provided operations

MATSHELL, see also Application Specific Custom Matrices

MATLMVM, MATLMVMDFP, MATLMVMBFGS, MATLMVMSR1, …

limited-memory BFGS style matrices

MatCreateHtoolFromKernel()

MatCreateH2OpusFromMat()

\(\mathcal H^2\) matrices

Transpose, \(A^T\), virtual

Hermitian Transpose, \(A^H\), virtual

MATHERMITIANTRANSPOSEVIRTUAL

MatCreateHermitianTranspose()

Normal, \(A^TA\), virtual

Hermitian Normal, \(A^HA\), virtual

MatCreateNormalHermitian()

MatCreateSchurComplement(), MatGetSchurComplement()

MatCreateSubMatrixVirtual()

Provides MatMult() and similar operations

For use in matrix assembly

\(I - \frac{1}{N}e e^T\), \(e=[1,\dots,1]^T\)

Summary of Vector Types Available In PETSc

Summary of Sparse Linear Solvers Available In PETSc

**Examples:**

Example 1 (unknown):
```unknown
MatCreateAIJ()
```

Example 2 (unknown):
```unknown
MatCreateMPIAIJMKL()
```

Example 3 (unknown):
```unknown
MatCreateMPIAIJSELL()
```

Example 4 (unknown):
```unknown
MatCreateMPIAIJPERM()
```

---

## Summary of Nonlinear Solvers Available In PETSc#

**URL:** https://petsc.org/release/overview/nonlinear_solve_table/

**Contents:**
- Summary of Nonlinear Solvers Available In PETSc#

See the paper Composing Scalable Nonlinear Algebraic Solvers for details on the algorithms.

Use -snes_mf for matrix-free linear solvers

Newton’s method with trust region

Newton with Arc Length Continuation

Essentially one step of Newtwon without a line search

Quasi-Newton method (BFGS)

Requires nearly symmetric Jacobian for good convergence

Nonlinear Gauss-Siedel

Full Approximation Scheme (nonlinear multigrid)

Nonlinear additive Schwarz

Nonlinear additive Schwarz preconditioned inexact Newton (ASPIN) methods

Composite (combine several nonlinear solvers)

Multi-stage smoothers

Preconditioned nonlinear solver

See SNESGetNPC()/ SNESSetNPC(), can be combined to accelerate many of the solvers

Summary of Sparse Linear Solvers Available In PETSc

Summary of Time Integrators Available In PETSc

**Examples:**

Example 1 (unknown):
```unknown
SNESNEWTONLS
```

Example 2 (unknown):
```unknown
SNESNEWTONTR
```

Example 3 (unknown):
```unknown
SNESNEWTONAL
```

Example 4 (unknown):
```unknown
SNESKSPONLY
```

---

## Summary of Sparse Linear Solvers Available In PETSc#

**URL:** https://petsc.org/release/overview/linear_solve_table/

**Contents:**
- Summary of Sparse Linear Solvers Available In PETSc#
- Preconditioners#
- Direct Solvers#
- Krylov Methods#

MATAIJ, MATBAIJ, MATSBAIJ, MATDENSE

MATAIJ, MATBAIJ, MATSBAIJ, MATKAIJ, MATMPISELL, MATIS

Variable Point Block Jacobi

MATAIJ, MATBAIJ, MATSBAIJ

MATAIJ, MATBAIJ, MATSBAIJ

MATAIJ, MATSEQDENSE, MATSEQSBAIJ

MATSEQBAIJ (only for bs = 2,3,4,5)

MATAIJ, MATBAIJ, MATSBAIJ

Vanka/overlapping patches

MATSEQAIJ, MATSEQBAIJ

ILU with drop tolerance

SuperLU Sequential ILU solver

Euclid/hypre (PCHYPRE)

MATSEQAIJ, MATSEQBAIJ, MATSEQSBAIJ

Algebraic recursive multilevel

Smoothed Aggregation (ML)

PCPFMG, PCSYSPFMG, PCSMG

BoomerAMG/hypre, AmgX

MATAIJ, MATBAIJ, MATSBAIJ, MATIS

Hierarchical matrices

Physics-based Splitting

Relaxation & Schur Complement

MATAIJ, MATBAIJ, MATNEST

Additive/multiplicative

Least Squares Commutator

Parallel transformation

Telescoping communicator

Parasails/hypre, SPAI

Balancing Neumann-Neumann

Balancing Domain Decomposition

2-level Schwarz wire basket

MATSEQAIJ, MATSEQBAIJ

MATAIJ, MATBAIJ, MATSEQSELL, MATDENSE, MATNEST

UMFPACK (SuiteSparse)

MATSEQAIJ, MATSEQBAIJ

MATMPIAIJ, MATMPIBAIJ

MATSEQAIJ, MATSEQSBAIJ

MATAIJ, MATSBAIJ, MATDENSE, MATNEST

MATSEQAIJ, MATSEQSBAIJ

CHOLMOD (SuiteSparse)

MATMPIAIJ, MATMPIBAIJ

Singular value decomposition

Two-stage with least squares residual minimization

Conjugate Gradient Squared

Conjugate Gradient for Least Squares

Conjugate Gradient on Normal Equations

Nash Conjugate Gradient with trust region constraint

Conjugate Gradient with trust region constraint

Gould et al Conjugate Gradient with trust region constraint

Steinhaug Conjugate Gradient with trust region constraint

Left Conjugate Direction

Bi-Conjugate Gradient

Stabilized Bi-Conjugate Gradient

Improved Stabilized Bi-Conjugate Gradient

Transpose-free variant of QMR developed by Tony Chan

Flexible Conjugate Gradients

Flexible stabilized Bi-Conjugate Gradients

Flexible stabilized Bi-Conjugate Gradients with fewer reductions

Stabilized Bi-Conjugate Gradients with length \(\ell\) recurrence

Generalized Conjugate Residual

Generalized Conjugate Residual (with inner normalization and deflated restarts)

FETI-DP (reduction to dual-primal sub-problem)

Gropp’s overlapped reduction pipelined Conjugate Gradient

Pipelined Conjugate Gradient

Pipelined Conjugate Gradient with residual replacement

Pipelined depth \(\ell\) Conjugate Gradient

Pipelined predict-and-recompute Conjugate Gradient

Pipelined Conjugate Gradient over iteration pairs

Pipelined flexible Conjugate Gradient

Pipelined stabilized Bi-Conjugate Gradients

Pipelined Conjugate Residual

Pipelined flexible GMRES

Pipelined Generalized Conjugate Residual

Summary of Matrix Types Available In PETSc

Summary of Nonlinear Solvers Available In PETSc

**Examples:**

Example 1 (unknown):
```unknown
MATSEQDENSE
```

Example 2 (unknown):
```unknown
MATSEQSBAIJ
```

Example 3 (unknown):
```unknown
PCDEFLATION
```

Example 4 (unknown):
```unknown
MATSEQSBAIJ
```

---

## Summary of Tao Solvers#

**URL:** https://petsc.org/release/overview/tao_solve_table/

**Contents:**
- Summary of Tao Solvers#
- Unconstrained#
- Bound Constrained#
- Complementarity#
- Nonlinear Least Squares#
- PDE-Constrained#
- Constrained#

Limited Memory Variable Metric (quasi-Newton)

Orthant-wise Limited Memory (quasi-Newton)

Bundle Method for Regularized Risk Minimization

Bounded Conjugate Gradient

Bounded Limited Memory Variable Metric (Quasi-Newton)

Bounded Quasi-Newton Line Search

Bounded Newton Line Search

Bounded Newton Trust-Region

Gradient Projection Conjugate Gradient

Bounded Quadratic Interior Point

Active-Set Feasible Line Search

Active-Set Infeasible Line Search

Semismooth Feasible Line Search

Semismooth Infeasible Line Searchx

Linearly Constrained Lagrangian

Interior Point Method

Barrier-Based Primal-Dual Interior Point

Summary of Time Integrators Available In PETSc

Summary of Discretization Management Systems

**Examples:**

Example 1 (unknown):
```unknown
TAOPOUNDERS
```

---

## Summary of Time Integrators Available In PETSc#

**URL:** https://petsc.org/release/overview/integrator_table/

**Contents:**
- Summary of Time Integrators Available In PETSc#

multistage SSP [Ket08]

Backward Differentiation Formulas

general linear [BJW07]

extrapolated IMEX [CS10]

diagonally implicit Runge-Kutta

See IMEX Runge-Kutta schemes

See Rosenbrock W-schemes

See GL schemes with global error estimation

explicit and implicit

Multirate Partitioned Runge-Kutta

Basic symplectic integrator for separable Hamiltonian

semi-implicit Euler and Velocity Verlet

fully implicit Runge-Kutta

J.C. Butcher, Z. Jackiewicz, and W.M. Wright. Error propagation of general linear methods for ordinary differential equations. Journal of Complexity, 23(4-6):560–580, 2007. doi:10.1016/j.jco.2007.01.009.

E.M. Constantinescu and A. Sandu. Extrapolated implicit-explicit time stepping. SIAM Journal on Scientific Computing, 31(6):4452–4477, 2010. doi:10.1137/080732833.

K.E. Jansen, C.H. Whiting, and G.M. Hulbert. A generalized-alpha method for integrating the filtered Navier–Stokes equations with a stabilized finite element method. Computer Methods in Applied Mechanics and Engineering, 190(3):305–319, 2000.

D.I. Ketcheson. Highly efficient strong stability-preserving Runge–Kutta methods with low-storage implementations. SIAM Journal on Scientific Computing, 30(4):2113–2136, 2008. doi:10.1137/07070485X.

Summary of Nonlinear Solvers Available In PETSc

Summary of Tao Solvers

---

## Summary of Unstructured Mesh Transformations#

**URL:** https://petsc.org/release/overview/plex_transform_table/

**Contents:**
- Summary of Unstructured Mesh Transformations#

Preserve a subset of the mesh marked by a DMLabel

Splits all k-cells into \(2^k\) pieces

Barycentric refinement for simplicies

Skeleton-based Refinement (SBR)

Simplicial refinement from Plaza and Carey

Optimized refinement for 1D meshes that preserves the canonical ordering

Simplex-to-Box transform

Replaces each simplex cell with \(2^d\) box cells

Box-to-Simplex transform

Replaces each box cell with simplex cells

Extrude n layers of cells from a surface

Boundary Layer Extrusion

refine_boundary_layer

Creates n layers of tensor cells along marked boundaries

Cohesive cell extrusion

Extrude a layer of cells into a mesh from an internal surface

Summary of Discretization Management Systems

**Examples:**

Example 1 (unknown):
```unknown
DMPlexTransformType
```

---

## Summary of Vector Types Available In PETSc#

**URL:** https://petsc.org/release/overview/vector_table/

**Contents:**
- Summary of Vector Types Available In PETSc#

Provides efficient access to inner vectors

Summary of Matrix Types Available In PETSc

**Examples:**

Example 1 (unknown):
```unknown
VECSTANDARD
```

---

## Supported Systems#

**URL:** https://petsc.org/release/overview/features/

**Contents:**
- Supported Systems#
- Accelerator/GPU Features#

Matrix/Vector CUDA support

Matrix/Vector OpenCL/ViennaCL support

Matrix/Vector HIP support

PETSc GPU support is under heavy development! See GPU support roadmap for more information on current support.

---
