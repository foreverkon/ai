# Petsc-Docs-Full-Raw - Tutorials Examples

**Pages:** 8

---

## Guide to the Stokes Equations using Finite Elements#

**URL:** https://petsc.org/release/tutorials/physics/guide_to_stokes/

**Contents:**
- Guide to the Stokes Equations using Finite Elements#
- Equation Definition#
- MMS Solutions#
- Dealing with Parameters#
- Investigating convergence#
  - Debugging#
  - Optimizing the Solver#
- Bibliography#

describe slow flow of an incompressible fluid with velocity \(u\), pressure \(p\), and body force \(f\).

This guide accompanies SNES Example 62> and SNES Example 69><\a>.

The Stokes equations for a fluid, a steady-state form of the Navier-Stokes equations, start with the balance of momentum, just as in elastostatics,

where \(\sigma\) is the stress tensor and \(f\) is the body force, combined with the conservation of mass

where \(\rho\) is the density and \(u\) is the fluid velocity. If we assume that the density is constant, making the fluid incompressible, and that the rheology is Newtonian, meaning that the viscous stress is linearly proportional to the local strain rate, then we have

where \(p\) is the pressure, \(\mu\) is the dynamic shear viscosity, with units \(N\cdot s/m^2\) or \(Pa\cdot s\). If we divide by the constant density, we would have the kinematic viscosity \(\nu\) and a force per unit mass. The second equation demands that the velocity field be divergence-free, indicating that the flow is incompressible. The pressure in this case can be thought of as the Lagrange multiplier enforcing the incompressibility constraint. In the compressible case, we would need an equation of state to relate the pressure to the density, and perhaps temperature.

We will discretize our Stokes equations with finite elements, so the first step is to write a variational weak form of the equations. We choose to use a Ritz-Galerkin setup, so let our velocity \(u \in V\) and pressure \(p \in Q\), so that

where integration by parts has added a boundary integral over the normal derivative of the stress (traction), and natural boundary conditions correspond to stress-free boundaries. We have multiplied the continuity equation by minus one in order to preserve symmetry.

The test functions \(v, q\) and their derivatives are determined by the discretization, whereas the form of the integrand is determined by the physics. Given a quadrature rule to evaluate the form integral, we would only need the evaluation of the physics integrand at the quadrature points, given the values of the fields and their derivatives. The entire scheme is detailed in [KnepleyBrownRuppSmith13]. The kernels paired with test functions we will call \(f_0\) and those paired with gradients of test functions will be called \(f_1\).

For example, the kernel for the continuity equation, paired with the pressure test function, is called f0_p and can be seen here

We use the components of the Jacobian of \(u\) to build up its divergence. For the balance of momentum excluding body force, we test against the gradient of the test function, as seen in f1_u,

Notice how the pressure \(p\) is referred to using u[uOff[1]] so that we can have many fields with different numbers of components. DMPlex uses these point functions to construct the residual. A similar set of point functions is also used to build the Jacobian. The last piece of our physics specification is the construction of exact solutions using the Method of Manufactured Solutions (MMS).

An MMS solution is chosen to elucidate some property of the problem, and to check that it is being solved accurately, since the error can be calculated explicitly. For our Stokes problem, we first choose a solution with quadratic velocity and linear pressure,

By plugging these solutions into our equations, assuming that the velocity we choose is divergence-free, we can determine the body force necessary to make them satisfy the Stokes equations. For the quadratic solution above, we find

which is implemented in our f0_quadratic_u pointwise function

We let PETSc know about these solutions

These solutions will be captured exactly by the \(P_2-P_1\) finite element space. We can use the -dmsnes_check option to activate function space checks. It gives the \(L_2\) error, or discretization error, of the exact solution, the residual computed using the interpolation of the exact solution into our finite element space, and uses a Taylor test to check that our Jacobian matches the residual. It should converge at order 2, or be exact in the case of linear equations like Stokes. Our \(P_2-P_1\) runs in the PETSc test section at the bottom of the source file

verify these claims, as we can see from the output files

We can carry out the same tests for the \(Q_2-Q_1\) element,

The quadratic solution, however, cannot tell us whether our discretization is attaining the correct order of convergence, especially for higher order elements. Thus, we will define another solution based on trigonometric functions.

We can now use -snes_convergence_estimate to determine the convergence exponent for the discretization. This options solves the problem on a series of refined meshes, calculates the error on each mesh, and determines the slope on a logarithmic scale. For example, we do this in two dimensions, refining our mesh twice using -convest_num_refine 2 in the following test.

However, the test needs an accurate linear solver. Sparse LU factorizations do not, in general, do full pivoting. Thus we must deal with the zero pressure block explicitly. We use the PCFIELDSPLIT preconditioner and the full Schur complement factorization, but we still need a preconditioner for the Schur complement \(B^T A^{-1} B\). We can have PETSc construct that matrix automatically, but the cost rises steeply as the problem size increases. Instead, we use the fact that the Schur complement is spectrally equivalent to the pressure mass matrix \(M_p\). We can make a matrix from which the preconditioner is constructed, which has the diagonal blocks we will use to build the preconditioners, letting PETSc know that we get the off-diagonal blocks from the original system with -pc_fieldsplit_off_diag_use_amat and to build the Schur complement from the original matrix using -pc_use_amat,

Putting this all together, and using exact solvers on the subblocks, we have

and we see it converges, however it is superconverging in the pressure,

If we refine the mesh using -dm_refine 3, the convergence rates become [3.0, 2.1].

Like most physical problems, the Stokes problem has a parameter, the dynamic shear viscosity, which determines what solution regime we are in. To handle these parameters in PETSc, we first define a C struct to hold them,

and then add a PetscBag object to our application context. We then setup the parameter object,

which will allow us to set the value from the command line using -mu. The PetscBag can also be persisted to disk with PetscBagLoad/View(). We can make these values available as constant to our pointwise functions through the PetscDS object.

In order to look at the convergence of some harder problems, we will examine SNES ex69. This example provides an exact solution to the variable viscosity Stokes equation. The sharp viscosity variation will allow us to investigate convergence of the solver and discretization. Briefly, a sharp viscosity variation is created across the unit square, imposed on a background pressure with given fundamental frequency. For example, we can create examples with period one half and viscosity \(e^{2 B x}\) (solKx)

which are show in the figure below.

Solution for \(m=2\), \(n=2\), \(B=1\)#

Solution for \(m=2\), \(n=2\), \(B=3.75\)#

If we can provide the PetscDS object in our problem with the exact solution function, PETSc has good support for debugging our discretization and solver. We can use the PetscConvEst object to check the convergence behavior of our element automatically. For example, if we use the -snes_convergence_estimate option, PETSc will solve our nonlinear equations on a series of refined meshes, use our exact solution to calculate the error, and then fit this line on a log-log scale to get the convergence rate,

If we initially refine the mesh twice, -dm_refine 2, we get

L_2 convergence rate: [3.0, 2.2]

which are the convergence rates we expect for the velocity and pressure using a \(P_2-P_1\) discretization. For \(Q_1-P_0\)

L_2 convergence rate: [2.0, 1.0]

This is a sensitive check that everything is working correctly. However, if this is wrong, where can I start? More fine-grained checks are available using the -dmsnes_check option. Using this for our \(P_2-P_1\) example (the p2p1 test), we have

The first line records the discretization error for our exact solution. This means that we project our solution function into the finite element space and then calculate the \(L_2\) norm of the difference between the exact solution and its projection. The norm is computed for each field separately. Next, PETSc calculates the residual using the projected exact solution as input. This should be small, and as the mesh is refined it should approach zero. Last, PETSc uses a Taylor test to try and determine how the error in the linear model scales as a function of the perturbation \(h\). Thus, in a nonlinear situation we would expect

Taylor approximation converging at order 2.0

In this case, since the viscosity does not depend on the velocity or pressure fields, we detect that the linear model is exact

Function appears to be linear

Suppose that we have made an error in the Jacobian. For instance, let us accidentally flip the sign of the pressure term in the momentum Jacobian.

When we run, we get a failure of the nonlinear solver. Our checking reveals that the Jacobian is wrong because it is converging at order 1 instead of 2, meaning the linear term is not correct in our model.

In order to track down the error, we can use -snes_test_jacobian which computes a finite difference approximation to the Jacobian and compares that to the analytic Jacobian. We ignore the first test, which occurs during our testing of the Jacobian, and look at the test that happens during the first Newton iterate. We see that the relative error in the Frobenius norm is about one percent, which indicates we have a real problem.

At this point, we could just go back and check the code. However, PETSc will also print out the differences between the analytic and approximate Jacobians. When we give the -snes_test_jacobian_view option, the code will print both Jacobians (which we omit) and then their difference, and will also do this for the matrix used to construct the preconditioner (which we omit). It is clear from the output that the \(u-p\) block of the Jacobian is wrong, and thus we know right where to look for our error. Moreover, if we look at the values in row 15, we see that the values just differ by a sign.

Can we see that the Schur complement of Q1-P0 is ill-conditioned?

In order to see exactly what solver we have employed, we can use the -snes_view option. When checking \(P_2-P_1\) convergence, we use an exact solver, but it must have several parts in order to deal with the saddle-point in the Jacobian. Using the test system to provide our extra option, we get

Going through this piece-by-piece, we can see all the parts of our solver. At the top level, we have a SNES using Newton’s method

For each nonlinear step, we use KSPGMRES to solve the Newton equation, preconditioned by PCFIELDSPLIT. We split the problem into two blocks, with the split determined by our DM, and combine those blocks using a Schur complement. The Schur complement is faithful since we use the FULL factorization type.

We form the preconditioner for the Schur complement from the (1,1) block of our matrix used to construct the preconditioner, which we have set to be the viscosity-weighted mass matrix

The solver for the first block, representing the velocity, is GMRES/LU. Note that the prefix is fieldsplit_velocity_, constructed automatically from the name of the field in our DM. Also note that there are two matrices, one from our original matrix, and one from our matrix used to construct the preconditioner, but they are identical. In an optimized, scalable solver, this block would likely be solved by multigrid, but here we use LU for verification purposes.

The solver for the second block, with prefix fieldsplit_pressure_, is also GMRES/LU, however we cannot factor the Schur complement operator since we never explicitly assemble it. Thus we assemble the viscosity-weighted mass matrix on the pressure space as an approximation. Notice that the Schur complement has the velocity solver embedded in it.

Finally, the SNES viewer reports the system matrix and matrix from which the preconditioner is constructed

We see that they have the same nonzero pattern, even though the matrix used to construct the preconditioner only contains the diagonal blocks. This is because zeros were inserted to define the nonzero structure. We can remove these nonzeros by telling the DM not to insert zero at preallocation time, and also telling the matrix itself to ignore the zeros from the assembly process.

We can see a sparsity portrait of the system and preconditioning matrices if the installation supports X-windows visualization

System matrix with sparse stencil#

Matrix used to construct the preconditioner#

Matrix used to construct the preconditioner with sparse stencil#

If we want to check the convergence of the solver, we can also do that using options. Both the linear and nonlinear solvers converge in a single iteration, which is exactly what we want. In order to have this happen, we must have the tolerance on both the outer KSP solver and the inner Schur complement solver be low enough. Notice that the sure complement solver is used twice, and converges in seven iterates each time.

We can look at the scalability of the solve by refining the mesh. We see that the Schur complement solve looks robust to grid refinement.

Starting off with an exact solver allows us to check that the discretization, equations, and boundary conditions are correct. Moreover, choosing the Schur complement formulation, rather than a sparse direct solve, gives us a path to incremental boost the scalability. Our first step will be to replace the direct solve of the momentum operator, which has cost superlinear in \(N\), with a more scalable alternative. Since the operator is still elliptic, despite the viscosity variation, we should be able to use some form of multigrid. We will start with algebraic multigrid because it handles coefficient variation well, even if the setup time is larger than the geometric variant.

This looks alright, but the number of iterates grows with refinement. At 3 refinements, it is 16, 30 at 4 refinements, and 70 at 5 refinements. Increasing the number of smoother iterates to four, -fieldsplit_velocity_mg_levels_ksp_max_it 4, brings down the number of iterates, but not the growth. Using w-cycles and full multigrid does not help either. It is likely that the coarse grids made by MIS are inaccurate for the \(P_2\) discretization.

We can instead use geometric multigrid, and we would hope get more accurate coarse bases. The -dm_refine_hierarchy allows us to make a hierarchy of refined meshes and sets the number of multigrid levels automatically. Then all we need to specify is -fieldsplit_velocity_pc_type mg, as we see in the test

This behaves well for the initial mesh,

and is also stable under refinement

Finally, we can back off the pressure solve. ILU(0) is good enough to maintain a constant number of iterates as we refine the grid. We could continue to refine our preconditioner by playing with the tolerance of the inner multigrid and Schur complement solves, trading fewer inner iterates for more outer iterates.

We can make the problem harder by increasing the wave number and size of the viscosity perturbation. If we set the \(B\) parameter to 6.9, we have a factor of one million increase in viscosity across the cell. At this scale, we see that we lose enough accuracy in our Jacobian calculation to defeat our Taylor test, but we are still able to solve the problem efficiently.

M. G. Knepley, J. Brown, K. Rupp, and B. F. Smith. Achieving high performance with unified residual evaluation. ArXiv e-prints, September 2013. arXiv:1309.1204.

**Examples:**

Example 1 (sass):
```sass
static void f0_p(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscInt d;
  for (d = 0, f0[0] = 0.0; d < dim; ++d) f0[0] -= u_x[d * dim + d];
}
```

Example 2 (sass):
```sass
static void f1_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  const PetscInt  Nc = uOff[1] - uOff[0];
  PetscInt        c, d;

  for (c = 0; c < Nc; ++c) {
    for (d = 0; d < dim; ++d) f1[c * dim + d] = mu * (u_x[c * dim + d] + u_x[d * dim + c]);
    f1[c * dim + c] -= u[uOff[1]];
  }
```

Example 3 (cpp):
```cpp
static PetscErrorCode quadratic_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt c;

  u[0] = (dim - 1) * PetscSqr(x[0]);
  for (c = 1; c < Nc; ++c) {
    u[0] += PetscSqr(x[c]);
    u[c] = 2.0 * PetscSqr(x[0]) - 2.0 * x[0] * x[c];
  }
  return PETSC_SUCCESS;
}

static PetscErrorCode quadratic_p(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;

  u[0] = -0.5 * dim;
  for (d = 0; d < dim; ++d) u[0] += x[d];
  return PETSC_SUCCESS;
}

static void f0_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  PetscInt        d;

  f0[0] = (dim - 1) * 4.0 * mu - 1.0;
  for (d = 1; d < dim; ++d) f0[d] = 4.0 * mu - 1.0;
}

/* Trigonometric MMS Solution
   2D:

     u = sin(pi x) + sin(pi y)
     v = -pi cos(pi x) y
     p = sin(2 pi x) + sin(2 pi y)
     f = <2pi cos(2 pi x) + mu pi^2 sin(pi x) + mu pi^2 sin(pi y), 2pi cos(2 pi y) - mu pi^3 cos(pi x) y>

   so that

     e(u) = (grad u + grad u^T) = /        2pi cos(pi x)             pi cos(pi y) + pi^2 sin(pi x) y \
                                  \ pi cos(pi y) + pi^2 sin(pi x) y          -2pi cos(pi x)          /
     div mu e(u) - \nabla p + f = mu <-pi^2 sin(pi x) - pi^2 sin(pi y), pi^3 cos(pi x) y> - <2pi cos(2 pi x), 2pi cos(2 pi y)> + <f_x, f_y> = 0
     \nabla \cdot u             = pi cos(pi x) - pi cos(pi x) = 0

   3D:

     u = 2 sin(pi x) + sin(pi y) + sin(pi z)
     v = -pi cos(pi x) y
     w = -pi cos(pi x) z
     p = sin(2 pi x) + sin(2 pi y) + sin(2 pi z)
     f = <2pi cos(2 pi x) + mu 2pi^2 sin(pi x) + mu pi^2 sin(pi y) + mu pi^2 sin(pi z), 2pi cos(2 pi y) - mu pi^3 cos(pi x) y, 2pi cos(2 pi z) - mu pi^3 cos(pi x) z>

   so that

     e(u) = (grad u + grad u^T) = /        4pi cos(pi x)             pi cos(pi y) + pi^2 sin(pi x) y  pi cos(pi z) + pi^2 sin(pi x) z \
                                  | pi cos(pi y) + pi^2 sin(pi x) y          -2pi cos(pi x)                        0                  |
                                  \ pi cos(pi z) + pi^2 sin(pi x) z               0                         -2pi cos(pi x)            /
     div mu e(u) - \nabla p + f = mu <-2pi^2 sin(pi x) - pi^2 sin(pi y) - pi^2 sin(pi z), pi^3 cos(pi x) y, pi^3 cos(pi x) z> - <2pi cos(2 pi x), 2pi cos(2 pi y), 2pi cos(2 pi z)> + <f_x, f_y, f_z> = 0
     \nabla \cdot u             = 2 pi cos(pi x) - pi cos(pi x) - pi cos(pi x) = 0
*/
static PetscErrorCode trig_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt c;

  u[0] = (dim - 1) * PetscSinReal(PETSC_PI * x[0]);
  for (c = 1; c < Nc; ++c) {
    u[0] += PetscSinReal(PETSC_PI * x[c]);
    u[c] = -PETSC_PI * PetscCosReal(PETSC_PI * x[0]) * x[c];
  }
  return PETSC_SUCCESS;
}

static PetscErrorCode trig_p(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;

  for (d = 0, u[0] = 0.0; d < dim; ++d) u[0] += PetscSinReal(2.0 * PETSC_PI * x[d]);
  return PETSC_SUCCESS;
}

static void f0_trig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  PetscInt        d;

  f0[0] = -2.0 * PETSC_PI * PetscCosReal(2.0 * PETSC_PI * x[0]) - (dim - 1) * mu * PetscSqr(PETSC_PI) * PetscSinReal(PETSC_PI * x[0]);
  for (d = 1; d < dim; ++d) {
    f0[0] -= mu * PetscSqr(PETSC_PI) * PetscSinReal(PETSC_PI * x[d]);
    f0[d] = -2.0 * PETSC_PI * PetscCosReal(2.0 * PETSC_PI * x[d]) + mu * PetscPowRealInt(PETSC_PI, 3) * PetscCosReal(PETSC_PI * x[0]) * x[d];
  }
}

/* Inline helpers for computing exact velocity in void boundary kernels */
static inline void ExactVelocityQuadratic(PetscInt dim, const PetscReal x[], PetscScalar g[])
{
  PetscInt c;

  g[0] = (dim - 1) * x[0] * x[0];
  for (c = 1; c < dim; ++c) {
    g[0] += x[c] * x[c];
    g[c] = 2.0 * x[0] * x[0] - 2.0 * x[0] * x[c];
  }
}

static inline void ExactVelocityTrig(PetscInt dim, const PetscReal x[], PetscScalar g[])
{
  PetscInt c;

  g[0] = (dim - 1) * PetscSinReal(PETSC_PI * x[0]);
  for (c = 1; c < dim; ++c) {
    g[0] += PetscSinReal(PETSC_PI * x[c]);
    g[c] = -PETSC_PI * PetscCosReal(PETSC_PI * x[0]) * x[c];
  }
}

/* Nitsche boundary residual kernels for velocity (field 0)
   f0_bd_u[c] = -mu * sum_d (u_x[c*dim+d] + u_x[d*dim+c]) * n[d]   (consistency: stress flux from IBP)
              + p * n[c]                                               (pressure flux from IBP)
              + penalty * (u[c] - g[c])                                (penalty) */
static void f0_bd_nitsche_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu      = PetscRealPart(constants[0]);
  const PetscReal penalty = PetscRealPart(constants[1]);
  PetscScalar     g[3];
  PetscInt        c, d;

  ExactVelocityQuadratic(dim, x, g);
  for (c = 0; c < dim; ++c) {
    f0[c] = penalty * (u[c] - g[c]) + u[uOff[1]] * n[c];
    for (d = 0; d < dim; ++d) f0[c] -= mu * (u_x[c * dim + d] + u_x[d * dim + c]) * n[d];
  }
}

static void f0_bd_nitsche_trig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu      = PetscRealPart(constants[0]);
  const PetscReal penalty = PetscRealPart(constants[1]);
  PetscScalar     g[3];
  PetscInt        c, d;

  ExactVelocityTrig(dim, x, g);
  for (c = 0; c < dim; ++c) {
    f0[c] = penalty * (u[c] - g[c]) + u[uOff[1]] * n[c];
    for (d = 0; d < dim; ++d) f0[c] -= mu * (u_x[c * dim + d] + u_x[d * dim + c]) * n[d];
  }
}

/* f1_bd_u[c*dim+d] = -mu * (n[d]*(u[c]-g[c]) + n[c]*(u[d]-g[d]))  (symmetry / adjoint consistency) */
static void f1_bd_nitsche_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  PetscScalar     g[3];
  PetscInt        c, d;

  ExactVelocityQuadratic(dim, x, g);
  for (c = 0; c < dim; ++c)
    for (d = 0; d < dim; ++d) f1[c * dim + d] = -mu * (n[d] * (u[c] - g[c]) + n[c] * (u[d] - g[d]));
}

static void f1_bd_nitsche_trig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  PetscScalar     g[3];
  PetscInt        c, d;

  ExactVelocityTrig(dim, x, g);
  for (c = 0; c < dim; ++c)
    for (d = 0; d < dim; ++d) f1[c * dim + d] = -mu * (n[d] * (u[c] - g[c]) + n[c] * (u[d] - g[d]));
}

/* Nitsche boundary residual kernels for pressure (field 1)
   f0_bd_p = sum_d n[d] * (u[d] - g[d])  (continuity equation boundary correction) */
static void f0_bd_nitsche_quadratic_p(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscScalar g[3];
  PetscInt    d;

  ExactVelocityQuadratic(dim, x, g);
  f0[0] = 0.0;
  for (d = 0; d < dim; ++d) f0[0] += n[d] * (u[d] - g[d]);
}

static void f0_bd_nitsche_trig_p(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscScalar g[3];
  PetscInt    d;

  ExactVelocityTrig(dim, x, g);
  f0[0] = 0.0;
  for (d = 0; d < dim; ++d) f0[0] += n[d] * (u[d] - g[d]);
}

/* Nitsche boundary Jacobian kernels (solution-independent)
   g0_bd_uu[c*Nc+d] = delta(c,d) * penalty  (penalty Jacobian) */
static void g0_bd_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  const PetscReal penalty = PetscRealPart(constants[1]);
  const PetscInt  Nc      = uOff[1] - uOff[0];
  PetscInt        c;

  for (c = 0; c < Nc; ++c) g0[c * Nc + c] = penalty;
}

/* g1_bd_uu[(c*Nc+d)*dim+e] = -mu * (delta(c,d)*n[e] + delta(c,e)*n[d])  (consistency Jacobian: df0/du_x) */
static void g1_bd_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g1[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  const PetscInt  Nc = uOff[1] - uOff[0];
  PetscInt        c, d, e;

  for (c = 0; c < Nc; ++c)
    for (d = 0; d < Nc; ++d)
      for (e = 0; e < dim; ++e) g1[(c * Nc + d) * dim + e] = -mu * ((c == d ? 1.0 : 0.0) * n[e] + (c == e ? 1.0 : 0.0) * n[d]);
}

/* g2_bd_uu[(c*Nc+d)*dim+e] = -mu * (n[e]*delta(c,d) + n[c]*delta(e,d))  (symmetry Jacobian: df1/du) */
static void g2_bd_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g2[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  const PetscInt  Nc = uOff[1] - uOff[0];
  PetscInt        c, d, e;

  for (c = 0; c < Nc; ++c)
    for (d = 0; d < Nc; ++d)
      for (e = 0; e < dim; ++e) g2[(c * Nc + d) * dim + e] = -mu * (n[e] * (c == d ? 1.0 : 0.0) + n[c] * (e == d ? 1.0 : 0.0));
}

/* g0_bd_up[c*1+0] = n[c]  (velocity-pressure coupling: df0_u/dp) */
static void g0_bd_up(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  PetscInt c;

  for (c = 0; c < dim; ++c) g0[c] = n[c];
}

/* g0_bd_pu[0*Nc+d] = n[d]  (pressure-velocity coupling: df0_p/du) */
static void g0_bd_pu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  PetscInt d;

  for (d = 0; d < dim; ++d) g0[d] = n[d];
}

static PetscErrorCode ProcessOptions(MPI_Comm comm, AppCtx *options)
{
  PetscInt sol, bc;

  PetscFunctionBeginUser;
  options->sol = SOL_QUADRATIC;
  options->bc  = BC_ESSENTIAL;
  PetscOptionsBegin(comm, "", "Stokes Problem Options", "DMPLEX");
  sol = options->sol;
  PetscCall(PetscOptionsEList("-sol", "The MMS solution", "ex62.c", SolTypes, PETSC_STATIC_ARRAY_LENGTH(SolTypes) - 3, SolTypes[options->sol], &sol, NULL));
  options->sol = (SolType)sol;
  bc           = options->bc;
  PetscCall(PetscOptionsEList("-bc", "The boundary condition type", "ex62.c", BCTypes, PETSC_STATIC_ARRAY_LENGTH(BCTypes) - 3, BCTypes[options->bc], &bc, NULL));
  options->bc = (BCType)bc;
  PetscOptionsEnd();
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode CreateMesh(MPI_Comm comm, AppCtx *user, DM *dm)
{
  PetscFunctionBeginUser;
  PetscCall(DMCreate(comm, dm));
  PetscCall(DMSetType(*dm, DMPLEX));
  PetscCall(DMSetFromOptions(*dm));
  PetscCall(DMViewFromOptions(*dm, NULL, "-dm_view"));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupParameters(MPI_Comm comm, AppCtx *ctx)
{
  Parameter *p;

  PetscFunctionBeginUser;
  /* setup PETSc parameter bag */
  PetscCall(PetscBagCreate(PETSC_COMM_SELF, sizeof(Parameter), &ctx->bag));
  PetscCall(PetscBagGetData(ctx->bag, &p));
  PetscCall(PetscBagSetName(ctx->bag, "par", "Stokes Parameters"));
  PetscCall(PetscBagRegisterScalar(ctx->bag, &p->mu, 1.0, "mu", "Dynamic Shear Viscosity, Pa s"));
  PetscCall(PetscBagRegisterScalar(ctx->bag, &p->eta, 100.0, "eta", "Nitsche penalty parameter (dimensionless)"));
  PetscCall(PetscBagSetFromOptions(ctx->bag));
  {
    PetscViewer       viewer;
    PetscViewerFormat format;
    PetscBool         flg;

    PetscCall(PetscOptionsCreateViewer(comm, NULL, NULL, "-param_view", &viewer, &format, &flg));
    if (flg) {
      PetscCall(PetscViewerPushFormat(viewer, format));
      PetscCall(PetscBagView(ctx->bag, viewer));
      PetscCall(PetscViewerFlush(viewer));
      PetscCall(PetscViewerPopFormat(viewer));
      PetscCall(PetscViewerDestroy(&viewer));
    }
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupEqn(DM dm, AppCtx *user)
{
  PetscErrorCode (*exactFuncs[2])(PetscInt, PetscReal, const PetscReal[], PetscInt, PetscScalar *, void *);
  void (*f0_bd_u)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]);
  void (*f1_bd_u)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]);
  void (*f0_bd_p)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]);
  PetscDS        ds;
  DMLabel        label;
  const PetscInt id = 1;

  PetscFunctionBeginUser;
  PetscCall(DMGetDS(dm, &ds));
  switch (user->sol) {
  case SOL_QUADRATIC:
    PetscCall(PetscDSSetResidual(ds, 0, f0_quadratic_u, f1_u));
    exactFuncs[0] = quadratic_u;
    exactFuncs[1] = quadratic_p;
    f0_bd_u       = f0_bd_nitsche_quadratic_u;
    f1_bd_u       = f1_bd_nitsche_quadratic_u;
    f0_bd_p       = f0_bd_nitsche_quadratic_p;
    break;
  case SOL_TRIG:
    PetscCall(PetscDSSetResidual(ds, 0, f0_trig_u, f1_u));
    exactFuncs[0] = trig_u;
    exactFuncs[1] = trig_p;
    f0_bd_u       = f0_bd_nitsche_trig_u;
    f1_bd_u       = f1_bd_nitsche_trig_u;
    f0_bd_p       = f0_bd_nitsche_trig_p;
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)dm), PETSC_ERR_ARG_WRONG, "Unsupported solution type: %s (%d)", SolTypes[PetscMin(user->sol, SOL_UNKNOWN)], user->sol);
  }
  PetscCall(PetscDSSetResidual(ds, 1, f0_p, NULL));
  PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_uu));
  PetscCall(PetscDSSetJacobian(ds, 0, 1, NULL, NULL, g2_up, NULL));
  PetscCall(PetscDSSetJacobian(ds, 1, 0, NULL, g1_pu, NULL, NULL));
  PetscCall(PetscDSSetJacobianPreconditioner(ds, 0, 0, NULL, NULL, NULL, g3_uu));
  PetscCall(PetscDSSetJacobianPreconditioner(ds, 1, 1, g0_pp, NULL, NULL, NULL));

  PetscCall(PetscDSSetExactSolution(ds, 0, exactFuncs[0], user));
  PetscCall(PetscDSSetExactSolution(ds, 1, exactFuncs[1], user));

  PetscCall(DMGetLabel(dm, "marker", &label));
  switch (user->bc) {
  case BC_ESSENTIAL:
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)exactFuncs[0], NULL, user, NULL));
    break;
  case BC_NITSCHE: {
    PetscWeakForm   wf;
    DMLabel         faceSetsLabel;
    IS              valueIS;
    const PetscInt *faceSetValues;
    PetscInt        numValues, bd, i;

    PetscCall(DMGetLabel(dm, "Face Sets", &faceSetsLabel));
    PetscCall(DMLabelGetNumValues(faceSetsLabel, &numValues));
    PetscCall(DMLabelGetValueIS(faceSetsLabel, &valueIS));
    PetscCall(ISGetIndices(valueIS, &faceSetValues));

    /* Velocity boundary: natural BC with Nitsche terms on all boundary faces */
    PetscCall(DMAddBoundary(dm, DM_BC_NATURAL, "wall", faceSetsLabel, numValues, faceSetValues, 0, 0, NULL, NULL, NULL, user, &bd));
    PetscCall(PetscDSGetBoundary(ds, bd, &wf, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL));
    for (i = 0; i < numValues; ++i) {
      /* Velocity residual (field 0): f0 and f1 */
      PetscCall(PetscWeakFormSetIndexBdResidual(wf, faceSetsLabel, faceSetValues[i], 0, 0, 0, f0_bd_u, 0, f1_bd_u));
      /* Velocity-velocity Jacobian (field 0, field 0): g0 (penalty), g1 (consistency), g2 (symmetry) */
      PetscCall(PetscWeakFormSetIndexBdJacobian(wf, faceSetsLabel, faceSetValues[i], 0, 0, 0, 0, g0_bd_uu, 0, g1_bd_uu, 0, g2_bd_uu, 0, NULL));
      /* Velocity-pressure Jacobian (field 0, field 1): g0 (pressure coupling) */
      PetscCall(PetscWeakFormSetIndexBdJacobian(wf, faceSetsLabel, faceSetValues[i], 0, 1, 0, 0, g0_bd_up, 0, NULL, 0, NULL, 0, NULL));
    }

    /* Pressure boundary: natural BC for continuity equation correction */
    PetscCall(DMAddBoundary(dm, DM_BC_NATURAL, "wall_pres", faceSetsLabel, numValues, faceSetValues, 1, 0, NULL, NULL, NULL, user, &bd));
    PetscCall(PetscDSGetBoundary(ds, bd, &wf, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL));
    for (i = 0; i < numValues; ++i) {
      /* Pressure residual (field 1): f0 */
      PetscCall(PetscWeakFormSetIndexBdResidual(wf, faceSetsLabel, faceSetValues[i], 1, 0, 0, f0_bd_p, 0, NULL));
      /* Pressure-velocity Jacobian (field 1, field 0): g0 */
      PetscCall(PetscWeakFormSetIndexBdJacobian(wf, faceSetsLabel, faceSetValues[i], 1, 0, 0, 0, g0_bd_pu, 0, NULL, 0, NULL, 0, NULL));
    }
    PetscCall(ISRestoreIndices(valueIS, &faceSetValues));
    PetscCall(ISDestroy(&valueIS));
  } break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)dm), PETSC_ERR_ARG_WRONG, "Unsupported BC type: %s (%d)", BCTypes[PetscMin(user->bc, BC_UNKNOWN)], user->bc);
  }

  /* Make constant values available to pointwise functions */
  {
    Parameter  *param;
    PetscScalar constants[2];

    PetscCall(PetscBagGetData(user->bag, &param));
    constants[0] = param->mu; /* dynamic shear viscosity, Pa s */
    constants[1] = 0.0;       /* Nitsche penalty (set below if needed) */
    if (user->bc == BC_NITSCHE) {
      /* Compute cell size h from mesh */
      PetscInt  dim, cStart;
      PetscReal vol, h;

      PetscCall(DMGetDimension(dm, &dim));
      PetscCall(DMPlexGetHeightStratum(dm, 0, &cStart, NULL));
      PetscCall(DMPlexComputeCellGeometryFVM(dm, cStart, &vol, NULL, NULL));
      h            = PetscPowReal(vol, 1.0 / dim);
      constants[1] = PetscRealPart(param->eta) * PetscRealPart(param->mu) / h;
    }
    PetscCall(PetscDSSetConstants(ds, 2, constants));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode zero(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt c;
  for (c = 0; c < Nc; ++c) u[c] = 0.0;
  return PETSC_SUCCESS;
}
static PetscErrorCode one(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt c;
  for (c = 0; c < Nc; ++c) u[c] = 1.0;
  return PETSC_SUCCESS;
}

static PetscErrorCode CreatePressureNullSpace(DM dm, PetscInt origField, PetscInt field, MatNullSpace *nullspace)
{
  Vec vec;
  PetscErrorCode (*funcs[2])(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *u, PetscCtx ctx) = {zero, one};

  PetscFunctionBeginUser;
  PetscCheck(origField == 1, PetscObjectComm((PetscObject)dm), PETSC_ERR_ARG_WRONG, "Field %" PetscInt_FMT " should be 1 for pressure", origField);
  funcs[field] = one;
  {
    PetscDS ds;
    PetscCall(DMGetDS(dm, &ds));
    PetscCall(PetscObjectViewFromOptions((PetscObject)ds, NULL, "-ds_view"));
  }
  PetscCall(DMCreateGlobalVector(dm, &vec));
  PetscCall(DMProjectFunction(dm, 0.0, funcs, NULL, INSERT_ALL_VALUES, vec));
  PetscCall(VecNormalize(vec, NULL));
  PetscCall(MatNullSpaceCreate(PetscObjectComm((PetscObject)dm), PETSC_FALSE, 1, &vec, nullspace));
  PetscCall(VecDestroy(&vec));
  /* New style for field null spaces */
  {
    PetscObject  pressure;
    MatNullSpace nullspacePres;

    PetscCall(DMGetField(dm, field, NULL, &pressure));
    PetscCall(MatNullSpaceCreate(PetscObjectComm(pressure), PETSC_TRUE, 0, NULL, &nullspacePres));
    PetscCall(PetscObjectCompose(pressure, "nullspace", (PetscObject)nullspacePres));
    PetscCall(MatNullSpaceDestroy(&nullspacePres));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupProblem(DM dm, PetscErrorCode (*setupEqn)(DM, AppCtx *), AppCtx *user)
{
  DM              cdm = dm;
  PetscQuadrature q   = NULL;
  PetscBool       simplex;
  PetscInt        dim, Nf = 2, f, Nc[2];
  const char     *name[2]   = {"velocity", "pressure"};
  const char     *prefix[2] = {"vel_", "pres_"};

  PetscFunctionBegin;
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMPlexIsSimplex(dm, &simplex));
  Nc[0] = dim;
  Nc[1] = 1;
  for (f = 0; f < Nf; ++f) {
    PetscFE fe;

    PetscCall(PetscFECreateDefault(PETSC_COMM_SELF, dim, Nc[f], simplex, prefix[f], -1, &fe));
    PetscCall(PetscObjectSetName((PetscObject)fe, name[f]));
    if (!q) PetscCall(PetscFEGetQuadrature(fe, &q));
    PetscCall(PetscFESetQuadrature(fe, q));
    PetscCall(DMSetField(dm, f, NULL, (PetscObject)fe));
    PetscCall(PetscFEDestroy(&fe));
  }
  PetscCall(DMCreateDS(dm));
  PetscCall((*setupEqn)(dm, user));
  while (cdm) {
    PetscCall(DMCopyDisc(dm, cdm));
    PetscCall(DMSetNullSpaceConstructor(cdm, 1, CreatePressureNullSpace));
    PetscCall(DMGetCoarseDM(cdm, &cdm));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

int main(int argc, char **argv)
{
  SNES   snes;
  DM     dm;
  Vec    u;
  AppCtx user;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(ProcessOptions(PETSC_COMM_WORLD, &user));
  PetscCall(CreateMesh(PETSC_COMM_WORLD, &user, &dm));
  PetscCall(SNESCreate(PetscObjectComm((PetscObject)dm), &snes));
  PetscCall(SNESSetDM(snes, dm));
  PetscCall(DMSetApplicationContext(dm, &user));

  PetscCall(SetupParameters(PETSC_COMM_WORLD, &user));
  PetscCall(SetupProblem(dm, SetupEqn, &user));
  PetscCall(DMPlexCreateClosureIndex(dm, NULL));

  PetscCall(DMCreateGlobalVector(dm, &u));
  PetscCall(DMPlexSetSNESLocalFEM(dm, PETSC_FALSE, &user));
  PetscCall(SNESSetFromOptions(snes));
  PetscCall(DMSNESCheckFromOptions(snes, u));
  PetscCall(PetscObjectSetName((PetscObject)u, "Solution"));
  {
    Mat          J;
    MatNullSpace sp;

    PetscCall(SNESSetUp(snes));
    PetscCall(CreatePressureNullSpace(dm, 1, 1, &sp));
    PetscCall(SNESGetJacobian(snes, &J, NULL, NULL, NULL));
    PetscCall(MatSetNullSpace(J, sp));
    PetscCall(MatNullSpaceDestroy(&sp));
    PetscCall(PetscObjectSetName((PetscObject)J, "Jacobian"));
    PetscCall(MatViewFromOptions(J, NULL, "-J_view"));
  }
  PetscCall(SNESSolve(snes, NULL, u));

  PetscCall(VecDestroy(&u));
  PetscCall(SNESDestroy(&snes));
  PetscCall(DMDestroy(&dm));
  PetscCall(PetscBagDestroy(&user.bag));
  PetscCall(PetscFinalize());
  return 0;
}
```

Example 4 (cpp):
```cpp
static PetscErrorCode quadratic_p(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;

  u[0] = -0.5 * dim;
  for (d = 0; d < dim; ++d) u[0] += x[d];
  return PETSC_SUCCESS;
}

static void f0_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  PetscInt        d;

  f0[0] = (dim - 1) * 4.0 * mu - 1.0;
  for (d = 1; d < dim; ++d) f0[d] = 4.0 * mu - 1.0;
}

/* Trigonometric MMS Solution
   2D:

     u = sin(pi x) + sin(pi y)
     v = -pi cos(pi x) y
     p = sin(2 pi x) + sin(2 pi y)
     f = <2pi cos(2 pi x) + mu pi^2 sin(pi x) + mu pi^2 sin(pi y), 2pi cos(2 pi y) - mu pi^3 cos(pi x) y>

   so that

     e(u) = (grad u + grad u^T) = /        2pi cos(pi x)             pi cos(pi y) + pi^2 sin(pi x) y \
                                  \ pi cos(pi y) + pi^2 sin(pi x) y          -2pi cos(pi x)          /
     div mu e(u) - \nabla p + f = mu <-pi^2 sin(pi x) - pi^2 sin(pi y), pi^3 cos(pi x) y> - <2pi cos(2 pi x), 2pi cos(2 pi y)> + <f_x, f_y> = 0
     \nabla \cdot u             = pi cos(pi x) - pi cos(pi x) = 0

   3D:

     u = 2 sin(pi x) + sin(pi y) + sin(pi z)
     v = -pi cos(pi x) y
     w = -pi cos(pi x) z
     p = sin(2 pi x) + sin(2 pi y) + sin(2 pi z)
     f = <2pi cos(2 pi x) + mu 2pi^2 sin(pi x) + mu pi^2 sin(pi y) + mu pi^2 sin(pi z), 2pi cos(2 pi y) - mu pi^3 cos(pi x) y, 2pi cos(2 pi z) - mu pi^3 cos(pi x) z>

   so that

     e(u) = (grad u + grad u^T) = /        4pi cos(pi x)             pi cos(pi y) + pi^2 sin(pi x) y  pi cos(pi z) + pi^2 sin(pi x) z \
                                  | pi cos(pi y) + pi^2 sin(pi x) y          -2pi cos(pi x)                        0                  |
                                  \ pi cos(pi z) + pi^2 sin(pi x) z               0                         -2pi cos(pi x)            /
     div mu e(u) - \nabla p + f = mu <-2pi^2 sin(pi x) - pi^2 sin(pi y) - pi^2 sin(pi z), pi^3 cos(pi x) y, pi^3 cos(pi x) z> - <2pi cos(2 pi x), 2pi cos(2 pi y), 2pi cos(2 pi z)> + <f_x, f_y, f_z> = 0
     \nabla \cdot u             = 2 pi cos(pi x) - pi cos(pi x) - pi cos(pi x) = 0
*/
static PetscErrorCode trig_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt c;

  u[0] = (dim - 1) * PetscSinReal(PETSC_PI * x[0]);
  for (c = 1; c < Nc; ++c) {
    u[0] += PetscSinReal(PETSC_PI * x[c]);
    u[c] = -PETSC_PI * PetscCosReal(PETSC_PI * x[0]) * x[c];
  }
  return PETSC_SUCCESS;
}

static PetscErrorCode trig_p(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;

  for (d = 0, u[0] = 0.0; d < dim; ++d) u[0] += PetscSinReal(2.0 * PETSC_PI * x[d]);
  return PETSC_SUCCESS;
}

static void f0_trig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  PetscInt        d;

  f0[0] = -2.0 * PETSC_PI * PetscCosReal(2.0 * PETSC_PI * x[0]) - (dim - 1) * mu * PetscSqr(PETSC_PI) * PetscSinReal(PETSC_PI * x[0]);
  for (d = 1; d < dim; ++d) {
    f0[0] -= mu * PetscSqr(PETSC_PI) * PetscSinReal(PETSC_PI * x[d]);
    f0[d] = -2.0 * PETSC_PI * PetscCosReal(2.0 * PETSC_PI * x[d]) + mu * PetscPowRealInt(PETSC_PI, 3) * PetscCosReal(PETSC_PI * x[0]) * x[d];
  }
}

/* Inline helpers for computing exact velocity in void boundary kernels */
static inline void ExactVelocityQuadratic(PetscInt dim, const PetscReal x[], PetscScalar g[])
{
  PetscInt c;

  g[0] = (dim - 1) * x[0] * x[0];
  for (c = 1; c < dim; ++c) {
    g[0] += x[c] * x[c];
    g[c] = 2.0 * x[0] * x[0] - 2.0 * x[0] * x[c];
  }
}

static inline void ExactVelocityTrig(PetscInt dim, const PetscReal x[], PetscScalar g[])
{
  PetscInt c;

  g[0] = (dim - 1) * PetscSinReal(PETSC_PI * x[0]);
  for (c = 1; c < dim; ++c) {
    g[0] += PetscSinReal(PETSC_PI * x[c]);
    g[c] = -PETSC_PI * PetscCosReal(PETSC_PI * x[0]) * x[c];
  }
}

/* Nitsche boundary residual kernels for velocity (field 0)
   f0_bd_u[c] = -mu * sum_d (u_x[c*dim+d] + u_x[d*dim+c]) * n[d]   (consistency: stress flux from IBP)
              + p * n[c]                                               (pressure flux from IBP)
              + penalty * (u[c] - g[c])                                (penalty) */
static void f0_bd_nitsche_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu      = PetscRealPart(constants[0]);
  const PetscReal penalty = PetscRealPart(constants[1]);
  PetscScalar     g[3];
  PetscInt        c, d;

  ExactVelocityQuadratic(dim, x, g);
  for (c = 0; c < dim; ++c) {
    f0[c] = penalty * (u[c] - g[c]) + u[uOff[1]] * n[c];
    for (d = 0; d < dim; ++d) f0[c] -= mu * (u_x[c * dim + d] + u_x[d * dim + c]) * n[d];
  }
}

static void f0_bd_nitsche_trig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu      = PetscRealPart(constants[0]);
  const PetscReal penalty = PetscRealPart(constants[1]);
  PetscScalar     g[3];
  PetscInt        c, d;

  ExactVelocityTrig(dim, x, g);
  for (c = 0; c < dim; ++c) {
    f0[c] = penalty * (u[c] - g[c]) + u[uOff[1]] * n[c];
    for (d = 0; d < dim; ++d) f0[c] -= mu * (u_x[c * dim + d] + u_x[d * dim + c]) * n[d];
  }
}

/* f1_bd_u[c*dim+d] = -mu * (n[d]*(u[c]-g[c]) + n[c]*(u[d]-g[d]))  (symmetry / adjoint consistency) */
static void f1_bd_nitsche_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  PetscScalar     g[3];
  PetscInt        c, d;

  ExactVelocityQuadratic(dim, x, g);
  for (c = 0; c < dim; ++c)
    for (d = 0; d < dim; ++d) f1[c * dim + d] = -mu * (n[d] * (u[c] - g[c]) + n[c] * (u[d] - g[d]));
}

static void f1_bd_nitsche_trig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  PetscScalar     g[3];
  PetscInt        c, d;

  ExactVelocityTrig(dim, x, g);
  for (c = 0; c < dim; ++c)
    for (d = 0; d < dim; ++d) f1[c * dim + d] = -mu * (n[d] * (u[c] - g[c]) + n[c] * (u[d] - g[d]));
}

/* Nitsche boundary residual kernels for pressure (field 1)
   f0_bd_p = sum_d n[d] * (u[d] - g[d])  (continuity equation boundary correction) */
static void f0_bd_nitsche_quadratic_p(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscScalar g[3];
  PetscInt    d;

  ExactVelocityQuadratic(dim, x, g);
  f0[0] = 0.0;
  for (d = 0; d < dim; ++d) f0[0] += n[d] * (u[d] - g[d]);
}

static void f0_bd_nitsche_trig_p(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscScalar g[3];
  PetscInt    d;

  ExactVelocityTrig(dim, x, g);
  f0[0] = 0.0;
  for (d = 0; d < dim; ++d) f0[0] += n[d] * (u[d] - g[d]);
}

/* Nitsche boundary Jacobian kernels (solution-independent)
   g0_bd_uu[c*Nc+d] = delta(c,d) * penalty  (penalty Jacobian) */
static void g0_bd_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  const PetscReal penalty = PetscRealPart(constants[1]);
  const PetscInt  Nc      = uOff[1] - uOff[0];
  PetscInt        c;

  for (c = 0; c < Nc; ++c) g0[c * Nc + c] = penalty;
}

/* g1_bd_uu[(c*Nc+d)*dim+e] = -mu * (delta(c,d)*n[e] + delta(c,e)*n[d])  (consistency Jacobian: df0/du_x) */
static void g1_bd_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g1[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  const PetscInt  Nc = uOff[1] - uOff[0];
  PetscInt        c, d, e;

  for (c = 0; c < Nc; ++c)
    for (d = 0; d < Nc; ++d)
      for (e = 0; e < dim; ++e) g1[(c * Nc + d) * dim + e] = -mu * ((c == d ? 1.0 : 0.0) * n[e] + (c == e ? 1.0 : 0.0) * n[d]);
}

/* g2_bd_uu[(c*Nc+d)*dim+e] = -mu * (n[e]*delta(c,d) + n[c]*delta(e,d))  (symmetry Jacobian: df1/du) */
static void g2_bd_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g2[])
{
  const PetscReal mu = PetscRealPart(constants[0]);
  const PetscInt  Nc = uOff[1] - uOff[0];
  PetscInt        c, d, e;

  for (c = 0; c < Nc; ++c)
    for (d = 0; d < Nc; ++d)
      for (e = 0; e < dim; ++e) g2[(c * Nc + d) * dim + e] = -mu * (n[e] * (c == d ? 1.0 : 0.0) + n[c] * (e == d ? 1.0 : 0.0));
}

/* g0_bd_up[c*1+0] = n[c]  (velocity-pressure coupling: df0_u/dp) */
static void g0_bd_up(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  PetscInt c;

  for (c = 0; c < dim; ++c) g0[c] = n[c];
}

/* g0_bd_pu[0*Nc+d] = n[d]  (pressure-velocity coupling: df0_p/du) */
static void g0_bd_pu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  PetscInt d;

  for (d = 0; d < dim; ++d) g0[d] = n[d];
}

static PetscErrorCode ProcessOptions(MPI_Comm comm, AppCtx *options)
{
  PetscInt sol, bc;

  PetscFunctionBeginUser;
  options->sol = SOL_QUADRATIC;
  options->bc  = BC_ESSENTIAL;
  PetscOptionsBegin(comm, "", "Stokes Problem Options", "DMPLEX");
  sol = options->sol;
  PetscCall(PetscOptionsEList("-sol", "The MMS solution", "ex62.c", SolTypes, PETSC_STATIC_ARRAY_LENGTH(SolTypes) - 3, SolTypes[options->sol], &sol, NULL));
  options->sol = (SolType)sol;
  bc           = options->bc;
  PetscCall(PetscOptionsEList("-bc", "The boundary condition type", "ex62.c", BCTypes, PETSC_STATIC_ARRAY_LENGTH(BCTypes) - 3, BCTypes[options->bc], &bc, NULL));
  options->bc = (BCType)bc;
  PetscOptionsEnd();
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode CreateMesh(MPI_Comm comm, AppCtx *user, DM *dm)
{
  PetscFunctionBeginUser;
  PetscCall(DMCreate(comm, dm));
  PetscCall(DMSetType(*dm, DMPLEX));
  PetscCall(DMSetFromOptions(*dm));
  PetscCall(DMViewFromOptions(*dm, NULL, "-dm_view"));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupParameters(MPI_Comm comm, AppCtx *ctx)
{
  Parameter *p;

  PetscFunctionBeginUser;
  /* setup PETSc parameter bag */
  PetscCall(PetscBagCreate(PETSC_COMM_SELF, sizeof(Parameter), &ctx->bag));
  PetscCall(PetscBagGetData(ctx->bag, &p));
  PetscCall(PetscBagSetName(ctx->bag, "par", "Stokes Parameters"));
  PetscCall(PetscBagRegisterScalar(ctx->bag, &p->mu, 1.0, "mu", "Dynamic Shear Viscosity, Pa s"));
  PetscCall(PetscBagRegisterScalar(ctx->bag, &p->eta, 100.0, "eta", "Nitsche penalty parameter (dimensionless)"));
  PetscCall(PetscBagSetFromOptions(ctx->bag));
  {
    PetscViewer       viewer;
    PetscViewerFormat format;
    PetscBool         flg;

    PetscCall(PetscOptionsCreateViewer(comm, NULL, NULL, "-param_view", &viewer, &format, &flg));
    if (flg) {
      PetscCall(PetscViewerPushFormat(viewer, format));
      PetscCall(PetscBagView(ctx->bag, viewer));
      PetscCall(PetscViewerFlush(viewer));
      PetscCall(PetscViewerPopFormat(viewer));
      PetscCall(PetscViewerDestroy(&viewer));
    }
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupEqn(DM dm, AppCtx *user)
{
  PetscErrorCode (*exactFuncs[2])(PetscInt, PetscReal, const PetscReal[], PetscInt, PetscScalar *, void *);
  void (*f0_bd_u)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]);
  void (*f1_bd_u)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]);
  void (*f0_bd_p)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]);
  PetscDS        ds;
  DMLabel        label;
  const PetscInt id = 1;

  PetscFunctionBeginUser;
  PetscCall(DMGetDS(dm, &ds));
  switch (user->sol) {
  case SOL_QUADRATIC:
    PetscCall(PetscDSSetResidual(ds, 0, f0_quadratic_u, f1_u));
    exactFuncs[0] = quadratic_u;
    exactFuncs[1] = quadratic_p;
    f0_bd_u       = f0_bd_nitsche_quadratic_u;
    f1_bd_u       = f1_bd_nitsche_quadratic_u;
    f0_bd_p       = f0_bd_nitsche_quadratic_p;
    break;
  case SOL_TRIG:
    PetscCall(PetscDSSetResidual(ds, 0, f0_trig_u, f1_u));
    exactFuncs[0] = trig_u;
    exactFuncs[1] = trig_p;
    f0_bd_u       = f0_bd_nitsche_trig_u;
    f1_bd_u       = f1_bd_nitsche_trig_u;
    f0_bd_p       = f0_bd_nitsche_trig_p;
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)dm), PETSC_ERR_ARG_WRONG, "Unsupported solution type: %s (%d)", SolTypes[PetscMin(user->sol, SOL_UNKNOWN)], user->sol);
  }
  PetscCall(PetscDSSetResidual(ds, 1, f0_p, NULL));
  PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_uu));
  PetscCall(PetscDSSetJacobian(ds, 0, 1, NULL, NULL, g2_up, NULL));
  PetscCall(PetscDSSetJacobian(ds, 1, 0, NULL, g1_pu, NULL, NULL));
  PetscCall(PetscDSSetJacobianPreconditioner(ds, 0, 0, NULL, NULL, NULL, g3_uu));
  PetscCall(PetscDSSetJacobianPreconditioner(ds, 1, 1, g0_pp, NULL, NULL, NULL));

  PetscCall(PetscDSSetExactSolution(ds, 0, exactFuncs[0], user));
  PetscCall(PetscDSSetExactSolution(ds, 1, exactFuncs[1], user));

  PetscCall(DMGetLabel(dm, "marker", &label));
  switch (user->bc) {
  case BC_ESSENTIAL:
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)exactFuncs[0], NULL, user, NULL));
    break;
  case BC_NITSCHE: {
    PetscWeakForm   wf;
    DMLabel         faceSetsLabel;
    IS              valueIS;
    const PetscInt *faceSetValues;
    PetscInt        numValues, bd, i;

    PetscCall(DMGetLabel(dm, "Face Sets", &faceSetsLabel));
    PetscCall(DMLabelGetNumValues(faceSetsLabel, &numValues));
    PetscCall(DMLabelGetValueIS(faceSetsLabel, &valueIS));
    PetscCall(ISGetIndices(valueIS, &faceSetValues));

    /* Velocity boundary: natural BC with Nitsche terms on all boundary faces */
    PetscCall(DMAddBoundary(dm, DM_BC_NATURAL, "wall", faceSetsLabel, numValues, faceSetValues, 0, 0, NULL, NULL, NULL, user, &bd));
    PetscCall(PetscDSGetBoundary(ds, bd, &wf, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL));
    for (i = 0; i < numValues; ++i) {
      /* Velocity residual (field 0): f0 and f1 */
      PetscCall(PetscWeakFormSetIndexBdResidual(wf, faceSetsLabel, faceSetValues[i], 0, 0, 0, f0_bd_u, 0, f1_bd_u));
      /* Velocity-velocity Jacobian (field 0, field 0): g0 (penalty), g1 (consistency), g2 (symmetry) */
      PetscCall(PetscWeakFormSetIndexBdJacobian(wf, faceSetsLabel, faceSetValues[i], 0, 0, 0, 0, g0_bd_uu, 0, g1_bd_uu, 0, g2_bd_uu, 0, NULL));
      /* Velocity-pressure Jacobian (field 0, field 1): g0 (pressure coupling) */
      PetscCall(PetscWeakFormSetIndexBdJacobian(wf, faceSetsLabel, faceSetValues[i], 0, 1, 0, 0, g0_bd_up, 0, NULL, 0, NULL, 0, NULL));
    }

    /* Pressure boundary: natural BC for continuity equation correction */
    PetscCall(DMAddBoundary(dm, DM_BC_NATURAL, "wall_pres", faceSetsLabel, numValues, faceSetValues, 1, 0, NULL, NULL, NULL, user, &bd));
    PetscCall(PetscDSGetBoundary(ds, bd, &wf, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL));
    for (i = 0; i < numValues; ++i) {
      /* Pressure residual (field 1): f0 */
      PetscCall(PetscWeakFormSetIndexBdResidual(wf, faceSetsLabel, faceSetValues[i], 1, 0, 0, f0_bd_p, 0, NULL));
      /* Pressure-velocity Jacobian (field 1, field 0): g0 */
      PetscCall(PetscWeakFormSetIndexBdJacobian(wf, faceSetsLabel, faceSetValues[i], 1, 0, 0, 0, g0_bd_pu, 0, NULL, 0, NULL, 0, NULL));
    }
    PetscCall(ISRestoreIndices(valueIS, &faceSetValues));
    PetscCall(ISDestroy(&valueIS));
  } break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)dm), PETSC_ERR_ARG_WRONG, "Unsupported BC type: %s (%d)", BCTypes[PetscMin(user->bc, BC_UNKNOWN)], user->bc);
  }

  /* Make constant values available to pointwise functions */
  {
    Parameter  *param;
    PetscScalar constants[2];

    PetscCall(PetscBagGetData(user->bag, &param));
    constants[0] = param->mu; /* dynamic shear viscosity, Pa s */
    constants[1] = 0.0;       /* Nitsche penalty (set below if needed) */
    if (user->bc == BC_NITSCHE) {
      /* Compute cell size h from mesh */
      PetscInt  dim, cStart;
      PetscReal vol, h;

      PetscCall(DMGetDimension(dm, &dim));
      PetscCall(DMPlexGetHeightStratum(dm, 0, &cStart, NULL));
      PetscCall(DMPlexComputeCellGeometryFVM(dm, cStart, &vol, NULL, NULL));
      h            = PetscPowReal(vol, 1.0 / dim);
      constants[1] = PetscRealPart(param->eta) * PetscRealPart(param->mu) / h;
    }
    PetscCall(PetscDSSetConstants(ds, 2, constants));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode zero(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt c;
  for (c = 0; c < Nc; ++c) u[c] = 0.0;
  return PETSC_SUCCESS;
}
static PetscErrorCode one(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt c;
  for (c = 0; c < Nc; ++c) u[c] = 1.0;
  return PETSC_SUCCESS;
}

static PetscErrorCode CreatePressureNullSpace(DM dm, PetscInt origField, PetscInt field, MatNullSpace *nullspace)
{
  Vec vec;
  PetscErrorCode (*funcs[2])(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *u, PetscCtx ctx) = {zero, one};

  PetscFunctionBeginUser;
  PetscCheck(origField == 1, PetscObjectComm((PetscObject)dm), PETSC_ERR_ARG_WRONG, "Field %" PetscInt_FMT " should be 1 for pressure", origField);
  funcs[field] = one;
  {
    PetscDS ds;
    PetscCall(DMGetDS(dm, &ds));
    PetscCall(PetscObjectViewFromOptions((PetscObject)ds, NULL, "-ds_view"));
  }
  PetscCall(DMCreateGlobalVector(dm, &vec));
  PetscCall(DMProjectFunction(dm, 0.0, funcs, NULL, INSERT_ALL_VALUES, vec));
  PetscCall(VecNormalize(vec, NULL));
  PetscCall(MatNullSpaceCreate(PetscObjectComm((PetscObject)dm), PETSC_FALSE, 1, &vec, nullspace));
  PetscCall(VecDestroy(&vec));
  /* New style for field null spaces */
  {
    PetscObject  pressure;
    MatNullSpace nullspacePres;

    PetscCall(DMGetField(dm, field, NULL, &pressure));
    PetscCall(MatNullSpaceCreate(PetscObjectComm(pressure), PETSC_TRUE, 0, NULL, &nullspacePres));
    PetscCall(PetscObjectCompose(pressure, "nullspace", (PetscObject)nullspacePres));
    PetscCall(MatNullSpaceDestroy(&nullspacePres));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupProblem(DM dm, PetscErrorCode (*setupEqn)(DM, AppCtx *), AppCtx *user)
{
  DM              cdm = dm;
  PetscQuadrature q   = NULL;
  PetscBool       simplex;
  PetscInt        dim, Nf = 2, f, Nc[2];
  const char     *name[2]   = {"velocity", "pressure"};
  const char     *prefix[2] = {"vel_", "pres_"};

  PetscFunctionBegin;
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMPlexIsSimplex(dm, &simplex));
  Nc[0] = dim;
  Nc[1] = 1;
  for (f = 0; f < Nf; ++f) {
    PetscFE fe;

    PetscCall(PetscFECreateDefault(PETSC_COMM_SELF, dim, Nc[f], simplex, prefix[f], -1, &fe));
    PetscCall(PetscObjectSetName((PetscObject)fe, name[f]));
    if (!q) PetscCall(PetscFEGetQuadrature(fe, &q));
    PetscCall(PetscFESetQuadrature(fe, q));
    PetscCall(DMSetField(dm, f, NULL, (PetscObject)fe));
    PetscCall(PetscFEDestroy(&fe));
  }
  PetscCall(DMCreateDS(dm));
  PetscCall((*setupEqn)(dm, user));
  while (cdm) {
    PetscCall(DMCopyDisc(dm, cdm));
    PetscCall(DMSetNullSpaceConstructor(cdm, 1, CreatePressureNullSpace));
    PetscCall(DMGetCoarseDM(cdm, &cdm));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

int main(int argc, char **argv)
{
  SNES   snes;
  DM     dm;
  Vec    u;
  AppCtx user;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(ProcessOptions(PETSC_COMM_WORLD, &user));
  PetscCall(CreateMesh(PETSC_COMM_WORLD, &user, &dm));
  PetscCall(SNESCreate(PetscObjectComm((PetscObject)dm), &snes));
  PetscCall(SNESSetDM(snes, dm));
  PetscCall(DMSetApplicationContext(dm, &user));

  PetscCall(SetupParameters(PETSC_COMM_WORLD, &user));
  PetscCall(SetupProblem(dm, SetupEqn, &user));
  PetscCall(DMPlexCreateClosureIndex(dm, NULL));

  PetscCall(DMCreateGlobalVector(dm, &u));
  PetscCall(DMPlexSetSNESLocalFEM(dm, PETSC_FALSE, &user));
  PetscCall(SNESSetFromOptions(snes));
  PetscCall(DMSNESCheckFromOptions(snes, u));
  PetscCall(PetscObjectSetName((PetscObject)u, "Solution"));
  {
    Mat          J;
    MatNullSpace sp;

    PetscCall(SNESSetUp(snes));
    PetscCall(CreatePressureNullSpace(dm, 1, 1, &sp));
    PetscCall(SNESGetJacobian(snes, &J, NULL, NULL, NULL));
    PetscCall(MatSetNullSpace(J, sp));
    PetscCall(MatNullSpaceDestroy(&sp));
    PetscCall(PetscObjectSetName((PetscObject)J, "Jacobian"));
    PetscCall(MatViewFromOptions(J, NULL, "-J_view"));
  }
  PetscCall(SNESSolve(snes, NULL, u));

  PetscCall(VecDestroy(&u));
  PetscCall(SNESDestroy(&snes));
  PetscCall(DMDestroy(&dm));
  PetscCall(PetscBagDestroy(&user.bag));
  PetscCall(PetscFinalize());
  return 0;
}
```

---

## In-Person Tutorials#

**URL:** https://petsc.org/release/tutorials/in_person/

**Contents:**
- In-Person Tutorials#

Please contact us at mailto:petsc-maint@mcs.anl.gov if you are interested in hosting a tutorial.

SIAM Geosciences 2025 Slides

2025 PETSc Annual Users Meeting and Tutorial

“PETSc with GPUs” at the 2022 CIG Developer’s Workshop (slides and source).

PETSc Tutorial at NASA Langley Research Center, March 2019 (Oana, Barry)

PETSc Tutorial at the ECP Annual Meeting, Jan 2019 (Alp, Hong, Matt, Rich, Todd) Slides1 Slides2 Slides3 Slides4

PETSc Tutorial at Memorial University AARMS Workshop on Scientific Computing Software, May 2017 (Jed) Slides

PETSc Tutorial at the CEMRACS 2016 in Marseille (Matt) Slides Video

PETSc Tutorial at the PETSc-20 anniversary conference and workshop

PETSc Tutorial at IT4I, Ostrava, Czech Republic, May 21-22, 2015 (Jed)

Intro to Parallel Algebraic Solvers using PETSc, UC Merced, Oct 31, 2014 (Jed) Slides

PETSc Tutorial at the SUNY Buffalo, Buffalo, NY, April 22 2014 (Matt and Jed) Slides

PETSc Tutorial at the Imperial College, London, UK, March 19 2014 (Matt) Slides

PETSc Tutorial at the Minnesota Supercomputing Institute, University of Minnesota, Minneapolis MN, September 30 2013 (Matt) Slides

PETSc Tutorial/Implicit Solvers, PRACE Summer School, Ostrava, Czech Republic, June 2013 (Jed) Slides

Advanced PETSc Tutorial, Maison de la Simulation, Orsay, France, June 2013 (Matt) Slides

Tutorial (ViennaCL & PETSc) at FEMTEC 2013 Las Vegas, NV, May 2013 (Karl) Slides

PETSc at the Second National Workshop on High Performance Computing for Scientific Applications (WHPC13), Cordoba, Argentina, May 2013 (Karl) Slides 1, Slides 2, Slides 3, Tutorial code

Tutorial at the 21st High Performance Computing Symposia (HPC’13), San Diego, CA, April 2013 (Karl) Slides

Tutorial at ACTS, Berkeley, CA, August 2012 (Matt) Slides, Hands-On

Advanced PETSc, TACC, Feb 20, 2012 (Jed). Video. Slides.

Tutorial at ICES, UT Austin, TX September 2011 (Matt) Slides

Tutorial at ACTS, Berkeley, CA, August 2011 (Jed) Slides, Video

What’s New in PETSc? from 39th Speedup Conference, ETH Zurich, Switzerland, September 2010

Short course at the Arctic Region Supercomputing Center, Fairbanks Alaska, August 2010 (Jed). Slides.

Short Course at the Graduate University, Chinese Academy of Sciences, Beijing, China, July 2010 (Matt) Slides.

New developments, memory performance, and algorithmic experimentation. at the ninth annual meeting on High Performance Computing and Infrastructure for computational science in Norway (NOTUR), Bergen, May 2010 (Jed)

Short course at the Swiss National Supercomputing Center, Manno, May 2010 (Jed). Slides. Tutorial code

Short Course at the Graduate University, Chinese Academy of Sciences, Beijing, China, July 2009 (Matt) Slides

Tutorial at TACC, Austin, TX, May 2009 (Matt) Slides

Tutorial at TACC, Austin, TX, July 2008 (Matt) Slides

Tutorial at ACTS NERSC, Berkeley, CA, August 2008 (Satish)

ACTS NERSC, Berkeley, CA, August 2007 (Matt) Slides

Parallel CFD, Antalya, Turkey, May 2007 (Matt) Slides

CCT at LSU, Baton Rouge, LA, April 2007 (Hong) Slides

Lorena Barba’s SCAT Summer School, Valparaiso, Chile, January 2007, (Matt) Slides

David Keyes’ Columbia class, New York City, October 2006 (Matt) Slides

ACTS NERSC, Berkeley, CA, August 2006, (Matt) Slides

LCRC PETSc Tutorial, Argonne National Laboratory, August 2006 (Barry)

Scientific Computing Advanced Training Daresbury Laboratory,June 2006, (Barry) Slides

Parallel Implementation of PETSc Finite Element Code, Clemson University, May 2006. (J.K. Houchins) Slides

SIAM Parallel Processing Conference, February 2006, San Francisco(Barry) Slides

Machine Learning Tools Satellite Workshop at the Neural Information Processing Systems, Vancouver, December 2005 (Barry)

5 hour course; ACTS Workshop, NERSC, August 2005 (Matt)

6 hour course; University of Houston, Houston, Texas, April 2005 (Matt)

Whole day course at INL, February 2005, (Matt) Slides

6 hour course, including 3 hours devoted to multigrid and domain decomposition with PETSc. Columbia University, New York City, January 2005, (Barry, Matt, Dinesh, Bill) Slides

2-day PETSc short course in conjunction with the International Parallel CFD 2004 Conference, Gran Canaria, Canary Islands, Spain, May 2004 (Matt, Kris)

At the Workshop on the ACTS Toolkit at NERSC, August 2003 (Bill, David)

At the 15th Annual Domain Decomposition Meeting, Freie Universität Berlin (FUB), July 2003 (Bill, David)

At the Workshop on the ACTS Toolkit at NERSC, September 2002 (Barry, Kris)

3 day tutorial as part of the Parallel Computing Workshop, Center for Computational Science and Engineering, Peking University, Beijing, China, July 1-August 2, 2002, (Bill)

1/2-day PETSc tutorial as part of a Workshop on the ACTS Toolkit at NERSC, October 2001 (Lois, Satish)

2-day PETSc tutorial on the Access Grid, October 2000 (Barry, Satish)

2-day tutorial on PETSc, including its support for domain decomposition and multigrid, Lyon, France, October 2000 (Bill)

1/2-day PETSc tutorial at a Workshop on the ACTS Toolkit at NERSC, September 2000 (Lois, Satish)

1/2-day PETSc short course: Williamsburg, Virginia, in conjunction with the International Parallel CFD 1999 Conference, May 1999 (Lois, Satish, Dinesh)

1-day PETSc short course: San Antonio, Texas, in conjunction with the Ninth SIAM Conference on Parallel Processing for Scientific Computing, March 1999 (Lois, Satish)

Tutorial at Supercomputing ‘97 - 1/2-day November, 1997 (Barry, Lois, Satish)

“Bring Your Own Code” Workshop - 3-day, with lectures and hands-on computer sessions, Cornell Theory Center, April, 1997 (Barry, Lois, Satish)

“Bring Your Own Code” Workshop - 3-day, with lectures and hands-on computer sessions, ICASE, NASA Langley Research Center, December, 1996 (Bill, Barry, Lois, Satish)

Time, Accuracy, Speed Analysis (TAS)

---

## Meshing for Subsurface Flows in PETSc#

**URL:** https://petsc.org/release/tutorials/meshing/guide_to_subsurface/

**Contents:**
- Meshing for Subsurface Flows in PETSc#

This tutorials guides users in creating meshes for the TDyCore simulation framework for subsurface flows. The user inputs a surface mesh, a refinement prescription, and an extrusion prescription in order to create the simulation mesh.

Reading the ASCII Output

For example, a very simple mesh would start with a square surface mesh divided into two triangles, which is then extruded to form two triangular prisms. This is the first test in the DMPlex tutorial code ex10,

We can see that there are two 3-cells, meaning three-dimensional cells, and from the celltype label we see that those cells have celltype 9, meaning they are triangular prisms. The original surface mesh had 5 edges, so we would expect 10 edges for the two surfaces and four edges connecting those surfaces. This is exactly what we see, since there are 14 1-cells, but 4 of them noted in parentheses are tensor cells created by extrusion. We can see this another way in the celltype label, where there are ten mesh points of type 1, meaning segments, and four mesh points of type 2, meaning tensor products of a vertex and segment. Similarly, there are 9 2-cells, but 5 of them stretch between the two surfaces, meaning they are tensor products of two segments.

Regular Refinement of Simplex Meshes

We can regularly refine the surface before extrusion using -dm_refine <k>, where k is the number of refinements,

which produces the following surface

Fig. 31 Surface mesh refined twice#

and the extruded mesh can be visualized using VTK. Here I make the image using Paraview, and give the extrusion 3 layers

Fig. 32 Extruded mesh with refined surface#

We can similarly look at this in parallel. Test 2 uses three refinements and three extrusion layers on five processes

Fig. 33 Parallel extruded mesh with refined surface#

Adaptive Refinement of Simplex Meshes

Adaptive refinement of simplicial meshes is somewhat tricky when we demand that the meshes be conforming, as we do in this case. We would like different grid cells to have different levels of refinement, for example headwaters cells in a watershed be refined twice, while river channel cells be refined four times. In order to differentiate between cells, we first mark the cells on the surface using a DMLabel. We can do this programmatically,

or you can label the mesh using a GUI, such as GMsh, and PETSc will read the label values from the input file.

We next create a label marking each cell in the mesh with an action, such as DM_ADAPT_REFINE or DM_ADAPT_COARSEN. We do this based on a volume constraint, namely that cells with a certain label value should have a certain volume. You could, of course, choose a more complex strategy, but here we just want a clear criterion. We can give volume constraints for label value v using the command line argument -volume_constraint_<v> <vol>. The mesh is then refined iteratively, checking the volume constraints each time,

Test 3 from ex10 constrains the headwater cells (with marker 1) to have volume less than 0.01, and the river channel cells (with marker 2) to be smaller than 0.000625

We can look at a parallel run using extra options for the test system

Fig. 34 Parallel extruded mesh with adaptively refined surface#

By turning on PetscInfo, we can see what decisions the refiner is making

Tutorials, by Mathematical Problem

Time, Accuracy, Speed Analysis (TAS)

**Examples:**

Example 1 (unknown):
```unknown
$ make -f ./gmakefile test search="dm_impls_plex_tutorials-ex10_0"
```

Example 2 (yaml):
```yaml
DM Object: Mesh 1 MPI process
  type: plex
Mesh in 3 dimensions:
  Number of 0-cells per rank: 8
  Number of 1-cells per rank: 14 (4)
  Number of 2-cells per rank: 9 (5)
  Number of 3-cells per rank: 2
Labels:
  celltype: 6 strata with value/size (0 (8), 1 (10), 2 (4), 3 (4), 5 (5), 9 (2))
  depth: 4 strata with value/size (0 (8), 1 (14), 2 (9), 3 (2))
  marker: 1 strata with value/size (1 (24))
  Face Sets: 4 strata with value/size (1 (3), 2 (3), 3 (3), 4 (3))
```

Example 3 (typescript):
```typescript
-dm_refine <k>
```

Example 4 (bash):
```bash
$ make -f ./gmakefile test search="dm_impls_plex_tutorials-ex10_1" EXTRA_OPTIONS="-srf_dm_refine 2 -srf_dm_view draw -draw_save $PETSC_DIR/surface.png -draw_save_single_file"
```

---

## STREAMS: Example Study#

**URL:** https://petsc.org/release/manual/streams/

**Contents:**
- STREAMS: Example Study#
- Detailed STREAMS study for large arrays#
- Detailed study with application#
- Application with the MPI linear solver server#

Most algorithms in PETSc are memory bandwidth limited. The speed of a simulation depends more on the total achievable [1] memory bandwidth of the computer than the speed (or number) of floating point units. The STREAMS benchmark, a key tool in our field, is invaluable for gaining insights into parallel performance (scaling) by measuring achievable memory bandwidth. PETSc contains multiple implementations of the triad STREAMS benchmark: including an OpenMP version and an MPI version.

STREAMS measures the total memory bandwidth achievable when running n independent threads or processes on non-overlapping memory regions of an array of total length N on a shared memory node. The bandwidth is then computed as 3*n*sizeof(double)/min(time[]). The timing is done with MPI_Wtime(). A call to the timer takes less than 3e-08 seconds, significantly smaller than the benchmark time. The STREAMS benchmark is intentionally embarrassingly parallel, that is, each thread or process works on its own data, completely independently of other threads or processes data. Though real simulations have more complex memory access patterns, most computations for PDEs have large sections of private data and share only data along ghost (halo) regions. Thus the completely independent non-overlapping memory STREAMS model still provides useful information.

As more threads or processes are added, the bandwidth achieved begins to saturate at some n, generally less than the number of cores on the node. How quickly the bandwidth saturates, and the speed up (or parallel efficiency) obtained on a given system indicates the likely performance of memory bandwidth-limited computations.

Fig. STREAMS benchmark gcc plots the total memory bandwidth achieved and the speedup for runs on an Intel system whose details are provided below. The achieved bandwidth increases rapidly with more cores initially but then less so as more cores are utilized. Also, note that the improvement may, unintuitively, be non-monotone when adding more cores. This is due to the complex interconnect between the cores and their various levels of caches and how the threads or processes are assigned to cores.

Fig. 16 STREAMS benchmark gcc#

There are three important concepts needed to understand memory bandwidth-limited computing.

Thread or process binding to hardware subsets of the shared memory node. The Unix operating system allows threads and processes to migrate among the cores of a node during a computation. This migration is managed by the operating system (OS). [2] A thread or process that is “near” some data may suddenly be far from the data when the thread or process gets migrated. Binding the thread or process to a hardware unit prevents or limits the migration.

Thread or process mapping (assignment) to hardware subsets when more threads or processes are used. Physical memory is divided into multiple distinct units, each of which can independently provide a certain memory bandwidth. Different cores may be more closely connected to different memory units. This results in non-uniform memory access (NUMA), meaning the memory latency or bandwidth for any particular core depends on the physical address of the requested memory. When increasing from one thread or process to two, one obviously would like the second thread or process to use a different memory unit and not share the same unit with the first thread or process. Mapping each new thread or process to cores that do not share the previously assigned core’s memory unit ensures a higher total achievable bandwidth.

In addition to mapping, one must ensure that each thread or process uses data on the closest memory unit. The OS selects the memory unit to place new pages of virtual memory based on first touch: the core of the first thread or process to touch (read or write to) a memory address determines to which memory unit the page of the data is assigned. This is automatic for multiple processes since only one process (on a particular core) will ever touch its data. For threads, care must be taken that the data a thread is to compute on is first touched by that thread. For example, the performance will suffer if the first thread initializes an entire array that multiple threads will later access. For small data arrays that remain in the cache, first touch may produce no performance difference.

MPI and OpenMP provide ways to bind and map processes and cores. They also provide ways to display the current mapping.

MPI, options to mpiexec

–bind-to hwthread | core | l1cache | l2cache | l3cache | socket | numa | board

–map-by hwthread | core | socket | numa | board | node

–cpu-list list of cores

–cpu-set list of sets of cores

OpenMP, environmental variables

OMP_PROC_BIND=close | spread

OMP_PLACES=”list of sets of cores” for example {0:2},{2:2},{32:2},{34:2}

OMP_DISPLAY_ENV=false | true

OMP_DISPLAY_AFFINITY=false | true

Providing appropriate values may be crucial to high performance; the defaults may produce poor results. The best bindings for the STREAMS benchmark are often the best bindings for large PETSc applications. The Linux commands lscpu and numactl -H provide useful information about the hardware configuration.

It is possible that the MPI initialization (including the use of mpiexec) can change the default OpenMP binding/mapping behavior and thus seriously affect the application runtime. The C and Fortran) examples demonstrate this.

We run ex69f with four OpenMP threads without mpiexec and see almost perfect scaling. The CPU time of the process, which is summed over the four threads in process, is the same as the wall clock time indicating that each thread is run on a different core as desired.

Running under mpiexec gives a very different wall clock time, indicating that all four threads ran on the same core.

If we add some binding/mapping options to mpiexec we obtain

Thus we conclude that this mpiexec implementation is, by default, binding the process (including all of its threads) to a single core. Consider also the mpiexec option --map-by socket:pe=$OMP_NUM_THREADS to ensure each thread gets is own core for computation.

Note that setting OMP_PROC_BIND=spread alone does not resolve the problem, as the output below indicates.

The Fortran routine cpu_time() can sometimes produce misleading results when run with multiple threads. Consider again the Fortran example. For an OpenMP parallel loop with enough available cores and the proper binding of threads to cores, one expects the CPU time for the process to be roughly the number of threads times the wall clock time. However, for a loop that is not parallelized (like the second loop in the Fortran example), the CPU time one would expect would match the wall clock time. However, this may not be the case; for example, we have run the Fortran example on an Intel system with the Intel ifort compiler and observed the recorded CPU for the second loop to be roughly the number of threads times the wall clock time even though only a single thread is computing the loop. Thus, comparing the CPU time to the wall clock time of a computation with OpenMP does not give you a good measure of the speedup produced by OpenMP.

We now present a detailed study of a particular Intel Icelake system, the Intel(R) Xeon(R) Platinum 8362 CPU @ 2.80GH. It has 32 cores on each of two sockets (each with a single NUMA region, so a total of two NUMA regions), a 48 Megabyte L3 cache and 32 1.25 Megabyte L2 caches, each shared by 2 cores. It is running the Rocky Linux 8.8 (Green Obsidian) distribution. The compilers used are GNU 12.2, Intel(R) oneAPI Compiler 2023.0.0 with both icc and icx, and NVIDIA nvhpc/23.1. The MPI implementation is OpenMPI 4.0.7, except for nvhpc, which uses 3.15. The compiler options were

gcc -O3 -march=native

icc -O3 -march=native

icx -O3 -ffinite-math-only (the -xHost option, that replaces -march=native, crashed the compiler so was not used)

nvc -O3 -march=native

We first run the STREAMS benchmark with large double precision arrays of length \(1.6\times10^8\); the size was selected to be large enough to eliminate cache effects. Fig. Comprehensive STREAMS performance on Intel system shows the achieved bandwidth for gcc, icc, icx, and nvc using MPI and OpenMP with their default bindings and with the MPI binding of --bind-to core --map-by numa and the OpenMP binding of spread.

Fig. 17 Comprehensive STREAMS performance on Intel system#

Note the two dips in the performance with OpenMP and gcc using binding in Fig. STREAMS benchmark gcc. Requesting the spread binding produces better results for small core counts but poorer ones for larger ones. These are a result of a bug in the gcc spread option, placing more threads in one NUMA domain than the other. For example, with gcc, the OMP_DISPLAY_AFFINITY shows that for 28 threads, 12 are placed on NUMA region 1, and 16 are placed on the other NUMA region. The other compilers spread the cores evenly.

Fig. STREAMS benchmark icc shows the performance with the icc compiler. Note that the icc compiler produces significantly faster code for the benchmark than the other compilers so its STREAMS speedups are smaller, though it provides better performance. No significant dips occur with the OpenMP binding using icc, icx, and nvc; using OMP_DISPLAY_AFFINITY confirms, for example, that 14 threads (out of 28) are assigned to each NUMA domain, unlike with gcc. Using the exact thread placement that icc uses with gcc using the OpenMP OMP_PLACES option removes most of the dip in the gcc OpenMP binding result. Thus, we conclude that on this system, the spread option does not always give the best thread placement with gcc due to its bug.

Fig. 18 STREAMS benchmark icc#

Fig. STREAMS benchmark icx shows the performance with the icx compiler.

Fig. 19 STREAMS benchmark icx#

Fig. 20 STREAMS benchmark nvc#

To understand the disparity in the STREAMS performance with icc we reran it with the highest optimization level that produced the same results as gcc and icx: -O1 without -march=native. The results are displayed in Fig. STREAMS benchmark icc -O1; sure enough, the results now match that of gcc and icx.

Fig. 21 STREAMS benchmark icc -O1#

Next we display the STREAMS results using gcc with parallel efficiency instead of speedup in STREAMS parallel efficiency gcc

Fig. 22 STREAMS parallel efficiency gcc#

For MPI, the default binding and mapping on this system produces results that are as good as providing a specific binding and mapping. This is not true on many systems!

For OpenMP gcc, the default binding is better than using spread, because spread has a bug. For the other compilers using spread is crucial for good performance on more than 32 cores.

We do not have any explanation why the improvement in speedup for gcc, icx, and nvc slows down between 32 and 48 cores and then improves rapidly since we believe appropriate bindings are being used.

We now present a limited version of the analysis above on an Apple MacBook Pro M2 Max using MPICH, version 4.1, gcc version 13.2 (installed via Homebrew), XCode 15.0.1 and -O3 optimization flags with a smaller N of 80,000,000. macOS contains no public API for setting or controlling affinities so it is not possible to set bindings for either MPI or OpenMP. In addition, the M2 has a combination of performance and efficiency cores which we have no control over the use of.

Fig. STREAMS benchmark on Apple M2 provides the results. Based on the plateau in the middle of the plot, we assume that the core numbering that is used by MPICH does not produce the best binding.

Fig. 23 STREAMS benchmark on Apple M2#

OpenMPI (installed via Homebrew) produced similar results.

We now move on to a PETSc application which solves a three-dimensional Poisson problem on a unit cube discretized with finite differences whose linear system is solved with the PETSc algebraic multigrid preconditioner, PCGAMG and Krylov accelerator GMRES. Strong scaling is used to compare with the STREAMS benchmark: measuring the time to construct the preconditioner, the time to solve the linear system with the preconditioner, and the time for the matrix-vector products. These are displayed in Fig. GAMG speedup. The runtime options were -da_refine 6 -pc_type gamg -log_view. This study did not attempt to tune the default PCGAMG parameters. There were very similar speedups for all the compilers so we only display results for gcc.

Fig. 24 GAMG speedup#

Fig. 25 GAMG parallel efficiency#

The dips in the performance at certain core counts are consistent between compilers and results from the amount of MPI communication required from the communication pattern which results from the different three-dimensional parallel grid layout.

We now present GAMG on the Apple MacBook Pro M2 Max. Fig. GAMG speedup Apple M2 provides the results. The performance is better than predicted by the STREAMS benchmark for all portions of the solver.

Fig. 26 GAMG speedup Apple M2#

We now run the same PETSc application using the MPI linear solver server mode, set using -mpi_linear_solver_server. All compilers deliver largely the same performance so we only present results with gcc. We plot the speedup in Fig. GAMG server speedup and parallel efficiency in GAMG server parallel efficiency Note that it is far below the parallel solve without the server. However, the distribution time for these runs was always less than three percent of the complete solution time. The reason for the poorer performance is because in the pure MPI version, the vectors are partitioned directly from the three-dimensional grid; the cube is divided into (approximate) sub-cubes, this minimizes the inter-process communication, especially in the matrix-vector product. In server mode, the vector is laid out using the cube’s natural ordering, and then each MPI process is assigned a contiguous subset of the vector. As a result, the flop rate for the matrix-vector product is significantly higher than that of the pure MPI version. This indicates that a naive use of the MPI linear solver server will not produce as much performance as a usage that considers the matrix/vector layouts by performing an initial grid partitioning. For example, if OpenMP is used to generate the matrix, it would be appropriate to have each OpenMP thread assigned a contiguous vector mapping to a sub-cube of the domain. This would require, of course, a far more complicated OpenMP code that is written using MPI-like parallelism and decomposition of the data.

PCMPI has two approaches for distributing the linear system. The first uses MPI_Scatterv() to communicate the matrix and vector entries from the initial compute process to all of the server processes. Unfortunately, MPI_Scatterv() does not scale with more MPI processes; hence, the solution time is limited by the MPI_Scatterv(). To remove this limitation, the second communication mechanism is Unix shared memory shmget(). Here, PCMPI allocates shared memory from which all the MPI processes in the server can access their portion of the matrices and vectors that they need. There is still a (now much smaller) server processing overhead since the initial data storage of the sequential matrix (in MATSEQAIJ storage) still must be converted to MATMPIAIJ storage. VecPlaceArray() is used to convert the sequential vector to an MPI vector, so there is no overhead, not even a copy, for this operation.

Fig. 27 GAMG server speedup#

Fig. 28 GAMG server parallel efficiency#

Fig. 29 GAMG server parallel efficiency vs STREAMS#

In GAMG server parallel efficiency vs STREAMS, we plot the parallel efficiency of the linear solve and the STREAMS benchmark, which track each other well. This example demonstrates the utility of the STREAMS benchmark to predict the speedup (parallel efficiency) of a memory bandwidth limited application on a shared memory Linux system.

For the Apple M2, we present the results using Unix shared-memory communication of the matrix and vectors to the server processes in GAMG server solver speedup on Apple M2. To run this one must first set up the machine to use shared memory as described in PetscShmgetAllocateArray()

Fig. 30 GAMG server solver speedup on Apple M2#

This example demonstrates that the MPI linear solver server feature of PETSc can generate a reasonable speedup in the linear solver on machines that have significant memory bandwidth. However, one should not expect the speedup to be near the total number of cores on the compute node.

Achievable memory bandwidth is the actual bandwidth one can obtain as opposed to the theoretical peak that is calculated using the hardware specification.

Data can also be migrated among different memory sockets during a computation by the OS, but we ignore this possibility in the discussion.

Hints for Performance Tuning

The Use of BLAS and LAPACK in PETSc and external libraries

**Examples:**

Example 1 (sass):
```sass
for (int j = 0; j < n; ++j) a[j] = b[j]+scalar*c[j]
```

Example 2 (unknown):
```unknown
3*n*sizeof(double)/min(time[])
```

Example 3 (unknown):
```unknown
MPI_Wtime()
```

Example 4 (sass):
```sass
$ OMP_NUM_THREADS=4  ./ex69f
  CPU time reported by cpu_time()               6.1660000000000006E-002
  Wall clock time reported by system_clock()    1.8335562000000000E-002
  Wall clock time reported by omp_get_wtime()   1.8330062011955306E-002
```

---

## Time, Accuracy, Speed Analysis (TAS)#

**URL:** https://petsc.org/release/tutorials/performance/guide_to_TAS/

**Contents:**
- Time, Accuracy, Speed Analysis (TAS)#

Below is the guide to running TAS using ex13, which is a Poisson Problem in 2D and 3D with Finite Elements:

This example source file, and the corresponding makefile are located in PETSC_DIR/src/snes/tutorials/

Compile with the command:

Run ex13 with the following command:

A log file in the above directory called ex_13_test.py should now be present. This is also the same directory that contains the TAS python3 script petsc_tas_analysis.py

Now run petsc_tas_analysis.py:

You should see something similar to the following in your terminal window:

Finally the graphs will appear in the subdirectory graphs/

See detailed user’s guide

On the command line use ./petsc_tas_analysis.py -h

Meshing for Subsurface Flows in PETSc

**Examples:**

Example 1 (unknown):
```unknown
PETSC_DIR/src/snes/tutorials/
```

Example 2 (unknown):
```unknown
$ make ex13
```

Example 3 (jsx):
```jsx
mpiexec -n 2 ./ex13 -log_view :/home/<user name>/PETSC_DIR/lib/petsc/bin/ex_13_test.py:ascii_info_detail \
  -dm_distribute \
  -dm_plex_box_faces 8,8 \
  -potential_petscspace_degree 1 \
  -snes_convergence_estimate \
  -convest_num_refine 5
```

Example 4 (unknown):
```unknown
ex_13_test.py
```

---

## Tutorials#

**URL:** https://petsc.org/release/tutorials/

**Contents:**
- Tutorials#

This page provides connections to PETSc tutorial examples by type of physics being modeled, discretization technique being used, solvers used, etc.

In addition, PETSc has many additionally poorly curated tutorial examples, found in the tutorials/ directories throughout the PETSc src/ tree.

Least-squares (Manual: Nonlinear Least-Squares)

Quadratic (Manual: Quadratic Solvers)

Unconstrained (Manual: Unconstrained Minimization)

Bound (Manual: Bound-Constrained Optimization)

Constrained (Manual: Generally Constrained Solvers)

Complementarity (Manual: Complementarity)

PDE constrained (Manual: PDE-constrained Optimization)n

Tutorials, by Physics

---

## Tutorials, by Mathematical Problem#

**URL:** https://petsc.org/release/tutorials/handson/

**Contents:**
- Tutorials, by Mathematical Problem#
- Linear elliptic PDE on a 2D grid#
- Nonlinear ODE arising from a time-dependent one-dimensional PDE#
- Nonlinear PDE on a structured grid#
- Nonlinear time dependent PDE on unstructured grid#

TODO: Add link to Python example here

WHAT THIS EXAMPLE DEMONSTRATES:

Using command line options

Handling a simple structured grid

Mathematical description of the problem

Compile src/ksp/ksp/tutorials/ex50.c

Run a 1 processor example with a 3x3 mesh and view the matrix assembled

Run with a 120x120 mesh on 4 processors using superlu_dist and view the solver options used

Run with a 1025x1025 grid using multigrid solver on 4 processors with 9 multigrid levels

WHAT THIS EXAMPLE DEMONSTRATES:

Using command line options

Handling a simple structured grid

Using the ODE integrator

Using call-back functions

Mathematical description of the problem

Compile src/ts/tutorials/ex2.c

Run a 1 processor example on the default grid with all the default solver options

Run with the same options on 4 processors plus monitor convergence of the nonlinear and linear solvers

Run with the same options on 4 processors with 128 grid points

WHAT THIS EXAMPLE DEMONSTRATES:

Handling a 2d structured grid

Using the nonlinear solvers

Changing the default linear solver

Mathematical description of the problem

main program source code

Compile src/snes/tutorials/ex19.c

Run a 4 processor example with 5 levels of grid refinement, monitor the convergence of the nonlinear and linear solver and examine the exact solver used

Run with the same options but use geometric multigrid as the linear solver

Note this requires many fewer iterations than the default solver

Run with the same options but use algebraic multigrid (hypre’s BoomerAMG) as the linear solver

Note this requires many fewer iterations than the default solver but requires more linear solver iterations than geometric multigrid.

Run with the same options but use the ML preconditioner from Trilinos

Run on 1 processor with the default linear solver and profile the run

Search for the line beginning with SNESSolve, the fourth column gives the time for the nonlinear solve.

Run on 1 processor with the geometric multigrid linear solver and profile the run

Compare the runtime for SNESSolve to the case with the default solver

Run on 4 processors with the default linear solver and profile the run

Compare the runtime for SNESSolve to the 1 processor case with the default solver. What is the speedup?

Run on 4 processors with the geometric multigrid linear solver and profile the run

Compare the runtime for SNESSolve to the 1 processor case with multigrid. What is the speedup? Why is the speedup for multigrid lower than the speedup for the default solver?

WHAT THIS EXAMPLE DEMONSTRATES:

Changing the default ODE integrator

Handling unstructured grids

Registering your own interchangeable physics and algorithm modules

Mathematical description of the problem

main program source code

source code of physics modules

Compile src/ts/tutorials/ex11.c

Run simple advection through a tiny hybrid mesh

Run simple advection through a small mesh with a Rosenbrock-W solver

Run simple advection through a larger quadrilateral mesh of an annulus with least squares reconstruction and no limiting, monitoring the error

Compare turning to the error after turning off reconstruction.

Run shallow water on the larger mesh with least squares reconstruction and minmod limiting, monitoring water Height (integral is conserved) and Energy (not conserved)

Tutorials, by Physics

Meshing for Subsurface Flows in PETSc

**Examples:**

Example 1 (unknown):
```unknown
src/ksp/ksp/tutorials/ex50.c
```

Example 2 (unknown):
```unknown
$ cd petsc/src/ksp/ksp/tutorials
$ make ex50
```

Example 3 (unknown):
```unknown
$ mpiexec -n 1 ./ex50  -da_grid_x 4 -da_grid_y 4 -mat_view
```

Example 4 (sass):
```sass
Mat Object: 1 MPI process
  type: seqaij
row 0: (0, 0.)  (1, 0.)  (4, 0.) 
row 1: (0, 0.)  (1, 0.)  (2, 0.)  (5, 0.) 
row 2: (1, 0.)  (2, 0.)  (3, 0.)  (6, 0.) 
row 3: (2, 0.)  (3, 0.)  (7, 0.) 
row 4: (0, 0.)  (4, 0.)  (5, 0.)  (8, 0.) 
row 5: (1, 0.)  (4, 0.)  (5, 0.)  (6, 0.)  (9, 0.) 
row 6: (2, 0.)  (5, 0.)  (6, 0.)  (7, 0.)  (10, 0.) 
row 7: (3, 0.)  (6, 0.)  (7, 0.)  (11, 0.) 
row 8: (4, 0.)  (8, 0.)  (9, 0.)  (12, 0.) 
row 9: (5, 0.)  (8, 0.)  (9, 0.)  (10, 0.)  (13, 0.) 
row 10: (6, 0.)  (9, 0.)  (10, 0.)  (11, 0.)  (14, 0.) 
row 11: (7, 0.)  (10, 0.)  (11, 0.)  (15, 0.) 
row 12: (8, 0.)  (12, 0.)  (13, 0.) 
row 13: (9, 0.)  (12, 0.)  (13, 0.)  (14, 0.) 
row 14: (10, 0.)  (13, 0.)  (14, 0.)  (15, 0.) 
row 15: (11, 0.)  (14, 0.)  (15, 0.) 
Mat Object: 1 MPI process
  type: seqaij
row 0: (0, 2.)  (1, -1.)  (4, -1.) 
row 1: (0, -1.)  (1, 3.)  (2, -1.)  (5, -1.) 
row 2: (1, -1.)  (2, 3.)  (3, -1.)  (6, -1.) 
row 3: (2, -1.)  (3, 2.)  (7, -1.) 
row 4: (0, -1.)  (4, 3.)  (5, -1.)  (8, -1.) 
row 5: (1, -1.)  (4, -1.)  (5, 4.)  (6, -1.)  (9, -1.) 
row 6: (2, -1.)  (5, -1.)  (6, 4.)  (7, -1.)  (10, -1.) 
row 7: (3, -1.)  (6, -1.)  (7, 3.)  (11, -1.) 
row 8: (4, -1.)  (8, 3.)  (9, -1.)  (12, -1.) 
row 9: (5, -1.)  (8, -1.)  (9, 4.)  (10, -1.)  (13, -1.) 
row 10: (6, -1.)  (9, -1.)  (10, 4.)  (11, -1.)  (14, -1.) 
row 11: (7, -1.)  (10, -1.)  (11, 3.)  (15, -1.) 
row 12: (8, -1.)  (12, 2.)  (13, -1.) 
row 13: (9, -1.)  (12, -1.)  (13, 3.)  (14, -1.) 
row 14: (10, -1.)  (13, -1.)  (14, 3.)  (15, -1.) 
row 15: (11, -1.)  (14, -1.)  (15, 2.)
```

---

## Tutorials, by Physics#

**URL:** https://petsc.org/release/tutorials/guide_to_examples_by_physics/

**Contents:**
- Tutorials, by Physics#
- Poisson#
- Elastostatics#
- Stokes#
- Euler#
- Heat equation#
- Navier-Stokes#

Below we list examples which simulate particular physics problems so that users interested in a particular set of governing equations can easily locate a relevant example. Often PETSc will have several examples looking at the same physics using different numerical tools, such as different discretizations, meshing strategy, closure model, or parameter regime.

is used to model electrostatics, steady-state diffusion, and other physical processes. Many PETSc examples solve this equation.

The equation for elastostatics balances body forces against stresses in the body

where \(\bm\sigma\) is the stress tensor. Linear, isotropic elasticity governing infinitesimal strains has the particular stress-strain relation

where the strain tensor \(\bm \varepsilon\) is given by

where \(\bm u\) is the infinitesimal displacement of the body. The resulting discretizations use PETSc’s nonlinear solvers

If we allow finite strains in the body, we can express the stress-strain relation in terms of the Jacobian of the deformation gradient

and the right Cauchy-Green deformation tensor

In the example everything is expressed in terms of determinants and cofactors of \(F\).

Guide to the Stokes Equations using Finite Elements

The time-dependent heat equation

is used to model heat flow, time-dependent diffusion, and other physical processes.

The time-dependent incompressible Navier-Stokes equations

are appropriate for flow of an incompressible fluid at low to moderate Reynolds number.

Tutorials, by Mathematical Problem

---
