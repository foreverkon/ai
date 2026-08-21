# Official tutorial source patterns

These C listings are the examples directly linked by the official tutorials-by-mathematical-problem and tutorials-by-physics guides. Use them as workflow patterns, then verify each API contract in the matching manual-page reference.

## KSP ex50.c

- Selected by: Tutorials by mathematical problem
- Rendered listing: <https://petsc.org/release/src/ksp/ksp/tutorials/ex50.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/ksp/ksp/tutorials/ex50.c>

````c
/*   DMDA/KSP solving a system of linear equations.
     Poisson equation in 2D:

     div(grad p) = f,  0 < x,y < 1
     with
       forcing function f = -cos(m*pi*x)*cos(n*pi*y),
       Neumann boundary conditions
        dp/dx = 0 for x = 0, x = 1.
        dp/dy = 0 for y = 0, y = 1.

     Contributed by Michael Boghosian <boghmic@iit.edu>, 2008,
         based on petsc/src/ksp/ksp/tutorials/ex29.c and ex32.c

     Compare to ex66.c

     Example of Usage:
          ./ex50 -da_grid_x 3 -da_grid_y 3 -pc_type mg -da_refine 3 -ksp_monitor -ksp_view -dm_view draw -draw_pause -1
          ./ex50 -da_grid_x 100 -da_grid_y 100 -pc_type mg  -pc_mg_levels 1 -mg_levels_0_pc_type ilu -mg_levels_0_pc_factor_levels 1 -ksp_monitor -ksp_view
          ./ex50 -da_grid_x 100 -da_grid_y 100 -pc_type mg -pc_mg_levels 1 -mg_levels_0_pc_type lu -mg_levels_0_pc_factor_shift_type NONZERO -ksp_monitor
          mpiexec -n 4 ./ex50 -da_grid_x 3 -da_grid_y 3 -pc_type mg -da_refine 10 -ksp_monitor -ksp_view -log_view
*/

static char help[] = "Solves 2D Poisson equation using multigrid.\n\n";

#include <petscdm.h>
#include <petscdmda.h>
#include <petscksp.h>
#include <petscsys.h>
#include <petscvec.h>

extern PetscErrorCode ComputeJacobian(KSP, Mat, Mat, void *);
extern PetscErrorCode ComputeRHS(KSP, Vec, void *);

typedef struct {
  PetscScalar uu, tt;
} UserContext;

int main(int argc, char **argv)
{
  KSP         ksp;
  DM          da;
  UserContext user;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(KSPCreate(PETSC_COMM_WORLD, &ksp));
  PetscCall(DMDACreate2d(PETSC_COMM_WORLD, DM_BOUNDARY_NONE, DM_BOUNDARY_NONE, DMDA_STENCIL_STAR, 11, 11, PETSC_DECIDE, PETSC_DECIDE, 1, 1, NULL, NULL, &da));
  PetscCall(DMSetFromOptions(da));
  PetscCall(DMSetUp(da));
  PetscCall(KSPSetDM(ksp, (DM)da));
  PetscCall(DMSetApplicationContext(da, &user));

  user.uu = 1.0;
  user.tt = 1.0;

  PetscCall(KSPSetComputeRHS(ksp, ComputeRHS, &user));
  PetscCall(KSPSetComputeOperators(ksp, ComputeJacobian, &user));
  PetscCall(KSPSetFromOptions(ksp));
  PetscCall(KSPSolve(ksp, NULL, NULL));

  PetscCall(DMDestroy(&da));
  PetscCall(KSPDestroy(&ksp));
  PetscCall(PetscFinalize());
  return 0;
}

PetscErrorCode ComputeRHS(KSP ksp, Vec b, PetscCtx ctx)
{
  UserContext  *user = (UserContext *)ctx;
  PetscInt      i, j, M, N, xm, ym, xs, ys;
  PetscScalar   Hx, Hy, pi, uu, tt;
  PetscScalar **array;
  DM            da;
  MatNullSpace  nullspace;

  PetscFunctionBeginUser;
  PetscCall(KSPGetDM(ksp, &da));
  PetscCall(DMDAGetInfo(da, 0, &M, &N, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0));
  uu = user->uu;
  tt = user->tt;
  pi = 4 * atan(1.0);
  Hx = 1.0 / (PetscReal)M;
  Hy = 1.0 / (PetscReal)N;

  PetscCall(DMDAGetCorners(da, &xs, &ys, 0, &xm, &ym, 0)); /* Fine grid */
  PetscCall(DMDAVecGetArray(da, b, &array));
  for (j = ys; j < ys + ym; j++) {
    for (i = xs; i < xs + xm; i++) array[j][i] = -PetscCosScalar(uu * pi * ((PetscReal)i + 0.5) * Hx) * PetscCosScalar(tt * pi * ((PetscReal)j + 0.5) * Hy) * Hx * Hy;
  }
  PetscCall(DMDAVecRestoreArray(da, b, &array));
  PetscCall(VecAssemblyBegin(b));
  PetscCall(VecAssemblyEnd(b));

  /* force right-hand side to be consistent for singular matrix */
  /* note this is really a hack, normally the model would provide you with a consistent right handside */
  PetscCall(MatNullSpaceCreate(PETSC_COMM_WORLD, PETSC_TRUE, 0, 0, &nullspace));
  PetscCall(MatNullSpaceRemove(nullspace, b));
  PetscCall(MatNullSpaceDestroy(&nullspace));
  PetscFunctionReturn(PETSC_SUCCESS);
}

PetscErrorCode ComputeJacobian(KSP ksp, Mat J, Mat jac, PetscCtx ctx)
{
  PetscInt     i, j, M, N, xm, ym, xs, ys, num, numi, numj;
  PetscScalar  v[5], Hx, Hy, HydHx, HxdHy;
  MatStencil   row, col[5];
  DM           da;
  MatNullSpace nullspace;

  PetscFunctionBeginUser;
  PetscCall(KSPGetDM(ksp, &da));
  PetscCall(DMDAGetInfo(da, 0, &M, &N, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0));
  Hx    = 1.0 / (PetscReal)M;
  Hy    = 1.0 / (PetscReal)N;
  HxdHy = Hx / Hy;
  HydHx = Hy / Hx;
  PetscCall(DMDAGetCorners(da, &xs, &ys, 0, &xm, &ym, 0));
  for (j = ys; j < ys + ym; j++) {
    for (i = xs; i < xs + xm; i++) {
      row.i = i;
      row.j = j;

      if (i == 0 || j == 0 || i == M - 1 || j == N - 1) {
        num  = 0;
        numi = 0;
        numj = 0;
        if (j != 0) {
          v[num]     = -HxdHy;
          col[num].i = i;
          col[num].j = j - 1;
          num++;
          numj++;
        }
        if (i != 0) {
          v[num]     = -HydHx;
          col[num].i = i - 1;
          col[num].j = j;
          num++;
          numi++;
        }
        if (i != M - 1) {
          v[num]     = -HydHx;
          col[num].i = i + 1;
          col[num].j = j;
          num++;
          numi++;
        }
        if (j != N - 1) {
          v[num]     = -HxdHy;
          col[num].i = i;
          col[num].j = j + 1;
          num++;
          numj++;
        }
        v[num]     = (PetscReal)numj * HxdHy + (PetscReal)numi * HydHx;
        col[num].i = i;
        col[num].j = j;
        num++;
        PetscCall(MatSetValuesStencil(jac, 1, &row, num, col, v, INSERT_VALUES));
      } else {
        v[0]     = -HxdHy;
        col[0].i = i;
        col[0].j = j - 1;
        v[1]     = -HydHx;
        col[1].i = i - 1;
        col[1].j = j;
        v[2]     = 2.0 * (HxdHy + HydHx);
        col[2].i = i;
        col[2].j = j;
        v[3]     = -HydHx;
        col[3].i = i + 1;
        col[3].j = j;
        v[4]     = -HxdHy;
        col[4].i = i;
        col[4].j = j + 1;
        PetscCall(MatSetValuesStencil(jac, 1, &row, 5, col, v, INSERT_VALUES));
      }
    }
  }
  PetscCall(MatAssemblyBegin(jac, MAT_FINAL_ASSEMBLY));
  PetscCall(MatAssemblyEnd(jac, MAT_FINAL_ASSEMBLY));

  PetscCall(MatNullSpaceCreate(PETSC_COMM_WORLD, PETSC_TRUE, 0, 0, &nullspace));
  PetscCall(MatSetNullSpace(J, nullspace));
  PetscCall(MatNullSpaceDestroy(&nullspace));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/*TEST

   build:
      requires: !complex !single

   test:
      args: -pc_type mg -pc_mg_type full -ksp_type cg -ksp_monitor_short -da_refine 3 -mg_coarse_pc_type svd -ksp_view

   test:
      suffix: 2
      nsize: 4
      args: -pc_type mg -pc_mg_type full -ksp_type cg -ksp_monitor_short -da_refine 3 -mg_coarse_pc_type redundant -mg_coarse_redundant_pc_type svd -ksp_view

   test:
      suffix: 3
      nsize: 2
      args: -pc_type mg -pc_mg_type full -ksp_monitor_short -da_refine 5 -mg_coarse_ksp_type cg -mg_coarse_ksp_converged_reason -mg_coarse_ksp_rtol 1e-2 -mg_coarse_ksp_max_it 5 -mg_coarse_pc_type none -pc_mg_levels 2 -ksp_type pipefgmres -ksp_pipefgmres_shift 1.5

   test:
      suffix: tut_1
      nsize: 1
      args: -da_grid_x 4 -da_grid_y 4 -mat_view

   test:
      suffix: tut_2
      requires: superlu_dist parmetis
      nsize: 4
      args: -da_grid_x 120 -da_grid_y 120 -pc_type lu -pc_factor_mat_solver_type superlu_dist -ksp_monitor -ksp_view

   test:
      suffix: tut_3
      nsize: 4
      args: -da_grid_x 1025 -da_grid_y 1025 -pc_type mg -pc_mg_levels 9 -ksp_monitor

TEST*/
````

## SNES ex19.c

- Selected by: Tutorials by mathematical problem
- Rendered listing: <https://petsc.org/release/src/snes/tutorials/ex19.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/snes/tutorials/ex19.c>

````c
/* Portions of this code are under:
   Copyright (C) 2022 Advanced Micro Devices, Inc. All rights reserved.
*/
static char help[] = "Nonlinear driven cavity with multigrid in 2d.\n \
  \n\
The 2D driven cavity problem is solved in a velocity-vorticity formulation.\n\
The flow can be driven with the lid or with buoyancy or both:\n\
  -lidvelocity &ltlid&gt, where &ltlid&gt = dimensionless velocity of lid\n\
  -grashof &ltgr&gt, where &ltgr&gt = dimensionless temperature gradent\n\
  -prandtl &ltpr&gt, where &ltpr&gt = dimensionless thermal/momentum diffusity ratio\n\
 -contours : draw contour plots of solution\n\n";
/* in HTML, '&lt' = '<' and '&gt' = '>' */

/*
      See src/ksp/ksp/tutorials/ex45.c
*/

/*F-----------------------------------------------------------------------

    We thank David E. Keyes for contributing the driven cavity discretization within this example code.

    This problem is modeled by the partial differential equation system

\begin{eqnarray}
        - \triangle U - \nabla_y \Omega & = & 0  \\
        - \triangle V + \nabla_x\Omega & = & 0  \\
        - \triangle \Omega + \nabla \cdot ([U*\Omega,V*\Omega]) - GR* \nabla_x T & = & 0  \\
        - \triangle T + PR* \nabla \cdot ([U*T,V*T]) & = & 0
\end{eqnarray}

    in the unit square, which is uniformly discretized in each of x and y in this simple encoding.

    No-slip, rigid-wall Dirichlet conditions are used for $ [U,V]$.
    Dirichlet conditions are used for Omega, based on the definition of
    vorticity: $ \Omega = - \nabla_y U + \nabla_x V$, where along each
    constant coordinate boundary, the tangential derivative is zero.
    Dirichlet conditions are used for T on the left and right walls,
    and insulation homogeneous Neumann conditions are used for T on
    the top and bottom walls.

    A finite difference approximation with the usual 5-point stencil
    is used to discretize the boundary value problem to obtain a
    nonlinear system of equations.  Upwinding is used for the divergence
    (convective) terms and central for the gradient (source) terms.

    The Jacobian can be either
      * formed via finite differencing using coloring (the default), or
      * applied matrix-free via the option -snes_mf
        (for larger grid problems this variant may not converge
        without a preconditioner due to ill-conditioning).

  ------------------------------------------------------------------------F*/

/*
   Include "petscdmda.h" so that we can use distributed arrays (DMDAs).
   Include "petscsnes.h" so that we can use SNES solvers.  Note that this
   file automatically includes:
     petscsys.h       - base PETSc routines   petscvec.h - vectors
     petscmat.h - matrices
     petscis.h     - index sets            petscksp.h - Krylov subspace methods
     petscviewer.h - viewers               petscpc.h  - preconditioners
     petscksp.h   - linear solvers
*/
#if defined(PETSC_APPLE_FRAMEWORK)
  #import <PETSc/petscsnes.h>
  #import <PETSc/petscdmda.h>
#else
#include <petscsnes.h>
#include <petscdm.h>
#include <petscdmda.h>
#endif

/*
   User-defined routines and data structures
*/
typedef struct {
  PetscScalar u, v, omega, temp;
} Field;

PetscErrorCode FormFunctionLocal(DMDALocalInfo *, Field **, Field **, void *);

typedef struct {
  PetscReal lidvelocity, prandtl, grashof; /* physical parameters */
  PetscBool draw_contours;                 /* flag - 1 indicates drawing contours */
} AppCtx;

extern PetscErrorCode FormInitialGuess(AppCtx *, DM, Vec);
extern PetscErrorCode NonlinearGS(SNES, Vec, Vec, void *);

int main(int argc, char **argv)
{
  AppCtx   user; /* user-defined work context */
  PetscInt mx, my, its;
  MPI_Comm comm;
  SNES     snes;
  DM       da;
  Vec      x;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  comm = PETSC_COMM_WORLD;
  PetscCall(SNESCreate(comm, &snes));

  /*
      Create distributed array object to manage parallel grid and vectors
      for principal unknowns (x) and governing residuals (f)
  */
  PetscCall(DMDACreate2d(PETSC_COMM_WORLD, DM_BOUNDARY_NONE, DM_BOUNDARY_NONE, DMDA_STENCIL_STAR, 4, 4, PETSC_DECIDE, PETSC_DECIDE, 4, 1, 0, 0, &da));
  PetscCall(DMSetFromOptions(da));
  PetscCall(DMSetUp(da));
  PetscCall(SNESSetDM(snes, da));
  PetscCall(SNESSetNGS(snes, NonlinearGS, (void *)&user));

  PetscCall(DMDAGetInfo(da, 0, &mx, &my, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE));
  /*
     Problem parameters (velocity of lid, prandtl, and grashof numbers)
  */
  user.lidvelocity = 1.0 / (mx * my);
  user.prandtl     = 1.0;
  user.grashof     = 1.0;

  PetscCall(PetscOptionsGetReal(NULL, NULL, "-lidvelocity", &user.lidvelocity, NULL));
  PetscCall(PetscOptionsGetReal(NULL, NULL, "-prandtl", &user.prandtl, NULL));
  PetscCall(PetscOptionsGetReal(NULL, NULL, "-grashof", &user.grashof, NULL));
  PetscCall(PetscOptionsHasName(NULL, NULL, "-contours", &user.draw_contours));

  PetscCall(DMDASetFieldName(da, 0, "x_velocity"));
  PetscCall(DMDASetFieldName(da, 1, "y_velocity"));
  PetscCall(DMDASetFieldName(da, 2, "Omega"));
  PetscCall(DMDASetFieldName(da, 3, "temperature"));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create user context, set problem data, create vector data structures.
     Also, compute the initial guess.
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create nonlinear solver context

     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(DMSetApplicationContext(da, &user));
  PetscCall(DMDASNESSetFunctionLocal(da, INSERT_VALUES, (DMDASNESFunctionFn *)FormFunctionLocal, &user));
  PetscCall(SNESSetFromOptions(snes));
  PetscCall(PetscPrintf(comm, "lid velocity = %g, prandtl # = %g, grashof # = %g\n", (double)user.lidvelocity, (double)user.prandtl, (double)user.grashof));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Solve the nonlinear system
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(DMCreateGlobalVector(da, &x));
  PetscCall(FormInitialGuess(&user, da, x));

  PetscCall(SNESSolve(snes, NULL, x));

  PetscCall(SNESGetIterationNumber(snes, &its));
  PetscCall(PetscPrintf(comm, "Number of SNES iterations = %" PetscInt_FMT "\n", its));

  /*
     Visualize solution
  */
  if (user.draw_contours) PetscCall(VecView(x, PETSC_VIEWER_DRAW_WORLD));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Free work space.  All PETSc objects should be destroyed when they
     are no longer needed.
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(VecDestroy(&x));
  PetscCall(DMDestroy(&da));
  PetscCall(SNESDestroy(&snes));
  PetscCall(PetscFinalize());
  return 0;
}

/* ------------------------------------------------------------------- */

/*
   FormInitialGuess - Forms initial approximation.

   Input Parameters:
   user - user-defined application context
   X - vector

   Output Parameter:
   X - vector
*/
PetscErrorCode FormInitialGuess(AppCtx *user, DM da, Vec X)
{
  PetscInt  i, j, mx, xs, ys, xm, ym;
  PetscReal grashof, dx;
  Field   **x;

  PetscFunctionBeginUser;
  grashof = user->grashof;

  PetscCall(DMDAGetInfo(da, 0, &mx, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0));
  dx = 1.0 / (mx - 1);

  /*
     Get local grid boundaries (for 2-dimensional DMDA):
       xs, ys   - starting grid indices (no ghost points)
       xm, ym   - widths of local grid (no ghost points)
  */
  PetscCall(DMDAGetCorners(da, &xs, &ys, NULL, &xm, &ym, NULL));

  /*
     Get a pointer to vector data.
       - For default PETSc vectors, VecGetArray() returns a pointer to
         the data array.  Otherwise, the routine is implementation dependent.
       - You MUST call VecRestoreArray() when you no longer need access to
         the array.
  */
  PetscCall(DMDAVecGetArrayWrite(da, X, &x));

  /*
     Compute initial guess over the locally owned part of the grid
     Initial condition is motionless fluid and equilibrium temperature
  */
  for (j = ys; j < ys + ym; j++) {
    for (i = xs; i < xs + xm; i++) {
      x[j][i].u     = 0.0;
      x[j][i].v     = 0.0;
      x[j][i].omega = 0.0;
      x[j][i].temp  = (grashof > 0) * i * dx;
    }
  }

  /*
     Restore vector
  */
  PetscCall(DMDAVecRestoreArrayWrite(da, X, &x));
  PetscFunctionReturn(PETSC_SUCCESS);
}

PetscErrorCode FormFunctionLocal(DMDALocalInfo *info, Field **x, Field **f, void *ptr)
{
  AppCtx     *user = (AppCtx *)ptr;
  PetscInt    xints, xinte, yints, yinte, i, j;
  PetscReal   hx, hy, dhx, dhy, hxdhy, hydhx;
  PetscReal   grashof, prandtl, lid;
  PetscScalar u, uxx, uyy, vx, vy, avx, avy, vxp, vxm, vyp, vym;

  PetscFunctionBeginUser;
  grashof = user->grashof;
  prandtl = user->prandtl;
  lid     = user->lidvelocity;

  /*
     Define mesh intervals ratios for uniform grid.

     Note: FD formulae below are normalized by multiplying through by
     local volume element (i.e. hx*hy) to obtain coefficients O(1) in two dimensions.

  */
  dhx   = (PetscReal)(info->mx - 1);
  dhy   = (PetscReal)(info->my - 1);
  hx    = 1.0 / dhx;
  hy    = 1.0 / dhy;
  hxdhy = hx * dhy;
  hydhx = hy * dhx;

  xints = info->xs;
  xinte = info->xs + info->xm;
  yints = info->ys;
  yinte = info->ys + info->ym;

  /* Test whether we are on the bottom edge of the global array */
  if (yints == 0) {
    j     = 0;
    yints = yints + 1;
    /* bottom edge */
    for (i = info->xs; i < info->xs + info->xm; i++) {
      f[j][i].u     = x[j][i].u;
      f[j][i].v     = x[j][i].v;
      f[j][i].omega = x[j][i].omega + (x[j + 1][i].u - x[j][i].u) * dhy;
      f[j][i].temp  = x[j][i].temp - x[j + 1][i].temp;
    }
  }

  /* Test whether we are on the top edge of the global array */
  if (yinte == info->my) {
    j     = info->my - 1;
    yinte = yinte - 1;
    /* top edge */
    for (i = info->xs; i < info->xs + info->xm; i++) {
      f[j][i].u     = x[j][i].u - lid;
      f[j][i].v     = x[j][i].v;
      f[j][i].omega = x[j][i].omega + (x[j][i].u - x[j - 1][i].u) * dhy;
      f[j][i].temp  = x[j][i].temp - x[j - 1][i].temp;
    }
  }

  /* Test whether we are on the left edge of the global array */
  if (xints == 0) {
    i     = 0;
    xints = xints + 1;
    /* left edge */
    for (j = info->ys; j < info->ys + info->ym; j++) {
      f[j][i].u     = x[j][i].u;
      f[j][i].v     = x[j][i].v;
      f[j][i].omega = x[j][i].omega - (x[j][i + 1].v - x[j][i].v) * dhx;
      f[j][i].temp  = x[j][i].temp;
    }
  }

  /* Test whether we are on the right edge of the global array */
  if (xinte == info->mx) {
    i     = info->mx - 1;
    xinte = xinte - 1;
    /* right edge */
    for (j = info->ys; j < info->ys + info->ym; j++) {
      f[j][i].u     = x[j][i].u;
      f[j][i].v     = x[j][i].v;
      f[j][i].omega = x[j][i].omega - (x[j][i].v - x[j][i - 1].v) * dhx;
      f[j][i].temp  = x[j][i].temp - (PetscReal)(grashof > 0);
    }
  }

  /* Compute over the interior points */
  for (j = yints; j < yinte; j++) {
    for (i = xints; i < xinte; i++) {
      /*
       convective coefficients for upwinding
      */
      vx  = x[j][i].u;
      avx = PetscAbsScalar(vx);
      vxp = .5 * (vx + avx);
      vxm = .5 * (vx - avx);
      vy  = x[j][i].v;
      avy = PetscAbsScalar(vy);
      vyp = .5 * (vy + avy);
      vym = .5 * (vy - avy);

      /* U velocity */
      u         = x[j][i].u;
      uxx       = (2.0 * u - x[j][i - 1].u - x[j][i + 1].u) * hydhx;
      uyy       = (2.0 * u - x[j - 1][i].u - x[j + 1][i].u) * hxdhy;
      f[j][i].u = uxx + uyy - .5 * (x[j + 1][i].omega - x[j - 1][i].omega) * hx;

      /* V velocity */
      u         = x[j][i].v;
      uxx       = (2.0 * u - x[j][i - 1].v - x[j][i + 1].v) * hydhx;
      uyy       = (2.0 * u - x[j - 1][i].v - x[j + 1][i].v) * hxdhy;
      f[j][i].v = uxx + uyy + .5 * (x[j][i + 1].omega - x[j][i - 1].omega) * hy;

      /* Omega */
      u             = x[j][i].omega;
      uxx           = (2.0 * u - x[j][i - 1].omega - x[j][i + 1].omega) * hydhx;
      uyy           = (2.0 * u - x[j - 1][i].omega - x[j + 1][i].omega) * hxdhy;
      f[j][i].omega = uxx + uyy + (vxp * (u - x[j][i - 1].omega) + vxm * (x[j][i + 1].omega - u)) * hy + (vyp * (u - x[j - 1][i].omega) + vym * (x[j + 1][i].omega - u)) * hx - .5 * grashof * (x[j][i + 1].temp - x[j][i - 1].temp) * hy;

      /* Temperature */
      u            = x[j][i].temp;
      uxx          = (2.0 * u - x[j][i - 1].temp - x[j][i + 1].temp) * hydhx;
      uyy          = (2.0 * u - x[j - 1][i].temp - x[j + 1][i].temp) * hxdhy;
      f[j][i].temp = uxx + uyy + prandtl * ((vxp * (u - x[j][i - 1].temp) + vxm * (x[j][i + 1].temp - u)) * hy + (vyp * (u - x[j - 1][i].temp) + vym * (x[j + 1][i].temp - u)) * hx);
    }
  }

  /*
     Flop count (multiply-adds are counted as 2 operations)
  */
  PetscCall(PetscLogFlops(84.0 * info->ym * info->xm));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/*
    Performs sweeps of point block nonlinear Gauss-Seidel on all the local grid points
*/
PetscErrorCode NonlinearGS(SNES snes, Vec X, Vec B, PetscCtx ctx)
{
  DMDALocalInfo info;
  Field       **x, **b;
  Vec           localX, localB;
  DM            da;
  PetscInt      xints, xinte, yints, yinte, i, j, k, l;
  PetscInt      max_its, tot_its;
  PetscInt      sweeps;
  PetscReal     rtol, atol, stol;
  PetscReal     hx, hy, dhx, dhy, hxdhy, hydhx;
  PetscReal     grashof, prandtl, lid;
  PetscScalar   u, uxx, uyy, vx, vy, avx, avy, vxp, vxm, vyp, vym;
  PetscScalar   fu, fv, fomega, ftemp;
  PetscScalar   dfudu;
  PetscScalar   dfvdv;
  PetscScalar   dfodu, dfodv, dfodo;
  PetscScalar   dftdu, dftdv, dftdt;
  PetscScalar   yu = 0, yv = 0, yo = 0, yt = 0;
  PetscScalar   bjiu, bjiv, bjiomega, bjitemp;
  PetscBool     ptconverged;
  PetscReal     pfnorm, pfnorm0, pynorm, pxnorm;
  AppCtx       *user = (AppCtx *)ctx;

  PetscFunctionBeginUser;
  grashof = user->grashof;
  prandtl = user->prandtl;
  lid     = user->lidvelocity;
  tot_its = 0;
  PetscCall(SNESNGSGetTolerances(snes, &rtol, &atol, &stol, &max_its));
  PetscCall(SNESNGSGetSweeps(snes, &sweeps));
  PetscCall(SNESGetDM(snes, &da));
  PetscCall(DMGetLocalVector(da, &localX));
  if (B) PetscCall(DMGetLocalVector(da, &localB));
  /*
     Scatter ghost points to local vector, using the 2-step process
        DMGlobalToLocalBegin(), DMGlobalToLocalEnd().
  */
  PetscCall(DMGlobalToLocalBegin(da, X, INSERT_VALUES, localX));
  PetscCall(DMGlobalToLocalEnd(da, X, INSERT_VALUES, localX));
  if (B) {
    PetscCall(DMGlobalToLocalBegin(da, B, INSERT_VALUES, localB));
    PetscCall(DMGlobalToLocalEnd(da, B, INSERT_VALUES, localB));
  }
  PetscCall(DMDAGetLocalInfo(da, &info));
  PetscCall(DMDAVecGetArrayWrite(da, localX, &x));
  if (B) PetscCall(DMDAVecGetArrayRead(da, localB, &b));
  /* looks like a combination of the formfunction / formjacobian routines */
  dhx   = (PetscReal)(info.mx - 1);
  dhy   = (PetscReal)(info.my - 1);
  hx    = 1.0 / dhx;
  hy    = 1.0 / dhy;
  hxdhy = hx * dhy;
  hydhx = hy * dhx;

  xints = info.xs;
  xinte = info.xs + info.xm;
  yints = info.ys;
  yinte = info.ys + info.ym;

  /* Set the boundary conditions on the momentum equations */
  /* Test whether we are on the bottom edge of the global array */
  if (yints == 0) {
    j = 0;
    /* bottom edge */
    for (i = info.xs; i < info.xs + info.xm; i++) {
      if (B) {
        bjiu = b[j][i].u;
        bjiv = b[j][i].v;
      } else {
        bjiu = 0.0;
        bjiv = 0.0;
      }
      x[j][i].u = 0.0 + bjiu;
      x[j][i].v = 0.0 + bjiv;
    }
  }

  /* Test whether we are on the top edge of the global array */
  if (yinte == info.my) {
    j = info.my - 1;
    /* top edge */
    for (i = info.xs; i < info.xs + info.xm; i++) {
      if (B) {
        bjiu = b[j][i].u;
        bjiv = b[j][i].v;
      } else {
        bjiu = 0.0;
        bjiv = 0.0;
      }
      x[j][i].u = lid + bjiu;
      x[j][i].v = bjiv;
    }
  }

  /* Test whether we are on the left edge of the global array */
  if (xints == 0) {
    i = 0;
    /* left edge */
    for (j = info.ys; j < info.ys + info.ym; j++) {
      if (B) {
        bjiu = b[j][i].u;
        bjiv = b[j][i].v;
      } else {
        bjiu = 0.0;
        bjiv = 0.0;
      }
      x[j][i].u = 0.0 + bjiu;
      x[j][i].v = 0.0 + bjiv;
    }
  }

  /* Test whether we are on the right edge of the global array */
  if (xinte == info.mx) {
    i = info.mx - 1;
    /* right edge */
    for (j = info.ys; j < info.ys + info.ym; j++) {
      if (B) {
        bjiu = b[j][i].u;
        bjiv = b[j][i].v;
      } else {
        bjiu = 0.0;
        bjiv = 0.0;
      }
      x[j][i].u = 0.0 + bjiu;
      x[j][i].v = 0.0 + bjiv;
    }
  }

  for (k = 0; k < sweeps; k++) {
    for (j = info.ys; j < info.ys + info.ym; j++) {
      for (i = info.xs; i < info.xs + info.xm; i++) {
        ptconverged = PETSC_FALSE;
        pfnorm0     = 0.0;
        fu          = 0.0;
        fv          = 0.0;
        fomega      = 0.0;
        ftemp       = 0.0;
        /*  Run Newton's method on a single grid point */
        for (l = 0; l < max_its && !ptconverged; l++) {
          if (B) {
            bjiu     = b[j][i].u;
            bjiv     = b[j][i].v;
            bjiomega = b[j][i].omega;
            bjitemp  = b[j][i].temp;
          } else {
            bjiu     = 0.0;
            bjiv     = 0.0;
            bjiomega = 0.0;
            bjitemp  = 0.0;
          }

          if (i != 0 && i != info.mx - 1 && j != 0 && j != info.my - 1) {
            /* U velocity */
            u     = x[j][i].u;
            uxx   = (2.0 * u - x[j][i - 1].u - x[j][i + 1].u) * hydhx;
            uyy   = (2.0 * u - x[j - 1][i].u - x[j + 1][i].u) * hxdhy;
            fu    = uxx + uyy - .5 * (x[j + 1][i].omega - x[j - 1][i].omega) * hx - bjiu;
            dfudu = 2.0 * (hydhx + hxdhy);
            /* V velocity */
            u     = x[j][i].v;
            uxx   = (2.0 * u - x[j][i - 1].v - x[j][i + 1].v) * hydhx;
            uyy   = (2.0 * u - x[j - 1][i].v - x[j + 1][i].v) * hxdhy;
            fv    = uxx + uyy + .5 * (x[j][i + 1].omega - x[j][i - 1].omega) * hy - bjiv;
            dfvdv = 2.0 * (hydhx + hxdhy);
            /*
             convective coefficients for upwinding
             */
            vx  = x[j][i].u;
            avx = PetscAbsScalar(vx);
            vxp = .5 * (vx + avx);
            vxm = .5 * (vx - avx);
            vy  = x[j][i].v;
            avy = PetscAbsScalar(vy);
            vyp = .5 * (vy + avy);
            vym = .5 * (vy - avy);
            /* Omega */
            u      = x[j][i].omega;
            uxx    = (2.0 * u - x[j][i - 1].omega - x[j][i + 1].omega) * hydhx;
            uyy    = (2.0 * u - x[j - 1][i].omega - x[j + 1][i].omega) * hxdhy;
            fomega = uxx + uyy + (vxp * (u - x[j][i - 1].omega) + vxm * (x[j][i + 1].omega - u)) * hy + (vyp * (u - x[j - 1][i].omega) + vym * (x[j + 1][i].omega - u)) * hx - .5 * grashof * (x[j][i + 1].temp - x[j][i - 1].temp) * hy - bjiomega;
            /* convective coefficient derivatives */
            dfodo = 2.0 * (hydhx + hxdhy) + ((vxp - vxm) * hy + (vyp - vym) * hx);
            if (PetscRealPart(vx) > 0.0) dfodu = (u - x[j][i - 1].omega) * hy;
            else dfodu = (x[j][i + 1].omega - u) * hy;

            if (PetscRealPart(vy) > 0.0) dfodv = (u - x[j - 1][i].omega) * hx;
            else dfodv = (x[j + 1][i].omega - u) * hx;

            /* Temperature */
            u     = x[j][i].temp;
            uxx   = (2.0 * u - x[j][i - 1].temp - x[j][i + 1].temp) * hydhx;
            uyy   = (2.0 * u - x[j - 1][i].temp - x[j + 1][i].temp) * hxdhy;
            ftemp = uxx + uyy + prandtl * ((vxp * (u - x[j][i - 1].temp) + vxm * (x[j][i + 1].temp - u)) * hy + (vyp * (u - x[j - 1][i].temp) + vym * (x[j + 1][i].temp - u)) * hx) - bjitemp;
            dftdt = 2.0 * (hydhx + hxdhy) + prandtl * ((vxp - vxm) * hy + (vyp - vym) * hx);
            if (PetscRealPart(vx) > 0.0) dftdu = prandtl * (u - x[j][i - 1].temp) * hy;
            else dftdu = prandtl * (x[j][i + 1].temp - u) * hy;

            if (PetscRealPart(vy) > 0.0) dftdv = prandtl * (u - x[j - 1][i].temp) * hx;
            else dftdv = prandtl * (x[j + 1][i].temp - u) * hx;

            /* invert the system:
             [ dfu / du     0        0        0    ][yu] = [fu]
             [     0    dfv / dv     0        0    ][yv]   [fv]
             [ dfo / du dfo / dv dfo / do     0    ][yo]   [fo]
             [ dft / du dft / dv     0    dft / dt ][yt]   [ft]
             by simple back-substitution
           */
            yu = fu / dfudu;
            yv = fv / dfvdv;
            yo = (fomega - (dfodu * yu + dfodv * yv)) / dfodo;
            yt = (ftemp - (dftdu * yu + dftdv * yv)) / dftdt;

            x[j][i].u     = x[j][i].u - yu;
            x[j][i].v     = x[j][i].v - yv;
            x[j][i].temp  = x[j][i].temp - yt;
            x[j][i].omega = x[j][i].omega - yo;
          }
          if (i == 0) {
            fomega        = x[j][i].omega - (x[j][i + 1].v - x[j][i].v) * dhx - bjiomega;
            ftemp         = x[j][i].temp - bjitemp;
            yo            = fomega;
            yt            = ftemp;
            x[j][i].omega = x[j][i].omega - fomega;
            x[j][i].temp  = x[j][i].temp - ftemp;
          }
          if (i == info.mx - 1) {
            fomega        = x[j][i].omega - (x[j][i].v - x[j][i - 1].v) * dhx - bjiomega;
            ftemp         = x[j][i].temp - (PetscReal)(grashof > 0) - bjitemp;
            yo            = fomega;
            yt            = ftemp;
            x[j][i].omega = x[j][i].omega - fomega;
            x[j][i].temp  = x[j][i].temp - ftemp;
          }
          if (j == 0) {
            fomega        = x[j][i].omega + (x[j + 1][i].u - x[j][i].u) * dhy - bjiomega;
            ftemp         = x[j][i].temp - x[j + 1][i].temp - bjitemp;
            yo            = fomega;
            yt            = ftemp;
            x[j][i].omega = x[j][i].omega - fomega;
            x[j][i].temp  = x[j][i].temp - ftemp;
          }
          if (j == info.my - 1) {
            fomega        = x[j][i].omega + (x[j][i].u - x[j - 1][i].u) * dhy - bjiomega;
            ftemp         = x[j][i].temp - x[j - 1][i].temp - bjitemp;
            yo            = fomega;
            yt            = ftemp;
            x[j][i].omega = x[j][i].omega - fomega;
            x[j][i].temp  = x[j][i].temp - ftemp;
          }
          tot_its++;
          pfnorm = PetscRealPart(fu * fu + fv * fv + fomega * fomega + ftemp * ftemp);
          pfnorm = PetscSqrtReal(pfnorm);
          pynorm = PetscRealPart(yu * yu + yv * yv + yo * yo + yt * yt);
          pynorm = PetscSqrtReal(pynorm);
          pxnorm = PetscRealPart(x[j][i].u * x[j][i].u + x[j][i].v * x[j][i].v + x[j][i].omega * x[j][i].omega + x[j][i].temp * x[j][i].temp);
          pxnorm = PetscSqrtReal(pxnorm);
          if (l == 0) pfnorm0 = pfnorm;
          if (rtol * pfnorm0 > pfnorm || atol > pfnorm || pxnorm * stol > pynorm) ptconverged = PETSC_TRUE;
        }
      }
    }
  }
  PetscCall(DMDAVecRestoreArrayWrite(da, localX, &x));
  if (B) PetscCall(DMDAVecRestoreArrayRead(da, localB, &b));
  PetscCall(DMLocalToGlobalBegin(da, localX, INSERT_VALUES, X));
  PetscCall(DMLocalToGlobalEnd(da, localX, INSERT_VALUES, X));
  PetscCall(PetscLogFlops(tot_its * (84.0 + 41.0 + 26.0)));
  PetscCall(DMRestoreLocalVector(da, &localX));
  if (B) PetscCall(DMRestoreLocalVector(da, &localB));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/*TEST

   test:
      nsize: 2
      args: -da_refine 3 -snes_monitor_short -pc_type mg -ksp_type fgmres -pc_mg_type full
      requires: !single

   test:
      suffix: 10
      nsize: 3
      args: -snes_monitor_short -ksp_monitor_short -pc_type fieldsplit -pc_fieldsplit_type symmetric_multiplicative -snes_view -da_refine 1 -ksp_type fgmres
      requires: !single

   test:
      suffix: 11
      nsize: 4
      requires: pastix
      args: -snes_monitor_short -pc_type redundant -dm_mat_type mpiaij -redundant_pc_factor_mat_solver_type pastix -mat_pastix_thread_nbr 1 -pc_redundant_number 2 -da_refine 4 -ksp_type fgmres

   test:
      suffix: 12
      nsize: 12
      requires: pastix
      args: -snes_monitor_short -pc_type redundant -dm_mat_type mpiaij -redundant_pc_factor_mat_solver_type pastix -mat_pastix_thread_nbr 1 -pc_redundant_number 5 -da_refine 4 -ksp_type fgmres

   test:
      suffix: 13
      nsize: 3
      args: -snes_monitor_short -ksp_monitor_short -pc_type fieldsplit -pc_fieldsplit_type multiplicative -snes_view -da_refine 1 -ksp_type fgmres -snes_mf_operator
      requires: !single

   test:
      suffix: 14
      nsize: 4
      args: -snes_monitor_short -pc_type mg -dm_mat_type baij -mg_coarse_pc_type bjacobi -da_refine 3 -ksp_type fgmres
      requires: !single

   test:
      suffix: 14_ds
      nsize: 4
      args: -snes_converged_reason -pc_type mg -dm_mat_type baij -mg_coarse_pc_type bjacobi -da_refine 3 -ksp_type fgmres -mat_fd_type ds
      output_file: output/ex19_2.out
      requires: !single

   test:
      suffix: 17
      args: -snes_monitor_short -ksp_pc_side right
      requires: !single

   test:
      suffix: 18
      args: -snes_monitor_ksp draw::draw_lg -ksp_pc_side right
      requires: x !single

   test:
      suffix: 19
      nsize: 2
      args: -da_refine 3 -snes_monitor_short -pc_type mg -ksp_type fgmres -pc_mg_type full -snes_type newtontrdc
      requires: !single

   test:
      suffix: 20
      nsize: 2
      args: -da_refine 3 -snes_monitor_short -pc_type mg -ksp_type fgmres -pc_mg_type full -snes_type newtontrdc -snes_trdc_use_cauchy false
      requires: !single

   test:
      suffix: 2
      nsize: 4
      args: -da_refine 3 -snes_converged_reason -pc_type mg -mat_fd_type ds
      requires: !single

   test:
      suffix: 2_bcols1
      nsize: 4
      args: -da_refine 3 -snes_converged_reason -pc_type mg -mat_fd_type ds -mat_fd_coloring_bcols
      output_file: output/ex19_2.out
      requires: !single

   test:
      suffix: 3
      nsize: 4
      requires: mumps
      args: -da_refine 3 -snes_monitor_short -pc_type redundant -dm_mat_type mpiaij -redundant_ksp_type preonly -redundant_pc_factor_mat_solver_type mumps -pc_redundant_number 2

   test:
      suffix: 4
      nsize: 12
      requires: mumps
      args: -da_refine 3 -snes_monitor_short -pc_type redundant -dm_mat_type mpiaij -redundant_ksp_type preonly -redundant_pc_factor_mat_solver_type mumps -pc_redundant_number 5
      output_file: output/ex19_3.out

   test:
      suffix: 6
      args: -snes_monitor_short -ksp_monitor_short -pc_type fieldsplit -snes_view -ksp_type fgmres -da_refine 1
      requires: !single

   test:
      suffix: 7
      nsize: 3
      args: -snes_monitor_short -ksp_monitor_short -pc_type fieldsplit -snes_view -da_refine 1 -ksp_type fgmres

      requires: !single
   test:
      suffix: 8
      args: -snes_monitor_short -ksp_monitor_short -pc_type fieldsplit -pc_fieldsplit_block_size 2 -pc_fieldsplit_0_fields 0,1 -pc_fieldsplit_1_fields 0,1 -pc_fieldsplit_type multiplicative -snes_view -fieldsplit_pc_type lu -da_refine 1 -ksp_type fgmres
      requires: !single

   test:
      suffix: 9
      nsize: 3
      args: -snes_monitor_short -ksp_monitor_short -pc_type fieldsplit -pc_fieldsplit_type multiplicative -snes_view -da_refine 1 -ksp_type fgmres
      requires: !single

   test:
      suffix: aspin
      nsize: 4
      args: -da_refine 3 -da_overlap 2 -snes_monitor_short -snes_type aspin -grashof 4e4 -lidvelocity 100 -ksp_monitor_short -npc_sub_ksp_type preonly -npc_sub_pc_type lu
      requires: !single

   test:
      suffix: bcgsl
      nsize: 2
      args: -ksp_type bcgsl -ksp_monitor_short -da_refine 2 -ksp_bcgsl_ell 3 -snes_view
      requires: !single

   test:
      suffix: bcols1
      nsize: 2
      args: -da_refine 3 -snes_monitor_short -pc_type mg -ksp_type fgmres -pc_mg_type full -mat_fd_coloring_bcols 1
      output_file: output/ex19_1.out
      requires: !single

   test:
      suffix: bjacobi
      nsize: 4
      args: -da_refine 4 -ksp_type fgmres -pc_type bjacobi -pc_bjacobi_blocks 2 -sub_ksp_type gmres -sub_ksp_max_it 2 -sub_pc_type bjacobi -sub_sub_ksp_type preonly -sub_sub_pc_type ilu -snes_monitor_short
      requires: !single

   test:
      suffix: cgne
      args: -da_refine 2 -pc_type lu -ksp_type cgne -ksp_monitor_short -ksp_converged_reason -ksp_view -ksp_norm_type unpreconditioned
      filter: grep -v HERMITIAN
      requires: !single

   test:
      suffix: cgs
      args: -da_refine 1 -ksp_monitor_short -ksp_type cgs
      requires: !single

   test:
      suffix: composite_fieldsplit
      args: -ksp_type fgmres -pc_type composite -pc_composite_type MULTIPLICATIVE -pc_composite_pcs fieldsplit,none -sub_0_pc_fieldsplit_block_size 4 -sub_0_pc_fieldsplit_type additive -sub_0_pc_fieldsplit_0_fields 0,1,2 -sub_0_pc_fieldsplit_1_fields 3 -snes_monitor_short -ksp_monitor_short
      requires: !single

   test:
      suffix: composite_fieldsplit_bjacobi
      args: -ksp_type fgmres -pc_type composite -pc_composite_type MULTIPLICATIVE -pc_composite_pcs fieldsplit,bjacobi -sub_0_pc_fieldsplit_block_size 4 -sub_0_pc_fieldsplit_type additive -sub_0_pc_fieldsplit_0_fields 0,1,2 -sub_0_pc_fieldsplit_1_fields 3 -sub_1_pc_bjacobi_blocks 16 -sub_1_sub_pc_type lu -snes_monitor_short -ksp_monitor_short
      requires: !single

   test:
      suffix: composite_fieldsplit_bjacobi_2
      nsize: 4
      args: -ksp_type fgmres -pc_type composite -pc_composite_type MULTIPLICATIVE -pc_composite_pcs fieldsplit,bjacobi -sub_0_pc_fieldsplit_block_size 4 -sub_0_pc_fieldsplit_type additive -sub_0_pc_fieldsplit_0_fields 0,1,2 -sub_0_pc_fieldsplit_1_fields 3 -sub_1_pc_bjacobi_blocks 16 -sub_1_sub_pc_type lu -snes_monitor_short -ksp_monitor_short
      requires: !single

   test:
      suffix: composite_gs_newton
      nsize: 2
      args: -da_refine 3 -grashof 4e4 -lidvelocity 100 -snes_monitor_short -snes_type composite -snes_composite_type additiveoptimal -snes_composite_sneses ngs,newtonls -sub_0_snes_max_it 20 -sub_1_pc_type mg
      requires: !single

   test:
      suffix: cuda
      requires: cuda !single
      args: -dm_vec_type cuda -dm_mat_type aijcusparse -pc_type none -ksp_type fgmres -snes_monitor_short -snes_rtol 1.e-5

   test:
      suffix: hip
      requires: hip !single
      args: -dm_vec_type hip -dm_mat_type aijhipsparse -pc_type none -ksp_type fgmres -snes_monitor_short -snes_rtol 1.e-5

   test:
      suffix: draw
      args: -pc_type fieldsplit -snes_view draw -fieldsplit_x_velocity_pc_type mg -fieldsplit_x_velocity_pc_mg_galerkin pmat -fieldsplit_x_velocity_pc_mg_levels 2 -da_refine 1 -fieldsplit_x_velocity_mg_coarse_pc_type svd
      requires: x !single

   test:
      suffix: drawports
      args: -snes_monitor_solution draw::draw_ports -da_refine 1
      output_file: output/ex19_draw.out
      requires: x !single

   test:
      suffix: fas
      args: -da_refine 4 -snes_monitor_short -snes_type fas -fas_levels_snes_type ngs -fas_levels_snes_ngs_sweeps 3 -fas_levels_snes_ngs_atol 0.0 -fas_levels_snes_ngs_stol 0.0 -grashof 4e4 -snes_fas_smoothup 6 -snes_fas_smoothdown 6 -lidvelocity 100
      requires: !single

   test:
      suffix: fas_full
      args: -da_refine 4 -snes_monitor_short -snes_type fas -snes_fas_type full -snes_fas_full_downsweep -fas_levels_snes_type ngs -fas_levels_snes_ngs_sweeps 3 -fas_levels_snes_ngs_atol 0.0 -fas_levels_snes_ngs_stol 0.0 -grashof 4e4 -snes_fas_smoothup 6 -snes_fas_smoothdown 6 -lidvelocity 100
      requires: !single

   test:
      suffix: fdcoloring_ds
      args: -da_refine 3 -snes_converged_reason -pc_type mg -mat_fd_type ds
      output_file: output/ex19_2.out
      requires: !single

   test:
      suffix: fdcoloring_ds_baij
      args: -da_refine 3 -snes_converged_reason -pc_type mg -mat_fd_type ds -dm_mat_type baij
      output_file: output/ex19_2.out
      requires: !single

   test:
      suffix: fdcoloring_ds_bcols1
      args: -da_refine 3 -snes_converged_reason -pc_type mg -mat_fd_type ds -mat_fd_coloring_bcols 1
      output_file: output/ex19_2.out
      requires: !single

   test:
      suffix: fdcoloring_wp
      args: -da_refine 3 -snes_monitor_short -pc_type mg
      requires: !single

   test:
      suffix: fdcoloring_wp_baij
      args: -da_refine 3 -snes_monitor_short -pc_type mg -dm_mat_type baij
      output_file: output/ex19_fdcoloring_wp.out
      requires: !single

   test:
      suffix: fdcoloring_wp_bcols1
      args: -da_refine 3 -snes_monitor_short -pc_type mg -mat_fd_coloring_bcols 1
      output_file: output/ex19_fdcoloring_wp.out
      requires: !single

   test:
      suffix: fieldsplit_2
      args: -ksp_type fgmres -pc_type fieldsplit -pc_fieldsplit_block_size 4 -pc_fieldsplit_type additive -pc_fieldsplit_0_fields 0,1,2 -pc_fieldsplit_1_fields 3 -snes_monitor_short -ksp_monitor_short
      requires: !single

   test:
      suffix: fieldsplit_3
      args: -ksp_type fgmres -pc_type fieldsplit -pc_fieldsplit_block_size 4 -pc_fieldsplit_type additive -pc_fieldsplit_0_fields 0,1,2 -pc_fieldsplit_1_fields 3 -fieldsplit_0_pc_type lu -fieldsplit_1_pc_type lu -snes_monitor_short -ksp_monitor_short
      requires: !single

   test:
      suffix: fieldsplit_4
      args: -ksp_type fgmres -pc_type fieldsplit -pc_fieldsplit_block_size 4 -pc_fieldsplit_type SCHUR -pc_fieldsplit_0_fields 0,1,2 -pc_fieldsplit_1_fields 3 -fieldsplit_0_pc_type lu -fieldsplit_1_pc_type lu -snes_monitor_short -ksp_monitor_short
      requires: !single

   # HYPRE PtAP broken with complex numbers
   test:
      suffix: fieldsplit_hypre
      nsize: 2
      requires: hypre mumps !complex !defined(PETSC_HAVE_HYPRE_DEVICE)
      args: -pc_type fieldsplit -pc_fieldsplit_block_size 4 -pc_fieldsplit_type SCHUR -pc_fieldsplit_0_fields 0,1,2 -pc_fieldsplit_1_fields 3 -fieldsplit_0_pc_type lu -fieldsplit_0_pc_factor_mat_solver_type mumps -fieldsplit_1_pc_type hypre -fieldsplit_1_pc_hypre_type boomeramg -snes_monitor_short -ksp_monitor_short

   test:
      suffix: fieldsplit_mumps
      nsize: 2
      requires: mumps
      args: -pc_type fieldsplit -pc_fieldsplit_block_size 4 -pc_fieldsplit_type SCHUR -pc_fieldsplit_0_fields 0,1,2 -pc_fieldsplit_1_fields 3 -fieldsplit_0_pc_type lu -fieldsplit_1_pc_type lu -snes_monitor_short -ksp_monitor_short -fieldsplit_0_pc_factor_mat_solver_type mumps -fieldsplit_1_pc_factor_mat_solver_type mumps
      output_file: output/ex19_fieldsplit_5.out

   test:
      suffix: greedy_coloring
      nsize: 2
      args: -da_refine 3 -snes_monitor_short -snes_fd_color -snes_fd_color_use_mat -mat_coloring_type greedy -mat_coloring_weight_type lf -mat_coloring_view> ex19_greedy_coloring.tmp 2>&1
      requires: !single

   # HYPRE PtAP broken with complex numbers
   test:
      suffix: hypre
      nsize: 2
      requires: hypre !complex !defined(PETSC_HAVE_HYPRE_DEVICE)
      args: -da_refine 3 -snes_monitor_short -pc_type hypre -ksp_norm_type unpreconditioned

   # ibcgs is broken when using device vectors
   test:
      suffix: ibcgs
      nsize: 2
      args: -ksp_type ibcgs -ksp_monitor_short -da_refine 2 -snes_view
      requires: !complex !single

   test:
      suffix: kaczmarz
      nsize: 2
      args: -pc_type kaczmarz -ksp_monitor_short -snes_monitor_short -snes_view
      requires: !single

   test:
      suffix: klu
      requires: suitesparse
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type klu
      output_file: output/ex19_superlu.out

   test:
      suffix: klu_2
      requires: suitesparse
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type klu -pc_factor_mat_ordering_type nd
      output_file: output/ex19_superlu.out

   test:
      suffix: klu_3
      requires: suitesparse
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type klu -mat_klu_use_btf 0
      output_file: output/ex19_superlu.out

   test:
      suffix: ml
      nsize: 2
      requires: ml
      args: -da_refine 3 -snes_monitor_short -pc_type ml

   test:
      suffix: ngmres_fas
      args: -da_refine 4 -snes_monitor_short -snes_type ngmres -npc_fas_levels_snes_type ngs -npc_fas_levels_snes_ngs_sweeps 3 -npc_fas_levels_snes_ngs_atol 0.0 -npc_fas_levels_snes_ngs_stol 0.0 -npc_snes_type fas -npc_fas_levels_snes_type ngs -npc_snes_max_it 1 -npc_snes_fas_smoothup 6 -npc_snes_fas_smoothdown 6 -lidvelocity 100 -grashof 4e4
      requires: !single

   test:
      suffix: ngmres_fas_gssecant
      args: -da_refine 3 -snes_monitor_short -snes_type ngmres -npc_snes_type fas -npc_fas_levels_snes_type ngs -npc_fas_levels_snes_max_it 6 -npc_fas_levels_snes_ngs_secant -npc_fas_levels_snes_ngs_max_it 1 -npc_fas_coarse_snes_max_it 1 -lidvelocity 100 -grashof 4e4
      requires: !single

   test:
      suffix: ngmres_fas_ms
      nsize: 2
      args: -snes_grid_sequence 2 -lidvelocity 200 -grashof 1e4 -snes_monitor_short -snes_view -snes_converged_reason -snes_type ngmres -npc_snes_type fas -npc_fas_coarse_snes_type newtonls -npc_fas_coarse_ksp_type preonly -npc_snes_max_it 1
      requires: !single

   test:
      suffix: ngmres_nasm
      nsize: 4
      args: -da_refine 4 -da_overlap 2 -snes_monitor_short -snes_type ngmres -snes_max_it 10 -npc_snes_type nasm -npc_snes_nasm_type basic -grashof 4e4 -lidvelocity 100
      requires: !single

   test:
      suffix: ngs
      args: -snes_type ngs -snes_view -snes_monitor -snes_rtol 1e-4
      requires: !single

   test:
      suffix: ngs_fd
      args: -snes_type ngs -snes_ngs_secant -snes_view -snes_monitor -snes_rtol 1e-4
      requires: !single

   test:
      suffix: parms
      nsize: 2
      requires: parms
      args: -pc_type parms -ksp_monitor_short -snes_view

   test:
      suffix: superlu
      requires: superlu
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type superlu

   test:
      suffix: superlu_sell
      requires: superlu
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type superlu -dm_mat_type sell -pc_factor_mat_ordering_type natural
      output_file: output/ex19_superlu.out

   test:
      suffix: superlu_dist
      requires: superlu_dist
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type superlu_dist
      output_file: output/ex19_superlu.out

   test:
      suffix: superlu_dist_2
      nsize: 2
      requires: superlu_dist
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type superlu_dist
      output_file: output/ex19_superlu.out

   test:
      suffix: superlu_dist_3d
      nsize: 4
      requires: superlu_dist !defined(PETSCTEST_VALGRIND)
      filter: grep -v iam | grep -v openMP | sed -e "s/Column permutation MMD_AT_PLUS_A/Column permutation METIS_AT_PLUS_A/g"
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type superlu_dist -mat_superlu_dist_3d -mat_superlu_dist_d 2 -snes_view -snes_monitor -ksp_monitor

   test:
      suffix: superlu_dist_2s
      nsize: 2
      requires: superlu_dist defined(PETSC_HAVE_SUPERLU_DIST_SINGLE)
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type superlu_dist -pc_precision single
      output_file: output/ex19_superlu.out

   test:
      suffix: mumps_mixed
      nsize: 2
      requires: mumps defined(PETSC_HAVE_MUMPS_MIXED_PRECISION)
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type mumps -pc_precision {{single double}}
      output_file: output/ex19_superlu.out

   test:
      suffix: superlu_dist_3ds
      nsize: 4
      requires: superlu_dist !defined(PETSCTEST_VALGRIND) defined(PETSC_HAVE_SUPERLU_DIST_SINGLE)
      filter: grep -v iam | grep -v openMP | sed -e "s/Column permutation MMD_AT_PLUS_A/Column permutation METIS_AT_PLUS_A/g"
      args: -da_grid_x 20 -da_grid_y 20 -pc_type lu -pc_factor_mat_solver_type superlu_dist -mat_superlu_dist_3d -mat_superlu_dist_d 2 -snes_view -snes_monitor -ksp_monitor -pc_precision single

   test:
      suffix: superlu_equil
      requires: superlu
      args: -da_grid_x 20 -da_grid_y 20 -{snes,ksp}_monitor_short -pc_type lu -pc_factor_mat_solver_type superlu -mat_superlu_equil

   test:
      suffix: superlu_equil_sell
      requires: superlu
      args: -da_grid_x 20 -da_grid_y 20 -{snes,ksp}_monitor_short -pc_type lu -pc_factor_mat_solver_type superlu -mat_superlu_equil -dm_mat_type sell -pc_factor_mat_ordering_type natural
      output_file: output/ex19_superlu_equil.out

   test:
      suffix: tcqmr
      args: -da_refine 1 -ksp_monitor_short -ksp_type tcqmr
      requires: !single

   test:
      suffix: tfqmr
      args: -da_refine 1 -ksp_monitor_short -ksp_type tfqmr
      requires: !single

   test:
      suffix: umfpack
      requires: suitesparse
      args: -da_refine 2 -pc_type lu -pc_factor_mat_solver_type umfpack -snes_view -snes_monitor_short -ksp_monitor_short -pc_factor_mat_ordering_type external

   test:
      suffix: tut_1
      nsize: 4
      requires: !single
      args: -da_refine 5 -snes_monitor -ksp_monitor -snes_view

   test:
      suffix: tut_2
      nsize: 4
      requires: !single
      args: -da_refine 5 -snes_monitor -ksp_monitor -snes_view -pc_type mg

   # HYPRE PtAP broken with complex numbers
   test:
      suffix: tut_3
      nsize: 4
      requires: hypre !single !complex !defined(PETSC_HAVE_HYPRE_DEVICE)
      args: -da_refine 5 -snes_monitor -snes_converged_reason -pc_type hypre -dm_mat_type {{aij baij}}

   test:
      suffix: tut_3_seq
      nsize: 1
      requires: hypre !single !complex !defined(PETSC_HAVE_HYPRE_DEVICE)
      args: -da_refine 1 -snes_monitor -snes_converged_reason -pc_type hypre -dm_mat_type {{seqaij mpiaij seqbaij mpibaij}}

   test:
      suffix: tut_8
      nsize: 4
      requires: ml !single
      args: -da_refine 5 -snes_monitor -ksp_monitor -snes_view -pc_type ml

   test:
      suffix: tut_4
      nsize: 1
      requires: !single
      args: -da_refine 5 -log_view
      filter: head -n 2
      filter_output: head -n 2

   test:
      suffix: tut_5
      nsize: 1
      requires: !single
      args: -da_refine 5 -log_view -pc_type mg
      filter: head -n 2
      filter_output: head -n 2

   test:
      suffix: tut_6
      nsize: 4
      requires: !single
      args: -da_refine 5 -log_view
      filter: head -n 2
      filter_output: head -n 2

   test:
      suffix: tut_7
      nsize: 4
      requires: !single
      args: -da_refine 5 -log_view -pc_type mg
      filter: head -n 2
      filter_output: head -n 2

   test:
      suffix: cuda_1
      nsize: 1
      requires: cuda
      args: -snes_monitor -dm_mat_type seqaijcusparse -dm_vec_type seqcuda -pc_type gamg -ksp_monitor -mg_levels_ksp_max_it 1

   test:
      suffix: cuda_2
      nsize: 3
      requires: cuda !single
      args: -snes_monitor -dm_mat_type mpiaijcusparse -dm_vec_type mpicuda -pc_type gamg -ksp_monitor -mg_levels_ksp_max_it 1

   test:
      suffix: cuda_dm_bind_below
      nsize: 2
      requires: cuda defined(PETSC_USE_LOG)
      args: -dm_mat_type aijcusparse -dm_vec_type cuda -da_refine 3 -pc_type mg -mg_levels_ksp_type chebyshev -mg_levels_pc_type jacobi -log_view -pc_mg_log -dm_bind_below 10000
      filter: awk "/Level/ {print \$NF}"

   test:
      suffix: hip_1
      nsize: 1
      requires: hip
      args: -snes_monitor -dm_mat_type mpiaijhipsparse -dm_vec_type hip -pc_type gamg -ksp_monitor -mg_levels_ksp_max_it 1

   test:
      suffix: hip_2
      nsize: 3
      requires: hip !single
      args: -snes_monitor -dm_mat_type mpiaijhipsparse -dm_vec_type mpihip -pc_type gamg -ksp_monitor -mg_levels_ksp_max_it 1

   test:
      suffix: hip_dm_bind_below
      nsize: 2
      requires: hip
      args: -dm_mat_type aijhipsparse -dm_vec_type hip -da_refine 3 -pc_type mg -mg_levels_ksp_type chebyshev -mg_levels_pc_type jacobi -log_view -pc_mg_log -dm_bind_below 10000
      filter: awk "/Level/ {print \$NF}"

   test:
      suffix: viennacl_dm_bind_below
      nsize: 2
      requires: viennacl
      args: -dm_mat_type aijviennacl -dm_vec_type viennacl -da_refine 3 -pc_type mg -mg_levels_ksp_type chebyshev -mg_levels_pc_type jacobi -log_view -pc_mg_log -dm_bind_below 10000
      filter: awk "/Level/ {print \$NF}"

   test:
      suffix: seqbaijmkl
      nsize: 1
      requires: defined(PETSC_HAVE_MKL_SPARSE_OPTIMIZE)
      args: -dm_mat_type baij -snes_monitor -ksp_monitor -snes_view

   test:
      suffix: mpibaijmkl
      nsize: 2
      requires: defined(PETSC_HAVE_MKL_SPARSE_OPTIMIZE)
      args: -dm_mat_type baij -snes_monitor -ksp_monitor -snes_view

   test:
     suffix: cpardiso
     nsize: 4
     requires: mkl_cpardiso
     args: -pc_type lu -pc_factor_mat_solver_type mkl_cpardiso -ksp_monitor

   test:
     suffix: logviewmemory
     requires: defined(PETSC_USE_LOG) !defined(PETSC_HAVE_THREADSAFETY)
     args: -log_view -log_view_memory -da_refine 4
     filter: grep MatFDColorSetUp | wc -w | xargs -I % sh -c "expr % \> 21"

   test:
     suffix: fs
     requires: !single
     args: -pc_type fieldsplit -da_refine 3 -all_ksp_monitor -fieldsplit_y_velocity_pc_type lu -fieldsplit_temperature_pc_type lu -fieldsplit_x_velocity_pc_type lu -snes_view

   test:
     suffix: asm_matconvert
     args: -mat_type aij -pc_type asm -pc_asm_sub_mat_type dense -snes_view

   test:
      suffix: euclid
      nsize: 2
      requires: hypre !single !complex !defined(PETSC_HAVE_HYPRE_MIXEDINT) !defined(PETSC_HAVE_HYPRE_DEVICE)
      args: -da_refine 2 -ksp_monitor -snes_monitor -snes_view -pc_type hypre -pc_hypre_type euclid

   test:
      suffix: euclid_bj
      nsize: 2
      requires: hypre !single !complex !defined(PETSC_HAVE_HYPRE_MIXEDINT) !defined(PETSC_HAVE_HYPRE_DEVICE)
      args: -da_refine 2 -ksp_monitor -snes_monitor -snes_view -pc_type hypre -pc_hypre_type euclid -pc_hypre_euclid_bj

   test:
      suffix: euclid_droptolerance
      nsize: 1
      requires: hypre !single !complex !defined(PETSC_HAVE_HYPRE_MIXEDINT) !defined(PETSC_HAVE_HYPRE_DEVICE)
      args: -da_refine 2 -ksp_monitor -snes_monitor -snes_view -pc_type hypre -pc_hypre_type euclid -pc_hypre_euclid_droptolerance .1

   test:
      suffix: failure_size
      nsize: 1
      requires: !defined(PETSC_USE_64BIT_INDICES) !defined(PETSCTEST_VALGRIND) !defined(PETSC_HAVE_SANITIZER)
      args: -da_refine 100 -petsc_ci_portable_error_output -error_output_stdout
      filter: grep -E -v "(memory block|leaked context|not freed before MPI_Finalize|Could be the program crashed)"

   testset:
      requires: hpddm cuda
      args: -snes_monitor -ksp_converged_reason -ksp_type hpddm -pc_type jacobi -dm_mat_type aijcusparse -dm_vec_type cuda
      test:
        suffix: hpddm_cuda
        filter: sed -e "s/Linear solve converged due to CONVERGED_RTOL iterations 15/Linear solve converged due to CONVERGED_RTOL iterations 14/g"
        args: -ksp_hpddm_type {{gmres gcrodr}separate output} -ksp_hpddm_precision {{single double}shared output}
      test:
        suffix: hpddm_cuda_right
        filter: sed -e "s/Linear solve converged due to CONVERGED_RTOL iterations 15/Linear solve converged due to CONVERGED_RTOL iterations 14/g"
        args: -ksp_hpddm_type gcrodr -ksp_pc_side right
        output_file: output/ex19_hpddm_cuda_ksp_hpddm_type-gcrodr.out

TEST*/
````

## TS ex11.c

- Selected by: Tutorials by mathematical problem
- Rendered listing: <https://petsc.org/release/src/ts/tutorials/ex11.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/ts/tutorials/ex11.c>

````c
static char help[] = "Second Order TVD Finite Volume Example.\n";
/*F

We use a second order TVD finite volume method to evolve a system of PDEs. Our simple upwinded residual evaluation loops
over all mesh faces and uses a Riemann solver to produce the flux given the face geometry and cell values,
\begin{equation}
  f_i = \mathrm{riemann}(\mathrm{phys}, p_\mathrm{centroid}, \hat n, x^L, x^R)
\end{equation}
and then update the cell values given the cell volume.
\begin{eqnarray}
    f^L_i &-=& \frac{f_i}{vol^L} \\
    f^R_i &+=& \frac{f_i}{vol^R}
\end{eqnarray}

As an example, we can consider the shallow water wave equation,
\begin{eqnarray}
     h_t + \nabla\cdot \left( uh                              \right) &=& 0 \\
  (uh)_t + \nabla\cdot \left( u\otimes uh + \frac{g h^2}{2} I \right) &=& 0
\end{eqnarray}
where $h$ is wave height, $u$ is wave velocity, and $g$ is the acceleration due to gravity.

A representative Riemann solver for the shallow water equations is given in the PhysicsRiemann_SW() function,
\begin{eqnarray}
  f^{L,R}_h    &=& uh^{L,R} \cdot \hat n \\
  f^{L,R}_{uh} &=& \frac{f^{L,R}_h}{h^{L,R}} uh^{L,R} + g (h^{L,R})^2 \hat n \\
  c^{L,R}      &=& \sqrt{g h^{L,R}} \\
  s            &=& \max\left( \left|\frac{uh^L \cdot \hat n}{h^L}\right| + c^L, \left|\frac{uh^R \cdot \hat n}{h^R}\right| + c^R \right) \\
  f_i          &=& \frac{A_\mathrm{face}}{2} \left( f^L_i + f^R_i + s \left( x^L_i - x^R_i \right) \right)
\end{eqnarray}
where $c$ is the local gravity wave speed and $f_i$ is a Rusanov flux.

The more sophisticated residual evaluation in RHSFunctionLocal_LS() uses a least-squares fit to a quadratic polynomial
over a neighborhood of the given element.

The mesh is read in from an ExodusII file, usually generated by Cubit.

The example also shows how to handle AMR in a time-dependent TS solver.
F*/
#include <petscdmplex.h>
#include <petscdmforest.h>
#include <petscds.h>
#include <petscts.h>

#include "ex11.h"

static PetscFunctionList PhysicsList, PhysicsRiemannList_SW, PhysicsRiemannList_Euler;

/* 'User' implements a discretization of a continuous model. */
typedef struct _n_User *User;
typedef PetscErrorCode (*SolutionFunction)(Model, PetscReal, const PetscReal *, PetscScalar *, void *);
typedef PetscErrorCode (*SetUpBCFunction)(DM, PetscDS, Physics);
typedef PetscErrorCode (*FunctionalFunction)(Model, PetscReal, const PetscReal *, const PetscScalar *, PetscReal *, void *);
typedef PetscErrorCode (*SetupFields)(Physics, PetscSection);
static PetscErrorCode ModelSolutionSetDefault(Model, SolutionFunction, void *);
static PetscErrorCode ModelFunctionalRegister(Model, const char *, PetscInt *, FunctionalFunction, void *);
static PetscErrorCode OutputVTK(DM, const char *, PetscViewer *);

typedef struct _n_FunctionalLink *FunctionalLink;
struct _n_FunctionalLink {
  char              *name;
  FunctionalFunction func;
  void              *ctx;
  PetscInt           offset;
  FunctionalLink     next;
};

struct _n_Model {
  MPI_Comm         comm; /* Does not do collective communication, but some error conditions can be collective */
  Physics          physics;
  FunctionalLink   functionalRegistry;
  PetscInt         maxComputed;
  PetscInt         numMonitored;
  FunctionalLink  *functionalMonitored;
  PetscInt         numCall;
  FunctionalLink  *functionalCall;
  SolutionFunction solution;
  SetUpBCFunction  setupbc;
  void            *solutionctx;
  PetscReal        maxspeed; /* estimate of global maximum speed (for CFL calculation) */
  PetscReal        bounds[2 * DIM];
  PetscErrorCode (*errorIndicator)(PetscInt, PetscReal, PetscInt, const PetscScalar[], const PetscScalar[], PetscReal *, void *);
  void *errorCtx;
  PetscErrorCode (*setupCEED)(DM, Physics);
};

struct _n_User {
  PetscInt  vtkInterval;                        /* For monitor */
  char      outputBasename[PETSC_MAX_PATH_LEN]; /* Basename for output files */
  PetscInt  monitorStepOffset;
  Model     model;
  PetscBool vtkmon;
};

#ifdef PETSC_HAVE_LIBCEED
// Free a plain data context that was allocated using PETSc; returning libCEED error codes
static int FreeContextPetsc(void *data)
{
  if (PetscFree(data)) return CeedError(NULL, CEED_ERROR_ACCESS, "PetscFree failed");
  return CEED_ERROR_SUCCESS;
}
#endif

/******************* Advect ********************/
typedef enum {
  ADVECT_SOL_TILTED,
  ADVECT_SOL_BUMP,
  ADVECT_SOL_BUMP_CAVITY
} AdvectSolType;
static const char *const AdvectSolTypes[] = {"TILTED", "BUMP", "BUMP_CAVITY", "AdvectSolType", "ADVECT_SOL_", 0};
typedef enum {
  ADVECT_SOL_BUMP_CONE,
  ADVECT_SOL_BUMP_COS
} AdvectSolBumpType;
static const char *const AdvectSolBumpTypes[] = {"CONE", "COS", "AdvectSolBumpType", "ADVECT_SOL_BUMP_", 0};

typedef struct {
  PetscReal wind[DIM];
} Physics_Advect_Tilted;
typedef struct {
  PetscReal         center[DIM];
  PetscReal         radius;
  AdvectSolBumpType type;
} Physics_Advect_Bump;

typedef struct {
  PetscReal     inflowState;
  AdvectSolType soltype;
  union
  {
    Physics_Advect_Tilted tilted;
    Physics_Advect_Bump   bump;
  } sol;
  struct {
    PetscInt Solution;
    PetscInt Error;
  } functional;
} Physics_Advect;

static const struct FieldDescription PhysicsFields_Advect[] = {
  {"U",  1},
  {NULL, 0}
};

static PetscErrorCode PhysicsBoundary_Advect_Inflow(PetscReal time, const PetscReal *c, const PetscReal *n, const PetscScalar *xI, PetscScalar *xG, PetscCtx ctx)
{
  Physics         phys   = (Physics)ctx;
  Physics_Advect *advect = (Physics_Advect *)phys->data;

  PetscFunctionBeginUser;
  xG[0] = advect->inflowState;
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode PhysicsBoundary_Advect_Outflow(PetscReal time, const PetscReal *c, const PetscReal *n, const PetscScalar *xI, PetscScalar *xG, PetscCtx ctx)
{
  PetscFunctionBeginUser;
  xG[0] = xI[0];
  PetscFunctionReturn(PETSC_SUCCESS);
}

static void PhysicsRiemann_Advect(PetscInt dim, PetscInt Nf, const PetscReal *qp, const PetscReal *n, const PetscScalar *xL, const PetscScalar *xR, PetscInt numConstants, const PetscScalar constants[], PetscScalar *flux, Physics phys)
{
  Physics_Advect *advect = (Physics_Advect *)phys->data;
  PetscReal       wind[DIM], wn;

  switch (advect->soltype) {
  case ADVECT_SOL_TILTED: {
    Physics_Advect_Tilted *tilted = &advect->sol.tilted;
    wind[0]                       = tilted->wind[0];
    wind[1]                       = tilted->wind[1];
  } break;
  case ADVECT_SOL_BUMP:
    wind[0] = -qp[1];
    wind[1] = qp[0];
    break;
  case ADVECT_SOL_BUMP_CAVITY: {
    PetscInt  i;
    PetscReal comp2[3] = {0., 0., 0.}, rad2;

    rad2 = 0.;
    for (i = 0; i < dim; i++) {
      comp2[i] = qp[i] * qp[i];
      rad2 += comp2[i];
    }

    wind[0] = -qp[1];
    wind[1] = qp[0];
    if (rad2 > 1.) {
      PetscInt  maxI     = 0;
      PetscReal maxComp2 = comp2[0];

      for (i = 1; i < dim; i++) {
        if (comp2[i] > maxComp2) {
          maxI     = i;
          maxComp2 = comp2[i];
        }
      }
      wind[maxI] = 0.;
    }
  } break;
  default: {
    PetscInt i;
    for (i = 0; i < DIM; ++i) wind[i] = 0.0;
  }
    /* default: SETERRQ(PETSC_COMM_SELF,PETSC_ERR_SUP,"No support for solution type %s",AdvectSolBumpTypes[advect->soltype]); */
  }
  wn      = Dot2Real(wind, n);
  flux[0] = (wn > 0 ? xL[0] : xR[0]) * wn;
}

static PetscErrorCode PhysicsSolution_Advect(Model mod, PetscReal time, const PetscReal *x, PetscScalar *u, PetscCtx ctx)
{
  Physics         phys   = (Physics)ctx;
  Physics_Advect *advect = (Physics_Advect *)phys->data;

  PetscFunctionBeginUser;
  switch (advect->soltype) {
  case ADVECT_SOL_TILTED: {
    PetscReal              x0[DIM];
    Physics_Advect_Tilted *tilted = &advect->sol.tilted;
    Waxpy2Real(-time, tilted->wind, x, x0);
    if (x0[1] > 0) u[0] = 1. * x[0] + 3. * x[1];
    else u[0] = advect->inflowState;
  } break;
  case ADVECT_SOL_BUMP_CAVITY:
  case ADVECT_SOL_BUMP: {
    Physics_Advect_Bump *bump = &advect->sol.bump;
    PetscReal            x0[DIM], v[DIM], r, cost, sint;
    cost  = PetscCosReal(time);
    sint  = PetscSinReal(time);
    x0[0] = cost * x[0] + sint * x[1];
    x0[1] = -sint * x[0] + cost * x[1];
    Waxpy2Real(-1, bump->center, x0, v);
    r = Norm2Real(v);
    switch (bump->type) {
    case ADVECT_SOL_BUMP_CONE:
      u[0] = PetscMax(1 - r / bump->radius, 0);
      break;
    case ADVECT_SOL_BUMP_COS:
      u[0] = 0.5 + 0.5 * PetscCosReal(PetscMin(r / bump->radius, 1) * PETSC_PI);
      break;
    }
  } break;
  default:
    SETERRQ(PETSC_COMM_SELF, PETSC_ERR_SUP, "Unknown solution type");
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode PhysicsFunctional_Advect(Model mod, PetscReal time, const PetscReal *x, const PetscScalar *y, PetscReal *f, PetscCtx ctx)
{
  Physics         phys      = (Physics)ctx;
  Physics_Advect *advect    = (Physics_Advect *)phys->data;
  PetscScalar     yexact[1] = {0.0};

  PetscFunctionBeginUser;
  PetscCall(PhysicsSolution_Advect(mod, time, x, yexact, phys));
  f[advect->functional.Solution] = PetscRealPart(y[0]);
  f[advect->functional.Error]    = PetscAbsScalar(y[0] - yexact[0]);
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetUpBC_Advect(DM dm, PetscDS prob, Physics phys)
{
  const PetscInt inflowids[] = {100, 200, 300}, outflowids[] = {101};
  DMLabel        label;

  PetscFunctionBeginUser;
  /* Register "canned" boundary conditions and defaults for where to apply. */
  PetscCall(DMGetLabel(dm, "Face Sets", &label));
  PetscCall(PetscDSAddBoundary(prob, DM_BC_NATURAL_RIEMANN, "inflow", label, PETSC_STATIC_ARRAY_LENGTH(inflowids), inflowids, 0, 0, NULL, (PetscVoidFn *)PhysicsBoundary_Advect_Inflow, NULL, phys, NULL));
  PetscCall(PetscDSAddBoundary(prob, DM_BC_NATURAL_RIEMANN, "outflow", label, PETSC_STATIC_ARRAY_LENGTH(outflowids), outflowids, 0, 0, NULL, (PetscVoidFn *)PhysicsBoundary_Advect_Outflow, NULL, phys, NULL));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode PhysicsCreate_Advect(Model mod, Physics phys, PetscOptionItems PetscOptionsObject)
{
  Physics_Advect *advect;

  PetscFunctionBeginUser;
  phys->field_desc = PhysicsFields_Advect;
  phys->riemann    = (PetscRiemannFn *)(PetscVoidFn *)PhysicsRiemann_Advect;
  PetscCall(PetscNew(&advect));
  phys->data   = advect;
  mod->setupbc = SetUpBC_Advect;

  PetscOptionsHeadBegin(PetscOptionsObject, "Advect options");
  {
    PetscInt two = 2, dof = 1;
    advect->soltype = ADVECT_SOL_TILTED;
    PetscCall(PetscOptionsEnum("-advect_sol_type", "solution type", "", AdvectSolTypes, (PetscEnum)advect->soltype, (PetscEnum *)&advect->soltype, NULL));
    switch (advect->soltype) {
    case ADVECT_SOL_TILTED: {
      Physics_Advect_Tilted *tilted = &advect->sol.tilted;
      two                           = 2;
      tilted->wind[0]               = 0.0;
      tilted->wind[1]               = 1.0;
      PetscCall(PetscOptionsRealArray("-advect_tilted_wind", "background wind vx,vy", "", tilted->wind, &two, NULL));
      advect->inflowState = -2.0;
      PetscCall(PetscOptionsRealArray("-advect_tilted_inflow", "Inflow state", "", &advect->inflowState, &dof, NULL));
      phys->maxspeed = Norm2Real(tilted->wind);
    } break;
    case ADVECT_SOL_BUMP_CAVITY:
    case ADVECT_SOL_BUMP: {
      Physics_Advect_Bump *bump = &advect->sol.bump;
      two                       = 2;
      bump->center[0]           = 2.;
      bump->center[1]           = 0.;
      PetscCall(PetscOptionsRealArray("-advect_bump_center", "location of center of bump x,y", "", bump->center, &two, NULL));
      bump->radius = 0.9;
      PetscCall(PetscOptionsReal("-advect_bump_radius", "radius of bump", "", bump->radius, &bump->radius, NULL));
      bump->type = ADVECT_SOL_BUMP_CONE;
      PetscCall(PetscOptionsEnum("-advect_bump_type", "type of bump", "", AdvectSolBumpTypes, (PetscEnum)bump->type, (PetscEnum *)&bump->type, NULL));
      phys->maxspeed = 3.; /* radius of mesh, kludge */
    } break;
    }
  }
  PetscOptionsHeadEnd();
  /* Initial/transient solution with default boundary conditions */
  PetscCall(ModelSolutionSetDefault(mod, PhysicsSolution_Advect, phys));
  /* Register "canned" functionals */
  PetscCall(ModelFunctionalRegister(mod, "Solution", &advect->functional.Solution, PhysicsFunctional_Advect, phys));
  PetscCall(ModelFunctionalRegister(mod, "Error", &advect->functional.Error, PhysicsFunctional_Advect, phys));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/******************* Shallow Water ********************/
static const struct FieldDescription PhysicsFields_SW[] = {
  {"Height",   1  },
  {"Momentum", DIM},
  {NULL,       0  }
};

static PetscErrorCode PhysicsBoundary_SW_Wall(PetscReal time, const PetscReal *c, const PetscReal *n, const PetscScalar *xI, PetscScalar *xG, PetscCtx ctx)
{
  PetscFunctionBeginUser;
  xG[0] = xI[0];
  xG[1] = -xI[1];
  xG[2] = -xI[2];
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode PhysicsSolution_SW(Model mod, PetscReal time, const PetscReal *x, PetscScalar *u, PetscCtx ctx)
{
  PetscReal dx[2], r, sigma;

  PetscFunctionBeginUser;
  PetscCheck(time == 0.0, mod->comm, PETSC_ERR_SUP, "No solution known for time %g", (double)time);
  dx[0] = x[0] - 1.5;
  dx[1] = x[1] - 1.0;
  r     = Norm2Real(dx);
  sigma = 0.5;
  u[0]  = 1 + 2 * PetscExpReal(-PetscSqr(r) / (2 * PetscSqr(sigma)));
  u[1]  = 0.0;
  u[2]  = 0.0;
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode PhysicsFunctional_SW(Model mod, PetscReal time, const PetscReal *coord, const PetscScalar *xx, PetscReal *f, PetscCtx ctx)
{
  Physics       phys = (Physics)ctx;
  Physics_SW   *sw   = (Physics_SW *)phys->data;
  const SWNode *x    = (const SWNode *)xx;
  PetscReal     u[2];
  PetscReal     h;

  PetscFunctionBeginUser;
  h = x->h;
  Scale2Real(1. / x->h, x->uh, u);
  f[sw->functional.Height] = h;
  f[sw->functional.Speed]  = Norm2Real(u) + PetscSqrtReal(sw->gravity * h);
  f[sw->functional.Energy] = 0.5 * (Dot2Real(x->uh, u) + sw->gravity * PetscSqr(h));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetUpBC_SW(DM dm, PetscDS prob, Physics phys)
{
  const PetscInt wallids[] = {100, 101, 200, 300};
  DMLabel        label;

  PetscFunctionBeginUser;
  PetscCall(DMGetLabel(dm, "Face Sets", &label));
  PetscCall(PetscDSAddBoundary(prob, DM_BC_NATURAL_RIEMANN, "wall", label, PETSC_STATIC_ARRAY_LENGTH(wallids), wallids, 0, 0, NULL, (PetscVoidFn *)PhysicsBoundary_SW_Wall, NULL, phys, NULL));
  PetscFunctionReturn(PETSC_SUCCESS);
}

#ifdef PETSC_HAVE_LIBCEED
static PetscErrorCode CreateQFunctionContext_SW(Physics phys, Ceed ceed, CeedQFunctionContext *qfCtx)
{
  Physics_SW *in = (Physics_SW *)phys->data;
  Physics_SW *sw;

  PetscFunctionBeginUser;
  PetscCall(PetscCalloc1(1, &sw));

  sw->gravity = in->gravity;

  PetscCallCEED(CeedQFunctionContextCreate(ceed, qfCtx));
  PetscCallCEED(CeedQFunctionContextSetData(*qfCtx, CEED_MEM_HOST, CEED_USE_POINTER, sizeof(*sw), sw));
  PetscCallCEED(CeedQFunctionContextSetDataDestroy(*qfCtx, CEED_MEM_HOST, FreeContextPetsc));
  PetscCallCEED(CeedQFunctionContextRegisterDouble(*qfCtx, "gravity", offsetof(Physics_SW, gravity), 1, "Acceleration due to gravity"));
  PetscFunctionReturn(PETSC_SUCCESS);
}
#endif

static PetscErrorCode SetupCEED_SW(DM dm, Physics physics)
{
#ifdef PETSC_HAVE_LIBCEED
  Ceed                 ceed;
  CeedQFunctionContext qfCtx;
#endif

  PetscFunctionBegin;
#ifdef PETSC_HAVE_LIBCEED
  PetscCall(DMGetCeed(dm, &ceed));
  PetscCall(CreateQFunctionContext_SW(physics, ceed, &qfCtx));
  PetscCall(DMCeedCreateFVM(dm, PETSC_TRUE, PhysicsRiemann_SW_Rusanov_CEED, PhysicsRiemann_SW_Rusanov_CEED_loc, qfCtx));
  PetscCallCEED(CeedQFunctionContextDestroy(&qfCtx));
#endif
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode PhysicsCreate_SW(Model mod, Physics phys, PetscOptionItems PetscOptionsObject)
{
  Physics_SW *sw;
  char        sw_riemann[64] = "rusanov";

  PetscFunctionBeginUser;
  phys->field_desc = PhysicsFields_SW;
  PetscCall(PetscNew(&sw));
  phys->data     = sw;
  mod->setupbc   = SetUpBC_SW;
  mod->setupCEED = SetupCEED_SW;

  PetscCall(PetscFunctionListAdd(&PhysicsRiemannList_SW, "rusanov", PhysicsRiemann_SW_Rusanov));
  PetscCall(PetscFunctionListAdd(&PhysicsRiemannList_SW, "hll", PhysicsRiemann_SW_HLL));
#ifdef PETSC_HAVE_LIBCEED
  PetscCall(PetscFunctionListAdd(&PhysicsRiemannList_SW, "rusanov_ceed", PhysicsRiemann_SW_Rusanov_CEED));
#endif

  PetscOptionsHeadBegin(PetscOptionsObject, "SW options");
  {
    void (*PhysicsRiemann_SW)(PetscInt, PetscInt, const PetscReal *, const PetscReal *, const PetscScalar *, const PetscScalar *, PetscInt, const PetscScalar, PetscScalar *, Physics);
    sw->gravity = 1.0;
    PetscCall(PetscOptionsReal("-sw_gravity", "Gravitational constant", "", sw->gravity, &sw->gravity, NULL));
    PetscCall(PetscOptionsFList("-sw_riemann", "Riemann solver", "", PhysicsRiemannList_SW, sw_riemann, sw_riemann, sizeof sw_riemann, NULL));
    PetscCall(PetscFunctionListFind(PhysicsRiemannList_SW, sw_riemann, &PhysicsRiemann_SW));
    phys->riemann = (PetscRiemannFn *)(PetscVoidFn *)PhysicsRiemann_SW;
  }
  PetscOptionsHeadEnd();
  phys->maxspeed = PetscSqrtReal(2.0 * sw->gravity); /* Mach 1 for depth of 2 */

  PetscCall(ModelSolutionSetDefault(mod, PhysicsSolution_SW, phys));
  PetscCall(ModelFunctionalRegister(mod, "Height", &sw->functional.Height, PhysicsFunctional_SW, phys));
  PetscCall(ModelFunctionalRegister(mod, "Speed", &sw->functional.Speed, PhysicsFunctional_SW, phys));
  PetscCall(ModelFunctionalRegister(mod, "Energy", &sw->functional.Energy, PhysicsFunctional_SW, phys));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/******************* Euler Density Shock (EULER_IV_SHOCK,EULER_SS_SHOCK) ********************/
/* An initial-value and self-similar solutions of the compressible Euler equations */
/* Ravi Samtaney and D. I. Pullin */
/* Phys. Fluids 8, 2650 (1996); http://dx.doi.org/10.1063/1.869050 */
static const struct FieldDescription PhysicsFields_Euler[] = {
  {"Density",  1  },
  {"Momentum", DIM},
  {"Energy",   1  },
  {NULL,       0  }
};

/* initial condition */
int                   initLinearWave(EulerNode *ux, const PetscReal gamma, const PetscReal coord[], const PetscReal Lx);
static PetscErrorCode PhysicsSolution_Euler(Model mod, PetscReal time, const PetscReal *x, PetscScalar *u, PetscCtx ctx)
{
  PetscInt       i;
  Physics        phys = (Physics)ctx;
  Physics_Euler *eu   = (Physics_Euler *)phys->data;
  EulerNode     *uu   = (EulerNode *)u;
  PetscReal      p0, gamma, c = 0.;

  PetscFunctionBeginUser;
  PetscCheck(time == 0.0, mod->comm, PETSC_ERR_SUP, "No solution known for time %g", (double)time);

  for (i = 0; i < DIM; i++) uu->ru[i] = 0.0; /* zero out initial velocity */
  /* set E and rho */
  gamma = eu->gamma;

  if (eu->type == EULER_IV_SHOCK || eu->type == EULER_SS_SHOCK) {
    /******************* Euler Density Shock ********************/
    /* On initial-value and self-similar solutions of the compressible Euler equations */
    /* Ravi Samtaney and D. I. Pullin */
    /* Phys. Fluids 8, 2650 (1996); http://dx.doi.org/10.1063/1.869050 */
    /* initial conditions 1: left of shock, 0: left of discontinuity 2: right of discontinuity,  */
    p0 = 1.;
    if (x[0] < 0.0 + x[1] * eu->itana) {
      if (x[0] < mod->bounds[0] * 0.5) { /* left of shock (1) */
        PetscReal amach, rho, press, gas1, p1;
        amach     = eu->amach;
        rho       = 1.;
        press     = p0;
        p1        = press * (1.0 + 2.0 * gamma / (gamma + 1.0) * (amach * amach - 1.0));
        gas1      = (gamma - 1.0) / (gamma + 1.0);
        uu->r     = rho * (p1 / press + gas1) / (gas1 * p1 / press + 1.0);
        uu->ru[0] = ((uu->r - rho) * PetscSqrtReal(gamma * press / rho) * amach);
        uu->E     = p1 / (gamma - 1.0) + .5 / uu->r * uu->ru[0] * uu->ru[0];
      } else {      /* left of discontinuity (0) */
        uu->r = 1.; /* rho = 1 */
        uu->E = p0 / (gamma - 1.0);
      }
    } else { /* right of discontinuity (2) */
      uu->r = eu->rhoR;
      uu->E = p0 / (gamma - 1.0);
    }
  } else if (eu->type == EULER_SHOCK_TUBE) {
    /* For (x<x0) set (rho,u,p)=(8,0,10) and for (x>x0) set (rho,u,p)=(1,0,1). Choose x0 to the midpoint of the domain in the x-direction. */
    if (x[0] < 0.0) {
      uu->r = 8.;
      uu->E = 10. / (gamma - 1.);
    } else {
      uu->r = 1.;
      uu->E = 1. / (gamma - 1.);
    }
  } else if (eu->type == EULER_LINEAR_WAVE) {
    initLinearWave(uu, gamma, x, mod->bounds[1] - mod->bounds[0]);
  } else SETERRQ(mod->comm, PETSC_ERR_SUP, "Unknown type %d", eu->type);

  /* set phys->maxspeed: (mod->maxspeed = phys->maxspeed) in main; */
  PetscCall(SpeedOfSound_PG(gamma, uu, &c));
  c = (uu->ru[0] / uu->r) + c;
  if (c > phys->maxspeed) phys->maxspeed = c;
  PetscFunctionReturn(PETSC_SUCCESS);
}

/* PetscReal* => EulerNode* conversion */
static PetscErrorCode PhysicsBoundary_Euler_Wall(PetscReal time, const PetscReal *c, const PetscReal *n, const PetscScalar *a_xI, PetscScalar *a_xG, PetscCtx ctx)
{
  PetscInt         i;
  const EulerNode *xI   = (const EulerNode *)a_xI;
  EulerNode       *xG   = (EulerNode *)a_xG;
  Physics          phys = (Physics)ctx;
  Physics_Euler   *eu   = (Physics_Euler *)phys->data;

  PetscFunctionBeginUser;
  xG->r = xI->r;                                     /* ghost cell density - same */
  xG->E = xI->E;                                     /* ghost cell energy - same */
  if (n[1] != 0.) {                                  /* top and bottom */
    xG->ru[0] = xI->ru[0];                           /* copy tang to wall */
    xG->ru[1] = -xI->ru[1];                          /* reflect perp to t/b wall */
  } else {                                           /* sides */
    for (i = 0; i < DIM; i++) xG->ru[i] = xI->ru[i]; /* copy */
  }
  if (eu->type == EULER_LINEAR_WAVE) { /* debug */
#if 0
    PetscPrintf(PETSC_COMM_WORLD,"%s coord=%g,%g\n",PETSC_FUNCTION_NAME,(double)c[0],(double)c[1]);
#endif
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode PhysicsFunctional_Euler(Model mod, PetscReal time, const PetscReal *coord, const PetscScalar *xx, PetscReal *f, PetscCtx ctx)
{
  Physics          phys = (Physics)ctx;
  Physics_Euler   *eu   = (Physics_Euler *)phys->data;
  const EulerNode *x    = (const EulerNode *)xx;
  PetscReal        p;

  PetscFunctionBeginUser;
  f[eu->monitor.Density]  = x->r;
  f[eu->monitor.Momentum] = NormDIM(x->ru);
  f[eu->monitor.Energy]   = x->E;
  f[eu->monitor.Speed]    = NormDIM(x->ru) / x->r;
  PetscCall(Pressure_PG(eu->gamma, x, &p));
  f[eu->monitor.Pressure] = p;
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetUpBC_Euler(DM dm, PetscDS prob, Physics phys)
{
  Physics_Euler *eu = (Physics_Euler *)phys->data;
  DMLabel        label;

  PetscFunctionBeginUser;
  PetscCall(DMGetLabel(dm, "Face Sets", &label));
  if (eu->type == EULER_LINEAR_WAVE) {
    const PetscInt wallids[] = {100, 101};
    PetscCall(PetscDSAddBoundary(prob, DM_BC_NATURAL_RIEMANN, "wall", label, PETSC_STATIC_ARRAY_LENGTH(wallids), wallids, 0, 0, NULL, (PetscVoidFn *)PhysicsBoundary_Euler_Wall, NULL, phys, NULL));
  } else {
    const PetscInt wallids[] = {100, 101, 200, 300};
    PetscCall(PetscDSAddBoundary(prob, DM_BC_NATURAL_RIEMANN, "wall", label, PETSC_STATIC_ARRAY_LENGTH(wallids), wallids, 0, 0, NULL, (PetscVoidFn *)PhysicsBoundary_Euler_Wall, NULL, phys, NULL));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

#ifdef PETSC_HAVE_LIBCEED
static PetscErrorCode CreateQFunctionContext_Euler(Physics phys, Ceed ceed, CeedQFunctionContext *qfCtx)
{
  Physics_Euler *in = (Physics_Euler *)phys->data;
  Physics_Euler *eu;

  PetscFunctionBeginUser;
  PetscCall(PetscCalloc1(1, &eu));

  eu->gamma = in->gamma;

  PetscCallCEED(CeedQFunctionContextCreate(ceed, qfCtx));
  PetscCallCEED(CeedQFunctionContextSetData(*qfCtx, CEED_MEM_HOST, CEED_USE_POINTER, sizeof(*eu), eu));
  PetscCallCEED(CeedQFunctionContextSetDataDestroy(*qfCtx, CEED_MEM_HOST, FreeContextPetsc));
  PetscCallCEED(CeedQFunctionContextRegisterDouble(*qfCtx, "gamma", offsetof(Physics_Euler, gamma), 1, "Heat capacity ratio"));
  PetscFunctionReturn(PETSC_SUCCESS);
}
#endif

static PetscErrorCode SetupCEED_Euler(DM dm, Physics physics)
{
#ifdef PETSC_HAVE_LIBCEED
  Ceed                 ceed;
  CeedQFunctionContext qfCtx;
#endif

  PetscFunctionBegin;
#ifdef PETSC_HAVE_LIBCEED
  PetscCall(DMGetCeed(dm, &ceed));
  PetscCall(CreateQFunctionContext_Euler(physics, ceed, &qfCtx));
  PetscCall(DMCeedCreateFVM(dm, PETSC_TRUE, PhysicsRiemann_Euler_Godunov_CEED, PhysicsRiemann_Euler_Godunov_CEED_loc, qfCtx));
  PetscCallCEED(CeedQFunctionContextDestroy(&qfCtx));
#endif
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode PhysicsCreate_Euler(Model mod, Physics phys, PetscOptionItems PetscOptionsObject)
{
  Physics_Euler *eu;

  PetscFunctionBeginUser;
  phys->field_desc = PhysicsFields_Euler;
  phys->riemann    = (PetscRiemannFn *)(PetscVoidFn *)PhysicsRiemann_Euler_Godunov;
  PetscCall(PetscNew(&eu));
  phys->data     = eu;
  mod->setupbc   = SetUpBC_Euler;
  mod->setupCEED = SetupCEED_Euler;

  PetscCall(PetscFunctionListAdd(&PhysicsRiemannList_Euler, "godunov", PhysicsRiemann_Euler_Godunov));
#ifdef PETSC_HAVE_LIBCEED
  PetscCall(PetscFunctionListAdd(&PhysicsRiemannList_Euler, "godunov_ceed", PhysicsRiemann_Euler_Godunov_CEED));
#endif

  PetscOptionsHeadBegin(PetscOptionsObject, "Euler options");
  {
    void (*PhysicsRiemann_Euler)(PetscInt, PetscInt, const PetscReal *, const PetscReal *, const PetscScalar *, const PetscScalar *, PetscInt, const PetscScalar, PetscScalar *, Physics);
    PetscReal alpha;
    char      type[64]       = "linear_wave";
    char      eu_riemann[64] = "godunov";
    PetscBool is;
    eu->gamma = 1.4;
    eu->amach = 2.02;
    eu->rhoR  = 3.0;
    eu->itana = 0.57735026918963; /* angle of Euler self similar (SS) shock */
    PetscCall(PetscOptionsFList("-eu_riemann", "Riemann solver", "", PhysicsRiemannList_Euler, eu_riemann, eu_riemann, sizeof eu_riemann, NULL));
    PetscCall(PetscFunctionListFind(PhysicsRiemannList_Euler, eu_riemann, &PhysicsRiemann_Euler));
    phys->riemann = (PetscRiemannFn *)(PetscVoidFn *)PhysicsRiemann_Euler;
    PetscCall(PetscOptionsReal("-eu_gamma", "Heat capacity ratio", "", eu->gamma, &eu->gamma, NULL));
    PetscCall(PetscOptionsReal("-eu_amach", "Shock speed (Mach)", "", eu->amach, &eu->amach, NULL));
    PetscCall(PetscOptionsReal("-eu_rho2", "Density right of discontinuity", "", eu->rhoR, &eu->rhoR, NULL));
    alpha = 60.;
    PetscCall(PetscOptionsRangeReal("-eu_alpha", "Angle of discontinuity", "", alpha, &alpha, NULL, 0.0, 90.0));
    eu->itana = 1. / PetscTanReal(alpha * PETSC_PI / 180.0);
    PetscCall(PetscOptionsString("-eu_type", "Type of Euler test", "", type, type, sizeof(type), NULL));
    PetscCall(PetscStrcmp(type, "linear_wave", &is));
    if (is) {
      /* Remember this should be periodic */
      eu->type = EULER_LINEAR_WAVE;
      PetscCall(PetscPrintf(PETSC_COMM_WORLD, "%s set Euler type: %s\n", PETSC_FUNCTION_NAME, "linear_wave"));
    } else {
      PetscCheck(DIM == 2, PETSC_COMM_WORLD, PETSC_ERR_SUP, "DIM must be 2 unless linear wave test %s", type);
      PetscCall(PetscStrcmp(type, "iv_shock", &is));
      if (is) {
        eu->type = EULER_IV_SHOCK;
        PetscCall(PetscPrintf(PETSC_COMM_WORLD, "%s set Euler type: %s\n", PETSC_FUNCTION_NAME, "iv_shock"));
      } else {
        PetscCall(PetscStrcmp(type, "ss_shock", &is));
        if (is) {
          eu->type = EULER_SS_SHOCK;
          PetscCall(PetscPrintf(PETSC_COMM_WORLD, "%s set Euler type: %s\n", PETSC_FUNCTION_NAME, "ss_shock"));
        } else {
          PetscCall(PetscStrcmp(type, "shock_tube", &is));
          PetscCheck(is, PETSC_COMM_WORLD, PETSC_ERR_SUP, "Unknown Euler type %s", type);
          eu->type = EULER_SHOCK_TUBE;
          PetscCall(PetscPrintf(PETSC_COMM_WORLD, "%s set Euler type: %s\n", PETSC_FUNCTION_NAME, "shock_tube"));
        }
      }
    }
  }
  PetscOptionsHeadEnd();
  phys->maxspeed = 0.; /* will get set in solution */
  PetscCall(ModelSolutionSetDefault(mod, PhysicsSolution_Euler, phys));
  PetscCall(ModelFunctionalRegister(mod, "Speed", &eu->monitor.Speed, PhysicsFunctional_Euler, phys));
  PetscCall(ModelFunctionalRegister(mod, "Energy", &eu->monitor.Energy, PhysicsFunctional_Euler, phys));
  PetscCall(ModelFunctionalRegister(mod, "Density", &eu->monitor.Density, PhysicsFunctional_Euler, phys));
  PetscCall(ModelFunctionalRegister(mod, "Momentum", &eu->monitor.Momentum, PhysicsFunctional_Euler, phys));
  PetscCall(ModelFunctionalRegister(mod, "Pressure", &eu->monitor.Pressure, PhysicsFunctional_Euler, phys));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode ErrorIndicator_Simple(PetscInt dim, PetscReal volume, PetscInt numComps, const PetscScalar u[], const PetscScalar grad[], PetscReal *error, PetscCtx ctx)
{
  PetscReal err = 0.;
  PetscInt  i, j;

  PetscFunctionBeginUser;
  for (i = 0; i < numComps; i++) {
    for (j = 0; j < dim; j++) err += PetscSqr(PetscRealPart(grad[i * dim + j]));
  }
  *error = volume * err;
  PetscFunctionReturn(PETSC_SUCCESS);
}

PetscErrorCode CreatePartitionVec(DM dm, DM *dmCell, Vec *partition)
{
  PetscSF      sfPoint;
  PetscSection coordSection;
  Vec          coordinates;
  PetscSection sectionCell;
  PetscScalar *part;
  PetscInt     cStart, cEnd, c;
  PetscMPIInt  rank;

  PetscFunctionBeginUser;
  PetscCall(DMGetCoordinateSection(dm, &coordSection));
  PetscCall(DMGetCoordinatesLocal(dm, &coordinates));
  PetscCall(DMClone(dm, dmCell));
  PetscCall(DMGetPointSF(dm, &sfPoint));
  PetscCall(DMSetPointSF(*dmCell, sfPoint));
  PetscCall(DMSetCoordinateSection(*dmCell, PETSC_DETERMINE, coordSection));
  PetscCall(DMSetCoordinatesLocal(*dmCell, coordinates));
  PetscCallMPI(MPI_Comm_rank(PetscObjectComm((PetscObject)dm), &rank));
  PetscCall(PetscSectionCreate(PetscObjectComm((PetscObject)dm), &sectionCell));
  PetscCall(DMPlexGetHeightStratum(*dmCell, 0, &cStart, &cEnd));
  PetscCall(PetscSectionSetChart(sectionCell, cStart, cEnd));
  for (c = cStart; c < cEnd; ++c) PetscCall(PetscSectionSetDof(sectionCell, c, 1));
  PetscCall(PetscSectionSetUp(sectionCell));
  PetscCall(DMSetLocalSection(*dmCell, sectionCell));
  PetscCall(PetscSectionDestroy(&sectionCell));
  PetscCall(DMCreateLocalVector(*dmCell, partition));
  PetscCall(PetscObjectSetName((PetscObject)*partition, "partition"));
  PetscCall(VecGetArray(*partition, &part));
  for (c = cStart; c < cEnd; ++c) {
    PetscScalar *p;

    PetscCall(DMPlexPointLocalRef(*dmCell, c, part, &p));
    p[0] = rank;
  }
  PetscCall(VecRestoreArray(*partition, &part));
  PetscFunctionReturn(PETSC_SUCCESS);
}

PetscErrorCode CreateMassMatrix(DM dm, Vec *massMatrix, User user)
{
  DM                 plex, dmMass, dmFace, dmCell, dmCoord;
  PetscSection       coordSection;
  Vec                coordinates, facegeom, cellgeom;
  PetscSection       sectionMass;
  PetscScalar       *m;
  const PetscScalar *fgeom, *cgeom, *coords;
  PetscInt           vStart, vEnd, v;

  PetscFunctionBeginUser;
  PetscCall(DMConvert(dm, DMPLEX, &plex));
  PetscCall(DMGetCoordinateSection(dm, &coordSection));
  PetscCall(DMGetCoordinatesLocal(dm, &coordinates));
  PetscCall(DMClone(dm, &dmMass));
  PetscCall(DMSetCoordinateSection(dmMass, PETSC_DETERMINE, coordSection));
  PetscCall(DMSetCoordinatesLocal(dmMass, coordinates));
  PetscCall(PetscSectionCreate(PetscObjectComm((PetscObject)dm), &sectionMass));
  PetscCall(DMPlexGetDepthStratum(dm, 0, &vStart, &vEnd));
  PetscCall(PetscSectionSetChart(sectionMass, vStart, vEnd));
  for (v = vStart; v < vEnd; ++v) {
    PetscInt numFaces;

    PetscCall(DMPlexGetSupportSize(dmMass, v, &numFaces));
    PetscCall(PetscSectionSetDof(sectionMass, v, numFaces * numFaces));
  }
  PetscCall(PetscSectionSetUp(sectionMass));
  PetscCall(DMSetLocalSection(dmMass, sectionMass));
  PetscCall(PetscSectionDestroy(&sectionMass));
  PetscCall(DMGetLocalVector(dmMass, massMatrix));
  PetscCall(VecGetArray(*massMatrix, &m));
  PetscCall(DMPlexGetGeometryFVM(plex, &facegeom, &cellgeom, NULL));
  PetscCall(VecGetDM(facegeom, &dmFace));
  PetscCall(VecGetArrayRead(facegeom, &fgeom));
  PetscCall(VecGetDM(cellgeom, &dmCell));
  PetscCall(VecGetArrayRead(cellgeom, &cgeom));
  PetscCall(DMGetCoordinateDM(dm, &dmCoord));
  PetscCall(VecGetArrayRead(coordinates, &coords));
  for (v = vStart; v < vEnd; ++v) {
    const PetscInt  *faces;
    PetscFVFaceGeom *fgA, *fgB, *cg;
    PetscScalar     *vertex;
    PetscInt         numFaces, sides[2], f, g;

    PetscCall(DMPlexPointLocalRead(dmCoord, v, coords, &vertex));
    PetscCall(DMPlexGetSupportSize(dmMass, v, &numFaces));
    PetscCall(DMPlexGetSupport(dmMass, v, &faces));
    for (f = 0; f < numFaces; ++f) {
      sides[0] = faces[f];
      PetscCall(DMPlexPointLocalRead(dmFace, faces[f], fgeom, &fgA));
      for (g = 0; g < numFaces; ++g) {
        const PetscInt *cells = NULL;
        PetscReal       area  = 0.0;
        PetscInt        numCells;

        sides[1] = faces[g];
        PetscCall(DMPlexPointLocalRead(dmFace, faces[g], fgeom, &fgB));
        PetscCall(DMPlexGetJoin(dmMass, 2, sides, &numCells, &cells));
        PetscCheck(numCells == 1, PETSC_COMM_SELF, PETSC_ERR_LIB, "Invalid join for faces");
        PetscCall(DMPlexPointLocalRead(dmCell, cells[0], cgeom, &cg));
        area += PetscAbsScalar((vertex[0] - cg->centroid[0]) * (fgA->centroid[1] - cg->centroid[1]) - (vertex[1] - cg->centroid[1]) * (fgA->centroid[0] - cg->centroid[0]));
        area += PetscAbsScalar((vertex[0] - cg->centroid[0]) * (fgB->centroid[1] - cg->centroid[1]) - (vertex[1] - cg->centroid[1]) * (fgB->centroid[0] - cg->centroid[0]));
        m[f * numFaces + g] = Dot2Real(fgA->normal, fgB->normal) * area * 0.5;
        PetscCall(DMPlexRestoreJoin(dmMass, 2, sides, &numCells, &cells));
      }
    }
  }
  PetscCall(VecRestoreArrayRead(facegeom, &fgeom));
  PetscCall(VecRestoreArrayRead(cellgeom, &cgeom));
  PetscCall(VecRestoreArrayRead(coordinates, &coords));
  PetscCall(VecRestoreArray(*massMatrix, &m));
  PetscCall(DMDestroy(&dmMass));
  PetscCall(DMDestroy(&plex));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/* Behavior will be different for multi-physics or when using non-default boundary conditions */
static PetscErrorCode ModelSolutionSetDefault(Model mod, SolutionFunction func, PetscCtx ctx)
{
  PetscFunctionBeginUser;
  mod->solution    = func;
  mod->solutionctx = ctx;
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode ModelFunctionalRegister(Model mod, const char *name, PetscInt *offset, FunctionalFunction func, PetscCtx ctx)
{
  FunctionalLink link, *ptr;
  PetscInt       lastoffset = -1;

  PetscFunctionBeginUser;
  for (ptr = &mod->functionalRegistry; *ptr; ptr = &(*ptr)->next) lastoffset = (*ptr)->offset;
  PetscCall(PetscNew(&link));
  PetscCall(PetscStrallocpy(name, &link->name));
  link->offset = lastoffset + 1;
  link->func   = func;
  link->ctx    = ctx;
  link->next   = NULL;
  *ptr         = link;
  *offset      = link->offset;
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode ModelFunctionalSetFromOptions(Model mod, PetscOptionItems PetscOptionsObject)
{
  PetscInt       i, j;
  FunctionalLink link;
  char          *names[256];

  PetscFunctionBeginUser;
  mod->numMonitored = PETSC_STATIC_ARRAY_LENGTH(names);
  PetscCall(PetscOptionsStringArray("-monitor", "list of functionals to monitor", "", names, &mod->numMonitored, NULL));
  /* Create list of functionals that will be computed somehow */
  PetscCall(PetscMalloc1(mod->numMonitored, &mod->functionalMonitored));
  /* Create index of calls that we will have to make to compute these functionals (over-allocation in general). */
  PetscCall(PetscMalloc1(mod->numMonitored, &mod->functionalCall));
  mod->numCall = 0;
  for (i = 0; i < mod->numMonitored; i++) {
    for (link = mod->functionalRegistry; link; link = link->next) {
      PetscBool match;
      PetscCall(PetscStrcasecmp(names[i], link->name, &match));
      if (match) break;
    }
    PetscCheck(link, mod->comm, PETSC_ERR_USER, "No known functional '%s'", names[i]);
    mod->functionalMonitored[i] = link;
    for (j = 0; j < i; j++) {
      if (mod->functionalCall[j]->func == link->func && mod->functionalCall[j]->ctx == link->ctx) goto next_name;
    }
    mod->functionalCall[mod->numCall++] = link; /* Just points to the first link using the result. There may be more results. */
  next_name:
    PetscCall(PetscFree(names[i]));
  }

  /* Find out the maximum index of any functional computed by a function we will be calling (even if we are not using it) */
  mod->maxComputed = -1;
  for (link = mod->functionalRegistry; link; link = link->next) {
    for (i = 0; i < mod->numCall; i++) {
      FunctionalLink call = mod->functionalCall[i];
      if (link->func == call->func && link->ctx == call->ctx) mod->maxComputed = PetscMax(mod->maxComputed, link->offset);
    }
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode FunctionalLinkDestroy(FunctionalLink *link)
{
  FunctionalLink l, next;

  PetscFunctionBeginUser;
  if (!link) PetscFunctionReturn(PETSC_SUCCESS);
  l     = *link;
  *link = NULL;
  for (; l; l = next) {
    next = l->next;
    PetscCall(PetscFree(l->name));
    PetscCall(PetscFree(l));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

/* put the solution callback into a functional callback */
static PetscErrorCode SolutionFunctional(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *u, void *modctx)
{
  Model mod;

  PetscFunctionBeginUser;
  mod = (Model)modctx;
  PetscCall((*mod->solution)(mod, time, x, u, mod->solutionctx));
  PetscFunctionReturn(PETSC_SUCCESS);
}

PetscErrorCode SetInitialCondition(DM dm, Vec X, User user)
{
  PetscErrorCode (*func[1])(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *u, PetscCtx ctx);
  PetscCtx ctx[1];
  Model    mod = user->model;

  PetscFunctionBeginUser;
  func[0] = SolutionFunctional;
  ctx[0]  = (void *)mod;
  PetscCall(DMProjectFunction(dm, 0.0, func, ctx, INSERT_ALL_VALUES, X));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode OutputVTK(DM dm, const char *filename, PetscViewer *viewer)
{
  PetscFunctionBeginUser;
  PetscCall(PetscViewerCreate(PetscObjectComm((PetscObject)dm), viewer));
  PetscCall(PetscViewerSetType(*viewer, PETSCVIEWERVTK));
  PetscCall(PetscViewerFileSetName(*viewer, filename));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode MonitorVTK(TS ts, PetscInt stepnum, PetscReal time, Vec X, PetscCtx ctx)
{
  User        user = (User)ctx;
  DM          dm, plex;
  PetscViewer viewer;
  char        filename[PETSC_MAX_PATH_LEN], *ftable = NULL;
  PetscReal   xnorm;
  PetscBool   rollback;

  PetscFunctionBeginUser;
  PetscCall(TSGetStepRollBack(ts, &rollback));
  if (rollback) PetscFunctionReturn(PETSC_SUCCESS);
  PetscCall(PetscObjectSetName((PetscObject)X, "u"));
  PetscCall(VecGetDM(X, &dm));
  PetscCall(VecNorm(X, NORM_INFINITY, &xnorm));

  if (stepnum >= 0) stepnum += user->monitorStepOffset;
  if (stepnum >= 0) { /* No summary for final time */
    Model              mod = user->model;
    Vec                cellgeom;
    PetscInt           c, cStart, cEnd, fcount, i;
    size_t             ftableused, ftablealloc;
    const PetscScalar *cgeom, *x;
    DM                 dmCell;
    DMLabel            vtkLabel;
    PetscReal         *fmin, *fmax, *fintegral, *ftmp;

    PetscCall(DMConvert(dm, DMPLEX, &plex));
    PetscCall(DMPlexGetGeometryFVM(plex, NULL, &cellgeom, NULL));
    fcount = mod->maxComputed + 1;
    PetscCall(PetscMalloc4(fcount, &fmin, fcount, &fmax, fcount, &fintegral, fcount, &ftmp));
    for (i = 0; i < fcount; i++) {
      fmin[i]      = PETSC_MAX_REAL;
      fmax[i]      = PETSC_MIN_REAL;
      fintegral[i] = 0;
    }
    PetscCall(VecGetDM(cellgeom, &dmCell));
    PetscCall(DMPlexGetSimplexOrBoxCells(dmCell, 0, &cStart, &cEnd));
    PetscCall(VecGetArrayRead(cellgeom, &cgeom));
    PetscCall(VecGetArrayRead(X, &x));
    PetscCall(DMGetLabel(dm, "vtk", &vtkLabel));
    for (c = cStart; c < cEnd; ++c) {
      PetscFVCellGeom   *cg;
      const PetscScalar *cx     = NULL;
      PetscInt           vtkVal = 0;

      /* not that these two routines as currently implemented work for any dm with a
       * localSection/globalSection */
      PetscCall(DMPlexPointLocalRead(dmCell, c, cgeom, &cg));
      PetscCall(DMPlexPointGlobalRead(dm, c, x, &cx));
      if (vtkLabel) PetscCall(DMLabelGetValue(vtkLabel, c, &vtkVal));
      if (!vtkVal || !cx) continue; /* ghost, or not a global cell */
      for (i = 0; i < mod->numCall; i++) {
        FunctionalLink flink = mod->functionalCall[i];
        PetscCall((*flink->func)(mod, time, cg->centroid, cx, ftmp, flink->ctx));
      }
      for (i = 0; i < fcount; i++) {
        fmin[i] = PetscMin(fmin[i], ftmp[i]);
        fmax[i] = PetscMax(fmax[i], ftmp[i]);
        fintegral[i] += cg->volume * ftmp[i];
      }
    }
    PetscCall(VecRestoreArrayRead(cellgeom, &cgeom));
    PetscCall(VecRestoreArrayRead(X, &x));
    PetscCall(DMDestroy(&plex));
    PetscCallMPI(MPIU_Allreduce(MPI_IN_PLACE, fmin, (PetscMPIInt)fcount, MPIU_REAL, MPIU_MIN, PetscObjectComm((PetscObject)ts)));
    PetscCallMPI(MPIU_Allreduce(MPI_IN_PLACE, fmax, (PetscMPIInt)fcount, MPIU_REAL, MPIU_MAX, PetscObjectComm((PetscObject)ts)));
    PetscCallMPI(MPIU_Allreduce(MPI_IN_PLACE, fintegral, (PetscMPIInt)fcount, MPIU_REAL, MPIU_SUM, PetscObjectComm((PetscObject)ts)));

    ftablealloc = fcount * 100;
    ftableused  = 0;
    PetscCall(PetscMalloc1(ftablealloc, &ftable));
    for (i = 0; i < mod->numMonitored; i++) {
      size_t         countused;
      char           buffer[256], *p;
      FunctionalLink flink = mod->functionalMonitored[i];
      PetscInt       id    = flink->offset;
      if (i % 3) {
        PetscCall(PetscArraycpy(buffer, "  ", 2));
        p = buffer + 2;
      } else if (i) {
        char newline[] = "\n";
        PetscCall(PetscMemcpy(buffer, newline, sizeof(newline) - 1));
        p = buffer + sizeof(newline) - 1;
      } else {
        p = buffer;
      }
      PetscCall(PetscSNPrintfCount(p, sizeof buffer - (p - buffer), "%12s [%10.7g,%10.7g] int %10.7g", &countused, flink->name, (double)fmin[id], (double)fmax[id], (double)fintegral[id]));
      countused--;
      countused += p - buffer;
      if (countused > ftablealloc - ftableused - 1) { /* reallocate */
        char *ftablenew;
        ftablealloc = 2 * ftablealloc + countused;
        PetscCall(PetscMalloc(ftablealloc, &ftablenew));
        PetscCall(PetscArraycpy(ftablenew, ftable, ftableused));
        PetscCall(PetscFree(ftable));
        ftable = ftablenew;
      }
      PetscCall(PetscArraycpy(ftable + ftableused, buffer, countused));
      ftableused += countused;
      ftable[ftableused] = 0;
    }
    PetscCall(PetscFree4(fmin, fmax, fintegral, ftmp));

    PetscCall(PetscPrintf(PetscObjectComm((PetscObject)ts), "% 3" PetscInt_FMT "  time %8.4g  |x| %8.4g  %s\n", stepnum, (double)time, (double)xnorm, ftable ? ftable : ""));
    PetscCall(PetscFree(ftable));
  }
  if (user->vtkInterval < 1) PetscFunctionReturn(PETSC_SUCCESS);
  if ((stepnum == -1) ^ (stepnum % user->vtkInterval == 0)) {
    if (stepnum == -1) { /* Final time is not multiple of normal time interval, write it anyway */
      PetscCall(TSGetStepNumber(ts, &stepnum));
    }
    PetscCall(PetscSNPrintf(filename, sizeof filename, "%s-%03" PetscInt_FMT ".vtu", user->outputBasename, stepnum));
    PetscCall(OutputVTK(dm, filename, &viewer));
    PetscCall(VecView(X, viewer));
    PetscCall(PetscViewerDestroy(&viewer));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode initializeTS(DM dm, User user, TS *ts)
{
#ifdef PETSC_HAVE_LIBCEED
  PetscBool useCeed;
#endif

  PetscFunctionBeginUser;
  PetscCall(TSCreate(PetscObjectComm((PetscObject)dm), ts));
  PetscCall(TSSetType(*ts, TSSSP));
  PetscCall(TSSetDM(*ts, dm));
  if (user->vtkmon) PetscCall(TSMonitorSet(*ts, MonitorVTK, user, NULL));
  PetscCall(DMTSSetBoundaryLocal(dm, DMPlexTSComputeBoundary, user));
#ifdef PETSC_HAVE_LIBCEED
  PetscCall(DMPlexGetUseCeed(dm, &useCeed));
  if (useCeed) PetscCall(DMTSSetRHSFunctionLocal(dm, DMPlexTSComputeRHSFunctionFVMCEED, user));
  else
#endif
    PetscCall(DMTSSetRHSFunctionLocal(dm, DMPlexTSComputeRHSFunctionFVM, user));
  PetscCall(TSSetMaxTime(*ts, 2.0));
  PetscCall(TSSetExactFinalTime(*ts, TS_EXACTFINALTIME_STEPOVER));
  PetscFunctionReturn(PETSC_SUCCESS);
}

typedef struct {
  PetscFV      fvm;
  VecTagger    refineTag;
  VecTagger    coarsenTag;
  DM           adaptedDM;
  User         user;
  PetscReal    cfl;
  PetscLimiter limiter;
  PetscLimiter noneLimiter;
} TransferCtx;

static PetscErrorCode adaptToleranceFVMSetUp(TS ts, PetscInt nstep, PetscReal time, Vec sol, PetscBool *resize, PetscCtx ctx)
{
  TransferCtx       *tctx       = (TransferCtx *)ctx;
  PetscFV            fvm        = tctx->fvm;
  VecTagger          refineTag  = tctx->refineTag;
  VecTagger          coarsenTag = tctx->coarsenTag;
  User               user       = tctx->user;
  DM                 dm, gradDM, plex, cellDM, adaptedDM = NULL;
  Vec                cellGeom, faceGeom;
  PetscBool          computeGradient;
  Vec                grad, locGrad, locX, errVec;
  PetscInt           cStart, cEnd, c, dim, nRefine, nCoarsen;
  PetscReal          minMaxInd[2] = {PETSC_MAX_REAL, PETSC_MIN_REAL}, minMaxIndGlobal[2];
  PetscScalar       *errArray;
  const PetscScalar *pointVals;
  const PetscScalar *pointGrads;
  const PetscScalar *pointGeom;
  DMLabel            adaptLabel = NULL;
  IS                 refineIS, coarsenIS;

  PetscFunctionBeginUser;
  *resize = PETSC_FALSE;
  PetscCall(VecGetDM(sol, &dm));
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(PetscFVSetLimiter(fvm, tctx->noneLimiter));
  PetscCall(PetscFVGetComputeGradients(fvm, &computeGradient));
  PetscCall(PetscFVSetComputeGradients(fvm, PETSC_TRUE));
  PetscCall(DMConvert(dm, DMPLEX, &plex));
  PetscCall(DMPlexGetDataFVM(plex, fvm, &cellGeom, &faceGeom, &gradDM));
  PetscCall(DMCreateLocalVector(plex, &locX));
  PetscCall(DMPlexInsertBoundaryValues(plex, PETSC_TRUE, locX, 0.0, faceGeom, cellGeom, NULL));
  PetscCall(DMGlobalToLocalBegin(plex, sol, INSERT_VALUES, locX));
  PetscCall(DMGlobalToLocalEnd(plex, sol, INSERT_VALUES, locX));
  PetscCall(DMCreateGlobalVector(gradDM, &grad));
  PetscCall(DMPlexReconstructGradientsFVM(plex, locX, grad));
  PetscCall(DMCreateLocalVector(gradDM, &locGrad));
  PetscCall(DMGlobalToLocalBegin(gradDM, grad, INSERT_VALUES, locGrad));
  PetscCall(DMGlobalToLocalEnd(gradDM, grad, INSERT_VALUES, locGrad));
  PetscCall(VecDestroy(&grad));
  PetscCall(DMPlexGetSimplexOrBoxCells(plex, 0, &cStart, &cEnd));
  PetscCall(VecGetArrayRead(locGrad, &pointGrads));
  PetscCall(VecGetArrayRead(cellGeom, &pointGeom));
  PetscCall(VecGetArrayRead(locX, &pointVals));
  PetscCall(VecGetDM(cellGeom, &cellDM));
  PetscCall(DMLabelCreate(PETSC_COMM_SELF, "adapt", &adaptLabel));
  PetscCall(VecCreateFromOptions(PetscObjectComm((PetscObject)plex), NULL, 1, cEnd - cStart, PETSC_DETERMINE, &errVec));
  PetscCall(VecSetUp(errVec));
  PetscCall(VecGetArray(errVec, &errArray));
  for (c = cStart; c < cEnd; c++) {
    PetscReal        errInd = 0.;
    PetscScalar     *pointGrad;
    PetscScalar     *pointVal;
    PetscFVCellGeom *cg;

    PetscCall(DMPlexPointLocalRead(gradDM, c, pointGrads, &pointGrad));
    PetscCall(DMPlexPointLocalRead(cellDM, c, pointGeom, &cg));
    PetscCall(DMPlexPointLocalRead(plex, c, pointVals, &pointVal));

    PetscCall((*user->model->errorIndicator)(dim, cg->volume, user->model->physics->dof, pointVal, pointGrad, &errInd, user->model->errorCtx));
    errArray[c - cStart] = errInd;
    minMaxInd[0]         = PetscMin(minMaxInd[0], errInd);
    minMaxInd[1]         = PetscMax(minMaxInd[1], errInd);
  }
  PetscCall(VecRestoreArray(errVec, &errArray));
  PetscCall(VecRestoreArrayRead(locX, &pointVals));
  PetscCall(VecRestoreArrayRead(cellGeom, &pointGeom));
  PetscCall(VecRestoreArrayRead(locGrad, &pointGrads));
  PetscCall(VecDestroy(&locGrad));
  PetscCall(VecDestroy(&locX));
  PetscCall(DMDestroy(&plex));

  PetscCall(VecTaggerComputeIS(refineTag, errVec, &refineIS, NULL));
  PetscCall(VecTaggerComputeIS(coarsenTag, errVec, &coarsenIS, NULL));
  PetscCall(ISGetSize(refineIS, &nRefine));
  PetscCall(ISGetSize(coarsenIS, &nCoarsen));
  if (nRefine) PetscCall(DMLabelSetStratumIS(adaptLabel, DM_ADAPT_REFINE, refineIS));
  if (nCoarsen) PetscCall(DMLabelSetStratumIS(adaptLabel, DM_ADAPT_COARSEN, coarsenIS));
  PetscCall(ISDestroy(&coarsenIS));
  PetscCall(ISDestroy(&refineIS));
  PetscCall(VecDestroy(&errVec));

  PetscCall(PetscFVSetComputeGradients(fvm, computeGradient));
  PetscCall(PetscFVSetLimiter(fvm, tctx->limiter));
  minMaxInd[1] = -minMaxInd[1];
  PetscCallMPI(MPIU_Allreduce(minMaxInd, minMaxIndGlobal, 2, MPIU_REAL, MPI_MIN, PetscObjectComm((PetscObject)dm)));
  PetscCall(PetscInfo(ts, "error indicator range (%E, %E)\n", (double)minMaxIndGlobal[0], (double)(-minMaxIndGlobal[1])));
  if (nRefine || nCoarsen) { /* at least one cell is over the refinement threshold */
    PetscCall(DMAdaptLabel(dm, adaptLabel, &adaptedDM));
  }
  PetscCall(DMLabelDestroy(&adaptLabel));
  if (adaptedDM) {
    tctx->adaptedDM = adaptedDM;
    PetscCall(PetscInfo(ts, "Step %" PetscInt_FMT " adapted mesh, marking %" PetscInt_FMT " cells for refinement, and %" PetscInt_FMT " cells for coarsening\n", nstep, nRefine, nCoarsen));
    *resize = PETSC_TRUE;
  } else {
    PetscCall(PetscInfo(ts, "Step %" PetscInt_FMT " no adaptation\n", nstep));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode Transfer(TS ts, PetscInt nv, Vec vecsin[], Vec vecsout[], PetscCtx ctx)
{
  TransferCtx *tctx = (TransferCtx *)ctx;
  DM           dm;
  PetscReal    time;

  PetscFunctionBeginUser;
  PetscCall(TSGetDM(ts, &dm));
  PetscCall(TSGetTime(ts, &time));
  PetscCheck(tctx->adaptedDM, PetscObjectComm((PetscObject)ts), PETSC_ERR_ARG_WRONGSTATE, "Missing adaptedDM");
  for (PetscInt i = 0; i < nv; i++) {
    PetscCall(DMCreateGlobalVector(tctx->adaptedDM, &vecsout[i]));
    PetscCall(DMForestTransferVec(dm, vecsin[i], tctx->adaptedDM, vecsout[i], PETSC_TRUE, time));
  }
  PetscCall(DMForestSetAdaptivityForest(tctx->adaptedDM, NULL)); /* clear internal references to the previous dm */

  Model     mod  = tctx->user->model;
  Physics   phys = mod->physics;
  PetscReal minRadius;

  PetscCall(DMPlexGetGeometryFVM(tctx->adaptedDM, NULL, NULL, &minRadius));
  PetscCallMPI(MPIU_Allreduce(&phys->maxspeed, &mod->maxspeed, 1, MPIU_REAL, MPIU_MAX, PetscObjectComm((PetscObject)ts)));
  PetscCheck(mod->maxspeed > 0, PetscObjectComm((PetscObject)ts), PETSC_ERR_ARG_WRONGSTATE, "Physics did not set maxspeed");

  PetscReal dt = tctx->cfl * minRadius / mod->maxspeed;
  PetscCall(TSSetTimeStep(ts, dt));

  PetscCall(TSSetDM(ts, tctx->adaptedDM));
  PetscCall(DMDestroy(&tctx->adaptedDM));
  PetscFunctionReturn(PETSC_SUCCESS);
}

int main(int argc, char **argv)
{
  MPI_Comm          comm;
  PetscDS           prob;
  PetscFV           fvm;
  PetscLimiter      limiter = NULL, noneLimiter = NULL;
  User              user;
  Model             mod;
  Physics           phys;
  DM                dm, plex;
  PetscReal         ftime, cfl, dt, minRadius;
  PetscInt          dim, nsteps;
  TS                ts;
  TSConvergedReason reason;
  Vec               X;
  PetscViewer       viewer;
  PetscBool         vtkCellGeom, useAMR;
  PetscInt          adaptInterval;
  char              physname[256] = "advect";
  VecTagger         refineTag = NULL, coarsenTag = NULL;
  TransferCtx       tctx;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  comm = PETSC_COMM_WORLD;

  PetscCall(PetscNew(&user));
  PetscCall(PetscNew(&user->model));
  PetscCall(PetscNew(&user->model->physics));
  mod           = user->model;
  phys          = mod->physics;
  mod->comm     = comm;
  useAMR        = PETSC_FALSE;
  adaptInterval = 1;

  /* Register physical models to be available on the command line */
  PetscCall(PetscFunctionListAdd(&PhysicsList, "advect", PhysicsCreate_Advect));
  PetscCall(PetscFunctionListAdd(&PhysicsList, "sw", PhysicsCreate_SW));
  PetscCall(PetscFunctionListAdd(&PhysicsList, "euler", PhysicsCreate_Euler));

  PetscOptionsBegin(comm, NULL, "Unstructured Finite Volume Mesh Options", "");
  {
    cfl = 0.9 * 4; /* default SSPRKS2 with s=5 stages is stable for CFL number s-1 */
    PetscCall(PetscOptionsReal("-ufv_cfl", "CFL number per step", "", cfl, &cfl, NULL));
    user->vtkInterval = 1;
    PetscCall(PetscOptionsInt("-ufv_vtk_interval", "VTK output interval (0 to disable)", "", user->vtkInterval, &user->vtkInterval, NULL));
    user->vtkmon = PETSC_TRUE;
    PetscCall(PetscOptionsBool("-ufv_vtk_monitor", "Use VTKMonitor routine", "", user->vtkmon, &user->vtkmon, NULL));
    vtkCellGeom = PETSC_FALSE;
    PetscCall(PetscStrncpy(user->outputBasename, "ex11", sizeof(user->outputBasename)));
    PetscCall(PetscOptionsString("-ufv_vtk_basename", "VTK output basename", "", user->outputBasename, user->outputBasename, sizeof(user->outputBasename), NULL));
    PetscCall(PetscOptionsBool("-ufv_vtk_cellgeom", "Write cell geometry (for debugging)", "", vtkCellGeom, &vtkCellGeom, NULL));
    PetscCall(PetscOptionsBool("-ufv_use_amr", "use local adaptive mesh refinement", "", useAMR, &useAMR, NULL));
    PetscCall(PetscOptionsInt("-ufv_adapt_interval", "time steps between AMR", "", adaptInterval, &adaptInterval, NULL));
  }
  PetscOptionsEnd();

  if (useAMR) {
    VecTaggerBox refineBox, coarsenBox;

    refineBox.min = refineBox.max = PETSC_MAX_REAL;
    coarsenBox.min = coarsenBox.max = PETSC_MIN_REAL;

    PetscCall(VecTaggerCreate(comm, &refineTag));
    PetscCall(PetscObjectSetOptionsPrefix((PetscObject)refineTag, "refine_"));
    PetscCall(VecTaggerSetType(refineTag, VECTAGGERABSOLUTE));
    PetscCall(VecTaggerAbsoluteSetBox(refineTag, &refineBox));
    PetscCall(VecTaggerSetFromOptions(refineTag));
    PetscCall(VecTaggerSetUp(refineTag));
    PetscCall(PetscObjectViewFromOptions((PetscObject)refineTag, NULL, "-tag_view"));

    PetscCall(VecTaggerCreate(comm, &coarsenTag));
    PetscCall(PetscObjectSetOptionsPrefix((PetscObject)coarsenTag, "coarsen_"));
    PetscCall(VecTaggerSetType(coarsenTag, VECTAGGERABSOLUTE));
    PetscCall(VecTaggerAbsoluteSetBox(coarsenTag, &coarsenBox));
    PetscCall(VecTaggerSetFromOptions(coarsenTag));
    PetscCall(VecTaggerSetUp(coarsenTag));
    PetscCall(PetscObjectViewFromOptions((PetscObject)coarsenTag, NULL, "-tag_view"));
  }

  PetscOptionsBegin(comm, NULL, "Unstructured Finite Volume Physics Options", "");
  {
    PetscErrorCode (*physcreate)(Model, Physics, PetscOptionItems);
    PetscCall(PetscOptionsFList("-physics", "Physics module to solve", "", PhysicsList, physname, physname, sizeof physname, NULL));
    PetscCall(PetscFunctionListFind(PhysicsList, physname, &physcreate));
    PetscCall(PetscMemzero(phys, sizeof(struct _n_Physics)));
    PetscCall((*physcreate)(mod, phys, PetscOptionsObject));
    /* Count number of fields and dofs */
    for (phys->nfields = 0, phys->dof = 0; phys->field_desc[phys->nfields].name; phys->nfields++) phys->dof += phys->field_desc[phys->nfields].dof;
    PetscCheck(phys->dof > 0, comm, PETSC_ERR_ARG_WRONGSTATE, "Physics '%s' did not set dof", physname);
    PetscCall(ModelFunctionalSetFromOptions(mod, PetscOptionsObject));
  }
  PetscOptionsEnd();

  /* Create mesh */
  {
    PetscInt i;

    PetscCall(DMCreate(comm, &dm));
    PetscCall(DMSetType(dm, DMPLEX));
    PetscCall(DMSetFromOptions(dm));
    for (i = 0; i < DIM; i++) {
      mod->bounds[2 * i]     = 0.;
      mod->bounds[2 * i + 1] = 1.;
    }
    dim = DIM;
    { /* a null name means just do a hex box */
      PetscInt  cells[3] = {1, 1, 1}, n = 3;
      PetscBool flg2, skew              = PETSC_FALSE;
      PetscInt  nret2 = 2 * DIM;
      PetscOptionsBegin(comm, NULL, "Rectangular mesh options", "");
      PetscCall(PetscOptionsRealArray("-grid_bounds", "bounds of the mesh in each direction (i.e., x_min,x_max,y_min,y_max", "", mod->bounds, &nret2, &flg2));
      PetscCall(PetscOptionsBool("-grid_skew_60", "Skew grid for 60 degree shock mesh", "", skew, &skew, NULL));
      PetscCall(PetscOptionsIntArray("-dm_plex_box_faces", "Number of faces along each dimension", "", cells, &n, NULL));
      PetscOptionsEnd();
      /* TODO Rewrite this with Mark, and remove grid_bounds at that time */
      if (flg2) {
        PetscInt     dimEmbed, i;
        PetscInt     nCoords;
        PetscScalar *coords;
        Vec          coordinates;

        PetscCall(DMGetCoordinatesLocal(dm, &coordinates));
        PetscCall(DMGetCoordinateDim(dm, &dimEmbed));
        PetscCall(VecGetLocalSize(coordinates, &nCoords));
        PetscCheck(!(nCoords % dimEmbed), PETSC_COMM_SELF, PETSC_ERR_ARG_SIZ, "Coordinate vector the wrong size");
        PetscCall(VecGetArray(coordinates, &coords));
        for (i = 0; i < nCoords; i += dimEmbed) {
          PetscInt j;

          PetscScalar *coord = &coords[i];
          for (j = 0; j < dimEmbed; j++) {
            coord[j] = mod->bounds[2 * j] + coord[j] * (mod->bounds[2 * j + 1] - mod->bounds[2 * j]);
            if (dim == 2 && cells[1] == 1 && j == 0 && skew) {
              if (cells[0] == 2 && i == 8) {
                coord[j] = .57735026918963; /* hack to get 60 deg skewed mesh */
              } else if (cells[0] == 3) {
                if (i == 2 || i == 10) coord[j] = mod->bounds[1] / 4.;
                else if (i == 4) coord[j] = mod->bounds[1] / 2.;
                else if (i == 12) coord[j] = 1.57735026918963 * mod->bounds[1] / 2.;
              }
            }
          }
        }
        PetscCall(VecRestoreArray(coordinates, &coords));
        PetscCall(DMSetCoordinatesLocal(dm, coordinates));
      }
    }
  }
  PetscCall(DMViewFromOptions(dm, NULL, "-orig_dm_view"));
  PetscCall(DMGetDimension(dm, &dim));

  /* set up BCs, functions, tags */
  PetscCall(DMCreateLabel(dm, "Face Sets"));
  mod->errorIndicator = ErrorIndicator_Simple;

  {
    DM gdm;

    PetscCall(DMPlexConstructGhostCells(dm, NULL, NULL, &gdm));
    PetscCall(DMDestroy(&dm));
    dm = gdm;
    PetscCall(DMViewFromOptions(dm, NULL, "-dm_view"));
  }

  PetscCall(PetscFVCreate(comm, &fvm));
  PetscCall(PetscFVSetFromOptions(fvm));
  PetscCall(PetscFVSetNumComponents(fvm, phys->dof));
  PetscCall(PetscFVSetSpatialDimension(fvm, dim));
  PetscCall(PetscObjectSetName((PetscObject)fvm, ""));
  {
    PetscInt f, dof;
    for (f = 0, dof = 0; f < phys->nfields; f++) {
      PetscInt newDof = phys->field_desc[f].dof;

      if (newDof == 1) PetscCall(PetscFVSetComponentName(fvm, dof, phys->field_desc[f].name));
      else {
        PetscInt j;

        for (j = 0; j < newDof; j++) {
          char compName[256] = "Unknown";

          PetscCall(PetscSNPrintf(compName, sizeof(compName), "%s_%" PetscInt_FMT, phys->field_desc[f].name, j));
          PetscCall(PetscFVSetComponentName(fvm, dof + j, compName));
        }
      }
      dof += newDof;
    }
  }
  /* FV is now structured with one field having all physics as components */
  PetscCall(DMAddField(dm, NULL, (PetscObject)fvm));
  PetscCall(DMCreateDS(dm));
  PetscCall(DMGetDS(dm, &prob));
  PetscCall(PetscDSSetRiemannSolver(prob, 0, user->model->physics->riemann));
  PetscCall(PetscDSSetContext(prob, 0, user->model->physics));
  PetscCall((*mod->setupbc)(dm, prob, phys));
  PetscCall(PetscDSSetFromOptions(prob));
  {
    char      convType[256];
    PetscBool flg;

    PetscOptionsBegin(comm, "", "Mesh conversion options", "DMPLEX");
    PetscCall(PetscOptionsFList("-dm_type", "Convert DMPlex to another format", "ex12", DMList, DMPLEX, convType, 256, &flg));
    PetscOptionsEnd();
    if (flg) {
      DM dmConv;

      PetscCall(DMConvert(dm, convType, &dmConv));
      if (dmConv) {
        PetscCall(DMViewFromOptions(dmConv, NULL, "-dm_conv_view"));
        PetscCall(DMDestroy(&dm));
        dm = dmConv;
        PetscCall(DMSetFromOptions(dm));
      }
    }
  }
#ifdef PETSC_HAVE_LIBCEED
  {
    PetscBool useCeed;
    PetscCall(DMPlexGetUseCeed(dm, &useCeed));
    if (useCeed) PetscCall((*user->model->setupCEED)(dm, user->model->physics));
  }
#endif

  PetscCall(initializeTS(dm, user, &ts));

  PetscCall(DMCreateGlobalVector(dm, &X));
  PetscCall(PetscObjectSetName((PetscObject)X, "solution"));
  PetscCall(SetInitialCondition(dm, X, user));
  if (useAMR) {
    PetscInt adaptIter;

    /* use no limiting when reconstructing gradients for adaptivity */
    PetscCall(PetscFVGetLimiter(fvm, &limiter));
    PetscCall(PetscObjectReference((PetscObject)limiter));
    PetscCall(PetscLimiterCreate(PetscObjectComm((PetscObject)fvm), &noneLimiter));
    PetscCall(PetscLimiterSetType(noneLimiter, PETSCLIMITERNONE));

    /* Refinement context */
    tctx.fvm         = fvm;
    tctx.refineTag   = refineTag;
    tctx.coarsenTag  = coarsenTag;
    tctx.adaptedDM   = NULL;
    tctx.user        = user;
    tctx.noneLimiter = noneLimiter;
    tctx.limiter     = limiter;
    tctx.cfl         = cfl;

    /* Do some initial refinement steps */
    for (adaptIter = 0;; ++adaptIter) {
      PetscLogDouble bytes;
      PetscBool      resize;

      PetscCall(PetscMemoryGetCurrentUsage(&bytes));
      PetscCall(PetscInfo(ts, "refinement loop %" PetscInt_FMT ": memory used %g\n", adaptIter, bytes));
      PetscCall(DMViewFromOptions(dm, NULL, "-initial_dm_view"));
      PetscCall(VecViewFromOptions(X, NULL, "-initial_vec_view"));

      PetscCall(adaptToleranceFVMSetUp(ts, -1, 0.0, X, &resize, &tctx));
      if (!resize) break;
      PetscCall(DMDestroy(&dm));
      PetscCall(VecDestroy(&X));
      dm             = tctx.adaptedDM;
      tctx.adaptedDM = NULL;
      PetscCall(TSSetDM(ts, dm));
      PetscCall(DMCreateGlobalVector(dm, &X));
      PetscCall(PetscObjectSetName((PetscObject)X, "solution"));
      PetscCall(SetInitialCondition(dm, X, user));
    }
  }

  PetscCall(DMConvert(dm, DMPLEX, &plex));
  if (vtkCellGeom) {
    DM  dmCell;
    Vec cellgeom, partition;

    PetscCall(DMPlexGetGeometryFVM(plex, NULL, &cellgeom, NULL));
    PetscCall(OutputVTK(dm, "ex11-cellgeom.vtk", &viewer));
    PetscCall(VecView(cellgeom, viewer));
    PetscCall(PetscViewerDestroy(&viewer));
    PetscCall(CreatePartitionVec(dm, &dmCell, &partition));
    PetscCall(OutputVTK(dmCell, "ex11-partition.vtk", &viewer));
    PetscCall(VecView(partition, viewer));
    PetscCall(PetscViewerDestroy(&viewer));
    PetscCall(VecDestroy(&partition));
    PetscCall(DMDestroy(&dmCell));
  }
  /* collect max maxspeed from all processes -- todo */
  PetscCall(DMPlexGetGeometryFVM(plex, NULL, NULL, &minRadius));
  PetscCall(DMDestroy(&plex));
  PetscCallMPI(MPIU_Allreduce(&phys->maxspeed, &mod->maxspeed, 1, MPIU_REAL, MPIU_MAX, PetscObjectComm((PetscObject)ts)));
  PetscCheck(mod->maxspeed > 0, comm, PETSC_ERR_ARG_WRONGSTATE, "Physics '%s' did not set maxspeed", physname);
  dt = cfl * minRadius / mod->maxspeed;
  PetscCall(TSSetTimeStep(ts, dt));
  PetscCall(TSSetFromOptions(ts));

  /* When using adaptive mesh refinement
     specify callbacks to refine the solution
     and interpolate data from old to new mesh
     When mesh adaption is requested, the step will be rolled back
  */
  if (useAMR) PetscCall(TSSetResize(ts, PETSC_TRUE, adaptToleranceFVMSetUp, Transfer, &tctx));
  PetscCall(TSSetSolution(ts, X));
  PetscCall(VecDestroy(&X));
  PetscCall(TSSolve(ts, NULL));
  PetscCall(TSGetSolveTime(ts, &ftime));
  PetscCall(TSGetStepNumber(ts, &nsteps));
  PetscCall(TSGetConvergedReason(ts, &reason));
  PetscCall(PetscPrintf(PETSC_COMM_WORLD, "%s at time %g after %" PetscInt_FMT " steps\n", TSConvergedReasons[reason], (double)ftime, nsteps));
  PetscCall(TSDestroy(&ts));

  PetscCall(VecTaggerDestroy(&refineTag));
  PetscCall(VecTaggerDestroy(&coarsenTag));
  PetscCall(PetscFunctionListDestroy(&PhysicsList));
  PetscCall(PetscFunctionListDestroy(&PhysicsRiemannList_SW));
  PetscCall(PetscFunctionListDestroy(&PhysicsRiemannList_Euler));
  PetscCall(FunctionalLinkDestroy(&user->model->functionalRegistry));
  PetscCall(PetscFree(user->model->functionalMonitored));
  PetscCall(PetscFree(user->model->functionalCall));
  PetscCall(PetscFree(user->model->physics->data));
  PetscCall(PetscFree(user->model->physics));
  PetscCall(PetscFree(user->model));
  PetscCall(PetscFree(user));
  PetscCall(PetscLimiterDestroy(&limiter));
  PetscCall(PetscLimiterDestroy(&noneLimiter));
  PetscCall(PetscFVDestroy(&fvm));
  PetscCall(DMDestroy(&dm));
  PetscCall(PetscFinalize());
  return 0;
}

/* Subroutine to set up the initial conditions for the */
/* Shock Interface interaction or linear wave (Ravi Samtaney,Mark Adams). */
/* ----------------------------------------------------------------------- */
int projecteqstate(PetscReal wc[], const PetscReal ueq[], PetscReal lv[][3])
{
  int j, k;
  /*      Wc=matmul(lv,Ueq) 3 vars */
  for (k = 0; k < 3; ++k) {
    wc[k] = 0.;
    for (j = 0; j < 3; ++j) wc[k] += lv[k][j] * ueq[j];
  }
  return 0;
}
/* ----------------------------------------------------------------------- */
int projecttoprim(PetscReal v[], const PetscReal wc[], PetscReal rv[][3])
{
  int k, j;
  /*      V=matmul(rv,WC) 3 vars */
  for (k = 0; k < 3; ++k) {
    v[k] = 0.;
    for (j = 0; j < 3; ++j) v[k] += rv[k][j] * wc[j];
  }
  return 0;
}
/* ---------------------------------------------------------------------- */
int eigenvectors(PetscReal rv[][3], PetscReal lv[][3], const PetscReal ueq[], PetscReal gamma)
{
  int       j, k;
  PetscReal rho, csnd, p0;
  /* PetscScalar u; */

  for (k = 0; k < 3; ++k)
    for (j = 0; j < 3; ++j) {
      lv[k][j] = 0.;
      rv[k][j] = 0.;
    }
  rho = ueq[0];
  /* u = ueq[1]; */
  p0       = ueq[2];
  csnd     = PetscSqrtReal(gamma * p0 / rho);
  lv[0][1] = rho * .5;
  lv[0][2] = -.5 / csnd;
  lv[1][0] = csnd;
  lv[1][2] = -1. / csnd;
  lv[2][1] = rho * .5;
  lv[2][2] = .5 / csnd;
  rv[0][0] = -1. / csnd;
  rv[1][0] = 1. / rho;
  rv[2][0] = -csnd;
  rv[0][1] = 1. / csnd;
  rv[0][2] = 1. / csnd;
  rv[1][2] = 1. / rho;
  rv[2][2] = csnd;
  return 0;
}

int initLinearWave(EulerNode *ux, const PetscReal gamma, const PetscReal coord[], const PetscReal Lx)
{
  PetscReal p0, u0, wcp[3], wc[3];
  PetscReal lv[3][3];
  PetscReal vp[3];
  PetscReal rv[3][3];
  PetscReal eps, ueq[3], rho0, twopi;

  /* Function Body */
  twopi  = 2. * PETSC_PI;
  eps    = 1e-4;    /* perturbation */
  rho0   = 1e3;     /* density of water */
  p0     = 101325.; /* init pressure of 1 atm (?) */
  u0     = 0.;
  ueq[0] = rho0;
  ueq[1] = u0;
  ueq[2] = p0;
  /* Project initial state to characteristic variables */
  eigenvectors(rv, lv, ueq, gamma);
  projecteqstate(wc, ueq, lv);
  wcp[0] = wc[0];
  wcp[1] = wc[1];
  wcp[2] = wc[2] + eps * PetscCosReal(coord[0] * 2. * twopi / Lx);
  projecttoprim(vp, wcp, rv);
  ux->r     = vp[0];         /* density */
  ux->ru[0] = vp[0] * vp[1]; /* x momentum */
  ux->ru[1] = 0.;
  /* E = rho * e + rho * v^2/2 = p/(gam-1) + rho*v^2/2 */
  ux->E = vp[2] / (gamma - 1.) + 0.5 * vp[0] * vp[1] * vp[1];
  return 0;
}

/*TEST

  testset:
    args: -dm_plex_adj_cone -dm_plex_adj_closure 0

    test:
      suffix: adv_2d_tri_0
      requires: triangle
      TODO: how did this ever get in main when there is no support for this
      args: -ufv_vtk_interval 0 -simplex -dm_refine 3 -dm_plex_faces 1,1 -dm_plex_separate_marker -bc_inflow 1,2,4 -bc_outflow 3

    test:
      suffix: adv_2d_tri_1
      requires: triangle
      TODO: how did this ever get in main when there is no support for this
      args: -ufv_vtk_interval 0 -simplex -dm_refine 5 -dm_plex_faces 1,1 -dm_plex_separate_marker -grid_bounds -0.5,0.5,-0.5,0.5 -bc_inflow 1,2,4 -bc_outflow 3 -advect_sol_type bump -advect_bump_center 0.25,0 -advect_bump_radius 0.1

    test:
      suffix: tut_1
      requires: exodusii
      nsize: 1
      args: -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside.exo -

    test:
      suffix: tut_2
      requires: exodusii
      nsize: 1
      args: -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside.exo -ts_type rosw

    test:
      suffix: tut_3
      requires: exodusii
      nsize: 4
      args: -dm_distribute_overlap 1 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/annulus-20.exo -monitor Error -advect_sol_type bump -petscfv_type leastsquares -petsclimiter_type sin

    test:
      suffix: tut_4
      requires: exodusii !single
      nsize: 4
      args: -dm_distribute_overlap 1 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/annulus-20.exo -physics sw -monitor Height,Energy -petscfv_type leastsquares -petsclimiter_type minmod

  testset:
    args: -dm_plex_adj_cone -dm_plex_adj_closure 0 -dm_plex_simplex 0 -dm_plex_box_faces 1,1,1

    # 2D Advection 0-10
    test:
      suffix: 0
      requires: exodusii
      args: -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside.exo

    test:
      suffix: 1
      requires: exodusii
      args: -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside-quad-15.exo

    test:
      suffix: 2
      requires: exodusii
      nsize: 2
      args: -dm_distribute_overlap 1 -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside.exo

    test:
      suffix: 3
      requires: exodusii
      nsize: 2
      args: -dm_distribute_overlap 1 -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside-quad-15.exo

    test:
      suffix: 4
      requires: exodusii
      nsize: 4
      args: -dm_distribute_overlap 1 -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside-quad.exo -petscpartitioner_type simple

    test:
      suffix: 5
      requires: exodusii
      args: -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside.exo -ts_type rosw -ts_adapt_reject_safety 1

    test:
      suffix: 7
      requires: exodusii
      args: -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside-quad-15.exo -dm_refine 1

    test:
      suffix: 8
      requires: exodusii
      nsize: 2
      args: -dm_distribute_overlap 1 -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside-quad-15.exo -dm_refine 1

    test:
      suffix: 9
      requires: exodusii
      nsize: 8
      args: -dm_distribute_overlap 1 -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside-quad-15.exo -dm_refine 1

    test:
      suffix: 10
      requires: exodusii
      args: -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/sevenside-quad.exo

  # 2D Shallow water
  testset:
    args: -physics sw -ufv_vtk_interval 0 -dm_plex_adj_cone -dm_plex_adj_closure 0

    test:
      suffix: sw_0
      requires: exodusii
      args: -bc_wall 100,101 -ufv_cfl 5 -petscfv_type leastsquares -petsclimiter_type sin \
            -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/annulus-20.exo \
            -ts_max_time 1 -ts_ssp_type rks2 -ts_ssp_num_stages 10 \
            -monitor height,energy

    test:
      suffix: sw_ceed
      requires: exodusii libceed
      args: -sw_riemann rusanov_ceed -bc_wall 100,101 -ufv_cfl 5 -petsclimiter_type sin \
            -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/annulus-20.exo -dm_plex_use_ceed \
            -ts_max_time 1 -ts_ssp_type rks2 -ts_ssp_num_stages 10 \
            -monitor height,energy

    test:
      suffix: sw_ceed_small
      requires: exodusii libceed
      args: -sw_riemann rusanov_ceed -bc_wall 1,3 -ufv_cfl 5 -petsclimiter_type sin -dm_plex_use_ceed \
            -dm_plex_shape annulus -dm_plex_simplex 0 -dm_plex_box_lower 0,1 -dm_plex_box_upper 6.28,3 -dm_plex_box_faces 8,2 \
            -ts_max_time 1 -ts_ssp_type rks2 -ts_ssp_num_stages 10 \
            -monitor height,energy

    test:
      suffix: sw_1
      nsize: 2
      args: -bc_wall 1,3 -ufv_cfl 5 -petsclimiter_type sin \
            -dm_plex_shape annulus -dm_plex_simplex 0 -dm_plex_box_faces 24,12 -dm_plex_box_lower 0,1 -dm_plex_box_upper 1,3 -dm_distribute_overlap 1 \
            -ts_max_time 1 -ts_ssp_type rks2 -ts_ssp_num_stages 10 \
            -monitor height,energy

    test:
      suffix: sw_hll
      args: -sw_riemann hll -bc_wall 1,2,3,4 -ufv_cfl 3 -petscfv_type leastsquares -petsclimiter_type sin \
            -grid_bounds 0,5,0,5 -dm_plex_simplex 0 -dm_plex_box_faces 25,25 \
            -ts_max_steps 5 -ts_ssp_type rks2 -ts_ssp_num_stages 10 \
            -monitor height,energy

  # 2D Euler
  testset:
    args: -physics euler -eu_type linear_wave -eu_gamma 1.4 -dm_plex_adj_cone -dm_plex_adj_closure 0 \
          -ufv_vtk_interval 0 -ufv_vtk_basename ${wPETSC_DIR}/ex11 -monitor density,energy

    test:
      suffix: euler_0
      requires: exodusii !complex !single
      args: -eu_riemann godunov -bc_wall 100,101 -ufv_cfl 5 -petsclimiter_type sin \
            -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/annulus-20.exo \
            -ts_max_time 1 -ts_ssp_type rks2 -ts_ssp_num_stages 10

    test:
      suffix: euler_ceed
      requires: exodusii libceed
      args: -eu_riemann godunov_ceed -bc_wall 100,101 -ufv_cfl 5 -petsclimiter_type sin \
            -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/annulus-20.exo -dm_plex_use_ceed \
            -ts_max_time 1 -ts_ssp_type rks2 -ts_ssp_num_stages 10

  testset:
    args: -dm_plex_adj_cone -dm_plex_adj_closure 0 -dm_plex_simplex 0 -dm_plex_box_faces 1,1,1

    # 2D Advection: p4est
    test:
      suffix: p4est_advec_2d
      requires: p4est
      args: -ufv_vtk_interval 0 -dm_type p4est -dm_forest_minimum_refinement 1 -dm_forest_initial_refinement 2 -dm_p4est_refine_pattern hash -dm_forest_maximum_refinement 5

    # Advection in a box
    test:
      suffix: adv_2d_quad_0
      args: -ufv_vtk_interval 0 -dm_refine 3 -dm_plex_separate_marker -bc_inflow 1,2,4 -bc_outflow 3

    test:
      suffix: adv_2d_quad_1
      args: -ufv_vtk_interval 0 -dm_refine 3 -dm_plex_separate_marker -grid_bounds -0.5,0.5,-0.5,0.5 -bc_inflow 1,2,4 -bc_outflow 3 -advect_sol_type bump -advect_bump_center 0.25,0 -advect_bump_radius 0.1
      timeoutfactor: 3

    test:
      suffix: adv_2d_quad_p4est_0
      requires: p4est
      args: -ufv_vtk_interval 0 -dm_refine 5 -dm_type p4est -dm_plex_separate_marker -bc_inflow 1,2,4 -bc_outflow 3

    test:
      suffix: adv_2d_quad_p4est_1
      requires: p4est
      args: -ufv_vtk_interval 0 -dm_refine 5 -dm_type p4est -dm_plex_separate_marker -grid_bounds -0.5,0.5,-0.5,0.5 -bc_inflow 1,2,4 -bc_outflow 3 -advect_sol_type bump -advect_bump_center 0.25,0 -advect_bump_radius 0.1
      timeoutfactor: 3

    test: # broken for quad precision
      suffix: adv_2d_quad_p4est_adapt_0
      requires: p4est !__float128
      args: -ufv_vtk_interval 0 -dm_refine 3 -dm_type p4est -dm_plex_separate_marker -grid_bounds -0.5,0.5,-0.5,0.5 -bc_inflow 1,2,4 -bc_outflow 3 -advect_sol_type bump -advect_bump_center 0.25,0 -advect_bump_radius 0.1 -ufv_use_amr -refine_vec_tagger_box 0.005,inf -coarsen_vec_tagger_box 0,1.e-5 -petscfv_type leastsquares -ts_max_time 0.01
      timeoutfactor: 3

    test:
      suffix: adv_0
      requires: exodusii
      args: -ufv_vtk_interval 0 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/blockcylinder-50.exo -bc_inflow 100,101,200 -bc_outflow 201

    # Run with -dm_forest_maximum_refinement 6 -ts_max_time 0.5 instead to get the full movie
    test:
      suffix: shock_0
      requires: p4est !single !complex
      args: -dm_plex_box_faces 2,1 -grid_bounds -1,1.,0.,1 -grid_skew_60 \
      -dm_type p4est -dm_forest_partition_overlap 1 -dm_forest_maximum_refinement 2 -dm_forest_minimum_refinement 2 -dm_forest_initial_refinement 2 \
      -ufv_use_amr -refine_vec_tagger_box 0.5,inf -coarsen_vec_tagger_box 0,1.e-2 -refine_tag_view -coarsen_tag_view \
      -bc_wall 1,2,3,4 -physics euler -eu_type iv_shock -ufv_cfl 10 -eu_alpha 60. -eu_gamma 1.4 -eu_amach 2.02 -eu_rho2 3. \
      -petscfv_type leastsquares -petsclimiter_type minmod -petscfv_compute_gradients 0 \
      -ts_max_steps 3 -ts_ssp_type rks2 -ts_ssp_num_stages 10 \
      -ufv_vtk_basename ${wPETSC_DIR}/ex11 -ufv_vtk_interval 0 -monitor density,energy

    # Test GLVis visualization of PetscFV fields
    test:
      suffix: glvis_adv_2d_tri
      args: -ufv_vtk_interval 0 -ufv_vtk_monitor 0 \
            -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/square_periodic.msh -dm_plex_gmsh_periodic 0 \
            -ts_monitor_solution glvis: -ts_max_steps 0

    test:
      suffix: glvis_adv_2d_quad
      args: -ufv_vtk_interval 0 -ufv_vtk_monitor 0 -bc_inflow 1,2,4 -bc_outflow 3 \
            -dm_refine 5 -dm_plex_separate_marker \
            -ts_monitor_solution glvis: -ts_max_steps 0

    # Test CGNS file writing for PetscFV fields
    test:
      suffix: cgns_adv_2d_tri
      requires: cgns
      args: -ufv_vtk_interval 0 -ufv_vtk_monitor 0 \
            -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/square_periodic.msh -dm_plex_gmsh_periodic 0 \
            -ts_monitor_solution cgns:sol.cgns -ts_max_steps 0

    test:
      suffix: cgns_adv_2d_quad
      requires: cgns
      args: -ufv_vtk_interval 0 -ufv_vtk_monitor 0 -bc_inflow 1,2,4 -bc_outflow 3 \
            -dm_refine 5 -dm_plex_separate_marker \
            -ts_monitor_solution cgns:sol.cgns -ts_max_steps 0

    # Test CGNS file writing, cgns_batch_size, ts_run_steps, ts_monitor_skip_initial
    test:
      suffix: cgns_adv_2d_tri_monitor
      requires: cgns
      args: -ufv_vtk_interval 0 -ufv_vtk_monitor 0 \
            -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/square_periodic.msh -dm_plex_gmsh_periodic 0 \
            -ts_monitor_solution cgns:sol-%d.cgns -ts_run_steps 4 -ts_monitor_solution_interval 2 \
            -viewer_cgns_batch_size 1 -ts_monitor_solution_skip_initial

    # Test VTK file writing for PetscFV fields with -ts_monitor_solution_vtk
    test:
      suffix: vtk_adv_2d_tri
      args: -ufv_vtk_interval 0 -ufv_vtk_monitor 0 \
            -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/square_periodic.msh -dm_plex_gmsh_periodic 0 \
            -ts_monitor_solution_vtk 'bar-%03d.vtu'  -ts_monitor_solution_vtk_interval  2 -ts_max_steps 5

TEST*/
````

## TS ex2.c

- Selected by: Tutorials by mathematical problem
- Rendered listing: <https://petsc.org/release/src/ts/tutorials/ex2.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/ts/tutorials/ex2.c>

````c
static char help[] = "Solves a time-dependent nonlinear PDE. Uses implicit\n\
timestepping.  Runtime options include:\n\
  -M <xg>, where <xg> = number of grid points\n\
  -debug : Activate debugging printouts\n\
  -nox   : Deactivate x-window graphics\n\n";

/* ------------------------------------------------------------------------

   This program solves the PDE

               u * u_xx
         u_t = ---------
               2*(t+1)^2

    on the domain 0 <= x <= 1, with boundary conditions
         u(t,0) = t + 1,  u(t,1) = 2*t + 2,
    and initial condition
         u(0,x) = 1 + x*x.

    The exact solution is:
         u(t,x) = (1 + x*x) * (1 + t)

    Note that since the solution is linear in time and quadratic in x,
    the finite difference scheme actually computes the "exact" solution.

    We use by default the backward Euler method.

  ------------------------------------------------------------------------- */

/*
   Include "petscts.h" to use the PETSc timestepping routines. Note that
   this file automatically includes "petscsys.h" and other lower-level
   PETSc include files.

   Include the "petscdmda.h" to allow us to use the distributed array data
   structures to manage the parallel grid.
*/
#include <petscts.h>
#include <petscdm.h>
#include <petscdmda.h>
#include <petscdraw.h>

/*
   User-defined application context - contains data needed by the
   application-provided callback routines.
*/
typedef struct {
  MPI_Comm  comm;      /* communicator */
  DM        da;        /* distributed array data structure */
  Vec       localwork; /* local ghosted work vector */
  Vec       u_local;   /* local ghosted approximate solution vector */
  Vec       solution;  /* global exact solution vector */
  PetscInt  m;         /* total number of grid points */
  PetscReal h;         /* mesh width: h = 1/(m-1) */
  PetscBool debug;     /* flag (1 indicates activation of debugging printouts) */
} AppCtx;

/*
   User-defined routines, provided below.
*/
extern PetscErrorCode InitialConditions(Vec, AppCtx *);
extern PetscErrorCode RHSFunction(TS, PetscReal, Vec, Vec, void *);
extern PetscErrorCode RHSJacobian(TS, PetscReal, Vec, Mat, Mat, void *);
extern PetscErrorCode Monitor(TS, PetscInt, PetscReal, Vec, void *);
extern PetscErrorCode ExactSolution(PetscReal, Vec, AppCtx *);

int main(int argc, char **argv)
{
  AppCtx    appctx;               /* user-defined application context */
  TS        ts;                   /* timestepping context */
  Mat       A;                    /* Jacobian matrix data structure */
  Vec       u;                    /* approximate solution vector */
  PetscInt  time_steps_max = 100; /* default max timesteps */
  PetscReal dt;
  PetscReal time_total_max = 100.0; /* default max total time */
  PetscBool mymonitor      = PETSC_FALSE;
  PetscReal bounds[]       = {1.0, 3.3};

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Initialize program and set problem parameters
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(PetscViewerDrawSetBounds(PETSC_VIEWER_DRAW_(PETSC_COMM_WORLD), 1, bounds));

  appctx.comm = PETSC_COMM_WORLD;
  appctx.m    = 60;

  PetscCall(PetscOptionsGetInt(NULL, NULL, "-M", &appctx.m, NULL));
  PetscCall(PetscOptionsHasName(NULL, NULL, "-debug", &appctx.debug));
  PetscCall(PetscOptionsHasName(NULL, NULL, "-mymonitor", &mymonitor));

  appctx.h = 1.0 / (appctx.m - 1.0);

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create vector data structures
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  /*
     Create distributed array (DMDA) to manage parallel grid and vectors
     and to set up the ghost point communication pattern.  There are M
     total grid values spread equally among all the processors.
  */
  PetscCall(DMDACreate1d(PETSC_COMM_WORLD, DM_BOUNDARY_NONE, appctx.m, 1, 1, NULL, &appctx.da));
  PetscCall(DMSetFromOptions(appctx.da));
  PetscCall(DMSetUp(appctx.da));

  /*
     Extract global and local vectors from DMDA; we use these to store the
     approximate solution.  Then duplicate these for remaining vectors that
     have the same types.
  */
  PetscCall(DMCreateGlobalVector(appctx.da, &u));
  PetscCall(DMCreateLocalVector(appctx.da, &appctx.u_local));

  /*
     Create local work vector for use in evaluating right-hand-side function;
     create global work vector for storing exact solution.
  */
  PetscCall(VecDuplicate(appctx.u_local, &appctx.localwork));
  PetscCall(VecDuplicate(u, &appctx.solution));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create timestepping solver context; set callback routine for
     right-hand-side function evaluation.
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  PetscCall(TSCreate(PETSC_COMM_WORLD, &ts));
  PetscCall(TSSetProblemType(ts, TS_NONLINEAR));
  PetscCall(TSSetRHSFunction(ts, NULL, RHSFunction, &appctx));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Set optional user-defined monitoring routine
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  if (mymonitor) PetscCall(TSMonitorSet(ts, Monitor, &appctx, NULL));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     For nonlinear problems, the user can provide a Jacobian evaluation
     routine (or use a finite differencing approximation).

     Create matrix data structure; set Jacobian evaluation routine.
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  PetscCall(MatCreate(PETSC_COMM_WORLD, &A));
  PetscCall(MatSetSizes(A, PETSC_DECIDE, PETSC_DECIDE, appctx.m, appctx.m));
  PetscCall(MatSetFromOptions(A));
  PetscCall(MatSetUp(A));
  PetscCall(TSSetRHSJacobian(ts, A, A, RHSJacobian, &appctx));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Set solution vector and initial timestep
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  dt = appctx.h / 2.0;
  PetscCall(TSSetTimeStep(ts, dt));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Customize timestepping solver:
       - Set the solution method to be the Backward Euler method.
       - Set timestepping duration info
     Then set runtime options, which can override these defaults.
     For example,
          -ts_max_steps <maxsteps> -ts_max_time <maxtime>
     to override the defaults set by TSSetMaxSteps()/TSSetMaxTime().
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  PetscCall(TSSetType(ts, TSBEULER));
  PetscCall(TSSetMaxSteps(ts, time_steps_max));
  PetscCall(TSSetMaxTime(ts, time_total_max));
  PetscCall(TSSetExactFinalTime(ts, TS_EXACTFINALTIME_STEPOVER));
  PetscCall(TSSetFromOptions(ts));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Solve the problem
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  /*
     Evaluate initial conditions
  */
  PetscCall(InitialConditions(u, &appctx));

  /*
     Run the timestepping solver
  */
  PetscCall(TSSolve(ts, u));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Free work space.  All PETSc objects should be destroyed when they
     are no longer needed.
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  PetscCall(TSDestroy(&ts));
  PetscCall(VecDestroy(&u));
  PetscCall(MatDestroy(&A));
  PetscCall(DMDestroy(&appctx.da));
  PetscCall(VecDestroy(&appctx.localwork));
  PetscCall(VecDestroy(&appctx.solution));
  PetscCall(VecDestroy(&appctx.u_local));

  /*
     Always call PetscFinalize() before exiting a program.  This routine
       - finalizes the PETSc libraries as well as MPI
       - provides summary and diagnostic information if certain runtime
         options are chosen (e.g., -log_view).
  */
  PetscCall(PetscFinalize());
  return 0;
}
/* --------------------------------------------------------------------- */
/*
   InitialConditions - Computes the solution at the initial time.

   Input Parameters:
   u - uninitialized solution vector (global)
   appctx - user-defined application context

   Output Parameter:
   u - vector with solution at initial time (global)
*/
PetscErrorCode InitialConditions(Vec u, AppCtx *appctx)
{
  PetscScalar *u_localptr, h = appctx->h, x;
  PetscInt     i, mybase, myend;

  PetscFunctionBeginUser;
  /*
     Determine starting point of each processor's range of
     grid values.
  */
  PetscCall(VecGetOwnershipRange(u, &mybase, &myend));

  /*
    Get a pointer to vector data.
    - For default PETSc vectors, VecGetArray() returns a pointer to
      the data array.  Otherwise, the routine is implementation dependent.
    - You MUST call VecRestoreArray() when you no longer need access to
      the array.
    - Note that the Fortran interface to VecGetArray() differs from the
      C version.  See the users manual for details.
  */
  PetscCall(VecGetArray(u, &u_localptr));

  /*
     We initialize the solution array by simply writing the solution
     directly into the array locations.  Alternatively, we could use
     VecSetValues() or VecSetValuesLocal().
  */
  for (i = mybase; i < myend; i++) {
    x                      = h * (PetscReal)i; /* current location in global grid */
    u_localptr[i - mybase] = 1.0 + x * x;
  }

  /*
     Restore vector
  */
  PetscCall(VecRestoreArray(u, &u_localptr));

  /*
     Print debugging information if desired
  */
  if (appctx->debug) {
    PetscCall(PetscPrintf(appctx->comm, "initial guess vector\n"));
    PetscCall(VecView(u, PETSC_VIEWER_STDOUT_WORLD));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}
/* --------------------------------------------------------------------- */
/*
   ExactSolution - Computes the exact solution at a given time.

   Input Parameters:
   t - current time
   solution - vector in which exact solution will be computed
   appctx - user-defined application context

   Output Parameter:
   solution - vector with the newly computed exact solution
*/
PetscErrorCode ExactSolution(PetscReal t, Vec solution, AppCtx *appctx)
{
  PetscScalar *s_localptr, h = appctx->h, x;
  PetscInt     i, mybase, myend;

  PetscFunctionBeginUser;
  /*
     Determine starting and ending points of each processor's
     range of grid values
  */
  PetscCall(VecGetOwnershipRange(solution, &mybase, &myend));

  /*
     Get a pointer to vector data.
  */
  PetscCall(VecGetArray(solution, &s_localptr));

  /*
     Simply write the solution directly into the array locations.
     Alternatively, we could use VecSetValues() or VecSetValuesLocal().
  */
  for (i = mybase; i < myend; i++) {
    x                      = h * (PetscReal)i;
    s_localptr[i - mybase] = (t + 1.0) * (1.0 + x * x);
  }

  /*
     Restore vector
  */
  PetscCall(VecRestoreArray(solution, &s_localptr));
  PetscFunctionReturn(PETSC_SUCCESS);
}
/* --------------------------------------------------------------------- */
/*
   Monitor - User-provided routine to monitor the solution computed at
   each timestep.  This example plots the solution and computes the
   error in two different norms.

   Input Parameters:
   ts     - the timestep context
   step   - the count of the current step (with 0 meaning the
            initial condition)
   time   - the current time
   u      - the solution at this timestep
   ctx    - the user-provided context for this monitoring routine.
            In this case we use the application context which contains
            information about the problem size, workspace and the exact
            solution.
*/
PetscErrorCode Monitor(TS ts, PetscInt step, PetscReal time, Vec u, PetscCtx ctx)
{
  AppCtx   *appctx = (AppCtx *)ctx; /* user-defined application context */
  PetscReal en2, en2s, enmax;
  PetscDraw draw;

  PetscFunctionBeginUser;
  /*
     We use the default X Windows viewer
             PETSC_VIEWER_DRAW_(appctx->comm)
     that is associated with the current communicator. This saves
     the effort of calling PetscViewerDrawOpen() to create the window.
     Note that if we wished to plot several items in separate windows we
     would create each viewer with PetscViewerDrawOpen() and store them in
     the application context, appctx.

     PetscReal buffering makes graphics look better.
  */
  PetscCall(PetscViewerDrawGetDraw(PETSC_VIEWER_DRAW_(appctx->comm), 0, &draw));
  PetscCall(PetscDrawSetDoubleBuffer(draw));
  PetscCall(VecView(u, PETSC_VIEWER_DRAW_(appctx->comm)));

  /*
     Compute the exact solution at this timestep
  */
  PetscCall(ExactSolution(time, appctx->solution, appctx));

  /*
     Print debugging information if desired
  */
  if (appctx->debug) {
    PetscCall(PetscPrintf(appctx->comm, "Computed solution vector\n"));
    PetscCall(VecView(u, PETSC_VIEWER_STDOUT_WORLD));
    PetscCall(PetscPrintf(appctx->comm, "Exact solution vector\n"));
    PetscCall(VecView(appctx->solution, PETSC_VIEWER_STDOUT_WORLD));
  }

  /*
     Compute the 2-norm and max-norm of the error
  */
  PetscCall(VecAXPY(appctx->solution, -1.0, u));
  PetscCall(VecNorm(appctx->solution, NORM_2, &en2));
  en2s = PetscSqrtReal(appctx->h) * en2; /* scale the 2-norm by the grid spacing */
  PetscCall(VecNorm(appctx->solution, NORM_MAX, &enmax));

  /*
     PetscPrintf() causes only the first processor in this
     communicator to print the timestep information.
  */
  PetscCall(PetscPrintf(appctx->comm, "Timestep %" PetscInt_FMT ": time = %g 2-norm error = %g  max norm error = %g\n", step, (double)time, (double)en2s, (double)enmax));

  /*
     Print debugging information if desired
  */
  if (appctx->debug) {
    PetscCall(PetscPrintf(appctx->comm, "Error vector\n"));
    PetscCall(VecView(appctx->solution, PETSC_VIEWER_STDOUT_WORLD));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}
/* --------------------------------------------------------------------- */
/*
   RHSFunction - User-provided routine that evalues the right-hand-side
   function of the ODE.  This routine is set in the main program by
   calling TSSetRHSFunction().  We compute:
          global_out = F(global_in)

   Input Parameters:
   ts         - timesteping context
   t          - current time
   global_in  - vector containing the current iterate
   ctx        - (optional) user-provided context for function evaluation.
                In this case we use the appctx defined above.

   Output Parameter:
   global_out - vector containing the newly evaluated function
*/
PetscErrorCode RHSFunction(TS ts, PetscReal t, Vec global_in, Vec global_out, PetscCtx ctx)
{
  AppCtx            *appctx    = (AppCtx *)ctx;     /* user-defined application context */
  DM                 da        = appctx->da;        /* distributed array */
  Vec                local_in  = appctx->u_local;   /* local ghosted input vector */
  Vec                localwork = appctx->localwork; /* local ghosted work vector */
  PetscInt           i, localsize;
  PetscMPIInt        rank, size;
  PetscScalar       *copyptr, sc;
  const PetscScalar *localptr;

  PetscFunctionBeginUser;
  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Get ready for local function computations
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  /*
     Scatter ghost points to local vector, using the 2-step process
        DMGlobalToLocalBegin(), DMGlobalToLocalEnd().
     By placing code between these two statements, computations can be
     done while messages are in transition.
  */
  PetscCall(DMGlobalToLocalBegin(da, global_in, INSERT_VALUES, local_in));
  PetscCall(DMGlobalToLocalEnd(da, global_in, INSERT_VALUES, local_in));

  /*
      Access directly the values in our local INPUT work array
  */
  PetscCall(VecGetArrayRead(local_in, &localptr));

  /*
      Access directly the values in our local OUTPUT work array
  */
  PetscCall(VecGetArray(localwork, &copyptr));

  sc = 1.0 / (appctx->h * appctx->h * 2.0 * (1.0 + t) * (1.0 + t));

  /*
      Evaluate our function on the nodes owned by this processor
  */
  PetscCall(VecGetLocalSize(local_in, &localsize));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Compute entries for the locally owned part
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  /*
     Handle boundary conditions: This is done by using the boundary condition
        u(t,boundary) = g(t,boundary)
     for some function g. Now take the derivative with respect to t to obtain
        u_{t}(t,boundary) = g_{t}(t,boundary)

     In our case, u(t,0) = t + 1, so that u_{t}(t,0) = 1
             and  u(t,1) = 2t+ 2, so that u_{t}(t,1) = 2
  */
  PetscCallMPI(MPI_Comm_rank(appctx->comm, &rank));
  PetscCallMPI(MPI_Comm_size(appctx->comm, &size));
  if (rank == 0) copyptr[0] = 1.0;
  if (rank == size - 1) copyptr[localsize - 1] = 2.0;

  /*
     Handle the interior nodes where the PDE is replace by finite
     difference operators.
  */
  for (i = 1; i < localsize - 1; i++) copyptr[i] = localptr[i] * sc * (localptr[i + 1] + localptr[i - 1] - 2.0 * localptr[i]);

  /*
     Restore vectors
  */
  PetscCall(VecRestoreArrayRead(local_in, &localptr));
  PetscCall(VecRestoreArray(localwork, &copyptr));

  /*
     Insert values from the local OUTPUT vector into the global
     output vector
  */
  PetscCall(DMLocalToGlobalBegin(da, localwork, INSERT_VALUES, global_out));
  PetscCall(DMLocalToGlobalEnd(da, localwork, INSERT_VALUES, global_out));

  /* Print debugging information if desired */
  if (appctx->debug) {
    PetscCall(PetscPrintf(appctx->comm, "RHS function vector\n"));
    PetscCall(VecView(global_out, PETSC_VIEWER_STDOUT_WORLD));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}
/* --------------------------------------------------------------------- */
/*
   RHSJacobian - User-provided routine to compute the Jacobian of
   the nonlinear right-hand-side function of the ODE.

   Input Parameters:
   ts - the TS context
   t - current time
   global_in - global input vector
   dummy - optional user-defined context, as set by TSetRHSJacobian()

   Output Parameters:
   AA - Jacobian matrix
   BB - optionally different matrix used to construct the preconditioner

  Notes:
  RHSJacobian computes entries for the locally owned part of the Jacobian.
   - Currently, all PETSc parallel matrix formats are partitioned by
     contiguous chunks of rows across the processors.
   - Each processor needs to insert only elements that it owns
     locally (but any non-local elements will be sent to the
     appropriate processor during matrix assembly).
   - Always specify global row and columns of matrix entries when
     using MatSetValues().
   - Here, we set all entries for a particular row at once.
   - Note that MatSetValues() uses 0-based row and column numbers
     in Fortran as well as in C.
*/
PetscErrorCode RHSJacobian(TS ts, PetscReal t, Vec global_in, Mat AA, Mat BB, PetscCtx ctx)
{
  AppCtx            *appctx   = (AppCtx *)ctx;   /* user-defined application context */
  Vec                local_in = appctx->u_local; /* local ghosted input vector */
  DM                 da       = appctx->da;      /* distributed array */
  PetscScalar        v[3], sc;
  const PetscScalar *localptr;
  PetscInt           i, mstart, mend, mstarts, mends, idx[3], is;

  PetscFunctionBeginUser;
  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Get ready for local Jacobian computations
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  /*
     Scatter ghost points to local vector, using the 2-step process
        DMGlobalToLocalBegin(), DMGlobalToLocalEnd().
     By placing code between these two statements, computations can be
     done while messages are in transition.
  */
  PetscCall(DMGlobalToLocalBegin(da, global_in, INSERT_VALUES, local_in));
  PetscCall(DMGlobalToLocalEnd(da, global_in, INSERT_VALUES, local_in));

  /*
     Get pointer to vector data
  */
  PetscCall(VecGetArrayRead(local_in, &localptr));

  /*
     Get starting and ending locally owned rows of the matrix
  */
  PetscCall(MatGetOwnershipRange(BB, &mstarts, &mends));
  mstart = mstarts;
  mend   = mends;

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Compute entries for the locally owned part of the Jacobian.
      - Currently, all PETSc parallel matrix formats are partitioned by
        contiguous chunks of rows across the processors.
      - Each processor needs to insert only elements that it owns
        locally (but any non-local elements will be sent to the
        appropriate processor during matrix assembly).
      - Here, we set all entries for a particular row at once.
      - We can set matrix entries either using either
        MatSetValuesLocal() or MatSetValues().
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  /*
     Set matrix rows corresponding to boundary data
  */
  if (mstart == 0) {
    v[0] = 0.0;
    PetscCall(MatSetValues(BB, 1, &mstart, 1, &mstart, v, INSERT_VALUES));
    mstart++;
  }
  if (mend == appctx->m) {
    mend--;
    v[0] = 0.0;
    PetscCall(MatSetValues(BB, 1, &mend, 1, &mend, v, INSERT_VALUES));
  }

  /*
     Set matrix rows corresponding to interior data.  We construct the
     matrix one row at a time.
  */
  sc = 1.0 / (appctx->h * appctx->h * 2.0 * (1.0 + t) * (1.0 + t));
  for (i = mstart; i < mend; i++) {
    idx[0] = i - 1;
    idx[1] = i;
    idx[2] = i + 1;
    is     = i - mstart + 1;
    v[0]   = sc * localptr[is];
    v[1]   = sc * (localptr[is + 1] + localptr[is - 1] - 4.0 * localptr[is]);
    v[2]   = sc * localptr[is];
    PetscCall(MatSetValues(BB, 1, &i, 3, idx, v, INSERT_VALUES));
  }

  /*
     Restore vector
  */
  PetscCall(VecRestoreArrayRead(local_in, &localptr));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Complete the matrix assembly process and set some options
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  /*
     Assemble matrix, using the 2-step process:
       MatAssemblyBegin(), MatAssemblyEnd()
     Computations can be done while messages are in transition
     by placing code between these two statements.
  */
  PetscCall(MatAssemblyBegin(BB, MAT_FINAL_ASSEMBLY));
  PetscCall(MatAssemblyEnd(BB, MAT_FINAL_ASSEMBLY));
  if (BB != AA) {
    PetscCall(MatAssemblyBegin(AA, MAT_FINAL_ASSEMBLY));
    PetscCall(MatAssemblyEnd(AA, MAT_FINAL_ASSEMBLY));
  }

  /*
     Set and option to indicate that we will never add a new nonzero location
     to the matrix. If we do, it will generate an error.
  */
  PetscCall(MatSetOption(BB, MAT_NEW_NONZERO_LOCATION_ERR, PETSC_TRUE));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/*TEST

    test:
      args: -nox -ts_time_step 10 -mymonitor
      nsize: 2
      requires: !single

    test:
      suffix: tut_1
      nsize: 1
      args: -ts_max_steps 10 -ts_monitor

    test:
      suffix: tut_2
      nsize: 4
      args: -ts_max_steps 10 -ts_monitor -snes_monitor -ksp_monitor
      # GEMV sensitive to single
      args: -vec_mdot_use_gemv 0 -vec_maxpy_use_gemv 0

    test:
      suffix: tut_3
      nsize: 4
      args: -ts_max_steps 10 -ts_monitor -M 128

TEST*/
````

## KSP ex45.c

- Selected by: Tutorials by physics
- Rendered listing: <https://petsc.org/release/src/ksp/ksp/tutorials/ex45.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/ksp/ksp/tutorials/ex45.c>

````c
/*
Laplacian in 3D. Modeled by the partial differential equation

   - Laplacian u = 1,0 < x,y,z < 1,

with boundary conditions

   u = 1 for x = 0, x = 1, y = 0, y = 1, z = 0, z = 1.

   This uses multigrid to solve the linear system

   See src/snes/tutorials/ex50.c

   Can also be run with -pc_type exotic -ksp_type fgmres

*/

static char help[] = "Solves 3D Laplacian using multigrid.\n\n";

#include <petscksp.h>
#include <petscdm.h>
#include <petscdmda.h>

PetscLogEvent setvalues, usertime;

extern PetscErrorCode ComputeMatrix(KSP, Mat, Mat, void *);
extern PetscErrorCode ComputeRHS(KSP, Vec, void *);
extern PetscErrorCode ComputeInitialGuess(KSP, Vec, void *);

int main(int argc, char **argv)
{
  KSP       ksp;
  PetscReal norm;
  DM        da;
  Vec       x, b, r;
  Mat       A;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(PetscLogEventRegister("Set values", MAT_CLASSID, &setvalues));
  PetscCall(PetscLogEventRegister("User time", MAT_CLASSID, &usertime));
  PetscCallMPI(MPI_Barrier(PETSC_COMM_WORLD));
  PetscCall(PetscLogEventBegin(usertime, NULL, NULL, NULL, NULL));

  PetscCall(KSPCreate(PETSC_COMM_WORLD, &ksp));
  PetscCall(DMDACreate3d(PETSC_COMM_WORLD, DM_BOUNDARY_NONE, DM_BOUNDARY_NONE, DM_BOUNDARY_NONE, DMDA_STENCIL_STAR, 7, 7, 7, PETSC_DECIDE, PETSC_DECIDE, PETSC_DECIDE, 1, 1, 0, 0, 0, &da));
  PetscCall(DMSetFromOptions(da));
  PetscCall(DMSetUp(da));
  PetscCall(KSPSetDM(ksp, da));
  PetscCall(KSPSetComputeInitialGuess(ksp, ComputeInitialGuess, NULL));
  PetscCall(KSPSetComputeRHS(ksp, ComputeRHS, NULL));
  PetscCall(KSPSetComputeOperators(ksp, ComputeMatrix, NULL));
  PetscCall(DMDestroy(&da));

  PetscCall(KSPSetFromOptions(ksp));
  PetscCall(KSPSolve(ksp, NULL, NULL));
  PetscCall(KSPGetSolution(ksp, &x));
  PetscCall(KSPGetRhs(ksp, &b));
  PetscCall(VecDuplicate(b, &r));
  PetscCall(KSPGetOperators(ksp, &A, NULL));

  PetscCall(MatMult(A, x, r));
  PetscCall(VecAXPY(r, -1.0, b));
  PetscCall(VecNorm(r, NORM_2, &norm));
  PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Residual norm %g\n", (double)norm));

  PetscCall(VecDestroy(&r));
  PetscCall(KSPDestroy(&ksp));
  PetscCall(PetscLogEventEnd(usertime, NULL, NULL, NULL, NULL));
  PetscCall(PetscFinalize());
  return 0;
}

PetscErrorCode ComputeRHS(KSP ksp, Vec b, PetscCtx ctx)
{
  PetscInt       i, j, k, mx, my, mz, xm, ym, zm, xs, ys, zs;
  DM             dm;
  PetscScalar    Hx, Hy, Hz, HxHydHz, HyHzdHx, HxHzdHy;
  PetscScalar ***barray;

  PetscFunctionBeginUser;
  PetscCall(PetscLogEventBegin(setvalues, NULL, NULL, NULL, NULL));
  PetscCall(KSPGetDM(ksp, &dm));
  PetscCall(DMDAGetInfo(dm, 0, &mx, &my, &mz, 0, 0, 0, 0, 0, 0, 0, 0, 0));
  Hx      = 1.0 / (PetscReal)(mx - 1);
  Hy      = 1.0 / (PetscReal)(my - 1);
  Hz      = 1.0 / (PetscReal)(mz - 1);
  HxHydHz = Hx * Hy / Hz;
  HxHzdHy = Hx * Hz / Hy;
  HyHzdHx = Hy * Hz / Hx;
  PetscCall(DMDAGetCorners(dm, &xs, &ys, &zs, &xm, &ym, &zm));
  PetscCall(DMDAVecGetArray(dm, b, &barray));

  for (k = zs; k < zs + zm; k++) {
    for (j = ys; j < ys + ym; j++) {
      for (i = xs; i < xs + xm; i++) {
        if (i == 0 || j == 0 || k == 0 || i == mx - 1 || j == my - 1 || k == mz - 1) {
          barray[k][j][i] = 2.0 * (HxHydHz + HxHzdHy + HyHzdHx);
        } else {
          barray[k][j][i] = Hx * Hy * Hz;
        }
      }
    }
  }
  PetscCall(DMDAVecRestoreArray(dm, b, &barray));
  PetscCall(PetscLogEventEnd(setvalues, NULL, NULL, NULL, NULL));
  PetscFunctionReturn(PETSC_SUCCESS);
}

PetscErrorCode ComputeInitialGuess(KSP ksp, Vec b, PetscCtx ctx)
{
  PetscFunctionBeginUser;
  PetscCall(VecSet(b, 0));
  PetscFunctionReturn(PETSC_SUCCESS);
}

PetscErrorCode ComputeMatrix(KSP ksp, Mat jac, Mat B, PetscCtx ctx)
{
  DM          da;
  PetscInt    i, j, k, mx, my, mz, xm, ym, zm, xs, ys, zs;
  PetscScalar v[7], Hx, Hy, Hz, HxHydHz, HyHzdHx, HxHzdHy;
  MatStencil  row, col[7];

  PetscFunctionBeginUser;
  PetscCall(PetscLogEventBegin(setvalues, NULL, NULL, NULL, NULL));
  PetscCall(KSPGetDM(ksp, &da));
  PetscCall(DMDAGetInfo(da, 0, &mx, &my, &mz, 0, 0, 0, 0, 0, 0, 0, 0, 0));
  Hx      = 1.0 / (PetscReal)(mx - 1);
  Hy      = 1.0 / (PetscReal)(my - 1);
  Hz      = 1.0 / (PetscReal)(mz - 1);
  HxHydHz = Hx * Hy / Hz;
  HxHzdHy = Hx * Hz / Hy;
  HyHzdHx = Hy * Hz / Hx;
  PetscCall(DMDAGetCorners(da, &xs, &ys, &zs, &xm, &ym, &zm));

  for (k = zs; k < zs + zm; k++) {
    for (j = ys; j < ys + ym; j++) {
      for (i = xs; i < xs + xm; i++) {
        row.i = i;
        row.j = j;
        row.k = k;
        if (i == 0 || j == 0 || k == 0 || i == mx - 1 || j == my - 1 || k == mz - 1) {
          v[0] = 2.0 * (HxHydHz + HxHzdHy + HyHzdHx);
          PetscCall(MatSetValuesStencil(B, 1, &row, 1, &row, v, INSERT_VALUES));
        } else {
          v[0]     = -HxHydHz;
          col[0].i = i;
          col[0].j = j;
          col[0].k = k - 1;
          v[1]     = -HxHzdHy;
          col[1].i = i;
          col[1].j = j - 1;
          col[1].k = k;
          v[2]     = -HyHzdHx;
          col[2].i = i - 1;
          col[2].j = j;
          col[2].k = k;
          v[3]     = 2.0 * (HxHydHz + HxHzdHy + HyHzdHx);
          col[3].i = row.i;
          col[3].j = row.j;
          col[3].k = row.k;
          v[4]     = -HyHzdHx;
          col[4].i = i + 1;
          col[4].j = j;
          col[4].k = k;
          v[5]     = -HxHzdHy;
          col[5].i = i;
          col[5].j = j + 1;
          col[5].k = k;
          v[6]     = -HxHydHz;
          col[6].i = i;
          col[6].j = j;
          col[6].k = k + 1;
          PetscCall(MatSetValuesStencil(B, 1, &row, 7, col, v, INSERT_VALUES));
        }
      }
    }
  }
  PetscCall(MatAssemblyBegin(B, MAT_FINAL_ASSEMBLY));
  PetscCall(MatAssemblyEnd(B, MAT_FINAL_ASSEMBLY));
  PetscCall(PetscLogEventEnd(setvalues, NULL, NULL, NULL, NULL));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/*TEST

   test:
      nsize: 4
      args: -pc_type exotic -ksp_monitor_short -ksp_type fgmres -mg_levels_ksp_type gmres -mg_levels_ksp_max_it 1 -mg_levels_pc_type bjacobi
      output_file: output/ex45_1.out

   test:
      suffix: 2
      nsize: 4
      args: -ksp_monitor_short -da_grid_x 21 -da_grid_y 21 -da_grid_z 21 -pc_type mg -pc_mg_levels 3 -mg_levels_ksp_type richardson -mg_levels_ksp_max_it 1 -mg_levels_pc_type bjacobi

   test:
      suffix: telescope
      nsize: 4
      args: -ksp_type fgmres -ksp_monitor_short -pc_type mg -mg_levels_ksp_type richardson -mg_levels_pc_type jacobi -pc_mg_levels 2 -da_grid_x 65 -da_grid_y 65 -da_grid_z 65 -mg_coarse_pc_type telescope -mg_coarse_pc_telescope_ignore_kspcomputeoperators -mg_coarse_pc_telescope_reduction_factor 4 -mg_coarse_telescope_pc_type mg -mg_coarse_telescope_pc_mg_galerkin pmat -mg_coarse_telescope_pc_mg_levels 3 -mg_coarse_telescope_mg_levels_ksp_type richardson -mg_coarse_telescope_mg_levels_pc_type jacobi -mg_levels_ksp_type richardson -mg_coarse_telescope_mg_levels_ksp_type richardson -ksp_rtol 1.0e-4

   test:
      suffix: telescope_2
      nsize: 4
      args: -ksp_type fgmres -ksp_monitor_short -pc_type mg -mg_levels_ksp_type richardson -mg_levels_pc_type jacobi -pc_mg_levels 2 -da_grid_x 65 -da_grid_y 65 -da_grid_z 65 -mg_coarse_pc_type telescope -mg_coarse_pc_telescope_reduction_factor 2 -mg_coarse_telescope_pc_type mg -mg_coarse_telescope_pc_mg_galerkin pmat -mg_coarse_telescope_pc_mg_levels 3 -mg_coarse_telescope_mg_levels_ksp_type richardson -mg_coarse_telescope_mg_levels_pc_type jacobi -mg_levels_ksp_type richardson -mg_coarse_telescope_mg_levels_ksp_type richardson -ksp_rtol 1.0e-4

TEST*/
````

## SNES ex12.c

- Selected by: Tutorials by physics
- Rendered listing: <https://petsc.org/release/src/snes/tutorials/ex12.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/snes/tutorials/ex12.c>

````c
static char help[] = "Poisson Problem in 2d and 3d with simplicial finite elements.\n\
We solve the Poisson problem in a rectangular\n\
domain, using a parallel unstructured mesh (DMPLEX) to discretize it.\n\
This example supports discretized auxiliary fields (conductivity) as well as\n\
multilevel nonlinear solvers.\n\n\n";

/*
A visualization of the adaptation can be accomplished using:

  -dm_adapt_view hdf5:$PWD/adapt.h5 -sol_adapt_view hdf5:$PWD/adapt.h5::append -dm_adapt_pre_view hdf5:$PWD/orig.h5 -sol_adapt_pre_view hdf5:$PWD/orig.h5::append

Information on refinement:

   -info :~sys,vec,is,mat,ksp,snes,ts
*/

#include <petscdmplex.h>
#include <petscdmadaptor.h>
#include <petscsnes.h>
#include <petscds.h>
#include <petscviewerhdf5.h>

typedef enum {
  NEUMANN,
  DIRICHLET,
  NONE
} BCType;
typedef enum {
  RUN_FULL,
  RUN_EXACT,
  RUN_TEST,
  RUN_PERF
} RunType;
typedef enum {
  COEFF_NONE,
  COEFF_ANALYTIC,
  COEFF_FIELD,
  COEFF_NONLINEAR,
  COEFF_BALL,
  COEFF_CROSS,
  COEFF_CHECKERBOARD_0,
  COEFF_CHECKERBOARD_1
} CoeffType;

typedef struct {
  RunType   runType;    /* Whether to run tests, or solve the full problem */
  PetscBool jacobianMF; /* Whether to calculate the Jacobian action on the fly */
  PetscBool showInitial, showSolution, restart, quiet, nonzInit;
  /* Problem definition */
  BCType    bcType;
  CoeffType variableCoefficient;
  PetscErrorCode (**exactFuncs)(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx);
  PetscBool fieldBC;
  void (**exactFields)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]);
  PetscBool bdIntegral; /* Compute the integral of the solution on the boundary */
  /* Reproducing tests from SISC 40(3), pp. A1473-A1493, 2018 */
  PetscInt  div;   /* Number of divisions */
  PetscInt  k;     /* Parameter for checkerboard coefficient */
  PetscInt *kgrid; /* Random parameter grid */
  PetscBool rand;  /* Make random assignments */
  /* Solver */
  PC        pcmg;     /* This is needed for error monitoring */
  PetscBool checkksp; /* Whether to check the KSPSolve for runType == RUN_TEST */
} AppCtx;

static PetscErrorCode zero(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  u[0] = 0.0;
  return PETSC_SUCCESS;
}

static PetscErrorCode ecks(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  u[0] = x[0];
  return PETSC_SUCCESS;
}

/*
  In 2D for Dirichlet conditions, we use exact solution:

    u = x^2 + y^2
    f = 4

  so that

    -\Delta u + f = -4 + 4 = 0

  For Neumann conditions, we have

    -\nabla u \cdot -\hat y |_{y=0} =  (2y)|_{y=0} =  0 (bottom)
    -\nabla u \cdot  \hat y |_{y=1} = -(2y)|_{y=1} = -2 (top)
    -\nabla u \cdot -\hat x |_{x=0} =  (2x)|_{x=0} =  0 (left)
    -\nabla u \cdot  \hat x |_{x=1} = -(2x)|_{x=1} = -2 (right)

  Which we can express as

    \nabla u \cdot  \hat n|_\Gamma = {2 x, 2 y} \cdot \hat n = 2 (x + y)

  The boundary integral of this solution is (assuming we are not orienting the edges)

    \int^1_0 x^2 dx + \int^1_0 (1 + y^2) dy + \int^1_0 (x^2 + 1) dx + \int^1_0 y^2 dy = 1/3 + 4/3 + 4/3 + 1/3 = 3 1/3
*/
static PetscErrorCode quadratic_u_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = x[0] * x[0] + x[1] * x[1];
  return PETSC_SUCCESS;
}

static void quadratic_u_field_2d(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar uexact[])
{
  uexact[0] = a[0];
}

static PetscErrorCode ball_u_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  const PetscReal alpha   = 500.;
  const PetscReal radius2 = PetscSqr(0.15);
  const PetscReal r2      = PetscSqr(x[0] - 0.5) + PetscSqr(x[1] - 0.5);
  const PetscReal xi      = alpha * (radius2 - r2);

  *u = PetscTanhScalar(xi) + 1.0;
  return PETSC_SUCCESS;
}

static PetscErrorCode cross_u_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  const PetscReal alpha = 50 * 4;
  const PetscReal xy    = (x[0] - 0.5) * (x[1] - 0.5);

  *u = PetscSinReal(alpha * xy) * (alpha * PetscAbsReal(xy) < 2 * PETSC_PI ? 1 : 0.01);
  return PETSC_SUCCESS;
}

static void f0_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = 4.0;
}

static void f0_ball_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscInt        d;
  const PetscReal alpha = 500., radius2 = PetscSqr(0.15);
  PetscReal       r2, xi;

  for (d = 0, r2 = 0.0; d < dim; ++d) r2 += PetscSqr(x[d] - 0.5);
  xi    = alpha * (radius2 - r2);
  f0[0] = (-2.0 * dim * alpha - 8.0 * PetscSqr(alpha) * r2 * PetscTanhReal(xi)) * PetscSqr(1.0 / PetscCoshReal(xi));
}

static void f0_cross_u_2d(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal alpha = 50 * 4;
  const PetscReal xy    = (x[0] - 0.5) * (x[1] - 0.5);

  f0[0] = PetscSinReal(alpha * xy) * (alpha * PetscAbsReal(xy) < 2 * PETSC_PI ? 1 : 0.01);
}

static void f0_checkerboard_0_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = -20.0 * PetscExpReal(-(PetscSqr(x[0] - 0.5) + PetscSqr(x[1] - 0.5)));
}

static void f0_bd_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscInt d;
  for (d = 0, f0[0] = 0.0; d < dim; ++d) f0[0] += -n[d] * 2.0 * x[d];
}

/* gradU[comp*dim+d] = {u_x, u_y} or {u_x, u_y, u_z} */
static void f1_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) f1[d] = u_x[d];
}

/* < \nabla v, \nabla u + {\nabla u}^T >
   This just gives \nabla u, give the perdiagonal for the transpose */
static void g3_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) g3[d * dim + d] = 1.0;
}

/*
  In 2D for x periodicity and y Dirichlet conditions, we use exact solution:

    u = sin(2 pi x)
    f = -4 pi^2 sin(2 pi x)

  so that

    -\Delta u + f = 4 pi^2 sin(2 pi x) - 4 pi^2 sin(2 pi x) = 0
*/
static PetscErrorCode xtrig_u_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = PetscSinReal(2.0 * PETSC_PI * x[0]);
  return PETSC_SUCCESS;
}

static void f0_xtrig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = -4.0 * PetscSqr(PETSC_PI) * PetscSinReal(2.0 * PETSC_PI * x[0]);
}

/*
  In 2D for x-y periodicity, we use exact solution:

    u = sin(2 pi x) sin(2 pi y)
    f = -8 pi^2 sin(2 pi x)

  so that

    -\Delta u + f = 4 pi^2 sin(2 pi x) sin(2 pi y) + 4 pi^2 sin(2 pi x) sin(2 pi y) - 8 pi^2 sin(2 pi x) = 0
*/
static PetscErrorCode xytrig_u_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = PetscSinReal(2.0 * PETSC_PI * x[0]) * PetscSinReal(2.0 * PETSC_PI * x[1]);
  return PETSC_SUCCESS;
}

static void f0_xytrig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = -8.0 * PetscSqr(PETSC_PI) * PetscSinReal(2.0 * PETSC_PI * x[0]);
}

/*
  In 2D for Dirichlet conditions with a variable coefficient, we use exact solution:

    u  = x^2 + y^2
    f  = 6 (x + y)
    nu = (x + y)

  so that

    -\div \nu \grad u + f = -6 (x + y) + 6 (x + y) = 0
*/
static PetscErrorCode nu_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = x[0] + x[1];
  return PETSC_SUCCESS;
}

static PetscErrorCode checkerboardCoeff(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  AppCtx  *user = (AppCtx *)ctx;
  PetscInt div  = user->div;
  PetscInt k    = user->k;
  PetscInt mask = 0, ind = 0, d;

  PetscFunctionBeginUser;
  for (d = 0; d < dim; ++d) mask = (mask + (PetscInt)(x[d] * div)) % 2;
  if (user->kgrid) {
    for (d = 0; d < dim; ++d) {
      if (d > 0) ind *= dim;
      ind += (PetscInt)(x[d] * div);
    }
    k = user->kgrid[ind];
  }
  u[0] = mask ? 1.0 : PetscPowRealInt(10.0, -k);
  PetscFunctionReturn(PETSC_SUCCESS);
}

void f0_analytic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = 6.0 * (x[0] + x[1]);
}

/* gradU[comp*dim+d] = {u_x, u_y} or {u_x, u_y, u_z} */
void f1_analytic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) f1[d] = (x[0] + x[1]) * u_x[d];
}

void f1_field_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) f1[d] = a[0] * u_x[d];
}

/* < \nabla v, \nabla u + {\nabla u}^T >
   This just gives \nabla u, give the perdiagonal for the transpose */
void g3_analytic_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) g3[d * dim + d] = x[0] + x[1];
}

void g3_field_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) g3[d * dim + d] = a[0];
}

/*
  In 2D for Dirichlet conditions with a nonlinear coefficient (p-Laplacian with p = 4), we use exact solution:

    u  = x^2 + y^2
    f  = 16 (x^2 + y^2)
    nu = 1/2 |grad u|^2

  so that

    -\div \nu \grad u + f = -16 (x^2 + y^2) + 16 (x^2 + y^2) = 0
*/
void f0_analytic_nonlinear_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = 16.0 * (x[0] * x[0] + x[1] * x[1]);
}

/* gradU[comp*dim+d] = {u_x, u_y} or {u_x, u_y, u_z} */
void f1_analytic_nonlinear_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  PetscScalar nu = 0.0;
  PetscInt    d;
  for (d = 0; d < dim; ++d) nu += u_x[d] * u_x[d];
  for (d = 0; d < dim; ++d) f1[d] = 0.5 * nu * u_x[d];
}

/*
  grad (u + eps w) - grad u = eps grad w

  1/2 |grad (u + eps w)|^2 grad (u + eps w) - 1/2 |grad u|^2 grad u
= 1/2 (|grad u|^2 + 2 eps <grad u,grad w>) (grad u + eps grad w) - 1/2 |grad u|^2 grad u
= 1/2 (eps |grad u|^2 grad w + 2 eps <grad u,grad w> grad u)
= eps (1/2 |grad u|^2 grad w + grad u <grad u,grad w>)
*/
void g3_analytic_nonlinear_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  PetscScalar nu = 0.0;
  PetscInt    d, e;
  for (d = 0; d < dim; ++d) nu += u_x[d] * u_x[d];
  for (d = 0; d < dim; ++d) {
    g3[d * dim + d] = 0.5 * nu;
    for (e = 0; e < dim; ++e) g3[d * dim + e] += u_x[d] * u_x[e];
  }
}

/*
  In 3D for Dirichlet conditions we use exact solution:

    u = 2/3 (x^2 + y^2 + z^2)
    f = 4

  so that

    -\Delta u + f = -2/3 * 6 + 4 = 0

  For Neumann conditions, we have

    -\nabla u \cdot -\hat z |_{z=0} =  (2z)|_{z=0} =  0 (bottom)
    -\nabla u \cdot  \hat z |_{z=1} = -(2z)|_{z=1} = -2 (top)
    -\nabla u \cdot -\hat y |_{y=0} =  (2y)|_{y=0} =  0 (front)
    -\nabla u \cdot  \hat y |_{y=1} = -(2y)|_{y=1} = -2 (back)
    -\nabla u \cdot -\hat x |_{x=0} =  (2x)|_{x=0} =  0 (left)
    -\nabla u \cdot  \hat x |_{x=1} = -(2x)|_{x=1} = -2 (right)

  Which we can express as

    \nabla u \cdot  \hat n|_\Gamma = {2 x, 2 y, 2z} \cdot \hat n = 2 (x + y + z)
*/
static PetscErrorCode quadratic_u_3d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = 2.0 * (x[0] * x[0] + x[1] * x[1] + x[2] * x[2]) / 3.0;
  return PETSC_SUCCESS;
}

static PetscErrorCode ball_u_3d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  const PetscReal alpha   = 500.;
  const PetscReal radius2 = PetscSqr(0.15);
  const PetscReal r2      = PetscSqr(x[0] - 0.5) + PetscSqr(x[1] - 0.5) + PetscSqr(x[2] - 0.5);
  const PetscReal xi      = alpha * (radius2 - r2);

  *u = PetscTanhScalar(xi) + 1.0;
  return PETSC_SUCCESS;
}

static void quadratic_u_field_3d(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar uexact[])
{
  uexact[0] = a[0];
}

static PetscErrorCode cross_u_3d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  const PetscReal alpha = 50 * 4;
  const PetscReal xyz   = (x[0] - 0.5) * (x[1] - 0.5) * (x[2] - 0.5);

  *u = PetscSinReal(alpha * xyz) * (alpha * PetscAbsReal(xyz) < 2 * PETSC_PI ? (alpha * PetscAbsReal(xyz) > -2 * PETSC_PI ? 1.0 : 0.01) : 0.01);
  return PETSC_SUCCESS;
}

static void f0_cross_u_3d(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal alpha = 50 * 4;
  const PetscReal xyz   = (x[0] - 0.5) * (x[1] - 0.5) * (x[2] - 0.5);

  f0[0] = PetscSinReal(alpha * xyz) * (alpha * PetscAbsReal(xyz) < 2 * PETSC_PI ? (alpha * PetscAbsReal(xyz) > -2 * PETSC_PI ? 1.0 : 0.01) : 0.01);
}

static void bd_integral_2d(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar *uint)
{
  uint[0] = u[0];
}

static PetscErrorCode ProcessOptions(MPI_Comm comm, AppCtx *options)
{
  const char *bcTypes[3]    = {"neumann", "dirichlet", "none"};
  const char *runTypes[4]   = {"full", "exact", "test", "perf"};
  const char *coeffTypes[8] = {"none", "analytic", "field", "nonlinear", "ball", "cross", "checkerboard_0", "checkerboard_1"};
  PetscInt    bc, run, coeff;

  PetscFunctionBeginUser;
  options->runType             = RUN_FULL;
  options->bcType              = DIRICHLET;
  options->variableCoefficient = COEFF_NONE;
  options->fieldBC             = PETSC_FALSE;
  options->jacobianMF          = PETSC_FALSE;
  options->showInitial         = PETSC_FALSE;
  options->showSolution        = PETSC_FALSE;
  options->restart             = PETSC_FALSE;
  options->quiet               = PETSC_FALSE;
  options->nonzInit            = PETSC_FALSE;
  options->bdIntegral          = PETSC_FALSE;
  options->checkksp            = PETSC_FALSE;
  options->div                 = 4;
  options->k                   = 1;
  options->kgrid               = NULL;
  options->rand                = PETSC_FALSE;

  PetscOptionsBegin(comm, "", "Poisson Problem Options", "DMPLEX");
  run = options->runType;
  PetscCall(PetscOptionsEList("-run_type", "The run type", "ex12.c", runTypes, 4, runTypes[options->runType], &run, NULL));
  options->runType = (RunType)run;
  bc               = options->bcType;
  PetscCall(PetscOptionsEList("-bc_type", "Type of boundary condition", "ex12.c", bcTypes, 3, bcTypes[options->bcType], &bc, NULL));
  options->bcType = (BCType)bc;
  coeff           = options->variableCoefficient;
  PetscCall(PetscOptionsEList("-variable_coefficient", "Type of variable coefficient", "ex12.c", coeffTypes, 8, coeffTypes[options->variableCoefficient], &coeff, NULL));
  options->variableCoefficient = (CoeffType)coeff;

  PetscCall(PetscOptionsBool("-field_bc", "Use a field representation for the BC", "ex12.c", options->fieldBC, &options->fieldBC, NULL));
  PetscCall(PetscOptionsBool("-jacobian_mf", "Calculate the action of the Jacobian on the fly", "ex12.c", options->jacobianMF, &options->jacobianMF, NULL));
  PetscCall(PetscOptionsBool("-show_initial", "Output the initial guess for verification", "ex12.c", options->showInitial, &options->showInitial, NULL));
  PetscCall(PetscOptionsBool("-show_solution", "Output the solution for verification", "ex12.c", options->showSolution, &options->showSolution, NULL));
  PetscCall(PetscOptionsBool("-restart", "Read in the mesh and solution from a file", "ex12.c", options->restart, &options->restart, NULL));
  PetscCall(PetscOptionsBool("-quiet", "Don't print any vecs", "ex12.c", options->quiet, &options->quiet, NULL));
  PetscCall(PetscOptionsBool("-nonzero_initial_guess", "nonzero initial guess", "ex12.c", options->nonzInit, &options->nonzInit, NULL));
  PetscCall(PetscOptionsBool("-bd_integral", "Compute the integral of the solution on the boundary", "ex12.c", options->bdIntegral, &options->bdIntegral, NULL));
  if (options->runType == RUN_TEST) PetscCall(PetscOptionsBool("-run_test_check_ksp", "Check solution of KSP", "ex12.c", options->checkksp, &options->checkksp, NULL));
  PetscCall(PetscOptionsInt("-div", "The number of division for the checkerboard coefficient", "ex12.c", options->div, &options->div, NULL));
  PetscCall(PetscOptionsInt("-k", "The exponent for the checkerboard coefficient", "ex12.c", options->k, &options->k, NULL));
  PetscCall(PetscOptionsBool("-k_random", "Assign random k values to checkerboard", "ex12.c", options->rand, &options->rand, NULL));
  PetscOptionsEnd();
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode CreateBCLabel(DM dm, const char name[])
{
  DM      plex;
  DMLabel label;

  PetscFunctionBeginUser;
  PetscCall(DMCreateLabel(dm, name));
  PetscCall(DMGetLabel(dm, name, &label));
  PetscCall(DMConvert(dm, DMPLEX, &plex));
  PetscCall(DMPlexMarkBoundaryFaces(plex, 1, label));
  PetscCall(DMDestroy(&plex));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode CreateMesh(MPI_Comm comm, AppCtx *user, DM *dm)
{
  PetscFunctionBeginUser;
  PetscCall(DMCreate(comm, dm));
  PetscCall(DMSetType(*dm, DMPLEX));
  PetscCall(DMSetFromOptions(*dm));
  {
    char      convType[256];
    PetscBool flg;

    PetscOptionsBegin(comm, "", "Mesh conversion options", "DMPLEX");
    PetscCall(PetscOptionsFList("-dm_plex_convert_type", "Convert DMPlex to another format", "ex12", DMList, DMPLEX, convType, 256, &flg));
    PetscOptionsEnd();
    if (flg) {
      DM dmConv;

      PetscCall(DMConvert(*dm, convType, &dmConv));
      if (dmConv) {
        PetscCall(DMDestroy(dm));
        *dm = dmConv;
      }
      PetscCall(DMSetFromOptions(*dm));
      PetscCall(DMSetUp(*dm));
    }
  }
  PetscCall(DMViewFromOptions(*dm, NULL, "-dm_view"));
  if (user->rand) {
    PetscRandom r;
    PetscReal   val;
    PetscInt    dim, N, i;

    PetscCall(DMGetDimension(*dm, &dim));
    N = PetscPowInt(user->div, dim);
    PetscCall(PetscMalloc1(N, &user->kgrid));
    PetscCall(PetscRandomCreate(PETSC_COMM_SELF, &r));
    PetscCall(PetscRandomSetFromOptions(r));
    PetscCall(PetscRandomSetInterval(r, 0.0, user->k));
    PetscCall(PetscRandomSetSeed(r, 1973));
    PetscCall(PetscRandomSeed(r));
    for (i = 0; i < N; ++i) {
      PetscCall(PetscRandomGetValueReal(r, &val));
      user->kgrid[i] = 1 + (PetscInt)val;
    }
    PetscCall(PetscRandomDestroy(&r));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupProblem(DM dm, AppCtx *user)
{
  PetscDS          ds;
  DMLabel          label;
  PetscWeakForm    wf;
  const PetscReal *L;
  const PetscInt   id = 1;
  PetscInt         bd, dim;

  PetscFunctionBeginUser;
  PetscCall(DMGetDS(dm, &ds));
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMGetPeriodicity(dm, NULL, NULL, &L));
  switch (user->variableCoefficient) {
  case COEFF_NONE:
    if (L && L[0]) {
      if (L && L[1]) {
        PetscCall(PetscDSSetResidual(ds, 0, f0_xytrig_u, f1_u));
        PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_uu));
      } else {
        PetscCall(PetscDSSetResidual(ds, 0, f0_xtrig_u, f1_u));
        PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_uu));
      }
    } else {
      PetscCall(PetscDSSetResidual(ds, 0, f0_u, f1_u));
      PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_uu));
    }
    break;
  case COEFF_ANALYTIC:
    PetscCall(PetscDSSetResidual(ds, 0, f0_analytic_u, f1_analytic_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_analytic_uu));
    break;
  case COEFF_FIELD:
    PetscCall(PetscDSSetResidual(ds, 0, f0_analytic_u, f1_field_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_field_uu));
    break;
  case COEFF_NONLINEAR:
    PetscCall(PetscDSSetResidual(ds, 0, f0_analytic_nonlinear_u, f1_analytic_nonlinear_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_analytic_nonlinear_uu));
    break;
  case COEFF_BALL:
    PetscCall(PetscDSSetResidual(ds, 0, f0_ball_u, f1_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_uu));
    break;
  case COEFF_CROSS:
    switch (dim) {
    case 2:
      PetscCall(PetscDSSetResidual(ds, 0, f0_cross_u_2d, f1_u));
      break;
    case 3:
      PetscCall(PetscDSSetResidual(ds, 0, f0_cross_u_3d, f1_u));
      break;
    default:
      SETERRQ(PETSC_COMM_WORLD, PETSC_ERR_ARG_OUTOFRANGE, "Invalid dimension %" PetscInt_FMT, dim);
    }
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_uu));
    break;
  case COEFF_CHECKERBOARD_0:
    PetscCall(PetscDSSetResidual(ds, 0, f0_checkerboard_0_u, f1_field_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_field_uu));
    break;
  default:
    SETERRQ(PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Invalid variable coefficient type %d", user->variableCoefficient);
  }
  switch (dim) {
  case 2:
    switch (user->variableCoefficient) {
    case COEFF_BALL:
      user->exactFuncs[0] = ball_u_2d;
      break;
    case COEFF_CROSS:
      user->exactFuncs[0] = cross_u_2d;
      break;
    case COEFF_CHECKERBOARD_0:
      user->exactFuncs[0] = zero;
      break;
    default:
      if (L && L[0]) {
        if (L && L[1]) {
          user->exactFuncs[0] = xytrig_u_2d;
        } else {
          user->exactFuncs[0] = xtrig_u_2d;
        }
      } else {
        user->exactFuncs[0]  = quadratic_u_2d;
        user->exactFields[0] = quadratic_u_field_2d;
      }
    }
    if (user->bcType == NEUMANN) {
      PetscCall(DMGetLabel(dm, "boundary", &label));
      PetscCall(DMAddBoundary(dm, DM_BC_NATURAL, "wall", label, 1, &id, 0, 0, NULL, NULL, NULL, user, &bd));
      PetscCall(PetscDSGetBoundary(ds, bd, &wf, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL));
      PetscCall(PetscWeakFormSetIndexBdResidual(wf, label, id, 0, 0, 0, f0_bd_u, 0, NULL));
    }
    break;
  case 3:
    switch (user->variableCoefficient) {
    case COEFF_BALL:
      user->exactFuncs[0] = ball_u_3d;
      break;
    case COEFF_CROSS:
      user->exactFuncs[0] = cross_u_3d;
      break;
    default:
      user->exactFuncs[0]  = quadratic_u_3d;
      user->exactFields[0] = quadratic_u_field_3d;
    }
    if (user->bcType == NEUMANN) {
      PetscCall(DMGetLabel(dm, "boundary", &label));
      PetscCall(DMAddBoundary(dm, DM_BC_NATURAL, "wall", label, 1, &id, 0, 0, NULL, NULL, NULL, user, &bd));
      PetscCall(PetscDSGetBoundary(ds, bd, &wf, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL));
      PetscCall(PetscWeakFormSetIndexBdResidual(wf, label, id, 0, 0, 0, f0_bd_u, 0, NULL));
    }
    break;
  default:
    SETERRQ(PETSC_COMM_WORLD, PETSC_ERR_ARG_OUTOFRANGE, "Invalid dimension %" PetscInt_FMT, dim);
  }
  /* Setup constants */
  switch (user->variableCoefficient) {
  case COEFF_CHECKERBOARD_0: {
    PetscScalar constants[2];

    constants[0] = user->div;
    constants[1] = user->k;
    PetscCall(PetscDSSetConstants(ds, 2, constants));
  } break;
  default:
    break;
  }
  PetscCall(PetscDSSetExactSolution(ds, 0, user->exactFuncs[0], user));
  /* Setup Boundary Conditions */
  if (user->bcType == DIRICHLET) {
    PetscCall(DMGetLabel(dm, "marker", &label));
    if (!label) {
      /* Right now, p4est cannot create labels immediately */
      PetscCall(PetscDSAddBoundaryByName(ds, user->fieldBC ? DM_BC_ESSENTIAL_FIELD : DM_BC_ESSENTIAL, "wall", "marker", 1, &id, 0, 0, NULL, user->fieldBC ? (PetscVoidFn *)user->exactFields[0] : (PetscVoidFn *)user->exactFuncs[0], NULL, user, NULL));
    } else {
      PetscCall(DMAddBoundary(dm, user->fieldBC ? DM_BC_ESSENTIAL_FIELD : DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, user->fieldBC ? (PetscVoidFn *)user->exactFields[0] : (PetscVoidFn *)user->exactFuncs[0], NULL, user, NULL));
    }
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupMaterial(DM dm, DM dmAux, AppCtx *user)
{
  PetscErrorCode (*matFuncs[1])(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar u[], PetscCtx ctx) = {nu_2d};
  PetscCtx ctx[1];
  Vec      nu;

  PetscFunctionBegin;
  ctx[0] = user;
  if (user->variableCoefficient == COEFF_CHECKERBOARD_0) matFuncs[0] = checkerboardCoeff;
  PetscCall(DMCreateLocalVector(dmAux, &nu));
  PetscCall(PetscObjectSetName((PetscObject)nu, "Coefficient"));
  PetscCall(DMProjectFunctionLocal(dmAux, 0.0, matFuncs, ctx, INSERT_ALL_VALUES, nu));
  PetscCall(DMSetAuxiliaryVec(dm, NULL, 0, 0, nu));
  PetscCall(VecDestroy(&nu));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupBC(DM dm, DM dmAux, AppCtx *user)
{
  PetscErrorCode (*bcFuncs[1])(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar u[], PetscCtx ctx);
  Vec      uexact;
  PetscInt dim;

  PetscFunctionBegin;
  PetscCall(DMGetDimension(dm, &dim));
  if (dim == 2) bcFuncs[0] = quadratic_u_2d;
  else bcFuncs[0] = quadratic_u_3d;
  PetscCall(DMCreateLocalVector(dmAux, &uexact));
  PetscCall(DMProjectFunctionLocal(dmAux, 0.0, bcFuncs, NULL, INSERT_ALL_VALUES, uexact));
  PetscCall(DMSetAuxiliaryVec(dm, NULL, 0, 0, uexact));
  PetscCall(VecDestroy(&uexact));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupAuxDM(DM dm, PetscFE feAux, AppCtx *user)
{
  DM dmAux, coordDM;

  PetscFunctionBegin;
  /* MUST call DMGetCoordinateDM() in order to get p4est setup if present */
  PetscCall(DMGetCoordinateDM(dm, &coordDM));
  if (!feAux) PetscFunctionReturn(PETSC_SUCCESS);
  PetscCall(DMClone(dm, &dmAux));
  PetscCall(DMSetCoordinateDM(dmAux, coordDM));
  PetscCall(DMSetField(dmAux, 0, NULL, (PetscObject)feAux));
  PetscCall(DMCreateDS(dmAux));
  if (user->fieldBC) PetscCall(SetupBC(dm, dmAux, user));
  else PetscCall(SetupMaterial(dm, dmAux, user));
  PetscCall(DMDestroy(&dmAux));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupDiscretization(DM dm, AppCtx *user)
{
  DM        plex, cdm = dm;
  PetscFE   fe, feAux = NULL;
  PetscBool simplex;
  PetscInt  dim;

  PetscFunctionBeginUser;
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMConvert(dm, DMPLEX, &plex));
  PetscCall(DMPlexIsSimplex(plex, &simplex));
  PetscCall(DMDestroy(&plex));
  PetscCall(PetscFECreateDefault(PETSC_COMM_SELF, dim, 1, simplex, NULL, -1, &fe));
  PetscCall(PetscObjectSetName((PetscObject)fe, "potential"));
  if (user->variableCoefficient == COEFF_FIELD || user->variableCoefficient == COEFF_CHECKERBOARD_0) {
    PetscCall(PetscFECreateDefault(PETSC_COMM_SELF, dim, 1, simplex, "mat_", -1, &feAux));
    PetscCall(PetscObjectSetName((PetscObject)feAux, "coefficient"));
    PetscCall(PetscFECopyQuadrature(fe, feAux));
  } else if (user->fieldBC) {
    PetscCall(PetscFECreateDefault(PETSC_COMM_SELF, dim, 1, simplex, "bc_", -1, &feAux));
    PetscCall(PetscFECopyQuadrature(fe, feAux));
  }
  /* Set discretization and boundary conditions for each mesh */
  PetscCall(DMSetField(dm, 0, NULL, (PetscObject)fe));
  PetscCall(DMCreateDS(dm));
  PetscCall(SetupProblem(dm, user));
  while (cdm) {
    PetscCall(SetupAuxDM(cdm, feAux, user));
    if (user->bcType == DIRICHLET) {
      PetscBool hasLabel;

      PetscCall(DMHasLabel(cdm, "marker", &hasLabel));
      if (!hasLabel) PetscCall(CreateBCLabel(cdm, "marker"));
    }
    PetscCall(DMCopyDisc(dm, cdm));
    PetscCall(DMGetCoarseDM(cdm, &cdm));
  }
  PetscCall(PetscFEDestroy(&fe));
  PetscCall(PetscFEDestroy(&feAux));
  PetscFunctionReturn(PETSC_SUCCESS);
}

int main(int argc, char **argv)
{
  DM           dm;          /* Problem specification */
  SNES         snes;        /* nonlinear solver */
  Vec          u;           /* solution vector */
  Mat          A, J;        /* Jacobian matrix */
  MatNullSpace nullSpace;   /* May be necessary for Neumann conditions */
  AppCtx       user;        /* user-defined work context */
  JacActionCtx userJ;       /* context for Jacobian MF action */
  PetscReal    error = 0.0; /* L_2 error in the solution */

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(ProcessOptions(PETSC_COMM_WORLD, &user));
  PetscCall(SNESCreate(PETSC_COMM_WORLD, &snes));
  PetscCall(CreateMesh(PETSC_COMM_WORLD, &user, &dm));
  PetscCall(SNESSetDM(snes, dm));
  PetscCall(DMSetApplicationContext(dm, &user));

  PetscCall(PetscMalloc2(1, &user.exactFuncs, 1, &user.exactFields));
  PetscCall(SetupDiscretization(dm, &user));

  PetscCall(DMCreateGlobalVector(dm, &u));
  PetscCall(PetscObjectSetName((PetscObject)u, "potential"));

  PetscCall(DMCreateMatrix(dm, &J));
  if (user.jacobianMF) {
    PetscInt M, m, N, n;

    PetscCall(MatGetSize(J, &M, &N));
    PetscCall(MatGetLocalSize(J, &m, &n));
    PetscCall(MatCreate(PETSC_COMM_WORLD, &A));
    PetscCall(MatSetSizes(A, m, n, M, N));
    PetscCall(MatSetType(A, MATSHELL));
    PetscCall(MatSetUp(A));
#if 0
    PetscCall(MatShellSetOperation(A, MATOP_MULT, (PetscErrorCodeFn *)FormJacobianAction));
#endif

    userJ.dm   = dm;
    userJ.J    = J;
    userJ.user = &user;

    PetscCall(DMCreateLocalVector(dm, &userJ.u));
    if (user.fieldBC) PetscCall(DMProjectFieldLocal(dm, 0.0, userJ.u, user.exactFields, INSERT_BC_VALUES, userJ.u));
    else PetscCall(DMProjectFunctionLocal(dm, 0.0, user.exactFuncs, NULL, INSERT_BC_VALUES, userJ.u));
    PetscCall(MatShellSetContext(A, &userJ));
  } else {
    A = J;
  }

  nullSpace = NULL;
  if (user.bcType != DIRICHLET) {
    PetscCall(MatNullSpaceCreate(PetscObjectComm((PetscObject)dm), PETSC_TRUE, 0, NULL, &nullSpace));
    PetscCall(MatSetNullSpace(A, nullSpace));
  }

  PetscCall(DMPlexSetSNESLocalFEM(dm, PETSC_FALSE, &user));
  PetscCall(SNESSetJacobian(snes, A, J, NULL, NULL));

  PetscCall(SNESSetFromOptions(snes));

  if (user.fieldBC) PetscCall(DMProjectField(dm, 0.0, u, user.exactFields, INSERT_ALL_VALUES, u));
  else PetscCall(DMProjectFunction(dm, 0.0, user.exactFuncs, NULL, INSERT_ALL_VALUES, u));
  if (user.restart) {
#if defined(PETSC_HAVE_HDF5)
    PetscViewer viewer;
    char        filename[PETSC_MAX_PATH_LEN];

    PetscCall(PetscOptionsGetString(NULL, NULL, "-dm_plex_filename", filename, sizeof(filename), NULL));
    PetscCall(PetscViewerCreate(PETSC_COMM_WORLD, &viewer));
    PetscCall(PetscViewerSetType(viewer, PETSCVIEWERHDF5));
    PetscCall(PetscViewerFileSetMode(viewer, FILE_MODE_READ));
    PetscCall(PetscViewerFileSetName(viewer, filename));
    PetscCall(PetscViewerHDF5PushGroup(viewer, "/fields"));
    PetscCall(VecLoad(u, viewer));
    PetscCall(PetscViewerHDF5PopGroup(viewer));
    PetscCall(PetscViewerDestroy(&viewer));
#endif
  }
  if (user.showInitial) {
    Vec lv;
    PetscCall(DMGetLocalVector(dm, &lv));
    PetscCall(DMGlobalToLocalBegin(dm, u, INSERT_VALUES, lv));
    PetscCall(DMGlobalToLocalEnd(dm, u, INSERT_VALUES, lv));
    PetscCall(DMPrintLocalVec(dm, "Local function", 1.0e-10, lv));
    PetscCall(DMRestoreLocalVector(dm, &lv));
  }
  if (user.runType == RUN_FULL || user.runType == RUN_EXACT) {
    PetscErrorCode (*initialGuess[1])(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar u[], PetscCtx ctx) = {zero};

    if (user.nonzInit) initialGuess[0] = ecks;
    if (user.runType == RUN_FULL) PetscCall(DMProjectFunction(dm, 0.0, initialGuess, NULL, INSERT_VALUES, u));
    PetscCall(VecViewFromOptions(u, NULL, "-guess_vec_view"));
    PetscCall(SNESSolve(snes, NULL, u));
    PetscCall(SNESGetSolution(snes, &u));
    PetscCall(SNESGetDM(snes, &dm));

    if (user.showSolution) {
      PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Solution\n"));
      PetscCall(VecFilter(u, 3.0e-9));
      PetscCall(VecView(u, PETSC_VIEWER_STDOUT_WORLD));
    }
  } else if (user.runType == RUN_PERF) {
    Vec       r;
    PetscReal res = 0.0;

    PetscCall(SNESGetFunction(snes, &r, NULL, NULL));
    PetscCall(SNESComputeFunction(snes, u, r));
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Initial Residual\n"));
    PetscCall(VecFilter(r, 1.0e-10));
    PetscCall(VecNorm(r, NORM_2, &res));
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "L_2 Residual: %g\n", (double)res));
  } else {
    Vec       r;
    PetscReal res = 0.0, tol = 1.0e-11;

    /* Check discretization error */
    PetscCall(SNESGetFunction(snes, &r, NULL, NULL));
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Initial guess\n"));
    if (!user.quiet) PetscCall(VecView(u, PETSC_VIEWER_STDOUT_WORLD));
    PetscCall(DMComputeL2Diff(dm, 0.0, user.exactFuncs, NULL, u, &error));
    if (error < tol) PetscCall(PetscPrintf(PETSC_COMM_WORLD, "L_2 Error: < %2.1e\n", (double)tol));
    else PetscCall(PetscPrintf(PETSC_COMM_WORLD, "L_2 Error: %g\n", (double)error));
    /* Check residual */
    PetscCall(SNESComputeFunction(snes, u, r));
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Initial Residual\n"));
    PetscCall(VecFilter(r, 1.0e-10));
    if (!user.quiet) PetscCall(VecView(r, PETSC_VIEWER_STDOUT_WORLD));
    PetscCall(VecNorm(r, NORM_2, &res));
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "L_2 Residual: %g\n", (double)res));
    /* Check Jacobian */
    {
      Vec b;

      PetscCall(SNESComputeJacobian(snes, u, A, A));
      PetscCall(VecDuplicate(u, &b));
      PetscCall(VecSet(r, 0.0));
      PetscCall(SNESComputeFunction(snes, r, b));
      PetscCall(MatMult(A, u, r));
      PetscCall(VecAXPY(r, 1.0, b));
      PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Au - b = Au + F(0)\n"));
      PetscCall(VecFilter(r, 1.0e-10));
      if (!user.quiet) PetscCall(VecView(r, PETSC_VIEWER_STDOUT_WORLD));
      PetscCall(VecNorm(r, NORM_2, &res));
      PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Linear L_2 Residual: %g\n", (double)res));
      /* check solver */
      if (user.checkksp) {
        KSP ksp;

        if (nullSpace) PetscCall(MatNullSpaceRemove(nullSpace, u));
        PetscCall(SNESComputeJacobian(snes, u, A, J));
        PetscCall(MatMult(A, u, b));
        PetscCall(SNESGetKSP(snes, &ksp));
        PetscCall(KSPSetOperators(ksp, A, J));
        PetscCall(KSPSolve(ksp, b, r));
        PetscCall(VecAXPY(r, -1.0, u));
        PetscCall(VecNorm(r, NORM_2, &res));
        PetscCall(PetscPrintf(PETSC_COMM_WORLD, "KSP Error: %g\n", (double)res));
      }
      PetscCall(VecDestroy(&b));
    }
  }
  PetscCall(VecViewFromOptions(u, NULL, "-vec_view"));
  {
    Vec nu;

    PetscCall(DMGetAuxiliaryVec(dm, NULL, 0, 0, &nu));
    if (nu) PetscCall(VecViewFromOptions(nu, NULL, "-coeff_view"));
  }

  if (user.bdIntegral) {
    DMLabel         label;
    PetscBdPointFn *func[1] = {bd_integral_2d};
    PetscInt        id      = 1;
    PetscScalar     bdInt   = 0.0;
    PetscReal       exact   = 3.3333333333;

    PetscCall(DMGetLabel(dm, "marker", &label));
    PetscCall(DMPlexComputeBdIntegral(dm, u, label, 1, &id, func, &bdInt, NULL));
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Solution boundary integral: %.4g\n", (double)PetscAbsScalar(bdInt)));
    PetscCheck(PetscAbsReal(PetscAbsScalar(bdInt) - exact) <= PETSC_SQRT_MACHINE_EPSILON, PETSC_COMM_WORLD, PETSC_ERR_PLIB, "Invalid boundary integral %g != %g", (double)PetscAbsScalar(bdInt), (double)exact);
  }

  PetscCall(MatNullSpaceDestroy(&nullSpace));
  if (user.jacobianMF) PetscCall(VecDestroy(&userJ.u));
  if (A != J) PetscCall(MatDestroy(&A));
  PetscCall(MatDestroy(&J));
  PetscCall(VecDestroy(&u));
  PetscCall(SNESDestroy(&snes));
  PetscCall(DMDestroy(&dm));
  PetscCall(PetscFree2(user.exactFuncs, user.exactFields));
  PetscCall(PetscFree(user.kgrid));
  PetscCall(PetscFinalize());
  return 0;
}

/*TEST
  # 2D serial P1 test 0-4
  test:
    suffix: 2d_p1_0
    requires: triangle
    args: -run_type test -bc_type dirichlet -dm_plex_interpolate 0 -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 2d_p1_1
    requires: triangle
    args: -run_type test -bc_type dirichlet -petscspace_degree 1 -show_initial -dm_plex_print_fem 1 -cdm_dm_plex_coordinate_dim {{2 3}}

  test:
    suffix: 2d_p1_1b
    requires: triangle
    args: -run_type test -bc_type dirichlet -petscspace_degree 1 -show_initial -dm_plex_print_fem 1 -dm_refine 3 -dm_coord_space 0 \
          -dm_plex_option_phases proj_ -cdm_proj_dm_plex_coordinate_dim 3 -proj_dm_coord_space \
          -proj_dm_coord_remap -proj_dm_coord_map sinusoid -proj_dm_coord_map_params 0.1,1.,1.

  test:
    suffix: 2d_p1_2
    requires: triangle
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -bc_type dirichlet -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 2d_p1_neumann_0
    requires: triangle
    args: -dm_coord_space 0 -run_type test -bc_type neumann -dm_plex_boundary_label boundary -petscspace_degree 1 -show_initial -dm_plex_print_fem 1 -dm_view ascii::ascii_info_detail

  test:
    suffix: 2d_p1_neumann_1
    requires: triangle
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -bc_type neumann -dm_plex_boundary_label boundary -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  # 2D serial P2 test 5-8
  test:
    suffix: 2d_p2_0
    requires: triangle
    args: -run_type test -bc_type dirichlet -petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 2d_p2_1
    requires: triangle
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -bc_type dirichlet -petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 2d_p2_neumann_0
    requires: triangle
    args: -dm_coord_space 0 -run_type test -bc_type neumann -dm_plex_boundary_label boundary -petscspace_degree 2 -show_initial -dm_plex_print_fem 1 -dm_view ascii::ascii_info_detail

  test:
    suffix: 2d_p2_neumann_1
    requires: triangle
    args: -dm_coord_space 0 -run_type test -dm_refine_volume_limit_pre 0.0625 -bc_type neumann -dm_plex_boundary_label boundary -petscspace_degree 2 -show_initial -dm_plex_print_fem 1 -dm_view ascii::ascii_info_detail

  test:
    suffix: bd_int_0
    requires: triangle
    args: -run_type test -bc_type dirichlet -petscspace_degree 2 -bd_integral -dm_view -quiet

  test:
    suffix: bd_int_1
    requires: triangle
    args: -run_type test -dm_refine 2 -bc_type dirichlet -petscspace_degree 2 -bd_integral -dm_view -quiet

  # 3D serial P1 test 9-12
  test:
    suffix: 3d_p1_0
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -bc_type dirichlet -dm_plex_interpolate 0 -petscspace_degree 1 -show_initial -dm_plex_print_fem 1 -dm_view

  test:
    suffix: 3d_p1_1
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -bc_type dirichlet -petscspace_degree 1 -show_initial -dm_plex_print_fem 1 -dm_view

  test:
    suffix: 3d_p1_2
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine_volume_limit_pre 0.0125 -bc_type dirichlet -petscspace_degree 1 -show_initial -dm_plex_print_fem 1 -dm_view

  test:
    suffix: 3d_p1_neumann_0
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -bc_type neumann -dm_plex_boundary_label boundary -petscspace_degree 1 -snes_fd -show_initial -dm_plex_print_fem 1 -dm_view

  # Analytic variable coefficient 13-20
  test:
    suffix: 13
    requires: triangle
    args: -run_type test -variable_coefficient analytic -petscspace_degree 1 -show_initial -dm_plex_print_fem 1
  test:
    suffix: 14
    requires: triangle
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -variable_coefficient analytic -petscspace_degree 1 -show_initial -dm_plex_print_fem 1
  test:
    suffix: 15
    requires: triangle
    args: -run_type test -variable_coefficient analytic -petscspace_degree 2 -show_initial -dm_plex_print_fem 1
  test:
    suffix: 16
    requires: triangle
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -variable_coefficient analytic -petscspace_degree 2 -show_initial -dm_plex_print_fem 1
  test:
    suffix: 17
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -variable_coefficient analytic -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 18
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine_volume_limit_pre 0.0125 -variable_coefficient analytic -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 19
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -variable_coefficient analytic -petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 20
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine_volume_limit_pre 0.0125 -variable_coefficient analytic -petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  # P1 variable coefficient 21-28
  test:
    suffix: 21
    requires: triangle
    args: -run_type test -variable_coefficient field -petscspace_degree 1 -mat_petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 22
    requires: triangle
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -variable_coefficient field -petscspace_degree 1 -mat_petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 23
    requires: triangle
    args: -run_type test -variable_coefficient field -petscspace_degree 2 -mat_petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 24
    requires: triangle
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -variable_coefficient field -petscspace_degree 2 -mat_petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 25
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -variable_coefficient field -petscspace_degree 1 -mat_petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 26
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine_volume_limit_pre 0.0125 -variable_coefficient field -petscspace_degree 1 -mat_petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 27
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -variable_coefficient field -petscspace_degree 2 -mat_petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 28
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine_volume_limit_pre 0.0125 -variable_coefficient field -petscspace_degree 2 -mat_petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  # P0 variable coefficient 29-36
  test:
    suffix: 29
    requires: triangle
    args: -run_type test -variable_coefficient field -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 30
    requires: triangle
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -variable_coefficient field -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 31
    requires: triangle
    args: -run_type test -variable_coefficient field -petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    requires: triangle
    suffix: 32
    args: -run_type test -dm_refine_volume_limit_pre 0.0625 -variable_coefficient field -petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    requires: ctetgen
    suffix: 33
    args: -run_type test -dm_plex_dim 3 -variable_coefficient field -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 34
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine_volume_limit_pre 0.0125 -variable_coefficient field -petscspace_degree 1 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 35
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -variable_coefficient field -petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: 36
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine_volume_limit_pre 0.0125 -variable_coefficient field -petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  # Full solve 39-44
  test:
    suffix: 39
    requires: triangle !single
    args: -run_type full -dm_refine_volume_limit_pre 0.015625 -petscspace_degree 2 -pc_type gamg -pc_gamg_esteig_ksp_type cg -pc_gamg_esteig_ksp_max_it 10 -snes_rtol 1.0e-6 -ksp_rtol 1.0e-7 -ksp_monitor -ksp_converged_reason -snes_monitor_short -snes_converged_reason ::ascii_info_detail
  test:
    suffix: 40
    requires: triangle !single
    args: -run_type full -dm_refine_volume_limit_pre 0.015625 -variable_coefficient nonlinear -petscspace_degree 2 -pc_type svd -ksp_rtol 1.0e-10 -snes_monitor_short -snes_converged_reason ::ascii_info_detail
  test:
    suffix: 41
    requires: triangle !single
    args: -run_type full -dm_refine_volume_limit_pre 0.03125 -variable_coefficient nonlinear -petscspace_degree 1 -snes_type fas -snes_fas_levels 2 -fas_coarse_pc_type svd -fas_coarse_ksp_rtol 1.0e-10 -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -dm_refine_hierarchy 1 -snes_view -fas_levels_1_snes_type newtonls -fas_levels_1_pc_type svd -fas_levels_1_ksp_rtol 1.0e-10 -fas_levels_1_snes_monitor_short
  test:
    suffix: 42
    requires: triangle !single
    args: -run_type full -dm_refine_volume_limit_pre 0.0625 -variable_coefficient nonlinear -petscspace_degree 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type svd -fas_coarse_ksp_rtol 1.0e-10 -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -dm_refine_hierarchy 2 -snes_view -fas_levels_1_snes_type newtonls -fas_levels_1_pc_type svd -fas_levels_1_ksp_rtol 1.0e-10 -fas_levels_1_snes_monitor_short -fas_levels_2_snes_type newtonls -fas_levels_2_pc_type svd -fas_levels_2_ksp_rtol 1.0e-10 -fas_levels_2_snes_atol 1.0e-11 -fas_levels_2_snes_monitor_short
  test:
    suffix: 43
    requires: triangle !single
    nsize: 2
    args: -run_type full -dm_refine_volume_limit_pre 0.03125 -variable_coefficient nonlinear -petscspace_degree 1 -snes_type fas -snes_fas_levels 2 -fas_coarse_pc_type svd -fas_coarse_ksp_rtol 1.0e-10 -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -dm_refine_hierarchy 1 -snes_view -fas_levels_1_snes_type newtonls -fas_levels_1_pc_type svd -fas_levels_1_ksp_rtol 1.0e-10 -fas_levels_1_snes_monitor_short

  test:
    suffix: 44
    requires: triangle !single
    nsize: 2
    args: -run_type full -dm_refine_volume_limit_pre 0.0625 -variable_coefficient nonlinear -petscspace_degree 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type svd -fas_coarse_ksp_rtol 1.0e-10 -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -dm_refine_hierarchy 2 -dm_plex_print_fem 0 -snes_view -fas_levels_1_snes_type newtonls -fas_levels_1_pc_type svd -fas_levels_1_ksp_rtol 1.0e-10 -fas_levels_1_snes_monitor_short -fas_levels_2_snes_type newtonls -fas_levels_2_pc_type svd -fas_levels_2_ksp_rtol 1.0e-10 -fas_levels_2_snes_atol 1.0e-11 -fas_levels_2_snes_monitor_short

  # These tests use a loose tolerance just to exercise the PtAP operations for MATIS and multiple PCBDDC setup calls inside PCMG
  testset:
    requires: triangle !single
    nsize: 3
    args: -run_type full -petscspace_degree 1 -dm_mat_type is -pc_type mg -mg_coarse_pc_type bddc -pc_mg_galerkin pmat -ksp_rtol 1.0e-2 -snes_converged_reason -dm_refine_hierarchy 2 -snes_max_it 4
    test:
      suffix: gmg_bddc
      filter: sed -e "s/CONVERGED_FNORM_RELATIVE iterations 3/CONVERGED_FNORM_RELATIVE iterations 4/g"
      args: -mg_levels_pc_type jacobi
    test:
      filter: sed -e "s/iterations [0-4]/iterations 4/g"
      suffix: gmg_bddc_lev
      args: -mg_levels_pc_type bddc

  # VTU viewer with empty processes
  test:
    requires: !complex
    suffix: vtu_empty
    args: -quiet -run_type test -dm_plex_simplex 0 -dm_plex_box_faces 2,2 -vec_view vtk:test.vtu:vtk_vtu -petscspace_degree 1 -petscpartitioner_type simple

  # Restarting
  testset:
    suffix: restart
    requires: hdf5 triangle !complex
    args: -run_type test -bc_type dirichlet -petscspace_degree 1
    test:
      args: -dm_view hdf5:sol.h5 -vec_view hdf5:sol.h5::append
    test:
      args: -dm_plex_filename sol.h5 -dm_plex_name box -restart

  # Periodicity
  test:
    suffix: periodic_0
    requires: triangle
    args: -run_type full -bc_type dirichlet -petscspace_degree 1 -snes_converged_reason ::ascii_info_detail

  test:
    requires: !complex
    suffix: periodic_1
    args: -quiet -run_type test -dm_plex_simplex 0 -dm_plex_box_faces 3,3 -dm_plex_box_bd periodic,periodic -vec_view vtk:test.vtu:vtk_vtu -petscspace_degree 1 -dm_refine 1

  # 2D serial P1 test with field bc
  test:
    suffix: field_bc_2d_p1_0
    requires: triangle
    args: -run_type test -bc_type dirichlet -field_bc -petscspace_degree 1 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_2d_p1_1
    requires: triangle
    args: -run_type test -dm_refine 1 -bc_type dirichlet -field_bc -petscspace_degree 1 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_2d_p1_neumann_0
    requires: triangle
    args: -run_type test -bc_type neumann -dm_plex_boundary_label boundary -field_bc -petscspace_degree 1 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_2d_p1_neumann_1
    requires: triangle
    args: -run_type test -dm_refine 1 -bc_type neumann -dm_plex_boundary_label boundary -field_bc -petscspace_degree 1 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  # 3D serial P1 test with field bc
  test:
    suffix: field_bc_3d_p1_0
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -bc_type dirichlet -field_bc -petscspace_degree 1 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_3d_p1_1
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine 1 -bc_type dirichlet -field_bc -petscspace_degree 1 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_3d_p1_neumann_0
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -bc_type neumann -dm_plex_boundary_label boundary -field_bc -petscspace_degree 1 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_3d_p1_neumann_1
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine 1 -bc_type neumann -dm_plex_boundary_label boundary -field_bc -petscspace_degree 1 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  # 2D serial P2 test with field bc
  test:
    suffix: field_bc_2d_p2_0
    requires: triangle
    args: -run_type test -bc_type dirichlet -field_bc -petscspace_degree 2 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_2d_p2_1
    requires: triangle
    args: -run_type test -dm_refine 1 -bc_type dirichlet -field_bc -petscspace_degree 2 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_2d_p2_neumann_0
    requires: triangle
    args: -run_type test -bc_type neumann -dm_plex_boundary_label boundary -field_bc -petscspace_degree 2 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_2d_p2_neumann_1
    requires: triangle
    args: -run_type test -dm_refine 1 -bc_type neumann -dm_plex_boundary_label boundary -field_bc -petscspace_degree 2 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  # 3D serial P2 test with field bc
  test:
    suffix: field_bc_3d_p2_0
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -bc_type dirichlet -field_bc -petscspace_degree 2 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_3d_p2_1
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine 1 -bc_type dirichlet -field_bc -petscspace_degree 2 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_3d_p2_neumann_0
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -bc_type neumann -dm_plex_boundary_label boundary -field_bc -petscspace_degree 2 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  test:
    suffix: field_bc_3d_p2_neumann_1
    requires: ctetgen
    args: -run_type test -dm_plex_dim 3 -dm_refine 1 -bc_type neumann -dm_plex_boundary_label boundary -field_bc -petscspace_degree 2 -bc_petscspace_degree 2 -show_initial -dm_plex_print_fem 1

  # Full solve simplex: Convergence
  test:
    suffix: 3d_p1_conv
    requires: ctetgen
    args: -run_type full -dm_plex_dim 3 -dm_refine 1 -bc_type dirichlet -petscspace_degree 1 \
      -snes_convergence_estimate -convest_num_refine 1 -pc_type lu

  # Full solve simplex: PCBDDC
  test:
    suffix: tri_bddc
    requires: triangle !single
    nsize: 5
    args: -run_type full -petscpartitioner_type simple -dm_refine 2 -bc_type dirichlet -petscspace_degree 1 -ksp_type gmres -ksp_gmres_restart 100 -ksp_rtol 1.0e-9 -dm_mat_type is -pc_type bddc -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0

  # Full solve simplex: PCBDDC
  test:
    suffix: tri_parmetis_bddc
    requires: triangle !single parmetis
    nsize: 4
    args: -run_type full -petscpartitioner_type parmetis -dm_refine 2 -bc_type dirichlet -petscspace_degree 1 -ksp_type gmres -ksp_gmres_restart 100 -ksp_rtol 1.0e-9 -dm_mat_type is -pc_type bddc -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0

  testset:
    args: -run_type full -dm_plex_simplex 0 -dm_plex_box_faces 3,3 -petscpartitioner_type simple -dm_refine 2 -bc_type dirichlet -petscspace_degree 2 -dm_mat_type is -pc_type bddc -ksp_type gmres -snes_monitor_short -ksp_monitor_short -snes_view -petscspace_poly_tensor -pc_bddc_corner_selection -ksp_rtol 1.e-9 -pc_bddc_use_edges 0
    nsize: 5
    output_file: output/ex12_quad_bddc.out
    filter: sed -e "s/aijcusparse/aij/g" -e "s/aijviennacl/aij/g" -e "s/factorization: cusparse/factorization: petsc/g"
    test:
      requires: !single
      suffix: quad_bddc
    test:
      requires: !single cuda
      suffix: quad_bddc_cuda
      args: -mat_is_localmat_type aijcusparse -pc_bddc_dirichlet_pc_factor_mat_solver_type cusparse -pc_bddc_neumann_pc_factor_mat_solver_type cusparse
    test:
      requires: !single viennacl
      suffix: quad_bddc_viennacl
      args: -mat_is_localmat_type aijviennacl

  # Full solve simplex: ASM
  test:
    suffix: tri_q2q1_asm_lu
    requires: triangle !single
    args: -run_type full -dm_refine 3 -bc_type dirichlet -petscspace_degree 1 -ksp_type gmres -ksp_gmres_restart 100 -ksp_rtol 1.0e-9 -pc_type asm -pc_asm_type restrict -pc_asm_blocks 4 -sub_pc_type lu -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0

  test:
    suffix: tri_q2q1_msm_lu
    requires: triangle !single
    args: -run_type full -dm_refine 3 -bc_type dirichlet -petscspace_degree 1 -ksp_type gmres -ksp_gmres_restart 100 -ksp_rtol 1.0e-9 -pc_type asm -pc_asm_type restrict -pc_asm_local_type multiplicative -pc_asm_blocks 4 -sub_pc_type lu -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0

  test:
    suffix: tri_q2q1_asm_sor
    requires: triangle !single
    args: -run_type full -dm_refine 3 -bc_type dirichlet -petscspace_degree 1 -ksp_type gmres -ksp_gmres_restart 100 -ksp_rtol 1.0e-9 -pc_type asm -pc_asm_type restrict -pc_asm_blocks 4 -sub_pc_type sor -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0

  test:
    suffix: tri_q2q1_msm_sor
    requires: triangle !single
    args: -run_type full -dm_refine 3 -bc_type dirichlet -petscspace_degree 1 -ksp_type gmres -ksp_gmres_restart 100 -ksp_rtol 1.0e-9 -pc_type asm -pc_asm_type restrict -pc_asm_local_type multiplicative -pc_asm_blocks 4 -sub_pc_type sor -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0

  # Full solve simplex: FAS
  test:
    suffix: fas_newton_0
    requires: triangle !single
    args: -run_type full -variable_coefficient nonlinear -petscspace_degree 1 -snes_type fas -snes_fas_levels 2 -fas_coarse_pc_type svd -fas_coarse_ksp_rtol 1.0e-10 -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -dm_refine_hierarchy 1 -snes_view -fas_levels_1_snes_type newtonls -fas_levels_1_pc_type svd -fas_levels_1_ksp_rtol 1.0e-10 -fas_levels_1_snes_monitor_short

  test:
    suffix: fas_newton_1
    requires: triangle !single
    args: -run_type full -dm_refine_hierarchy 3 -petscspace_degree 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type lu -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_snes_linesearch_type basic -fas_levels_ksp_rtol 1.0e-10 -fas_levels_snes_monitor_short
    filter: sed -e "s/total number of linear solver iterations=14/total number of linear solver iterations=15/g"

  test:
    suffix: fas_ngs_0
    requires: triangle !single
    args: -run_type full -variable_coefficient nonlinear -petscspace_degree 1 -snes_type fas -snes_fas_levels 2 -fas_coarse_pc_type svd -fas_coarse_ksp_rtol 1.0e-10 -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -dm_refine_hierarchy 1 -snes_view -fas_levels_1_snes_type ngs -fas_levels_1_snes_monitor_short

  # These two tests are broken because DMPlexComputeInjectorFEM() only works for regularly refined meshes
  test:
    suffix: fas_newton_coarse_0
    requires: pragmatic triangle
    TODO: broken
    args: -run_type full -variable_coefficient nonlinear -petscspace_degree 1 \
          -dm_refine 2 -dm_coarsen_hierarchy 1 -dm_plex_hash_location -dm_adaptor pragmatic \
          -snes_type fas -snes_fas_levels 2 -snes_converged_reason ::ascii_info_detail -snes_monitor_short -snes_view \
            -fas_coarse_pc_type svd -fas_coarse_ksp_rtol 1.0e-10 -fas_coarse_snes_monitor_short -fas_coarse_snes_linesearch_type basic \
            -fas_levels_1_snes_type newtonls -fas_levels_1_pc_type svd -fas_levels_1_ksp_rtol 1.0e-10 -fas_levels_1_snes_monitor_short

  test:
    suffix: mg_newton_coarse_0
    requires: triangle pragmatic
    TODO: broken
    args: -run_type full -petscspace_degree 1 \
          -dm_refine 3 -dm_coarsen_hierarchy 3 -dm_plex_hash_location -dm_adaptor pragmatic \
          -snes_atol 1.0e-8 -snes_rtol 0.0 -snes_monitor_short -snes_converged_reason ::ascii_info_detail -snes_view \
            -ksp_type richardson -ksp_atol 1.0e-8 -ksp_rtol 0.0 -ksp_norm_type unpreconditioned -ksp_monitor_true_residual \
              -pc_type mg -pc_mg_levels 4 \
              -mg_levels_ksp_type gmres -mg_levels_pc_type ilu -mg_levels_ksp_max_it 10

  # Test cgns writer for ranks with no elements
  test:
    suffix: cgns
    nsize: 5
    requires: cgns
    args: -quiet -run_type test -dm_plex_simplex 0 -petscspace_degree 1 -dm_plex_box_faces 2,2 -vec_view cgns:test.cgns -dm_refine 0 -petscpartitioner_type simple

  # Full solve tensor
  test:
    suffix: tensor_plex_2d
    args: -run_type test -dm_plex_simplex 0 -bc_type dirichlet -petscspace_degree 1 -dm_refine_hierarchy 2

  test:
    suffix: tensor_p4est_2d
    requires: p4est
    args: -run_type test -dm_plex_simplex 0 -bc_type dirichlet -petscspace_degree 1 -dm_forest_initial_refinement 2 -dm_forest_minimum_refinement 0 -dm_plex_convert_type p4est

  test:
    suffix: tensor_plex_3d
    args: -run_type test -dm_plex_simplex 0 -bc_type dirichlet -petscspace_degree 1 -dm_plex_dim 3 -dm_refine_hierarchy 1 -dm_plex_box_faces 2,2,2

  test:
    suffix: tensor_p4est_3d
    requires: p4est
    args: -run_type test -dm_plex_simplex 0 -bc_type dirichlet -petscspace_degree 1 -dm_forest_initial_refinement 1 -dm_forest_minimum_refinement 0 -dm_plex_dim 3 -dm_plex_convert_type p8est -dm_plex_box_faces 2,2,2

  test:
    suffix: p4est_test_q2_conformal_serial
    requires: p4est
    args: -run_type test -petscspace_degree 2 -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2

  test:
    suffix: p4est_test_q2_conformal_parallel
    requires: p4est
    nsize: 7
    args: -run_type test -petscspace_degree 2 -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -petscpartitioner_type simple

  test:
    suffix: p4est_test_q2_conformal_parallel_parmetis
    requires: parmetis p4est
    nsize: 4
    args: -run_type test -petscspace_degree 2 -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -petscpartitioner_type parmetis

  test:
    suffix: p4est_test_q2_nonconformal_serial
    requires: p4est
    filter: grep -v "CG or CGNE: variant"
    args: -run_type test -petscspace_degree 2 -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash

  test:
    suffix: p4est_test_q2_nonconformal_parallel
    requires: p4est
    filter: grep -v "CG or CGNE: variant"
    nsize: 7
    args: -run_type test -petscspace_degree 2 -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -petscpartitioner_type simple

  test:
    suffix: p4est_test_q2_nonconformal_parallel_parmetis
    requires: parmetis p4est
    nsize: 4
    args: -run_type test -petscspace_degree 2 -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -petscpartitioner_type parmetis

  test:
    suffix: p4est_exact_q2_conformal_serial
    requires: p4est !single !complex !__float128
    args: -run_type exact -petscspace_degree 2 -fas_levels_snes_atol 1.e-10 -snes_max_it 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type none -fas_coarse_ksp_type preonly -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type none -fas_levels_ksp_type preonly -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2

  test:
    suffix: p4est_exact_q2_conformal_parallel
    requires: p4est !single !complex !__float128
    nsize: 4
    args: -run_type exact -petscspace_degree 2 -fas_levels_snes_atol 1.e-10 -snes_max_it 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type none -fas_coarse_ksp_type preonly -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type none -fas_levels_ksp_type preonly -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2

  test:
    suffix: p4est_exact_q2_conformal_parallel_parmetis
    requires: parmetis p4est !single
    nsize: 4
    args: -run_type exact -petscspace_degree 2 -fas_levels_snes_linesearch_type basic -fas_levels_snes_atol 1.e-10 -snes_max_it 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_snes_converged_reason -fas_coarse_pc_type none -fas_coarse_ksp_type preonly -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type none -fas_levels_ksp_type preonly -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -petscpartitioner_type parmetis

  test:
    suffix: p4est_exact_q2_nonconformal_serial
    requires: p4est
    args: -run_type exact -petscspace_degree 2 -fas_levels_snes_atol 1.e-10 -snes_max_it 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type none -fas_coarse_ksp_type preonly -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type none -fas_levels_ksp_type preonly -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash

  test:
    suffix: p4est_exact_q2_nonconformal_parallel
    requires: p4est
    nsize: 7
    args: -run_type exact -petscspace_degree 2 -fas_levels_snes_atol 1.e-10 -snes_max_it 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type none -fas_coarse_ksp_type preonly -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type none -fas_levels_ksp_type preonly -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -petscpartitioner_type simple

  test:
    suffix: p4est_exact_q2_nonconformal_parallel_parmetis
    requires: parmetis p4est
    nsize: 4
    args: -run_type exact -petscspace_degree 2 -fas_levels_snes_atol 1.e-10 -snes_max_it 1 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type none -fas_coarse_ksp_type preonly -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type none -fas_levels_ksp_type preonly -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -petscpartitioner_type parmetis

  test:
    suffix: p4est_full_q2_nonconformal_serial
    requires: p4est !single
    filter: grep -v "variant HERMITIAN"
    args: -run_type full -petscspace_degree 2 -snes_max_it 20 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type jacobi -fas_coarse_ksp_type cg -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type jacobi -fas_levels_ksp_type cg -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash

  test:
    suffix: p4est_full_q2_nonconformal_parallel
    requires: p4est !single
    filter: grep -v "variant HERMITIAN"
    nsize: 7
    args: -run_type full -petscspace_degree 2 -snes_max_it 20 -snes_type fas -snes_fas_levels 3 -fas_coarse_pc_type jacobi -fas_coarse_ksp_type cg -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type jacobi -fas_levels_ksp_type cg -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -petscpartitioner_type simple

  test:
    suffix: p4est_full_q2_nonconformal_parallel_bddcfas
    requires: p4est !single
    filter: grep -v "variant HERMITIAN"
    nsize: 7
    args: -run_type full -petscspace_degree 2 -snes_max_it 20 -snes_type fas -snes_fas_levels 3 -dm_mat_type is -fas_coarse_pc_type bddc -fas_coarse_ksp_type cg -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type bddc -fas_levels_ksp_type cg -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -petscpartitioner_type simple

  test:
    suffix: p4est_full_q2_nonconformal_parallel_bddc
    requires: p4est !single
    filter: grep -v "variant HERMITIAN"
    nsize: 7
    args: -run_type full -petscspace_degree 2 -snes_max_it 20 -snes_type newtonls -dm_mat_type is -pc_type bddc -ksp_type cg -snes_monitor_short -snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -petscpartitioner_type simple

  test:
    TODO: broken
    suffix: p4est_fas_q2_conformal_serial
    requires: p4est !complex !__float128
    args: -run_type full -variable_coefficient nonlinear -petscspace_degree 2 -snes_max_it 20 -snes_type fas -snes_fas_levels 3 -pc_type jacobi -ksp_type gmres -fas_coarse_pc_type svd -fas_coarse_ksp_type gmres -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type svd -fas_levels_ksp_type gmres -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_refine_hierarchy 3

  test:
    TODO: broken
    suffix: p4est_fas_q2_nonconformal_serial
    requires: p4est
    args: -run_type full -variable_coefficient nonlinear -petscspace_degree 2 -snes_max_it 20 -snes_type fas -snes_fas_levels 3 -pc_type jacobi -ksp_type gmres -fas_coarse_pc_type jacobi -fas_coarse_ksp_type gmres -fas_coarse_ksp_monitor_true_residual -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_snes_type newtonls -fas_levels_pc_type jacobi -fas_levels_ksp_type gmres -fas_levels_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash

  test:
    suffix: fas_newton_0_p4est
    requires: p4est !single !__float128
    args: -run_type full -variable_coefficient nonlinear -petscspace_degree 1 -snes_type fas -snes_fas_levels 2 -fas_coarse_pc_type svd -fas_coarse_ksp_rtol 1.0e-10 -fas_coarse_snes_monitor_short -snes_monitor_short -fas_coarse_snes_linesearch_type basic -snes_converged_reason ::ascii_info_detail -snes_view -fas_levels_1_snes_type newtonls -fas_levels_1_pc_type svd -fas_levels_1_ksp_rtol 1.0e-10 -fas_levels_1_snes_monitor_short -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash

  # Full solve simplicial AMR
  test:
    suffix: tri_p1_adapt_init_pragmatic
    requires: pragmatic
    args: -run_type exact -dm_refine 5 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -snes_adapt_initial 1 -adaptor_target_num 4000 -dm_plex_metric_h_max 0.5 -dm_adaptor pragmatic

  test:
    suffix: tri_p2_adapt_init_pragmatic
    requires: pragmatic
    args: -run_type exact -dm_refine 5 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -snes_adapt_initial 1 -adaptor_target_num 4000 -dm_plex_metric_h_max 0.5 -dm_adaptor pragmatic

  test:
    suffix: tri_p1_adapt_init_mmg
    requires: mmg
    args: -run_type exact -dm_refine 5 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -snes_adapt_initial 1 -adaptor_target_num 4000 -dm_plex_metric_h_max 0.5 -dm_adaptor mmg

  test:
    suffix: tri_p2_adapt_init_mmg
    requires: mmg
    args: -run_type exact -dm_refine 5 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -snes_adapt_initial 1 -adaptor_target_num 4000 -dm_plex_metric_h_max 0.5 -dm_adaptor mmg

  test:
    suffix: tri_p1_adapt_seq_pragmatic
    requires: pragmatic
    args: -run_type exact -dm_refine 5 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -snes_adapt_sequence 2 -adaptor_target_num 4000 -dm_plex_metric_h_max 0.5 -dm_adaptor pragmatic

  test:
    suffix: tri_p2_adapt_seq_pragmatic
    requires: pragmatic
    args: -run_type exact -dm_refine 5 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -snes_adapt_sequence 2 -adaptor_target_num 4000 -dm_plex_metric_h_max 0.5 -dm_adaptor pragmatic

  test:
    suffix: tri_p1_adapt_seq_mmg
    requires: mmg
    args: -run_type exact -dm_refine 5 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -snes_adapt_sequence 2 -adaptor_target_num 4000 -dm_plex_metric_h_max 0.5 -dm_adaptor mmg

  test:
    suffix: tri_p2_adapt_seq_mmg
    requires: mmg
    args: -run_type exact -dm_refine 5 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -snes_adapt_sequence 2 -adaptor_target_num 4000 -dm_plex_metric_h_max 0.5 -dm_adaptor mmg

  test:
    suffix: tri_p1_adapt_analytic_pragmatic
    requires: pragmatic
    args: -run_type exact -dm_refine 3 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient cross -snes_adapt_initial 4 -adaptor_target_num 500 -dm_plex_metric_h_min 0.0001 -dm_plex_metric_h_max 0.05 -dm_adaptor pragmatic
    output_file: output/empty.out

  test:
    suffix: tri_p2_adapt_analytic_pragmatic
    requires: pragmatic
    args: -run_type exact -dm_refine 3 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient cross -snes_adapt_initial 4 -adaptor_target_num 500 -dm_plex_metric_h_min 0.0001 -dm_plex_metric_h_max 0.05 -dm_adaptor pragmatic
    output_file: output/empty.out

  test:
    suffix: tri_p1_adapt_analytic_mmg
    requires: mmg
    args: -run_type exact -dm_refine 3 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient cross -snes_adapt_initial 4 -adaptor_target_num 500 -dm_plex_metric_h_max 0.5 -dm_adaptor mmg
    output_file: output/empty.out

  test:
    suffix: tri_p2_adapt_analytic_mmg
    requires: mmg
    args: -run_type exact -dm_refine 3 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient cross -snes_adapt_initial 4 -adaptor_target_num 500 -dm_plex_metric_h_max 0.5 -dm_adaptor mmg
    output_file: output/empty.out

  test:
    suffix: tri_p1_adapt_uniform_pragmatic
    requires: pragmatic tetgen
    nsize: 2
    args: -run_type full -dm_plex_box_faces 8,8,8 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient none -snes_converged_reason ::ascii_info_detail -ksp_type cg -pc_type sor -snes_adapt_sequence 3 -adaptor_target_num 400 -dm_plex_metric_h_max 0.5 -dm_plex_dim 3 -dm_adaptor pragmatic
    timeoutfactor: 2

  test:
    suffix: tri_p2_adapt_uniform_pragmatic
    requires: pragmatic tetgen
    nsize: 2
    args: -run_type full -dm_plex_box_faces 8,8,8 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient none -snes_converged_reason ::ascii_info_detail -ksp_type cg -pc_type sor -snes_adapt_sequence 1 -adaptor_target_num 400 -dm_plex_metric_h_max 0.5 -dm_plex_dim 3 -dm_adaptor pragmatic
    timeoutfactor: 1

  test:
    suffix: tri_p1_adapt_uniform_mmg
    requires: mmg tetgen
    args: -run_type full -dm_plex_box_faces 4,4,4 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient none -snes_converged_reason ::ascii_info_detail -ksp_type cg -pc_type sor -snes_adapt_sequence 3 -adaptor_target_num 400 -dm_plex_metric_h_max 0.5 -dm_plex_dim 3 -dm_adaptor mmg
    timeoutfactor: 2

  test:
    suffix: tri_p2_adapt_uniform_mmg
    requires: mmg tetgen
    TODO: broken
    args: -run_type full -dm_plex_box_faces 4,4,4 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient none -snes_converged_reason ::ascii_info_detail -ksp_type cg -pc_type sor -snes_adapt_sequence 1 -adaptor_target_num 400 -dm_plex_metric_h_max 0.5 -dm_plex_dim 3 -dm_adaptor mmg
    timeoutfactor: 1

  test:
    suffix: tri_p1_adapt_uniform_parmmg
    requires: parmmg tetgen
    nsize: 2
    args: -run_type full -dm_plex_box_faces 8,8,8 -bc_type dirichlet -petscspace_degree 1 -variable_coefficient none -snes_converged_reason ::ascii_info_detail -ksp_type cg -pc_type sor -snes_adapt_sequence 3 -adaptor_target_num 400 -dm_plex_metric_h_max 0.5 -dm_plex_dim 3 -dm_adaptor parmmg
    timeoutfactor: 2

  test:
    suffix: tri_p2_adapt_uniform_parmmg
    requires: parmmg tetgen
    nsize: 2
    args: -run_type full -dm_plex_box_faces 8,8,8 -bc_type dirichlet -petscspace_degree 2 -variable_coefficient none -snes_converged_reason ::ascii_info_detail -ksp_type cg -pc_type sor -snes_adapt_sequence 1 -adaptor_target_num 400 -dm_plex_metric_h_max 0.5 -dm_plex_dim 3 -dm_adaptor parmmg
    timeoutfactor: 1

  # Full solve tensor AMR
  test:
    suffix: quad_q1_adapt_0
    requires: p4est
    args: -run_type exact -dm_plex_simplex 0 -dm_plex_convert_type p4est -bc_type dirichlet -petscspace_degree 1 -variable_coefficient ball -snes_converged_reason ::ascii_info_detail -pc_type lu -dm_forest_initial_refinement 4 -snes_adapt_initial 1 -dm_view
    filter: grep -v DM_

  test:
    suffix: amr_0
    nsize: 5
    args: -run_type test -petscpartitioner_type simple -dm_plex_simplex 0 -bc_type dirichlet -petscspace_degree 1 -dm_refine 1

  test:
    suffix: amr_1
    requires: p4est !complex
    args: -run_type test -dm_plex_simplex 0 -bc_type dirichlet -petscspace_degree 1 -dm_plex_convert_type p4est -dm_p4est_refine_pattern center -dm_forest_maximum_refinement 5 -dm_view vtk:amr.vtu:vtk_vtu -vec_view vtk:amr.vtu:vtk_vtu:append

  test:
    suffix: p4est_solve_bddc
    requires: p4est !complex
    args: -run_type full -variable_coefficient nonlinear -nonzero_initial_guess 1 -petscspace_degree 2 -snes_max_it 20 -snes_type newtonls -dm_mat_type is -pc_type bddc -ksp_type cg -snes_monitor_short -ksp_monitor -snes_linesearch_type bt -snes_converged_reason -snes_view -dm_plex_simplex 0 -petscspace_poly_tensor -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -petscpartitioner_type simple -pc_bddc_detect_disconnected
    nsize: 4

  test:
    suffix: p4est_solve_fas
    requires: p4est
    args: -run_type full -variable_coefficient nonlinear -nonzero_initial_guess 1 -petscspace_degree 2 -snes_max_it 10 -snes_type fas -snes_linesearch_type bt -snes_fas_levels 3 -fas_coarse_snes_type newtonls -fas_coarse_snes_linesearch_type basic -fas_coarse_ksp_type cg -fas_coarse_pc_type jacobi -fas_coarse_snes_monitor_short -fas_levels_snes_max_it 4 -fas_levels_snes_type newtonls -fas_levels_snes_linesearch_type bt -fas_levels_ksp_type cg -fas_levels_pc_type jacobi -fas_levels_snes_monitor_short -fas_levels_cycle_snes_linesearch_type bt -snes_monitor_short -snes_converged_reason -snes_view -dm_plex_simplex 0 -petscspace_poly_tensor -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash
    nsize: 4
    TODO: identical machine two runs produce slightly different solver trackers

  test:
    suffix: p4est_convergence_test_1
    requires: p4est
    args: -quiet -run_type test -petscspace_degree 1 -dm_plex_simplex 0 -petscspace_poly_tensor -dm_plex_convert_type p4est -dm_forest_minimum_refinement 2 -dm_forest_initial_refinement 2 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash
    nsize: 4

  # Serial tests with GLVis visualization
  test:
    suffix: glvis_2d_tet_p1
    args: -quiet -run_type test -bc_type dirichlet -petscspace_degree 1 -vec_view glvis: -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/square_periodic.msh -dm_plex_boundary_label marker -dm_plex_gmsh_periodic 0 -dm_coord_space 0
  test:
    suffix: glvis_2d_tet_p2
    args: -quiet -run_type test -bc_type dirichlet -petscspace_degree 2 -vec_view glvis: -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/square_periodic.msh -dm_plex_boundary_label marker -dm_plex_gmsh_periodic 0 -dm_coord_space 0
  test:
    suffix: glvis_2d_hex_p1
    args: -quiet -run_type test -bc_type dirichlet -petscspace_degree 1 -vec_view glvis: -dm_plex_simplex 0 -dm_refine 1 -dm_coord_space 0
  test:
    suffix: glvis_2d_hex_p2
    args: -quiet -run_type test -bc_type dirichlet -petscspace_degree 2 -vec_view glvis: -dm_plex_simplex 0 -dm_refine 1 -dm_coord_space 0
  test:
    suffix: glvis_2d_hex_p2_p4est
    requires: p4est
    args: -quiet -run_type test -bc_type dirichlet -petscspace_degree 2 -vec_view glvis: -dm_plex_simplex 0 -dm_plex_convert_type p4est -dm_forest_minimum_refinement 0 -dm_forest_initial_refinement 1 -dm_forest_maximum_refinement 4 -dm_p4est_refine_pattern hash -viewer_glvis_dm_plex_enable_ncmesh
  test:
    suffix: glvis_2d_tet_p0
    args: -run_type exact -guess_vec_view glvis: -nonzero_initial_guess 1 -dm_plex_filename ${wPETSC_DIR}/share/petsc/datafiles/meshes/square_periodic.msh -dm_plex_boundary_label marker -petscspace_degree 0 -dm_coord_space 0 -pc_type jacobi
  test:
    suffix: glvis_2d_hex_p0
    args: -run_type exact -guess_vec_view glvis: -nonzero_initial_guess 1 -dm_plex_box_faces 5,7 -dm_plex_simplex 0 -petscspace_degree 0 -dm_coord_space 0 -pc_type jacobi

  # PCHPDDM tests
  testset:
    nsize: 4
    requires: hpddm slepc !single defined(PETSC_HAVE_DYNAMIC_LIBRARIES) defined(PETSC_USE_SHARED_LIBRARIES)
    args: -run_type test -run_test_check_ksp -quiet -petscspace_degree 1 -petscpartitioner_type simple -bc_type none -dm_plex_simplex 0 -pc_type hpddm -pc_hpddm_levels_1_sub_pc_type lu -pc_hpddm_levels_1_eps_nev 2 -pc_hpddm_coarse_p 1 -pc_hpddm_coarse_pc_type svd -ksp_rtol 1.e-10 -pc_hpddm_levels_1_st_pc_factor_shift_type INBLOCKS -ksp_converged_reason
    test:
      suffix: quad_singular_hpddm
      args: -dm_plex_box_faces 6,7
    test:
      requires: p4est
      suffix: p4est_singular_2d_hpddm
      args: -dm_plex_convert_type p4est -dm_forest_minimum_refinement 1 -dm_forest_initial_refinement 3 -dm_forest_maximum_refinement 3
    test:
      requires: p4est
      suffix: p4est_nc_singular_2d_hpddm
      args: -dm_plex_convert_type p4est -dm_forest_minimum_refinement 1 -dm_forest_initial_refinement 1 -dm_forest_maximum_refinement 3 -dm_p4est_refine_pattern hash
  testset:
    nsize: 4
    requires: hpddm slepc triangle !single defined(PETSC_HAVE_DYNAMIC_LIBRARIES) defined(PETSC_USE_SHARED_LIBRARIES)
    args: -run_type full -petscpartitioner_type simple -dm_refine 2 -bc_type dirichlet -petscspace_degree 2 -ksp_type gmres -ksp_gmres_restart 100 -pc_type hpddm -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0 -pc_type hpddm -pc_hpddm_levels_1_sub_pc_type lu -pc_hpddm_levels_1_eps_nev 4 -pc_hpddm_coarse_p 2 -pc_hpddm_coarse_pc_type redundant -ksp_rtol 1.e-1
    test:
      args: -pc_hpddm_coarse_mat_type baij -options_left no
      suffix: tri_hpddm_reuse_baij
    test:
      requires: !complex
      suffix: tri_hpddm_reuse
  testset:
    nsize: 4
    requires: hpddm slepc !single defined(PETSC_HAVE_DYNAMIC_LIBRARIES) defined(PETSC_USE_SHARED_LIBRARIES)
    args: -run_type full -petscpartitioner_type simple -dm_plex_box_faces 7,5 -dm_refine 2 -dm_plex_simplex 0 -bc_type dirichlet -petscspace_degree 2 -ksp_type gmres -ksp_gmres_restart 100 -pc_type hpddm -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0 -pc_type hpddm -pc_hpddm_levels_1_sub_pc_type lu -pc_hpddm_levels_1_eps_nev 4 -pc_hpddm_coarse_p 2 -pc_hpddm_coarse_pc_type redundant -ksp_rtol 1.e-1
    test:
      args: -pc_hpddm_coarse_mat_type baij -options_left no
      suffix: quad_hpddm_reuse_baij
    test:
      requires: !complex
      suffix: quad_hpddm_reuse
  testset:
    nsize: 4
    requires: hpddm slepc !single defined(PETSC_HAVE_DYNAMIC_LIBRARIES) defined(PETSC_USE_SHARED_LIBRARIES)
    args: -run_type full -petscpartitioner_type simple -dm_plex_box_faces 7,5 -dm_refine 2 -dm_plex_simplex 0 -bc_type dirichlet -petscspace_degree 1 -ksp_type gmres -ksp_gmres_restart 100 -pc_type hpddm -snes_monitor_short -ksp_monitor_short -snes_converged_reason ::ascii_info_detail -ksp_converged_reason -snes_view -show_solution 0 -pc_type hpddm -pc_hpddm_levels_1_sub_pc_type lu -pc_hpddm_levels_1_eps_threshold_absolute 0.1 -pc_hpddm_coarse_p 2 -pc_hpddm_coarse_pc_type redundant -ksp_rtol 1.e-1
    test:
      args: -pc_hpddm_coarse_mat_type baij -options_left no
      suffix: quad_hpddm_reuse_threshold_baij
    test:
      requires: !complex
      suffix: quad_hpddm_reuse_threshold
  testset:
    nsize: 4
    requires: hpddm slepc parmetis !single defined(PETSC_HAVE_DYNAMIC_LIBRARIES) defined(PETSC_USE_SHARED_LIBRARIES)
    filter: sed -e "s/linear solver iterations=17/linear solver iterations=16/g"
    args: -run_type full -petscpartitioner_type parmetis -dm_refine 3 -bc_type dirichlet -petscspace_degree 1 -ksp_type gmres -ksp_gmres_restart 100 -pc_type hpddm -snes_monitor_short -snes_converged_reason ::ascii_info_detail -snes_view -show_solution 0 -pc_type hpddm -pc_hpddm_levels_1_sub_pc_type icc -pc_hpddm_levels_1_eps_nev 20 -pc_hpddm_coarse_p 2 -pc_hpddm_coarse_pc_type redundant -ksp_rtol 1.e-10 -dm_plex_filename ${PETSC_DIR}/share/petsc/datafiles/meshes/square_periodic.msh -dm_plex_boundary_label marker -pc_hpddm_levels_1_sub_pc_factor_levels 3 -variable_coefficient ball -dm_plex_gmsh_periodic 0 -fp_trap 0
    test:
      args: -pc_hpddm_coarse_mat_type baij -options_left no
      filter: grep -v "      total: nonzeros=" | grep -v "      rows=" | sed -e "s/total number of linear solver iterations=[1-2][4-7]/total number of linear solver iterations=16/g"
      suffix: tri_parmetis_hpddm_baij
    test:
      filter: grep -v "      total: nonzeros=" | grep -v "      rows=" | sed -e "s/total number of linear solver iterations=[1-2][4-7]/total number of linear solver iterations=16/g"
      requires: !complex
      suffix: tri_parmetis_hpddm

  # 2D serial P1 tests for adaptive MG
  test:
    suffix: 2d_p1_adaptmg_0
    requires: triangle
    args: -petscpartitioner_type simple -dm_refine_hierarchy 3 -dm_plex_box_faces 4,4 -bc_type dirichlet -petscspace_degree 1 \
          -variable_coefficient checkerboard_0 -mat_petscspace_degree 0 -div 16 -k 3 \
          -snes_max_it 1 -ksp_converged_reason \
          -ksp_rtol 1e-8 -pc_type mg
  test:
    suffix: 2d_p1_adaptmg_1
    requires: triangle bamg
    args: -petscpartitioner_type simple -dm_refine_hierarchy 3 -dm_plex_box_faces 4,4 -bc_type dirichlet -petscspace_degree 1 \
          -variable_coefficient checkerboard_0 -mat_petscspace_degree 0 -div 16 -k 3 \
          -snes_max_it 1 -ksp_converged_reason \
          -ksp_rtol 1e-8 -pc_type mg -pc_mg_galerkin -pc_mg_adapt_interp_coarse_space eigenvector -pc_mg_adapt_interp_n 1 \
            -pc_mg_mesp_ksp_type richardson -pc_mg_mesp_ksp_richardson_self_scale -pc_mg_mesp_ksp_max_it 100 -pc_mg_mesp_pc_type none
  test:
    suffix: 2d_p1_adaptmg_gdsw
    requires: triangle
    nsize: 4
    args: -petscpartitioner_type simple -dm_refine 3 -dm_plex_box_faces 4,4 -bc_type dirichlet -petscspace_degree 1 \
          -variable_coefficient checkerboard_0 -mat_petscspace_degree 0 -div 16 -k 3 \
          -snes_max_it 1 -ksp_converged_reason \
          -ksp_rtol 1e-8 -pc_type mg -pc_mg_galerkin -pc_mg_adapt_interp_coarse_space gdsw -pc_mg_levels 2 -mg_levels_pc_type asm -dm_mat_type {{aij is}}

  test:
    suffix: 2d_p1_adaptmg_agdsw
    requires: triangle mumps
    nsize: 4
    args: -petscpartitioner_type simple -dm_refine 3 -dm_plex_box_faces 4,4 -bc_type dirichlet -petscspace_degree 1 \
          -variable_coefficient checkerboard_0 -mat_petscspace_degree 0 -div 16 -k 3 \
          -snes_max_it 1 -ksp_converged_reason \
          -ksp_rtol 1e-8 -pc_type mg -pc_mg_galerkin -pc_mg_adapt_interp_coarse_space gdsw -pc_mg_levels 2 -mg_levels_pc_type asm -dm_mat_type is -mg_levels_gdsw_tolerance 0.1 -mg_levels_gdsw_pseudo_pc_type qr

  test:
    suffix: p4est_2d_asm
    requires: p4est
    nsize: 4
    args: -run_type test -run_test_check_ksp -quiet -petscspace_degree 1 -petscpartitioner_type simple -bc_type none -dm_plex_simplex 0 \
          -pc_type asm -ksp_converged_reason -dm_plex_convert_type p4est -dm_forest_minimum_refinement 1 -dm_forest_initial_refinement 3 -dm_forest_maximum_refinement 5 \
          -pc_asm_dm_subdomains -dm_p4est_refine_pattern hash -dm_plex_dd_overlap 1 -sub_pc_type lu

TEST*/
````

## SNES ex17.c

- Selected by: Tutorials by physics
- Rendered listing: <https://petsc.org/release/src/snes/tutorials/ex17.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/snes/tutorials/ex17.c>

````c
static char help[] = "Linear elasticity in 2d and 3d with finite elements.\n\
We solve the elasticity problem in a rectangular\n\
domain, using a parallel unstructured mesh (DMPLEX) to discretize it.\n\
This example supports automatic convergence estimation\n\
and eventually adaptivity.\n\n\n";

/*
  https://en.wikipedia.org/wiki/Linear_elasticity

  Converting elastic constants:
    lambda = E nu / ((1 + nu) (1 - 2 nu))
    mu     = E / (2 (1 + nu))
*/

#include <petscdmplex.h>
#include <petscsnes.h>
#include <petscds.h>
#include <petscbag.h>
#include <petscconvest.h>

typedef enum {
  SOL_VLAP_QUADRATIC,
  SOL_ELAS_QUADRATIC,
  SOL_VLAP_TRIG,
  SOL_ELAS_TRIG,
  SOL_ELAS_AXIAL_DISP,
  SOL_ELAS_UNIFORM_STRAIN,
  SOL_ELAS_GE,
  SOL_MASS_QUADRATIC,
  NUM_SOLUTION_TYPES
} SolutionType;
const char *solutionTypes[NUM_SOLUTION_TYPES + 1] = {"vlap_quad", "elas_quad", "vlap_trig", "elas_trig", "elas_axial_disp", "elas_uniform_strain", "elas_ge", "mass_quad", "unknown"};

typedef enum {
  DEFORM_NONE,
  DEFORM_SHEAR,
  DEFORM_STEP,
  NUM_DEFORM_TYPES
} DeformType;
const char *deformTypes[NUM_DEFORM_TYPES + 1] = {"none", "shear", "step", "unknown"};

typedef struct {
  PetscScalar mu;     /* shear modulus */
  PetscScalar lambda; /* Lame's first parameter */
  PetscScalar N;      /* Tension force on right wall */
} Parameter;

typedef struct {
  /* Domain and mesh definition */
  char       dmType[256]; /* DM type for the solve */
  DeformType deform;      /* Domain deformation type */
  /* Problem definition */
  SolutionType solType; /* Type of exact solution */
  PetscBag     bag;     /* Problem parameters */
  /* Solver definition */
  PetscBool useNearNullspace; /* Use the rigid body modes as a near nullspace for AMG */
} AppCtx;

static PetscErrorCode zero(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;
  for (d = 0; d < dim; ++d) u[d] = 0.0;
  return PETSC_SUCCESS;
}

static PetscErrorCode ge_shift(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;
  u[0] = 0.1;
  for (d = 1; d < dim; ++d) u[d] = 0.0;
  return PETSC_SUCCESS;
}

static PetscErrorCode quadratic_2d_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  u[0] = x[0] * x[0];
  u[1] = x[1] * x[1] - 2.0 * x[0] * x[1];
  return PETSC_SUCCESS;
}

static PetscErrorCode quadratic_3d_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  u[0] = x[0] * x[0];
  u[1] = x[1] * x[1] - 2.0 * x[0] * x[1];
  u[2] = x[2] * x[2] - 2.0 * x[1] * x[2];
  return PETSC_SUCCESS;
}

/*
  u = x^2
  v = y^2 - 2xy
  Delta <u,v> - f = <2, 2> - <2, 2>

  u = x^2
  v = y^2 - 2xy
  w = z^2 - 2yz
  Delta <u,v,w> - f = <2, 2, 2> - <2, 2, 2>
*/
static void f0_vlap_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) f0[d] += 2.0;
}

/*
  u = x^2
  v = y^2 - 2xy
  \varepsilon = / 2x     -y    \
                \ -y   2y - 2x /
  Tr(\varepsilon) = div u = 2y
  div \sigma = \partial_i \lambda \delta_{ij} \varepsilon_{kk} + \partial_i 2\mu\varepsilon_{ij}
    = \lambda \partial_j (2y) + 2\mu < 2-1, 2 >
    = \lambda < 0, 2 > + \mu < 2, 4 >

  u = x^2
  v = y^2 - 2xy
  w = z^2 - 2yz
  \varepsilon = / 2x     -y       0   \
                | -y   2y - 2x   -z   |
                \  0     -z    2z - 2y/
  Tr(\varepsilon) = div u = 2z
  div \sigma = \partial_i \lambda \delta_{ij} \varepsilon_{kk} + \partial_i 2\mu\varepsilon_{ij}
    = \lambda \partial_j (2z) + 2\mu < 2-1, 2-1, 2 >
    = \lambda < 0, 0, 2 > + \mu < 2, 2, 4 >
*/
static void f0_elas_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu     = PetscRealPart(constants[0]);
  const PetscReal lambda = PetscRealPart(constants[1]);

  for (PetscInt d = 0; d < dim - 1; ++d) f0[d] += 2.0 * mu;
  f0[dim - 1] += 2.0 * lambda + 4.0 * mu;
}

static void f0_mass_quadratic_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  if (dim == 2) {
    f0[0] -= x[0] * x[0];
    f0[1] -= x[1] * x[1] - 2.0 * x[0] * x[1];
  } else {
    f0[0] -= x[0] * x[0];
    f0[1] -= x[1] * x[1] - 2.0 * x[0] * x[1];
    f0[2] -= x[2] * x[2] - 2.0 * x[1] * x[2];
  }
}

static PetscErrorCode trig_2d_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  u[0] = PetscSinReal(2.0 * PETSC_PI * x[0]);
  u[1] = PetscSinReal(2.0 * PETSC_PI * x[1]) - 2.0 * x[0] * x[1];
  return PETSC_SUCCESS;
}

static PetscErrorCode trig_3d_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  u[0] = PetscSinReal(2.0 * PETSC_PI * x[0]);
  u[1] = PetscSinReal(2.0 * PETSC_PI * x[1]) - 2.0 * x[0] * x[1];
  u[2] = PetscSinReal(2.0 * PETSC_PI * x[2]) - 2.0 * x[1] * x[2];
  return PETSC_SUCCESS;
}

/*
  u = sin(2 pi x)
  v = sin(2 pi y) - 2xy
  Delta <u,v> - f = <-4 pi^2 u, -4 pi^2 v> - <-4 pi^2 sin(2 pi x), -4 pi^2 sin(2 pi y)>

  u = sin(2 pi x)
  v = sin(2 pi y) - 2xy
  w = sin(2 pi z) - 2yz
  Delta <u,v,2> - f = <-4 pi^2 u, -4 pi^2 v, -4 pi^2 w> - <-4 pi^2 sin(2 pi x), -4 pi^2 sin(2 pi y), -4 pi^2 sin(2 pi z)>
*/
static void f0_vlap_trig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) f0[d] += -4.0 * PetscSqr(PETSC_PI) * PetscSinReal(2.0 * PETSC_PI * x[d]);
}

/*
  u = sin(2 pi x)
  v = sin(2 pi y) - 2xy
  \varepsilon = / 2 pi cos(2 pi x)             -y        \
                \      -y          2 pi cos(2 pi y) - 2x /
  Tr(\varepsilon) = div u = 2 pi (cos(2 pi x) + cos(2 pi y)) - 2 x
  div \sigma = \partial_i \lambda \delta_{ij} \varepsilon_{kk} + \partial_i 2\mu\varepsilon_{ij}
    = \lambda \partial_j 2 pi (cos(2 pi x) + cos(2 pi y)) + 2\mu < -4 pi^2 sin(2 pi x) - 1, -4 pi^2 sin(2 pi y) >
    = \lambda < -4 pi^2 sin(2 pi x) - 2, -4 pi^2 sin(2 pi y) > + \mu < -8 pi^2 sin(2 pi x) - 2, -8 pi^2 sin(2 pi y) >

  u = sin(2 pi x)
  v = sin(2 pi y) - 2xy
  w = sin(2 pi z) - 2yz
  \varepsilon = / 2 pi cos(2 pi x)            -y                     0         \
                |         -y       2 pi cos(2 pi y) - 2x            -z         |
                \          0                  -z         2 pi cos(2 pi z) - 2y /
  Tr(\varepsilon) = div u = 2 pi (cos(2 pi x) + cos(2 pi y) + cos(2 pi z)) - 2 x - 2 y
  div \sigma = \partial_i \lambda \delta_{ij} \varepsilon_{kk} + \partial_i 2\mu\varepsilon_{ij}
    = \lambda \partial_j (2 pi (cos(2 pi x) + cos(2 pi y) + cos(2 pi z)) - 2 x - 2 y) + 2\mu < -4 pi^2 sin(2 pi x) - 1, -4 pi^2 sin(2 pi y) - 1, -4 pi^2 sin(2 pi z) >
    = \lambda < -4 pi^2 sin(2 pi x) - 2, -4 pi^2 sin(2 pi y) - 2, -4 pi^2 sin(2 pi z) > + 2\mu < -4 pi^2 sin(2 pi x) - 1, -4 pi^2 sin(2 pi y) - 1, -4 pi^2 sin(2 pi z) >
*/
static void f0_elas_trig_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal mu     = PetscRealPart(constants[0]);
  const PetscReal lambda = PetscRealPart(constants[1]);
  const PetscReal fact   = 4.0 * PetscSqr(PETSC_PI);

  for (PetscInt d = 0; d < dim; ++d) f0[d] += -(2.0 * mu + lambda) * fact * PetscSinReal(2.0 * PETSC_PI * x[d]) - (d < dim - 1 ? 2.0 * (mu + lambda) : 0.0);
}

static PetscErrorCode axial_disp_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  AppCtx    *user = (AppCtx *)ctx;
  Parameter *param;

  PetscCall(PetscBagGetData(user->bag, &param));
  {
    const PetscReal mu     = PetscRealPart(param->mu);
    const PetscReal lambda = PetscRealPart(param->lambda);
    const PetscReal N      = PetscRealPart(param->N);

    u[0] = (3. * lambda * lambda + 8. * lambda * mu + 4 * mu * mu) / (4 * mu * (3 * lambda * lambda + 5. * lambda * mu + 2 * mu * mu)) * N * x[0];
    u[1] = 0.25 * lambda / mu / (lambda + mu) * N * x[1];
    for (PetscInt d = 2; d < dim; ++d) u[d] = 0.0;
  }
  return PETSC_SUCCESS;
}

/*
  We will pull/push on the right side of a block of linearly elastic material. The uniform traction conditions on the
  right side of the box will result in a uniform strain along x and y. The Neumann BC is given by

     n_i \sigma_{ij} = t_i

  u = (1/(2\mu) - 1) x
  v = -y
  f = 0
  t = <4\mu/\lambda (\lambda + \mu), 0>
  \varepsilon = / 1/(2\mu) - 1   0 \
                \ 0             -1 /
  Tr(\varepsilon) = div u = 1/(2\mu) - 2
  div \sigma = \partial_i \lambda \delta_{ij} \varepsilon_{kk} + \partial_i 2\mu\varepsilon_{ij}
    = \lambda \partial_j (1/(2\mu) - 2) + 2\mu < 0, 0 >
    = \lambda < 0, 0 > + \mu < 0, 0 > = 0
  NBC =  <1,0> . <4\mu/\lambda (\lambda + \mu), 0> = 4\mu/\lambda (\lambda + \mu)

  u = x - 1/2
  v = 0
  w = 0
  \varepsilon = / x  0  0 \
                | 0  0  0 |
                \ 0  0  0 /
  Tr(\varepsilon) = div u = x
  div \sigma = \partial_i \lambda \delta_{ij} \varepsilon_{kk} + \partial_i 2\mu\varepsilon_{ij}
    = \lambda \partial_j x + 2\mu < 1, 0, 0 >
    = \lambda < 1, 0, 0 > + \mu < 2, 0, 0 >
*/
static void f0_elas_axial_disp_bd_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal N = PetscRealPart(constants[2]);

  f0[0] = N;
}

static PetscErrorCode uniform_strain_u(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  const PetscReal eps_xx = 0.1;
  const PetscReal eps_xy = 0.3;
  const PetscReal eps_yy = 0.25;
  PetscInt        d;

  u[0] = eps_xx * x[0] + eps_xy * x[1];
  u[1] = eps_xy * x[0] + eps_yy * x[1];
  for (d = 2; d < dim; ++d) u[d] = 0.0;
  return PETSC_SUCCESS;
}

static void f0_mass_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscInt Nc = dim;
  PetscInt       c;

  for (c = 0; c < Nc; ++c) f0[c] = u[c];
}

static void f1_vlap_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscInt Nc = dim;
  PetscInt       c, d;

  for (c = 0; c < Nc; ++c)
    for (d = 0; d < dim; ++d) f1[c * dim + d] += u_x[c * dim + d];
}

static void f1_elas_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscReal mu     = PetscRealPart(constants[0]);
  const PetscReal lambda = PetscRealPart(constants[1]);
  const PetscInt  Nc     = dim;

  for (PetscInt c = 0; c < Nc; ++c) {
    for (PetscInt d = 0; d < dim; ++d) {
      f1[c * dim + d] += mu * (u_x[c * dim + d] + u_x[d * dim + c]);
      f1[c * dim + c] += lambda * u_x[d * dim + d];
    }
  }
}

static void g0_mass_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  const PetscInt Nc = dim;
  PetscInt       c;

  for (c = 0; c < Nc; ++c) g0[c * Nc + c] = 1.0;
}

static void g3_vlap_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  const PetscInt Nc = dim;
  PetscInt       c, d;

  for (c = 0; c < Nc; ++c) {
    for (d = 0; d < dim; ++d) g3[((c * Nc + c) * dim + d) * dim + d] = 1.0;
  }
}

/*
  \partial_df \phi_fc g_{fc,gc,df,dg} \partial_dg \phi_gc

  \partial_df \phi_fc \lambda \delta_{fc,df} \sum_gc \partial_dg \phi_gc \delta_{gc,dg}
  = \partial_fc \phi_fc \sum_gc \partial_gc \phi_gc
*/
static void g3_elas_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  const PetscReal mu     = PetscRealPart(constants[0]);
  const PetscReal lambda = PetscRealPart(constants[1]);
  const PetscInt  Nc     = dim;

  for (PetscInt c = 0; c < Nc; ++c) {
    for (PetscInt d = 0; d < dim; ++d) {
      g3[((c * Nc + c) * dim + d) * dim + d] += mu;
      g3[((c * Nc + d) * dim + d) * dim + c] += mu;
      g3[((c * Nc + d) * dim + c) * dim + d] += lambda;
    }
  }
}

static PetscErrorCode ProcessOptions(MPI_Comm comm, AppCtx *options)
{
  PetscInt sol = 0, def = 0;

  PetscFunctionBeginUser;
  options->deform           = DEFORM_NONE;
  options->solType          = SOL_VLAP_QUADRATIC;
  options->useNearNullspace = PETSC_TRUE;
  PetscCall(PetscStrncpy(options->dmType, DMPLEX, 256));

  PetscOptionsBegin(comm, "", "Linear Elasticity Problem Options", "DMPLEX");
  PetscCall(PetscOptionsEList("-deform_type", "Type of domain deformation", "ex17.c", deformTypes, NUM_DEFORM_TYPES, deformTypes[options->deform], &def, NULL));
  options->deform = (DeformType)def;
  PetscCall(PetscOptionsEList("-sol_type", "Type of exact solution", "ex17.c", solutionTypes, NUM_SOLUTION_TYPES, solutionTypes[options->solType], &sol, NULL));
  options->solType = (SolutionType)sol;
  PetscCall(PetscOptionsBool("-near_nullspace", "Use the rigid body modes as an AMG near nullspace", "ex17.c", options->useNearNullspace, &options->useNearNullspace, NULL));
  PetscCall(PetscOptionsFList("-dm_type", "Convert DMPlex to another format", "ex17.c", DMList, options->dmType, options->dmType, 256, NULL));
  PetscOptionsEnd();
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupParameters(MPI_Comm comm, AppCtx *ctx)
{
  PetscBag   bag;
  Parameter *p;

  PetscFunctionBeginUser;
  /* setup PETSc parameter bag */
  PetscCall(PetscBagGetData(ctx->bag, &p));
  PetscCall(PetscBagSetName(ctx->bag, "par", "Elastic Parameters"));
  bag = ctx->bag;
  PetscCall(PetscBagRegisterScalar(bag, &p->mu, 1.0, "mu", "Shear Modulus, Pa"));
  PetscCall(PetscBagRegisterScalar(bag, &p->lambda, 1.0, "lambda", "Lame's first parameter, Pa"));
  PetscCall(PetscBagRegisterScalar(bag, &p->N, -1.0, "N", "Tension on right wall, Pa"));
  PetscCall(PetscBagSetFromOptions(bag));
  {
    PetscViewer       viewer;
    PetscViewerFormat format;
    PetscBool         flg;

    PetscCall(PetscOptionsCreateViewer(comm, NULL, NULL, "-param_view", &viewer, &format, &flg));
    if (flg) {
      PetscCall(PetscViewerPushFormat(viewer, format));
      PetscCall(PetscBagView(bag, viewer));
      PetscCall(PetscViewerFlush(viewer));
      PetscCall(PetscViewerPopFormat(viewer));
      PetscCall(PetscViewerDestroy(&viewer));
    }
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode DMPlexDistortGeometry(DM dm)
{
  DM           cdm;
  DMLabel      label;
  Vec          coordinates;
  PetscScalar *coords;
  PetscReal    mid = 0.5;
  PetscInt     cdim, d, vStart, vEnd, v;

  PetscFunctionBeginUser;
  PetscCall(DMGetCoordinateDM(dm, &cdm));
  PetscCall(DMGetCoordinateDim(dm, &cdim));
  PetscCall(DMPlexGetDepthStratum(dm, 0, &vStart, &vEnd));
  PetscCall(DMGetLabel(dm, "marker", &label));
  PetscCall(DMGetCoordinatesLocal(dm, &coordinates));
  PetscCall(VecGetArrayWrite(coordinates, &coords));
  for (v = vStart; v < vEnd; ++v) {
    PetscScalar *pcoords, shift;
    PetscInt     val;

    PetscCall(DMLabelGetValue(label, v, &val));
    if (val >= 0) continue;
    PetscCall(DMPlexPointLocalRef(cdm, v, coords, &pcoords));
    shift = 0.2 * PetscAbsScalar(pcoords[0] - mid);
    shift = PetscRealPart(pcoords[0]) > mid ? shift : -shift;
    for (d = 1; d < cdim; ++d) pcoords[d] += shift;
  }
  PetscCall(VecRestoreArrayWrite(coordinates, &coords));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode CreateMesh(MPI_Comm comm, AppCtx *user, DM *dm)
{
  PetscFunctionBeginUser;
  PetscCall(DMCreate(comm, dm));
  PetscCall(DMSetType(*dm, DMPLEX));
  PetscCall(DMSetFromOptions(*dm));
  switch (user->deform) {
  case DEFORM_NONE:
    break;
  case DEFORM_SHEAR:
    PetscCall(DMPlexShearGeometry(*dm, DM_X, NULL));
    break;
  case DEFORM_STEP:
    PetscCall(DMPlexDistortGeometry(*dm));
    break;
  default:
    SETERRQ(comm, PETSC_ERR_ARG_OUTOFRANGE, "Invalid deformation type: %s (%d)", deformTypes[PetscMin(user->deform, NUM_DEFORM_TYPES)], user->deform);
  }
  PetscCall(DMSetApplicationContext(*dm, user));
  PetscCall(DMViewFromOptions(*dm, NULL, "-dm_view"));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupPrimalProblem(DM dm, AppCtx *user)
{
  PetscErrorCode (*exact)(PetscInt, PetscReal, const PetscReal[], PetscInt, PetscScalar *, void *);
  Parameter    *param;
  PetscDS       ds;
  PetscWeakForm wf;
  DMLabel       label;
  PetscInt      id, bd;
  PetscInt      dim;

  PetscFunctionBeginUser;
  PetscCall(DMGetDS(dm, &ds));
  PetscCall(PetscDSGetWeakForm(ds, &wf));
  PetscCall(PetscDSGetSpatialDimension(ds, &dim));
  PetscCall(PetscBagGetData(user->bag, &param));
  switch (user->solType) {
  case SOL_MASS_QUADRATIC:
    PetscCall(PetscDSSetResidual(ds, 0, f0_mass_u, NULL));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, g0_mass_uu, NULL, NULL, NULL));
    PetscCall(PetscWeakFormSetIndexResidual(wf, NULL, 0, 0, 0, 1, f0_mass_quadratic_u, 0, NULL));
    switch (dim) {
    case 2:
      exact = quadratic_2d_u;
      break;
    case 3:
      exact = quadratic_3d_u;
      break;
    default:
      SETERRQ(PetscObjectComm((PetscObject)ds), PETSC_ERR_ARG_WRONG, "Invalid dimension: %" PetscInt_FMT, dim);
    }
    break;
  case SOL_VLAP_QUADRATIC:
    PetscCall(PetscDSSetResidual(ds, 0, f0_vlap_quadratic_u, f1_vlap_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_vlap_uu));
    switch (dim) {
    case 2:
      exact = quadratic_2d_u;
      break;
    case 3:
      exact = quadratic_3d_u;
      break;
    default:
      SETERRQ(PetscObjectComm((PetscObject)ds), PETSC_ERR_ARG_WRONG, "Invalid dimension: %" PetscInt_FMT, dim);
    }
    break;
  case SOL_ELAS_QUADRATIC:
    PetscCall(PetscDSSetResidual(ds, 0, f0_elas_quadratic_u, f1_elas_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_elas_uu));
    switch (dim) {
    case 2:
      exact = quadratic_2d_u;
      break;
    case 3:
      exact = quadratic_3d_u;
      break;
    default:
      SETERRQ(PetscObjectComm((PetscObject)ds), PETSC_ERR_ARG_WRONG, "Invalid dimension: %" PetscInt_FMT, dim);
    }
    break;
  case SOL_VLAP_TRIG:
    PetscCall(PetscDSSetResidual(ds, 0, f0_vlap_trig_u, f1_vlap_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_vlap_uu));
    switch (dim) {
    case 2:
      exact = trig_2d_u;
      break;
    case 3:
      exact = trig_3d_u;
      break;
    default:
      SETERRQ(PetscObjectComm((PetscObject)ds), PETSC_ERR_ARG_WRONG, "Invalid dimension: %" PetscInt_FMT, dim);
    }
    break;
  case SOL_ELAS_TRIG:
    PetscCall(PetscDSSetResidual(ds, 0, f0_elas_trig_u, f1_elas_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_elas_uu));
    switch (dim) {
    case 2:
      exact = trig_2d_u;
      break;
    case 3:
      exact = trig_3d_u;
      break;
    default:
      SETERRQ(PetscObjectComm((PetscObject)ds), PETSC_ERR_ARG_WRONG, "Invalid dimension: %" PetscInt_FMT, dim);
    }
    break;
  case SOL_ELAS_AXIAL_DISP:
    PetscCall(PetscDSSetResidual(ds, 0, NULL, f1_elas_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_elas_uu));
    id = dim == 3 ? 5 : 2;
    PetscCall(DMGetLabel(dm, "marker", &label));
    PetscCall(DMAddBoundary(dm, DM_BC_NATURAL, "right", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)NULL, NULL, user, &bd));
    PetscCall(PetscDSGetBoundary(ds, bd, &wf, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL));
    PetscCall(PetscWeakFormSetIndexBdResidual(wf, label, id, 0, 0, 0, f0_elas_axial_disp_bd_u, 0, NULL));
    exact = axial_disp_u;
    break;
  case SOL_ELAS_UNIFORM_STRAIN:
    PetscCall(PetscDSSetResidual(ds, 0, NULL, f1_elas_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_elas_uu));
    exact = uniform_strain_u;
    break;
  case SOL_ELAS_GE:
    PetscCall(PetscDSSetResidual(ds, 0, NULL, f1_elas_u));
    PetscCall(PetscDSSetJacobian(ds, 0, 0, NULL, NULL, NULL, g3_elas_uu));
    exact = zero; /* No exact solution available */
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)ds), PETSC_ERR_ARG_WRONG, "Invalid solution type: %s (%d)", solutionTypes[PetscMin(user->solType, NUM_SOLUTION_TYPES)], user->solType);
  }
  PetscCall(PetscDSSetExactSolution(ds, 0, exact, user));
  PetscCall(DMGetLabel(dm, "marker", &label));
  if (user->solType == SOL_ELAS_AXIAL_DISP) {
    PetscInt cmp;

    id  = dim == 3 ? 6 : 4;
    cmp = 0;
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "left", label, 1, &id, 0, 1, &cmp, (PetscVoidFn *)zero, NULL, user, NULL));
    cmp = dim == 3 ? 2 : 1;
    id  = dim == 3 ? 1 : 1;
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "bottom", label, 1, &id, 0, 1, &cmp, (PetscVoidFn *)zero, NULL, user, NULL));
    if (dim == 3) {
      cmp = 1;
      id  = 3;
      PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "front", label, 1, &id, 0, 1, &cmp, (PetscVoidFn *)zero, NULL, user, NULL));
    }
  } else if (user->solType == SOL_ELAS_GE) {
    PetscInt cmp;

    id = dim == 3 ? 6 : 4;
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "left", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)zero, NULL, user, NULL));
    id  = dim == 3 ? 5 : 2;
    cmp = 0;
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "right", label, 1, &id, 0, 1, &cmp, (PetscVoidFn *)ge_shift, NULL, user, NULL));
  } else {
    id = 1;
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)exact, NULL, user, NULL));
  }
  /* Setup constants */
  {
    PetscScalar constants[3];

    constants[0] = param->mu;     /* shear modulus, Pa */
    constants[1] = param->lambda; /* Lame's first parameter, Pa */
    constants[2] = param->N;      /* Tension on right wall, Pa */
    PetscCall(PetscDSSetConstants(ds, 3, constants));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode CreateElasticityNullSpace(DM dm, PetscInt origField, PetscInt field, MatNullSpace *nullspace)
{
  PetscFunctionBegin;
  PetscCall(DMPlexCreateRigidBody(dm, origField, nullspace));
  PetscFunctionReturn(PETSC_SUCCESS);
}

PetscErrorCode SetupFE(DM dm, const char name[], PetscErrorCode (*setup)(DM, AppCtx *), PetscCtx ctx)
{
  AppCtx        *user = (AppCtx *)ctx;
  DM             cdm  = dm;
  PetscFE        fe;
  char           prefix[PETSC_MAX_PATH_LEN];
  DMPolytopeType ct;
  PetscInt       dim, cStart;

  PetscFunctionBegin;
  /* Create finite element */
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMPlexGetHeightStratum(dm, 0, &cStart, NULL));
  PetscCall(DMPlexGetCellType(dm, cStart, &ct));
  PetscCall(PetscSNPrintf(prefix, PETSC_MAX_PATH_LEN, "%s_", name));
  PetscCall(PetscFECreateByCell(PETSC_COMM_SELF, dim, dim, ct, name ? prefix : NULL, -1, &fe));
  PetscCall(PetscObjectSetName((PetscObject)fe, name));
  /* Set discretization and boundary conditions for each mesh */
  PetscCall(DMSetField(dm, 0, NULL, (PetscObject)fe));
  PetscCall(DMCreateDS(dm));
  PetscCall((*setup)(dm, user));
  while (cdm) {
    PetscCall(DMCopyDisc(dm, cdm));
    if (user->useNearNullspace) PetscCall(DMSetNearNullSpaceConstructor(cdm, 0, CreateElasticityNullSpace));
    PetscCall(DMGetCoarseDM(cdm, &cdm));
  }
  PetscCall(PetscFEDestroy(&fe));
  PetscFunctionReturn(PETSC_SUCCESS);
}

int main(int argc, char **argv)
{
  DM     dm;   /* Problem specification */
  SNES   snes; /* Nonlinear solver */
  Vec    u;    /* Solutions */
  AppCtx user; /* User-defined work context */

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(ProcessOptions(PETSC_COMM_WORLD, &user));
  PetscCall(PetscBagCreate(PETSC_COMM_SELF, sizeof(Parameter), &user.bag));
  PetscCall(SetupParameters(PETSC_COMM_WORLD, &user));
  /* Primal system */
  PetscCall(SNESCreate(PETSC_COMM_WORLD, &snes));
  PetscCall(CreateMesh(PETSC_COMM_WORLD, &user, &dm));
  PetscCall(SNESSetDM(snes, dm));
  PetscCall(SetupFE(dm, "displacement", SetupPrimalProblem, &user));
  PetscCall(DMCreateGlobalVector(dm, &u));
  PetscCall(VecSet(u, 0.0));
  PetscCall(PetscObjectSetName((PetscObject)u, "displacement"));
  PetscCall(DMPlexSetSNESLocalFEM(dm, PETSC_FALSE, &user));
  PetscCall(SNESSetFromOptions(snes));
  PetscCall(DMSNESCheckFromOptions(snes, u));
  PetscCall(SNESSolve(snes, NULL, u));
  PetscCall(SNESGetSolution(snes, &u));
  PetscCall(VecViewFromOptions(u, NULL, "-displacement_view"));
  /* Cleanup */
  PetscCall(VecDestroy(&u));
  PetscCall(SNESDestroy(&snes));
  PetscCall(DMDestroy(&dm));
  PetscCall(PetscBagDestroy(&user.bag));
  PetscCall(PetscFinalize());
  return 0;
}

/*TEST

  testset:
    args: -dm_plex_box_faces 1,1,1

    test:
      suffix: 2d_p1_quad_vlap
      requires: triangle
      args: -displacement_petscspace_degree 1 -dm_refine 2 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_p2_quad_vlap
      requires: triangle
      args: -displacement_petscspace_degree 2 -dm_refine 2 -dmsnes_check .0001
    test:
      suffix: 2d_p3_quad_vlap
      requires: triangle
      args: -displacement_petscspace_degree 3 -dm_refine 2 -dmsnes_check .0001
    test:
      suffix: 2d_q1_quad_vlap
      args: -dm_plex_simplex 0 -displacement_petscspace_degree 1 -dm_refine 2 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q2_quad_vlap
      args: -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_refine 2 -dmsnes_check .0001
    test:
      suffix: 2d_q3_quad_vlap
      requires: !single
      args: -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_refine 2 -dmsnes_check .0001
    test:
      suffix: 2d_p1_quad_elas
      requires: triangle
      args: -sol_type elas_quad -displacement_petscspace_degree 1 -dm_refine 2 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_p2_quad_elas
      requires: triangle
      args: -sol_type elas_quad -displacement_petscspace_degree 2 -dmsnes_check .0001
    test:
      suffix: 2d_p3_quad_elas
      requires: triangle
      args: -sol_type elas_quad -displacement_petscspace_degree 3 -dmsnes_check .0001
    test:
      suffix: 2d_q1_quad_elas
      args: -sol_type elas_quad -dm_plex_simplex 0 -displacement_petscspace_degree 1 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q1_quad_elas_shear
      args: -sol_type elas_quad -dm_plex_simplex 0 -deform_type shear -displacement_petscspace_degree 1 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q2_quad_elas
      args: -sol_type elas_quad -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dmsnes_check .0001
    test:
      suffix: 2d_q2_quad_elas_shear
      args: -sol_type elas_quad -dm_plex_simplex 0 -deform_type shear -displacement_petscspace_degree 2 -dmsnes_check
    test:
      suffix: 2d_q3_quad_elas
      args: -sol_type elas_quad -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dmsnes_check .0001
    test:
      suffix: 2d_q3_quad_elas_shear
      requires: !single
      args: -sol_type elas_quad -dm_plex_simplex 0 -deform_type shear -displacement_petscspace_degree 3 -dmsnes_check

    test:
      suffix: 3d_p1_quad_vlap
      requires: ctetgen
      args: -dm_plex_dim 3 -dm_refine 1 -displacement_petscspace_degree 1 -convest_num_refine 2 -snes_convergence_estimate
    test:
      suffix: 3d_p2_quad_vlap
      requires: ctetgen
      args: -dm_plex_dim 3 -displacement_petscspace_degree 2 -dm_refine 1 -dmsnes_check .0001
    test:
      suffix: 3d_p3_quad_vlap
      requires: ctetgen
      args: -dm_plex_dim 3 -displacement_petscspace_degree 3 -dm_refine 0 -dmsnes_check .0001
    test:
      suffix: 3d_q1_quad_vlap
      args: -dm_plex_dim 3 -dm_plex_box_faces 2,2,2 -dm_plex_simplex 0 -displacement_petscspace_degree 1 -convest_num_refine 2 -snes_convergence_estimate
    test:
      suffix: 3d_q2_quad_vlap
      args: -dm_plex_dim 3 -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_refine 1 -dmsnes_check .0001
    test:
      suffix: 3d_q3_quad_vlap
      args: -dm_plex_dim 3 -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_refine 0 -dmsnes_check .0001
    test:
      suffix: 3d_p1_quad_elas
      requires: ctetgen
      args: -sol_type elas_quad -dm_plex_dim 3 -dm_refine 1 -displacement_petscspace_degree 1 -convest_num_refine 2 -snes_convergence_estimate
    test:
      suffix: 3d_p2_quad_elas
      requires: ctetgen
      args: -sol_type elas_quad -dm_plex_dim 3 -displacement_petscspace_degree 2 -dm_refine 1 -dmsnes_check .0001
    test:
      suffix: 3d_p3_quad_elas
      requires: ctetgen
      args: -sol_type elas_quad -dm_plex_dim 3 -displacement_petscspace_degree 3 -dm_refine 0 -dmsnes_check .0001
    test:
      suffix: 3d_q1_quad_elas
      args: -sol_type elas_quad -dm_plex_dim 3 -dm_plex_box_faces 2,2,2 -dm_plex_simplex 0 -displacement_petscspace_degree 1 -convest_num_refine 2 -snes_convergence_estimate
    test:
      suffix: 3d_q2_quad_elas
      args: -sol_type elas_quad -dm_plex_dim 3 -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_refine 1 -dmsnes_check .0001
    test:
      suffix: 3d_q3_quad_elas
      requires: !single
      args: -sol_type elas_quad -dm_plex_dim 3 -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_refine 0 -dmsnes_check .0001

    test:
      suffix: 2d_p1_trig_vlap
      requires: triangle
      args: -sol_type vlap_trig -displacement_petscspace_degree 1 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_p2_trig_vlap
      requires: triangle
      args: -sol_type vlap_trig -displacement_petscspace_degree 2 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_p3_trig_vlap
      requires: triangle
      args: -sol_type vlap_trig -displacement_petscspace_degree 3 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q1_trig_vlap
      args: -sol_type vlap_trig -dm_plex_simplex 0 -displacement_petscspace_degree 1 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q2_trig_vlap
      args: -sol_type vlap_trig -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q3_trig_vlap
      args: -sol_type vlap_trig -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_p1_trig_elas
      requires: triangle
      args: -sol_type elas_trig -displacement_petscspace_degree 1 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_p2_trig_elas
      requires: triangle
      args: -sol_type elas_trig -displacement_petscspace_degree 2 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_p3_trig_elas
      requires: triangle
      args: -sol_type elas_trig -displacement_petscspace_degree 3 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q1_trig_elas
      args: -sol_type elas_trig -dm_plex_simplex 0 -displacement_petscspace_degree 1 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q1_trig_elas_shear
      args: -sol_type elas_trig -dm_plex_simplex 0 -deform_type shear -displacement_petscspace_degree 1 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q2_trig_elas
      args: -sol_type elas_trig -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q2_trig_elas_shear
      args: -sol_type elas_trig -dm_plex_simplex 0 -deform_type shear -displacement_petscspace_degree 2 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q3_trig_elas
      args: -sol_type elas_trig -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate
    test:
      suffix: 2d_q3_trig_elas_shear
      args: -sol_type elas_trig -dm_plex_simplex 0 -deform_type shear -displacement_petscspace_degree 3 -dm_refine 1 -convest_num_refine 3 -snes_convergence_estimate

    test:
      suffix: 3d_p1_trig_vlap
      requires: ctetgen
      args: -sol_type vlap_trig -dm_plex_dim 3 -dm_refine 1 -displacement_petscspace_degree 1 -convest_num_refine 2 -snes_convergence_estimate
    test:
      suffix: 3d_p2_trig_vlap
      requires: ctetgen
      args: -sol_type vlap_trig -dm_plex_dim 3 -displacement_petscspace_degree 2 -dm_refine 0 -convest_num_refine 1 -snes_convergence_estimate
    test:
      suffix: 3d_p3_trig_vlap
      requires: ctetgen
      args: -sol_type vlap_trig -dm_plex_dim 3 -displacement_petscspace_degree 3 -dm_refine 0 -convest_num_refine 1 -snes_convergence_estimate
    test:
      suffix: 3d_q1_trig_vlap
      args: -sol_type vlap_trig -dm_plex_dim 3 -dm_plex_box_faces 2,2,2 -dm_plex_simplex 0 -displacement_petscspace_degree 1 -convest_num_refine 2 -snes_convergence_estimate
    test:
      suffix: 3d_q2_trig_vlap
      args: -sol_type vlap_trig -dm_plex_dim 3 -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_refine 0 -convest_num_refine 1 -snes_convergence_estimate
    test:
      suffix: 3d_q3_trig_vlap
      requires: !__float128
      args: -sol_type vlap_trig -dm_plex_dim 3 -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_refine 0 -convest_num_refine 1 -snes_convergence_estimate
    test:
      suffix: 3d_p1_trig_elas
      requires: ctetgen
      args: -sol_type elas_trig -dm_plex_dim 3 -dm_refine 1 -displacement_petscspace_degree 1 -convest_num_refine 2 -snes_convergence_estimate
    test:
      suffix: 3d_p2_trig_elas
      requires: ctetgen
      args: -sol_type elas_trig -dm_plex_dim 3 -displacement_petscspace_degree 2 -dm_refine 0 -convest_num_refine 1 -snes_convergence_estimate
    test:
      suffix: 3d_p3_trig_elas
      requires: ctetgen
      args: -sol_type elas_trig -dm_plex_dim 3 -displacement_petscspace_degree 3 -dm_refine 0 -convest_num_refine 1 -snes_convergence_estimate
    test:
      suffix: 3d_q1_trig_elas
      args: -sol_type elas_trig -dm_plex_dim 3 -dm_plex_box_faces 2,2,2 -dm_plex_simplex 0 -displacement_petscspace_degree 1 -convest_num_refine 2 -snes_convergence_estimate
    test:
      suffix: 3d_q2_trig_elas
      args: -sol_type elas_trig -dm_plex_dim 3 -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_refine 0 -convest_num_refine 1 -snes_convergence_estimate
    test:
      suffix: 3d_q3_trig_elas
      requires: !__float128
      args: -sol_type elas_trig -dm_plex_dim 3 -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_refine 0 -convest_num_refine 1 -snes_convergence_estimate

    test:
      suffix: 2d_p1_axial_elas
      requires: triangle
      args: -sol_type elas_axial_disp -displacement_petscspace_degree 1 -dm_plex_separate_marker -dm_refine 2 -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_p2_axial_elas
      requires: triangle
      args: -sol_type elas_axial_disp -displacement_petscspace_degree 2 -dm_plex_separate_marker -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_p3_axial_elas
      requires: triangle
      args: -sol_type elas_axial_disp -displacement_petscspace_degree 3 -dm_plex_separate_marker -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_q1_axial_elas
      args: -sol_type elas_axial_disp -dm_plex_simplex 0 -displacement_petscspace_degree 1 -dm_plex_separate_marker -dm_refine 1 -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_q2_axial_elas
      args: -sol_type elas_axial_disp -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_plex_separate_marker -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_q3_axial_elas
      args: -sol_type elas_axial_disp -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_plex_separate_marker -dmsnes_check .0001 -pc_type lu

    test:
      suffix: 2d_p1_uniform_elas
      requires: triangle
      args: -sol_type elas_uniform_strain -displacement_petscspace_degree 1 -dm_refine 2 -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_p2_uniform_elas
      requires: triangle
      args: -sol_type elas_uniform_strain -displacement_petscspace_degree 2 -dm_refine 2 -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_p3_uniform_elas
      requires: triangle
      args: -sol_type elas_uniform_strain -displacement_petscspace_degree 3 -dm_refine 2 -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_q1_uniform_elas
      args: -sol_type elas_uniform_strain -dm_plex_simplex 0 -displacement_petscspace_degree 1 -dm_refine 2 -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_q2_uniform_elas
      requires: !single
      args: -sol_type elas_uniform_strain -dm_plex_simplex 0 -displacement_petscspace_degree 2 -dm_refine 2 -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_q3_uniform_elas
      requires: !single
      args: -sol_type elas_uniform_strain -dm_plex_simplex 0 -displacement_petscspace_degree 3 -dm_refine 2 -dmsnes_check .0001 -pc_type lu
    test:
      suffix: 2d_p1_uniform_elas_step
      requires: triangle
      args: -sol_type elas_uniform_strain -deform_type step -displacement_petscspace_degree 1 -dm_refine 2 -dmsnes_check .0001 -pc_type lu

  testset:
    args: -dm_plex_simplex 0 -dm_plex_box_faces 3,3 -deform_type step -displacement_petscspace_degree 1 -dmsnes_check .0001 -pc_type lu

    test:
      suffix: 2d_q1_uniform_elas_step
      args: -sol_type elas_uniform_strain -dm_refine 2
    test:
      suffix: 2d_q1_quad_vlap_step
      args:
    test:
      suffix: 2d_q2_quad_vlap_step
      args: -displacement_petscspace_degree 2
    test:
      suffix: 2d_q1_quad_mass_step
      args: -sol_type mass_quad

  testset:
    filter: grep -v "variant HERMITIAN"
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower -5,-5,-0.25 -dm_plex_box_upper 5,5,0.25 \
          -dm_plex_box_faces 5,5,2 -dm_plex_separate_marker -dm_refine 0 -petscpartitioner_type simple \
          -sol_type elas_ge

    test:
      suffix: ge_q1_0
      args: -displacement_petscspace_degree 1 \
            -snes_max_it 2 -snes_rtol 1.e-10 \
            -ksp_type cg -ksp_rtol 1.e-10 -ksp_max_it 100 -ksp_norm_type unpreconditioned \
            -pc_type gamg -pc_gamg_type agg -pc_gamg_agg_nsmooths 1 \
              -pc_gamg_coarse_eq_limit 10 -pc_gamg_reuse_interpolation true \
              -pc_gamg_threshold 0.05 -pc_gamg_threshold_scale .0 \
              -mg_levels_ksp_max_it 2 -mg_levels_ksp_type chebyshev -mg_levels_ksp_chebyshev_esteig 0,0.05,0,1.1 -mg_levels_pc_type jacobi \
              -matptap_via scalable
      output_file: output/empty.out
    test:
      suffix: ge_q1_gmg
      args: -displacement_petscspace_degree 1 \
            -dm_plex_box_faces 2,2 -dm_refine_hierarchy 3 \
            -snes_max_it 2 -snes_rtol 1.e-10 \
            -ksp_type cg -ksp_rtol 1.e-10 -ksp_max_it 100 -ksp_norm_type unpreconditioned \
            -pc_type mg -pc_mg_type full \
              -mg_levels_ksp_max_it 4 -mg_levels_esteig_ksp_type cg \
              -mg_levels_esteig_ksp_max_it 10 -mg_levels_ksp_chebyshev_esteig 0,0.1,0,1.1 \
              -mg_levels_pc_type jacobi
      output_file: output/empty.out
    test:
      nsize: 5
      suffix: ge_q1_gdsw
      args: -snes_max_it 1 -ksp_type cg -ksp_norm_type natural -displacement_petscspace_degree 1 -snes_monitor_short -ksp_monitor_short -pc_type mg -pc_mg_adapt_interp_coarse_space gdsw -pc_mg_levels 2 -pc_mg_galerkin -mg_levels_pc_type bjacobi -mg_levels_esteig_ksp_type cg -mg_levels_sub_pc_type icc -mg_coarse_redundant_pc_type cholesky -ksp_view

TEST*/
````

## SNES ex5.c

- Selected by: Tutorials by physics
- Rendered listing: <https://petsc.org/release/src/snes/tutorials/ex5.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/snes/tutorials/ex5.c>

````c
static char help[] = "Bratu nonlinear PDE in 2d.\n\
We solve the  Bratu (SFI - solid fuel ignition) problem in a 2D rectangular\n\
domain, using distributed arrays (DMDAs) to partition the parallel grid.\n\
The command line options include:\n\
  -par <parameter>, where <parameter> indicates the problem's nonlinearity\n\
     problem SFI:  <parameter> = Bratu parameter (0 <= par <= 6.81)\n\n\
  -m_par/n_par <parameter>, where <parameter> indicates an integer\n \
      that MMS3 will be evaluated with 2^m_par, 2^n_par";

/* ------------------------------------------------------------------------

    Solid Fuel Ignition (SFI) problem.  This problem is modeled by
    the partial differential equation

            -Laplacian u - lambda*exp(u) = 0,  0 < x,y < 1,

    with boundary conditions

             u = 0  for  x = 0, x = 1, y = 0, y = 1.

    A finite difference approximation with the usual 5-point stencil
    is used to discretize the boundary value problem to obtain a nonlinear
    system of equations.

      This example shows how geometric multigrid can be run transparently with a nonlinear solver so long
      as SNESSetDM() is provided. Example usage

      ./ex5 -pc_type mg -ksp_monitor  -snes_view -pc_mg_levels 3 -pc_mg_galerkin pmat -da_grid_x 17 -da_grid_y 17
             -mg_levels_ksp_monitor -snes_monitor -mg_levels_pc_type sor -pc_mg_type full

      or to run with grid sequencing on the nonlinear problem (note that you do not need to provide the number of
         multigrid levels, it will be determined automatically based on the number of refinements done)

      ./ex5 -pc_type mg -ksp_monitor  -snes_view -pc_mg_galerkin pmat -snes_grid_sequence 3
             -mg_levels_ksp_monitor -snes_monitor -mg_levels_pc_type sor -pc_mg_type full

  ------------------------------------------------------------------------- */

/*
   Include "petscdmda.h" so that we can use distributed arrays (DMDAs).
   Include "petscsnes.h" so that we can use SNES solvers.  Note that this
*/
#include <petscdm.h>
#include <petscdmda.h>
#include <petscsnes.h>
#include <petscmatlab.h>
#include <petsc/private/snesimpl.h>

/*
   User-defined application context - contains data needed by the
   application-provided call-back routines, FormJacobianLocal() and
   FormFunctionLocal().
*/
typedef struct AppCtx AppCtx;
struct AppCtx {
  PetscReal param; /* test problem parameter */
  PetscInt  m, n;  /* MMS3 parameters */
  PetscErrorCode (*mms_solution)(AppCtx *, const DMDACoor2d *, PetscScalar *);
  PetscErrorCode (*mms_forcing)(AppCtx *, const DMDACoor2d *, PetscScalar *);
};

/* ------------------------------------------------------------------- */
/*
   FormInitialGuess - Forms initial approximation.

   Input Parameters:
   da - The DM
   user - user-defined application context

   Output Parameter:
   X - vector
 */
static PetscErrorCode FormInitialGuess(DM da, AppCtx *user, Vec X)
{
  PetscInt      i, j, Mx, My, xs, ys, xm, ym;
  PetscReal     lambda, temp1, temp, hx, hy;
  PetscScalar **x;

  PetscFunctionBeginUser;
  PetscCall(DMDAGetInfo(da, PETSC_IGNORE, &Mx, &My, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE));

  lambda = user->param;
  hx     = 1.0 / (PetscReal)(Mx - 1);
  hy     = 1.0 / (PetscReal)(My - 1);
  temp1  = lambda / (lambda + 1.0);

  /*
     Get a pointer to vector data.
       - For default PETSc vectors, VecGetArray() returns a pointer to
         the data array.  Otherwise, the routine is implementation dependent.
       - You MUST call VecRestoreArray() when you no longer need access to
         the array.
  */
  PetscCall(DMDAVecGetArray(da, X, &x));

  /*
     Get local grid boundaries (for 2-dimensional DMDA):
       xs, ys   - starting grid indices (no ghost points)
       xm, ym   - widths of local grid (no ghost points)

  */
  PetscCall(DMDAGetCorners(da, &xs, &ys, NULL, &xm, &ym, NULL));

  /*
     Compute initial guess over the locally owned part of the grid
  */
  for (j = ys; j < ys + ym; j++) {
    temp = (PetscReal)(PetscMin(j, My - j - 1)) * hy;
    for (i = xs; i < xs + xm; i++) {
      if (i == 0 || j == 0 || i == Mx - 1 || j == My - 1) {
        /* boundary conditions are all zero Dirichlet */
        x[j][i] = 0.0;
      } else {
        x[j][i] = temp1 * PetscSqrtReal(PetscMin((PetscReal)(PetscMin(i, Mx - i - 1)) * hx, temp));
      }
    }
  }

  /*
     Restore vector
  */
  PetscCall(DMDAVecRestoreArray(da, X, &x));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/*
  FormExactSolution - Forms MMS solution

  Input Parameters:
  da - The DM
  user - user-defined application context

  Output Parameter:
  X - vector
 */
static PetscErrorCode FormExactSolution(DM da, AppCtx *user, Vec U)
{
  DM            coordDA;
  Vec           coordinates;
  DMDACoor2d  **coords;
  PetscScalar **u;
  PetscInt      xs, ys, xm, ym, i, j;

  PetscFunctionBeginUser;
  PetscCall(DMDAGetCorners(da, &xs, &ys, NULL, &xm, &ym, NULL));
  PetscCall(DMGetCoordinateDM(da, &coordDA));
  PetscCall(DMGetCoordinates(da, &coordinates));
  PetscCall(DMDAVecGetArray(coordDA, coordinates, &coords));
  PetscCall(DMDAVecGetArray(da, U, &u));
  for (j = ys; j < ys + ym; ++j) {
    for (i = xs; i < xs + xm; ++i) PetscCall(user->mms_solution(user, &coords[j][i], &u[j][i]));
  }
  PetscCall(DMDAVecRestoreArray(da, U, &u));
  PetscCall(DMDAVecRestoreArray(coordDA, coordinates, &coords));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode ZeroBCSolution(AppCtx *user, const DMDACoor2d *c, PetscScalar *u)
{
  u[0] = 0.;
  return PETSC_SUCCESS;
}

/* The functions below evaluate the MMS solution u(x,y) and associated forcing

     f(x,y) = -u_xx - u_yy - lambda exp(u)

  such that u(x,y) is an exact solution with f(x,y) as the right-hand side forcing term.
 */
static PetscErrorCode MMSSolution1(AppCtx *user, const DMDACoor2d *c, PetscScalar *u)
{
  PetscReal x = PetscRealPart(c->x), y = PetscRealPart(c->y);

  PetscFunctionBeginUser;
  u[0] = x * (1 - x) * y * (1 - y);
  PetscCall(PetscLogFlops(5));
  PetscFunctionReturn(PETSC_SUCCESS);
}
static PetscErrorCode MMSForcing1(AppCtx *user, const DMDACoor2d *c, PetscScalar *f)
{
  PetscReal x = PetscRealPart(c->x), y = PetscRealPart(c->y);

  PetscFunctionBeginUser;
  f[0] = 2 * x * (1 - x) + 2 * y * (1 - y) - user->param * PetscExpReal(x * (1 - x) * y * (1 - y));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode MMSSolution2(AppCtx *user, const DMDACoor2d *c, PetscScalar *u)
{
  PetscReal x = PetscRealPart(c->x), y = PetscRealPart(c->y);

  PetscFunctionBeginUser;
  u[0] = PetscSinReal(PETSC_PI * x) * PetscSinReal(PETSC_PI * y);
  PetscCall(PetscLogFlops(5));
  PetscFunctionReturn(PETSC_SUCCESS);
}
static PetscErrorCode MMSForcing2(AppCtx *user, const DMDACoor2d *c, PetscScalar *f)
{
  PetscReal x = PetscRealPart(c->x), y = PetscRealPart(c->y);

  PetscFunctionBeginUser;
  f[0] = 2 * PetscSqr(PETSC_PI) * PetscSinReal(PETSC_PI * x) * PetscSinReal(PETSC_PI * y) - user->param * PetscExpReal(PetscSinReal(PETSC_PI * x) * PetscSinReal(PETSC_PI * y));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode MMSSolution3(AppCtx *user, const DMDACoor2d *c, PetscScalar *u)
{
  PetscReal x = PetscRealPart(c->x), y = PetscRealPart(c->y);

  PetscFunctionBeginUser;
  u[0] = PetscSinReal(user->m * PETSC_PI * x * (1 - y)) * PetscSinReal(user->n * PETSC_PI * y * (1 - x));
  PetscCall(PetscLogFlops(5));
  PetscFunctionReturn(PETSC_SUCCESS);
}
static PetscErrorCode MMSForcing3(AppCtx *user, const DMDACoor2d *c, PetscScalar *f)
{
  PetscReal x = PetscRealPart(c->x), y = PetscRealPart(c->y);
  PetscReal m = user->m, n = user->n, lambda = user->param;

  PetscFunctionBeginUser;
  f[0] = (-(PetscExpReal(PetscSinReal(m * PETSC_PI * x * (1 - y)) * PetscSinReal(n * PETSC_PI * (1 - x) * y)) * lambda) + PetscSqr(PETSC_PI) * (-2 * m * n * ((-1 + x) * x + (-1 + y) * y) * PetscCosReal(m * PETSC_PI * x * (-1 + y)) * PetscCosReal(n * PETSC_PI * (-1 + x) * y) + (PetscSqr(m) * (PetscSqr(x) + PetscSqr(-1 + y)) + PetscSqr(n) * (PetscSqr(-1 + x) + PetscSqr(y))) * PetscSinReal(m * PETSC_PI * x * (-1 + y)) * PetscSinReal(n * PETSC_PI * (-1 + x) * y)));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode MMSSolution4(AppCtx *user, const DMDACoor2d *c, PetscScalar *u)
{
  const PetscReal Lx = 1., Ly = 1.;
  PetscReal       x = PetscRealPart(c->x), y = PetscRealPart(c->y);

  PetscFunctionBeginUser;
  u[0] = (PetscPowReal(x, 4) - PetscSqr(Lx) * PetscSqr(x)) * (PetscPowReal(y, 4) - PetscSqr(Ly) * PetscSqr(y));
  PetscCall(PetscLogFlops(9));
  PetscFunctionReturn(PETSC_SUCCESS);
}
static PetscErrorCode MMSForcing4(AppCtx *user, const DMDACoor2d *c, PetscScalar *f)
{
  const PetscReal Lx = 1., Ly = 1.;
  PetscReal       x = PetscRealPart(c->x), y = PetscRealPart(c->y);

  PetscFunctionBeginUser;
  f[0] = (2 * PetscSqr(x) * (PetscSqr(x) - PetscSqr(Lx)) * (PetscSqr(Ly) - 6 * PetscSqr(y)) + 2 * PetscSqr(y) * (PetscSqr(Lx) - 6 * PetscSqr(x)) * (PetscSqr(y) - PetscSqr(Ly)) - user->param * PetscExpReal((PetscPowReal(x, 4) - PetscSqr(Lx) * PetscSqr(x)) * (PetscPowReal(y, 4) - PetscSqr(Ly) * PetscSqr(y))));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/* ------------------------------------------------------------------- */
/*
   FormFunctionLocal - Evaluates nonlinear function, F(x) on local process patch

 */
static PetscErrorCode FormFunctionLocal(DMDALocalInfo *info, PetscScalar **x, PetscScalar **f, AppCtx *user)
{
  PetscInt    i, j;
  PetscReal   lambda, hx, hy, hxdhy, hydhx;
  PetscScalar u, ue, uw, un, us, uxx, uyy, mms_solution, mms_forcing;
  DMDACoor2d  c;

  PetscFunctionBeginUser;
  lambda = user->param;
  hx     = 1.0 / (PetscReal)(info->mx - 1);
  hy     = 1.0 / (PetscReal)(info->my - 1);
  hxdhy  = hx / hy;
  hydhx  = hy / hx;
  /*
     Compute function over the locally owned part of the grid
  */
  for (j = info->ys; j < info->ys + info->ym; j++) {
    for (i = info->xs; i < info->xs + info->xm; i++) {
      if (i == 0 || j == 0 || i == info->mx - 1 || j == info->my - 1) {
        c.x = i * hx;
        c.y = j * hy;
        PetscCall(user->mms_solution(user, &c, &mms_solution));
        f[j][i] = 2.0 * (hydhx + hxdhy) * (x[j][i] - mms_solution);
      } else {
        u  = x[j][i];
        uw = x[j][i - 1];
        ue = x[j][i + 1];
        un = x[j - 1][i];
        us = x[j + 1][i];

        /* Enforce boundary conditions at neighboring points -- setting these values causes the Jacobian to be symmetric. */
        if (i - 1 == 0) {
          c.x = (i - 1) * hx;
          c.y = j * hy;
          PetscCall(user->mms_solution(user, &c, &uw));
        }
        if (i + 1 == info->mx - 1) {
          c.x = (i + 1) * hx;
          c.y = j * hy;
          PetscCall(user->mms_solution(user, &c, &ue));
        }
        if (j - 1 == 0) {
          c.x = i * hx;
          c.y = (j - 1) * hy;
          PetscCall(user->mms_solution(user, &c, &un));
        }
        if (j + 1 == info->my - 1) {
          c.x = i * hx;
          c.y = (j + 1) * hy;
          PetscCall(user->mms_solution(user, &c, &us));
        }

        uxx         = (2.0 * u - uw - ue) * hydhx;
        uyy         = (2.0 * u - un - us) * hxdhy;
        mms_forcing = 0;
        c.x         = i * hx;
        c.y         = j * hy;
        if (user->mms_forcing) PetscCall(user->mms_forcing(user, &c, &mms_forcing));
        f[j][i] = uxx + uyy - hx * hy * (lambda * PetscExpScalar(u) + mms_forcing);
      }
    }
  }
  PetscCall(PetscLogFlops(11.0 * info->ym * info->xm));
  PetscFunctionReturn(PETSC_SUCCESS);
}

/* FormObjectiveLocal - Evaluates nonlinear function, F(x) on local process patch */
static PetscErrorCode FormObjectiveLocal(DMDALocalInfo *info, PetscScalar **x, PetscReal *obj, AppCtx *user)
{
  PetscInt    i, j;
  PetscReal   lambda, hx, hy, hxdhy, hydhx, sc, lobj = 0;
  PetscScalar u, ue, uw, un, us, uxux, uyuy;
  MPI_Comm    comm;

  PetscFunctionBeginUser;
  *obj = 0;
  PetscCall(PetscObjectGetComm((PetscObject)info->da, &comm));
  lambda = user->param;
  hx     = 1.0 / (PetscReal)(info->mx - 1);
  hy     = 1.0 / (PetscReal)(info->my - 1);
  sc     = hx * hy * lambda;
  hxdhy  = hx / hy;
  hydhx  = hy / hx;
  /*
     Compute function over the locally owned part of the grid
  */
  for (j = info->ys; j < info->ys + info->ym; j++) {
    for (i = info->xs; i < info->xs + info->xm; i++) {
      if (i == 0 || j == 0 || i == info->mx - 1 || j == info->my - 1) {
        lobj += PetscRealPart((hydhx + hxdhy) * x[j][i] * x[j][i]);
      } else {
        u  = x[j][i];
        uw = x[j][i - 1];
        ue = x[j][i + 1];
        un = x[j - 1][i];
        us = x[j + 1][i];

        if (i - 1 == 0) uw = 0.;
        if (i + 1 == info->mx - 1) ue = 0.;
        if (j - 1 == 0) un = 0.;
        if (j + 1 == info->my - 1) us = 0.;

        /* F[u] = 1/2\int_{\omega}\nabla^2u(x)*u(x)*dx */

        uxux = u * (2. * u - ue - uw) * hydhx;
        uyuy = u * (2. * u - un - us) * hxdhy;

        lobj += PetscRealPart(0.5 * (uxux + uyuy) - sc * PetscExpScalar(u));
      }
    }
  }
  PetscCall(PetscLogFlops(12.0 * info->ym * info->xm));
  *obj = lobj;
  PetscFunctionReturn(PETSC_SUCCESS);
}

/*
   FormJacobianLocal - Evaluates Jacobian matrix on local process patch
*/
static PetscErrorCode FormJacobianLocal(DMDALocalInfo *info, PetscScalar **x, Mat jac, Mat jacpre, AppCtx *user)
{
  PetscInt     i, j, k;
  MatStencil   col[5], row;
  PetscScalar  lambda, v[5], hx, hy, hxdhy, hydhx, sc;
  DM           coordDA;
  Vec          coordinates;
  DMDACoor2d **coords;

  PetscFunctionBeginUser;
  lambda = user->param;
  /* Extract coordinates */
  PetscCall(DMGetCoordinateDM(info->da, &coordDA));
  PetscCall(DMGetCoordinates(info->da, &coordinates));
  PetscCall(DMDAVecGetArray(coordDA, coordinates, &coords));
  hx = info->xm > 1 ? PetscRealPart(coords[info->ys][info->xs + 1].x) - PetscRealPart(coords[info->ys][info->xs].x) : 1.0;
  hy = info->ym > 1 ? PetscRealPart(coords[info->ys + 1][info->xs].y) - PetscRealPart(coords[info->ys][info->xs].y) : 1.0;
  PetscCall(DMDAVecRestoreArray(coordDA, coordinates, &coords));
  hxdhy = hx / hy;
  hydhx = hy / hx;
  sc    = hx * hy * lambda;

  /*
     Compute entries for the locally owned part of the Jacobian.
      - Currently, all PETSc parallel matrix formats are partitioned by
        contiguous chunks of rows across the processors.
      - Each processor needs to insert only elements that it owns
        locally (but any non-local elements will be sent to the
        appropriate processor during matrix assembly).
      - Here, we set all entries for a particular row at once.
      - We can set matrix entries either using either
        MatSetValuesLocal() or MatSetValues(), as discussed above.
  */
  for (j = info->ys; j < info->ys + info->ym; j++) {
    for (i = info->xs; i < info->xs + info->xm; i++) {
      row.j = j;
      row.i = i;
      /* boundary points */
      if (i == 0 || j == 0 || i == info->mx - 1 || j == info->my - 1) {
        v[0] = 2.0 * (hydhx + hxdhy);
        PetscCall(MatSetValuesStencil(jacpre, 1, &row, 1, &row, v, INSERT_VALUES));
      } else {
        k = 0;
        /* interior grid points */
        if (j - 1 != 0) {
          v[k]     = -hxdhy;
          col[k].j = j - 1;
          col[k].i = i;
          k++;
        }
        if (i - 1 != 0) {
          v[k]     = -hydhx;
          col[k].j = j;
          col[k].i = i - 1;
          k++;
        }

        v[k]     = 2.0 * (hydhx + hxdhy) - sc * PetscExpScalar(x[j][i]);
        col[k].j = row.j;
        col[k].i = row.i;
        k++;

        if (i + 1 != info->mx - 1) {
          v[k]     = -hydhx;
          col[k].j = j;
          col[k].i = i + 1;
          k++;
        }
        if (j + 1 != info->mx - 1) {
          v[k]     = -hxdhy;
          col[k].j = j + 1;
          col[k].i = i;
          k++;
        }
        PetscCall(MatSetValuesStencil(jacpre, 1, &row, k, col, v, INSERT_VALUES));
      }
    }
  }

  /*
     Assemble matrix, using the 2-step process:
       MatAssemblyBegin(), MatAssemblyEnd().
  */
  PetscCall(MatAssemblyBegin(jacpre, MAT_FINAL_ASSEMBLY));
  PetscCall(MatAssemblyEnd(jacpre, MAT_FINAL_ASSEMBLY));
  /*
     Tell the matrix we will never add a new nonzero location to the
     matrix. If we do, it will generate an error.
  */
  PetscCall(MatSetOption(jac, MAT_NEW_NONZERO_LOCATION_ERR, PETSC_TRUE));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode FormFunctionMatlab(SNES snes, Vec X, Vec F, void *ptr)
{
#if PetscDefined(HAVE_MATLAB)
  AppCtx   *user = (AppCtx *)ptr;
  PetscInt  Mx, My;
  PetscReal lambda, hx, hy;
  Vec       localX, localF;
  MPI_Comm  comm;
  DM        da;

  PetscFunctionBeginUser;
  PetscCall(SNESGetDM(snes, &da));
  PetscCall(DMGetLocalVector(da, &localX));
  PetscCall(DMGetLocalVector(da, &localF));
  PetscCall(PetscObjectSetName((PetscObject)localX, "localX"));
  PetscCall(PetscObjectSetName((PetscObject)localF, "localF"));
  PetscCall(DMDAGetInfo(da, PETSC_IGNORE, &Mx, &My, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE));

  lambda = user->param;
  hx     = 1.0 / (PetscReal)(Mx - 1);
  hy     = 1.0 / (PetscReal)(My - 1);

  PetscCall(PetscObjectGetComm((PetscObject)snes, &comm));
  /*
     Scatter ghost points to local vector,using the 2-step process
        DMGlobalToLocalBegin(),DMGlobalToLocalEnd().
     By placing code between these two statements, computations can be
     done while messages are in transition.
  */
  PetscCall(DMGlobalToLocalBegin(da, X, INSERT_VALUES, localX));
  PetscCall(DMGlobalToLocalEnd(da, X, INSERT_VALUES, localX));
  PetscCall(PetscMatlabEnginePut(PETSC_MATLAB_ENGINE_(comm), (PetscObject)localX));
  PetscCall(PetscMatlabEngineEvaluate(PETSC_MATLAB_ENGINE_(comm), "localF=ex5m(localX,%18.16e,%18.16e,%18.16e)", (double)hx, (double)hy, (double)lambda));
  PetscCall(PetscMatlabEngineGet(PETSC_MATLAB_ENGINE_(comm), (PetscObject)localF));

  /*
     Insert values into global vector
  */
  PetscCall(DMLocalToGlobalBegin(da, localF, INSERT_VALUES, F));
  PetscCall(DMLocalToGlobalEnd(da, localF, INSERT_VALUES, F));
  PetscCall(DMRestoreLocalVector(da, &localX));
  PetscCall(DMRestoreLocalVector(da, &localF));
  PetscFunctionReturn(PETSC_SUCCESS);
#else
  return PETSC_SUCCESS; /* Never called */
#endif
}

/* ------------------------------------------------------------------- */
/*
      Applies some sweeps on nonlinear Gauss-Seidel on each process

 */
static PetscErrorCode NonlinearGS(SNES snes, Vec X, Vec B, PetscCtx ctx)
{
  PetscInt      i, j, k, Mx, My, xs, ys, xm, ym, its, tot_its, sweeps, l;
  PetscReal     lambda, hx, hy, hxdhy, hydhx, sc;
  PetscScalar **x, **b, bij, F, F0 = 0, J, u, un, us, ue, eu, uw, uxx, uyy, y;
  PetscReal     atol, rtol, stol;
  DM            da;
  AppCtx       *user;
  Vec           localX, localB;

  PetscFunctionBeginUser;
  tot_its = 0;
  PetscCall(SNESNGSGetSweeps(snes, &sweeps));
  PetscCall(SNESNGSGetTolerances(snes, &atol, &rtol, &stol, &its));
  PetscCall(SNESGetDM(snes, &da));
  PetscCall(DMGetApplicationContext(da, &user));

  PetscCall(DMDAGetInfo(da, PETSC_IGNORE, &Mx, &My, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE, PETSC_IGNORE));

  lambda = user->param;
  hx     = 1.0 / (PetscReal)(Mx - 1);
  hy     = 1.0 / (PetscReal)(My - 1);
  sc     = hx * hy * lambda;
  hxdhy  = hx / hy;
  hydhx  = hy / hx;

  PetscCall(DMGetLocalVector(da, &localX));
  if (B) PetscCall(DMGetLocalVector(da, &localB));
  for (l = 0; l < sweeps; l++) {
    PetscCall(DMGlobalToLocalBegin(da, X, INSERT_VALUES, localX));
    PetscCall(DMGlobalToLocalEnd(da, X, INSERT_VALUES, localX));
    if (B) {
      PetscCall(DMGlobalToLocalBegin(da, B, INSERT_VALUES, localB));
      PetscCall(DMGlobalToLocalEnd(da, B, INSERT_VALUES, localB));
    }
    /*
     Get a pointer to vector data.
     - For default PETSc vectors, VecGetArray() returns a pointer to
     the data array.  Otherwise, the routine is implementation dependent.
     - You MUST call VecRestoreArray() when you no longer need access to
     the array.
     */
    PetscCall(DMDAVecGetArray(da, localX, &x));
    if (B) PetscCall(DMDAVecGetArray(da, localB, &b));
    /*
     Get local grid boundaries (for 2-dimensional DMDA):
     xs, ys   - starting grid indices (no ghost points)
     xm, ym   - widths of local grid (no ghost points)
     */
    PetscCall(DMDAGetCorners(da, &xs, &ys, NULL, &xm, &ym, NULL));

    for (j = ys; j < ys + ym; j++) {
      for (i = xs; i < xs + xm; i++) {
        if (i == 0 || j == 0 || i == Mx - 1 || j == My - 1) {
          /* boundary conditions are all zero Dirichlet */
          x[j][i] = 0.0;
        } else {
          if (B) bij = b[j][i];
          else bij = 0.;

          u  = x[j][i];
          un = x[j - 1][i];
          us = x[j + 1][i];
          ue = x[j][i - 1];
          uw = x[j][i + 1];

          for (k = 0; k < its; k++) {
            eu  = PetscExpScalar(u);
            uxx = (2.0 * u - ue - uw) * hydhx;
            uyy = (2.0 * u - un - us) * hxdhy;
            F   = uxx + uyy - sc * eu - bij;
            if (k == 0) F0 = F;
            J = 2.0 * (hydhx + hxdhy) - sc * eu;
            y = F / J;
            u -= y;
            tot_its++;

            if (atol > PetscAbsReal(PetscRealPart(F)) || rtol * PetscAbsReal(PetscRealPart(F0)) > PetscAbsReal(PetscRealPart(F)) || stol * PetscAbsReal(PetscRealPart(u)) > PetscAbsReal(PetscRealPart(y))) break;
          }
          x[j][i] = u;
        }
      }
    }
    /*
     Restore vector
     */
    PetscCall(DMDAVecRestoreArray(da, localX, &x));
    PetscCall(DMLocalToGlobalBegin(da, localX, INSERT_VALUES, X));
    PetscCall(DMLocalToGlobalEnd(da, localX, INSERT_VALUES, X));
  }
  PetscCall(PetscLogFlops(tot_its * (21.0)));
  PetscCall(DMRestoreLocalVector(da, &localX));
  if (B) {
    PetscCall(DMDAVecRestoreArray(da, localB, &b));
    PetscCall(DMRestoreLocalVector(da, &localB));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

int main(int argc, char **argv)
{
  SNES      snes; /* nonlinear solver */
  Vec       x;    /* solution vector */
  AppCtx    user; /* user-defined work context */
  PetscInt  its;  /* iterations for convergence */
  PetscReal bratu_lambda_max = 6.81;
  PetscReal bratu_lambda_min = 0.;
  PetscInt  MMS              = 1;
  PetscBool flg              = PETSC_FALSE, setMMS;
  DM        da;
  Vec       r = NULL;
  KSP       ksp;
  PetscInt  lits, slits;

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Initialize program
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Initialize problem parameters
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  user.param = 6.0;
  PetscCall(PetscOptionsGetReal(NULL, NULL, "-par", &user.param, NULL));
  PetscCheck(user.param <= bratu_lambda_max && user.param >= bratu_lambda_min, PETSC_COMM_SELF, PETSC_ERR_ARG_OUTOFRANGE, "Lambda, %g, is out of range, [%g, %g]", (double)user.param, (double)bratu_lambda_min, (double)bratu_lambda_max);
  PetscCall(PetscOptionsGetInt(NULL, NULL, "-mms", &MMS, &setMMS));
  if (MMS == 3) {
    PetscInt mPar = 2, nPar = 1;
    PetscCall(PetscOptionsGetInt(NULL, NULL, "-m_par", &mPar, NULL));
    PetscCall(PetscOptionsGetInt(NULL, NULL, "-n_par", &nPar, NULL));
    user.m = PetscPowInt(2, mPar);
    user.n = PetscPowInt(2, nPar);
  }

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create nonlinear solver context
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(SNESCreate(PETSC_COMM_WORLD, &snes));
  PetscCall(SNESSetCountersReset(snes, PETSC_FALSE));
  PetscCall(SNESSetNGS(snes, NonlinearGS, NULL));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create distributed array (DMDA) to manage parallel grid and vectors
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(DMDACreate2d(PETSC_COMM_WORLD, DM_BOUNDARY_NONE, DM_BOUNDARY_NONE, DMDA_STENCIL_STAR, 4, 4, PETSC_DECIDE, PETSC_DECIDE, 1, 1, NULL, NULL, &da));
  PetscCall(DMSetFromOptions(da));
  PetscCall(DMSetUp(da));
  PetscCall(DMDASetUniformCoordinates(da, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0));
  PetscCall(DMSetApplicationContext(da, &user));
  PetscCall(SNESSetDM(snes, da));
  /*  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Extract global vectors from DMDA; then duplicate for remaining
     vectors that are the same types
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(DMCreateGlobalVector(da, &x));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Set local function evaluation routine
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  switch (MMS) {
  case 0:
    user.mms_solution = ZeroBCSolution;
    user.mms_forcing  = NULL;
    break;
  case 1:
    user.mms_solution = MMSSolution1;
    user.mms_forcing  = MMSForcing1;
    break;
  case 2:
    user.mms_solution = MMSSolution2;
    user.mms_forcing  = MMSForcing2;
    break;
  case 3:
    user.mms_solution = MMSSolution3;
    user.mms_forcing  = MMSForcing3;
    break;
  case 4:
    user.mms_solution = MMSSolution4;
    user.mms_forcing  = MMSForcing4;
    break;
  default:
    SETERRQ(PETSC_COMM_WORLD, PETSC_ERR_USER, "Unknown MMS type %" PetscInt_FMT, MMS);
  }
  PetscCall(DMDASNESSetFunctionLocal(da, INSERT_VALUES, (DMDASNESFunctionFn *)FormFunctionLocal, &user));
  PetscCall(PetscOptionsGetBool(NULL, NULL, "-fd", &flg, NULL));
  if (!flg) PetscCall(DMDASNESSetJacobianLocal(da, (DMDASNESJacobianFn *)FormJacobianLocal, &user));

  PetscCall(PetscOptionsGetBool(NULL, NULL, "-obj", &flg, NULL));
  if (flg) PetscCall(DMDASNESSetObjectiveLocal(da, (DMDASNESObjectiveFn *)FormObjectiveLocal, &user));

  if (PetscDefined(HAVE_MATLAB)) {
    PetscBool matlab_function = PETSC_FALSE;
    PetscCall(PetscOptionsGetBool(NULL, NULL, "-matlab_function", &matlab_function, 0));
    if (matlab_function) {
      PetscCall(VecDuplicate(x, &r));
      PetscCall(SNESSetFunction(snes, r, FormFunctionMatlab, &user));
    }
  }

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Customize nonlinear solver; set runtime options
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(SNESSetFromOptions(snes));

  PetscCall(FormInitialGuess(da, &user, x));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Solve nonlinear system
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(SNESSolve(snes, NULL, x));
  PetscCall(SNESGetIterationNumber(snes, &its));

  PetscCall(SNESGetLinearSolveIterations(snes, &slits));
  PetscCall(SNESGetKSP(snes, &ksp));
  PetscCall(KSPGetTotalIterations(ksp, &lits));
  PetscCheck(lits == slits, PETSC_COMM_WORLD, PETSC_ERR_PLIB, "Number of total linear iterations reported by SNES %" PetscInt_FMT " does not match reported by KSP %" PetscInt_FMT, slits, lits);
  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     If using MMS, check the l_2 error
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  if (setMMS) {
    Vec       e;
    PetscReal errorl2, errorinf;
    PetscInt  N;

    PetscCall(VecDuplicate(x, &e));
    PetscCall(PetscObjectViewFromOptions((PetscObject)x, NULL, "-sol_view"));
    PetscCall(FormExactSolution(da, &user, e));
    PetscCall(PetscObjectViewFromOptions((PetscObject)e, NULL, "-exact_view"));
    PetscCall(VecAXPY(e, -1.0, x));
    PetscCall(PetscObjectViewFromOptions((PetscObject)e, NULL, "-error_view"));
    PetscCall(VecNorm(e, NORM_2, &errorl2));
    PetscCall(VecNorm(e, NORM_INFINITY, &errorinf));
    PetscCall(VecGetSize(e, &N));
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "N: %" PetscInt_FMT " error L2 %g inf %g\n", N, (double)(errorl2 / PetscSqrtReal((PetscReal)N)), (double)errorinf));
    PetscCall(VecDestroy(&e));
    PetscCall(PetscLogEventSetDof(SNES_Solve, 0, N));
    PetscCall(PetscLogEventSetError(SNES_Solve, 0, errorl2 / PetscSqrtReal(N)));
  }

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Free work space.  All PETSc objects should be destroyed when they
     are no longer needed.
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(VecDestroy(&r));
  PetscCall(VecDestroy(&x));
  PetscCall(SNESDestroy(&snes));
  PetscCall(DMDestroy(&da));
  PetscCall(PetscFinalize());
  return 0;
}

/*TEST

   test:
     suffix: asm_0
     requires: !single
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 2 -pc_asm_overlap 0 -pc_asm_local_type additive -sub_pc_type lu

   test:
     suffix: msm_0
     requires: !single
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 2 -pc_asm_overlap 0 -pc_asm_local_type multiplicative -sub_pc_type lu

   test:
     suffix: asm_1
     requires: !single
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 2 -pc_asm_overlap 0 -pc_asm_local_type additive -sub_pc_type lu -da_grid_x 8

   test:
     suffix: msm_1
     requires: !single
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 2 -pc_asm_overlap 0 -pc_asm_local_type multiplicative -sub_pc_type lu -da_grid_x 8

   test:
     suffix: asm_2
     requires: !single
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 3 -pc_asm_overlap 0 -pc_asm_local_type additive -sub_pc_type lu -da_grid_x 8

   test:
     suffix: msm_2
     requires: !single
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 3 -pc_asm_overlap 0 -pc_asm_local_type multiplicative -sub_pc_type lu -da_grid_x 8

   test:
     suffix: asm_3
     requires: !single
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 4 -pc_asm_overlap 0 -pc_asm_local_type additive -sub_pc_type lu -da_grid_x 8

   test:
     suffix: msm_3
     requires: !single
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 4 -pc_asm_overlap 0 -pc_asm_local_type multiplicative -sub_pc_type lu -da_grid_x 8

   test:
     suffix: asm_4
     requires: !single
     nsize: 2
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 2 -pc_asm_overlap 0 -pc_asm_local_type additive -sub_pc_type lu -da_grid_x 8

   test:
     suffix: msm_4
     requires: !single
     nsize: 2
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 2 -pc_asm_overlap 0 -pc_asm_local_type multiplicative -sub_pc_type lu -da_grid_x 8

   test:
     suffix: asm_5
     requires: !single
     nsize: 2
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 4 -pc_asm_overlap 0 -pc_asm_local_type additive -sub_pc_type lu -da_grid_x 8

   test:
     suffix: msm_5
     requires: !single
     nsize: 2
     args: -mms 1 -par 0.0 -snes_monitor_short -snes_converged_reason -snes_view -ksp_rtol 1.0e-9 -ksp_monitor_short -ksp_type richardson -pc_type asm -pc_asm_blocks 4 -pc_asm_overlap 0 -pc_asm_local_type multiplicative -sub_pc_type lu -da_grid_x 8

   test:
     args: -snes_rtol 1.e-5 -pc_type mg -ksp_monitor_short -snes_view -pc_mg_levels 3 -pc_mg_galerkin pmat -da_grid_x 17 -da_grid_y 17 -mg_levels_ksp_monitor_short -mg_levels_ksp_norm_type unpreconditioned -snes_monitor_short -mg_levels_ksp_chebyshev_esteig 0.5,1.1 -mg_levels_pc_type sor -pc_mg_type full
     requires: !single

   test:
     suffix: 2
     args: -pc_type mg -ksp_converged_reason -snes_view -pc_mg_galerkin pmat -snes_grid_sequence 3 -mg_levels_ksp_norm_type unpreconditioned -snes_monitor_short -mg_levels_ksp_chebyshev_esteig 0.5,1.1 -mg_levels_pc_type sor -pc_mg_type full -ksp_atol 0

   test:
     suffix: 3
     nsize: 2
     args: -snes_grid_sequence 2 -snes_mf_operator -snes_converged_reason -snes_view -pc_type mg -snes_atol 0 -snes_rtol 1.e-2
     filter: grep -v "otal number of function evaluations"

   test:
     suffix: 4
     nsize: 2
     args: -snes_grid_sequence 2 -snes_monitor_short -ksp_converged_reason -snes_converged_reason -snes_view -pc_type mg -snes_atol 0 -ksp_atol 0

   test:
     suffix: 5_anderson
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type anderson

   test:
     suffix: 5_aspin
     nsize: 4
     args: -snes_monitor_short -ksp_monitor_short -snes_converged_reason -da_refine 4 -da_overlap 3 -snes_type aspin -snes_view -npc_sub_pc_type lu -npc_sub_ksp_type preonly

   test:
     suffix: 5_broyden
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type qn -snes_qn_type broyden -snes_qn_m 10

   test:
     suffix: 5_fas
     args: -fas_coarse_snes_max_it 1 -fas_coarse_pc_type lu -fas_coarse_ksp_type preonly -snes_monitor_short -snes_type fas -fas_coarse_ksp_type richardson -da_refine 6
     requires: !single

   test:
     suffix: 5_fas_additive
     args: -fas_coarse_snes_max_it 1 -fas_coarse_pc_type lu -fas_coarse_ksp_type preonly -snes_monitor_short -snes_type fas -fas_coarse_ksp_type richardson -da_refine 6 -snes_fas_type additive -snes_max_it 50 -snes_linesearch_maxlambda 2.0

   test:
     suffix: 5_fas_monitor
     args: -da_refine 1 -snes_type fas -snes_fas_monitor
     requires: !single

   test:
     suffix: 5_ls
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type newtonls

   test:
     suffix: 5_ls_sell_sor
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type newtonls -dm_mat_type sell -pc_type sor
     output_file: output/ex5_5_ls.out

   test:
     suffix: 5_nasm
     nsize: 4
     args: -snes_monitor_short -snes_converged_reason -da_refine 4 -da_overlap 3 -snes_type nasm -snes_nasm_type restrict -snes_max_it 10

   test:
     suffix: 5_ncg
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type ncg -snes_ncg_type fr

   test:
     suffix: 5_newton_asm_dmda
     nsize: 4
     args: -snes_monitor_short -ksp_monitor_short -snes_converged_reason -da_refine 4 -da_overlap 3 -snes_type newtonls -pc_type asm -pc_asm_dm_subdomains -malloc_dump
     requires: !single

   test:
     suffix: 5_newton_gasm_dmda
     nsize: 4
     args: -snes_monitor_short -ksp_monitor_short -snes_converged_reason -da_refine 4 -da_overlap 3 -snes_type newtonls -pc_type gasm -malloc_dump
     requires: !single

   test:
     suffix: 5_ngmres
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type ngmres -snes_ngmres_m 10

   test:
     suffix: 5_ngmres_fas
     args: -snes_rtol 1.e-4 -snes_type ngmres -npc_fas_coarse_snes_max_it 1 -npc_fas_coarse_snes_type newtonls -npc_fas_coarse_pc_type lu -npc_fas_coarse_ksp_type preonly -snes_ngmres_m 10 -snes_monitor_short -npc_snes_max_it 1 -npc_snes_type fas -npc_fas_coarse_ksp_type richardson -da_refine 6

   test:
     suffix: 5_ngmres_ngs
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type ngmres -npc_snes_type ngs -npc_snes_max_it 1

   test:
     suffix: 5_ngmres_nrichardson
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type ngmres -snes_ngmres_m 10 -npc_snes_type nrichardson -npc_snes_max_it 3
     output_file: output/ex5_5_ngmres_richardson.out

   test:
     suffix: 5_nrichardson
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type nrichardson

   test:
     suffix: 5_qn
     args: -da_grid_x 81 -da_grid_y 81 -snes_monitor_short -snes_max_it 50 -par 6.0 -snes_type qn -snes_linesearch_type cp -snes_qn_m 10

   test:
     suffix: 6
     nsize: 4
     args: -snes_converged_reason -ksp_converged_reason -da_grid_x 129 -da_grid_y 129 -pc_type mg -pc_mg_levels 8 -mg_levels_ksp_type chebyshev -mg_levels_ksp_chebyshev_esteig 0,0.5,0,1.1 -mg_levels_ksp_max_it 2

   test:
     requires: complex !single
     suffix: complex
     args: -snes_mf_operator -mat_mffd_complex -snes_monitor

   test:
     requires: !single
     suffix: 7_ksp_view_pre
     args: -pc_type gamg -ksp_view_pre

   test:
     requires: !single
     suffix: hem_view_detailed
     args: -pc_type gamg -ksp_view ::ascii_info_detail -pc_gamg_mat_coarsen_type hem

   test:
     requires: !single
     suffix: mis_view_detailed
     args: -pc_type gamg -ksp_view ::ascii_info_detail -pc_gamg_mat_coarsen_type mis

   test:
     requires: !single
     suffix: snes_test_jacobian
     nsize: 4
     args: -snes_test_jacobian -snes_test_jacobian_view

TEST*/
````

## SNES ex56.c

- Selected by: Tutorials by physics
- Rendered listing: <https://petsc.org/release/src/snes/tutorials/ex56.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/snes/tutorials/ex56.c>

````c
/* Portions of this code are under:
   Copyright (C) 2022 Advanced Micro Devices, Inc. All rights reserved.
*/
static char help[] = "3D tensor hexahedra & 3D Laplacian displacement finite element formulation\n\
of linear elasticity.  E=1.0, nu=1/3.\n\
Unit cube domain with Dirichlet boundary\n\n";

#include <petscdmplex.h>
#include <petscsnes.h>
#include <petscds.h>
#include <petscdmforest.h>

static PetscReal s_soft_alpha = 0.01;
static PetscReal s_mu         = 0.4;
static PetscReal s_lambda     = 0.4;

static void f0_bd_u_3d(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = 1;     /* x direction pull */
  f0[1] = -x[2]; /* add a twist around x-axis */
  f0[2] = x[1];
}

static void f1_bd_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscInt Ncomp = dim;
  PetscInt       comp, d;
  for (comp = 0; comp < Ncomp; ++comp) {
    for (d = 0; d < dim; ++d) f1[comp * dim + d] = 0.0;
  }
}

/* gradU[comp*dim+d] = {u_x, u_y} or {u_x, u_y, u_z} */
static void f1_u_3d_alpha(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  PetscReal trace, mu = s_mu, lambda = s_lambda, rad;
  PetscInt  i, j;
  for (i = 0, rad = 0.; i < dim; i++) {
    PetscReal t = x[i];
    rad += t * t;
  }
  rad = PetscSqrtReal(rad);
  if (rad > 0.25) {
    mu *= s_soft_alpha;
    lambda *= s_soft_alpha; /* we could keep the bulk the same like rubberish */
  }
  for (i = 0, trace = 0; i < dim; ++i) trace += PetscRealPart(u_x[i * dim + i]);
  for (i = 0; i < dim; ++i) {
    for (j = 0; j < dim; ++j) f1[i * dim + j] = mu * (u_x[i * dim + j] + u_x[j * dim + i]);
    f1[i * dim + i] += lambda * trace;
  }
}

/* gradU[comp*dim+d] = {u_x, u_y} or {u_x, u_y, u_z} */
static void f1_u_3d(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  PetscReal trace, mu = s_mu, lambda = s_lambda;
  PetscInt  i, j;
  for (i = 0, trace = 0; i < dim; ++i) trace += PetscRealPart(u_x[i * dim + i]);
  for (i = 0; i < dim; ++i) {
    for (j = 0; j < dim; ++j) f1[i * dim + j] = mu * (u_x[i * dim + j] + u_x[j * dim + i]);
    f1[i * dim + i] += lambda * trace;
  }
}

static void f1_u_lap(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) f1[d] = u_x[d];
}

/* 3D elasticity */
#define IDX(ii, jj, kk, ll) (27 * ii + 9 * jj + 3 * kk + ll)

void g3_uu_3d_private(PetscScalar g3[], const PetscReal mu, const PetscReal lambda)
{
  if (1) {
    g3[0] += lambda;
    g3[0] += mu;
    g3[0] += mu;
    g3[4] += lambda;
    g3[8] += lambda;
    g3[10] += mu;
    g3[12] += mu;
    g3[20] += mu;
    g3[24] += mu;
    g3[28] += mu;
    g3[30] += mu;
    g3[36] += lambda;
    g3[40] += lambda;
    g3[40] += mu;
    g3[40] += mu;
    g3[44] += lambda;
    g3[50] += mu;
    g3[52] += mu;
    g3[56] += mu;
    g3[60] += mu;
    g3[68] += mu;
    g3[70] += mu;
    g3[72] += lambda;
    g3[76] += lambda;
    g3[80] += lambda;
    g3[80] += mu;
    g3[80] += mu;
  } else {
    int        i, j, k, l;
    static int cc = -1;
    cc++;
    for (i = 0; i < 3; ++i) {
      for (j = 0; j < 3; ++j) {
        for (k = 0; k < 3; ++k) {
          for (l = 0; l < 3; ++l) {
            if (k == l && i == j) g3[IDX(i, j, k, l)] += lambda;
            if (i == k && j == l) g3[IDX(i, j, k, l)] += mu;
            if (i == l && j == k) g3[IDX(i, j, k, l)] += mu;
            if (k == l && i == j && !cc) (void)PetscPrintf(PETSC_COMM_WORLD, "g3[%d] += lambda;\n", IDX(i, j, k, l));
            if (i == k && j == l && !cc) (void)PetscPrintf(PETSC_COMM_WORLD, "g3[%d] += mu;\n", IDX(i, j, k, l));
            if (i == l && j == k && !cc) (void)PetscPrintf(PETSC_COMM_WORLD, "g3[%d] += mu;\n", IDX(i, j, k, l));
          }
        }
      }
    }
  }
}

static void g3_uu_3d_alpha(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  PetscReal mu = s_mu, lambda = s_lambda, rad;
  PetscInt  i;
  for (i = 0, rad = 0.; i < dim; i++) {
    PetscReal t = x[i];
    rad += t * t;
  }
  rad = PetscSqrtReal(rad);
  if (rad > 0.25) {
    mu *= s_soft_alpha;
    lambda *= s_soft_alpha; /* we could keep the bulk the same like rubberish */
  }
  g3_uu_3d_private(g3, mu, lambda);
}

static void g3_uu_3d(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  g3_uu_3d_private(g3, s_mu, s_lambda);
}

static void g3_lap(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) g3[d * dim + d] = 1.0;
}

static void g3_lap_alpha(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  PetscReal lambda = 1, rad;
  PetscInt  i;
  for (i = 0, rad = 0.; i < dim; i++) {
    PetscReal t = x[i];
    rad += t * t;
  }
  rad = PetscSqrtReal(rad);
  if (rad > 0.25) lambda *= s_soft_alpha; /* we could keep the bulk the same like rubberish */
  for (int d = 0; d < dim; ++d) g3[d * dim + d] = lambda;
}

static void f0_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscInt Ncomp = dim;
  PetscInt       comp;

  for (comp = 0; comp < Ncomp; ++comp) f0[comp] = 0.0;
}

/* PI_i (x_i^4 - x_i^2) */
static void f0_u_x4(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  for (int comp = 0; comp < Nf; ++comp) {
    f0[comp] = 1e5;
    for (int i = 0; i < dim; ++i) f0[comp] *= /* (comp+1)* */ (x[i] * x[i] * x[i] * x[i] - x[i] * x[i]); /* assumes (0,1]^D domain */
  }
}

PetscErrorCode zero(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *u, PetscCtx ctx)
{
  const PetscInt Ncomp = dim;
  PetscInt       comp;

  for (comp = 0; comp < Ncomp; ++comp) u[comp] = 0;
  return PETSC_SUCCESS;
}

int main(int argc, char **args)
{
  Mat           Amat;
  SNES          snes;
  KSP           ksp;
  MPI_Comm      comm;
  PetscMPIInt   rank;
  PetscLogStage stage[17];
  PetscBool     test_nonzero_cols = PETSC_FALSE, use_nearnullspace = PETSC_TRUE, attach_nearnullspace = PETSC_FALSE;
  Vec           xx, bb;
  PetscInt      iter, i, N, dim = 3, max_conv_its, sizes[7], run_type = 1, Ncomp = dim;
  DM            dm;
  PetscBool     flg;
  PetscReal     Lx, mdisp[10], err[10];

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &args, NULL, help));
  comm = PETSC_COMM_WORLD;
  PetscCallMPI(MPI_Comm_rank(comm, &rank));
  /* options */
  PetscOptionsBegin(comm, NULL, "3D bilinear Q1 elasticity options", "");
  {
    Lx           = 1.; /* or ne for rod */
    max_conv_its = 3;
    PetscCall(PetscOptionsInt("-max_conv_its", "Number of iterations in convergence study", "", max_conv_its, &max_conv_its, NULL));
    PetscCheck(max_conv_its > 0 && max_conv_its < 8, PETSC_COMM_WORLD, PETSC_ERR_USER, "Bad number of iterations for convergence test (%" PetscInt_FMT ")", max_conv_its);
    PetscCall(PetscOptionsReal("-lx", "Length of domain", "", Lx, &Lx, NULL));
    PetscCall(PetscOptionsReal("-alpha", "material coefficient inside circle", "", s_soft_alpha, &s_soft_alpha, NULL));
    PetscCall(PetscOptionsBool("-test_nonzero_cols", "nonzero test", "", test_nonzero_cols, &test_nonzero_cols, NULL));
    PetscCall(PetscOptionsBool("-use_mat_nearnullspace", "MatNearNullSpace API test", "", use_nearnullspace, &use_nearnullspace, NULL));
    PetscCall(PetscOptionsBool("-attach_mat_nearnullspace", "MatNearNullSpace API test (via MatSetNearNullSpace)", "", attach_nearnullspace, &attach_nearnullspace, NULL));
    PetscCall(PetscOptionsInt("-run_type", "0: twisting load on cantalever, 1: Elasticty convergence test on cube, 2: Laplacian, 3: soft core Laplacian", "", run_type, &run_type, NULL));
  }
  PetscOptionsEnd();
  PetscCall(PetscLogStageRegister("Mesh Setup", &stage[16]));
  for (iter = 0; iter < max_conv_its; iter++) {
    char str[] = "Solve 0";
    str[6] += iter;
    PetscCall(PetscLogStageRegister(str, &stage[iter]));
  }
  /* create DM, Plex calls DMSetup */
  PetscCall(PetscLogStagePush(stage[16]));
  PetscCall(DMCreate(comm, &dm));
  PetscCall(DMSetType(dm, DMPLEX));
  PetscCall(PetscObjectSetName((PetscObject)dm, "Mesh"));
  PetscCall(DMSetFromOptions(dm));
  PetscCall(DMPlexDistributeSetDefault(dm, PETSC_FALSE));
  PetscCall(DMGetDimension(dm, &dim));
  {
    DMLabel label;
    IS      is;
    PetscCall(DMCreateLabel(dm, "boundary"));
    PetscCall(DMGetLabel(dm, "boundary", &label));
    PetscCall(DMPlexMarkBoundaryFaces(dm, 1, label));
    if (run_type == 0) {
      PetscCall(DMGetStratumIS(dm, "boundary", 1, &is));
      PetscCall(DMCreateLabel(dm, "Faces"));
      if (is) {
        PetscInt        d, f, Nf;
        const PetscInt *faces;
        PetscInt        csize;
        PetscSection    cs;
        Vec             coordinates;
        DM              cdm;
        PetscCall(ISGetLocalSize(is, &Nf));
        PetscCall(ISGetIndices(is, &faces));
        PetscCall(DMGetCoordinatesLocal(dm, &coordinates));
        PetscCall(DMGetCoordinateDM(dm, &cdm));
        PetscCall(DMGetLocalSection(cdm, &cs));
        /* Check for each boundary face if any component of its centroid is either 0.0 or 1.0 */
        for (f = 0; f < Nf; ++f) {
          PetscReal    faceCoord;
          PetscInt     b, v;
          PetscScalar *coords = NULL;
          PetscInt     Nv;
          PetscCall(DMPlexVecGetClosure(cdm, cs, coordinates, faces[f], &csize, &coords));
          Nv = csize / dim; /* Calculate mean coordinate vector */
          for (d = 0; d < dim; ++d) {
            faceCoord = 0.0;
            for (v = 0; v < Nv; ++v) faceCoord += PetscRealPart(coords[v * dim + d]);
            faceCoord /= Nv;
            for (b = 0; b < 2; ++b) {
              if (PetscAbs(faceCoord - b) < PETSC_SMALL) { /* domain have not been set yet, still [0,1]^3 */
                PetscCall(DMSetLabelValue(dm, "Faces", faces[f], d * 2 + b + 1));
              }
            }
          }
          PetscCall(DMPlexVecRestoreClosure(cdm, cs, coordinates, faces[f], &csize, &coords));
        }
        PetscCall(ISRestoreIndices(is, &faces));
      }
      PetscCall(ISDestroy(&is));
      PetscCall(DMGetLabel(dm, "Faces", &label));
      PetscCall(DMPlexLabelComplete(dm, label));
    }
  }
  PetscCall(PetscLogStagePop());
  for (iter = 0; iter < max_conv_its; iter++) {
    PetscCall(PetscLogStagePush(stage[16]));
    /* snes */
    PetscCall(SNESCreate(comm, &snes));
    PetscCall(SNESSetDM(snes, dm));
    PetscCall(DMViewFromOptions(dm, NULL, "-dm_view"));
    /* fem */
    {
      const PetscInt components[] = {0, 1, 2};
      const PetscInt Nfid = 1, Npid = 1;
      PetscInt       fid[] = {1}; /* The fixed faces (x=0) */
      const PetscInt pid[] = {2}; /* The faces with loading (x=L_x) */
      PetscFE        fe;
      PetscDS        prob;
      DMLabel        label;

      if (run_type == 2 || run_type == 3) Ncomp = 1;
      else Ncomp = dim;
      PetscCall(PetscFECreateDefault(PETSC_COMM_SELF, dim, Ncomp, PETSC_FALSE, NULL, PETSC_DECIDE, &fe));
      PetscCall(PetscObjectSetName((PetscObject)fe, "deformation"));
      /* FEM prob */
      PetscCall(DMSetField(dm, 0, NULL, (PetscObject)fe));
      PetscCall(DMCreateDS(dm));
      PetscCall(DMGetDS(dm, &prob));
      /* setup problem */
      if (run_type == 1) { // elast
        PetscCall(PetscDSSetJacobian(prob, 0, 0, NULL, NULL, NULL, g3_uu_3d));
        PetscCall(PetscDSSetResidual(prob, 0, f0_u_x4, f1_u_3d));
      } else if (run_type == 0) { //twisted not maintained
        PetscWeakForm wf;
        PetscInt      bd, i;
        PetscCall(PetscDSSetJacobian(prob, 0, 0, NULL, NULL, NULL, g3_uu_3d_alpha));
        PetscCall(PetscDSSetResidual(prob, 0, f0_u, f1_u_3d_alpha));
        PetscCall(DMGetLabel(dm, "Faces", &label));
        PetscCall(DMAddBoundary(dm, DM_BC_NATURAL, "traction", label, Npid, pid, 0, Ncomp, components, NULL, NULL, NULL, &bd));
        PetscCall(PetscDSGetBoundary(prob, bd, &wf, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL));
        for (i = 0; i < Npid; ++i) PetscCall(PetscWeakFormSetIndexBdResidual(wf, label, pid[i], 0, 0, 0, f0_bd_u_3d, 0, f1_bd_u));
      } else if (run_type == 2) { // Laplacian
        PetscCall(PetscDSSetJacobian(prob, 0, 0, NULL, NULL, NULL, g3_lap));
        PetscCall(PetscDSSetResidual(prob, 0, f0_u_x4, f1_u_lap));
      } else if (run_type == 3) { // soft core Laplacian
        PetscCall(PetscDSSetJacobian(prob, 0, 0, NULL, NULL, NULL, g3_lap_alpha));
        PetscCall(PetscDSSetResidual(prob, 0, f0_u_x4, f1_u_lap));
      }
      /* bcs */
      if (run_type != 0) {
        PetscInt id = 1;
        PetscCall(DMGetLabel(dm, "boundary", &label));
        PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)zero, NULL, NULL, NULL));
      } else {
        PetscCall(DMGetLabel(dm, "Faces", &label));
        PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "fixed", label, Nfid, fid, 0, Ncomp, components, (PetscVoidFn *)zero, NULL, NULL, NULL));
      }
      PetscCall(PetscFEDestroy(&fe));
    }
    /* vecs & mat */
    PetscCall(DMCreateGlobalVector(dm, &xx));
    PetscCall(VecDuplicate(xx, &bb));
    PetscCall(PetscObjectSetName((PetscObject)bb, "b"));
    PetscCall(PetscObjectSetName((PetscObject)xx, "u"));
    PetscCall(DMCreateMatrix(dm, &Amat));
    PetscCall(MatSetOption(Amat, MAT_SYMMETRIC, PETSC_TRUE));        /* Some matrix kernels can take advantage of symmetry if we set this. */
    PetscCall(MatSetOption(Amat, MAT_SYMMETRY_ETERNAL, PETSC_TRUE)); /* Inform PETSc that Amat is always symmetric, so info set above isn't lost. */
    PetscCall(MatSetBlockSize(Amat, Ncomp));
    PetscCall(MatSetOption(Amat, MAT_SPD, PETSC_TRUE));
    PetscCall(MatSetOption(Amat, MAT_SPD_ETERNAL, PETSC_TRUE));
    PetscCall(VecGetSize(bb, &N));
    sizes[iter] = N;
    PetscCall(PetscInfo(snes, "%" PetscInt_FMT " global equations, %" PetscInt_FMT " vertices\n", N, N / dim));
    if ((use_nearnullspace || attach_nearnullspace) && N / dim > 1 && Ncomp > 1) {
      /* Set up the near null space (a.k.a. rigid body modes) that will be used by the multigrid preconditioner */
      DM           subdm;
      MatNullSpace nearNullSpace;
      PetscInt     fields = 0;
      PetscObject  deformation;
      PetscCall(DMCreateSubDM(dm, 1, &fields, NULL, &subdm));
      PetscCall(DMPlexCreateRigidBody(subdm, 0, &nearNullSpace));
      PetscCall(DMGetField(dm, 0, NULL, &deformation));
      PetscCall(PetscObjectCompose(deformation, "nearnullspace", (PetscObject)nearNullSpace));
      PetscCall(DMDestroy(&subdm));
      if (attach_nearnullspace) PetscCall(MatSetNearNullSpace(Amat, nearNullSpace));
      PetscCall(MatNullSpaceDestroy(&nearNullSpace)); /* created by DM and destroyed by Mat */
    }
    PetscCall(DMPlexSetSNESLocalFEM(dm, PETSC_FALSE, NULL));
    PetscCall(SNESSetJacobian(snes, Amat, Amat, NULL, NULL));
    PetscCall(SNESSetFromOptions(snes));
    PetscCall(DMSetUp(dm));
    PetscCall(PetscLogStagePop());
    PetscCall(PetscLogStagePush(stage[16]));
    /* ksp */
    PetscCall(SNESGetKSP(snes, &ksp));
    PetscCall(KSPSetComputeSingularValues(ksp, PETSC_TRUE));
    if (!use_nearnullspace) {
      PC pc;
      PetscCall(KSPGetPC(ksp, &pc));
      PetscCall(PCGAMGASMSetHEM(pc, 3)); // code coverage
    }
    /* test BCs */
    PetscCall(VecZeroEntries(xx));
    if (test_nonzero_cols) {
      if (rank == 0) PetscCall(VecSetValue(xx, 0, 1.0, INSERT_VALUES));
      PetscCall(VecAssemblyBegin(xx));
      PetscCall(VecAssemblyEnd(xx));
    }
    PetscCall(VecZeroEntries(bb));
    PetscCall(VecGetSize(bb, &i));
    sizes[iter] = i;
    PetscCall(PetscInfo(snes, "%" PetscInt_FMT " equations in vector, %" PetscInt_FMT " vertices\n", i, i / dim));
    PetscCall(PetscLogStagePop());
    /* solve */
    PetscCall(SNESComputeJacobian(snes, xx, Amat, Amat));
    PetscCall(MatViewFromOptions(Amat, NULL, "-my_mat_view"));
    PetscCall(PetscLogStagePush(stage[iter]));
    PetscCall(SNESSolve(snes, bb, xx));
    PetscCall(PetscLogStagePop());
    PetscCall(VecNorm(xx, NORM_INFINITY, &mdisp[iter]));
    {
      PetscViewer       viewer = NULL;
      PetscViewerFormat fmt;
      PetscCall(PetscOptionsCreateViewer(comm, NULL, "", "-vec_view", &viewer, &fmt, &flg));
      if (flg) {
        PetscCall(PetscViewerPushFormat(viewer, fmt));
        PetscCall(VecView(xx, viewer));
        PetscCall(VecView(bb, viewer));
        PetscCall(PetscViewerPopFormat(viewer));
      }
      PetscCall(PetscViewerDestroy(&viewer));
    }
    /* Free work space */
    PetscCall(SNESDestroy(&snes));
    PetscCall(VecDestroy(&xx));
    PetscCall(VecDestroy(&bb));
    PetscCall(MatDestroy(&Amat));
    if (iter + 1 < max_conv_its) {
      DM newdm;
      PetscCall(DMViewFromOptions(dm, NULL, "-my_dm_view"));
      PetscCall(DMRefine(dm, comm, &newdm));
      if (rank == -1) {
        PetscDS prob;
        PetscCall(DMGetDS(dm, &prob));
        PetscCall(PetscDSViewFromOptions(prob, NULL, "-ds_view"));
        PetscCall(DMGetDS(newdm, &prob));
        PetscCall(PetscDSViewFromOptions(prob, NULL, "-ds_view"));
      }
      PetscCall(DMDestroy(&dm));
      dm = newdm;
      PetscCall(PetscObjectSetName((PetscObject)dm, "Mesh"));
      PetscCall(DMViewFromOptions(dm, NULL, "-my_dm_view"));
      PetscCall(DMSetFromOptions(dm));
    }
  }
  PetscCall(DMDestroy(&dm));
  if (run_type == 1) err[0] = 5.97537599375e+01 - mdisp[0]; /* error with what I think is the exact solution */
  else if (run_type == 0) err[0] = 0;
  else if (run_type == 2) err[0] = 3.527795e+01 - mdisp[0];
  else err[0] = 0;
  PetscCall(PetscPrintf(PETSC_COMM_WORLD, "[%d] %d) N=%12" PetscInt_FMT ", max displ=%9.7e, error=%4.3e\n", rank, 0, sizes[0], (double)mdisp[0], (double)err[0]));
  for (iter = 1; iter < max_conv_its; iter++) {
    if (run_type == 1) err[iter] = 5.97537599375e+01 - mdisp[iter];
    else if (run_type == 0) err[iter] = 0;
    else if (run_type == 2) err[iter] = 3.527795e+01 - mdisp[iter];
    else err[iter] = 0;
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "[%d] %" PetscInt_FMT ") N=%12" PetscInt_FMT ", max displ=%9.7e, disp diff=%9.2e, error=%4.3e, rate=%3.2g\n", rank, iter, sizes[iter], (double)mdisp[iter], (double)(mdisp[iter] - mdisp[iter - 1]), (double)err[iter], (double)(PetscLogReal(PetscAbs(err[iter - 1] / err[iter])) / PetscLogReal(2.))));
  }

  PetscCall(PetscFinalize());
  return 0;
}

/*TEST

  testset:
    nsize: 4
    requires: !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -petscspace_degree 2 -snes_max_it 1 -ksp_max_it 100 -ksp_type cg -ksp_rtol 1.e-10 -ksp_norm_type unpreconditioned -pc_type gamg -pc_gamg_coarse_eq_limit 10 -pc_gamg_reuse_interpolation true -pc_gamg_aggressive_coarsening 1 -pc_gamg_threshold 0.001 -ksp_converged_reason -use_mat_nearnullspace true -mg_levels_ksp_max_it 2 -mg_levels_ksp_type chebyshev -mg_levels_ksp_chebyshev_esteig 0,0.2,0,1.1 -mg_levels_pc_type jacobi -petscpartitioner_type simple -my_dm_view -snes_lag_jacobian -2 -snes_type ksponly -pc_gamg_mis_k_minimum_degree_ordering true -pc_gamg_low_memory_threshold_filter
    timeoutfactor: 2
    test:
      suffix: 0
      args: -run_type 1 -max_conv_its 3 -pc_gamg_mat_coarsen_type hem -pc_gamg_mat_coarsen_max_it 5 -pc_gamg_asm_hem_aggs 4 -ksp_rtol 1.e-6
      filter: sed -e "s/Linear solve converged due to CONVERGED_RTOL iterations 7/Linear solve converged due to CONVERGED_RTOL iterations 8/g"
    test:
      suffix: 1
      filter: grep -v HERMITIAN
      args: -run_type 2 -max_conv_its 2 -use_mat_nearnullspace false -snes_view

  test:
    nsize: 1
    requires: !single
    suffix: 2
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -petscspace_degree 2 -snes_max_it 1 -ksp_type cg -ksp_norm_type unpreconditioned -pc_type gamg -pc_gamg_coarse_eq_limit 10 -pc_gamg_aggressive_coarsening 1 -ksp_converged_reason -use_mat_nearnullspace true -my_dm_view -snes_type ksponly
    timeoutfactor: 2

  # HYPRE PtAP broken with complex numbers
  test:
    suffix: hypre
    requires: hypre !single !complex !defined(PETSC_HAVE_HYPRE_DEVICE)
    nsize: 4
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type cg -ksp_monitor_short -ksp_rtol 1.e-8 -pc_type hypre -pc_hypre_type boomeramg -pc_hypre_boomeramg_no_CF true -pc_hypre_boomeramg_agg_nl 1 -pc_hypre_boomeramg_coarsen_type HMIS -pc_hypre_boomeramg_interp_type ext+i -ksp_converged_reason -use_mat_nearnullspace true -petscpartitioner_type simple

  test:
    suffix: ml
    requires: ml !single
    nsize: 4
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type cg -ksp_monitor_short -ksp_converged_reason -ksp_rtol 1.e-8 -pc_type ml -mg_levels_ksp_type chebyshev -mg_levels_ksp_max_it 3 -mg_levels_ksp_chebyshev_esteig 0,0.05,0,1.05 -mg_levels_pc_type sor -petscpartitioner_type simple -use_mat_nearnullspace

  test:
    suffix: hpddm
    requires: hpddm slepc !single defined(PETSC_HAVE_DYNAMIC_LIBRARIES) defined(PETSC_USE_SHARED_LIBRARIES)
    nsize: 4
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type fgmres -ksp_monitor_short -ksp_converged_reason -ksp_rtol 1.e-8 -pc_type hpddm -petscpartitioner_type simple -pc_hpddm_levels_1_sub_pc_type lu -pc_hpddm_levels_1_eps_nev 6 -pc_hpddm_coarse_p 1 -pc_hpddm_coarse_pc_type svd

  test:
    suffix: repart
    nsize: 4
    requires: parmetis !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -petscspace_degree 2 -snes_max_it 4 -ksp_max_it 100 -ksp_type cg -ksp_rtol 1.e-2 -ksp_norm_type unpreconditioned -snes_rtol 1.e-3 -pc_type gamg -pc_gamg_esteig_ksp_max_it 10 -pc_gamg_type agg -pc_gamg_agg_nsmooths 1 -pc_gamg_aggressive_coarsening 1 -pc_gamg_threshold 0.05 -pc_gamg_threshold_scale .0 -use_mat_nearnullspace true -mg_levels_ksp_max_it 2 -mg_levels_ksp_type chebyshev -mg_levels_ksp_chebyshev_esteig 0,0.05,0,1.05 -mg_levels_pc_type jacobi -pc_gamg_mat_partitioning_type parmetis -pc_gamg_repartition true -pc_gamg_process_eq_limit 20 -pc_gamg_coarse_eq_limit 10 -ksp_converged_reason -pc_gamg_reuse_interpolation true -petscpartitioner_type simple

  test:
    suffix: bddc
    nsize: 4
    requires: !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type cg -ksp_monitor_short -ksp_rtol 1.e-8 -ksp_converged_reason -petscpartitioner_type simple -dm_mat_type is -mat_is_localmat_type {{sbaij baij aij}} -pc_type bddc

  testset:
    nsize: 4
    requires: !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type cg -ksp_monitor_short -ksp_rtol 1.e-10 -ksp_converged_reason -petscpartitioner_type simple -dm_mat_type is -mat_is_localmat_type aij -pc_type bddc -attach_mat_nearnullspace {{0 1}separate output}
    test:
      suffix: bddc_approx_gamg
      args: -pc_bddc_switch_static -prefix_push pc_bddc_dirichlet_ -approximate -pc_type gamg -pc_gamg_esteig_ksp_max_it 10 -pc_gamg_type agg -pc_gamg_agg_nsmooths 1 -pc_gamg_reuse_interpolation true -pc_gamg_aggressive_coarsening 1 -pc_gamg_threshold 0.05 -pc_gamg_threshold_scale .0 -mg_levels_ksp_max_it 1 -mg_levels_ksp_type chebyshev -prefix_pop -prefix_push pc_bddc_neumann_ -approximate -pc_type gamg -pc_gamg_esteig_ksp_max_it 10 -pc_gamg_type agg -pc_gamg_agg_nsmooths 1 -pc_gamg_coarse_eq_limit 10 -pc_gamg_reuse_interpolation true -pc_gamg_aggressive_coarsening 1 -pc_gamg_threshold 0.05 -pc_gamg_threshold_scale .0 -mg_levels_ksp_max_it 1 -mg_levels_ksp_type chebyshev -prefix_pop
    # HYPRE PtAP broken with complex numbers
    test:
      requires: hypre !complex !defined(PETSC_HAVE_HYPRE_DEVICE)
      suffix: bddc_approx_hypre
      args: -pc_bddc_switch_static -prefix_push pc_bddc_dirichlet_ -pc_type hypre -pc_hypre_boomeramg_no_CF true -pc_hypre_boomeramg_strong_threshold 0.75 -pc_hypre_boomeramg_agg_nl 1 -pc_hypre_boomeramg_coarsen_type HMIS -pc_hypre_boomeramg_interp_type ext+i -prefix_pop -prefix_push pc_bddc_neumann_ -pc_type hypre -pc_hypre_boomeramg_no_CF true -pc_hypre_boomeramg_strong_threshold 0.75 -pc_hypre_boomeramg_agg_nl 1 -pc_hypre_boomeramg_coarsen_type HMIS -pc_hypre_boomeramg_interp_type ext+i -prefix_pop
    test:
      requires: ml
      suffix: bddc_approx_ml
      args: -pc_bddc_switch_static -prefix_push pc_bddc_dirichlet_ -approximate -pc_type ml -mg_levels_ksp_max_it 1 -mg_levels_ksp_type chebyshev -prefix_pop -prefix_push pc_bddc_neumann_ -approximate -pc_type ml -mg_levels_ksp_max_it 1 -mg_levels_ksp_type chebyshev -prefix_pop

  test:
    suffix: fetidp
    nsize: 4
    requires: !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type fetidp -fetidp_ksp_type cg -ksp_monitor_short -ksp_rtol 1.e-8 -ksp_converged_reason -petscpartitioner_type simple -dm_mat_type is -mat_is_localmat_type {{sbaij baij aij}}

  test:
    suffix: bddc_elast
    nsize: 4
    requires: !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type cg -ksp_monitor_short -ksp_rtol 1.e-8 -ksp_converged_reason -petscpartitioner_type simple -dm_mat_type is -mat_is_localmat_type sbaij -pc_type bddc -pc_bddc_monolithic -attach_mat_nearnullspace

  test:
    suffix: fetidp_elast
    nsize: 4
    requires: !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type fetidp -fetidp_ksp_type cg -ksp_monitor_short -ksp_rtol 1.e-8 -ksp_converged_reason -petscpartitioner_type simple -dm_mat_type is -mat_is_localmat_type sbaij -fetidp_bddc_pc_bddc_monolithic -attach_mat_nearnullspace

  test:
    suffix: gdsw
    nsize: 4
    requires: !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -lx 1. -alpha .01 -petscspace_degree 2 -ksp_type cg -ksp_monitor_short -ksp_rtol 1.e-8 -ksp_converged_reason -petscpartitioner_type simple -dm_mat_type is -attach_mat_nearnullspace \
          -pc_type mg -pc_mg_galerkin -pc_mg_adapt_interp_coarse_space gdsw -pc_mg_levels 2 -mg_levels_pc_type bjacobi -mg_levels_sub_pc_type icc

  testset:
    nsize: 4
    requires: !single
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -petscspace_degree 2 -snes_max_it 2 -ksp_max_it 100 -ksp_type cg -ksp_rtol 1.e-10 -ksp_norm_type unpreconditioned -snes_rtol 1.e-10 -pc_type gamg -pc_gamg_esteig_ksp_max_it 10 -pc_gamg_type agg -pc_gamg_agg_nsmooths 1 -pc_gamg_coarse_eq_limit 10 -pc_gamg_reuse_interpolation true -pc_gamg_aggressive_coarsening 0 -pc_gamg_threshold 0.05 -pc_gamg_threshold_scale .0 -use_mat_nearnullspace true -mg_levels_ksp_max_it 2 -mg_levels_ksp_type chebyshev -mg_levels_ksp_chebyshev_esteig 0,0.05,0,1.05 -mg_levels_pc_type jacobi -ksp_monitor_short -ksp_converged_reason -snes_monitor_short -dm_view -petscpartitioner_type simple -pc_gamg_process_eq_limit 20 -pc_gamg_coarse_eq_limit 40
    output_file: output/ex56_cuda.out

    test:
      suffix: cuda
      requires: cuda
      args: -dm_mat_type aijcusparse -dm_vec_type cuda

    test:
      suffix: hip
      requires: hip
      args: -dm_mat_type aijhipsparse -dm_vec_type hip

    test:
      suffix: viennacl
      requires: viennacl
      args: -dm_mat_type aijviennacl -dm_vec_type viennacl

    test:
      suffix: kokkos
      requires: kokkos_kernels
      args: -dm_mat_type aijkokkos -dm_vec_type kokkos
  # Don't run AIJMKL caes with complex scalars because of convergence issues.
  # Note that we need to test both single and multiple MPI rank cases, because these use different sparse MKL routines to implement the PtAP operation.
  test:
    suffix: seqaijmkl
    nsize: 1
    requires: defined(PETSC_HAVE_MKL_SPARSE_OPTIMIZE) !single !complex
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -petscspace_degree 2 -snes_max_it 2 -ksp_max_it 100 -ksp_type cg -ksp_rtol 1.e-11 -ksp_norm_type unpreconditioned -snes_rtol 1.e-10 -pc_type gamg -pc_gamg_type agg -pc_gamg_agg_nsmooths 1 -pc_gamg_coarse_eq_limit 1000 -pc_gamg_reuse_interpolation true -pc_gamg_aggressive_coarsening 1 -pc_gamg_threshold 0.05 -pc_gamg_threshold_scale .0 -ksp_converged_reason -use_mat_nearnullspace true -mg_levels_ksp_max_it 1 -mg_levels_ksp_type chebyshev -pc_gamg_esteig_ksp_type cg -pc_gamg_esteig_ksp_max_it 10 -mg_levels_ksp_chebyshev_esteig 0,0.05,0,1.1 -mg_levels_pc_type jacobi -petscpartitioner_type simple -mat_block_size 3 -dm_view -mat_seqaij_type seqaijmkl
    timeoutfactor: 2

  test:
    suffix: mpiaijmkl
    nsize: 4
    requires: defined(PETSC_HAVE_MKL_SPARSE_OPTIMIZE) !single !complex
    args: -dm_plex_dim 3 -dm_plex_simplex 0 -dm_plex_box_lower 0,0,0 -dm_plex_box_upper 1,1,1 -run_type 1 -dm_plex_box_faces 2,2,1 -petscpartitioner_simple_process_grid 2,2,1 -max_conv_its 2 -petscspace_degree 2 -snes_max_it 2 -ksp_max_it 100 -ksp_type cg -ksp_rtol 1.e-11 -ksp_norm_type unpreconditioned -snes_rtol 1.e-10 -pc_type gamg -pc_gamg_type agg -pc_gamg_agg_nsmooths 1 -pc_gamg_coarse_eq_limit 1000 -pc_gamg_reuse_interpolation true -pc_gamg_aggressive_coarsening 1 -pc_gamg_threshold 0.05 -pc_gamg_threshold_scale .0 -ksp_converged_reason -use_mat_nearnullspace true -mg_levels_ksp_max_it 1 -mg_levels_ksp_type chebyshev -pc_gamg_esteig_ksp_type cg -pc_gamg_esteig_ksp_max_it 10 -mg_levels_ksp_chebyshev_esteig 0,0.05,0,1.1 -mg_levels_pc_type jacobi -petscpartitioner_type simple -mat_block_size 3 -dm_view -mat_seqaij_type seqaijmkl
    timeoutfactor: 2

TEST*/
````

## TS ex45.c

- Selected by: Tutorials by physics
- Rendered listing: <https://petsc.org/release/src/ts/tutorials/ex45.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/ts/tutorials/ex45.c>

````c
static char help[] = "Heat Equation in 2d and 3d with finite elements.\n\
We solve the heat equation in a rectangular\n\
domain, using a parallel unstructured mesh (DMPLEX) to discretize it.\n\
Contributed by: Julian Andrej <juan@tf.uni-kiel.de>\n\n\n";

#include <petscdmplex.h>
#include <petscds.h>
#include <petscts.h>

/*
  Heat equation:

    du/dt - \Delta u + f = 0
*/

typedef enum {
  SOL_QUADRATIC_LINEAR,
  SOL_QUADRATIC_TRIG,
  SOL_TRIG_LINEAR,
  SOL_TRIG_TRIG,
  NUM_SOLUTION_TYPES
} SolutionType;
const char *solutionTypes[NUM_SOLUTION_TYPES + 1] = {"quadratic_linear", "quadratic_trig", "trig_linear", "trig_trig", "unknown"};

typedef struct {
  SolutionType solType; /* Type of exact solution */
  /* Solver setup */
  PetscBool expTS;        /* Flag for explicit timestepping */
  PetscBool lumped;       /* Lump the mass matrix */
  PetscInt  remesh_every; /* Remesh every number of steps */
  DM        remesh_dm;    /* New DM after remeshing */
} AppCtx;

/*
Exact 2D solution:
  u    = 2t + x^2 + y^2
  u_t  = 2
  \Delta u = 2 + 2 = 4
  f    = 2
  F(u) = 2 - (2 + 2) + 2 = 0

Exact 3D solution:
  u = 3t + x^2 + y^2 + z^2
  F(u) = 3 - (2 + 2 + 2) + 3 = 0
*/
static PetscErrorCode mms_quad_lin(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;

  *u = dim * time;
  for (d = 0; d < dim; ++d) *u += x[d] * x[d];
  return PETSC_SUCCESS;
}

static PetscErrorCode mms_quad_lin_t(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = dim;
  return PETSC_SUCCESS;
}

static void f0_quad_lin_exp(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = -(PetscScalar)dim;
}
static void f0_quad_lin(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscScalar exp[1] = {0.};
  f0_quad_lin_exp(dim, Nf, NfAux, uOff, uOff_x, u, u_t, u_x, aOff, aOff_x, a, a_t, a_x, t, x, numConstants, constants, exp);
  f0[0] = u_t[0] - exp[0];
}

/*
Exact 2D solution:
  u = 2*cos(t) + x^2 + y^2
  F(u) = -2*sint(t) - (2 + 2) + 2*sin(t) + 4 = 0

Exact 3D solution:
  u = 3*cos(t) + x^2 + y^2 + z^2
  F(u) = -3*sin(t) - (2 + 2 + 2) + 3*sin(t) + 6 = 0
*/
static PetscErrorCode mms_quad_trig(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;

  *u = dim * PetscCosReal(time);
  for (d = 0; d < dim; ++d) *u += x[d] * x[d];
  return PETSC_SUCCESS;
}

static PetscErrorCode mms_quad_trig_t(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = -dim * PetscSinReal(time);
  return PETSC_SUCCESS;
}

static void f0_quad_trig_exp(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  f0[0] = -dim * (PetscSinReal(t) + 2.0);
}
static void f0_quad_trig(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscScalar exp[1] = {0.};
  f0_quad_trig_exp(dim, Nf, NfAux, uOff, uOff_x, u, u_t, u_x, aOff, aOff_x, a, a_t, a_x, t, x, numConstants, constants, exp);
  f0[0] = u_t[0] - exp[0];
}

/*
Exact 2D solution:
  u = 2\pi^2 t + cos(\pi x) + cos(\pi y)
  F(u) = 2\pi^2 - \pi^2 (cos(\pi x) + cos(\pi y)) + \pi^2 (cos(\pi x) + cos(\pi y)) - 2\pi^2 = 0

Exact 3D solution:
  u = 3\pi^2 t + cos(\pi x) + cos(\pi y) + cos(\pi z)
  F(u) = 3\pi^2 - \pi^2 (cos(\pi x) + cos(\pi y) + cos(\pi z)) + \pi^2 (cos(\pi x) + cos(\pi y) + cos(\pi z)) - 3\pi^2 = 0
*/
static PetscErrorCode mms_trig_lin(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;

  *u = dim * PetscSqr(PETSC_PI) * time;
  for (d = 0; d < dim; ++d) *u += PetscCosReal(PETSC_PI * x[d]);
  return PETSC_SUCCESS;
}

static PetscErrorCode mms_trig_lin_t(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = dim * PetscSqr(PETSC_PI);
  return PETSC_SUCCESS;
}

static void f0_trig_lin(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscInt d;
  f0[0] = u_t[0];
  for (d = 0; d < dim; ++d) f0[0] += PetscSqr(PETSC_PI) * (PetscCosReal(PETSC_PI * x[d]) - 1.0);
}

/*
Exact 2D solution:
  u    = pi^2 cos(t) + cos(\pi x) + cos(\pi y)
  u_t  = -pi^2 sin(t)
  \Delta u = -\pi^2 (cos(\pi x) + cos(\pi y))
  f    = pi^2 sin(t) - \pi^2 (cos(\pi x) + cos(\pi y))
  F(u) = -\pi^2 sin(t) + \pi^2 (cos(\pi x) + cos(\pi y)) - \pi^2 (cos(\pi x) + cos(\pi y)) + \pi^2 sin(t) = 0

Exact 3D solution:
  u    = pi^2 cos(t) + cos(\pi x) + cos(\pi y) + cos(\pi z)
  u_t  = -pi^2 sin(t)
  \Delta u = -\pi^2 (cos(\pi x) + cos(\pi y) + cos(\pi z))
  f    = pi^2 sin(t) - \pi^2 (cos(\pi x) + cos(\pi y) + cos(\pi z))
  F(u) = -\pi^2 sin(t) + \pi^2 (cos(\pi x) + cos(\pi y) + cos(\pi z)) - \pi^2 (cos(\pi x) + cos(\pi y) + cos(\pi z)) + \pi^2 sin(t) = 0
*/
static PetscErrorCode mms_trig_trig(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  PetscInt d;

  *u = PetscSqr(PETSC_PI) * PetscCosReal(time);
  for (d = 0; d < dim; ++d) *u += PetscCosReal(PETSC_PI * x[d]);
  return PETSC_SUCCESS;
}

static PetscErrorCode mms_trig_trig_t(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx)
{
  *u = -PetscSqr(PETSC_PI) * PetscSinReal(time);
  return PETSC_SUCCESS;
}

static void f0_trig_trig_exp(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscInt d;
  f0[0] -= PetscSqr(PETSC_PI) * PetscSinReal(t);
  for (d = 0; d < dim; ++d) f0[0] += PetscSqr(PETSC_PI) * PetscCosReal(PETSC_PI * x[d]);
}
static void f0_trig_trig(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscScalar exp[1] = {0.};
  f0_trig_trig_exp(dim, Nf, NfAux, uOff, uOff_x, u, u_t, u_x, aOff, aOff_x, a, a_t, a_x, t, x, numConstants, constants, exp);
  f0[0] = u_t[0] - exp[0];
}

static void f1_temp_exp(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  for (PetscInt d = 0; d < dim; ++d) f1[d] = -u_x[d];
}
static void f1_temp(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  for (PetscInt d = 0; d < dim; ++d) f1[d] = u_x[d];
}

static void g3_temp(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  for (PetscInt d = 0; d < dim; ++d) g3[d * dim + d] = 1.0;
}

static void g0_temp(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  g0[0] = u_tShift * 1.0;
}

static PetscErrorCode ProcessOptions(MPI_Comm comm, AppCtx *options)
{
  PetscInt sol;

  PetscFunctionBeginUser;
  options->solType      = SOL_QUADRATIC_LINEAR;
  options->expTS        = PETSC_FALSE;
  options->lumped       = PETSC_TRUE;
  options->remesh_every = 0;

  PetscOptionsBegin(comm, "", "Heat Equation Options", "DMPLEX");
  sol = options->solType;
  PetscCall(PetscOptionsEList("-sol_type", "Type of exact solution", "ex45.c", solutionTypes, NUM_SOLUTION_TYPES, solutionTypes[options->solType], &sol, NULL));
  options->solType = (SolutionType)sol;
  PetscCall(PetscOptionsBool("-explicit", "Use explicit timestepping", "ex45.c", options->expTS, &options->expTS, NULL));
  PetscCall(PetscOptionsBool("-lumped", "Lump the mass matrix", "ex45.c", options->lumped, &options->lumped, NULL));
  PetscCall(PetscOptionsInt("-remesh_every", "Remesh every number of steps", "ex45.c", options->remesh_every, &options->remesh_every, NULL));
  PetscOptionsEnd();
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode CreateMesh(MPI_Comm comm, DM *dm, AppCtx *ctx)
{
  PetscFunctionBeginUser;
  PetscCall(DMCreate(comm, dm));
  PetscCall(DMSetType(*dm, DMPLEX));
  PetscCall(DMSetFromOptions(*dm));
  {
    char      convType[256];
    PetscBool flg;
    PetscOptionsBegin(comm, "", "Mesh conversion options", "DMPLEX");
    PetscCall(PetscOptionsFList("-dm_plex_convert_type", "Convert DMPlex to another format", __FILE__, DMList, DMPLEX, convType, 256, &flg));
    PetscOptionsEnd();
    if (flg) {
      DM dmConv;
      PetscCall(DMConvert(*dm, convType, &dmConv));
      if (dmConv) {
        PetscCall(DMDestroy(dm));
        *dm = dmConv;
        PetscCall(DMSetFromOptions(*dm));
        PetscCall(DMSetUp(*dm));
      }
    }
  }
  PetscCall(DMViewFromOptions(*dm, NULL, "-dm_view"));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupProblem(DM dm, AppCtx *ctx)
{
  PetscDS        ds;
  DMLabel        label;
  const PetscInt id = 1;

  PetscFunctionBeginUser;
  PetscCall(DMGetLabel(dm, "marker", &label));
  PetscCall(DMGetDS(dm, &ds));
  PetscCall(PetscDSSetJacobian(ds, 0, 0, g0_temp, NULL, NULL, g3_temp));
  switch (ctx->solType) {
  case SOL_QUADRATIC_LINEAR:
    PetscCall(PetscDSSetResidual(ds, 0, f0_quad_lin, f1_temp));
    PetscCall(PetscDSSetRHSResidual(ds, 0, f0_quad_lin_exp, f1_temp_exp));
    PetscCall(PetscDSSetExactSolution(ds, 0, mms_quad_lin, ctx));
    PetscCall(PetscDSSetExactSolutionTimeDerivative(ds, 0, mms_quad_lin_t, ctx));
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)mms_quad_lin, (PetscVoidFn *)mms_quad_lin_t, ctx, NULL));
    break;
  case SOL_QUADRATIC_TRIG:
    PetscCall(PetscDSSetResidual(ds, 0, f0_quad_trig, f1_temp));
    PetscCall(PetscDSSetRHSResidual(ds, 0, f0_quad_trig_exp, f1_temp_exp));
    PetscCall(PetscDSSetExactSolution(ds, 0, mms_quad_trig, ctx));
    PetscCall(PetscDSSetExactSolutionTimeDerivative(ds, 0, mms_quad_trig_t, ctx));
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)mms_quad_trig, (PetscVoidFn *)mms_quad_trig_t, ctx, NULL));
    break;
  case SOL_TRIG_LINEAR:
    PetscCall(PetscDSSetResidual(ds, 0, f0_trig_lin, f1_temp));
    PetscCall(PetscDSSetExactSolution(ds, 0, mms_trig_lin, ctx));
    PetscCall(PetscDSSetExactSolutionTimeDerivative(ds, 0, mms_trig_lin_t, ctx));
    PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)mms_trig_lin, (PetscVoidFn *)mms_trig_lin_t, ctx, NULL));
    break;
  case SOL_TRIG_TRIG:
    PetscCall(PetscDSSetResidual(ds, 0, f0_trig_trig, f1_temp));
    PetscCall(PetscDSSetRHSResidual(ds, 0, f0_trig_trig_exp, f1_temp_exp));
    PetscCall(PetscDSSetExactSolution(ds, 0, mms_trig_trig, ctx));
    PetscCall(PetscDSSetExactSolutionTimeDerivative(ds, 0, mms_trig_trig_t, ctx));
    break;
  default:
    SETERRQ(PetscObjectComm((PetscObject)dm), PETSC_ERR_ARG_WRONG, "Invalid solution type: %s (%d)", solutionTypes[PetscMin(ctx->solType, NUM_SOLUTION_TYPES)], ctx->solType);
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupDiscretization(DM dm, AppCtx *ctx)
{
  DM        plex, cdm = dm;
  PetscFE   fe;
  PetscBool simplex;
  PetscInt  dim;

  PetscFunctionBeginUser;
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMConvert(dm, DMPLEX, &plex));
  PetscCall(DMPlexIsSimplex(plex, &simplex));
  PetscCall(DMDestroy(&plex));
  PetscCall(PetscFECreateDefault(PETSC_COMM_SELF, dim, 1, simplex, "temp_", -1, &fe));
  PetscCall(PetscObjectSetName((PetscObject)fe, "temperature"));
  /* Set discretization and boundary conditions for each mesh */
  PetscCall(DMSetField(dm, 0, NULL, (PetscObject)fe));
  PetscCall(DMCreateDS(dm));
  if (ctx->expTS) {
    PetscDS ds;

    PetscCall(DMGetDS(dm, &ds));
    PetscCall(PetscDSSetImplicit(ds, 0, PETSC_FALSE));
  }
  PetscCall(SetupProblem(dm, ctx));
  while (cdm) {
    PetscCall(DMCopyDisc(dm, cdm));
    PetscCall(DMGetCoarseDM(cdm, &cdm));
  }
  PetscCall(PetscFEDestroy(&fe));
  PetscFunctionReturn(PETSC_SUCCESS);
}

#include <petsc/private/dmpleximpl.h>
static PetscErrorCode Remesh(DM dm, Vec U, DM *newdm)
{
  PetscFunctionBeginUser;
  PetscCall(DMViewFromOptions(dm, NULL, "-remesh_dmin_view"));
  *newdm = NULL;

  PetscInt  dim;
  DM        plex;
  PetscBool simplex;
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMConvert(dm, DMPLEX, &plex));
  PetscCall(DMPlexIsSimplex(plex, &simplex));
  PetscCall(DMDestroy(&plex));

  DM      dmGrad;
  PetscFE fe;
  PetscCall(DMClone(dm, &dmGrad));
  PetscCall(PetscFECreateDefault(PETSC_COMM_SELF, dim, dim, simplex, "grad_", -1, &fe));
  PetscCall(DMSetField(dmGrad, 0, NULL, (PetscObject)fe));
  PetscCall(PetscFEDestroy(&fe));
  PetscCall(DMCreateDS(dmGrad));

  Vec locU, locG;
  PetscCall(DMGetLocalVector(dm, &locU));
  PetscCall(DMGetLocalVector(dmGrad, &locG));
  PetscCall(DMGlobalToLocal(dm, U, INSERT_VALUES, locU));
  PetscCall(VecViewFromOptions(locU, NULL, "-remesh_input_view"));
  PetscCall(DMPlexComputeGradientClementInterpolant(dm, locU, locG));
  PetscCall(VecViewFromOptions(locG, NULL, "-remesh_grad_view"));

  const PetscScalar *g;
  PetscScalar       *u;
  PetscInt           n;
  PetscCall(VecGetLocalSize(locU, &n));
  PetscCall(VecGetArrayWrite(locU, &u));
  PetscCall(VecGetArrayRead(locG, &g));
  for (PetscInt i = 0; i < n; i++) {
    PetscReal norm = 0.0;
    for (PetscInt d = 0; d < dim; d++) norm += PetscSqr(PetscRealPart(g[dim * i + d]));
    u[i] = PetscSqrtReal(norm);
  }
  PetscCall(VecRestoreArrayRead(locG, &g));
  PetscCall(VecRestoreArrayWrite(locU, &u));

  DM  dmM;
  Vec metric;
  PetscCall(DMClone(dm, &dmM));
  PetscCall(DMPlexMetricCreateIsotropic(dmM, 0, locU, &metric));
  PetscCall(DMDestroy(&dmM));
  PetscCall(DMRestoreLocalVector(dm, &locU));
  PetscCall(DMRestoreLocalVector(dmGrad, &locG));
  PetscCall(DMDestroy(&dmGrad));

  // TODO remove?
  PetscScalar scale = 10.0;
  PetscCall(PetscOptionsGetScalar(NULL, NULL, "-metric_scale", &scale, NULL));
  PetscCall(VecScale(metric, scale));
  PetscCall(VecViewFromOptions(metric, NULL, "-metric_view"));

  DMLabel label = NULL;
  PetscCall(DMGetLabel(dm, "marker", &label));
  PetscCall(DMAdaptMetric(dm, metric, label, NULL, newdm));
  PetscCall(VecDestroy(&metric));

  PetscCall(DMViewFromOptions(*newdm, NULL, "-remesh_dmout_view"));

  AppCtx *ctx;
  PetscCall(DMGetApplicationContext(dm, &ctx));
  PetscCall(DMSetApplicationContext(*newdm, ctx));
  PetscCall(SetupDiscretization(*newdm, ctx));

  // TODO
  ((DM_Plex *)(*newdm)->data)->useHashLocation = ((DM_Plex *)dm->data)->useHashLocation;
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetInitialConditions(TS ts, Vec u)
{
  DM        dm;
  PetscReal t;

  PetscFunctionBeginUser;
  PetscCall(TSGetDM(ts, &dm));
  PetscCall(TSGetTime(ts, &t));
  PetscCall(DMComputeExactSolution(dm, t, u, NULL));
  PetscCall(VecSetOptionsPrefix(u, NULL));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode TransferSetUp(TS ts, PetscInt step, PetscReal time, Vec U, PetscBool *remesh, void *tctx)
{
  AppCtx *ctx = (AppCtx *)tctx;

  PetscFunctionBeginUser;
  *remesh = PETSC_FALSE;
  if (ctx->remesh_every > 0 && step && step % ctx->remesh_every == 0) {
    DM dm;

    *remesh = PETSC_TRUE;
    PetscCall(TSGetDM(ts, &dm));
    PetscCall(Remesh(dm, U, &ctx->remesh_dm));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode TransferVecs(TS ts, PetscInt nv, Vec vin[], Vec vout[], void *tctx)
{
  AppCtx *ctx = (AppCtx *)tctx;
  DM      dm;
  Mat     Interp;

  PetscFunctionBeginUser;
  PetscCall(TSGetDM(ts, &dm));
  PetscCall(DMCreateInterpolation(dm, ctx->remesh_dm, &Interp, NULL));
  for (PetscInt i = 0; i < nv; i++) {
    PetscCall(DMCreateGlobalVector(ctx->remesh_dm, &vout[i]));
    PetscCall(MatMult(Interp, vin[i], vout[i]));
  }
  PetscCall(MatDestroy(&Interp));
  PetscCall(TSSetDM(ts, ctx->remesh_dm));
  PetscCall(DMDestroy(&ctx->remesh_dm));
  PetscFunctionReturn(PETSC_SUCCESS);
}

int main(int argc, char **argv)
{
  DM     dm;
  TS     ts;
  Vec    u;
  AppCtx ctx;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(ProcessOptions(PETSC_COMM_WORLD, &ctx));
  PetscCall(CreateMesh(PETSC_COMM_WORLD, &dm, &ctx));
  PetscCall(DMSetApplicationContext(dm, &ctx));
  PetscCall(SetupDiscretization(dm, &ctx));

  PetscCall(TSCreate(PETSC_COMM_WORLD, &ts));
  PetscCall(TSSetDM(ts, dm));
  PetscCall(DMTSSetBoundaryLocal(dm, DMPlexTSComputeBoundary, &ctx));
  if (ctx.expTS) {
    PetscCall(DMTSSetRHSFunctionLocal(dm, DMPlexTSComputeRHSFunctionFEM, &ctx));
    if (ctx.lumped) PetscCall(DMTSCreateRHSMassMatrixLumped(dm));
    else PetscCall(DMTSCreateRHSMassMatrix(dm));
  } else {
    PetscCall(DMTSSetIFunctionLocal(dm, DMPlexTSComputeIFunctionFEM, &ctx));
    PetscCall(DMTSSetIJacobianLocal(dm, DMPlexTSComputeIJacobianFEM, &ctx));
  }
  PetscCall(TSSetMaxTime(ts, 1.0));
  PetscCall(TSSetExactFinalTime(ts, TS_EXACTFINALTIME_MATCHSTEP));
  PetscCall(TSSetFromOptions(ts));
  PetscCall(TSSetComputeInitialCondition(ts, SetInitialConditions));
  PetscCall(TSSetResize(ts, PETSC_FALSE, TransferSetUp, TransferVecs, &ctx));

  PetscCall(DMCreateGlobalVector(dm, &u));
  PetscCall(DMTSCheckFromOptions(ts, u));
  PetscCall(SetInitialConditions(ts, u));
  PetscCall(PetscObjectSetName((PetscObject)u, "temperature"));

  PetscCall(TSSetSolution(ts, u));
  PetscCall(VecViewFromOptions(u, NULL, "-u0_view"));
  PetscCall(VecDestroy(&u));
  PetscCall(TSSolve(ts, NULL));

  PetscCall(TSGetSolution(ts, &u));
  PetscCall(VecViewFromOptions(u, NULL, "-uf_view"));
  PetscCall(DMTSCheckFromOptions(ts, u));
  if (ctx.expTS) PetscCall(DMTSDestroyRHSMassMatrix(dm));

  PetscCall(TSDestroy(&ts));
  PetscCall(DMDestroy(&dm));
  PetscCall(PetscFinalize());
  return 0;
}

/*TEST

  test:
    suffix: 2d_p1
    requires: triangle
    args: -sol_type quadratic_linear -dm_refine 1 -temp_petscspace_degree 1 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    suffix: 2d_p1_exp
    requires: triangle
    args: -sol_type quadratic_linear -dm_refine 1 -temp_petscspace_degree 1 -explicit \
          -ts_type euler -ts_max_steps 4 -ts_time_step 1e-3 -ts_monitor_error
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [1.9]
    suffix: 2d_p1_sconv
    requires: triangle
    args: -sol_type quadratic_linear -temp_petscspace_degree 1 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [2.1]
    suffix: 2d_p1_sconv_2
    requires: triangle
    args: -sol_type trig_trig -temp_petscspace_degree 1 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 1e-6 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 4 -convest_num_refine 3 get L_2 convergence rate: [1.2]
    suffix: 2d_p1_tconv
    requires: triangle
    args: -sol_type quadratic_trig -temp_petscspace_degree 1 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 6 -convest_num_refine 3 get L_2 convergence rate: [1.0]
    suffix: 2d_p1_tconv_2
    requires: triangle
    args: -sol_type trig_trig -temp_petscspace_degree 1 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # The L_2 convergence rate cannot be seen since stability of the explicit integrator requires that is be more accurate than the grid
    suffix: 2d_p1_exp_tconv_2
    requires: triangle
    args: -sol_type trig_trig -temp_petscspace_degree 1 -explicit -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type euler -ts_max_steps 4 -ts_time_step 1e-4 -lumped 0 -mass_pc_type lu
  test:
    # The L_2 convergence rate cannot be seen since stability of the explicit integrator requires that is be more accurate than the grid
    suffix: 2d_p1_exp_tconv_2_lump
    requires: triangle
    args: -sol_type trig_trig -temp_petscspace_degree 1 -explicit -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type euler -ts_max_steps 4 -ts_time_step 1e-4
  test:
    suffix: 2d_p2
    requires: triangle
    args: -sol_type quadratic_linear -dm_refine 0 -temp_petscspace_degree 2 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [2.9]
    suffix: 2d_p2_sconv
    requires: triangle
    args: -sol_type trig_linear -temp_petscspace_degree 2 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00000001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [3.1]
    suffix: 2d_p2_sconv_2
    requires: triangle
    args: -sol_type trig_trig -temp_petscspace_degree 2 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00000001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 3 -convest_num_refine 3 get L_2 convergence rate: [1.0]
    suffix: 2d_p2_tconv
    requires: triangle
    args: -sol_type quadratic_trig -temp_petscspace_degree 2 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 3 -convest_num_refine 3 get L_2 convergence rate: [1.0]
    suffix: 2d_p2_tconv_2
    requires: triangle
    args: -sol_type trig_trig -temp_petscspace_degree 2 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    suffix: 2d_q1
    args: -sol_type quadratic_linear -dm_plex_simplex 0 -dm_refine 1 -temp_petscspace_degree 1 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [1.9]
    suffix: 2d_q1_sconv
    args: -sol_type quadratic_linear -dm_plex_simplex 0 -temp_petscspace_degree 1 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 4 -convest_num_refine 3 get L_2 convergence rate: [1.2]
    suffix: 2d_q1_tconv
    args: -sol_type quadratic_trig -dm_plex_simplex 0 -temp_petscspace_degree 1 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    suffix: 2d_q2
    args: -sol_type quadratic_linear -dm_plex_simplex 0 -dm_refine 0 -temp_petscspace_degree 2 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [2.9]
    suffix: 2d_q2_sconv
    args: -sol_type trig_linear -dm_plex_simplex 0 -temp_petscspace_degree 2 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00000001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 3 -convest_num_refine 3 get L_2 convergence rate: [1.0]
    suffix: 2d_q2_tconv
    args: -sol_type quadratic_trig -dm_plex_simplex 0 -temp_petscspace_degree 2 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu

  test:
    suffix: 3d_p1
    requires: ctetgen
    args: -sol_type quadratic_linear -dm_refine 1 -temp_petscspace_degree 1 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [1.9]
    suffix: 3d_p1_sconv
    requires: ctetgen
    args: -sol_type quadratic_linear -temp_petscspace_degree 1 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 4 -convest_num_refine 3 get L_2 convergence rate: [1.2]
    suffix: 3d_p1_tconv
    requires: ctetgen
    args: -sol_type quadratic_trig -temp_petscspace_degree 1 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    suffix: 3d_p2
    requires: ctetgen
    args: -sol_type quadratic_linear -dm_refine 0 -temp_petscspace_degree 2 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [2.9]
    suffix: 3d_p2_sconv
    requires: ctetgen
    args: -sol_type trig_linear -temp_petscspace_degree 2 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00000001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 3 -convest_num_refine 3 get L_2 convergence rate: [1.0]
    suffix: 3d_p2_tconv
    requires: ctetgen
    args: -sol_type quadratic_trig -temp_petscspace_degree 2 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    suffix: 3d_q1
    args: -sol_type quadratic_linear -dm_plex_simplex 0 -dm_refine 1 -temp_petscspace_degree 1 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [1.9]
    suffix: 3d_q1_sconv
    args: -sol_type quadratic_linear -dm_plex_simplex 0 -temp_petscspace_degree 1 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 4 -convest_num_refine 3 get L_2 convergence rate: [1.2]
    suffix: 3d_q1_tconv
    args: -sol_type quadratic_trig -dm_plex_simplex 0 -temp_petscspace_degree 1 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    suffix: 3d_q2
    args: -sol_type quadratic_linear -dm_plex_simplex 0 -dm_refine 0 -temp_petscspace_degree 2 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 2 -convest_num_refine 3 get L_2 convergence rate: [2.9]
    suffix: 3d_q2_sconv
    args: -sol_type trig_linear -dm_plex_simplex 0 -temp_petscspace_degree 2 -ts_convergence_estimate -ts_convergence_temporal 0 -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 1 -ts_time_step 0.00000001 -snes_error_if_not_converged -pc_type lu
  test:
    # -dm_refine 3 -convest_num_refine 3 get L_2 convergence rate: [1.0]
    suffix: 3d_q2_tconv
    args: -sol_type quadratic_trig -dm_plex_simplex 0 -temp_petscspace_degree 2 -ts_convergence_estimate -convest_num_refine 1 \
          -ts_type beuler -ts_max_steps 4 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu

  test:
    # For a nice picture, -bd_dm_refine 2 -dm_refine 1 -dm_view hdf5:${PETSC_DIR}/sol.h5 -ts_monitor_solution hdf5:${PETSC_DIR}/sol.h5::append
    suffix: egads_sphere
    requires: egads ctetgen datafilespath
    args: -sol_type quadratic_linear \
          -dm_plex_boundary_filename ${DATAFILESPATH}/meshes/cad/sphere_example.egadslite -dm_plex_boundary_label marker \
          -temp_petscspace_degree 2 -dmts_check .0001 \
          -ts_type beuler -ts_max_steps 5 -ts_time_step 0.1 -snes_error_if_not_converged -pc_type lu

  test:
    suffix: remesh
    requires: triangle mmg
    args: -sol_type quadratic_trig -dm_refine 2 -temp_petscspace_degree 1 -ts_type beuler -ts_time_step 0.01 -snes_error_if_not_converged -pc_type lu -grad_petscspace_degree 1 -dm_adaptor mmg -dm_plex_hash_location -remesh_every 5
    output_file: output/empty.out

TEST*/
````

## TS ex46.c

- Selected by: Tutorials by physics
- Rendered listing: <https://petsc.org/release/src/ts/tutorials/ex46.c.html>
- Upstream source: <https://gitlab.com/petsc/petsc/-/blob/20dc33036117482b0e5e1c6ca4fe5a1a7b83f44e/src/ts/tutorials/ex46.c>

````c
static char help[] = "Time dependent Navier-Stokes problem in 2d and 3d with finite elements.\n\
We solve the Navier-Stokes in a rectangular\n\
domain, using a parallel unstructured mesh (DMPLEX) to discretize it.\n\
This example supports discretized auxiliary fields (Re) as well as\n\
multilevel nonlinear solvers.\n\
Contributed by: Julian Andrej <juan@tf.uni-kiel.de>\n\n\n";

#include <petscdmplex.h>
#include <petscsnes.h>
#include <petscts.h>
#include <petscds.h>

/*
  Navier-Stokes equation:

  du/dt + u . grad u - \Delta u - grad p = f
  div u  = 0
*/

typedef struct {
  PetscInt mms;
} AppCtx;

#define REYN 400.0

/* MMS1

  u = t + x^2 + y^2;
  v = t + 2*x^2 - 2*x*y;
  p = x + y - 1;

  f_x = -2*t*(x + y) + 2*x*y^2 - 4*x^2*y - 2*x^3 + 4.0/Re - 1.0
  f_y = -2*t*x       + 2*y^3 - 4*x*y^2 - 2*x^2*y + 4.0/Re - 1.0

  so that

    u_t + u \cdot \nabla u - 1/Re \Delta u + \nabla p + f = <1, 1> + <t (2x + 2y) + 2x^3 + 4x^2y - 2xy^2, t 2x + 2x^2y + 4xy^2 - 2y^3> - 1/Re <4, 4> + <1, 1>
                                                    + <-t (2x + 2y) + 2xy^2 - 4x^2y - 2x^3 + 4/Re - 1, -2xt + 2y^3 - 4xy^2 - 2x^2y + 4/Re - 1> = 0
    \nabla \cdot u                                  = 2x - 2x = 0

  where

    <u, v> . <<u_x, v_x>, <u_y, v_y>> = <u u_x + v u_y, u v_x + v v_y>
*/
PetscErrorCode mms1_u_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *u, PetscCtx ctx)
{
  u[0] = time + x[0] * x[0] + x[1] * x[1];
  u[1] = time + 2.0 * x[0] * x[0] - 2.0 * x[0] * x[1];
  return PETSC_SUCCESS;
}

PetscErrorCode mms1_p_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *p, PetscCtx ctx)
{
  *p = x[0] + x[1] - 1.0;
  return PETSC_SUCCESS;
}

/* MMS 2*/

static PetscErrorCode mms2_u_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *u, PetscCtx ctx)
{
  u[0] = PetscSinReal(time + x[0]) * PetscSinReal(time + x[1]);
  u[1] = PetscCosReal(time + x[0]) * PetscCosReal(time + x[1]);
  return PETSC_SUCCESS;
}

static PetscErrorCode mms2_p_2d(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nf, PetscScalar *p, PetscCtx ctx)
{
  *p = PetscSinReal(time + x[0] - x[1]);
  return PETSC_SUCCESS;
}

static void f0_mms1_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal Re    = REYN;
  const PetscInt  Ncomp = dim;
  PetscInt        c, d;

  for (c = 0; c < Ncomp; ++c) {
    for (d = 0; d < dim; ++d) f0[c] += u[d] * u_x[c * dim + d];
  }
  f0[0] += u_t[0];
  f0[1] += u_t[1];

  f0[0] += -2.0 * t * (x[0] + x[1]) + 2.0 * x[0] * x[1] * x[1] - 4.0 * x[0] * x[0] * x[1] - 2.0 * x[0] * x[0] * x[0] + 4.0 / Re - 1.0;
  f0[1] += -2.0 * t * x[0] + 2.0 * x[1] * x[1] * x[1] - 4.0 * x[0] * x[1] * x[1] - 2.0 * x[0] * x[0] * x[1] + 4.0 / Re - 1.0;
}

static void f0_mms2_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  const PetscReal Re    = REYN;
  const PetscInt  Ncomp = dim;
  PetscInt        c, d;

  for (c = 0; c < Ncomp; ++c) {
    for (d = 0; d < dim; ++d) f0[c] += u[d] * u_x[c * dim + d];
  }
  f0[0] += u_t[0];
  f0[1] += u_t[1];

  f0[0] -= (Re * ((1.0L / 2.0L) * PetscSinReal(2 * t + 2 * x[0]) + PetscSinReal(2 * t + x[0] + x[1]) + PetscCosReal(t + x[0] - x[1])) + 2.0 * PetscSinReal(t + x[0]) * PetscSinReal(t + x[1])) / Re;
  f0[1] -= (-Re * ((1.0L / 2.0L) * PetscSinReal(2 * t + 2 * x[1]) + PetscSinReal(2 * t + x[0] + x[1]) + PetscCosReal(t + x[0] - x[1])) + 2.0 * PetscCosReal(t + x[0]) * PetscCosReal(t + x[1])) / Re;
}

static void f1_u(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  const PetscReal Re    = REYN;
  const PetscInt  Ncomp = dim;
  PetscInt        comp, d;

  for (comp = 0; comp < Ncomp; ++comp) {
    for (d = 0; d < dim; ++d) f1[comp * dim + d] = 1.0 / Re * u_x[comp * dim + d];
    f1[comp * dim + comp] -= u[Ncomp];
  }
}

static void f0_p(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f0[])
{
  PetscInt d;
  for (d = 0, f0[0] = 0.0; d < dim; ++d) f0[0] += u_x[d * dim + d];
}

static void f1_p(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f1[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) f1[d] = 0.0;
}

/*
  (psi_i, u_j grad_j u_i) ==> (\psi_i, \phi_j grad_j u_i)
*/
static void g0_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[])
{
  PetscInt NcI = dim, NcJ = dim;
  PetscInt fc, gc;
  PetscInt d;

  for (d = 0; d < dim; ++d) g0[d * dim + d] = u_tShift;

  for (fc = 0; fc < NcI; ++fc) {
    for (gc = 0; gc < NcJ; ++gc) g0[fc * NcJ + gc] += u_x[fc * NcJ + gc];
  }
}

/*
  (psi_i, u_j grad_j u_i) ==> (\psi_i, \u_j grad_j \phi_i)
*/
static void g1_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g1[])
{
  PetscInt NcI = dim;
  PetscInt NcJ = dim;
  PetscInt fc, gc, dg;
  for (fc = 0; fc < NcI; ++fc) {
    for (gc = 0; gc < NcJ; ++gc) {
      for (dg = 0; dg < dim; ++dg) {
        /* kronecker delta */
        if (fc == gc) g1[(fc * NcJ + gc) * dim + dg] += u[dg];
      }
    }
  }
}

/* < q, \nabla\cdot u >
   NcompI = 1, NcompJ = dim */
static void g1_pu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g1[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) g1[d * dim + d] = 1.0; /* \frac{\partial\phi^{u_d}}{\partial x_d} */
}

/* -< \nabla\cdot v, p >
    NcompI = dim, NcompJ = 1 */
static void g2_up(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g2[])
{
  PetscInt d;
  for (d = 0; d < dim; ++d) g2[d * dim + d] = -1.0; /* \frac{\partial\psi^{u_d}}{\partial x_d} */
}

/* < \nabla v, \nabla u + {\nabla u}^T >
   This just gives \nabla u, give the perdiagonal for the transpose */
static void g3_uu(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g3[])
{
  const PetscReal Re    = REYN;
  const PetscInt  Ncomp = dim;
  PetscInt        compI, d;

  for (compI = 0; compI < Ncomp; ++compI) {
    for (d = 0; d < dim; ++d) g3[((compI * Ncomp + compI) * dim + d) * dim + d] = 1.0 / Re;
  }
}

static PetscErrorCode ProcessOptions(MPI_Comm comm, AppCtx *options)
{
  PetscFunctionBeginUser;
  options->mms = 1;

  PetscOptionsBegin(comm, "", "Navier-Stokes Equation Options", "DMPLEX");
  PetscCall(PetscOptionsInt("-mms", "The manufactured solution to use", "ex46.c", options->mms, &options->mms, NULL));
  PetscOptionsEnd();
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode CreateMesh(MPI_Comm comm, DM *dm, AppCtx *ctx)
{
  PetscFunctionBeginUser;
  PetscCall(DMCreate(comm, dm));
  PetscCall(DMSetType(*dm, DMPLEX));
  PetscCall(DMSetFromOptions(*dm));
  PetscCall(DMViewFromOptions(*dm, NULL, "-dm_view"));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupProblem(DM dm, AppCtx *ctx)
{
  PetscDS        ds;
  DMLabel        label;
  const PetscInt id = 1;
  PetscInt       dim;

  PetscFunctionBeginUser;
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMGetDS(dm, &ds));
  PetscCall(DMGetLabel(dm, "marker", &label));
  switch (dim) {
  case 2:
    switch (ctx->mms) {
    case 1:
      PetscCall(PetscDSSetResidual(ds, 0, f0_mms1_u, f1_u));
      PetscCall(PetscDSSetResidual(ds, 1, f0_p, f1_p));
      PetscCall(PetscDSSetJacobian(ds, 0, 0, g0_uu, g1_uu, NULL, g3_uu));
      PetscCall(PetscDSSetJacobian(ds, 0, 1, NULL, NULL, g2_up, NULL));
      PetscCall(PetscDSSetJacobian(ds, 1, 0, NULL, g1_pu, NULL, NULL));
      PetscCall(PetscDSSetExactSolution(ds, 0, mms1_u_2d, ctx));
      PetscCall(PetscDSSetExactSolution(ds, 1, mms1_p_2d, ctx));
      PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)mms1_u_2d, NULL, ctx, NULL));
      break;
    case 2:
      PetscCall(PetscDSSetResidual(ds, 0, f0_mms2_u, f1_u));
      PetscCall(PetscDSSetResidual(ds, 1, f0_p, f1_p));
      PetscCall(PetscDSSetJacobian(ds, 0, 0, g0_uu, g1_uu, NULL, g3_uu));
      PetscCall(PetscDSSetJacobian(ds, 0, 1, NULL, NULL, g2_up, NULL));
      PetscCall(PetscDSSetJacobian(ds, 1, 0, NULL, g1_pu, NULL, NULL));
      PetscCall(PetscDSSetExactSolution(ds, 0, mms2_u_2d, ctx));
      PetscCall(PetscDSSetExactSolution(ds, 1, mms2_p_2d, ctx));
      PetscCall(DMAddBoundary(dm, DM_BC_ESSENTIAL, "wall", label, 1, &id, 0, 0, NULL, (PetscVoidFn *)mms2_u_2d, NULL, ctx, NULL));
      break;
    default:
      SETERRQ(PETSC_COMM_WORLD, PETSC_ERR_ARG_OUTOFRANGE, "Invalid MMS %" PetscInt_FMT, ctx->mms);
    }
    break;
  default:
    SETERRQ(PETSC_COMM_WORLD, PETSC_ERR_ARG_OUTOFRANGE, "Invalid dimension %" PetscInt_FMT, dim);
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode SetupDiscretization(DM dm, AppCtx *ctx)
{
  MPI_Comm  comm;
  DM        cdm = dm;
  PetscFE   fe[2];
  PetscInt  dim;
  PetscBool simplex;

  PetscFunctionBeginUser;
  PetscCall(PetscObjectGetComm((PetscObject)dm, &comm));
  PetscCall(DMGetDimension(dm, &dim));
  PetscCall(DMPlexIsSimplex(dm, &simplex));
  PetscCall(PetscFECreateDefault(comm, dim, dim, simplex, "vel_", PETSC_DEFAULT, &fe[0]));
  PetscCall(PetscObjectSetName((PetscObject)fe[0], "velocity"));
  PetscCall(PetscFECreateDefault(comm, dim, 1, simplex, "pres_", PETSC_DEFAULT, &fe[1]));
  PetscCall(PetscFECopyQuadrature(fe[0], fe[1]));
  PetscCall(PetscObjectSetName((PetscObject)fe[1], "pressure"));
  /* Set discretization and boundary conditions for each mesh */
  PetscCall(DMSetField(dm, 0, NULL, (PetscObject)fe[0]));
  PetscCall(DMSetField(dm, 1, NULL, (PetscObject)fe[1]));
  PetscCall(DMCreateDS(dm));
  PetscCall(SetupProblem(dm, ctx));
  while (cdm) {
    PetscObject  pressure;
    MatNullSpace nsp;

    PetscCall(DMGetField(cdm, 1, NULL, &pressure));
    PetscCall(MatNullSpaceCreate(PetscObjectComm(pressure), PETSC_TRUE, 0, NULL, &nsp));
    PetscCall(PetscObjectCompose(pressure, "nullspace", (PetscObject)nsp));
    PetscCall(MatNullSpaceDestroy(&nsp));

    PetscCall(DMCopyDisc(dm, cdm));
    PetscCall(DMGetCoarseDM(cdm, &cdm));
  }
  PetscCall(PetscFEDestroy(&fe[0]));
  PetscCall(PetscFEDestroy(&fe[1]));
  PetscFunctionReturn(PETSC_SUCCESS);
}

static PetscErrorCode MonitorError(TS ts, PetscInt step, PetscReal crtime, Vec u, PetscCtx ctx)
{
  PetscSimplePointFn *funcs[2];
  void               *ctxs[2];
  DM                  dm;
  PetscDS             ds;
  PetscReal           ferrors[2];

  PetscFunctionBeginUser;
  PetscCall(TSGetDM(ts, &dm));
  PetscCall(DMGetDS(dm, &ds));
  PetscCall(PetscDSGetExactSolution(ds, 0, &funcs[0], &ctxs[0]));
  PetscCall(PetscDSGetExactSolution(ds, 1, &funcs[1], &ctxs[1]));
  PetscCall(DMComputeL2FieldDiff(dm, crtime, funcs, ctxs, u, ferrors));
  PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Timestep: %04d time = %-8.4g \t L_2 Error: [%2.3g, %2.3g]\n", (int)step, (double)crtime, (double)ferrors[0], (double)ferrors[1]));
  PetscFunctionReturn(PETSC_SUCCESS);
}

int main(int argc, char **argv)
{
  AppCtx ctx;
  DM     dm;
  TS     ts;
  Vec    u, r;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCall(ProcessOptions(PETSC_COMM_WORLD, &ctx));
  PetscCall(CreateMesh(PETSC_COMM_WORLD, &dm, &ctx));
  PetscCall(DMSetApplicationContext(dm, &ctx));
  PetscCall(SetupDiscretization(dm, &ctx));
  PetscCall(DMPlexCreateClosureIndex(dm, NULL));

  PetscCall(DMCreateGlobalVector(dm, &u));
  PetscCall(VecDuplicate(u, &r));

  PetscCall(TSCreate(PETSC_COMM_WORLD, &ts));
  PetscCall(TSMonitorSet(ts, MonitorError, &ctx, NULL));
  PetscCall(TSSetDM(ts, dm));
  PetscCall(DMTSSetBoundaryLocal(dm, DMPlexTSComputeBoundary, &ctx));
  PetscCall(DMTSSetIFunctionLocal(dm, DMPlexTSComputeIFunctionFEM, &ctx));
  PetscCall(DMTSSetIJacobianLocal(dm, DMPlexTSComputeIJacobianFEM, &ctx));
  PetscCall(TSSetExactFinalTime(ts, TS_EXACTFINALTIME_STEPOVER));
  PetscCall(TSSetFromOptions(ts));
  PetscCall(DMTSCheckFromOptions(ts, u));

  {
    PetscSimplePointFn *funcs[2];
    void               *ctxs[2];
    PetscDS             ds;

    PetscCall(DMGetDS(dm, &ds));
    PetscCall(PetscDSGetExactSolution(ds, 0, &funcs[0], &ctxs[0]));
    PetscCall(PetscDSGetExactSolution(ds, 1, &funcs[1], &ctxs[1]));
    PetscCall(DMProjectFunction(dm, 0.0, funcs, ctxs, INSERT_ALL_VALUES, u));
  }
  PetscCall(TSSolve(ts, u));
  PetscCall(VecViewFromOptions(u, NULL, "-sol_vec_view"));

  PetscCall(VecDestroy(&u));
  PetscCall(VecDestroy(&r));
  PetscCall(TSDestroy(&ts));
  PetscCall(DMDestroy(&dm));
  PetscCall(PetscFinalize());
  return 0;
}

/*TEST

  # Full solves
  test:
    suffix: 2d_p2p1_r1
    requires: !single triangle
    filter: sed -e "s~ATOL~RTOL~g" -e "s~ABS~RELATIVE~g"
    args: -dm_refine 1 -vel_petscspace_degree 2 -pres_petscspace_degree 1 \
          -ts_type beuler -ts_max_steps 10 -ts_time_step 0.1 -ts_monitor -dmts_check \
          -snes_monitor_short -snes_converged_reason \
          -ksp_monitor_short -ksp_converged_reason \
          -pc_type fieldsplit -pc_fieldsplit_type schur -pc_fieldsplit_schur_fact_type full \
            -fieldsplit_velocity_pc_type lu \
            -fieldsplit_pressure_ksp_rtol 1.0e-10 -fieldsplit_pressure_pc_type jacobi

  test:
    suffix: 2d_q2q1_r1
    requires: !single
    filter: sed -e "s~ATOL~RTOL~g" -e "s~ABS~RELATIVE~g" -e "s~ 0\]~ 0.0\]~g"
    args: -dm_plex_simplex 0 -dm_refine 1 -vel_petscspace_degree 2 -pres_petscspace_degree 1 \
          -ts_type beuler -ts_max_steps 10 -ts_time_step 0.1 -ts_monitor -dmts_check \
          -snes_monitor_short -snes_converged_reason \
          -ksp_monitor_short -ksp_converged_reason \
          -pc_type fieldsplit -pc_fieldsplit_type schur -pc_fieldsplit_schur_fact_type full \
            -fieldsplit_velocity_pc_type lu \
            -fieldsplit_pressure_ksp_rtol 1.0e-10 -fieldsplit_pressure_pc_type jacobi

TEST*/
````

