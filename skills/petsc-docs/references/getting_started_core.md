# Petsc-Docs-Full-Raw - Getting Started Core

**Pages:** 10

---

## Checking the PETSc version#

**URL:** https://petsc.org/release/manual/versionchecking/

**Contents:**
- Checking the PETSc version#
- During configure/make time#
- During compile time#
- At Runtime#

The PETSc version is defined in $PETSC_DIR/include/petscversion.h with the three macros PETSC_VERSION_MAJOR, PETSC_VERSION_MINOR, and PETSC_VERSION_SUBMINOR.

The shell commands make getversion or $PETSC_DIR/lib/petsc/bin/petscversion prints out the PETSc version. The command

allows one to add tests to make files, CMake files, configure scripts etc, to ensure the PETSc version is compatible with your applications. For example,

returns 1 if the PETSc version is 3.22 (any subminor version is allowed). While

returns 1 if the PETSc version is 3.21 or higher.

Though we try to avoid making changes to the PETSc API, they are inevitable; thus we provide tools to help manage one’s application to be robust to such changes.

prints out 1 if the PETSc version matches xxx.yyy[.zzz] and 0 otherwise. The command works in a similar way for lt, le, gt, and ge. This allows your application configure script, or makefile or CMake file to check if the PETSc version is compatible with application even before beginning to compile your code.

PETSC_VERSION_EQ(MAJOR,MINOR,SUBMINOR)

PETSC_VERSION_LT(MAJOR,MINOR,SUBMINOR)

PETSC_VERSION_LE(MAJOR,MINOR,SUBMINOR)

PETSC_VERSION_GT(MAJOR,MINOR,SUBMINOR)

PETSC_VERSION_GE(MAJOR,MINOR,SUBMINOR)

may be used in the source code to choose different code paths or error out depending on the PETSc version.

gives access to the version at runtime.

PETSc for Fortran Users

Using MATLAB with PETSc

**Examples:**

Example 1 (bash):
```bash
$PETSC_DIR/include/petscversion.h
```

Example 2 (unknown):
```unknown
PETSC_VERSION_MAJOR
```

Example 3 (unknown):
```unknown
PETSC_VERSION_MINOR
```

Example 4 (unknown):
```unknown
PETSC_VERSION_SUBMINOR
```

---

## Getting Started#

**URL:** https://petsc.org/release/manual/getting_started/

**Contents:**
- Getting Started#
- Suggested Reading#
- Running PETSc Programs#
- Writing PETSc Programs#
  - Error Checking#
- Simple PETSc Examples#
  - Include Files#
  - The Options Database#
  - Vectors#
  - Matrices#

PETSc consists of a collection of classes, which are discussed in detail in later parts of the manual (The Solvers in PETSc/TAO and Additional Information). The important PETSc classes include

index sets (IS), for indexing into vectors, renumbering, permuting, etc;

Vectors and Parallel Data (Vec);

(generally sparse) Matrices (Mat)

KSP: Linear System Solvers (KSP);

preconditioners, including multigrid, block solvers, patch solvers, and sparse direct solvers (PC);

SNES: Nonlinear Solvers (SNES);

TS: Scalable ODE and DAE Solvers for solving time-dependent (nonlinear) PDEs, including support for differential-algebraic-equations, and the computation of adjoints (sensitivities/gradients of the solutions) (TS);

scalable TAO: Optimization Solvers including a rich set of gradient-based optimizers, Newton-based optimizers and optimization with constraints (Tao).

{any}ch_regressor (PetscRegressor)

DM Basics code for managing interactions between mesh data structures and vectors, matrices, and solvers (DM);

Each class consists of an abstract interface (simply a set of calling sequences corresponding to an abstract base class in C++) and an implementation for each algorithm and data structure. This design enables easy comparison and use of different algorithms (for example, experimenting with different Krylov subspace methods, preconditioners, or truncated Newton methods). Hence, PETSc provides a rich environment for modeling scientific applications as well as for rapid algorithm design and prototyping.

The classes enable easy customization and extension of both algorithms and implementations. This approach promotes code reuse and flexibility. The PETSc infrastructure creates a foundation for building large-scale applications.

It is useful to consider the interrelationships among different pieces of PETSc. Numerical Libraries in PETSc is a diagram of some of these pieces. The figure illustrates the library’s hierarchical organization, enabling users to employ the most appropriate solvers for a particular problem.

Fig. 1 Numerical Libraries in PETSc#

The manual is divided into four parts:

Introduction to PETSc

The Solvers in PETSc/TAO

DM: Interfacing Between Solvers and Models/Discretizations

Additional Information

Introduction to PETSc describes the basic procedure for using the PETSc library and presents simple examples of solving linear systems with PETSc. This section conveys the typical style used throughout the library and enables the application programmer to begin using the software immediately.

The Solvers in PETSc/TAO explains in detail the use of the various PETSc algebraic objects, such as vectors, matrices, index sets, and PETSc solvers, including linear and nonlinear solvers, time integrators, and optimization support.

DM: Interfacing Between Solvers and Models/Discretizations details how a user’s models and discretizations can easily be interfaced with the solvers by using the DM construct.

Additional Information describes a variety of useful information, including profiling, the options database, viewers, error handling, and some details of PETSc design.

Visual Studio Code, Eclipse, Emacs, and Vim users may find their development environment’s options for searching in the source code are useful for exploring the PETSc source code. Details of this feature are provided in Developer Environments.

Note to Fortran Programmers: In most of the manual, the examples and calling sequences are given for the C/C++ family of programming languages. However, Fortran programmers can use all of the functionality of PETSc from Fortran, with only minor differences in the user interface. PETSc for Fortran Users provides a discussion of the differences between using PETSc from Fortran and C, as well as several complete Fortran examples.

Note to Python Programmers: To program with PETSc in Python, you need to enable Python bindings (i.e. petsc4py) with the configure option --with-petsc4py=1. See the PETSc installation guide for more details.

Before using PETSc, the user must first set the environmental variable PETSC_DIR to indicate the full path of the PETSc home directory. For example, under the Unix bash shell, a command of the form

can be placed in the user’s .bashrc or other startup file. In addition, the user may need to set the environment variable $PETSC_ARCH to specify a particular configuration of the PETSc libraries. Note that $PETSC_ARCH is just a name selected by the installer to refer to the libraries compiled for a particular set of compiler options and machine type. Using different values of $PETSC_ARCH allows one to switch between several different sets (say debug and optimized versions) of libraries easily. To determine if you need to set $PETSC_ARCH, look in the directory indicated by $PETSC_DIR, if there are subdirectories beginning with arch then those subdirectories give the possible values for $PETSC_ARCH.

See Tutorials, by Mathematical Problem to immediately jump in and run PETSc code.

All PETSc programs use the MPI (Message Passing Interface) standard for message-passing communication [For94]. Thus, to execute PETSc programs, users must know the procedure for beginning MPI jobs on their selected computer system(s). For instance, when using the MPICH implementation of MPI and many others, the following command initiates a program that uses eight processors:

PETSc also provides a script that automatically uses the correct mpiexec for your configuration.

Certain options are supported by all PETSc programs. We list a few particularly useful ones below; a complete list can be obtained by running any PETSc program with the option -help.

-log_view - summarize the program’s performance (see Profiling)

-fp_trap - stop on floating-point exceptions; for example divide by zero

-malloc_dump - enable memory tracing; dump list of unfreed memory at conclusion of the run, see Detecting Memory Allocation Problems and Memory Usage,

-malloc_debug - enable memory debugging (by default, this is activated for the debugging version of PETSc), see Detecting Memory Allocation Problems and Memory Usage,

-start_in_debugger [(noxterm)],[(gdb|lldb|...)] [-display name] - start all (or a subset of the) processes in a debugger. See Debugging, for more information on debugging PETSc programs.

-on_error_attach_debugger [(noxterm)],[(gdb|lldb|...)] [-display name] - start debugger only on encountering an error

-info - print a great deal of information about what the program is doing as it runs

-version - display the version of PETSc being used

Most PETSc programs begin with a call to

which initializes PETSc and MPI. The arguments argc and argv are the usual command line arguments in C and C++ programs. The argument file optionally indicates an alternative name for the PETSc options file, .petscrc, which resides by default in the user’s home directory. Runtime Options provides details regarding this file and the PETSc options database, which can be used for runtime customization. The final argument, help, is an optional character string that will be printed if the program is run with the -help option. In Fortran, the initialization command has the form

where the file argument is optional.

PetscInitialize() automatically calls MPI_Init() if MPI has not been not previously initialized. In certain circumstances in which MPI needs to be initialized directly (or is initialized by some other library), the user can first call MPI_Init() (or have the other library do it), and then call PetscInitialize(). By default, PetscInitialize() sets the PETSc “world” communicator PETSC_COMM_WORLD to MPI_COMM_WORLD.

For those unfamiliar with MPI, a communicator indicates a collection of processes that will be involved in a calculation or communication. Communicators have the variable type MPI_Comm. In most cases, users can employ the communicator PETSC_COMM_WORLD to indicate all processes in a given run and PETSC_COMM_SELF to indicate a single process.

MPI provides routines for generating new communicators consisting of subsets of processors, though most users rarely need to use these. The book Using MPI, by Lusk, Gropp, and Skjellum [GLS94] provides an excellent introduction to the concepts in MPI. See also the MPI homepage. Note that PETSc users need not program much message passing directly with MPI, but they must be familiar with the basic concepts of message passing and distributed memory computing.

All PETSc programs should call PetscFinalize() as their final (or nearly final) statement. This routine handles options to be called at the conclusion of the program and calls MPI_Finalize() if PetscInitialize() began MPI. If MPI was initiated externally from PETSc (by either the user or another software package), the user is responsible for calling MPI_Finalize().

Most PETSc functions return a PetscErrorCode, an integer indicating whether an error occurred during the call. The error code is set to be nonzero if an error has been detected; otherwise, it is zero. For the C/C++ interface, the error variable is the routine’s return value, while for the Fortran version, each PETSc routine has an integer error variable as its final argument.

One should always check these routine values as given below in the C/C++ formats, respectively:

These macros check the returned error code, and if it is nonzero, they call the PETSc error handler and then return from the function with the error code. The macros above should be used on all PETSc calls to enable a complete error traceback. See Error Checking for more details on PETSc error handling.

To help the user use PETSc immediately, we begin with a simple uniprocessor example that solves the one-dimensional Laplacian problem with finite differences. This sequential code illustrates the solution of a linear system with KSP, the interface to the preconditioners, Krylov subspace methods and direct linear solvers of PETSc. Following the code, we highlight a few of the most important parts of this example.

Listing: KSP Tutorial src/ksp/ksp/tutorials/ex1.c

The C/C++ include files for PETSc should be used via statements such as

where petscksp.h is the include file for the linear solver library. Each PETSc program must specify an include file corresponding to the highest level PETSc objects needed within the program; all of the required lower level include files are automatically included within the higher level files. For example, petscksp.h includes petscmat.h (matrices), petscvec.h (vectors), and petscsys.h (base PETSc file). The PETSc include files are located in the directory $PETSC_DIR/include. See Modules and Include Files for a discussion of PETSc include files in Fortran programs.

As shown in Simple PETSc Examples, the user can input control data at run time using the options database. In this example the command PetscOptionsGetInt(NULL,NULL,"-n",&n,NULL); checks whether the user has provided a command line option to set the value of n, the problem dimension. If so, the variable n is set accordingly; otherwise, n remains unchanged. A complete description of the options database may be found in Runtime Options.

One creates a new parallel or sequential vector, x, of global dimension M with the commands

where comm denotes the MPI communicator and m is the optional local size which may be PETSC_DECIDE. The type of storage for the vector may be set with either calls to VecSetType() or VecSetFromOptions(). Additional vectors of the same type can be formed with

respectively set all the components of a vector to a particular scalar value and assign a different value to each component. More detailed information about PETSc vectors, including their basic operations, scattering/gathering, index sets, and distributed arrays is available in Chapter Vectors and Parallel Data.

Note the use of the PETSc variable type PetscScalar in this example. PetscScalar is defined to be double in C/C++ (or correspondingly double precision in Fortran) for versions of PETSc that have not been compiled for use with complex numbers. The PetscScalar data type enables identical code to be used when the PETSc libraries have been compiled for use with complex numbers. Numbers discusses the use of complex numbers in PETSc programs.

The usage of PETSc matrices and vectors is similar. The user can create a new parallel or sequential matrix, A, which has M global rows and N global columns, with the routines

where the matrix format can be specified at runtime via the options database. The user could alternatively specify each processes’ number of local rows and columns using m and n.

Generally, one then sets the “type” of the matrix, with, for example,

This causes the matrix A to use the compressed sparse row storage format to store the matrix entries. See MatType for a list of all matrix types. Values can then be set with the command

After all elements have been inserted into the matrix, it must be processed with the pair of commands

Matrices discusses various matrix formats as well as the details of some basic matrix manipulation routines.

After creating the matrix and vectors that define a linear system, Ax \(=\) b, the user can then use KSP to solve the system with the following sequence of commands:

The user first creates the KSP context and sets the operators associated with the system (matrix that defines the linear system, Amat and matrix from which the preconditioner is constructed, Pmat ). The user then sets various options for customized solutions, solves the linear system, and finally destroys the KSP context. The command KSPSetFromOptions() enables the user to customize the linear solution method at runtime using the options database, which is discussed in Runtime Options. Through this database, the user not only can select an iterative method and preconditioner, but can also prescribe the convergence tolerance, set various monitoring routines, etc. (see, e.g., Profiling Programs).

KSP: Linear System Solvers describes in detail the KSP package, including the PC and KSP packages for preconditioners and Krylov subspace methods.

PETSc provides an interface to tackle nonlinear problems called SNES. SNES: Nonlinear Solvers describes the nonlinear solvers in detail. We highly recommend most PETSc users work directly with SNES, rather than using PETSc for the linear problem and writing their own nonlinear solver. Similarly, users should use TS rather than rolling their own time integrators.

As noted above, PETSc functions return a PetscErrorCode, which is an integer indicating whether an error has occurred during the call. Below, we indicate a traceback generated by error detection within a sample PETSc program. The error occurred on line 3618 of the file $PETSC_DIR/src/mat/impls/aij/seq/aij.c and was caused by trying to allocate too large an array in memory. The routine was called in the program ex3.c on line 66. See Error Checking for details regarding error checking when using the PETSc Fortran interface.

When running the debug version [1] of the PETSc libraries, it checks for memory corruption (writing outside of array bounds , etc.). The macro CHKMEMQ can be called anywhere in the code to check the current status of the memory for corruption. By putting several (or many) of these macros into your code, you can usually easily track down in what small segment of your code the corruption has occurred. One can also use Valgrind to track down memory errors; see the FAQ.

For complete error handling, calls to MPI functions should be made with PetscCallMPI(MPI_Function(Args)). In Fortran subroutines use PetscCallMPI(MPI_Function(Args, ierr)) and in Fortran main use PetscCallMPIA(MPI_Function(Args, ierr)).

PETSc has a small number of C/C++-only macros that do not explicitly return error codes. These are used in the style

and include PetscOptionsBegin(), PetscOptionsEnd(), PetscObjectOptionsBegin(), PetscOptionsHeadBegin(), PetscOptionsHeadEnd(), PetscDrawCollectiveBegin(), PetscDrawCollectiveEnd(), MatPreallocateEnd(), and MatPreallocateBegin(). These should not be checked for error codes. Another class of functions with the Begin() and End() paradigm including MatAssemblyBegin(), and MatAssemblyEnd() do return error codes that should be checked.

PETSc also has a set of C/C++-only macros that return an object, or NULL if an error has been detected. These include PETSC_VIEWER_STDOUT_WORLD, PETSC_VIEWER_DRAW_WORLD, PETSC_VIEWER_STDOUT_(MPI_Comm), and PETSC_VIEWER_DRAW_(MPI_Comm).

Finally PetscObjectComm((PetscObject)x) returns the communicator associated with the object x or MPI_COMM_NULL if an error was detected.

Numerical computing today has multiple levels of parallelism (concurrency).

Low-level, single instruction multiple data (SIMD) parallelism or, somewhat similar, on-GPU parallelism,

medium-level, multiple instruction multiple data shared memory parallelism (thread parallelism), and

high-level, distributed memory parallelism.

Traditional CPUs support the lower two levels via, for example, Intel AVX-like instructions (CPU SIMD parallelism) and Unix threads, often managed by using OpenMP pragmas (CPU OpenMP parallelism), (or multiple processes). GPUs also support the lower two levels via kernel functions (GPU kernel parallelism) and streams (GPU stream parallelism). Distributed memory parallelism is created by combining multiple CPUs and/or GPUs and using MPI for communication (MPI Parallelism).

In addition, there is also concurrency between computations (floating point operations) and data movement (from memory to caches and registers and via MPI between distinct memory nodes).

PETSc supports all these parallelism levels, but its strongest support is for MPI-based distributed memory parallelism.

Since PETSc uses the message-passing model for parallel programming and employs MPI for all interprocessor communication, the user can employ MPI routines as needed throughout an application code. However, by default, the user is shielded from many of the details of message passing within PETSc since these are hidden within parallel objects, such as vectors, matrices, and solvers. In addition, PETSc provides tools such as vector scatter and gather to assist in the management of parallel data.

Recall that the user must specify a communicator upon creation of any PETSc object (such as a vector, matrix, or solver) to indicate the processors over which the object is to be distributed. For example, as mentioned above, some commands for matrix, vector, and linear solver creation are:

The creation routines are collective on all processes in the communicator; thus, all processors in the communicator must call the creation routine. In addition, if a sequence of collective routines is being used, they must be called in the same order on each process.

The next example, given below, illustrates the solution of a linear system in parallel. This code, corresponding to KSP Tutorial ex2, handles the two-dimensional Laplacian discretized with finite differences, where the linear system is again solved with KSP. The code performs the same tasks as the sequential version within Simple PETSc Examples. Note that the user interface for initiating the program, creating vectors and matrices, and solving the linear system is exactly the same for the uniprocessor and multiprocessor examples. The primary difference between the examples in Simple PETSc Examples and here is each processor forms only its local part of the matrix and vectors in the parallel case.

Listing: KSP Tutorial src/ksp/ksp/tutorials/ex2.c

SIMD parallelism occurs most commonly in the Intel advanced vector extensions (AVX) families of instructions (see Wikipedia). It may be automatically used by the optimizing compiler or in low-level libraries that PETSc uses, such as BLAS (see BLIS), or rarely, directly in PETSc C/C++ code, as in MatMult_SeqSELL.

Compute nodes are the building blocks of HPC systems. A compute node (sometimes called a shared-memory node) consists of one or more physical CPUs. A compute node contains multiple cores that have access to a common memory. Within a compute node, the OS might freely migrate OS threads (independent streams of instructions) and processes between cores, unless constrained. Parallel HPC systems consist of multiple compute nodes connected via a network. On conventional clusters, OS threads and processes cannot migrate between compute nodes.

OpenMP parallelism is thread parallelism within a compute node. Multiple threads process data and perform computations on different parts of memory that is shared (accessible) by all threads. The OpenMP model is based on inserting pragmas into code, indicating that a series of instructions (often within a loop) can be run in parallel. This is also called a fork-join model of parallelism since much of the code remains sequential and only the computationally expensive parts in the ‘parallel region’ are parallel. Thus, OpenMP makes it relatively easy to add some parallelism to a conventional sequential code in a shared memory environment.

POSIX threads (pthreads) is a library that may be called from C/C++. The library contains routines to create, join, and remove threads, plus manage communications and synchronizations between threads. Pthreads is rarely used directly in numerical libraries and applications. Sometimes OpenMP is implemented on top of pthreads.

When using OpenMP parallelism with an MPI code, one must not over-subscribe the hardware resources. For example, if MPI already has one MPI process (rank) per hardware core, then using four OpenMP threads per MPI process will slow the code down since one core must switch back and forth between four OpenMP threads.

For application codes that use certain external packages, including BLAS/LAPACK, SuperLU_DIST, MUMPS, MKL, and SuiteSparse, one can build PETSc and these packages to take advantage of OpenMP by using the configure option --with-openmp. The number of OpenMP threads used in the application can be controlled with the PETSc command line option -omp_num_threads num or the environmental variable OMP_NUM_THREADS. Running a PETSc program with -omp_view will display the number of threads used. The default number is often absurdly high for the given hardware, so we recommend always setting it appropriately.

Users can also put OpenMP pragmas into their own code. However, since standard PETSc is not thread-safe, they should not, in general, call PETSc routines from inside the parallel regions.

There is an OpenMP thread-safe subset of PETSc that may be configured for using --with-threadsafety (often used along with --with-openmp or --download-concurrencykit). KSP Tutorial ex61f demonstrates how this may be used with OpenMP. In this mode, one may have individual OpenMP threads that each manage their own (sequential) PETSc objects (each thread can interact only with its own objects). This is useful when one has many small systems (or sets of ODEs) that must be integrated in an “embarrassingly parallel” fashion on multicore systems.

The ./configure option --with-openmp-kernels causes some PETSc numerical kernels to be compiled using OpenMP pragmas to take advantage of multiple cores. On each compute node, the product of the number of MPI processes and the number of OpenMP threads per MPI process must not exceed the number of cores; otherwise, the code will slow down dramatically due to over-subscription.

PETSc’s MPI-based linear solvers may be accessed from a sequential or non-MPI OpenMP program, see Using PETSc’s MPI parallel linear solvers from a non-MPI program.

Edward A. Lee, The Problem with Threads, Technical Report No. UCB/EECS-2006-1 January [DOI] 10, 2006

GPUs offer at least two levels of clearly defined parallelism. Kernel-level parallelism is much like SIMD parallelism applied to loops; many “iterations” of the loop index run on different hardware in “lock-step”. PETSc utilizes this parallelism with three similar but slightly different models:

CUDA, which is provided by NVIDIA and runs on NVIDIA GPUs

HIP, provided by AMD, which can, in theory, run on both AMD and NVIDIA GPUs

and Kokkos, an open-source package that provides a slightly higher-level programming model to utilize GPU kernels.

To utilize this one configures PETSc with either --with-cuda or --with-hip and, if they plan to use Kokkos, also --download-kokkos --download-kokkos-kernels.

In the GPU programming model that PETSc uses, the GPU memory is distinct from the CPU memory. This means that data that resides on the CPU memory must be copied to the GPU (often, this copy is done automatically by the libraries, and the user does not need to manage it) if one wishes to use the GPU computational power on it. This memory copy is slow compared to the GPU speed; hence, it is crucial to minimize these copies. This often translates to trying to do almost all the computation on the GPU and not constantly switching between computations on the CPU and the GPU on the same data.

PETSc utilizes GPUs by providing vector and matrix classes (Vec and Mat) specifically written to run on the GPU. However, since it is difficult to write an entire PETSc code that runs only on the GPU, one can also access and work with (for example, put entries into) the vectors and matrices on the CPU. The vector classes are VECCUDA, MATAIJCUSPARSE, VECKOKKOS, MATAIJKOKKOS, and VECHIP (matrices are not yet supported by PETSc with HIP).

More details on using GPUs from PETSc will follow in this document.

Please contribute to this document.

The output below illustrates compiling and running a PETSc program using MPICH on a macOS laptop. Note that different machines will have compilation commands as determined by the configuration process. See Writing C/C++ or Fortran Applications for a discussion about how to compile your PETSc programs. Users who are experiencing difficulties linking PETSc programs should refer to the FAQ.

The option -log_view activates printing of a performance summary, including times, floating point operation (flop) rates, and message-passing activity. Profiling provides details about profiling, including the interpretation of the output data below. This particular example involves the solution of a linear system on one processor using GMRES and ILU. The low floating point operation (flop) rates in this example are because the code solved a tiny system. We include this example merely to demonstrate the ease of extracting performance information.

The examples throughout the library demonstrate the software usage and can serve as templates for developing custom applications. We suggest that new PETSc users examine programs in the directories $PETSC_DIR/src/<library>/tutorials where <library> denotes any of the PETSc libraries (listed in the following section), such as SNES or KSP, TS, or TAO. The manual pages at https://petsc.org/release/documentation/ provide links (organized by routine names and concepts) to the tutorial examples.

To develop an application program that uses PETSc, we suggest the following:

Download and install PETSc.

For completely new applications

Make a directory for your source code: for example, mkdir $HOME/application

Change to that directory, for example, cd $HOME/application

Copy an example in the directory that corresponds to the problems of interest into your directory, for example, cp $PETSC_DIR/src/snes/tutorials/ex19.c app.c

Select an application build process. The PETSC_DIR (and PETSC_ARCH if the --prefix=directoryname option was not used when configuring PETSc) environmental variable(s) must be set for any of these approaches.

make (recommended). It uses the pkg-config tool and is the recommended approach. Copy $PETSC_DIR/share/petsc/Makefile.user or $PETSC_DIR/share/petsc/Makefile.basic.user to your directory, for example, cp $PETSC_DIR/share/petsc/Makefile.user makefile

Examine the comments in this makefile.

Makefile.user uses the pkg-config tool and is the recommended approach.

Use make app to compile your program.

CMake. Copy $PETSC_DIR/share/petsc/CMakeLists.txt to your directory, for example, cp $PETSC_DIR/share/petsc/CMakeLists.txt CMakeLists.txt

Edit CMakeLists.txt, read the comments on usage, and change the name of the application from ex1 to your application executable name.

Run the program, for example, ./app

Start to modify the program to develop your application.

For adding PETSc to an existing application

Start with a working version of your code that you build and run to confirm that it works.

Upgrade your build process. The PETSC_DIR (and PETSC_ARCH if the --prefix=directoryname option was not used when configuring PETSc) environmental variable(s) must be set for any of these approaches.

Using make. Update the application makefile to add the appropriate PETSc include directories and libraries.

Recommended approach. Examine the comments in $PETSC_DIR/share/petsc/Makefile.user and transfer selected portions of that file to your makefile.

Minimalist. Add the line

to the bottom of your makefile. This will provide a set of PETSc-specific make variables you may use in your makefile. See the comments in the file $PETSC_DIR/share/petsc/Makefile.basic.user for details on the usage.

Simple, but hands the build process over to PETSc’s control. Add the lines

to the bottom of your makefile. See the comments in the file $PETSC_DIR/share/petsc/Makefile.basic.user for details on the usage. Since PETSc’s rules now control the build process, you will likely need to simplify and remove much of the material that is in your makefile.

Not recommended since you must change your makefile for each new configuration/computing system. This approach does not require the environmental variable PETSC_DIR to be set when building your application since the information will be hardwired in your makefile. Run the following command in the PETSc root directory to get the information needed by your makefile:

All the libraries listed need to be linked into your executable, and the include directories and flags need to be passed to the compiler(s). Usually, this is done by setting LDFLAGS=<list of library flags and libraries> and CFLAGS=<list of -I and other flags> and FFLAGS=<list of -I and other flags> etc in your makefile.

Using CMake. Update the application CMakeLists.txt by examining the code and comments in $PETSC_DIR/share/petsc/CMakeLists.txt

Rebuild your application and ensure it still runs correctly.

Add a PetscInitialize() near the beginning of your code and PetscFinalize() near the end with appropriate include commands (and use statements in Fortran).

Rebuild your application and ensure it still runs correctly.

Slowly start utilizing PETSc functionality in your code, and ensure that your code continues to build and run correctly.

Though PETSc has a large API, conceptually, it’s rather simple. There are three abstract basic data objects (classes): index sets, IS, vectors, Vec, and matrices, Mat. Plus, a larger number of abstract algorithm objects (classes) starting with: preconditioners, PC, Krylov solvers, KSP, and so forth.

Let Object represent any of these objects. Objects are created with

The object is initially empty, and little can be done with it. A particular implementation of the class is associated with the object by setting the object’s “type”, where type is merely a string name of an implementation class using

Some objects support subclasses, which are specializations of the type. These are set with

For example, within TS one may do

The abstract class TS can embody any ODE/DAE integrator scheme. This example creates an additive Runge-Kutta ODE/DAE IMEX integrator, whose type name is TSARKIMEX, using a 3rd-order scheme with an L-stable implicit part, whose subtype name is TSARKIMEX3.

To allow PETSc objects to be runtime configurable, PETSc objects provide a universal way of selecting types (classes) and subtypes at runtime from what is referred to as the PETSc “options database”. The code above can be replaced with

now, both the type and subtype can be conveniently set from the command line

The object’s type (implementation class) or subclass can also be changed at any time simply by calling TSSetType() again (though to override command line options, the call to TSSetType() must be made _after_ TSSetFromOptions()). For example:

Since the later call always overrides the earlier call, the second form shown is rarely – if ever – used, as it is less flexible than configuring command line settings.

The standard methods on an object are of the general form.

Particular types and subtypes of objects may have their own methods, which are given in the form

where Name and SubName are the type and subtype names (for example, as above TSARKIMEX and 3. Most “set” operations have options database versions with the same names in lower case, separated by underscores, and with the word “set” removed. For example,

can be set at the command line with

A special subset of type-specific methods is ignored if the type does not match the function name. These are usually setter functions that control some aspect specific to the subtype. Note that we leveraged this functionality in the MPI example above (MPI Parallelism) by calling Mat*SetPreallocation() for a number of different matrix types. As another example,

These allow cleaner application code since it does not have many if statements to avoid inactive methods. That is, one does not need to write code like

Many “get” routines give one temporary access to an object’s internal data. They are used in the style

Objects obtained with a “get” routine should be returned with a “restore” routine, generally within the same function. Objects obtained with a “create” routine should be freed with a “destroy” routine.

There may be variants of the “get” routines that give more limited access to the obtained object. For example,

Objects can be displayed (in a large number of ways) with

Where PetscViewer is an abstract object that can represent standard output, an ASCII or binary file, a graphical window, etc. The second variant allows the user to delay until runtime the decision of what viewer and format to use to view the object or if to view the object at all.

Objects are destroyed with

Fig. 2 Sample lifetime of a PETSc object#

The user may wish to override or provide custom functionality in many situations. This is handled via callbacks, which the library will call at the appropriate time. The most general way to apply a callback has this form:

where ObjectCallbackSetter() is a callback setter such as SNESSetFunction(). callbackfunction() is what will be called by the library, ctx is an optional data structure (array, struct, PETSc object) that is used by callbackfunction() and contextdestroy(PetscCtx ctx) is an optional function that will be called when obj is destroyed to free anything in ctx. The use of the contextdestroy() allows users to “set and forget” data structures that will not be needed elsewhere but still need to be deleted when no longer needed. Here is an example of the use of a full-fledged callback

Occasionally, routines to set callback functions take additional data objects that will be used by the object but are not context data for the function. For example,

The r vector is an optional argument provided by the user, which will be used as work-space by SNES. Note that this callback does not provide a way for the user to have the ctx destroyed when the SNES object is destroyed; the users must ensure that they free it at an appropriate time. There is no logic to the various ways PETSc accepts callback functions in different places in the code.

See Tao use of PETSc and callbacks for a cartoon on callbacks in Tao.

We conclude this introduction with an overview of the organization of the PETSc software. The root directory of PETSc contains the following directories:

doc The source code and Python scripts for building the website and documentation

lib/petsc/conf - Base PETSc configuration files that define the standard make variables and rules used by PETSc

include - All include files for PETSc that are visible to the user.

include/petsc/finclude - PETSc Fortran include files.

include/petsc/private - Private PETSc include files that should not need to be used by application programmers.

share - Some small test matrices and other data files

src - The source code for all PETSc libraries, which currently includes

ksp - complete linear equations solvers,

ksp - Krylov subspace accelerators,

pc - preconditioners,

snes - nonlinear solvers

ts - ODE/DAE solvers and timestepping,

ml - Machine Learning

regressor - Regression solvers

da - Ensemble data assimilation

dm - data management between meshes and solvers, vectors, and matrices,

sys - general system-related routines,

logging - PETSc logging and profiling routines,

classes - low-level classes

draw - simple graphics,

viewer - a mechanism for printing and visualizing PETSc objects,

bag - mechanism for saving and loading from disk user data stored in C structs.

random - random number generators.

Each PETSc source code library directory has the following subdirectories:

tutorials - Programs designed to teach users about PETSc. These codes can serve as templates for applications.

tests - Programs designed for thorough testing of PETSc. As such, these codes are not intended for examination by users.

interface - Provides the abstract base classes for the objects. The code here does not know about particular implementations and does not perform operations on the underlying numerical data.

impls - Source code for one or more implementations of the class for particular data structures or algorithms.

utils - Utility routines. The source here may know about the implementations, but ideally, will not know about implementations for other components.

MPI Forum. MPI: a message-passing interface standard. International J. Supercomputing Applications, 1994.

William Gropp, Ewing Lusk, and Anthony Skjellum. Using MPI: Portable Parallel Programming with the Message Passing Interface. MIT Press, 1994.

Configure PETSc with --with-debugging.

The Solvers in PETSc/TAO

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor)
```

Example 2 (sass):
```sass
--with-petsc4py=1
```

Example 3 (bash):
```bash
$ export PETSC_DIR=$HOME/petsc
```

Example 4 (bash):
```bash
$PETSC_ARCH
```

---

## PetscFinalized#

**URL:** https://petsc.org/release/manualpages/Sys/PetscFinalized/

**Contents:**
- PetscFinalized#
- Synopsis#
- Output Parameter#
- See Also#
- Level#
- Location#

Determine whether PetscFinalize() has been called yet

isFinalized - PETSC_TRUE if PETSc is finalized, PETSC_FALSE otherwise

PetscInitialize(), PetscInitializeNoArguments(), PetscInitializeFortran()

src/sys/objects/pinit.c

Index of all Sys routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscFinalized(PetscBool *isFinalized)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscFinalize#

**URL:** https://petsc.org/release/manualpages/Sys/PetscFinalize/

**Contents:**
- PetscFinalize#
- Synopsis#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Checks for options to be called at the conclusion of a PETSc program and frees any remaining PETSc objects and data structures. of the program. Automatically calls MPI_Finalize() if the user had not called MPI_Init() before calling PetscInitialize().

Collective on PETSC_COMM_WORLD

-options_view - Calls PetscOptionsView() to display all options in the database

-options_left - Prints unused options that remain in the database (default value is true)

-objects_dump [all] - Prints list of objects allocated by the user that have not been freed, the option all cause all outstanding objects to be listed

-mpidump - Calls PetscMPIDump()

-malloc_dump [filename] - Calls PetscMallocDump(), displays all memory allocated that has not been freed

-memory_view - Prints total memory usage

-malloc_view [filename] - Prints list of all memory allocated and in what functions

See PetscInitialize() for other runtime options.

You can call PetscInitialize() after PetscFinalize() but only with MPI-Uni or if you called MPI_Init() before ever calling PetscInitialize().

PetscInitialize(), PetscOptionsView(), PetscMallocDump(), PetscMPIDump(), PetscEnd()

src/sys/objects/pinit.c

src/mat/tutorials/ex4.c src/mat/tutorials/ex20f.F90 src/mat/tutorials/ex18.c src/mat/tutorials/ex1.c src/mat/tutorials/ex15.c src/mat/tutorials/ex12.c src/mat/tutorials/ex6f.F90 src/mat/tutorials/ex8.c src/mat/tutorials/ex17.c src/mat/tutorials/ex4f.F90

Index of all Sys routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MPI_Finalize()
```

Example 2 (unknown):
```unknown
PetscInitialize()
```

Example 3 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscFinalize(void)
```

Example 4 (unknown):
```unknown
PETSC_COMM_WORLD
```

---

## PetscInitialized#

**URL:** https://petsc.org/release/manualpages/Sys/PetscInitialized/

**Contents:**
- PetscInitialized#
- Synopsis#
- Output Parameter#
- See Also#
- Level#
- Location#

Determine whether PETSc is initialized.

isInitialized - PETSC_TRUE if PETSc is initialized, PETSC_FALSE otherwise

PetscInitialize(), PetscInitializeNoArguments(), PetscInitializeFortran()

src/sys/objects/pinit.c

Index of all Sys routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscInitialized(PetscBool *isInitialized)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
PetscInitializeNoArguments()
```

---

## PetscInitializeFortran#

**URL:** https://petsc.org/release/manualpages/Sys/PetscInitializeFortran/

**Contents:**
- PetscInitializeFortran#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Routine that should be called soon AFTER the call to PetscInitialize() if one is using a C main program that calls Fortran routines that in turn call PETSc routines.

Collective on PETSC_COMM_WORLD

PetscInitializeFortran() initializes some of the default viewers, communicators, etc. for use in the Fortran if a user’s main program is written in C. PetscInitializeFortran() is NOT needed if a user’s main program is written in Fortran; in this case, just calling PetscInitialize() in the main (Fortran) program is sufficient.

This function exists and can be called even if PETSc has been configured with --with-fortran-bindings=0 or --with-fc=0. It just does nothing in that case.

src/sys/objects/finit.c

src/vec/vec/tutorials/ex7.c

Index of all Sys routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscInitialize()
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscInitializeFortran(void)
```

Example 3 (unknown):
```unknown
PETSC_COMM_WORLD
```

Example 4 (unknown):
```unknown
PetscInitializeFortran()
```

---

## PetscInitializeNoArguments#

**URL:** https://petsc.org/release/manualpages/Sys/PetscInitializeNoArguments/

**Contents:**
- PetscInitializeNoArguments#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Calls PetscInitialize() from C/C++ without the command line arguments.

PetscInitialize(), PetscInitializeFortran()

src/sys/objects/pinit.c

src/sys/tutorials/ex4f.F90

Index of all Sys routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscInitialize()
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscInitializeNoArguments(void) PeNS
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
PetscInitializeFortran()
```

---

## PetscInitializeNoPointers#

**URL:** https://petsc.org/release/manualpages/Sys/PetscInitializeNoPointers/

**Contents:**
- PetscInitializeNoPointers#
- Synopsis#
- Input Parameters#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Calls PetscInitialize() from C/C++ without the pointers to argc and args

Collective, No Fortran Support

argc - number of args

args - array of command line arguments

filename - optional name of the program file, pass NULL to ignore

help - optional help, pass NULL to ignore

this is called only by the PETSc Julia interface. Even though it might start MPI it sets the flag to indicate that it did NOT start MPI so that the PetscFinalize() does not end MPI, thus allowing PetscInitialize() to be called multiple times from Julia without the problem of trying to initialize MPI more than once.

Turns off PETSc signal handling to allow Julia to manage signals

PetscInitialize(), PetscInitializeFortran(), PetscInitializeNoArguments()

src/sys/objects/pinit.c

Index of all Sys routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscInitializeNoPointers(int argc, char **args, const char *filename, const char *help)
```

Example 2 (unknown):
```unknown
PetscFinalize()
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscInitialize#

**URL:** https://petsc.org/release/manualpages/Sys/PetscInitialize/

**Contents:**
- PetscInitialize#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Options Database Keys for Option Database#
- Options Database Keys for Profiling#
- Options Database Keys for SAWs#
- Environmental Variables#
- Note#
- Fortran Notes#

Initializes the PETSc database and MPI. PetscInitialize() calls MPI_Init() if that has yet to be called, so this routine should always be called near the beginning of your program – usually the very first line!

Collective on MPI_COMM_WORLD or PETSC_COMM_WORLD if it has been set

argc - count of number of command line arguments

args - the command line arguments

file - [optional] PETSc database file, append “:yaml” to filename to specify YAML options format. Use NULL or empty string to not check for code specific file. Also checks ~/.petscrc, .petscrc and petscrc. Use -skip_petscrc in the code specific file (or command line) to skip ~/.petscrc, .petscrc and petscrc files.

help - [optional] Help message to print, use NULL for no message

If you wish PETSc code to run ONLY on a subcommunicator of MPI_COMM_WORLD, create that communicator first and assign it to PETSC_COMM_WORLD BEFORE calling PetscInitialize(). then do this. If ALL processes in the job are using PetscInitialize() and PetscFinalize() then you don’t need to do this, even if different subcommunicators of the job are doing different things with PETSc.

-help [intro] - prints help method for each option; if intro is given the program stops after printing the introductory help message

-start_in_debugger [(noxterm)],[(gdb|lldb|…)] - Starts program in debugger

-on_error_attach_debugger [(noxterm)],[(gdb|lldb|…)] - Starts debugger when error detected

-on_error_emacs machinename - causes emacsclient to jump to error file if an error is detected

-on_error_abort - calls abort() when error detected (no traceback)

-on_error_mpiabort - calls MPI_abort() when error detected

-error_output_stdout - prints PETSc error messages to stdout instead of the default stderr

-error_output_none - does not print the error messages (but handles errors in the same way as if this was not called)

-debugger_ranks rank1,rank2,… - Indicates MPI ranks to start in debugger

-debugger_pause secs - Pauses debugger, use if it takes a long time for the debugger to start up on your system, sleeptime is number of seconds to sleep

-stop_for_debugger - Print message on how to attach debugger manually to process and wait (-debugger_pause) seconds for attachment

-malloc_dump - prints a list of all unfreed memory at the end of the run

-malloc_test - like -malloc_dump -malloc_debug, only active for debugging build, ignored in optimized build. Often set in PETSC_OPTIONS environmental variable

-malloc_view [filename] - show a list of all allocated memory during PetscFinalize()

-malloc_view_threshold t - only list memory allocations of size greater than t with -malloc_view

-malloc_requested_size - malloc logging will record the requested size rather than (possibly large) size after alignment

-fp_trap - Stops on floating point exceptions

-no_signal_handler - Indicates not to trap error signals

-python exe - Initializes Python, and optionally takes a Python executable name

-mpiuni- allow-multiprocess-launch - allow mpiexec to launch multiple independent MPI-Uni jobs, otherwise a sanity check error is invoked to prevent misuse of MPI-Uni

-skip_petscrc - skip the default option files ~/.petscrc, .petscrc, petscrc

-options_monitor - monitor all set options to standard output for the whole program run

-options_monitor_cancel - cancel options monitoring hard-wired using PetscOptionsMonitorSet()

Options -options_monitor_{all,cancel} are position-independent and apply to all options set since the PETSc start. They can be used also in option files.

See PetscOptionsMonitorSet() to do monitoring programmatically.

See Users-Manual: ch_profiling for details.

-info [filename][:[~]c1,c2,…[:[~]self]] - Prints verbose information for classes c1, c2, etc. See PetscInfo().

-log_sync - Enable barrier synchronization for all events. This option is useful to debug imbalance within each event, however it slows things down and gives a distorted view of the overall runtime.

-log_trace [filename] - Print traces of all PETSc calls to the screen (useful to determine where a program hangs without running in the debugger). See PetscLogTraceBegin().

-log_view [:filename:format][,[:filename:format]…] - Prints summary of flop and timing information to screen or file, see PetscLogView() (up to 4 viewers)

-log_view_memory - Includes in the summary from -log_view the memory used in each event, see PetscLogView().

-log_view_gpu_time - Includes in the summary from -log_view the time used in each GPU kernel, see `PetscLogView().

-log_view_gpu_energy - Includes in the summary from -log_view the energy (estimated with power*gtime) consumed in each GPU kernel, see PetscLogView().

-log_view_gpu_energy_meter - Includes in the summary from -log_view the energy (readings from meters) consumed in each GPU kernel, see PetscLogView().

-log_exclude: c1,c2,… - excludes subset of object classes from logging, for example vec,ksp would exclude the Vec and KSP classes

-log [filename] - Logs profiling information in a dump file, see PetscLogDump().

-log_all [filename] - Same as -log.

-log_mpe [filename] - Creates a logfile viewable by the utility Jumpshot (in MPICH distribution)

-log_perfstubs - Starts a log handler with the perfstubs interface (which is used by TAU)

-log_nvtx - Starts an nvtx log handler for use with Nsight

-log_roctx - Starts an roctx log handler for use with rocprof on AMD GPUs

-viewfromoptions on,off - Enable or disable XXXSetFromOptions() calls, for applications with many small solves turn this off

-get_total_flops - Returns total flops done by all processors

-memory_view - Print memory usage at end of run

-check_pointer_intensity 0,1,2 - if pointers are checked for validity (debug version only), using 0 will result in faster code

-saws_port portnumber - port number to publish SAWs data, default is 8080

-saws_port_auto_select - have SAWs select a new unique port number where it publishes the data, the URL is printed to the screen this is useful when you are running many jobs that utilize SAWs at the same time

-saws_log filename - save a log of all SAWs communication

-saws_https certificate_file - have SAWs use HTTPS instead of HTTP

-saws_root directory - allow SAWs to have access to the given directory to search for requested resources and files

PETSC_TMP - alternative directory to use instead of /tmp

PETSC_SHARED_TMP - /tmp is shared by all processes

PETSC_NOT_SHARED_TMP - each process has its own private /tmp

PETSC_OPTIONS - a string containing additional options for PETSc in the form of command line “-key value” pairs

PETSC_OPTIONS_YAML - (requires configuring PETSc to use libyaml with --download-yaml) a string containing additional options for PETSc in the form of a YAML document

PETSC_VIEWER_SOCKET_PORT - socket number to use for socket viewer

PETSC_VIEWER_SOCKET_MACHINE - machine to use for socket viewer to connect to

If for some reason you must call MPI_Init() separately from PetscInitialize(), call it before PetscInitialize().

In Fortran this routine can be called with

If your main program is C but you call Fortran code that also uses PETSc you need to call PetscInitializeFortran() soon after calling PetscInitialize().

-checkfunctionlist - automatically checks that function lists associated with objects are correctly cleaned up. Produces messages of the form: “function name: MatInodeGetInodeSizes_C” if they are not cleaned up. This flag is always set for the test harness (in framework.py)

PetscFinalize(), PetscInitializeFortran(), PetscGetArgs(), PetscInitializeNoArguments(), PetscLogGpuTime()

src/sys/objects/pinit.c

src/mat/tutorials/ex4.c src/mat/tutorials/ex20f.F90 src/mat/tutorials/ex18.c src/mat/tutorials/ex1.c src/mat/tutorials/ex15.c src/mat/tutorials/ex12.c src/mat/tutorials/ex6f.F90 src/mat/tutorials/ex8.c src/mat/tutorials/ex17.c src/mat/tutorials/ex4f.F90

PetscInitialize_MKL_CPARDISO() in src/mat/impls/aij/mpi/mkl_cpardiso/mkl_cpardiso.c

Index of all Sys routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscInitialize()
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscInitialize(int *argc, char ***args, const char file[], const char help[])
```

Example 3 (unknown):
```unknown
MPI_COMM_WORLD
```

Example 4 (unknown):
```unknown
PETSC_COMM_WORLD
```

---

## PETSc for Fortran Users#

**URL:** https://petsc.org/release/manual/fortran/

**Contents:**
- PETSc for Fortran Users#
- Fortran and MPI#
- Numerical Constants#
- Basic Fortran API Differences#
  - Modules and Include Files#
  - Declaring PETSc Object Variables#
  - Calling Sequences#
  - Error Checking#
  - Passing Arrays To PETSc Functions#
  - Passing null pointers to PETSc functions#

Make sure the suffix of your Fortran files is .F90, not .f or .f90.

By default PETSc uses the MPI Fortran module mpi. To use mpi_f08 run ./configure with --with-mpi-ftn-module=mpi_f08.

We do not recommend it but it is possible to write Fortran code that works with both use mpi or use mpi_f08. You must declare MPI objects using MPIU_XXX (for example MPIU_Comm, which the PETSc include files map to either integer4 or type(MPI_XXX). In addition, you must handle MPIU_Status declarations and access to entries using the Fortran preprocessor. For example,

Since Fortran compilers do not automatically change the length of numerical constant arguments (integer and real) in subroutine calls to the expected length PETSc provides parameters that indicate the constants’ kind.

You must use both PETSc include files and modules. At the beginning of every function and module definition you need something like

The Fortran include files for PETSc are located in the directory $PETSC_DIR/$PETSC_ARCH/include/petsc/finclude and the module files are located in $PETSC_DIR/$PETSC_ARCH/include

The include files are nested, that is, for example, petsc/finclude/petscmat.h automatically includes petsc/finclude/petscvec.h and so on. The modules are also nested. One can use

to include all of them.

You can declare PETSc object variables using either of the following:

PETSc types like PetscInt and PetscReal are simply aliases for basic Fortran types and cannot be written as type(tPetscInt)

PETSc objects are always automatically initialized when declared so you do not need to (and should not) do

To make a variable no longer point to its previously assigned PETSc object use, for example,

Otherwise y will be a dangling pointer whose access will cause a crash.

The calling sequences for the Fortran version are in most cases identical to the C version, except for the error checking variable discussed in Error Checking.

The key differences in handling arguments when calling PETSc functions from Fortran are

One cannot pass a scalar variable to a function expecting an array, Passing Arrays To PETSc Functions.

One must use type specific PETSC_NULL arguments, such as PETSC_NULL_INTEGER, Passing null pointers to PETSc functions.

One must pass pointers to arrays for arguments that output an array, for example PetscScalar, pointer \:\: a(\:), Output Arrays from PETSc functions.

PETSC_DECIDE and friends need to match the argument type, for example PETSC_DECIDE_INTEGER.

When passing floating point numbers into PETSc Fortran subroutines, always make sure you have them marked as double precision (e.g., pass in 10.d0 instead of 10.0 or declare them as PETSc variables, e.g. PetscScalar one = 1.0). Otherwise, the compiler interprets the input as a single precision number, which can cause crashes or other mysterious problems. We highly recommend using the implicit none option at the beginning of each Fortran subroutine and declaring all variables.

In the Fortran version, each PETSc routine has as its final argument an integer error variable. The error code is nonzero if an error has been detected; otherwise, it is zero. For example, the Fortran and C variants of KSPSolve() are given, respectively, below, where ierr denotes the PetscErrorCode error variable:

For proper error handling one should not use the above syntax instead one should use

Many PETSc functions take arrays as arguments; in Fortran they must be passed as arrays even if the “array” is of length one (unlike Fortran 77 where one can pass scalars to functions expecting arrays). When passing a single value one can use the Fortran [] notation to pass the scalar as an array, for example

This trick can only be used for arrays used to pass data into a PETSc routine, it cannot be used for arrays used to receive data from a PETSc routine. For example,

is invalid and will not set val with the correct value.

Many PETSc C functions have the option of passing a NULL argument (for example, the fifth argument of MatCreateSeqAIJ()). From Fortran, users must pass PETSC_NULL_XXX to indicate a null argument (where XXX is INTEGER, DOUBLE, CHARACTER, SCALAR, VEC, MAT, etc depending on the argument type). For example, when no options prefix is desired in the routine PetscOptionsGetInt(), one must use the following command in Fortran:

Where the code expects an array, then use PETSC_NULL_XXX_ARRAY. For example:

When a PETSc function returns multiple arrays, such as DMDAGetOwnershipRanges() and the user does not need certain arrays they must pass PETSC_NULL_XXX_POINTER as the argument. For example,

Arguments that are fully defined Fortran derived types (C structs), such as MatFactorInfo or PetscSFNode, cannot be passed as null from Fortran. A properly defined variable must be passed in for those arguments.

Finally when a subroutine returns a PetscObject through an argument, to check if it is NULL you must use:

will always return true, for any PETSc object.

These specializations with NULL types are required because of Fortran’s strict type checking system and lack of a concept of NULL, the Fortran compiler will often warn you if the wrong NULL type is passed.

For PETSc routine arguments that return an array of PetscInt, PetscScalar, PetscReal or of PETSc objects, one passes in a pointer to an array and the PETSc routine returns an array containing the values. For example,

For PETSc routine arguments that return a character string (array), e.g. const char *str[] pass a string long enough to hold the result. For example,

The result is copied into str.

Similarly, for PETSc routines where the user provides a character array (to be filled) followed by the array’s length, e.g. char name[], size_t nlen. In Fortran pass a string long enough to hold the result, but not the separate length argument. For example,

All matrices, vectors and IS in PETSc use zero-based indexing in the PETSc API regardless of whether C or Fortran is being used. For example, MatSetValues() and VecSetValues() always use zero indexing. See Basic Matrix Operations for further details.

Indexing into Fortran arrays, for example obtained with VecGetArray(), uses the Fortran convention and generally begin with 1 except for special routines such as DMDAVecGetArray() which uses the ranges provided by DMDAGetCorners().

Some PETSc functions take as arguments user-functions and contexts for the function. For example

where func has the calling sequence

and ctx can be almost anything (represented as void * in C).

In Fortran, it has to be a derived type as in

Certain PETSc functions return a context in an argument, for example, SNESGetApplicationContext(). In C, they are handled as a void * pointer so one can write code such as

In Fortran, they must be declared as a pointer with, for example,

But sadly, this alone will not work. One must also specifically tell the Fortran compiler in an interface definition that SNESGetApplicationContext() expects the ctx argument to be a pointer to type(AppCtx) since Fortran forbids pointers to unknown types. PETSc provides macros to provide this information easily using, for example,

One must insert these lines into the Fortran source code where one inserts interface definitions, see, for example, src/snes/tests/ex590.F90. For those interested, the source code of these macros may be found in the generated Fortran include files located at $PETSC_DIR/$PETSC_ARCH/include/petsc/finclude/*.h.

When a function pointer (declared as external in Fortran) is passed as an argument to a PETSc function, it is assumed that this function references a routine written in the same language as the PETSc interface function that was called. For instance, if SNESSetFunction() is called from C, the function must be a C function. Likewise, if it is called from Fortran, the function must be (a subroutine) written in Fortran.

If you are using Fortran classes that have bound functions (methods) as in src/snes/tests/ex18f90.F90, the context cannot be passed to function pointer setting routines, such as SNESSetFunction(). Instead, one must use SNESSetFunctionNoInterface(), and define the interface directly in the user code, see ex18f90.F90 for a full demonstration.

See Writing C/C++ or Fortran Applications.

Sample programs that illustrate the PETSc interface for Fortran are given below, corresponding to Vec Test ex19f, Vec Tutorial ex4f, Draw Test ex5f, and SNES Tutorial ex1f, respectively. We also refer Fortran programmers to the C examples listed throughout the manual, since PETSc usage within the two languages differs only slightly.

Listing: src/vec/vec/tests/ex19f.F90

Listing: src/vec/vec/tutorials/ex4f.F90

Listing: src/sys/classes/draw/tests/ex5f.F90

Listing: src/snes/tutorials/ex1f.F90

The information here applies only if you plan to call your own C functions from Fortran or Fortran functions from C. Different compilers have different methods of naming Fortran routines called from C (or C routines called from Fortran). Most Fortran compilers change the capital letters in Fortran routines to all lowercase. With some compilers, the Fortran compiler appends an underscore to the end of each Fortran routine name; for example, the Fortran routine Dabsc() would be called from C with dabsc_(). Other compilers change all the letters in Fortran routine names to capitals.

PETSc provides two macros (defined in C/C++) to help write portable code that mixes C/C++ and Fortran. They are PETSC_HAVE_FORTRAN_UNDERSCORE and PETSC_HAVE_FORTRAN_CAPS , which will be defined in the file $PETSC_DIR/$PETSC_ARCH/include/petscconf.h based on the compilers conventions. The macros are used, for example, as follows:

Additional Information

Checking the PETSc version

**Examples:**

Example 1 (unknown):
```unknown
./configure
```

Example 2 (sass):
```sass
--with-mpi-ftn-module=mpi_f08
```

Example 3 (elixir):
```elixir
use mpi_f08
```

Example 4 (unknown):
```unknown
type(MPI_XXX)
```

---
