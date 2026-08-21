# Coreform-Cubit-Docs-Skill_Docs - Reference

**Pages:** 17

---

## Alpha Commands

**URL:** https://coreform.com/cubit_help/appendix/alpha/alpha.htm

**Contents:**
- Alpha Commands

CUBIT has several functions that are currently in development and are considered "Alpha" features. These features can be can be accessed or hidden within Cubit by typing the following command:

Set Developer Commands {On|OFF}

The commands that are currently developer commands are:

---

## APREPRO

**URL:** https://coreform.com/cubit_help/appendix/aprepro/aprepro.htm

**Contents:**
- APREPRO

Within CUBIT there is support for a programming language called APREPRO (An Algebraic Preprocessor for Parameterizing Finite Element Analyses). In addition to the standard APREPRO functionality, CUBIT extends the language with its own functions to aid in the meshing process. Included here is a summary of the CUBIT-specific APREPRO functionality. For a description of the APREPRO language and its usage, please refer to the APREPRO user's manual (PDF).

Using APREPRO in CUBIT

Note: APREPRO variables can be created and modified from the GUI. Enable/disable the editor from the View/Aprepro editor menu option. The editor is a docking window and can be placed anywhere in the GUI.

---

## APREPRO Functions

**URL:** https://coreform.com/cubit_help/appendix/aprepro/aprepro_functions.htm

**Contents:**
- APREPRO Functions
- Table 1. Geometry Functions
- Table 2. Mesh Functions
- Table 3. Group, Block, and Assemblyl Metadata Functions
- Table 4. ID Functions
- Table 5. Miscellaneous Functions
- Table 6. Pre-defined Variables

CUBIT adds a number of APREPRO functions to aid in the meshing process. A description of each function is available in the categories below.

Acceptable metrics include: shape aspect ratio condition no distortion element area jacobian maximum angle minimum angle relative size scaled jacobian shape and size shear and size shear skew stretch taper warpage

Acceptable metrics include: shape aspect ratio condition no distortion element area jacobian maximum angle minimum angle relative size scaled jacobian shape and size shear and size shear skew stretch taper warpage

Acceptable metrics include: shape aspect ration bet aspect ratio gam aspect ratio condition no diagonal ratio dimension distortion element volume jacobian mass increase ratio mean ratio inradius node distance normalized inradius relative size scaled jacobian shape and size shear and size shear skew stretch taper timestep

Returns the name for the specified attribute index in the block within the given id

Returns the value for the specified attribute index in the block within the given id

Returns the number of blocks in the model.

Returns the number of sidesets in the model.

Returns the number of nodesets in the model.

The following APREPRO variables are predefined in CUBIT.

---

## Available Colors

**URL:** https://coreform.com/cubit_help/appendix/available_colors.htm

**Contents:**
- Available Colors

In addition to color specification by RGB values, all color commands in CUBIT allow the specification of a color name. The following table lists the colors available by ID or name in CUBIT. The table lists the color number (#), color name, and the red, green, and blue components corresponding to each color, for reference.

---

## Element Numbering

**URL:** https://coreform.com/cubit_help/appendix/element_numbering.htm

**Contents:**
- Element Numbering
- Node Numbering
- Side Numbering
- Triangular Shell Element Numbering
  - Node Ordering
  - Side Set Side Ordering

The node numbering used for the basic elements is shown Figure 1. Specific element types of lower order just contain the number of nodes needed for those elements; for example, QUAD4 or QUAD elements use just the first four nodes shown for quadrilaterals in Figure 1.

Figure 1. Local Node Numbering for CUBIT element types

Element sides are used to specify boundary conditions that act over a length or area, for example pressure- or flux-type boundary conditions. Each element side is represented in the Exodus II format by an element number and the local side number for that element. The local side numbering for the basic elements is shown in Figure 2.

Figure 2. Local side numbering for CUBIT element types

A three-dimensional shell element with triangular topology will have the element type 'TRISHELL'. This type can be modified for different element orders by appending the number of nodes onto the end of the type. For example, a 6-node shell could have the element type 'TRISHELL6'. However, any element whose type begins with the 8 letters 'TRISHELL' in upper, lower, or mixed case will refer to an element with a triangular topology. The element can exist in either three-space or two-space.

Attributes: 1. If the element exists in two-space, there are no required attributes.

2. If the element exists in three-space, there is one required attribute which is the thickness of the shell.

3. If the number of attributes is equal to the number of nodes in the connectivity of the element, then the attributes are assumed to specify the thickness of the element at each of the elements nodes. The ordering of the attributes matches the ordering of the elements nodes.

The node ordering of the 3D triangle matches the node ordering of the 2D triangle as shown in Figure 3.

Figure 3. Local Node Numbering for CUBIT triangular element types

The sideset side ordering is different for the element in the 2D and 3D instances.

In 2D, the sideset side ordering matches what is shown in Figure 4.

Figure 4. Local sideset numbering for CUBIT triangular element types

In 3D, the sideset side and node ordering is the same as for a quad shell except that there are only 3 or 6 nodes.

side 1 == {1,2,3} side 2 == {3,2,1} side 3 == {1,2} side 4 == {2,3} side 5 == {3,1}

If it is a higher order triangular shell (6 [or 7 nodes]), then the higher-order nodes are added on to the end of the above:

side 1 == {1,2,3,4,5,6[,7]} side 2 == {3,2,1,6,5,4[,7]} side 3 == {1,2,4} side 4 == {2,3,5} side 5 == {3,1,6}

---

## FASTQ

**URL:** https://coreform.com/cubit_help/appendix/fastq.htm

**Contents:**
- FASTQ

FASTQ is a program developed to create geometry and two-dimensional mesh. The user may choose to upload FASTQ files and work with the files in an environment that accepts a limited number of FASTQ commands.

Table 1. FASTQ Commands Executable in Cubit

Table 2. Brief List of Importable FASTQ Commands Supported in Cubit

---

## FeatureSize

**URL:** https://coreform.com/cubit_help/appendix/alpha/feature_size.htm

**Contents:**
- FeatureSize

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Summary: Meshes a curve based on its proximity to nearby geometry and size of nearby geometric features. This is an alpha feature and should be used with caution.

Curve <range> Scheme Featuresize

Curve <range> Density <density_factor>

The user may also automatically bias the mesh from small elements near complicated geometry to large elements near expanses of simple geometry. Meshing a curve with scheme featuresize places nodes roughly proportional to the distance from the node to a piece of geometry that is foreign to the curve. Foreign means that the geometric entity doesn't contain the curve, or any of its vertices (i.e. the entity's intersection with the curve is empty). It is known that featuresize is a continuous function that varies slowly. Featuresize meshing is very automatic and integrated with interval matching. Featuresize meshing works well with paving, and in some cases with structured surface-meshing schemes (map, submap) as well.

If desired, the user may specify the exact or goal number of intervals with a size or interval command, and then the featuresize function will be used to space the nodes.

The featuresize function may also be scaled by the user to produce a finer or coarser mesh using the density command as follows:

Curve <range> Density <density_factor>

The default scaling factor or density is 1. Higher densities also reduce the transition rate of the node spacing. A density of 2 usually gives a good quality mesh. A density below about 0.5 could produce rapid transitions and poor mesh quality. The following shows an example of different density values when using the featuresize scheme.

---

## FullHex vs. NodeHex Representation

**URL:** https://coreform.com/cubit_help/appendix/fullhex_vs_nodehex.htm

**Contents:**
- FullHex vs. NodeHex Representation

CUBIT has two different internal representations of hexes: FullHexes and NodeHexes. The NodeHex is a lighter weight data structure, but occasionally nodeset and sideset shortcomings can be overcome by using FullHexes. The user can select which type of hexes get created when generating or importing a volume mesh with the following command:

Set FullHex [Use] [on|OFF]

Using the FullHex representation increases the memory used to store a mesh by a factor of approximately five.

---

## Navigation XML Files

**URL:** https://coreform.com/cubit_help/appendix/navigation_xml.htm

**Contents:**
- Navigation XML Files

The Cubit GUI includes a section referred to as the Command Panel. It is comprised of a hierarchy of buttons used to navigate to panels that accept user input and generate Cubit command strings. The following example shows the command panel used to create a brick. The user navigates to the command panel by pressing the "Mode - Geometry" button, then the "Entity - Volume" button, followed by the "Action - Create" button, then finally selecting the "Brick" option from the pull-down menu.

Before Cubit 14.0, this hierarchy was not modifiable by any third party. With the release of Cubit 14.0, any user can modify the contents of the button hierarchy by adding, deleting, or modifying buttons and command panels. The button hierarchy is expressed in a series of XML files located in the directory 'bin/xml.'

The controlling XML file is named, "CubitNavigationRoot.xml." A snippet from the file is shown below:

The first two levels of the hierarchy are managed in this file. Subsequent levels of the hierarchy are managed in more specific XML files. For example, the remaining hierarchy associated with geometry volumes is managed in the file named, "GeometryVolumeNavigation.xml." A snippet from that file is shown below:

Users may modify the Label, ToolTip, or Icon url. Users may remove entire categories if necessary. Users should not modify NavigationNode or NavigationReference tags.

Users may create their own command panels using Qt and add them to the hierarchy.

---

## Optimize Jacobian

**URL:** https://coreform.com/cubit_help/appendix/alpha/optimize_jacobian.htm

**Contents:**
- Optimize Jacobian

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Applies to: Volume meshes

Summary: Produces locally-uniform hex meshes by optimizing element Jacobians

Volume <range> Smooth Scheme Optimize Jacobian [param]

The Optimize Jacobian method minimizes the sum of the squares of the Jacobians (i.e., volumes) attached to the smooth node. Meshes smoothed by this means tend to have locally-uniform hex volumes.

The parameter <param> has a default value of 1, meaning that the method will attempt to make local volumes equal. The parameter, which should always be between 1 and 2 (with 1.05 recommended), can be used to sacrifice local volume equality in favor of moving towards meshes with all-positive Jacobians.

---

## Periodic Space Filling Models (Tile)

**URL:** https://coreform.com/cubit_help/appendix/period_spacefilling_models.htm

**Contents:**
- Periodic Space Filling Models (Tile)
- Initial setup
- Creating Nodesets
- Smoothing
- Example

This appendix describes commands for producing good-quality meshes of models that tile space, such as polycrystalline materials models. Such models are often referred to as "periodic", but since that term already has a different meaning in Cubit, the keyword "tile" is used instead. Meshes may be smoothed across periodic boundaries. Periodic boundary conditions can be automatically set up, according to ALEGRA conventions (SAND99-2698).

Tile commands are alpha features and should be used with caution.

First import the model and merge the surfaces. Then mesh it with any method that will create meshes that match across the tile (periodic) boundary, say with scheme polyhedron or sweep. Once the mesh is created, specify the "tile vectors", which lets Cubit know that the nodes across the periodic boundaries are actually the same node:

Tile {x <period> | y <period> | z <period>} [x <period>] [y <period>] [z <period>]

The 'period' you specify is actually the vector offset from one boundary to its match. Specify one tile command for each coordinate axis that the model is periodic in. E.g.

Tile x 1 Tile y 1 Tile z 1

You can see which nodes are matched to a given node by some combination of tile vectors with the following command: Tile Debug Node <id>

If you later need to delete these tile vectors, use the following command:

Once the tile vectors are specified, you can set up periodic boundary conditions that meet ALEGRA specifications. The command is:

Tile Nodeset <start_id>

This will create a nodeset for all combinations of tile vectors that actually connect nodes. The nodesets created will be reported to you. The nodesets will be consecutive starting with the given 'start_id', except that if there are no nodes for a particular combination there will be no nodeset and the id space will have a hole. To delete these nodesets, use the

command rather than the usual commands to delete nodesets.

Once a mesh has been created and the tile vectors have been specified, you can smooth the mesh and keep the periodic boundaries exactly offset by the tile vectors. Only hex meshes are currently supported. A variety of 3d smoothing schemes are supported, including laplacian, equipotential, untangle, and condition number.

Smooth Volume <volume_id_range> [Global [Float <dim>] ]

Use "Global" if you are smoothing a collection of volumes. Use "float 3" if you want nodes on surfaces, curves, and vertices to be able to move off of their geometric owner. Use "float 2" if you want just nodes on curves and vertices to be able to move off of their owner (but stay on an owning surface). It is often useful to specify that some of the nodes are fixed using the "node position fixed" command.

# make the geometry #{brick_size=500} brick wid {brick_size} brick wid {brick_size} body 2 move {brick_size} 0 0 brick wid {brick_size} body 3 move {brick_size} {brick_size} 0 brick wid {brick_size} body 4 move 0 {brick_size} 0 brick wid {brick_size} body 5 move 0 0 {brick_size} brick wid {brick_size} body 6 move {brick_size} 0 {brick_size} brick wid {brick_size} body 7 move {brick_size} {brick_size} {brick_size} brick wid {brick_size} body 8 move 0 {brick_size} {brick_size} merge all

# mesh it vol all int 3 mesh vol all

# set the tiling vectors tile x {brick_size*2} tile y {brick_size*2} tile z {brick_size*2} tile debug node 256 tile debug node 245

# set the tiling nodesets tile nodeset

# mess up the mesh quality # volume all smooth scheme randomize # smooth volume all surface all smooth scheme randomize smooth surface all draw hex all

# fix the mesh quality node in volume all position fixed node in surface all position free volume all smooth scheme laplac # volume all smooth scheme untangle beta 0.08 smooth volume all global float 3 draw hex all

---

## Quick Reference

**URL:** https://coreform.com/cubit_help/quick_reference/quick_reference.htm

**Contents:**
- Quick Reference

Geometry | File Import | Meshing | Genesis | Program | Entity Parsing | Groups | Graphics | Settings

The following is a brief overview of some of the most used command-line CUBIT commands.

Brick X <> [Y <> Z <>] Cylinder Radius <> Height <> Frustum Z <> Radius <> [Top <>] Frustum Z <> Maj Rad <> Min Rad <> Prism Z <> Sides <> Rad <> [Maj <> Min <>] Pyramid Height <> Sides <> Radius <> Sphere Rad <> [Xpos] [Ypos] [Zpos] [Inn <>] Torus Major Rad <> Minor Rad <>

Unite <> [With <>] [keep] Subtract <> From <> [keep] Intersect <> [With <>] [keep]

Body <> [Copy] Move <dx> <dy> <dz> Move {} <> location {} <> [except [x] [y] [z]] Rotate {} <> About {x| y| z|<> <> <>} Angle <> Rotate {} <> About Vert <> Vert <> Angle <> Rotate {} <> About Nor Of Surf <> Angle <> Body <> [Copy] Scale <> Body <> [Copy] Reflect {x| y| z|< x> <y> <z>}

Webcut {} <> Pla Vert <> [Vert]<> [Vert]<> () Webcut {} <> Plane Surf <> () Webcut {} <> Plane {xpla| ypla| zpla} [offs <>] Webcut {} <> Tool [Body] <> Webcut {} <> With Sheet {Body| Surf} <> Webcut {} <> With Sheet Ext Fr Surf <> Webcut {} <> Cyl Rad <> Axis {x| y| z| Vert <> Vert <>| <x><y><z>} [cent] Options: [Noimprint| Imprint( default)], [Nomerge( default)| Merge], [group_ results] Section {} <> {{ xpla| ypla| zpla} [offs <>]} | Surf <>} [keep] [normal( default)| reverse]

Import Acis 'filename' Export Acis 'filename' [Body <>] Import Mesh Geometry 'filename' (options)

Mesh {} <> Delete Mesh {} <> [Propagate]

{} <> Interval {<> | Hard | Soft | Default} {} <> Size {<> | Auto} Match Intervals {} <> [Ass Grou [Onl| Infea]] [Seed Cur <>] [Map| Pave]

{} <> Scheme ... Curve: bias, copy, curvature, equal, stretch Surface: auto, circle, copy, hole, map, mirror, pave, pentagon, qtri, submap, triprimitive, trimap, trimesh, tripave Volume: auto, copy, map, sphere, submap, sweep, tetmesh, tetprimitive, thex Smooth {} <> {} <> Smooth Scheme ...

Curves: laplacian, randomize Surface: centroid area pull, equipotential, laplacian, condition number, randomize, untangle, winslow Volume: equipotential, laplacian, condition number, untangle, randomize

Block <> {Group| Vol| Surf| Curv} <> [Remove] SideSet <> {Group| Curve} <> [Remove] NodeSet <> {} <> [Remove] Export Genesis 'filename' Block <> Attribute <> Block <> Element Type <type_> Curves: bar[| 2| 3]| beam[| 2| 3]| truss[| 2| 3] Surfaces: quad[| 4| 8| 9]| shell[| 4| 8| 9]| tri[| 3| 6| 7] Volumes: hex[| 8| 20| 27]| pyr| tetra[| 4| 8| 10| 14] hexshell SideSet <> Surf <> [Rem|[ She][ For| Rev| Both]] SideSet <> Surf <> wrt Volume <> Reset {Genesis | Nodesets | Sidesets | Blocks}

Play 'filename' Record {' filename' | stop} Logging {off|on file <'filename'> [resume]} Reset Reset Genesis Quit

Surface 1 2 3 4 to 6 by 2 ... Curve all in Volume 2 ... Draw Edge all in Hex 32 List Curve 1 to 50 except 2 4 6 Draw Sideset 1 2 3 Curve 3 to 5 Hex 2 4 6

Group <> {add| equals| remove| xor} {} <> Group <> {inters| unite} grou <> with grou <> Group <> subtract group <> from group <>

Default mouse buttons (command line)

B1 - rotate; B2 - zoom; B3 - pan Control-B1: pick entity (In graph win: 0,1,2,3,4 - Pick vert, curv, surf, vol, body)

Shortcuts (focus in Graphics Window)

a Add to selection group b Toggle Bounding Box on Click c Clear "picked" Group d Display 'picked' group, make it the selection e Echo ID of selection to command line f Assign function to mouse button g List geometry of selection h Print help i Toggle visibility of selection j/k Move slicing plane down/up l List current selection (as if you typed 'list ...') control-l Give focus to the command prompt m/n List picked group/selection contents p Toggle Persistent Wireframe q Quit Current Mode (Exit slicing if slicing) r Remove from 'picked' Group s Toggle save-mesh on slice move u Toggle mouse circle visibility v Reset view w Toggle Wireframe on click x/y/z Slice along x/y/z-axis Shift-Z Zoom on current selection F1 Save view 1 Numbers: set what you're picking. ESC Cancel current Action Tab Next possible selection Shift-Tab Previous possible selection

---

## Randomize

**URL:** https://coreform.com/cubit_help/appendix/alpha/randomize.htm

**Contents:**
- Randomize

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Applies to: Curve, Surface and Volume meshes

Summary: Randomizes the placement of nodes on a geometry entity

{Surface|Volume} <range> Smooth Scheme Randomize [percent]

This scheme will create non-smooth meshes. If a percent argument is given, this sets the amount by which nodes will be moved as a percentage of the local edge length. The default value for percent is 0.40. This smooth scheme is primarily a research scheme to help test other smooth schemes.

---

## References

**URL:** https://coreform.com/cubit_help/appendix/references.htm

**Contents:**
- References

Attaway, Stephen W.; Mello, Frank J.; Heinstein, Martin W.; Swegle, Jeffrey W.; Ratner, Julie A.; Zadoks, Rick Ian, "PRONTO3D users' instructions: a transient dynamic code for nonlinear structural analysis," Sandia Report SAND 98-1361 Sandia National Laboratories, Albuquerque, NM (1998)

Attaway S. W., unpublished, (1993)

Blacker, T. D., FASTQ Users Manual Version 1.2, SAND88-1326, Sandia National Laboratories, (1988)

Blacker, Ted D. "An Adaptive Finite Element Technique Using Element Equilibrium and Paving", American Society of Mechanical Engineers, Annual Meeting Dallas Texas, November 25-30, 1990, ASME, Nov 1990

Blacker, Ted D., "Paving: A New Approach To Automated Quadrilateral Mesh Generation", International Journal For Numerical Methods in Engineering, John Wiley, Num 32, pp.811-847, 1991

Blacker T.D. and Meyers R.J,."Seams and Wedges in Plastering: A 3D Hexahedral Mesh Generation Algorithm", Engineering with Computers, Springer Verlag, Vol 2, Num 9, pp.83-93, 1993

Brewer, M., L. Diachin, P. Knupp, T. Leurent, and D. Melander, "The Mesquite Mesh Quality Improvement Toolkit", Proceedings, 12th International Meshing Roundtable, 2003

Brewer, M., "Geometry-Tolerant Meshing Using Advancing-Front Techniques", SAND Report, (6-2008)

Butlin, Geoffrey and Clive Stops, "CAD Data Repair", 5th International Meshing Roundtable, pp.7-12, 1996

Clark Brett W., "Removing Small Features with Real Solid Modeling Operations", Submitted to 16th International Meshing Roundtable, 2007

Cook, W. A. and W. R. Oakes (1982) Mapping methods for generating threedimensional meshes, Computers In Mechanical Engineering, CIME Research Supplement:67-72, August 1982

Folwell, Nathan T. and Scott A. Mitchell, "Reliable Whisker Weaving via Curve Contraction", Proceedings, 7th International Meshing Roundtable, Sandia National Lab, pp.365-378, October 1998

Freitag, Lori A. and Patrick M. Knupp , "Tetrahedral Element Shape Optimization via the Jacobian Determinant and Condition Number", Proceedings, 8th International Meshing Roundtable, South Lake Tahoe, CA, U.S.A., pp.247-258, October 1999

George, P.L., F. Hecht and E. Saltel, "Automatic Mesh Generator with Specified Boundary", Computer Methods in Applied Mechanics and Engineering, Vol. 92, pp. 269-288, 1991

Hardwick, Mike, "DART System Analysis Presented to Simulation Sciences Seminar", June 28, 2005

Jones, R.E., QMESH: A Self-Organizing Mesh Generation Program, SLA - 73 - 1088, Sandia National Laboratories, (1974).

Knupp, Patrick M., "Winslow Smoothing On Two-Dimensional Unstructured Meshes", Proceedings, 7th International Meshing Roundtable, Sandia National Lab, pp.449-457, October 1998

Knupp, Patrick M., "Matrix Norms & The Condition Number: A General Framework to Improve Mesh Quality Via Node-Movement", Proceedings, 8th International Meshing Roundtable, South Lake Tahoe, CA, U.S.A., pp.13-22, October 1999

Knupp, P., "Achieving Finite Element Mesh Quality via Optimization of the Jacobian Matrix Norm and Associated Quantities, Part I", Int. J. Num. Meth. Engr.. 2000

Lovejoy, S. C. and R. G. Whirley, DYNA3D Example Problem Manual, UCRL-MA--105259, University Of California and Lawrence Livermore National Laboratory, (1990).

Melander, Darryl J., Timothy J. Tautges, Steven E. Benzley "Generation of Multi-Million Element Meshes for Solid Model-Based Geometries: The Dicer Algorithm" AMD-Vol. 220 Trends in Unstructured Mesh Generation, ASME, pp.131-135, July 1997

Mezentsev, Andrey A., "Methods and Algorithms of Automated CAD Repair For Incremental Surface Meshing", Proceedings, 8th International Meshing Roundtable, pp.299-309, 1999

Murdoch, Peter and Steven E. Benzley, "The Spatial Twist Continuum", Proceedings, 4th International Meshing Roundtable, Sandia National Laboratories, pp.243-251, October 1995

Oddy, A., J. Goldak, M. McDill, and M. Bibby "A Distortion Metric for Isoparametric Finite Elements" Transactions of the Canadian Soc. Mech. Engr., pp213-217, Vol 12, No 4, 1988.

Owen, Steven J. and David R. White, "Mesh-Based Geometry: A Systematic Approach to Constructing Geometry from the Nodes and Elements of a Finite Element Mesh", 10th International Meshing Roundtable, Sandia National Laboratories, pp. 83-96, October 2001

Owen, Steven J., Clark, B.W., Melander, D.J., Brewer, M.B., Shepherd, J.F., Merkley, K., Ernst, C., Morris, R., "An Immersive Topology Environment for Meshing", Accepted to 16th International Meshing Roundtable, 2007

Parthasarathy V. N. et al, "A comparison of tetrahedron quality measures", Finite Elem. Anal. Des., Vol 15, 1993, 255-261.

Price, M.A. and C.G. Armstrong, "Hexahedral Mesh Generation by Medial Surface Subdivision: Part I, Solids With Convex Edges, International Journal for Numerical Methods in Engineering, Vol. 38, No. 19, pp. 3335-3359, 1995

W. Quadros, V. Vyas, M. Brewer, S. Owen, and K. Shimada, “A Computational Framework for Generating Sizing Function in Assembly Meshing”, Proceedings, 14 th International Meshing Roundtable, 2005

W. R. Quadros, K. Shimada, and S. J. Owen, “Skeleton-based computational method for the generation of a 3D finite element mesh sizing function”, Engineering with Computers, Springer Verlag, Vol 20, Num 3, pp.249-264, 2004

W. R. Quadros, S. J. Owen, M. Brewer, and K. Shimada, “Finite Element Mesh Sizing for Surfaces using Skeleton”, Proceedings, 13 th International Meshing Roundtable, 2004

Robinson, J., "CRE method of element testing and Jacobian shape parameters, Eng. Comput., Vol. 4 (1987).

Ruppert, Jim , "A New and Simple Algorithm for Quality 2-Dimensional Mesh Generation". Technical Report UCB/CSD 92/694, University of California at Berkely, Berkely California (1992)

Scott, Michael A., Matthew N. Earp, Steven E. Benzley, and Michael B. Stephenson, "Adaptive Sweeping Techniques," Proceedings of the 14th International Meshing Roundtable, Springer, pp. 417-432, 2005.

Schoof, L. A.and Victor R. Yarberry, "EXODUS II A Finite Element Data Model", SAND92-2137, Sandia National Laboratories, (1995).

Sheffer, A., "Model simplification for meshing using face clustering", Computer-Aided Design, Vol. 33, No. 13, pp. 925-934(10), 2001

Staten, Matthew L., Steven J. Owen, Ted D. Blacker, "Unconstrained Paving and Plastering: A New Idea for All Hexahedral Mesh Generation", Proceedings, 14th International Meshing Roundtable, pp.399-416, 2005

Staten, Matthew L., Robert A. Kerr, Steven J. Owen, Ted D. Blacker, "Unconstrained Paving and Plastering: Progress Update", Proceedings, 15th International Meshing Roundtable, pp.469-486, 2006

Staten, Matthew L., Brian Carnes, Corey McBride, Clint Stimpson, Jim Cox, "Mesh Scaling for Affordable Solution Verification", Proceedings, 25th International Meshing Roundtable, pp. 46-58, 2016

Stimpson, CJ, Ernst, CD, Knupp, P, Pebay; P, and Thompson, D. "The Verdict Geometric Quality Library", Sandia Report SAND2007-175, 2007

Tautges, Timothy J. and Scott A. Mitchell, "Whisker Weaving: Invalid Connectivity Resolution and Primal Construction Algorithm", Proceedings, 4th International Meshing Roundtable, Sandia National Laboratories, pp.115-127, October 1995

Tautges, Timothy J., Ted Blacker, Scott A. Mitchell, "The Whisker Weaving Algorithm: A Connectivity-Based Method for Constructing All-Hexahedral Finite Element Meshes", International Journal for Numerical Methods in Engineering, Wiley, Vol 39, pp.3327-3349, 1996

Tautges, Timothy J., "The Common Geometry Module (CGM): A Generic, Extensible Geometry Interface", Proceedings, 9th International Meshing Roundtable, pp. 337-348, 2000

Tautges, Timothy J., "Automatic Detail Reduction for Mesh Generation Applications", Proceedings, 10th International Meshing Roundtable, pp.407-418, 2001

Taylor, L. M. and D. P. Flanagan, "Pronto 3D--A Three-Dimensional Transient Solid Dynamics Program", SAND87-1912, Sandia National Laboratories, (1989).

Tipton ,R. E., "Grid Optimization by Equipotential Relaxation", unpublished, Lawrence Livermore National Laboratory, (1990)

Walton, D. J. and D. S. Meek, "A Triangular G1 Patch from Boundary Curves," Computer-Aided Design, Vol. 28 No. 2 pp. 113-123 (1996)

Watson, David F. , "Computing the Delaunay Tessellation with Application to Voronoi Polytopes", The Computer Journal, Vol 24(2) pp.167-172 (1981)

Wellman, Gerald W., "MAPVAR : a computer program to transfer solution data between finite element meshes", Sandia Report SAND 99-0466 Sandia National Laboratories, Albuquerque, NM (1999)

White, David R. and Paul Kinney, "Redesign of the Paving Algorithm: Robustness Enhancements through Element by Element Meshing", Proceedings, 6th International Meshing Roundtable, Sandia National Laboratories, pp.323-335, October 1997

White, David R. and Sunil Saigal (2002) Improved Imprint and Merge for Conformal Meshing, Proceedings, 11th International Meshing Roundtable, pp.285-296

White, David R. and Timothy J. Tautges, "Automatic Scheme Selection for Toolkit Hex Meshing", International Journal for Numerical Methods in Engineering, Vol. 49, No. 1, pp. 127-144, 2000

Whiteley, M., D. White, S. Benzley and T. Blacker, "Two and Three-Quarter Dimensional Meshing Facilitators", Engineering with Computers, Springer-Verlag, Vol 12, pp.155-167, December 1996

Yong Lu, Rajit Gadh, and Timothy J. Tautges, "Volume decomposition and feature recognition for hexahedral mesh generation", Proceedings, 8th International Meshing Roundtable, pp. 269-280, 1999

---

## Remove Tiny Edge Length

**URL:** https://coreform.com/cubit_help/appendix/alpha/remove_tiny_edge_length.htm

**Contents:**
- Remove Tiny Edge Length

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Applies to: Trimesh Surface Scheme

Summary: Tolerance specified to prevent small edges in a triangle mesh

[Set] Trimesher Remove Tiny Edge Length {<value>|[off]}

Setting the tiny edge length forces the MeshGems trimesher to generate triangles with edges greater than the specified value. It is actually a post processing step that collapses triangles with edges less than the specified value. This setting is necessary because the MeshGems triangle mesher sometimes inserts triangles with small edges along high curvature features, even though a larger size has been specified and geometry approximation has been turned off. Using this setting is the only way to guarantee that no edges smaller than the specified value will be created.

The off option resets the 'tiny edge length' value so it is not used.

The user should not use 'tiny edge length' values approaching the mesh size because an invalid mesh can result.

The images below show meshing a surface with and without setting a 'tiny edge length' value. In this example all surfaces have been composited into a single surface. Compositing small surfaces with larger neighbors in conjunction with using 'tiny edge length' has the effect of washing-over small features.

---

## Transition

**URL:** https://coreform.com/cubit_help/appendix/alpha/transition.htm

**Contents:**
- Transition

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Summary: Produces a specified transition mesh for specific situations

Surface <range> Scheme Transition {Triangle|Half_circle|Three_to_one|Two_to_one|Convex_corner|Four_to_two} [Source Curve <id>] [Source Vertex <id>]

The transition scheme supplies a set of transition primitives which serve to transition a mesh from one density to another across a given surface. The six transition sub-types are demonstrated here.

The user also has the option of specifying a source curve and/or a source vertex. The rules for these specifications are as follows

---

## Using APREPRO in CUBIT

**URL:** https://coreform.com/cubit_help/appendix/aprepro/using_aprepro_in_cubit.htm

**Contents:**
- Using APREPRO in CUBIT
- Loops
- Deleting APREPRO Variables
- Other Examples

To use APREPRO within CUBIT, simply enclose APREPRO statements within curly braces '{}' as part of the CUBIT command. Any APREPRO statements included in a command will be evaluated before the command is executed. For example, if the APREPRO variable 'my_x' is given the value of 3, the command

before the command is executed by CUBIT. Note that this means APREPRO will NOT give CUBIT parametric modeling abilities. In the above example, if the value of 'my_x' is later changed to 5, the size of the brick already created will not automatically change to five.

APREPRO expressions can also exist on separate lines. When doing this, it is recommended to add the CUBIT comment character '#' before the APREPRO statement. This will tell CUBIT to treat the evaluated expression as a comment, which will prevent errors from being issued in many cases.

Consider the following example:

brick x {my_x} y {my_y}

create cylinder radius {my_x} height {my_y}

In the first two lines, only APREPRO statements are being executed (values are assigned to the variables 'my_x' and 'my_y'). After being evaluated by APREPRO, these two lines will be sent to CUBIT as

If the comment character was omitted instead CUBIT would issue several errors about incorrect command syntax. However, because these lines start with the comment character, they are ignored by CUBIT. Also note that the character '$' may be used in place of '#' for comments.

Repeated processing of a group of lines can be controlled with the {loop(control)}, {endloop} commands, as noted in section 6.2.5 of the APREPRO documentation.

A loop may also be terminated before running the specified number of times using a #{break} statement. As soon as a #{break} statement is encountered, the loop is exited and the rest of the statements in the loop will not execute. Additional iterations of the loop will not be executed either.

For example, the following commands will create 3 bricks:

When a #{break} statement executes, anything in the loop following the #{break} statement will be skipped, including the #{endif}. For this reason, a #{break} statement not only exits the loops, but also terminates the most recent #{if} statement exactly as #{endif} would do. #{break} statements should not be used outside of #{if} statements.

It is also possible to terminate a loop using the #{abortloop} statement. #{abortloop} will terminate all loops (including nested loops) without executing the contents of the loop(s). This can be useful when a typo is made while manually entering a loop at the command line. Instead of ending the loop normally and waiting for the loop to execute with numerous errors, the loop will end immediately without any execution or errors. Please note, however, that the #{abortloop} statement is only valid within a loop block; otherwise, it will generate errors.

When creating a loop, APREPRO will record all lines that are given to the command line until the corresponding #{endloop} is reached. During this process, no commands will be passed to CUBIT. Once the terminating #{endloop} is reached, APREPRO will expand the loop, repeating the recorded lines the number of times specified by the loop counter, and send the expanded list of commands to CUBIT. If the terminating #{endloop} is accidentally omitted, CUBIT may appear to be unresponsive to commands because APREPRO is still recording lines for the loop. In situations like these, the #{abortloop} statement may be used to terminate any unfinished loops and restore the command line to a working state.

Also note that it is not recommended to use the 'pause' command within a loop, as it can lead to situations in which the user must repeatedly enter the command 'resume' to execute the entire loop. In situations like these #{abortloop} will NOT terminate the loop because it has already been expanded by APREPRO and CUBIT is simply executing a list of commands.

There are two ways to delete an APREPRO variable in CUBIT. The first is to use the APREPRO 'delete' function. The delete function takes the name of the variable to be deleted as its argument, as shown in the following example:

The second way to delete an APREPRO variable is by using the 'reset aprepro' command:

This will delete all APREPRO variables and reset APREPRO to its initial state.

The following example shows the use of some of the string functions.

#{t1 = "ATAN2"}{t2="(0,-1)"}

#{t3 = tolower(t1 // t2)}

... The variable t3 is equal to the string atan2(0,-1)

The result is the same as executing {atan2(0,-1)} This is admittedly a very contrived example; however, it does illustrate the workings of several of the functions. In the first example, an expression is constructed by concatenating two strings together and converting the resulting string to lowercase. This string is then executed.

The following example uses the rescan function to illustrate a basic macro capability in APREPRO. The example creates vertices in CUBIT equally spaced about the circumference of a 180 degree arc of radius 10. Note that the macro is 5 lines long (2 of the lines start with #, with the exception of the looping constructs - the actual journal file for this would not continue lines but would put each one on one long line).

#{num = 0} {rad = 10} {nintv = 10} {nloop = nintv + 1}

#{line = 'Create Vertex {polarX(rad,(++num-1)*180/nintv)} {polarY(rad,(num-1)*180/nintv)}'}

Note the loop construct to automatically repeat the rescan line. To modify this example to calculate the coordinates of 101 points rather than eleven, the only change necessary would be to set {nintv=100}.

---
