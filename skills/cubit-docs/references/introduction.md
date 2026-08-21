# Introduction, installation, and licensing

## Coreform Cubit Support

**URL:** https://coreform.com/cubit_help/introduction/coreform_cubit_support.htm

**Contents:**
- Coreform Cubit Support

Coreform Cubit users can get product support and help in several ways:

Forum: all users can visit our user-supported forum at https://forum.coreform.com.

The https://coreform.com website includes links to frequently asked questions, training videos, user documentation, and other aids.

Email: all users can send requests for help or bug reports to support@coreform.com.

---

## How to Use This Manual

**URL:** https://coreform.com/cubit_help/introduction/how_to.htm

**Contents:**
- How to Use This Manual

This manual provides specific information about the commands and features of CUBIT. It is divided into chapters, which roughly follow the process in which a finite element model is created, from geometry creation to mesh generation to boundary condition application. Examples are provided in the tutorial chapter. Appendices contain advanced topics, alpha commands, summary of APREPRO functions, FASTQ reference, a troubleshooting guide, and references.

Integrated in CUBIT are algorithms and tools, which are in a user-beware state. As they are further tested (often with the assistance of users) and improved, the tool becomes more stable and production-worthy. Since documentation of the tool is necessary for actual use, we have included the documentation of all available tools. However, a "hammer" icon is placed next to some capabilities as a warning.

---

## Introduction

**URL:** https://coreform.com/cubit_help/introduction/introduction.htm

**Contents:**
- Introduction

Welcome to Coreform Cubit, the comprehensive toolset for mesh generation. Coreform Cubit is a full-featured software toolkit for robust generation of two- and three-dimensional finite element meshes (grids) and geometry preparation. Its main goal is to reduce the time to generate meshes, particularly large hex meshes of complicated, interlocking assemblies. It is a solid-modeler based preprocessor that meshes volumes and surfaces for finite element analysis. Mesh generation algorithms include quadrilateral and triangular paving, 2D and 3D mapping, hex sweeping and multi-sweeping, tetrahedral meshing, and various special purpose primitives. Coreform Cubit contains many algorithms for controlling and automating much of the meshing process, such as automatic scheme selection, interval matching, sweep grouping, and also includes state-of-the-art smoothing algorithms

The Coreform Cubit environment is designed to provide the user with a powerful toolkit of meshing algorithms that require varying degrees of input to produce a complete finite element model. Many Coreform Cubit users want to experiment with capabilities as soon as possible. Hence, Coreform Cubit releases often contain algorithms which are not quite ready for production use. These features are listed in the Appendix, and are accessible to the user by specifying a developer flag.

The overall goal of the Coreform Cubit project is to reduce the time it takes a person to generate an analysis model. Generating meshes for complex, solid model-based geometries requires a variety of tools. Many Coreform Cubit tools are completely automatic, while others require user input. Usually, the automatic choices can be over-ridden by the user if necessary. Most meshing capabilities are integrated into the common Coreform Cubit framework; there are also stand-alone tools like Verde. The user is encouraged to become familiar with all of the available tools, so that he can choose the right one for the job.

---

## Key Features

**URL:** https://coreform.com/cubit_help/introduction/key_features.htm

**Contents:**
- Key Features
- Geometry Creation, Modification, and Healing
- Non-Manifold Topology
- Geometry Decomposition
- Mesh Generation
- Boundary Conditions
- Element Types
- Graphics Display Capabilities
- Graphical User Interface
- Command Line Interface

CUBIT usually relies on the ACIS solid modeling kernel for geometry representation; there is also mesh-based geometry. Other solid model kernels are planned. Geometry is imported or created within CUBIT. Geometry is created bottom-up or through primitives. CUBIT can also read STEP, IGES, and FASTQ files and convert them to the ACIS kernel. SolidWorks, AutoCAD, and some other commercial CAD systems can write SAT files directly.

Once in CUBIT, an ACIS model is modified through Booleans, or tweaking curves and surfaces. Without changing the geometric definition of the model, the topology of the model may be changed using virtual geometry. For example, virtual geometry can be used to composite two surfaces together, erasing the curve dividing them.

Sometimes, an ACIS model is poorly defined. This often happens with translated models. The model can be healed inside CUBIT.

Typical assembly meshes require contiguous mesh across multiple parts in an assembly. CUBIT accomplishes this by taking the two touching surfaces of neighboring volumes, and merging them into a single surface. There will be only one mesh of the surface, and both volume meshes will share that surface mesh. (In contrast, some meshing packages keep two surfaces, and take steps to ensure their mesh connectivity and positions match.)

These shared surfaces are called non-manifold topology. Geometric models are usually imported into CUBIT as manifold (non-shared) models; then, surfaces which pass a geometric and topological comparison are "merged". A similar technique is used to merge model edges and vertices across parts. These comparisons are performed automatically, and can optionally be restricted to subsets of the model (to allow representations of such features as slide lines).

Solid models often require decomposition to make them amenable to hexahedral meshing. CUBIT contains a wide variety of tools for interactive geometry decomposition, and a capability for performing automatic geometry decomposition is also under development.

CUBIT contains a variety of tools for generating meshes in one, two and three dimensions. While the primary focus of CUBIT is on generating unstructured quadrilateral and hexahedral meshes, algorithms are also available for structured mesh generation and triangle/tetrahedral mesh generation. Several algorithms for generating mixed hex-tet meshes are also being developed.

CUBIT uses different boundary conditions for EXODUS-II format and Non-Exodus formats such as ABAQUS, for importing and exporting mesh data. EXODUS represents boundary conditions on meshes using Element Blocks, Nodesets, and Sidesets. Element Blocks are used to group elements by material type. Nodesets are used to group nodes. Other analysis programs can apply nodal boundary conditions to these sets, such as enforced displacement or nodal temperature values. Sidesets are used to group sides of elements, such as faces of hexes or edges of quads. Other analysis programs can apply face-based and edge-based boundary conditions to these sets, for example pressure or heat flux.

Using Element Blocks, Nodesets and Sidesets, a mesh and boundary conditions can be specified in an analysis-independent manner. Typically this specification is combined with an additional data file which designates the specific type of boundary condition (temperature, displacement, pressure, etc.), along with boundary condition values.

Non-Exodus export formats such as Abaqus support more specific boundary condition sets. These sets may include displacements, temperatures, forces, heatflux, pressure, or contact pairs.

CUBIT supports a wide variety of element types, including 1d, 2d, and 3d elements of various orders. Each block has a unique element type. The element type is specified after the block is created, and after mesh generation (recommended). Higher order nodes are generated when the element type is specified. Higher order nodes are projected to curved geometry, depending on the user-settable node constraint flag.

CUBIT uses the VTK package for its graphics and rendering engine. CUBIT can display geometric and mesh entities in several modes, including hidden line, shaded, transparent or wireframe modes. CUBIT supports screen picking of geometric and mesh entities, as well as mouse-controlled view transformations like rotate, pan, and zoom. VTK takes advantage of hardware acceleration on most supported platforms. Image files of any displayed image can also be generated. CUBIT can also be run without graphics, to allow execution in batch mode or over slow network connections.

A full graphical user interface (GUI) with the standard look and feel consistent with major platforms is available on all supported Cubit platforms. The GUI version can improve productivity, making new users aware of the wide range of CUBIT capabilities, and freeing new and experienced users from having to remember esoteric syntax. The GUI and non-GUI versions create and play back identical journal files, making it easier to switch from one environment to the other.

In the command line interface, commands are specified by text rather than mouse clicks. Commands can be entered interactively or in batch mode by playing back a journal file. The command line interface is available in the GUI through a window. The non-GUI version supports graphical picking and echoing to the command line, and also mouse-driven view transformations, but no menus and dialog boxes. The command line and GUI dialog boxes support the APREPRO preprocessor, which allows parameterization of input. The non-GUI version is available on all platforms, including Windows.

---

## Licensing and Activation

**URL:** https://coreform.com/cubit_help/introduction/licensing_activation.htm

**Contents:**
- Licensing and Activation

Please refer to https://coreform.com/support/activation/cubit/activate/ for information on licensing and activation.

---

## Problem Reports and Enhancement Requests

**URL:** https://coreform.com/cubit_help/introduction/problem_reports.htm

**Contents:**
- Problem Reports and Enhancement Requests

Coreform Cubit bugs, problem reports, and enhancement requests can be sent to support@coreform.com.

---

## System Requirements

**URL:** https://coreform.com/cubit_help/introduction/system_requirements.htm

**Contents:**
- System Requirements
- Operating System Requirements
- Hardware Recommendations

Coreform Cubit is distributed as a 64-bit (x86_64) build for Windows and Linux.

Linux: any glibc-based distribution with glibc 2.28 or newer. This includes, but is not limited to:

To check the glibc version on a Linux host, run ldd --version.

Coreform Cubit's continuous-integration acceptance tests run on Windows 11, Ubuntu 22.04, Rocky Linux 8, and Rocky Linux 9. Other platforms meeting the requirements above are not formally tested. Please email support@coreform.com with any questions.

The Graphical User Interface version is available on all supported platforms.

For best results, local displays supporting OpenGL 3.2 or newer is recommended.

Coreform recommends the following minimum hardware specifications:

NOTE: More memory and faster processors are recommended for meshes with very large mesh element counts.

**Examples:**

Example 1 (unknown):
```unknown
ldd --version
```

---

## Trademark Notice

**URL:** https://coreform.com/cubit_help/introduction/trademark.htm

**Contents:**
- Trademark Notice

Coreform Cubit™ is a trademark of Coreform.

CUBIT™ is a trademark of Sandia National Laboratories.

ACIS™ is a proprietary format developed by Spatial Corporation.

Granite is a proprietary format developed by Parametric Technology Corporation

GAMBIT™ is a trademark of Ansys, Inc.

Parasolid™ is a trademark of Siemens.

SolidWorks™ is a trademark of SolidWorks Dassault Systèmes.

Pro/Engineer™ is a trademark of PTC.

Qt and Qt Designer are trademarks of The Qt Company Ltd.

All other trademarks are the property of their respective owners.

---
