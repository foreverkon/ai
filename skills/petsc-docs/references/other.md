# Additional PETSc topics

## About This Manual#

**URL:** https://petsc.org/release/manual/about_this_manual/

**Contents:**
- About This Manual#

This manual describes the use of the Portable, Extensible Toolkit for Scientific Computation (PETSc) and the Toolkit for Advanced Optimization (TAO) for the numerical solution of partial differential equations (PDEs) and related problems on high-performance computers. PETSc/TAO is a suite of data structures and routines that provide the building blocks for implementing large-scale application codes on parallel (and serial) computers. PETSc uses the MPI standard for all distributed memory communication.

PETSc/TAO includes a large suite of parallel linear solvers, nonlinear solvers, time integrators, and optimizers that may be used in application codes written in Fortran, C, C++, and Python (via petsc4py; see Getting Started ). The library is organized hierarchically, enabling users to employ the abstraction level most appropriate for a particular problem. By using techniques of object-oriented programming, PETSc provides enormous flexibility for users.

PETSc is a sophisticated set of software tools; it initially has a steeper learning curve than packages such as MATLAB or a simple subroutine library. In particular, for individuals without some experience programming in C, C++, Python, or Fortran and experience using a debugger such as gdb or lldb, it may require a significant amount of time to take full advantage of the features that enable efficient software use. However, the power of the PETSc design and the algorithms it incorporates makes the efficient implementation of many application codes simpler than “rolling them” yourself.

For many tasks, a package such as MATLAB is often the best tool; PETSc is not intended for the classes of problems for which effective MATLAB code can be written.

built on PETSc, may satisfy your needs without requiring directly using PETSc. We recommend reviewing these packages’ functionality before starting to code directly with PETSc.

PETSc can be used to provide a “MPI parallel linear solver” in an otherwise sequential or OpenMP parallel code. This approach can provide modest improvements in the application time by utilizing modest numbers of MPI processes. See PCMPI for details on how to utilize the PETSc MPI linear solver server.

Since PETSc is under continued development, small changes in usage and calling sequences of routines will occur. PETSc has been supported for twenty-five years; see mailing list information on our website for information on contacting support.

Introduction to PETSc

---

## C/Fortran API#

**URL:** https://petsc.org/release/manualpages/

**Contents:**
- C/Fortran API#

The manual pages are split into four categories; we recommend beginning with basic functionality and then gradually exploring more sophisticated library features. See PETSc for Fortran Users for API differences.

Beginner - Basic usage

Intermediate - Setting options for algorithms and data structures

Advanced - Setting more advanced options and customization

Developer - Interfaces intended primarily for library developers

Vectors and Index Sets

---

## PetscDA: Data Assimilation#

**URL:** https://petsc.org/release/manual/da/

**Contents:**
- PetscDA: Data Assimilation#
- Ensemble-based Data Assimilation#
- Lifecycle overview#
- Creating a PetscDA context#
- Degrees of freedom per grid point#
- Managing ensembles#
- Observation error#
- Analysis step#
- Forecast step#
- Inflation#

PETSc’s PetscDA object coordinates data assimilation (DA) workflows.

This is new code, please independently verify all results you obtain using it.

Some planned work for PetscDA is available as GitLab Issue #1882

Currently PetscDA only supports ensemble-based data assimilation with two PetscDAType: PETSCDAETKF and PETSCDALETKF. These focus on ensemble transform Kalman filter (ETKF)-style updates but are extensible to other assimilation techniques.

These centralize ensemble storage, observational metadata, and user-defined forecast/analysis operators so that algorithms can run independently of the MPI layout or the vector/matrix backends.

A typical assimilation cycle alternates between forecast propagation and statistical analysis:

Initialize a PetscDA context and configure ensemble sizes and data structures.

Populate the ensemble state vectors and optional observation-error descriptions.

Advance each ensemble member with a model operator supplied by the application.

Combine forecasts with observations through PetscDAEnsembleAnalysis() to produce the posterior ensemble.

Repeat until the desired simulation horizon is complete, optionally extracting diagnostics after each phase.

Throughout this loop the PetscDA object abstracts the global vectors, scatters, and reductions needed to compute ensemble means, anomalies, and square-root transforms.

Here we introduce a simple example to demonstrate PetscDA usage with the PETSCDALETKF on the Lorenz-96 model. Please read Implementations for more in-depth discussion of the available implementations.

Listing: src/ml/da/tutorials/ex1.c

Create, configure, and destroy a PetscDA object with the standard PETSc object lifecycle:

To create a PetscDA instance, call PetscDACreate():

To choose an implementation type, call

or use the command-line option -petscda_type <name>; details regarding the available implementations are presented in Implementations.

PetscDASetSizes() records the global state dimension and the number of observations:

For MPI-parallel runs where the state or observation vectors are distributed, the local partition sizes can be set explicitly with

Pass PETSC_DECIDE for either argument to let PETSc choose the partition automatically.

PetscDAEnsembleSetSize() records the number of ensemble members requested:

After having set these options, call PetscDASetFromOptions() to apply any command-line overrides, then PetscDASetUp() to allocate internal storage:

Finally, after the user is done using the DA object, destroy it with

When the state vector is laid out on a structured grid, the number of physical degrees of freedom per grid point can be recorded with

This metadata is used by some implementations and viewers; the default is 1.

PetscDA stores ensemble members as PETSc Vec objects and exposes convenience helpers to access them safely.

Individual ensemble members can be read or overwritten using a get/restore ownership pattern analogous to MatDenseGetColumnVec:

PetscDAEnsembleGetMember() / PetscDAEnsembleRestoreMember() map ensemble indices to Vec handles that participate in PETSc’s reference counting. PetscDAEnsembleSetMember() lets applications inject externally created vectors into specific slots, which is useful when importing state snapshots from disk or another solver component.

Ensemble statistics are computed with:

PetscDAEnsembleComputeAnomalies() returns a dense Mat whose columns are the mean-subtracted ensemble anomalies. Many square-root filters use this matrix to construct low-rank covariance factorizations. Pass NULL for mean to have the function compute it internally.

Observation-error variances (or more general descriptions) are supplied through PetscDASetObsErrorVariance(). The associated vector is assumed to follow the global observation ordering; PetscDAGetObsErrorVariance() returns the stored object for later inspection or reuse.

PetscDAEnsembleAnalysis() performs the assimilation step given an observation vector and a linear observation operator matrix:

H is a Mat (typically sparse AIJ) that maps the N-dimensional state vector to the P-dimensional observation space: y ≈ H*x. PetscDAAnalysis() handles all ensemble reductions, gain computations, and posterior updates.

PetscDAEnsembleForecast() wraps the forecast step. The user supplies a function that advances a single ensemble member:

Calling sequence for model:

input - the vector to be evolved, forecasted, time-stepped, or otherwise advanced

output - the forecast, evolved, or time-stepped result

ctx - the context for the model function

ModelForecast can call PETSc time integrators (TS: Scalable ODE and DAE Solvers), nonlinear solvers (SNES: Nonlinear Solvers), or bespoke device kernels. The PetscDA layer orchestrates calls across the entire ensemble, issuing them in rank-local loops while ensuring that ownership and recycling semantics remain correct.

Covariance inflation counteracts ensemble collapse by artificially widening the prior spread before the analysis step. The inflation factor \(\rho \ge 1\) scales each anomaly so that the effective prior covariance becomes \(\rho^2 P^f\). Set and retrieve the factor with

or at runtime with -petscda_ensemble_inflation <value> (default: 1.0, i.e. no inflation).

The available PetscDA implementations are listed in Table PETSc Data Assimilation Methods. Custom types can be registered with PetscDARegister() and selected at runtime with -petscda_type <name>.

Ensemble Transform Kalman Filter

Local Ensemble Transform Kalman Filter

The built-in square-root ETKF (PETSCDAETKF, -petscda_type etkf) is the default implementation. It implements Algorithm 6.4 in [ABN16] using a deterministic square-root update that avoids stochastic perturbations.

The ETKF supports two factorization strategies for the reduced-space T-matrix:

PETSCDA_SQRT_CHOLESKY

O(n³/3); preferred when the reduced-space matrix is positive definite

More robust for semi-definite matrices; handles small negative eigenvalues from round-off

Select at runtime with -petscda_ensemble_sqrt_type {cholesky,eigen} (default: eigen).

The Local ETKF (PETSCDALETKF, -petscda_type letkf) performs the analysis update locally around each grid point, enabling scalable assimilation on large domains by avoiding the global ensemble covariance matrix. LETKF-specific configuration:

Set the observation count at runtime with -petscda_letkf_obs_per_vertex <n> (default: 9).

The PetscDA object obeys standard PETSc options parsing. Commonly used switches include:

-petscda_type <name> – select a registered PetscDA implementation (etkf, letkf).

-petscda_ensemble_inflation <value> – set the covariance inflation factor (default: 1.0).

-petscda_ensemble_sqrt_type {cholesky,eigen} – select the T-matrix square-root algorithm for ETKF (default: eigen).

-petscda_letkf_obs_per_vertex <n> – set the number of observations per grid vertex for LETKF (default: 9).

-petscda_view – inspect ensemble metadata and internal sizes.

Because PetscDA participates in the PETSc object registry, any prefix applied with PetscDASetOptionsPrefix() scopes these options.

PetscDAView() and PetscDAViewFromOptions() expose ensemble sizing, observation dimensions, and implementation-specific diagnostics . Views can be directed to ASCII, HDF5, or custom PetscViewer targets, enabling lightweight instrumentation of assimilation experiments. For advanced profiling, the PetscDA package registers with PETSc’s logging infrastructure via PetscDAInitializePackage()/PetscDAFinalizePackage(), so standard -log_view outputs will include assimilation breakdown.

TS: Scalable ODE and DAE Solvers discusses PETSc time integrators that can supply the forecast operator passed to PetscDAForecast().

Vectors and Parallel Data documents vector assembly and parallel data management for the state and observation spaces.

SNES: Nonlinear Solvers outlines nonlinear solvers that often participate in observation or model operators.

DM Basics provides background on distributed mesh infrastructure that can coexist with PetscDA-managed ensembles.

PetscRegressor: Regression Solvers

DM: Interfacing Between Solvers and Models/Discretizations

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
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAEnsembleAnalysis()
```

---

## PetscRegressor: Regression Solvers#

**URL:** https://petsc.org/release/manual/regressor/

**Contents:**
- PetscRegressor: Regression Solvers#
- Basic Regressor Usage#
- Regression Solvers#
- Linear regressor#

The PetscRegressor component provides some basic infrastructure and a general API for supervised machine learning tasks at a higher level of abstraction than a purely algebraic “solvers” view. Methods are currently available for

Note that by “regressor” we mean an algorithm or implementation used to fit and apply a regression model, following standard parlance in the machine-learning community. Regressor here does NOT mean an independent (or predictor) variable, as it often does in the statistics community.

PetscRegressor supports supervised learning tasks: Given a matrix of observed data \(X\) with size \(n_{samples}\) by \(n_{features}\), predict a vector of “target” values \(y\) (of size \(n_{samples}\)), where the \(i\)th entry of \(y\) corresponds to the observation (or “sample”) stored in the \(i\)th row of \(X\). Traditionally, when the target consists of continuous values this is called “regression”, and when it consists of discrete values (or “labels”), this task is called “classification”; we use PetscRegressor to support both of these cases.

Before a regressor can be used to make predictions, the model must be fitted using an initial set of training data. Once a fitted model has been obtained, it can be used to predict target values for new observations. Every PetscRegressor implementation provides a Fit() and a Predict() method to support this workflow. Fitting (or “training”) a model is a relatively computationally intensive task that generally involves solving an optimization problem (often using TAO solvers) to determine the model parameters, whereas making predictions (or performing “inference”) is generally much simpler.

Here, we introduce a simple example to demonstrate PetscRegressor usage. Please read Regression Solvers for more in-depth discussion. The code presented below solves an ordinary linear regression problem, with various options for regularization.

In the simplest usage of a regressor, the user provides a training (or “design”) matrix (Mat) and a target vector (Vec) against which to fit the model. Once the regressor is fitted, the user can then obtain a vector of predicted values for a set of new observations.

PETSc’s default method for solving regression problems is ordinary least squares, REGRESSOR_LINEAR_OLS, which is a sub-type of linear regressor, PETSCREGRESSORLINEAR. By “linear” we mean that the model \(f(x, \theta)\) is linear in its coefficients \(\theta\) but not necessarily linear in its features \(x\).

Note that data creation, option parsing, and cleaning stages are omitted here for clarity. The complete code is available in ex3.c.

Listing: src/ml/regressor/tests/ex3.c

To create a PetscRegressor instance, one must first call PetscRegressorCreate():

To choose a regressor type, the user can either call

or use the command-line option -regressor_type <method>; details regarding the available methods are presented in Regression Solvers. The application code can specify the options used by underlying linear, nonlinear, and optimization solver methods used in fitting the model by calling

which interfaces with the PETSc options database and enables convenient runtime selection of the type of regression algorithm and setting various various solver or problem parameters. This routine can also control all inner solver options in the KSP, and Tao modules, as discussed in KSP: Linear System Solvers, TAO: Optimization Solvers.

After having set these routines and options, the user can fit (or “train”) the regressor by calling

where X is training data, and y is target values. Finally, after fitting the regressor, the user can compute model predictions, that is, perform inference, for a data matrix of unlabeled observations using the fitted regressor:

Finally, after the user is done using the regressor, the user should destroy its PetscRegressor context with

One can see the list of regressor types in Table PETSc Regressor. Currently, we only support one type, PETSCREGRESSORLINEAR, although we plan to add several others in the near future.

If the particular method being employed is one that supports regularization, the user can set regularizer’s weight via

or with the option -regressor_regularizer_weight <weight>.

The PETSCREGRESSORLINEAR (-regressor_type linear) implementation constructs a linear model to reduce the sum of squared differences between the actual target values (“observations”) in the dataset and the target values estimated by the fitted model. By default, bound-constrained regularized Gauss-Newton TAOBRGN is used to solve the underlying optimization problem.

Currently, linear regressor has three types, which are described in Table Linear Regressor types.

PetscRegressorLinearType

REGRESSOR_LINEAR_LASSO

REGRESSOR_LINEAR_RIDGE

If one wishes, the user can (when appropriate) use KSP to solve the problem, instead of Tao, via

or with the option -regressor_linear_use_ksp <true,false>.

Calculation of the intercept (also known as the “bias” or “offset”) is performed separately from the rest of the model fitting process, because data sets are often already mean-centered and because it is generally undesirable to regularize the intercept term. By default, this step is omitted; if the user wishes to compute the intercept, this can be done by calling

or by specifying the option -regressor_linear_fit_intercept <true,false>.

For a fitted regression, one can obtain the intercept and a vector of the model coefficients from a linear regression model via

TAO: Optimization Solvers

PetscDA: Data Assimilation

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
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

## User-Guide#

**URL:** https://petsc.org/release/manual/

**Contents:**
- User-Guide#

Argonne National Laboratory

Mathematics and Computer Science Division

S. Balay 1, S. Abhyankar 1,2, M. F. Adams 3, S. Benson 1, J. Brown 1,10, P. Brune 1, K. Buschelman 1, E. M. Constantinescu 1, L. Dalcin 4, A. Dener 1, V. Eijkhout 6, J. Faibussowitsch 1,18, W. D. Gropp 1,18, V. Hapla 8, T. Isaac 1,14, P. Jolivet 12,22, D. Karpeev 1, D. Kaushik 1, M. G. Knepley 1,9, F. Kong 1,11, S. Kruger 15, D. A. May 7,21, L. Curfman McInnes 1, R. Tran Mills 1, L. Mitchell 13,20, T. Munson 1, J. E. Roman 16, K. Rupp 1,19, P. Sanan 1,8, J. Sarich 1, B. F. Smith 1,17, H. Suh 1, S. Zampini 4, H. Zhang 1,5, H. Zhang 1, and J. Zhang 1

1 Mathematics and Computer Science Division, Argonne National Laboratory

2 Electricity Infrastructure and Buildings Division, Pacific Northwest National Laboratory

3 Computational Research, Lawrence Berkeley National Laboratory

4 Extreme Computing Research Center, King Abdullah University of Science and Technology

5 Department of Computer Science, Illinois Institute of Technology

6 Texas Advanced Computing Center, University of Texas at Austin

7 Department of Earth Sciences, University of Oxford

8 Institute of Geophysics, ETH Zurich

9 Department of Computer Science and Engineering, University at Buffalo

10 Department of Computer Science, University of Colorado, Boulder

11 Computational Frameworks, Idaho National Laboratory

12 Sorbonne Université, CNRS, LIP6

13 NVIDIA Corporation

14 College of Computing, Georgia Tech

15 Tech-X Corporation

16 DSIC, Universitat Politècnica de València

17 Flatiron Institute, Simons Foundation

18 University of Illinois, Urbana-Champaign

19 Institute for Microelectronics, TU Wien

20 Department of Computer Science, Durham University

21 Scripps Institution of Oceanography, University of California, San Diego

22 Toulouse INP, CNRS, Institute of Computer Science Research

This work was supported by the Office of Advanced Scientific Computing Research, Office of Science, U.S. Department of Energy, under Contract DE-AC02-06CH11357.

Summary of Unstructured Mesh Transformations

Introduction to PETSc

---
