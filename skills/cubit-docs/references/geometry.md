# Geometry

## ACIS Geometry Kernel

**URL:** https://coreform.com/cubit_help/geometry/model_definitions/acis.htm

**Contents:**
- ACIS Geometry Kernel

ACIS is a proprietary format developed by Spatial Technologies. CUBIT incorporates the ACIS third party libraries directly within the program. The ACIS third party libraries are used extensively within CUBIT to import, export and maintain the underlying geometric representations of the solid model for geometry decomposition and meshing. There are many ways to get geometry into the ACIS format. ACIS files can be exported directly from several commercial CAD packages, including SolidWorks, AutoCAD, and HP PE/SolidDesigner. Third party ACIS translators are also available for converting from native formats such as Pro Engineer. CUBIT also uses the ACIS libraries for importing IGES and STEP format files.

Importing and creating geometry using the ACIS geometric modeling kernel currently provides the widest set of capabilities within CUBIT. All geometry creation and modification tools have been designed to work directly on the ACIS representation of the model.

---

## Align Command

**URL:** https://coreform.com/cubit_help/geometry/transforms/align.htm

**Contents:**
- Align Command

The align command is a combination of the rotate and move commands. This transformation is useful for aligning surfaces in preparation for geometry decomposition and aligning models for axis-symmetric analysis. If the [include_merged] option is used, all entities that are merged with the specified volume will be included in the align transformation also.

The first align command will transform the specified volumes by computing a transformation that aligns the source axis or surface with the target axis or surface such that the source axis centroid or surface centroid is coincident with the target axis origin or surface centroid and the surface normal(s) and/or axis(s) are pointing either in the same or opposite direction (depending on their initial alignment). The source surface need not be in the specified volumes. If the [reverse] option is specified, the resulting alignment is flipped 180 degrees.

An optional second axis or surface source-target pair can be specified. This will result in an additional rotational alignment: The specified volumes will be rotated about the first target axis or surface normal such that the second target axis or surface is at the same angle about the first target axis or surface normal.

Align Volume <id_range> Source {Axis {options}|Surface <surface_id>} Target {Axis {options}|Surface <surface_id>} [Source {Axis {options}|Surface <surface_id>} Target {Axis {options}|Surface <surface_id>}] [reverse] [include_merged] [preview]

The image below shows the two alignments that occur when the additional source-target pair is specified.

Figure 1 - Aligning with optional rotation

The second form of the align command either aligns a face of a volume or two vertices (forming a direction) with the xy, yz, and xz planes or the x, y, and z axes. If the [reverse] option is specified, the resulting alignment is flipped 180 degrees.

Align Volume <id_range> {Surface <surface_id>| Vertex <vertex_id>} {{X|Y|Z Axis}|{XY|XZ|YZ plane}} [reverse] [include_merged] [preview]

The third form of the command is a rotational alignment, where the specified entities are rotated about the specified axis, where the angle of rotation is the angle between the first and second locations with respect to the axis.

Align Volume <id_range> Location {options} with Location {options} about Axis {options} [include_merged] [preview]

The fourth form of the command uses vertex pairs to define the transformation. The first pair of vertices define a translation so that the source and target vertices are coincident (i.e.,the source is moved to the target). The optional second pair of vertices define a rotation such that the source and target vertices are all collinear after the transformation. The optional third pair of vertices define a rotation such that all the source and target vertices will be coplanar.

{Body|Volume|Surface|Curve|Vertex|Group} <id_range> Align Using Vertex <src_id> <tgt_id> [Collinear Vertex <src_id> <tgt_id> [Coplanar Vertex <src_id> <tgt_id>] ] [include_merged]

---

## Attribute Behavior

**URL:** https://coreform.com/cubit_help/geometry/attributes/persistent_attributes/attribute_behavior.htm

**Contents:**
- Attribute Behavior

In this context, attributes are defined as data associated directly with a particular geometry entity. In CUBIT's implementation of attributes, these data can occupy one of three "states" at any given time: they can be stored in data fields on CUBIT's geometry entities; they can be stored in an intermediate representation, using CUBIT's attribute objects; or they can exist only on the ACIS objects. When they are stored on ACIS objects, those attributes are written to and read from disk files with the geometry. This mechanism allows CUBIT-specific information to be stored and retrieved with the geometry data. By default, attribute data is not stored with geometry. To enable the use of attributes, use the commands described in the following sections.

---

## Attribute Commands

**URL:** https://coreform.com/cubit_help/geometry/attributes/persistent_attributes/attribute_commands.htm

**Contents:**
- Attribute Commands
- Control By Attribute Type or Geometric Entity

Most non-CUBIT-developer uses of attributes will be to use all or none of the attributes. Therefore, the most common command to enable and disable the use of attributes is:

Set Attribute {On|Off}

When a geometry is imported into CUBIT, any attributes defined on that geometry and recognized as CUBIT attributes are imported and put into an intermediate representation (that is, this information is not assigned directly to the geometry entities). To find out which attributes are defined on a given set of entities, use the following command:

If no entities are entered, attribute information for all the geometric entities defined in CUBIT is printed.

The Type option can be used to list information about a specific attribute type; values for are the same as those in the previous table.

If the All option is entered, information about all attribute types will be printed, even if there are none of those attributes defined for the specified entities.

If the Print option is entered, the information stored in each attribute will be printed; this command is usually used only by CUBIT developers.

Attributes can be enabled or disabled by attribute type, to allow the use of only user-specified attribute types. To turn on or off specific attributes, use the command:

Set Attribute <attribute type> {On|Off}

Attributes can also be controlled to automatically write (update) and read (actuate) to/from solid model files automatically, using the command:

Set Attribute <attribute_type> Auto {Actuate|Update} {On|Off}

Finally, attributes can be manually written to and read from the geometric entities, and removed from cubit entities, using the command

{geom_list} Attribute {All|Attribute_type} {Actuate|Remove|Update|Read|Write}

where geom_list is a list of geometry entities. This command is recommended only for developers' use.

---

## Attribute Types

**URL:** https://coreform.com/cubit_help/geometry/attributes/persistent_attributes/attribute_types.htm

**Contents:**
- Attribute Types

The attribute types currently implemented in CUBIT are shown below.

---

## Automatic Forced Sweepability

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/auto_clean/auto_forced_sweep.htm

**Contents:**
- Automatic Forced Sweepability

In some cases, a volume can be "forced" into a sweepable configuration by compositing surfaces on the linking surfaces. The automatic forced sweep command will attempt to automatically composite linking surfaces together to create a sweepable topology. This command can be useful in cases where there are many linking surfaces that prohibit sweepability and are not needed to define the mesh. It is assumed that the user has assigned the source and target surfaces for the sweep prior to calling this function. CUBIT will try to composite linking surfaces together to get rid of problems such as 1) non-submappable linking surfaces, 2) interior angles between curves of a surface that deviate far from multiples of 90 degrees, and 3) surfaces with curves smaller than the small curve size, if a small curve size is specified. This command is incorporated into the ITEM GUI, but is also available from the command line using the following command syntax.

Auto_clean Volume <id_range> Force_sweepability [Small_curve_size <val>]

The small_curve_size qualifier is an optional argument. If a curve size is specified, the command will try to remove surfaces with curves smaller than this size by compositing the surface with adjacent surfaces.

The following cylinder has been webcut and had surface splits so that it is not sweepable. The split surface command has also introduced 3 small curves on the surfaces. After the source and target surfaces are set, the force sweepability command is issued to automatically composite neighboring surfaces to make the volume sweepable and remove the small curves. The results are shown in the image below.

auto_clean volume 1 force_sweepability small_curve_size .7

Figure 1. Linking surfaces are composited to force a sweepable volume topology

---

## Automatic Geometry Clean-up

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/auto_clean/auto_clean.htm

**Contents:**
- Automatic Geometry Clean-up

The automated geometry clean-up commands are used to automatically clean up geometry in preparation for meshing. These commands are built in to the ITEM interface, but they can also be used on their own. They include:

---

## Automatic Small Curve Removal

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/auto_clean/auto_small_curve.htm

**Contents:**
- Automatic Small Curve Removal

The automatic small curve removal command uses composites and collapse curves commands to automatically remove small curves from a volume. This is useful for removing small or unnecessary details from a model to facilitate meshing algorithms. The user enters a small curve size. Any curve smaller than this specified size will be removed. This command is issued from the ITEM toolbar. More information can be found by reading the section entitled Small Details in the Model in the ITEM documentation. This command can also be called from the command line. The syntax of this command is:

Auto_clean Volume <id_range> Small_curves Small_curve_size <val>

Note: The automatic curve removal should be used with caution, as the user has little control over how curves are removed.

The cylindrical model has 3 small curves just less than 0.7. The remove small curves command will remove two of the small curves by compositing two neighboring surfaces and the third using the collapse curve functionality.

auto_clean volume 1 small_curves small_curve_size .7

Figure 1. Automatic small curve removal on a cylinder

---

## Automatic Small Surface Removal

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/auto_clean/auto_small_surface.htm

**Contents:**
- Automatic Small Surface Removal

This auto clean command will attempt to remove small and narrow surfaces from the model by compositing them with neighboring surfaces. The user specifies a small curve size value. This value is used in two different ways. First, a small area is calculated as the small curve size squared. This value is used to compare against when looking for small surfaces. The small curve size is also used to identify surfaces that are narrower than the small curve size.

Auto_clean Volume <id_range> Small_surfaces Small_curve_size <val>

The cylindrical model has 2 small surfaces and a few narrow surfaces. The surfaces are composited to remove these.

Figure 1. Automatic small and narrow surface removal on a cylinder

---

## Automatic Surface Split

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/auto_clean/auto_narrow_region.htm

**Contents:**
- Automatic Surface Split

This auto clean command will attempt to automatically split narrow regions of surfaces. In this context, any surface that contains a portion that narrows down to a small angle is considered a narrow region. The command will use the split command from the underlying solid modeling kernel. The user specifies a size that defines what it narrow. This command also propagates the splits to neighboring narrow surfaces. This command is usually used as a preprocessor to the "tweak remove_topology" command but can also be used on its own.

Auto_clean Volume <id_range> Split_narrow_regions Narrow_size <val>

The model has a surface that necks down to a narrow region. This surface also has some neighboring narrow surfaces to which the splits are propagated.

Figure 1. Automatic small and narrow surface removal on a cylinder

---

## Auto Healing

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/healing/auto_healing.htm

**Contents:**
- Auto Healing

Healing is sometimes needed to fix models that have geometric problems. Geometry created in another modeling system and translated into an ACIS model may be imprecise due to the inherent limitations of the parent system, or due to limitations of data transfer through neutral file formats. This leads to problems such as gaps between entities and the absence of connectivity information (topology). Healing can fix these problems. The general steps to healing are:

Autohealing makes these steps automatic with the following command:

Healer Autoheal Body <id_range> [Keep]

The keep option will retain the original body, putting the resulting healed body in a new body.

---

## Bad geometry representation

**URL:** https://coreform.com/cubit_help/item/clean_up/geometry_representation.htm

**Contents:**
- Bad geometry representation
- Detecting Invalid Geometry
- Resolving Invalid Geometry

As a result of translation errors between CAD representations, errors or differences in the way the geometry is interpreted may occur. Depending on the severity of the problem, sometimes a mesh can be generated even with a less-than perfect geometric representation, however, in most cases, these should be resolved before meshing.

In most cases, bad or invalid topology or geometry definition comes from problems which arise in the CAD translation process. CUBIT’s main geometry kernel, ACIS is used to represent the model if it has been imported using an IGES or STEP format. Translation to and from these neutral formats is frequently the cause of bad geometry. ITEM will use the geometry validation procedures built into the ACIS kernel to detect if there is any bad geometry and will list the entities that may be causing a problem.

Since the validation procedures are specific to ACIS, models that may have been imported from another native format such as Pro/E will not provide this diagnostic. Although this may seem like a severe limitation, importing native formats rarely have bad geometry, since no translation process is necessary.

It is good practice to always check your model for bad geometry before proceeding to other geometry or meshing operations. In some cases, if a webcut or meshing operation fails, the cause is an invalid geometric definition that has not been adequately healed. Resolving bad geometry problems up front, in most cases is essential to obtaining a mesh. On the other hand, if the location of the bad geometry in the model is such that it will not effect subsequent Boolean or decomposition operations, there may be a chance that completely resolving bad geometry is not necessary. Simply ignoring bad geometry that cannot be easily repaired with automatic procedures may be a reasonable solution, provided the user is aware of the potential limitations.

To resolve invalid geometry, ITEM uses the heal procedure built into the ACIS geometry kernel. In almost all cases, this is a fully automatic procedure. Simply selecting the automatic repair button will make the appropriate adjustments to the geometry. This can be done one volume at a time by healing the owning volume, or by healing the full model all at once. If healing was successful, No problems detected should be displayed.

If auto repair does not successfully repair the geometry, you may want to try additional options available in Cubit for healing. See the Cubit documentation for a complete description of additional healing options.

---

## Basic Group Operations

**URL:** https://coreform.com/cubit_help/geometry/groups/basic_group_operations.htm

**Contents:**
- Basic Group Operations
- Geometry Groups
- Group Booleans
- Group Copy and Transform
- Deleting Groups
- Cleaning Out Groups

The common syntax to create or modify a group is to give it a name and a collection of entities:

Group ["name"] Equals <list of entities>

The Equals operation assigns the group to contain the given list. If the group already existed, its prior contents are overwritten. (Once a group is created, it can be refered to by id as well.) Here, entities can be geometry entities, mesh entities, or both. For example, the command,

group "Exterior" equals surface 1 to 2, curve 3 to 5

will create the group named (names are case sensitive). Any command taking entities can also take a group: e.g., mesh Exterior, list Exterior, or draw Exterior.

Geometry entities may specified by name as well. E.g.,

group 'Interior' add surface with name 'bill' 'john' 'fred'

will place the surfaces named 'bill' 'john' and 'fred' in the group Interior.

Wildcards (*) can also be used with names. To add all surfaces with the substring 'bob' in their name, use the command:

group 'interior' equals surface with name '*bill*'

There are a variety of operations for modifying the contents of a group, such as adding or removing entities. These can also be used to create a group from scratch by using a new name.

Group ["name" | <id>] Add <entity list>

Group ["name" | <id>] Remove <entity list>

Group ["name" | <id>] Xor <entity list>

Groups may also be created from the contents of existing groups by set booleans: Group A boolean B preposition C. These operations will also overwrite the contents of existing groups. The intersect command will create a new group that contains elements common to both groups: A = B ∩ C. The unite command collects entities that exist in either group: A = B ∪ C. The subtract command collect the entities in one group but not the other: A = C ∖ B.

Group {<'name'>|<id>} Intersect Group <id> with Group <id>

Group {<'name'>|<id>} Unite Group <id> with Group <id>

Group {<'name'>|<id>} Subtract Group <id> from Group <id>

The contents of a group can be copied and transformed (e.g. moved), or simply transformed. (The group itself is not copied, only the contents.) This works only for groups of geometry entities, or groups of free mesh elements without associated geometry. Groups can collect free mesh entities in much the same way as a geometric entity. If the optional copy keyword is provided, the entities in the group will be copied first, and the copy will be transformed. Geometric and mesh groups behave differently. For geometry groups, if the group contains geometric entities that are meshed, the mesh will also be copied and transformed, unless the optional nomesh keyword is specified. You can copy a single surface of a volume, but you cannot move just it, because geometric entities cannot be transformed unless the parent entity is also. In addition, all merged partners must be contained in the group. However, any geometric entity can be copied and transformed. For mesh groups, transforming the nodes will implicitly transform the elements containing those nodes. The copy keyword is ignored if the group contains mesh entities. These types of mesh groups can only contain free mesh entities; for copying and transforming mesh associated to geometry, use a geometry group. (In the following, recall that an existing group name can always be used in place of 'Group <id>'.)

Group <id> [Copy [nomesh]] [Move <dx> <dy> <dz>]

Group <id> [Copy [nomesh]] [Move {x|y|z} <distance>...]

Group <id> [Copy [nomesh]] [Move <direction> [distance]]

Group <id> [Copy [nomesh]] [Reflect {x|y|z}]

Group <id> [Copy [nomesh]] [Reflect <x> <y> <z>]

Group <id> [Copy [nomesh]] [Rotate <angle> About {x|y|z}]

Group <id> [Copy [nomesh]] [Rotate <angle> About <x> <y> <z>]

Group <id> [Copy [nomesh]] [Rotate <angle> About Vertex <Vertex_id1> <Vertex_id2>]

Group <id> [Copy [nomesh]] [Scale <scale> | x <val> y <val> z <val>]

Groups can be deleted with the following command:

Delete Group <id range> [Propagate]

The option propagate will also delete any contained groups, recursively. That is, if group A contains group B and group B contains group C, then Delete Group A Propagate will delete groups A, B, and C.

You can remove all of the entities in a group via the cleanout command:

Group <group_id_range> Cleanout [Geometry|Mesh] [Propagate]

By default all entities will be removed - optionally you can cleanout just geometry or mesh entities. As in delete, the propagate option will cleanout the group specified and all of its contained groups recursively.

---

## Blunt Tangency

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/blunt_tangency.htm

**Contents:**
- Blunt Tangency

The blunt tangency commands are used to eliminate small angles in the model caused by fillets. The operation 'blunts' the tangency, or small angle, using two different approaches. The first replaces the tangency with a pair of surfaces, essentially moving the vertex to a location with a larger angle. The second approach creates a surface with a larger radius through a tweak operation, increasing the sharp angle at the vertex.

Blunt tangency vertex <id> [remove_material] [composite] [angle <value>] [depth <value>] [preview]

Blunt tangency tweak vertex <ids> [angle <value>] [offset surface <id>] [tolerance <value>] [preview]

As shown in Figure 1, the depth parameter controls the depth of the surfaces that replace the tangency, while the angle parameter controls the resultant angle of the new tangency. Figure 2 demonstrates the behavior of the remove_material option which removes material instead of adding it.

Figure 1. Blunt Tangency Operation

Figure 2. Remove Material Option

Figure 3. Blunt Tangency with Composite Option. Highlighted surface is resulting composite surface.

The second form of the command replaces the surface with the radius at the vertex with a larger radius surface, increasing the angle. The command tweaks the surface that results in the least amount of material removed (Figure 4) or added (Figure 5). The angle option works the same as in the first form of the command. The offset surface option specifies which surface is tweaked (offset), as sometimes the surface that results in the smallest material added/removed is not correct. The tolerance option prevents small curves from being created, snapping to adjacent vertices within the tolerance (Figure 6) or possibly modifying an adjacent surface (Figure 7).

Figure 4. Blunt Tangency Tweak -- Material Removed

Figure 5. Blunt Tangency Tweak -- Material Added

Figure 6. Blunt Tangency Tweak -- Tolerance

Figure 7. Blunt Tangency Tweak -- Tolerance

---

## Bottom-Up Geometry Creation

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/bottom_up_creation/bottom_up_creation.htm

**Contents:**
- Bottom-Up Geometry Creation

CUBIT supports the ability to create geometry from a collection of lower order entities. This is accomplished by first creating vertices, connecting vertices with curves and connecting curves into surfaces. Currently only ACIS bodies or volumes may not be constructed by stitching a set of surfaces together, and only in a certain number of cases; however surfaces may also be swept or rotated to create bodies or volumes. Existing geometry may be combined with new geometry to create higher order entities. For example, a new surface can be created using a combination of new curves and curves already extant in the model. Commands and details for creating each type of geometry entity are given below.

The following describes each of the basic entities that can be generated with CUBIT using the bottom-up approach

---

## Chop Command

**URL:** https://coreform.com/cubit_help/geometry/decomposition/web_cutting/chop_command.htm

**Contents:**
- Chop Command

The chop command works similarly to a web cut command, but is faster. Given two bodies, the command will find the intersection of the two bodies, and divide the main body into a body that lies outside the intersection, and a body that lies inside the intersection. The tool body will be deleted, unless the keep option is specified. The syntax of the command is:

Chop [Volume|BODY] <id> with [Volume|BODY] <id> [keep] [nonreg]

The nonreg option results in the bodies being non-regularized.

---

## Clean Up the Geometry

**URL:** https://coreform.com/cubit_help/item/clean_up/clean-up.htm

**Contents:**
- Clean Up the Geometry

Meshing packages have the challenge of dealing with a host of geometry problems. Many of these problems can be generalized as file translation issues. Typically, the geometry used in a meshing package has not been created there but in one of many CAD packages. Exporting these files out of CAD and into a neutral file format (IGES, STEP, SAT) accepted by the meshing software can introduce misrepresentations in the geometry. If the CAD and meshing packages do not support the same file formats, a second translation may be necessary, possibly introducing even more problems.

Another complication caused by file translation is that of tolerances. Some CAD packages see two points as coincident if they are within 1e-3 units, while others use 1e-6. If the meshing software's tolerance is finer than the CAD package's, this disparity in tolerance can cause subsequent geometry modification operations in the meshing package to inadvertently create sliver features, which tend to be difficult and tedious to deal with. This tolerance problem also causes misalignment issues between adjacent volumes of assemblies, hindering the sharing of coincident geometry in order to produce a conformal mesh.

Modeling errors caused by the user in the CAD package is another problem that the meshing package has to correct. In the CAD package, the user may not create the geometry correctly, causing some parts to overlap, or introduce small gaps between parts that should touch. Many times these problems are detected in the meshing package at a point when it is not feasible to simply go back into the CAD system and fix the problem, so the meshing package must be capable of correcting it.

Several approaches for addressing the geometry cleanup problem have been proposed in the literature, but they typically provide operations that are automatically applied to the geometry once one or more topology problems have been identified. While very effective in many cases, they generally lack the ability for the user to have control over the resolution of these CAD issues while still maintaining the option for automation. The ITEM environment provides tools to both diagnose these common issues and to provide a list of solutions from which the user may select that will correct the problems.

For the purposes of mesh generation, features in a solid model that should be carefully considered and addressed prior to meshing generally fit in one of four categories:

Being able to recognize when a problem exists and what operations to apply to resolve issues in each of the four categories described above, is indeed an art-form and requires significant experience to become proficient. ITEM will not take the place of an experienced user, but it is intended to offer the user help along the way by detecting potential problems and suggesting solutions they might consider.

---

## Collapse Angle

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/collapse_geometry/collapse_angle.htm

**Contents:**
- Collapse Angle

The collapse command allows the user to collapse small angles using virtual geometry. The command syntax is:

Collapse Angle at Vertex <id range> [angle <degrees>] [Curve <id1> [Arc_length <length>]] [Curve <id2> [Arc_length <length> | Same_size | Perpendicular | Tangent]] [Composite_vertex <angle>] [Preview]

The collapse angle command is used to eliminate small angles at vertices, where curves meet at a tangential point. The command will split each curve at a specified distance (δ1 and δ2) as shown in Figure 1, and create two new vertices along those curves. The remaining small angle will be composited into its neighboring surface using virtual geometry. One of two methods may be used for specifying options for the collapse angle command: (1) Simple, and (2) Complete as described below:

Curves are not specified for this option. Instead, Cubit will automatically identify the smallest angle at the vertex and collapse it using the tangent option described below (see Figure 4). An optional angle option may also be specified that controls the arc length (δ1) along curve C1 where the curve will be split. If not specified a value of 30 degrees will be used. For the simple option of this command, a range of vertices may be used. The complete version of the command requires exactly one vertex and two curves.

The complete options of the command allow you to specify which curves and where to split each curve. You must input a distance for the first curve ( δ1 ), but the second location can be determined based on the length and direction of the first curve.

Figure 1. Collapse angle syntax

The arclength option will split each curve at a specified distance δ1 and δ2, (See Figure 1) measured from the vertex. You must input at least one arclength for each of the options listed below.

The same_size option will split curve 2 so that the two resulting curves, δ1 and δ2, are the same length as shown in Figure 2.

Figure 2. Collapse angle using the same_size option

The perpendicular option will split curve 2 so it is perpendicular to the split location on curve 1, as shown in Figure 3.

Figure 3. Collapse angle using the perpendicular option

The tangent option will split curve 2 where a line tangent to curve 1 at the split location intersects curve 2, as shown in Figure 4.

Figure 4. Collapse angle using the tangent option

The composite_vertex option automatically composites resulting surfaces if there are only two curves left at the vertex, and the angle is less than a specified tolerance.

The preview option will preview composited surface before applying changes.

Figure 5. An example of a meshed surface that is generated after using the collapse angle command.

---

## Collapse Curve

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/collapse_geometry/collapse_curve.htm

**Contents:**
- Collapse Curve

The collapse curve command allows the user to collapse small curves using virtual geometry. It is intended to be used in cases where removing a small curve to simplify topology will facilitate meshing. The operation can be thought of as reconnecting curves from one vertex on the small curve to the other vertex. If the user doesn’t specify which vertex to keep during the operation CUBIT will choose one of the vertices. The operation is performed using virtual partitions and composites on the curves and surfaces surrounding the small curve. The command syntax is:

Collapse Curve <id> [Vertex <id>] [Ignore] [Real_split]

The vertex keyword allows the user to specify which vertex on the small curve to keep during the operation or in other words which vertex to "collapse to". Depending on the surrounding topological configuration some vertices cannot currently be chosen so if the user specifies a vertex to collapse to that results in a complex topological configuration that CUBIT can’t currently handle the user will be notified and encouraged to pick a different vertex. If the user doesn’t specify a vertex CUBIT will attempt to choose the “best” vertex to keep based on surrounding topology and geometry. Currently, the collapse curve command only handles curves where the vertex that is NOT retained has a valence of 3 or 4.

The ignore keyword allows the user to specify whether or not small portions of surfaces that are partitioned off of one surface and composited with a neighboring surface during the collapse curve operation are considered when evaluating the new composite surface. By specifying the ignore option the user tells CUBIT that these small surfaces will be ignored in future evaluations of the composite surface. This can be beneficial in cases where the small surface makes a sharp angle with the neighboring surface it is being composited with. These first derivative discontinuities of composite surfaces can make it difficult for the meshing algorithms to proceed and ignoring the small surfaces during evaluation can help remedy this problem. By default the small surfaces will not be ignored.

The real_split option tells CUBIT to use the solid modeling kernel's (ACIS) split surface functionality to do the splitting rather than using virtual partitioning. The result is that you only have virtual composites at the end and no virtual partitions. The main advantage of using this option is that the solid modeling kernel's split operation is often more reliable than the virtual partition.

Figure 1 shows a typical example where the collapse curve command should be used to simplify the topology for meshing.

Figure 1. Example where the collapse curve operation is needed.

Figure 2 shows the above example after collapsing the small curve

Figure 2. Above example after collapsing the small curve.

---

## Collapse Geometry

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/collapse_geometry/collapse_geometry.htm

**Contents:**
- Collapse Geometry

The collapse geometry commands use virtual geometry to tweak small angles and curves to improve meshability of geometry models. The following options for collapsing geometry are available:

---

## Collapse Surface

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/collapse_geometry/collapse_surface.htm

**Contents:**
- Collapse Surface

The collapse surface command allows the user to remove surface boundaries from the model. This is accomplished by splitting the surface at two given locations and combining it into two adjacent surfaces using virtual geometry operations. The command syntax is:

Collapse Surface <id> Across Location1 Location2 With Surface <id_list> [Preview]

The locations option can use any of the general Cubit location commands. However, the vertex and curve options are among the most useful location options. For example, the command

collapse surface 15 across vertex 128 curve 40 with surface 26 117

would split surface 15 by the line that is formed between vertex 128 and the midpoint of curve 40. It would then composite the two parts of surface 15 that are adjacent to surfaces 26 and 117. The result is that three surfaces have been reduced to two.

The collapse surface command is most useful in removing blended surfaces (i.e. fillets and chamfers) from a model. For example, Figure 1 below shows a set of highlighted surfaces on a bracket. By collapsing all these surfaces the model shown in Figure 2 is created. Collapsing the surfaces for this model simplifies the model and allows for the creation of a higher quality mesh.

Figure 2. Bracket after highlighted edges have been collapsed

---

## Composite Curves

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/composite_geometry/composite_curve.htm

**Contents:**
- Composite Curves

The full command for the creation of composite curves is:

Composite Create Curve <id_range> [Keep Vertex <id_list>] [Angle <degrees>]

The additional arguments provide two methods to prevent vertices from being removed from the model or composited over. The first method, keep vertex explicitly specifies vertices which are not to be removed. This option can also be used to control which vertex is kept when compositing a set of curves results in a closed curve.

The angle option specifies vertices to keep by the angle between the tangents of the curves at that vertex. A value less than zero will result in no composite curves being created. A value of 180 or greater will result in all possible composites being created. The default behavior is an empty list of vertices to keep, and an angle of 180 degrees.

---

## Composite Geometry

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/composite_geometry/composite_geometry.htm

**Contents:**
- Composite Geometry

The virtual geometry module has the capability to combine a set of connected curves into a single composite curve, or a set of connected surfaces into a single surface. The general purpose is to suppress or remove the child geometry common to those entities being composited. For example, compositing a set of curves suppresses the vertices common to those curves, thus removing the constraint that a node must be placed at that vertex location.

The basic form of the command to create composites is:

Composite Create {Surface|Curve} <id_list>

This command will composite as many surfaces (or curves) as possible, in many cases creating multiple composites.

The entities combined to create the composite must either all be unmeshed or all be meshed. A meshed composite surface can not be removed unless the mesh is first deleted.

Care should be taken when compositing over large C1 discontinuities as it may cause problems for the meshing algorithms and may result in poor quality elements. C1 discontinuities are corners or abrupt changes in the surface normal.

The command to remove a composite is:

Composite Delete {Surface|Curve} <id>

---

## Composite Surfaces

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/composite_geometry/composite_surface.htm

**Contents:**
- Composite Surfaces
- Controlling the Surface Evaluation Method for Composite Surfaces
- Composite Determination

The general command for composite surface creation is:

Composite Create Surface <id_range> [Angle <degrees>] [Nocurves] [Keep [Angle <degrees>] [Vertex <id_list>]]

Graphics Composite {on|off}

The angle argument prevents curves from being removed from the model or composited over. Composites will not be generated where the angle between surface normals adjacent to the curve is greater than the specified angle.

When a composite surface is created, the default behavior is to also to composite curves on the boundary of the new composite surface.

Curves are automatically composited if the angle between tangents at the common vertex is less than 15 degrees. The nocurves option can be used to prevent any composite curves from being created.

The keep keyword can be used to change the default choice of which curves to composite. The arguments following the keep keyword behave the same as for explicit composite curve creation. The nocurves and keep arguments are mutually exclusive.

It typically takes longer to mesh a single composite surface than to mesh the surfaces used in the creation of the composite. To improve speed, composite surfaces use an approximation method to evaluate the closest point to a trimmed surface. However, this evaluation method may give poor results for composites of highly convoluted surfaces.

The virtual geometry module provides a way to change the way surfaces are evaluated using the following command:

Composite Closest_pt Surface <id> {Gme|Emulate}

The default behavior is to use the emulate method, as it is typically considerably faster. Specifying the gme option will force the specified composite surface to use the exact calculation of the closest point to a trimmed surface, as provided by the solid modeler. The gme option, however, can be considerably slower.

The composite create surface command is non-deterministic in some circumstances. When three or more adjacent surfaces are to be composited, all the surfaces may not be able to be composited into a single surface as illustrated in Figure 1. In this case different subsets of the surfaces may be composited and the command will choose arbitrary subsets to composite. As an example, there are three surfaces A, B, and C, all adjacent to each other. The common curve between A and B is AB, the common curve between B and C is BC, and the common curve between A and C is CA. If the curve BC cannot be removed, either due to the angle specified in the composite command, or because there is a fourth surface, D, also using that curve, the command will arbitrarily choose to either composite A and B or A and C.

Figure 1. In some cases, the program will make a determination of which surfaces to composite.

---

## Copy Command

**URL:** https://coreform.com/cubit_help/geometry/transforms/copy.htm

**Contents:**
- Copy Command

The copy command copies an existing entity to a new entity without modifying the existing entity. A copy can be made of several entities at once, and the resulting new entities can be translated or rotated at the same time. The commands for copying entities are:

Vertex <range> Copy [Move [X <dx>] [Y <dy>] [Z <dz>]] [Preview]

Vertex <range> Copy [Move <direction_options> [Distance <val>]] [Preview]

{Body|Volume|Surface|Curve|Vertex|Group} <range> Copy Move [X <dx>] [Y <dy>] [Z <dz>] [Nomesh] [Repeat <value>] [Preview]

{Body|Volume|Surface|Curve|Vertex|Group} <range> Copy Move <direction_options> [Distance <val>] [Nomesh] [Repeat <value>] [Preview]

{Body|Volume|Surface|Curve|Vertex|Group} <range> Copy Reflect {X|Y|Z} [Nomesh] [Preview]

{Body|Volume|Surface|Curve|Vertex|Group} <range> Copy Reflect [Vertex <v1_id> [Vertex] <v2_id] [Nomesh] [Preview]

{Body|Volume|Surface|Curve} <range> Copy Reflect <x> <y> <z> [Nomesh] [Preview]

{Body|Volume|Surface|Curve} <range> Copy Rotate <angle> About {X|Y|Z} [Repeat <value>] [Nomesh] [Preview]

{Body|Volume|Surface|Curve} <range> Copy Rotate <angle> About <x> <y> <z> [Nomesh] [Repeat <value>] [Repeat <value>] [Preview]

{Body|Volume|Surface|Curve} <range> Copy Scale <scale> | X <val> Y <val> Z <val> [About Vertex <id>] [Nomesh] [Repeat <value>] [Preview]

If the copy command is used to generate new entities, a copy of the original mesh generated in the original entity will also be copied directly onto the new entity unless the nomesh option is used.

Several of the commands include the Repeat token. If that token is used the command will repeat itself value times.

This is currently limited to copies that do not interact with adjacent geometry through non-manifold topology. For details on mesh copies, see the Mesh Duplication documentation.

---

## Creating ACIS Geometry From Mesh

**URL:** https://coreform.com/cubit_help/appendix/alpha/acis_geometry_from_mesh.htm

**Contents:**
- Creating ACIS Geometry From Mesh
  - Importing a Mesh
  - Existing Mesh - Create Mesh Geometry
  - Existing Mesh - Create Geometry

Note: These features are under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Using the Acis options (in red) in the commands below will produce ACIS geometry instead of mesh-based geometry. ACIS geometry is generally more desirable than mesh-based geometry because it can be modified easily.

Import Mesh Geometry '<exodusII_filename>' [Block <id_range>|ALL] [Unique Genesis IDs] [Start_id <id>] [Use [NODESET|no_nodeset] [SIDESET|no_sideset] [Feature_Angle <angle>] [LINEAR|Gradient|Quadratic|Spline|Acis] [Deformed {Time <time>|Step <step>|Last} [Scale <value>] ] [MERGE|No_Merge] [Export_facets <1|2|3>] [Merge_nodes <tolerance>]

This command tries to associate the mesh to the ACIS geometry that is created. If the association fails, the mesh ends up as free mesh. For more information on this command see: Importing Exodus II Files

Create Mesh Geometry {Hex|Tet|Face|Tri|Block} <range> [Feature_Angle <angle=135>] [Acis] [Keep]

This command tries to associate the mesh to the ACIS geometry that is created. If the association fails, the mesh ends up as free mesh. For more information on this command see: Free Meshes

Create Geometry {Hex|Tet|Face|Tri} <id_range>

These two commands do not use blocks, sidesets, nodesets or a user-specified dihedral angle to create vertices, curves, and surfaces. These commands use a proprietary third-party routine to create geometry. They also do not associate the mesh to the ACIS geometry that is created.

---

## Creating Bricks

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/primitive_geometry/creating_bricks.htm

**Contents:**
- Creating Bricks

The brick is a rectangular parallelepiped.

[Create] Brick {Width|X} <width> [{Depth|Y} <depth>] [{Height|Z} <height>] [Bounding Box {entity_type} <id_range>] [Tight] [[Extended] {Percentage| Absolute} <val>]]

---

## Creating Curves

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/bottom_up_creation/curve.htm

**Contents:**
- Creating Curves

Curves are created by specifying the bounding lower-order topology (i.e. the vertices) and the geometry (shape) of the curve (along with any parameters necessary for that geometry). There are several forms of this command:

1. Straight: The first form of the command creates a straight line or a line lying on the specified surface. If a surface is used, the curve will lie on that surface but will not be associated with the surface's topology.

Create Curve [Vertex] <vertex_id> [Vertex] <vertex_id> [On Surface <surface_id>]

Straight curves can be created using an axis. The syntax is as follows:

Create Curve Axis {options}

The length of the axis must be specified. Go to Location, Direction, and Axis Specification to see the axis command description.

Additionally, several connected straight curves can be created with a single command. The syntax for the polyline command is as follows:

Create Curve Polyline Location {options} Location {options} ...

Notice that two or more locations are used to define a polyline. See Location, Direction, and Axis Specification for the location command description.

2. Parabolic, Circular, Ellipse: The parabolic option creates a parabolic arc which goes through the three vertices. The circular and ellipse options create circular and elliptical curves respectively that go through the first and last vertices.

Create Curve [Vertex <vertex_id> [Vertex] <vertex_id> [[Vertex] <vertex_id> [Parabolic|Circular|ELLIPSE [start angle <val=0>] [stop angle <val=90>]]]

If 'ellipse' is specified, Cubit will create an ellipse assuming the vectors between vertices (1 and 3) and (2 and 3) are orthogonal. v1-v3 and v2-v3 define the major and minor axes of the ellipse and v3 defines the center point. These vectors should be at 90 degrees. If not, Cubit will issue a warning indicating the vertices are not sufficient to create an ellipse and will then default to creating a spiral.

The angle options will specify what portion of the ellipse to create. If none are specified, start angle will default to 0 and stop angle to 90 and the ellipse will go from vertex 1 to vertex 2; if the vertices are free vertices they will be consumed in the ellipse creation. Start angle tells Cubit where to start the ellipse -- the angle from the first axis (v1 - v3) specified. Stop angle tells Cubit where to end the ellipse -- the angle from the first axis. The angle follows the right-hand rule about the normal defined by (v1 - v3) X (v2 - v3).

3. Spline: The spline form of the command creates a spline curve that goes through all the input vertices or locations. To create a curve from a list of vertices use the syntax shown below. The delete option will remove all of the intermediate vertices used to create the spline leaving only the end vertices.

Create Curve [Vertex] <vertex_id_list> [Spline] [Delete]

Additionally, spline curves can be created by inputting a list of locations. Where the spline will pass through all of the specified locations. The syntax is shown below:

Create Curve Spline {List of locations}

See Location, Direction, and Axis Specification to view the location specification syntax.

4. Copy: This command actually copies the geometric definition in the specified curve to the newly created curve. The new curve is free floating.

Create Curve From Curve <curve_id>

5. Combine Existing Curves: This command creates a new curve from a connected chain of existing ACIS curves.

Create Curve combine curve <id_list> [delete]

6. Arc Three: The following command creates an arc either through 3 vertices or tangent to 3 curves. The Full qualifier will cause a complete circle to be created.

Create Curve Arc Three {Vertex|Curve} <id_list> [Full]

7. Arc End Vertices and Radius: The following command creates an arc using two vertices, the radius and a normal direction. The Full qualifier will cause a complete circle to be created.

Create Curve Arc Vertex <id_list> Radius <value> Normal {<x> <y> <z> | {direction options} [Full]

Go to Location, Direction, and Axis Specification to see the direction command description.

8. Arc Center Vertex: The next form of the command creates an arc using the center of the arc and 2 points on the arc. The arc will always have a radius at a distance from the center to the first point, unless the Radius value is given. Again, the Full qualifier will cause a complete circle to be created.

Create Curve Arc Center Vertex <center_id> <end1_id> <end2_id> [Radius <value>] [Full] [Normal {<x> <y> <z> | {direction options}]

Go to Location, Direction, and Axis Specification to see the direction command description.

Note: Requires 3 Vertices - first is the center, the other two are the end points of the arc. A normal direction is required when the three points are colinear. Otherwise a normal direction is optional.

9. Arc Center Angle: This form of the command creates an arc using the center position of the arc, the radius, the normal direction and the sweep angle.

Create Curve Arc Center {<x=0> <y=0> <z=0> | {location options} Radius <value> Normal {<x> <y> <z> | {direction options} Start Angle <value=0> Stop Angle <value=360>

Go to Location, Direction, and Axis Specification to see the location and direction command descriptions.

10. From Vertex Onto Curve: The following command will create a curve from a vertex onto a specified position along a curve. If none of the optional parameters are given, the location on the curve is calculated as using the shortest distance from the start vertex to the curve (i.e., the new curve will be normal to the existing curve).

Create Curve From Vertex <vertex_id> Onto Curve <curve_id> [Fraction <f> | Distance <d> | Position <xval><yval><zval> | Close_To Vertex <vertex_id> [[From] Vertex <vertex_id> (optional for 'Fraction' & 'Distance')]] [On Surface <surface_id>]

Note: Default = Normal to the Curve

11. Offset: The next command creates curves offset at a specified distance from a planar chain of curves. The direction vector is only needed if a single straight curve is given. The offset curves are trimmed or extended so that no overlaps or gaps exist between them. If the curves need to be extended the extension type can be Rounded like arcs, Extended tangentially (the default -straight lines are extended as straight lines and arcs are extended as arcs), or extended naturally.

Create Curve Offset Curve <id_list> Distance <val> [Direction <x> <y> <z>] [Rounded|EXTENDED|Natural]

Note: Direction is optional for offsets of individual straight curves only

In all cases, the specified vertices are not used directly but rather their positions are used to create new vertices.

12. From Mesh Edges: This commands creates a curve from an existing mesh given a starting node and an adjacent edge.

Create Curve From Mesh Node <id> Edge <id> [Length <val>]

The adjacent edge indicates which direction to propagate the curve. The curve will be composed of mesh edges up to the specified length. If no length is specified the curve will propagate as far as the boundary of the mesh. Figure 1 shows a example of a curve generated from the mesh.

Figure 1. Example of curve created from mesh

The underlying geometry kernel used for this command is Mesh-Based geometry. The new curve will also be meshed with the edges it was propagated through. A related command for assigning mesh edges directly to a mesh block is the Rebar command. See Element Block Specification for more details.

Note: Full hexes or full tets must be used to propagate the curves through the interior of volume.

13. Close_To This option takes two geometric entities and creates the shortest possible curve between the two entities at the location where the two entities are the closest. The two entities may NOT intersect. If two vertices are given, the command will create a straight line between the two vertices.

Create Curve Close_To {Vertex|Curve|Surface|Volume|Body} <id_1> {Vertex|Curve|Surface|Volume|Body} <id_2>

14. Surface Intersection The following command creates curves at surface intersections. Multiple curves can be created from a single command.

Create Curve Intersecting Surface <id_list>

15. By Projection The project command projects curves, or the curves of a surface another a single surface or multiple surfaces of a volume or body. The command syntax is as follows:

Project { Curve <id_list> | Surface <id_list> } Onto Surface <surface_id> [Imprint [Keepcurve] [Keepbody]] [Trim]

Project { Curve <id_list> | Surface <id_list> } Onto {Body <id> | Volume <id>} [Target_surface <id_list>] [Imprint [Keepcurve] [Keepbody]]

The first form of the command takes a list of curves or surfaces, and a projection surface. If a list of curves is given, the result will be the creation of a set of free curves on top of the projection surface. If a list of surfaces is given, the result will be the same as selecting the curves of the surface (i.e. a group of free curves on the projecting surface).

The second form will imprint the list of curves (or curves of the surface(s)) onto the surfaces of the specified bodies or volumes. The Target_surface option helps when the projection is ambiguous, for example projecting curves onto a thin-walled volume where the projection could be to either side, as shown in Figure 2.

Figure 2. Example of projecting curves to specific side of thin-walled volume.

The imprint option will imprint the resulting projected curves onto the projection surface. If this option is NOT given, the new curves will lie coincident to the surface, but will not be part of the surface. Imprinting changes the topology of the projection surface. Keepcurve option retains the new curves as both free curves, and curves in the projection surface. The keepbody option retains the original body under the new imprinted body. When projecting curves, the trim option will cause the curve to be trimmed to the target surface.

16. Creating a Helix: This command will create a helical curve. The command syntax is as follows:

Create Curve Helix { axis <xpoint ypoint zpoint xvector yvector zvector> | xaxis | yaxis | zaxis } location (options) thread_distance <value> angle <value> [RIGHT_HANDED | left_handed]

axis = axis about which to create the helix

location (options) = starting point of the helix

thread_distance = distance between each 360 degree segment of the helix

angle = number of degrees in rotation of the helix

handedness = right-handed or left- handed threads

17. Tangents: This command will create a spline curve by specifying the end points and the tangents at those points. The command syntax is as follows:

create curve tangent vertex <id> vertex <id> [start direction (options)] [end direction (options)]

create curve tangent start location (options) end location (options) start direction (options) end direction (options)

Both forms of the command can be broken into two parts: the points and the tangent directions. The first point is associated with the start direction.

The first form of the command takes an existing vertex and an optional tangent direction. If the direction is not specified, it will be taken from the tangent at the endpoint of the connected curve. If the vertex is not connected to a curve, or it is connected to multiple curves, the direction must be specified. If the vertex is not connected to a curve, it will be incorporated into the new curve. Otherwise, a new vertex will be created for the new curve.

The second form of the command takes a location and a tangent direction. The directions must be specified and vertices will be created for the locations.

The two command forms can also be mixed. A curve can be created from an existing vertex and a specified location.

create curve tangent start location 0 0 0 end location 1 1 0 start direction 1 0 0 end direction 1 0 0

Figure 3. Create tangent curve with locations and tangent directions

create curve tangent vertex 1 vertex 3

Figure 4. Create tangent curve by specifying vertices on curves. Tangents are extracted from the curve at the vertex location.

Go to Location, Direction, and Axis Specification to see the location and direction command description.

---

## Creating Cylinders

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/primitive_geometry/cylinder.htm

**Contents:**
- Creating Cylinders

The cylinder is a constant radius tube with right circular ends.

[Create] Cylinder [Height|Z] <val> Radius <val>

[Create] Cylinder [Height|Z] <val> Major Radius <val> Minor Radius <val>

[Create] Cylinder Volume <id> [Axis <options>]

---

## Creating Frustums

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/primitive_geometry/creating_frustums.htm

**Contents:**
- Creating Frustums

A frustum is a general elliptical right frustum, which can also be thought of as a portion of a right elliptical cone.

[Create] Frustum [Height|Z] <z-height> Radius <x-radius> [Top <top_radius>]

[Create] Frustum [Height|Z] <z-height> Major Radius <radius> Minor Radius <radius> [Top <top_radius>]

[Create] Frustum Volume <id> [Axis <options>]

---

## Creating Prisms

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/primitive_geometry/prism.htm

**Contents:**
- Creating Prisms

The prism is an n-sided, constant radius tube with n-sided planar faces on the ends of the tube.

[Create] Prism [Height|Z] <z-val> Sides <nsides> Radius <radius>

---

## Creating Pyramids

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/primitive_geometry/creating_pyramids.htm

**Contents:**
- Creating Pyramids

A pyramid is a general n-sided prism.

[Create] Pyramid [Height|Z] <z-height> Sides <nsides> Radius <radius> [Top <top-x-radius>]

[Create] Pyramid [Height|Z] <z-height> Sides <nsides> [Major [Radius] <x-radius> Minor [Radius] <y-radius> ] [Top <top-x-radius>]

---

## Creating Spheres

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/primitive_geometry/sphere.htm

**Contents:**
- Creating Spheres

The sphere command generates a simple sphere, or, optionally, a portion of a sphere or an annular sphere.

[Create] Sphere Radius <radius> [Xpositive]|[Xnegative] [Ypositive]|[Ynegative] [Zpositive]|[Znegative] [Delete] [Inner [Radius] <radius>]

---

## Creating Surfaces

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/bottom_up_creation/surface.htm

**Contents:**
- Creating Surfaces

There are two major ways to create surfaces in CUBIT. First, surfaces can be created in CUBIT by fitting an analytic or spline surface over a set of bounding curves. In this case, the curves must form a closed loop, and only one loop of curves may be supplied. The second method, is by sweeping a curve about an axis, along a vector, or along another curve. The result of these surface creation commands is a "sheet body" or a body that has zero measurable volume (it does however have a volume entity). This body may be decomposed with booleans and special webcutting commands or it may be used as a tool to decompose other bodies. Booleans can be used to cut holes out of these surfaces.

The following options may be used for creating a surface in CUBIT.

1. Bounding Curves: The first form of this command produces an analytic or spline surface fit to cover the bounding curves.

Create Surface Curve <curve_id_1> <curve_id_2> <curve_id_3>...

Another version of this command creates a surface from a set of bounding curves that all lie on one surface. If the curves are selected they must lie on the surface, and they must create a closed loop. The On Surface option forces the surface to match the geometry of the underlying surface exactly.

Create Surface Curve <id_list> On Surface <surface_id>

2. Bounding Vertices or Nodes: The second form of this command uses vertices to fit an analytic spline surface. The On Surface option creates the surface from a set of nodes and vertices that all lie on one surface and restrains the surface to match the geometry of the underlying surface. The project option will project the nodes or vertices to the specified surface.

Create Surface [Node|Vertex| <id_list> [On Surface <surface_id> {Project} ]

3. Copy: The next form creates a surface using the same geometric description of the specified surface. The new surface will be a stand-alone sheet body that is geometrically identical to the user supplied surface.

Create Surface From Surface <surface_id>

4. Extended Surface: The fourth form of the command creates a surface that is extended from a given surface or list of surfaces. The specified surface's geometry is examined and extended out "infinitely" relative to the current model in CUBIT (i.e. extended to just beyond the bounding box of the entire model). The given surfaces are extended as shown in the table.

Create Surface Extended From Surface <surface_id>

Table 1. Surface Extension Results

Resulting Extended Surface

Plane of infinite size relative to model

Conical, cone, cylinder...

Shell of outside conic axially aligned with given conic of infinite height relative to model

Surface is extended to extents of the spline definition. This may not be any further than the surface itself, so caution should be used here.

Multiple surfaces can be offset at the same time to form a sheet body, by using the Create Sheet Extended from Surface command.

5. Planar Surface: The following commands create planar surfaces. The first passes a plane through 3 vertices, the second uses an existing plane, the third creates a plane normal to one of the global axes, and the fourth creates a plane normal to the tangent of a curve at a location along the curve. By default, the commands create the surface just large enough to intersect the bounding box of the entire model with minimum surface area. Optionally, you can give a list of bodies to intersect for this calculation. You can also extend the size of the surface by either a percentage distance or an absolute distance of the minimum area size. The plane can be previewed with the command Draw Plane [with]... (where the rest of the command is the same as that to create the surface).

Create Planar Surface [With] Plane Vertex <v1_id> [Vertex] <v2_id> [Vertex] <v3_id> [Intersecting] Body <id_range>] [Extended Percentage|Absolute <val>]

Create Planar Surface [With] Plane Surface <surface_id> [Intersecting] Body <id_range>] [Extended Percentage|Absolute <val>]

Create Planar Surface [With] Plane {Xplane|Yplane|Zplane} [Offset <val>] [Intersecting] Body <id_range>] [Extended Percentage|Absolute <val>]

Create Planar Surface [With] Plane Normal To Curve <curve_id>{Fraction <f>| Distance <d> | Position <xval><yval><zval> | Close_to vertex <vertex_id>} [[From] Vertex <vertex_id> (optional for 'fraction' & 'distance')] [Intersecting] Body <id_range>] [Extended Percentage|Absolute <val>]

6. Net Surface: Net surfaces can be created with two different commands. A net surface passes through a set of curves in the u-direction and a set of curves in the v-direction (these u and v curves would looked like a mapped mesh). The first form of the command uses curves to create the net surface. The curves must pass within tolerance of each other to work. The second form uses a mapped mesh to create the surface. The mapped mesh can be of a single surface or a collection of mapped or submapped surfaces that form a logical rectangle. By default net surfaces are healed to take advantage of any possible internal simplification.

Create Surface Net U Curve <id_list> V Curve <id_list> [Tolerance <value>] [HEAL|Noheal]

Create Surface Net [From] [Mapped] Surface <id_list> [Tolerance <value>] [HEAL|Noheal]

A suggested geometry cleanup method is to use a virtual composite surface to map mesh a set of complicated surfaces then create a net surface from this mesh. Then the original surfaces can be removed with the noextend option and the new net surface combined back onto the body.

7. Offset: The following command creates surfaces offset from existing surfaces at the specified distances.

Create Surface Offset [From] Surface <id_list> Distance <val>

The surface offset command will only translate the existing surfaces, without extending or trimming them. An alternate form of the command for sheet bodies will maintain connections between surface by extending or trimming as they are offset, shown in Figure 1. On the left, the surfaces are offset using the surface offset command. On the left, the surface is created by using the "sheet" version of the command.

Figure 1. Offsetting surfaces to form individual surfaces or sheet bodies

8. Skinning: The following command creates a skin surface from a list of curves. An example of a skin surface is to create a surface through a set of parallel lines.

Create Surface Skin Curve <id_list> [pair tolerance <val>

The pair tolerance option indicates vertices on curves to skin will be paired up with a given tolerance. If a pair cannot be found for a vertex, a new vertex is inserted to split a curve and make a pair. This option is useful to control creation of lateral curves in the new surface and to avoid skew for meshes created on those surfaces.

9. Sweeping of Curves: A curve or a set of curves can be swept along a path to create new surfaces. The path may be specified as an axis and angle, a vector and distance, by indicating another curve or set of contiguous curves, or by specifying a target plane. The following commands show the options available:

Sweep Curve <curve_id_range> { Axis <xpoint ypoint zpoint xvector yvector zvector> | Xaxis | Yaxis | Zaxis } Angle <degrees> [Steps <Number_of_sweep_steps>] [Draft_angle <degrees>] [Draft_type <integer>] [Make_solid] [Include_mesh] [Keep][Rigid]

Sweep Curve <curve_id_range> Vector <xvector yvector zvector> [Distance <distance>] [Draft_angle <degrees>] [Draft_type <integer>] [Include_mesh] [Keep] [Rigid]

Sweep Curve <curve_id_range> Along Curve <refcurve_id_range> [Draft_angle <degrees>] [Draft_type <integer>] [Include_mesh] [Keep] [Rigid]

Sweep Curve <curve_id_range> Target Plane <options>

Sweep Curve <curve_id_range> Target {Volume|Body} <id> Direction {options} [Plane <options>] [Unite]

In the first command, the steps options provides a way of faceting the sweep, so instead of a smooth round sweep, there are facets to the surface. The make_solid option closes the newly-created surface to the axis, so that a solid is created instead of a surface.

In the above commands, the include_mesh option will create a surface mesh if the curve is already meshed (see figure below). The keep option will keep the original curve while creating the surface.

The sweep curve target plane command sweeps a curve until it hits a target plane. The options for the target plane are described under Specifying a Plane.

The last command sweeps a curve to a target volume or body and can only be used on sheet bodies. Use the direction keyword to specify the sweep direction and the plane keyword to specify a stopping plane. The unite keyword will unite the sheet bodies after sweeping

The other options are as follows:

draft_angle: determines how much drafting in of the surface is desired

draft_type: 0 => extended (draws two straight tangent lines from the ends of each segment until they intersect) 1 => rounded (create rounded corner between segments) 2 => natural (extends the shapes along their natural curve) ***

rigid: normally the curve will rotate to maintain its original orientation to the sweep path. The rigid option disallows this rotation.

10. Midsurface: Multisurfaces may be created midway between pairs of surfaces using the following command:

Create Midsurface {Body|Volume} <id> Surface <id11> <id12> ... <idN1> <idN2>

where N denotes the number of pairs of surfaces. An even number of surfaces must be specified, and the command will group them by pairs in the order in which they are provided. The resulting surface will be trimmed by the specified body or volume <id>. This replaces the Create Midplane command in previous versions of CUBIT.

Figure 2. Multisurface created with the Create Midsurface command

Figure 3. Midsurface created from 2 pairs of cylindrical surfaces

Midsufaces can also be extracted without surface pair specification if the resulting surface is a single sheet of surfaces (no T intersections). The following is the command syntax for automatic midsurface extraction:

Create Midsurface {Body|Volume} <id_range> Auto [Delete] [Transparent] [Thickness] [Limit <lower_bound> <upper_bound>] [Preview]

Figure 4 shows a simple auto midsurface example. The command for the example is:

create midsurface volume 1 auto delete

Figure 4. Midsurface created from a volume

The command option descriptions are listed below.

Auto enables the automatic mid-surface algorithm. Turning Auto off requires the user to specify a single surface pair to create a mid-surface.

Transparent shows the successfully midsurfaced volumes as transparent in the graphics display

Thickness applies a 2D property to the created mid-surface geometry.

Limit search range gives the algorithm a range to find surface pairs within.

11. Weld Profile: Surfaces may be created by specifying a weld profile using the following command:

Create Surface Weld [Root] Location {options} Weld Surface <id_list> Length <val> [<val2>]

Weld surfaces can be used to create a simulated welded joint by sweeping the surface along the root curve and uniting the new body to the model. An example of the command is illustrated below. For a detailed description of the location specifier see Location Direction, and Axis Specification.

create surface weld root location vertex 25 weld surface 13 14 length 2

Figure 5. Weld Profile surface with length and root specifications

12. Creating A Surface From Mesh Entities: Surfaces may be created from the boundaries of meshed volumes, surfaces, and/or from individual quadrilateral mesh elements. The individual option makes it so you can enter multiple surfaces at once, and not have them merged together into a larger surface, but instead retain their own original boundaries. The optional tolerance value allows the user to specify a tolerance to which the resulting surface should be fit. The default value is 0.001. If surface creation fails, increasing the tolerance value can help.

Create Acis [From] {Surface <id_range> | Volume <id_range> | Face < id_range> [Individual]} [Tolerance <value>]

Figure 6. Acis Surface created from a Set of Quadrilaterals

13. Creating a Circular Surface: This command creates a 2D circular surface. The surface will be centered at the origin and on the z-plane if a plane option is not specified.

This command creates a 2D circular surface by specifying three vertices; the first vertex will be the center of the surface, the second vertex will be used to define the radius of the surface, and the third vertex will assist in defining the plane that the surface will lie in.

This command creates a 2D circular surface by forming a circular curve through three points.

14. Creating a Parallelogram: This command creates a 2D parallelogram surface, centered at the origin, by specifying three corner vertices. These vertices will form three consecutive corners of the parallelogram surface.

15. Creating an Ellipse: This command creates a 2D elliptical surface, centered at the origin, by specifying at least a major radius. On an x-y plane this radius will be the radius along the x-direction. The minor radius will be the radius along the y-direction. By default, the surface will lie in the z-plane.

Create Surface Ellipse major radius <value> [minor radius <value>] [xplane|yplane|ZPLANE]

This command creates a 2D elliptical surface using three vertices. The first two vertices define the major and minor radii of the ellipse surface. The third point defines the center of the ellipse. It is important to note that a line from v1_id to v3_id must be orthogonal to a line from v2_id to v3_id, otherwise the command will fail.

Create Surface Ellipse vertex <v1_id> <v2_id> <v3_id>

16. Creating a Rectangle: This command creates a rectangular surface centered at the origin. If only a width value is specified, the surface will be a square. On an x-y plane, the width value is the x-direction and the height is the y-direction. By default, the surface will lie in the z-plane.

Create Surface rectangle width <value> [height <value>] [xplane|yplane|ZPLANE]

**Examples:**

Example 1 (typescript):
```typescript
create surface circle radius <value> {xplane|yplane|ZPLANE}
```

Example 2 (typescript):
```typescript
create surface circle center vertex <v1_id> <v2_id> <v3_id>
```

Example 3 (typescript):
```typescript
create surface circle vertex <v1_id> <v2_id> <v3_id>
```

Example 4 (typescript):
```typescript
create surface parallelogram vertex <v1_id> v2_<id> <v3_id>
```

---

## Creating Toruses

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/primitive_geometry/creating_torus.htm

**Contents:**
- Creating Toruses

The torus command generates a simple torus

[Create] Torus Major [Radius] <major-radius> Minor [Radius] <minor-radius>

[Create] Torus Volume [ID]

---

## Creating Vertices

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/bottom_up_creation/vertex.htm

**Contents:**
- Creating Vertices

The basic commands available for creating new vertices directly in CUBIT are:

1. XYZ location: The simplest form of this command is to specify the XYZ location of the vertex. It can also be created lying on a curve or surface in the geometric model by specifying the curve or surface id; the position of the vertex will be the point on the specified entity which is closest to the position specified on the command. With all of these commands, the user is able to specify the color of the vertex.

Create Vertex <x><y><z> [On [Curve | Surface] <id>] [Color <color_name>]

2. On Curve - Fraction: A vertex can be positioned a certain fraction of the arc length along a curve using the second form of the command.

Create Vertex On Curve <id> Fraction <0.0 to 1.0> [Color <color_name>]

Vertex 3 in the following example was created with this command:

create vertex on curve 1 fraction 0.25 from vertex 1

Figure 1. Create Vertex a Fraction of the length of a Curve

3. On Curve - General: A more general purpose form of the command is also available for creating vertices on curves:

Create Vertex On Curve <id_list> { MIDPOINT | Start | End | Fraction <val 0.0 to 1.0> [From Vertex <id> | Start|End] | Distance <val> [From {Vertex|Curve|Surface} <id> | Start|End] | {{Close_To|At} Location {options} | Position <xval><yval><zval>|{Node|Vertex} <id>} | Extrema [Direction] {options} [Direction {options}] [Direction {options}] | Segment <num_segs> | Crossing {Curve|Surface} <id_list> [Bounded|Near] } [Color <color_name>]

It allows the vertex to be created at a fractional distance along the curve, at an actual distance from one of the curves ends, at the closest location to an xyz position or another vertex, or at a specified distance from a vertex, curve or surface. You can also preview the location first with the command Draw Location On Curve (where the rest of the command is identical to the Create Vertex form).

4. From Vertex: Create a vertex from an existing vertex.

Create Vertex from Vertex <id_list> [ On {Curve|Surface} <id> ] [Color <color_name>]

If 'on curve|surface' option is used, the vertex is positioned on that curve or surface. When the 'on curve|surface' is not used, the new vertex is positioned on the existing vertex.

5. At Arc: Another form simply creates vertices at arc or circle centers.

Create Vertex Center Curve <id_list> [Color <color_name>]

6: At Intersection: The last form creates vertices at the intersection of two curves. If the bounded qualifier is used, the vertices are limited to lie on the curves, otherwise the extensions of the curves are also used to calculate the intersections. The near option is only valid for straight lines, where the closest point on each curve is created if they do not actually intersect (resulting in two new vertices).

Create Vertex AtIntersection Curve <id1> <id2> [Bounded] [Near] [Color <color_name>]

---

## Creating Volumes

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/bottom_up_creation/body.htm

**Contents:**
- Creating Volumes

Currently, CUBIT can create volumes:

Sweeping of planar surfaces, belonging either to two- or three-dimensional bodies, is allowed, and some non-planar faces can be swept successfully, although not all are supported at this time. The following methods for generating volumes are described:

There are five forms of the sweep command; the syntax and details for each are given below. Common options for first four forms are:

draft_angle: This parameter specifies the angle at which the lateral faces of the swept solid will be inclined to the sweep direction. It can also be described as the angle at which the profile expands or contracts as it is swept. The default value is 0.0.

draft_type: This parameter is an ACIS-related parameter and specifies what should be done to the corners of the swept solid when a non-zero draft angle is specified. A value of 0 is the default value and implies an extended treatment of the corners. A value of 1 is also valid and implies a rounded (blended) treatment of the corners.

anchor_entity: The default behavior for the sweep command is to move the source surface along a path to create a new 3D solid. The anchor_entity option instructs the sweep to leave the source surface in its original location.

include_mesh: This option will sweep the source surface and existing mesh into a meshed 3D solid. The mesh size is automatically computed using the Default auto interval specification.

The sweep operations have been designed to produce valid solids of positive volume, even though the underlying solid modeling kernel library that actually executes the operation, ACIS, allows the generation of solids of negative volume (i.e., voids) using a sweep.

1. Sweep Surface Along Vector: Sweeps a surface a specified distance along a specified vector. Specifying the distance of the sweep is optional; if this parameter is not provided, the face is swept a distance equal to the length of the specified vector. The include_mesh option will create a volumetric mesh if the surface is already meshed as shown below. The keep option will keep the original surface while creating the volume.

Sweep Surface {<surface_id_range>} Vector <x_vector y_vector z_vector> [Distance <distance_value>] [switchside] [Draft_angle <degrees>] [Draft_type <0|1>][rigid][anchor_entity][include_mesh] [keep] [merge]

Surface mesh swept along a vector

2. Sweep Surface About Axis: Sweeps a surface about a specified vector or axis through a specified angle. The axis of revolution is specified using either a starting point and a vector, or by a coordinate axis. This axis must lie in the plane of the surfaces being swept. The steps parameter defaults to a value of 0 which creates a circular sweep path. If a positive, non-zero value (say, n) is specified, then the sweep path consists of a series of n linear segments, each subtending an angle of [( sweep_angle ) / ( steps-1 )] at the axis of revolution. The include_mesh option will create a volumetric mesh if the surface is already meshed as shown below. The keep option will keep the original surface while creating the volume.

Sweep Surface {<surface_id_range>} Axis {<xpoint ypoint zpoint xvector yvector zvector>|Xaxis|Yaxis|Zaxis} Angle <degrees> [switchside] [Steps <number_of_sweep_steps>] [Draft_angle <degrees>] [Draft_type <0|1>][rigid][anchor_entity][include_mesh] [keep] [merge]

Surface swept around an axis of 50 degree angle

Specifying multiple surfaces that belong to the same body will not work as expected, as ACIS performs the sweep operation in place. Hence, if a range of surfaces is provided, they ought to each belong to different bodies.

3. Sweep Surface Along Curve: This command allows the user to sweep a planar surface along a curve:

Sweep Surface <surface_id_range> Along Curve <curve_id> [Draft_angle <degrees>] [Draft_type <0 | 1 | 2>] [Twist <degrees>][rigid][anchor_entity][include_mesh] [keep] [individual] [merge]

One of the ends of the curve must fall in the plane of the surface and the curve cannot be tangential to the surface. The relationship between the surface orientation and the guide curve is maintained through out the sweep. If the "rigid" option is specified the orientation of the surface is kept static throughout the sweep. Sweep along curve also supports an additional draft type "2" which implies a "natural" extension of the corners from their curves.

The optional twist option applies a twist to the swept solid about the guide curve. The specified angle, in degrees, is the total twist applied along the entire sweep path.

Volume swept along a curve with a twist angle applied.

The include_mesh option will create a volumetric mesh if the surface is already meshed as shown below. The keep option will keep the original surface while creating the volume. If multiple curves to sweep along are specified, the individual option creates an individual or separate volume along each curve.

Volume generated by sweeping a surface along a reference curve

4. Sweep Surface Perpendicular: This command allows the user to sweep a planar surface perpendicular to the surface:

Sweep Surface <surface_id_range> Perpendicular Distance <distance> [Switchside] [Draft_angle <degrees>] [Draft_type <integer>][anchor_entity][include_mesh] [keep] [merge]

The sweeping plane must be planar in order to determine the sweep direction. The switchside option will reverse the direction of the sweep.

The original surface is retained with the 'keep' option. A new volume is created by sweeping the surface along the surface normal.

The include_mesh option will create a volumetric mesh if the surface is already meshed as shown below. The keep option will keep the original surface while creating the volume.

5. Sweep Surface to a Volume: This command allows users to sweep a surface to a volume.

Sweep Surface <surface_id_range> Target {Volume|Body} <id> [Direction {options}] [Plane {options}]

The direction keyword can be used to control the direction of sweep. Without it, Cubit will determine the sweep direction (usually normal to the sweeping surface). The plane option can be used to define a stopping plane.

6. Offset: The following command creates a body offset from another body or set of surfaces at the specified distance. The new surfaces are extended or trimmed appropriately. A positive distance results in a larger body; a negative distance in a smaller body.

Create Body Offset [From] Body <id_range> Distance <value>

Create Sheet Offset From Surface <id_list> Offset <val> [Surface <id_list> Offset <val>] [Surface <id_list> Offset <val> ...] [Preview]

This option is also available for limited cases for facet-based surfaces.

7. Sheet Extended from Surface: The following command creates a body offset from another body or set of surfaces at the specified distance. The new surfaces are extended or trimmed appropriately. A positive distance results in a larger body; a negative distance in a smaller body.

Create Sheet Extended From Surface <id_list> [Intersecting <entity_list>] [Extended {Percentage|Absolute} <val>] [Preview]

This command allows multiple surfaces to be extended at the same time. Optionally, you can give a list of bodies to intersect for this calculation. You can also extend the size of the surface by either a percentage distance or an absolute distance of the minimum area size. The plane can be previewed with the preview option. Figure 1 shows a set of surfaces being created using the extended absolute option.

Figure 1. Sheet created from extending multiple surfaces

8. Sweep Curve About Axis: Sweeps a curve or set of curves about a given axis through a specified angle. The axis is specified the same as in the Sweep Surface About Axis command. The steps, draft_angle, and draft_type options are the same as are described above. To create the solid, the make_solid option must be specified, otherwise a surface will be created, rather than a solid. If the rigid option is specified, then the curve or set of curves will remain oriented as originally oriented, rather than rotating about the axis.

Sweep Curve <curve_id_range> {Axis <xpoint ypoint zpoint xvector yvector zvector>|Xaxis|Yaxis|Zaxis} Angle <degrees> [Steps <Number_of_sweep_steps>] [Draft_angle <degrees>] [Draft_type <integer>] [Make_solid] [Rigid]

9. Stitch Surfaces Together: A body can be created from various surfaces that form a closed volume with command below. The geometry must be ACIS-type geometry (i.e. imported from IGES, STEP or fastq files) This option is also available for limited cases for facet-based surfaces.

Create {Body|Volume} Surface <surface_id_range> [HEAL|Noheal] [Keep] [Sheet]

The heal option will attempt to close small gaps in the surface; the noheal option disables this behavior. The keep option preserves the original surfaces.

All of the surfaces must form a closed water-tight volume for this command to succeed unless the sheet option is specified.

The sheet option allows for the creation of an open body. If the set of surfaces form a closed volume a sheet body is created instead of a volume.

In situations where the boundaries are not exactly within tolerance, the following command may be more effective:

10. Loft Surfaces Together: A body can be "lofted" between two surfaces to form a new body. Surfaces from solid bodies and sheet bodies may be used to create a loft body. In order to create the loft body, two surfaces coincident to the input surfaces are created. The loft body is extruded along the shortest path between the corresponding vertices that define the shapes of the two surfaces. If guide curves are used the loft body is extruded along the guide curves. This new body is solid. The surfaces used to create the loft body are unchanged.

Create {Body|Volume} Loft Surface <ids> [guide curve <id_list> [global_guides]] [Takeoff_factors <one value per surface in order>=.001] [Takeoff_vector Surface <id> {direction options}] [match vertex <ids>] [closed] [preview] [show_matching_curves]

Note:Source surface ids must be specified in lofting order.

Go to Location, Direction, and Axis Specification to see the direction command description.

The following options are available for lofting:

Lofting can be used to split a body in order to create a more structured mesh. Figure 2 below shows a single volume swept from a large paved surface. Figure 3 shows this same volume after surfaces defined on the source and target surfaces have been used to create a loft body. This original body was chopped with the loft body. The resulting two bodies were merged. The yellow volume was swept as the volume in Figure 2 was but the purple volume was submapped, producing a much more structured mesh overall.

Figure 2. Mesh before loft. Single swept volume with a large paved face.

Figure 3. Mesh after loft. The yellow volume is paved and the purple volume is submapped.

11. Thicken Surfaces: A surface body can be thickened to create a volume body. The surface can be thickened in both directions using the "both" keyword, thickened in the direction of surface normal using a positive depth, or thickened in the opposite direction using a negative depth. To thicken multiple surfaces, all surface normals must be consistent.

Thicken [Volume|BODY] <id> Depth <depth> [Both]

12. Sweeping a Surface to a Plane: Sweeps a surface normal to a plane and towards the plane until the swept surface reaches the plane. See plane options for ways to describe a plane.

Sweep surface <id> target plane <options>

13. Sweep Surface along a Direction: Sweep a surface along a direction to create a volume. See direction options for ways to specify a direction.

Sweep Surface <surface_id_range> Direction (options) [switchside] [draft_angle <degrees>] [draft_type <integer>] [rigid] [anchor_entity] [include_mesh] [keep] [merge]

Surface extruded along -X direction without 'include_mesh' option

14. Sweep Surface along Helix: Sweep a surface along a helix, where the helix is defined by an axis, thread_distance (distance between turns in axis direction), axis, and handedness (right_handed or left_handed.

Sweep {Surface|Curve} <id_range> Helix {axis <xpoint ypoint zpoint xvector yvector zvector> | xaxis | yaxis | zaxis} thread_distance <val> angle <val> [RIGHT_HANDED|left_handed] [anchor_entity] [include_mesh] [keep] [merge]

*** Specifying multiple Surfaces that belong to the same Body can cause the creation of invalid Bodies and is discouraged. ***

axis = axis about which to create the sweep

thread_distance = distance between each 360 degree segment of the helix

angle = number of degrees in rotation of the helix

handedness = right-handed or left- handed threads

**Examples:**

Example 1 (json):
```json
Stitch {Body|Volume} <id_range> 
 
 
 [tolerance <value>] [no_tighten_gaps]
```

---

## CUBIT Geometry Formats

**URL:** https://coreform.com/cubit_help/geometry/model_definitions/model_definitions.htm

**Contents:**
- CUBIT Geometry Formats
- Setting the Geometry Kernel
- Terms
- Topology
  - Bodies and Volumes
  - Non-Manifold Topology
- Bounding Box Calculations

The geometry kernel can be switched between ACIS and Mesh-Based Geometry from the command line using the following command:

Set Geometry Engine {Acis|Facet}

The geometry engine will automatically be set when importing a model.

Before describing the functionality in CUBIT for viewing and modifying solid geometry, it is useful to give a precise definition of terms used to describe geometry in CUBIT. In this manual, the terms topology and geometry are both used to describe parts of the geometric model. The definitions of these terms are:

Topology: the manner in which geometric entities are connected within a solid model; topological entities in CUBIT include vertices, curves, surfaces, volumes and bodies.

Geometry: the definition of where a topological entity lies in space. For example, a curve may be represented by a straight line, a quadratic curve, or a b-spline. Thus, an element of topology (vertex, curve, etc.) can have one of several different geometric representations.

Within CUBIT, the topological entities consist of vertices, curves, surfaces, volumes, and bodies. Each topological entity has a corresponding dimension, representing the number of free parameters required to define that piece of topology. Each topological entity is bounded by one or more topological entities of lower dimension. For example, a surface is bounded by one or more curves, each of which is bounded by one or two vertices.

A CUBIT Body is defined as a collection of other pieces of topology, including curves, surfaces and volumes. The use of Body is not required, and is in fact deprecated in favor of using Volume. Bodies may still be used for grouping volumes, but it is suggested to use Groups instead.

Although a Body may contain groups of Surfaces or Volumes, for most practical purposes within the CUBIT environment, a single Volume or Surface will belong to a single Body. For typical three-dimensional models, this means that there should be one Body for every Volume in the model, where the default Body ID is the same as the Volume ID. For this reason, in many instances the term Volume and Body are used interchangeably, although it is more consistent to always refer to Volumes and Volume IDs, and only use Bodies when absolutely necessary.

In many applications, the geometry consists of an assembly of individual parts, which together represent a functioning component. These parts often have mating surfaces, and for typical analyses these surfaces should be joined into a single surface. This results in a mesh on that surface which is shared by the volume meshes on either side of the shared surface. This configuration of geometry is loosely referred to as non-manifold topology.

Bounding box calculations are used for many routines and subroutines in Cubit. These calculations are done using a faceted representation by default. To use the default modeling engine for more accurate (and longer) calculations change the Facet Bbox setting.

Set Facet BBox [ON|Off]

There are also various settings to control the accuracy of bounding box calculations based on point lists.

Set Tight [[Bounding] [Box] [{Surface|Curve|Vertex} {on|off}]]

If surfaces are used, surface facet points will be included in the point list used to calculate the tight bounding box. This will include vertices and points on the curves. This is the default implementation.

If curves are used, curve tesselation points will be included in the point list used to calculate the tight bounding box. This includes the vertices on the ends of the curves. One use for this is to find a more accurate tight bounding box, since curve tessellations are typically more fine than surface tessellations. However, in practice, it is recommended to just use surface tessellations. One special case is if the user sends in a list of curves as the criteria for the tight bounding box, the curve tessellations are always used, even if this parameter is false.

If vertices are used, vertex points will be included in the point list used to calculate the tight bounding box. In extremely large models, it could be advantageous to just use vertices. So the user would turn off both the surface and curve flags. One special case is if the user sends in a list of curves as the criteria for the tight bounding box, the curve tessellations are always used, even if the curve parameter is false and this parameter is true.

---

## Debugging Geometry

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/debugging_geometry.htm

**Contents:**
- Debugging Geometry

The following command checks for inconsistencies in the CUBIT topological model, by checking the specified entities and all child topology and/or comparing to solid model topology:

Geomdebug Validate [compare] <entity_list>

This command checks for:

Geomdebug Vertex <vertex_id>

Geomdebug Curve <curve_id>

Geomdebug Surface <surface_id>

Geomdebug body <body_id>

Geomdebug Containment {Curve | Surface} <id> {Location (options) | Node <id_list>}

The following command prints info about GeometryEntities owned by specified entity:

Geomdebug Geometry <entity_list> [interval <n>] [index <n>] [TEXT] [GRAPHIC] [attributes]

The following command lists (TopologyBridge) topology for specified entity:

Geomdebug solidmodel <entity_list> [index <n>] [depth<n>|up<n>|down<n>]

The following command lists GroupingEntities.

Geomdebug GPE <entity_list>

---

## Defining PARAMS for NASTRAN

**URL:** https://coreform.com/cubit_help/finite_element_model/export/defining_params_for_nastran.htm

**Contents:**
- Defining PARAMS for NASTRAN

List Nastran Exporter Params

Set Nastran Exporter Params Add '<param_string>'

Set Nastran Exporter Params Remove '<param_string>'

Set Nastran Exporter Params Clear

Nastran uses “PARAMS” to define additional instructions and settings in its Bulk Data file. Any string can be defined as a Nastran Exporter Param, and it will be exported to the Nastran file as “PARAM, <string>”.

---

## Defining the Geometric Model

**URL:** https://coreform.com/cubit_help/item/importing.htm

**Contents:**
- Defining the Geometric Model

Various methods may be used to define a geometric model. In most cases, a solid model is created in a commercial CAD tool such as Pro/Engineer or Solidworks. It can also be generated natively within Cubit using geometry commands. One of the most time consuming tasks in developing an analysis model is in dealing with geometric anomalies. Carefully considering how the model is constructed and what format the model will be defined in can eliminate many potential problems downstream in the model creation workflow. The following describes the various solutions for defining geometry within Cubit along with their pros and cons:

Cubit can use one of three different commercial geometry representations, ACIS (.sat, .sab), Pro/E (.g) or Catia (.cat). It may also use a facetted format (MBG) that is developed in-house at Sandia. When a model of any of these formats is imported, Cubit uses the appropriate third party geometry kernel to directly manage and evaluate the geometry. Since the geometry is considered “native” when any of these formats is used, no translation step is required.

Since commercial solid modelers do not necessarily agree on formats and representations, using a translation process to convert a non-native format to a native format, can introduce errors in the geometry. While this in itself may not be a show-stopper, it can frequently add hours to an otherwise simple process while the user is forced to clean up dirty geometry. Neutral formats such as STEP and IGES are common in the CAE industry. They can often be an ideal solution for representing the analysis solid model. In Cubit, when importing a neutral format, it is automatically translated to the ACIS format. The user should be careful however in selecting these formats as commercial solid modeling engines frequently interpret standard specifications for these formats in different ways sometimes resulting in unusual results. Wherever possible a native format should be used.

Native geometry kernels provide the most accurate way for transferring data between solid-model based applications. Since these geometry kernels must be licensed and incorporated into the Cubit distribution separately, one drawback is the additional licensing and cost for maintaining these kernels. Cubit is currently able to provide licenses for ACIS and Pro/E kernels for government and academic use. Additional licensing arrangements may be required for Catia or for any commercial use.

Creating your own geometry

Cubit offers a wide variety of tools for creating geometry natively. The advantage to this is the ability to control the geometry creation process without the need for another CAD tool. Although Cubit is not designed to be a CAD tool it does provide many tools for both bottom-up and primitive creation.

Bottom-up creation refers to the process of building geometry from its basic components starting with vertices, curves, surfaces and then volumes. This process can be somewhat tedious, but is often useful for generating auxiliary geometry once a CAD model has been imported.

Primitive creation refers to the various operations for generating geometric primitives such as bricks, spheres, cylinders and cones. Once defined, operations for repositioning the objects and performing Boolean operations between them may be used. Relatively complex models may be generated using this approach.

One advantage to generating your own geometry within Cubit is the ability to parameterize the construction of the model. Cubit utilizes a rich command language that can be stored as a script or journal file. Parameters representing dimensions of objects may be defined in the script and conveniently adjusted to update the geometry representation. For more ambitious users, Cubit also has the ability to interpret python scripts, allowing a high degree of customization that can employ the full capability of the python scripting language.

It should be noted that when using Cubit, commands are automatically echoed to an external temporary journal file on disk and to the history window. Observing these commands is a good way to become familiar with Cubit’s internal command language. Copying and pasting selected commands to a text editor is an ideal method for building a parameterized journal file. Journal files may be built up and played back to reproduce the entire process of building an analysis model.

A CUB file is Cubit’s database file. You may want to think of it as a snap-shot of the current state of the model. While journal files record the process for creating the model, a CUB file stores only the end state. It can include both geometry in its native format and any mesh information as well as attributes and boundary condition information. Restoring a CUB file will write over any existing data you currently have defined.

---

## Deleting Virtual Geometry

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/deleting_virtual_geometry.htm

**Contents:**
- Deleting Virtual Geometry
- Removing Virtual Geometry
- Using The Delete Command With Composites
- Using the Delete Command With Partitions

The following command removes all lower-order virtual geometry from the specified entities.

Virtual Remove <entity_list>

virtual remove surface 5

Removes all composite and partition curves from surface 5.

virtual remove body all

Remove all virtual geometry from all bodies.

For removing individual virtual entities, see the sections of the documentation for each type of virtual entity:

If the general delete command is invoked for a composite surface, the composite surface will be removed, and the original surfaces used to define the composite will be restored to the model. The defining surfaces are NOT also deleted. As with any other non-virtual surfaces, the delete command will fail if the composite has a parent volume.

To delete composite surfaces with a parent volume, the composite delete command can be used. The behavior is analogous for composite curves.

If the delete command is used on a volume containing a composite surface or curve, or on a surface containing a composite curve, the entire volume or surface will be deleted, including the original entities used to define the composite, as those entities are also children of the entity being deleted.

It is recommended that the delete command not be used with partitions, as it may break subsequent usage of the merge and delete forms of the partition command for other partitions of the same real geometry entity. However, if the delete command is used for partitions, the behavior is to delete the specified partition, and when the last partition of the real geometry is deleted, to restore the original geometry.

The delete command can also be used on parents of partitions. For example, a volume containing partitioned surfaces, or a surface containing partitioned curves can be deleted. In this case, the specified entity will be deleted along with all of its children, including the partition entities, and the original entities that were partitioned.

---

## Entity IDs

**URL:** https://coreform.com/cubit_help/geometry/attributes/entity_ids.htm

**Contents:**
- Entity IDs
- Element Ids
- Gaps in ID space
- Renumbering IDs
- Volume ID

Topological entities (including groups) are assigned integer identification numbers or ids in CUBIT in ascending order, starting with 1 (one). Each new entity created within CUBIT receives a unique id within the topological entity type. This id can be used for specifying the entity in CUBIT commands, for example "draw volume 3".

There is a separate id space for each type of topological entity. For example, all mesh nodes are given ids from 1 to n, where n is an integer greater than or equal to the number of nodes in the model. Likewise, all hexahedra are given ids from 1 to m, where m is an integer greater than or equal to the number of hexahedra in the model.

Each mesh entity (hex, tet, face, tri, edge, node, etc.) may also have a Global Element ID from an id space which is used for all mesh entities. A mesh entity is only assigned a Global Element ID if it is in a block, and is the global id that will be assigned to the element during Exodus export. The Global Element ID provides a single id space across all the different element types.

After working with a model for some time, various operations will cause gaps to be left in the numbering of the geometric & mesh entities. The compress ids commands can be used to eliminate these gaps:

Compress [ids] [all] [Retainmax] [Sort]

Compress [Ids] [All] {Group|Body|Volume|Surface|Curve|Vertex|Element|Hex|Tet|Face|Edge|Node} [Retainmax]

Typing compress with no options or compress all will compress the ids of all entities; otherwise, the entity type for which ids should be compressed can be specified. The retainmax argument will retain the maximum id for each entity type, so that entities created subsequent to this command will receive ids greater than that value. If the sort qualifier is included, the new id of each entity will be determined by its size and location. Small entities are given a lower id than large entities. Entities that are the same size are sorted by their location, with lower x coordinate, then y, then z leading to a lower id. For example, two vertices are always the same size, so they are sorted based on the lowest x coordinate. If they are equal, then lowest y coordinate, etc. If two entities are found to have the same size and location, they are sorted according to their previous ids. This option can be used to restore ids in translated models in a manner which leads to more persistence than purely random id assignment.

The renumber command can be used to change the id numbers assigned to meshed entities.

Renumber {Node|Edge|Tri|Face|Hex|Tet|Wedge|Element} <id_range> Start_id <id> [Uniqueids]

Any valid range specification can be used to specify the source ids. There is no requirement that the ids being renumbered are consecutively numbered. The new id numbers will be consecutive beginning at the specified start id. For the command to be successful there can be no existing ids within the effective range of the start id. If the resultant destination range is not free of id numbers, the command will fail with an appropriate error.

Using the uniqueids keyword will result in the elements to be renumbered such that no element shares the same ID.

For convenience, all elements and nodes in a block can be renumbered with a single command:

Renumber block <id_range> [node_start_id <id>] [elem_start_id <id>] [localids]

By default, the Global Element ID is renumbered with the renumber block command. If localids is specified, the hex, tet, face, tri, or edge id is renumbered instead.

The volume id command is used to renumber a single volume.

Volume <old_id> Id <new_id>

This command replaces the volume's old_id with the new_id if no other is using the new_id number. Entity renaming only works for volumes; it does not work for nodes, curves or surfaces.

---

## Entity Measurement

**URL:** https://coreform.com/cubit_help/geometry/measuring_btw_entities.htm

**Contents:**
- Entity Measurement
- Measure Between
- Measure Small
- Measure Angle
- Measure Void
- Measure Volume
- Measure Surface

To output various properties of entities, the following Measure command options are available.

Measure Between { { Vertex|Curve|Surface |Volume|Node} <id1> | Location <options> | Plane <options> | Axis <options> } With { {Vertex|Curve|Surface|Volume|Node} <id2> | Location <options> | Plane <options> | Axis <options> }

Measure Between {Surface|Curve} <id1 > [Surface|Curve] <id2> [Node]

Measure Between {Vertex|Curve|Surface|Volume|Node|Edge|Face|Tri|Hex|Tet} <id1> With {Vertex|Curve|Surface|Volume|Node|Edge|Face|Tri|Hex|Tet} <id2>

The Measure Between command outputs the distance from one entity, location, plane, or axis to the next. The two entities in the command should be separated by the word "with". The result will always be the minimum distance between entities. For example, measuring between two spheres will output the minimum distance between them, not the distance between centroids. The example shown below will output the minimum distance between vertex 1 and surface 2.

measure between vertex 1 surface 2

The second form of the command is just for surfaces or curves and contains the Node argument. This argument attempts to measure between corresponding nodes on a pair of surfaces or curves. The command tries to determine a one-to-one mapping of nodes between the pair. It returns the greatest distance between any two nodal pairs, least distance between any two nodal pairs, and average distance between all of the nodal pairs. The mapping algorithm works best on surfaces if they are parallel.

The last form of the command measures between any geometry or mesh entities. The measurement to the mesh entities is to their center (i.e. the averaged vector location of all of the nodes belonging to the mesh entity).

With 2 entities selected in the graphics window, the user can right click one of the entities and measure the distance between the entities.

Measure Small {Length|Area|Volume|All} {Body|Surface} <id_list>

The Measure Small command locates all of the lengths, areas, or volumes smaller than the Measure Small Tolerance setting. Entities meeting the small tolerance criteria are listed in the output window and typically highlighted in the view port. The following two commands set the small tolerance to 0.1 and output all of the curves within body 1 with lengths at or below the small tolerance.

set measure small tolerance 0.1

measure small length body 1

Measure Angle { Direction <options> | Plane <options> | Axis <options> } With { Direction <options> | Plane <options> | Axis <options> }

The Measure Angle command displays the interior angle between the two entered entities. When a plane and a direction are specified, the angle between the direction vector and its projection into the plane is displayed. The measured angle represents the distance between the orientations of entities, and does not require the entities to intersect. Angles of model features can be measured by using the various options associated with the Direction, Planes, and Axis commands.

measure angle direction tangent curve 1 with plane surf 1

Measure Void [Face | Tri] <range>[No_Checks]

The Measure Void command takes a closed list of quadrilaterals or triangles and calculates the volume of the internal region defined by the given list of elements. This command assumes that the normals on the given elements are consistently ordered. If the normals are pointing away from the interior of the void, the reported volume may be negative. This command will check to ensure that the given elements do form a closed, manifold shell, otherwise an error is reported. Common uses will be to calculate the volume of an internal void for use in determining bulk element properties for a thermal analysis.

Rather than issuing an error, the no_checks option does not check for closure of the faces and will compute a void volume regardless of their watertightness. This is useful if faces are all touching, but may not have complete topological closure.

Measure Volume <range> [Overlap | Shell]

The Measure Volume command prints summary information about the specified volumes and surfaces of these volumes, such as average volume, minimum volume, angles, average surface area, etc. If the shell option is specified information about the shells of the volumes is additionally printed. The overlap option does not print any summary information, but only reports pairs of intersecting volumes.

Measure Surface <range>

The Measure Surface command prints summary information about the specified surfaces and curves of these surfaces, such as average area, minimum area, angles, minimum curve length, etc.

---

## Entity Names

**URL:** https://coreform.com/cubit_help/geometry/attributes/entity_names.htm

**Contents:**
- Entity Names
- Case-Insensitive Names
- Valid and Invalid Names
- Reconciling Duplicate Names
- Automatic Name Creation
- Automatic Name Creation
- Applying Namespaces to Entities
- Naming Merged Entities

By default, geometric entities in CUBIT are referenced using an entity type (e.g. Surface, Volume) and an id, for example "draw surface 1". However, geometric entities can also be assigned names, to simplify working with specific entities. Once a name is assigned to an entity, that name can be used in any CUBIT command in place of the entity type and number. For example, if surface 1 were named 'mysurf1', the command above would be equivalent to "draw mysurf1". Also, since entity names are saved with the geometry, this also provides a means for persistent identifiers for geometric entities. Names can be added or removed using the following commands.

{Group|Body|Volume|Surface|Curve|Vertex} {Name | Rename} {`<entity_name>'| Default}

{Group|Body|Volume|Surface|Curve|Vertex} Remove Name {`<entity_name>'| All | Default}

The name of each topological entity appears in the output of the List command. In addition, topological entities can be labeled with their names (see label command). A list of all names currently assigned and their corresponding entity type and id (optionally filtered by entity type) can be obtained with the command

List Names [{Group|Body|Volume|Surface|Curve|Vertex|All}]

Entity names in CUBIT are case-insensitive. This means that there is no difference between the name 'mysurf1' and MySurf1'. The case of names will be preserved as assigned. For example, a volume named 'MyVolume' will display the name 'MyVolume' but can be referenced by any case version of the name, 'MYVOLUME', 'mYvOlume', etc. Case-sensitivity can be toggled on/off with the command:

[Set] Case Sensitive Names [on|OFF]

Although any string may be used as an entity name, only valid names may be used directly in commands. A name is valid if it begins with a letter or underscore ("_"), followed by any combination of zero or more letters, digits, or the characters ".", "_", ":", or "@". If an attempt is made to assign an invalid name to an entity, CUBIT will generate a valid version of the invalid name by replacing invalid characters with an underscore. Then both the valid and invalid versions of the name are assigned to the entity. For example, assigning the name "123#" to a volume will result in the volume having two names, "123#" and "_23_". The valid name can be used directly in commands (mesh _23_), while the invalid name can only be referenced using a longer, less direct syntax (mesh volume with name "123#").

When an attempt is made to assign the same name to two different entities, a suffix is added to the name of the second entity to make it unique. The suffix consists of the "@" character followed by one or more letters or numbers. For example, the following commands will result in volumes 1 to 3 having the names "hinge", "hinge@A", and "hinge@B", respectively:

volume 1 name "hinge" volume 2 name "hinge" volume 3 name "hinge"

To prevent this automatic "fixing" of names, the Fix Duplicate Names flag may be switched to off. If the user attempts to assign a duplicate name while the flag is set to off, the name will remain unchanged.

Set Fix Duplicate Names [ON|Off]

CUBIT provides an option for automatically assigning names to entities upon entity creation. This option is controlled with the command:

Set Default Names {On|OFF}

When this option is on, entities are assigned default names consisting of a geometry type concatenated with the entity id, for example 'cur1', 'surf26', or 'vol62'.

CUBIT automatically propagates names through webcuts. If an entity that has been assigned the name "Gear" is split through webcuts, the resulting bodies are named "Gear" and "Gear@A". Try the following example.

br x 10 volume 1 name "Cube" webcut volume 1 xplane webcut volume 1 2 yplane webcut volume 1 2 3 4 zplane label volume name

Figure 1. Name Propagation through Webcuts

You can operate on these propagated names using wildcards such as:

The namespace command adds options to prepend entity names with a namespace using "::" as a separator. The following namespace commands are available:

The namespace on the top of the stack is prepended if an entity has a n existing name. All newly created entities will have the namespace applied. This is especially useful for tracking newly created entities in a webcut. For example,

brick x 1 volume 1 name 'part' namespace push 'left' webcut volume 1 plane xplane

The new volume 2 will be named left::part.

If the process is continued as follows:

namespace push 'top' webcut vol all plane yplane

The two newly created volumes will be named top::part and top::left::part respectively. If a user wants to determine the ids of the newly created objects they can use a command such as

list volume with name "top*" ids

Geometry that has duplicate names will continue to be suffixed with an '@' and characters as previously.

set default names on brick x 10 volume 1 name 'hole' namespace push 'hole' cylinder radius 2 z 12 # named hole::vol2 subtract volume 1 from volume 2 list surface with first_name "hole*" # the hole surface is named hole::sur7

Naming Merged Entities When entities that have the same base name, such as "platform" and "platform@A", are merged, the resulting entities is assigned both names. The set merge base names on command tells Cubit that in this situation, it should merge the names too. The command syntax is: Set Merge Base Names [On|OFF] For example: brick x 10 vol 1 copy move 10 surf 6 name 'platform' surf 10 name 'platform' Surface 10 actually is named platform@A, since we don't want duplicate names merge all list surf 6 You see that surface 6 has both 'platform' and 'platform@A' as names. Now, for the contrasting example brick x 10 vol 1 copy move 10 surf 6 name 'platform' surf 10 name 'platform' set merge base names on merge all list surf 6 You see that surface 6 has only 'platform' as its name.

When entities that have the same base name, such as "platform" and "platform@A", are merged, the resulting entities is assigned both names. The set merge base names on command tells Cubit that in this situation, it should merge the names too. The command syntax is:

Set Merge Base Names [On|OFF]

brick x 10 vol 1 copy move 10 surf 6 name 'platform' surf 10 name 'platform'

Surface 10 actually is named platform@A, since we don't want duplicate names

merge all list surf 6

You see that surface 6 has both 'platform' and 'platform@A' as names. Now, for the contrasting example

brick x 10 vol 1 copy move 10 surf 6 name 'platform' surf 10 name 'platform' set merge base names on merge all list surf 6

You see that surface 6 has only 'platform' as its name.

---

## Examining Merged Entities

**URL:** https://coreform.com/cubit_help/geometry/imprint_merge/examining_merged_entities.htm

**Contents:**
- Examining Merged Entities

There are several mechanisms for examining which entities have been merged. The most useful mechanism is assigning all merged or unmerged entities of a specified type to a group, and examining that group graphically. This process can be used to examine the outer shell of an assembly of volumes, for example to verify if all interior surfaces have been merged. To put all the merged entities of a given type into a specified group, use the command:

Group {<`name'>|<id>} add [Surface | Curve | Vertex] with Is_merged

To put all the unmerged entities of a given type into a specified group, use the command:

Group {<`name'>|<id>} add [Surface | Curve | Vertex] with Is_merged=0

Entities can also be labeled in the graphics according to the state of their merge flag. See the Preventing geometry from merging section for information on controlling the merge flag. To turn merge labeling on for a specified entity type, use the command

Label {Vertex | Curve | Surface} Merge

---

## Example 7. Using virtual geometry in geometry decomposition

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/example07.htm

**Contents:**
- Example 7. Using virtual geometry in geometry decomposition
- Suggested webcuts
- Final mesh

Virtual geometry is used to change the properties of mesh without changing the underlying geometry. The next example uses virtual geometry to remove unwanted sliver curves, and to create a sweepable volume. The composite curve function is used to combine sliver curves that are created from webcutting a slightly curved surface. Then the partition surface command is used to create additional partitions on a surface to ensure sweepability.

CUBIT> webcut volume 1 sweep surface 2 vector 0 0 -1 through_all

CUBIT> webcut volume 3 sweep surface 108 vector 0 0 -1 through_all

CUBIT> webcut volume 3 sweep surface 13 vector 0 0 -1 through_all

CUBIT> webcut volume 3 sweep surface 28 vector 0 0 -1 through_all

CUBIT> webcut volume 3 sweep surface 74 vector 0 0 -1 through_all

CUBIT> webcut volume 3 with sheet extended from surface 197

CUBIT> webcut volume 8 with sheet extended from surface 224

CUBIT> webcut volume 11 10 12 9 with plane surface 28

CUBIT> webcut volume 3 with plane normal to curve 116 fraction 0.5

CUBIT> webcut volume 3 17 with plane normal to curve 835 close_to vertex 487

CUBIT> webcut volume 18 19 with sheet extended from surface 376

CUBIT> webcut volume 3 17 with sheet extended from surface 378

CUBIT> webcut volume 8 with sheet extended from surface 73

CUBIT> webcut volume 8 with sheet extended from surface 72

CUBIT> webcut volume 8 with sheet extended from surface 133

CUBIT> webcut volume 8 with sheet extended from surface 71

CUBIT> webcut volume 8 with plane vertex 709 vertex 713 vertex 702

CUBIT> unite volume 36 45

CUBIT> unite volume 37 43

CUBIT> unite volume 35 44

CUBIT> unite volume 39 42

CUBIT> webcut volume 29 with plane vertex 81 vertex 93 vertex 154

CUBIT> unite volume 33 36 50 11

CUBIT> unite volume 10 49 37 31

CUBIT> unite volume 12 52 35 34

CUBIT> unite volume 9 51 39 32

CUBIT> unite volume 9 22

CUBIT> unite volume 12 23

CUBIT> unite volume 20 33

CUBIT> unite volume 21 10

CUBIT> webcut volume 12 with plane vertex 86 vertex 71 vertex 76 CUBIT> webcut volume 53 with plane vertex 738 vertex 87 vertex 741 CUBIT> webcut volume 12 with plane vertex 72 vertex 85 vertex 74 CUBIT> webcut volume 55 with plane vertex 754 vertex 205 vertex 208 CUBIT> webcut volume 12 sweep surface 731 along curve 1073 through_all CUBIT> unite volume 53 57 56 CUBIT> unite volume 54 12 55

CUBIT> webcut volume 9 with plane vertex 99 vertex 101 vertex 103 CUBIT> webcut volume 58 with plane vertex 769 vertex 98 vertex 772 CUBIT> webcut volume 9 with plane vertex 106 vertex 104 vertex 100 CUBIT> webcut volume 60 with plane vertex 781 vertex 201 vertex 198 CUBIT> webcut volume 9 sweep surface 764 along curve 1078 through_all CUBIT> unite volume 58 62 60 CUBIT> unite volume 59 9 61

CUBIT> webcut volume 20 with plane vertex 140 vertex 138 vertex 135 CUBIT> webcut volume 63 with plane vertex 139 vertex 137 vertex 134 CUBIT> webcut volume 20 with plane vertex 141 vertex 800 vertex 796 CUBIT> webcut volume 64 with plane vertex 803 vertex 220 vertex 223 CUBIT> webcut volume 63 sweep surface 803 along curve 1238 through_all CUBIT> unite volume 20 67 66 CUBIT> unite volume 65 63 64

CUBIT> webcut volume 21 with plane vertex 165 vertex 163 vertex 160 CUBIT> webcut volume 68 with plane vertex 164 vertex 162 vertex 159 CUBIT> webcut volume 21 with plane vertex 825 vertex 169 vertex 822 CUBIT> webcut volume 69 with plane vertex 830 vertex 216 vertex 213 CUBIT> webcut volume 68 sweep surface 836 along curve 1069 through_all CUBIT> unite volume 21 72 69 CUBIT> unite volume 70 68 71

These are the steps to webcut each of the stiffeners into the configuration shown. It is repeated for each of the stiffeners. This is also the step which creates the sliver curves which must be composited out later.

CUBIT> webcut volume 70 65 59 54 with plane surface 2

CUBIT> unite volume 1 76 75 73 74

CUBIT> unite volume 28 47 46 41 48 38 8 30 29 40

CUBIT> webcut volume 28 with plane surface 870

CUBIT> webcut volume 28 77 with plane surface 871

CUBIT> webcut volume 28 77 with plane surface 878

CUBIT> webcut volume 28 77 with plane surface 879

CUBIT> webcut volume 1 81 2 82 with plane normal to curve 1849 fraction 0.5

CUBIT>webcut volume 19 18 with plane normal to curve 843 fraction 0.75

CUBIT> create curve vertex 1122 vertex 471 on surface 1134

CUBIT> webcut volume 19 sweep curve 2073 along curve 2042 through_all

CUBIT> webcut volume 18 with sheet extended from surface 1146

CUBIT> webcut volume 18 with sheet extended from surface 1135

CUBIT> unite volume 91 92

CUBIT> delete curve 2073

CUBIT> unite volume 89 18

CUBIT> unite volume 88 19

Composite small curves formed from webcuts

CUBIT> composite create curve 1456 1468 CUBIT> composite create curve 1459 1467 CUBIT> composite create curve 1499 1511 CUBIT> composite create curve 1502 1510 CUBIT> composite create curve 1371 1379 CUBIT> composite create curve 1370 1381 CUBIT> composite create curve 1423 1413 CUBIT> composite create curve 1422 1414 CUBIT> volume all scheme auto

Create the partitioned curves shown using existing vertices

CUBIT> partition create surface 1067 vertex 311 175 CUBIT> partition create surface 1067 vertex 174 312 CUBIT> partition create surface 1063 vertex 123 294 CUBIT> partition create surface 1251 vertex 170 226 CUBIT> partition create surface 1082 vertex 195 115 CUBIT> partition create surface 1082 vertex 242 116 CUBIT> partition create surface 1077 vertex 117 309 CUBIT> partition create surface 1255 vertex 118 310

Meshing order is significant in this case. Since meshing a volume will hard set the interval counts on curves and surfaces, you will need to make sure that all of the interval counts are the same on adjacent volumes. Usually the meshing algorithm can handle this interval matching, but sometimes it helps to mesh volumes in a certain order. In this case, the meshing order also significantly changes the quality in the resulting mesh.

CUBIT> reset volume all CUBIT> volume all scheme auto CUBIT> volume 81 scheme sweep source surface 979 target surface 1061 rotate off CUBIT> volume 81 sweep smooth auto CUBIT> volume 85 scheme sweep source surface 1061 target surface 889 rotate off CUBIT> volume 85 sweep smooth auto CUBIT> volume all size 0.1 CUBIT> curve 2125 2122 interval 12 CUBIT> mesh vol 5 6 7 13 14 15 16 (COLORED GREEN) CUBIT> mesh Volume 85 81 77 83 78 82 87 28 80 79 (COLORED RED) CUBIT> mesh vol 88 89 91 90 17 3 (COLORED YELLOW) CUBIT> mesh volume with not is_meshed (COLORED WHITE)

The final mesh is shown below.

---

## Exporting ABAQUS

**URL:** https://coreform.com/cubit_help/finite_element_model/export/exporting_abaqus.htm

**Contents:**
- Exporting ABAQUS

Mesh can be exported from CUBIT in the ABAQUS format. The command to export to ABAQUS is:

Export Abaqus <’filename’> [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [Group <id_list>] {[Instance Block <id_list> [Source_csys <id>] Target_csys <id_list>] | [Instance_per_block]} [partial] [Overwrite] [Everything]

The ABAQUS file written by CUBIT will contain a single part, or mulitple parts. Multiple parts can be defined by using the instance option. Additionally, a single block/part can be instanced multiple times by giving multiple target coordinate systems. A bolt mesh used several times is an example where one might want multiple instances. To instance a block, a source coordinate system and a target coordinate system (where the mesh will be translated and rotated to) need to be defined. If no source coordinate system is given in the command, the default (global) coordinate system is used. The default (global) coordinate system can be referenced specifcally using '0' for the id. The instance keyword can be used as many times as needed. For example, block 1 can be instanced 3 times using 2 defined coordinate systems and the global coordinate system using:

create coordinate frame origin location 2 0 0 tag 'R'

create coordinate frame origin location -2 0 0 tag 'R'

Export Abaqus "myfile.inp" Instance Block 1 Target_csys 0 1 2

To enable automatic instancing, with the global coordinate system, based on defined blocks, the Instance_per_block option can be used.

Materials are supported with ABAQUS export as well. See documentation on materials for more information.

create material "Steel-200" property_group "CUBIT-ABAQUS"

modify material "Steel-200" scalar_properties "DENSITY" 7.8240

block 1 add material "Steel-200"

Additionally, Groups may be used to define additional node and element sets. For example:

group 'set-material-statistic-200' add tet in block 1 node in block 1

Note: By default, the Abaqus exporter writes 6 decimal places. The command "set Abaqus precision <n>" can be used to change the number of decimal places written.

---

## Exporting ACIS Files

**URL:** https://coreform.com/cubit_help/geometry/export/exporting_acis.htm

**Contents:**
- Exporting ACIS Files

Geometry can be exported from within CUBIT to the ACIS "sat" (ASCII) and "sab" (binary) formats. These formats can be used to exchange geometry between ACIS-compliant applications. The command used to export geometry is:

Export Acis [Debug] 'filename' [<geometry_entity_list>] [Binary|Ascii] [Current] [Overwrite]

The filename should be enclosed in single or double quotes. By convention, binary and ASCII ACIS files use the .sab and .sat filename extensions, respectively. If a geometry entity list is not specified, the entire ACIS model is exported. A geometry entity list is specified in the same format used for other CUBIT commands (See Entity Specification). Note that the model is saved as manifold geometry, and will have that representation when imported back into CUBIT (See Non-Manifold Topology and Geometry Merging.)

When exporting, the filename extension will determine the default file type, either ASCII or binary. A .sat extension will default to ASCII; a .sab extension will default to binary. If you use a different file extension you can specify the type with the [binary|ascii] option (with an unsupported extension exporting will default to ASCII but importing requires the type to be specified). Binary files can be significantly faster but are not guaranteed to be upward compatible nor cross-platform compatible (although testing has determined compatibility between NT and HP/UX).

In the GUI version, the current option will set the default filename for autosave (cntrl-S or File->Save (auto inc)) to the imported filename. Also, the filename is then set in the window titlebar.

When exporting with the "file overwrite" option on, the software will check to see if the file exists already, and if it does, exporting will fail in the command line version or ask to confirm the overwrite in the GUI version of CUBIT. The overwrite option will override this option and overwrite the file. The "file overwrite" option defaults to ON in the GUI version, OFF in the command line version.

When exporting, you can set the version of the Acis geometry. This allows backwards compatibility to previous versions of Cubit or other Acis-based applications. The command to change the Acis geometry engine version is:

Set Geometry Version [version_number]

where version_number can be one of the following:106, 107, 201, 300, 301, 401, 402, 403, 500, 501, 502, 503, 600, 601, 602, 603, 700, 701, 702, 703, 704, 705, 800, 1007, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2100, 2200, 2401, 2502. Note that you cannot set a version number that is higher than that of your current engine. For example, Cubit 6.0 was based on Acis 6.2, so you cannot set a geometry version of 700.

To retain any merging information during export of an ACIS file, set attribute on and set attribute off need to be used before and after the export acis command.

See also Importing ACIS Models.

---

## Exporting an Exodus II File

**URL:** https://coreform.com/cubit_help/finite_element_model/export/exporting_exodus2_file.htm

**Contents:**
- Exporting an Exodus II File
- Element and Node ID Maps
- Exporting a Parallel Mesh for pCAMAL
- Converting an Exodus II file to ASCII
- Controlling Exodus II Output Precision
- 64 bit Ids
- Large Exodus Format
- Exodus NetCDF4/HDF5 Format
- Exporting Geometry Association with the Exodus Mesh

After defining the element blocks, nodesets and sidesets for a model, the model can be written to the Exodus II file using the command:

Export [Genesis|Mesh] '<filename>' [dimension {2|3}] [Block <id_list>] [no_ids] [Qualityfile] [XML '<filename>'] [Overwrite]

Note: The ordering of options in this command is important. Misordering the options can cause the command to ignore some options.

The Genesis or Mesh arguments are optional and both indicate that an Exodus II format will be written. The filename can be any valid filename. Where a full path is not specified, the file will be written in the current working directory.

The dimension argument is also optional. Most element types have an inherent dimensionality associated with them. For example, a truss or beam element is inherently 2D while a hex or tetra element is 3D. Without this argument, only the x-y location of the nodal coordinates of 2D elements are written to the Exodus II file. Using the argument dimension 3 in this example permits the full 3D coordinates to be written.

The optional Block argument may also be added to the Export command. Without this argument all blocks defined in the current model will be exported to the Exodus II file. This argument permits the user to specify only a subset of all the blocks in the model. The <id_list> may be any valid set of integers corresponding to the block ids in the current model.

no_ids prevents the writing of node and element id maps in the Exodus file. This can be useful if users do not want Cubit ids in downstream workflows.

The Qualityfile option exports, in addition to the mesh, a text file containing a printout of the element quality using the 'Allmetrics' option. The name of this file is the base name of the mesh file (file extension removed) and "_quality.txt" added.

The XML optional argument may also be added to the Export command. When this argument is included and assembly data exists in the model, an XML file is written which describes the relationship between block IDs in the Exodus II file and parts in the assembly. See the Parts, Assemblies and Metadata section for details.

Element ID map and node ID map are always written to the Exodus II file. The IDs written to the node ID map are the node IDs used to refer to nodes at the Cubit command line. The IDs written to the element ID map are the Global Element IDs which are assigned to the hex, tet, quad, etc. when they are added to an element block. The node and element ID maps can be used when a particular element or node is refered to in a downstream application and the corresponding node or element in Cubit must be found. Some analysis and post-processing applications consider these maps to be optional, while others ignore the maps even if they are present. See the Exodus manual for more information on element and node ID maps.

Export Parallel "<filename>" [Block <id_list>] [Overwrite] [Processor <number>]

The Export Parallel command is used to output an ExodusII file with the boundary mesh or shell for sweepable volumes that were meshed with set parallel meshing enabled. The options are the same as those for the "export genesis" command except for the addition of the processor option.

The processor option allows the user to specify the number of processors that will be used to mesh the volume with the pCAMAL option. This same option exists in the pCAMAL application and is more often used there since the number of available processors is known then rather than when the output file is created in Cubit.

If the processor option is given, Cubit attempts to balance the number of sweepable volumes to run on n processors by converting many-to-one sweeps to one-to-one sweeps, subdividing the sweep volume along its sweep direction, or partitioning the source surface of a one-to-one sweep if the number of source quads is much larger than the number of layers.

The Exodus II file format is binary. It is frequently necessary to view the contents of the Exodus II file as plain text. A publicly available tool known as ncdump can be used to view the contents of an Exodus II file. ncdump is part of the netCDF library and is currently available from Unidata at the following URL:

http://www.unidata.ucar.edu/

On a UNIX platform, typical use of the ncdump utility is:

ncdump filename.e > filename.txt

In this format, the ncdump utility will take the Exodus II file, filename.e, and dump the contents to an ASCII file filename.txt

Another option for converting between binary and ASCII formats of Exodus II files is a utility known as exotxt. Exotxt is part of the SEACAS tool suite. Contact the Sandia CUBIT development team for a copy of this utility.

By default, exodus files are written with double precision numbers. It may be useful to change this for large meshes to decrease output file size. This can be done using the following command:

Set Exodus Single Precision [On|Off]

This command toggles the Exodus output file between single precision (floats) and double precision.

The Set Exodus 64bit command enables 64 bit ids in the Exodus files. This may be useful when the file includes a large number of entities such that a 32 bit id can no longer represent distinct entities.

Set Exodus 64bit [on|OFF]

The Set Large Exodus command enables the large exodus file setting to create a model that can store individual datasets larger than 2 gigabytes. This modifies the internal storage used by ExodusII and also puts the underlying netcdf file into the "64-bit offset" mode.

Set Large Exodus [ON|Off]

The Set Exodus NetCDF command enables the exodus NetCDF4/HDF5 file setting to create a model that can store even larger files with unlimited dimensions. This modifies the internal storage used by ExodusII to an HDF5 based file. This setting overrides the Set Large Exodus setting.

Set Exodus NetCDF4 [On|OFF]

Optionally, you can also export the associated ACIS geometry and the correspondence between the mesh and the geometry by using the export m2g command.

---

## Exporting DAGMC Models

**URL:** https://coreform.com/cubit_help/finite_element_model/export/exporting_dagmc.htm

**Contents:**
- Exporting DAGMC Models
- Preparing a Model for DAGMC Export
- See Also

DAGMC (Direct Accelerated Geometry Monte Carlo) is an open-source toolkit for performing Monte Carlo radiation-transport simulations directly on CAD-based geometry. CUBIT can export a model to the MOAB-compatible .h5m file that DAGMC and the transport codes built on it (such as OpenMC and MCNP) consume.

The command used to export a DAGMC model is:

Export DAGMC '<filename>' [Overwrite]

Use the overwrite keyword to replace an existing file. The exporter writes the faceted (triangulated) surface mesh together with the geometric topology — vertices, curves, surfaces, and volumes — and the tags, surface senses, and group information that DAGMC requires, all in the HDF5-based .h5m format. Block names are recorded in the file decorated with the assigned material and its first few property values (for example mat:steel/ela:2.00e+11/poi:0.30); long names are truncated to the 31-character tag limit, with a warning when that happens.

A DAGMC model is a watertight surface mesh in which adjacent volumes share surfaces, so that particles can be tracked from one volume into the next. The typical preparation steps are:

imprint body all merge body all

Note: The command export cf_dagmc is a deprecated alias for export dagmc and will be removed in a future release. (Older tutorials may still refer to export cf_dagmc.)

---

## Exporting Facet Files

**URL:** https://coreform.com/cubit_help/geometry/export/exporting_facet.htm

**Contents:**
- Exporting Facet Files

Facet files may be exported directly, or by converting from an ACIS representation. The syntax for exporting facet files is:

Export Facets 'filename' <entity_list> [Overwrite]

The overwrite function allows you to overwrite an existing facet file.

STL facet files may be generated from geometry or from a triangle mesh. The syntax for exporting to the STL format is:

Export STL [ASCII|binary] 'filename' [<entity_list>] [tri <id_range>] [angle=15] [mesh|fast] [sidesets|sideset<ids>] [Overwrite]

The [entity_list] option is a list of geometric entities (bodies, volumes, or surfaces). By default, the graphics facets for the geometric entities will be written to the STL file. The [angle] keyword specifies the dihedral angle used during facet generation. By default, a "water-tight" set of graphics facets is exported for solid volumes. If a water-tight set of facets is not of interest to the user and performance is more important, the fast option can be used. It generates a faceting that does not take the extra step of ensuring water-tightness. To export the triangle mesh on the geometric entities, instead of the graphics facets, specify the [mesh] keyword. Note that STL export of quad meshes is not supported.

The [sidesets] or [sideset <ids>] options will export all or the specified sidesets respectively in your model as surface designation for any or all triangles in the file. If present, one sideset will be generated for each surface designation in the STL file. Following is an example surface designation in an STL file. It would appear following all triangles.

The id following the surface designation will be used as the sideset ID.

Alternatively, a list of mesh triangles can be specified for export. If neither geometry entities nor mesh are specified, all volumes and sheet bodies are written out.

**Examples:**

Example 1 (unknown):
```unknown
surface 1
          0 1 2 3 4 5 6 7 8 9
          10 11 12 13 14 15 16 17 18 19
          20 21 22 23
        endsurface 1
```

---

## Exporting Fluent Grid Files

**URL:** https://coreform.com/cubit_help/finite_element_model/export/exporting_fluent.htm

**Contents:**
- Exporting Fluent Grid Files

Export Fluent '<filename>' [Surface <id_list>|Volume <id_list>] [Overwrite]

The filename should be enclosed in either single or double quotes. By convention, the file extension .msh is applied to grid files. The extension should be included in the filename section. Other file extensions such as .cas may be used, but they cannot be guaranteed to be compatible with either GAMBIT or TGrid.

In order to guarantee that the grid file will be compatible with Fluent, all bodies must be merged (See Geometry Merging). Several types of Fluent boundary condition zones are now implemented in Cubit. They are:

Boundary condition zones created in two different ways. The first way involves user-defined mesh groups consisting only of quads (3D), triangles (3D), or element edges (2D) (See Geometry Groups). The second way involves sidesets. Specifying a boundary condition consists of selecting a user-defined mesh group or a sideset, or a surface. Selecting a surface automatically assigns the boundary condition to the sideset associated with that surface. The boundary condition type is specified and is either given a name or an id (See Using CFD Boundary Conditions). Groups or sidesets of mixed type (e.g. hexes and faces) will not be exported. All surfaces not set to one of the first seven boundary condition types are automatically set to type ‘wall’. The various parameters for each of the boundary condition types must be set within either Fluent or GAMBIT.

Cell zones are automatically created for 3D meshes containing blocks. Blocks must contain entire and continuous volumes in order to create a valid grid. In 2D models, the cell zones are created from sidesets containing only quads or tris. In order to create a valid grid, these sidesets must contain whole, continuous surfaces. All cell zones are by default set to type ‘fluid.’

If no entities are specified, the entire model is exported. In order to export selected entities, the types ‘volume’ and ‘surface’ can be specified. In 2D cases, use ‘surface’ while in the 3D case use ‘volume.’

---

## Exporting GDF Files

**URL:** https://coreform.com/cubit_help/finite_element_model/export/exporting_gdf_files.htm

**Contents:**
- Exporting GDF Files

The Geometric Data Format (GDF) is an export format used by WAMIT. The file format consists of quadrilateral and triangular elements.

Export GDF '<filename>' [entity_list] [Block <id_list>] [ulen <value=1.0>] [gravity <value=9.80665>] [isx <value=0>] [isy <value=0>] [Overwrite]

All elements to be exported should be part of a block. All blocks are exported unless otherwise specified in the command. The standard GDF parameters can be specified on export.

---

## Exporting Geometry

**URL:** https://coreform.com/cubit_help/geometry/export/geometry_export.htm

**Contents:**
- Exporting Geometry

Geometry can be exported from CUBIT in a variety of formats, including the ACIS ".sat" and ".sab" formats as well as in more portable exchange formats like STEP and IGES.

---

## Exporting IGES Files

**URL:** https://coreform.com/cubit_help/geometry/export/exporting_iges.htm

**Contents:**
- Exporting IGES Files

Export Iges 'filename' [<geometry_entity_list>] [Solid] [Logfile ['filename'] [Display]] [Overwrite]

As with ACIS file export, you can specify which individual entities to export. If unspecified, all ACIS entities are exported.

The logfile option is used to save information regarding the conversion to IGES format. This information saved to a file with the name specified by the user, or named 'iges_export.log' by default. When running the GUI version of CUBIT, the logfile can be displayed in a dialog window by using the display option.

The solid option allows solid volumes to be exported as Manifold Solid B-Rep Objects (MSBO). Without this option, the iges file is simply a collection of stand-alone surfaces.

The overwrite option works the same as with ACIS file export.

See Importing IGES Files for information on setting up the IGES import and export functionality.

Note that the IGES import and export functionality might not be available on all 64-bit platforms.

---

## Exporting Meshed Based Geometry Files (MBG)

**URL:** https://coreform.com/cubit_help/appendix/alpha/exporting_mbg_files.htm

**Contents:**
- Exporting Meshed Based Geometry Files (MBG)

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

CUBIT provides the capability to import a model composed of mesh based geometry. The command to import meshed based geometry is:

Export mbg ''<filename>"

MBG is created in Cubit when one meshes a volume or imputs the mesh from a previously meshed volume with the import mesh geometry command. Optionaly one may create geometry with the "set dev on" option.

In order to create, import and export MBG one needs to set the geometry engine to facet with the following command "set geom eng facet".

The following commands create a brick and export and import it as a MBG file:

set geometry engine facet

export mbg "brick.mbg" overwrite

import mbg "brick.mbg"

---

## Exporting SGM Files

**URL:** https://coreform.com/cubit_help/appendix/alpha/exporting_sgm_files.htm

**Contents:**
- Exporting SGM Files

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

SGM geometry in CUBIT can be exported to an SGM file:

Export SGM ''<filename>"

The SGM geometry in the current Cubit session will be written to the file. Specify the overwrite option to overwrite an existing file with the same name.

---

## Exporting STEP Files

**URL:** https://coreform.com/cubit_help/geometry/export/exporting_step.htm

**Contents:**
- Exporting STEP Files

CUBIT can export geometry to the STEP format, an emerging standard for storing geometry and other information. The STEP AP203 and STEP AP214 standards are supported. It is recommended to use AP214 for exchange of geometry information with CUBIT. The command used to export a STEP file is:

Export Step 'filename' [<geometry_entity_list>] [Logfile ['filename'] [Display]] [Overwrite]

As with ACIS file export, you can specify which individual entities to export. If unspecified, all ACIS entities are exported.

The logfile option is used to save information regarding the conversion to STEP format. This information saved to a file with the name specified by the user, or named 'step_export.log' by default. When running the GUI version of CUBIT, the logfile can be displayed in a dialog window by using the display option.

The overwrite option works the same as with ACIS file export.

If bodies, volumes, surfaces, curves, or vertices have names, they will be written into the STEP file.

See Importing STEP Files for information on setting up the STEP import and export functionality.

---

## Exporting the Finite Element Model

**URL:** https://coreform.com/cubit_help/finite_element_model/export/exporting_finite_element_model.htm

**Contents:**
- Exporting the Finite Element Model
- Supported element types
- Supported boundary conditions types

For information on exporting an Exodus File, see Exporting Exodus II Files. Custom translators are available to translate between the Exodus II format and a limited number of other analysis code formats. Contact the cubit development team for a current list of supported translator formats. For information on the GDF format, see Exporting GDF Files. The general syntax for the various exporters is as follows. The specific exporter commands are listed below.

Export {Abaqus [Explicit]* [Partial]* | CGNS | Nastran | Ideas | Patran | LSDyna | Fluent} <’filename’> [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [dimension {2|3}***] [Overwrite] [Everything] [NX]**

Export {Sierra | VRML} <'filename'> [Overwrite]

* Explicit and Partial keywords only available with Abaqus Exporter

** NX keyword only available with I-DEAS Exporter

***The dimension argument is also optional. Most element types have an inherent dimensionality associated with them. For example, a truss or beam element is inherently 2D while a hex or tetra element is 3D. Without this argument, only the x-y location of the nodal coordinates of 2D elements are written to the Exodus II file. Using the argument dimension 3, in this example, permits the full 3D coordinates to be written.

The Abaqus Exporter has a few additional keywords available. See the last paragraph below for an explanation of those keywords:

Export Abaqus <'filename'> [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [dimension {2|3}] [nodefile <'filename'>] [elementfile <'filename'>] [flat] [overwrite] [everything]

If no blocks are exported, Cubit will export all nodes and elements in the model. If one or more blocks are entered in the command, only those blocks will be exported. Similarly, if no BCSets are entered in the command, Cubit will export all boundary conditions as a single BCSet. If one or more BCSets are entered into the command, only those BCSets will be exported. Use the overwrite flag to overwrite an existing file.

By default, Cubit will reassign node and element IDs based on which block they are in. If the everything keyword is present, Cubit will export all nodes and elements in the model, whether they are in a block or not.

The I-DEAS Universal file can be read into Siemen’s NX application if the file is generated using the NX keyword. This is because extra information must be written to an I-DEAS Universal file in order for NX to be able to read it.

There are a few keywords specifically for the Abaqus exporter. Flat can be used if the user desires Cubit to write out the model as a "flat file." Abaqus refers to files a "flat files" when they do not use the *PART/*INSTANCE structure. All nodes and elements will be defined at the global level. The keywords elementfile and nodefile can be used to instruct Cubit to export the nodes and/or elements to a separate file.

If the Explicit keyword is used with Abaqus, Cubit will write an Abaqus Explicit deck. The one Explicit-only feature that Cubit supports is Fixed Mass Scaling.

If the Partial keyword is used with Abaqus, Cubit will write a partial Abaqus deck. Cubit will output the mesh as defined by the Abaqus keywords PART, NODE, ELEMENT, NSET, ELSET, and SURFACE. Everything else is ignored. Use the Abaqus keyword INCLUDE to include this file in a master Abaqus deck for analysis.

Specific Exporter Commands:

Export Abaqus [explicit] '<filename>' [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [group <id_list>] [instance block <id_list> [source_csys <id_list>] target_csys <id_list> [preview]] [dimension {2|3}] [overwrite] [everything] [partial]

Set Abaqus Precision <n=6>

Note: This command can be used to control the number of decimal places written to the Abaqus file.

Export CGNS '<filename>' [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [dimension {2|3}] [overwrite] [everything]

Export Nastran '<filename>' [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [dimension {2|3}] [overwrite] [everything]

Export Ideas '<filename>' [NX] [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [dimension {2|3}] [overwrite] [everything]

Export Patran '<filename>' [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [overwrite] [everything][dimension {2|3}]

Export Lsdyna '<filename>' [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [overwrite]

Export Fluent '<filename>' [Block <id_list>] [Sideset <id_list>] [Nodeset <id_list>] [BCSet <id_list>] [dimension {2|3}] [overwrite] [everything]

Note: The following command is for exporting mesh geometry, (.msh format.)

Export Fluent '<filename>' [Surface <id_list>|Volume <id_list>] [Overwrite]

Export Sierra <'filename'> [Overwrite]

Export VRML <'filename'> [Overwrite]

Export DAGMC <'filename'> [Overwrite]

Note: The DAGMC exporter writes a MOAB-compatible .h5m file for Monte Carlo radiation transport. See Exporting DAGMC Models.

Additional Information on building Cubit models for CFD

Defining PARAMS for NASTRAN

Exporting Solver-Specific Element Types

**Check to make sure the element's properties are correct after exporting

***Also exports lofting factor for shell elements (IDEAS)

† The element type will be HEX but the number of nodes will be the number of nodes in the pyramid.

*** Does not allow separate temperatures for top and bottom of shell elements. Values will be averaged.

---

## Export Mesh and Its Geometry Association

**URL:** https://coreform.com/cubit_help/finite_element_model/export/export_mesh_association.htm

**Contents:**
- Export Mesh and Its Geometry Association

Cubit offers the option to export a complete finite element mesh, along with its association to an ACIS geometry model. This is useful if a 3rd party application is going to be used to modify the mesh after exporting from Cubit, and you want the geometry available to project to during the modification operations. The command is:

Export m2g '<fileroot>' [{ACIS|mbg}] [overwrite]

The fileroot argument to this command is not a complete filename, rather, it is a full path and filename without the file extension. The export m2g command will write out:

The export m2g command can export either an ACIS (*.sat) file or an MBG file depending on the supported geometry types of the downstream 3rd party application in use. The default is to export an ACIS file.

An example usage of the export m2g command is the Sierra mesh_scale command. Sierra mesh_scale is a batch program which performs the same mesh scaling as can be performed in Cubit with the scale mesh command. When generating new nodes on the boundary of the mesh, Sierra mesh_scale projects the locations of the new nodes to the ACIS geometry model by leveraging the information exported by the export m2g command.

---

## Finding Surface Overlap

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/finding_surface_overlap.htm

**Contents:**
- Finding Surface Overlap
- Facetted Representation
- Find Overlap Settings

The surface overlap capability finds surfaces that overlap each other, with the capability to specify a distance and angle range between them. This is useful for debugging geometry imprinting and merging problems, as well as for finding gaps in large assembly models. Finding overlapping geometry is done using the command:

Find [Surface] Overlap [{Body|Surface|Volume} <id_list> [Filter_Sliver]

If a list of entities is not specified, all bodies in the model are checked. By default the command does not check the surfaces within a given body against each other; rather, it only checks surfaces between bodies. This can be overridden by inputting a surface list (i.e. find overlap surface all), or with a setting (see below).

The filter_sliver option will remove false positives from the list by weeding out sliver surfaces that have a merged curve between them. The following pictures is an example of a sliver surface.

Figure 1. Example of a sliver surface

If curves 27 and 29 are merged before you run the find overlapping surface checkthe user will get the two surfaces in the picture as an overlapping surface pair. However, if the filter_sliver keyword is used, Cubit will not find the two surfaces to be overlapping.

This command works entirely off of the facetted surface representation of the model (the facetted representation is what you see in a shaded view in the graphics). There are inherent advantages and disadvantages with this method. The biggest advantage is avoidance of closest-point calculations with NURBS based geometry, which tends to be slow. This method also eliminates possible problems with unhealed ACIS geometry. The disadvantage is working with a less accurate (i.e., facetted) representation of the geometry. To circumvent problems with this facetted geometry, various settings can be used to control the algorithm. For example, you might consider using a more accurate facetted representation of the model - see below.

Various settings are used to control the precision and handling of overlaps during the find overlap process. A listing of the settings that find overlap uses is printed using the command:

Find [Surface] Overlap Settings

These settings, and the commands used to control them, are described below.

Facet - Absolute/Angle - The angular tolerance indicates the maximum angle between normals of adjacent surface facets. The default angular tolerance is 15 - consider using a value of 5 . This will generate a more accurate facetted representation of the geometry for overlap detection. This can be particularly useful if the overlap command is not finding surface pairs as you would expect, particularly in "curvy" regions. Note however that the algorithm will run slower with more facets. The distance tolerance means the maximum actual distance between the generated facets and the surface. This value is by default ignored by the facetter - consider specifying a reasonable value here for more accurate results.

Gap - Minimum/Maximum - the algorithm will search for surfaces that are within a distance from the minimum to maximum specified. The default range is 0 to 0.01. Testing has shown this to be about right when searching for coincident surfaces. Gaps can be found by using a range such as 3.95 to 5.05.

Set Overlap {Minimum|Maximum} Gap <value>

Angle - Minimum/Maximum - the algorithm will search for surfaces that are within this angle range of each other. The default range is 0.0 to 5.0 degrees. Testing has shown that this range works well for most models. It is usually necessary to have a range up to 5.0 degrees even if you are looking for coincident surfaces because of the different types of faceting that can occur on curvy type surfaces. For example, for the case of a shaft in a hole, the facets of the shaft usually won't be coincident with the facets of the hole, but may be offset by a certain distance circumferentially with each other. The 5 degree max angle range will account for this. If you find that the algorithm is not finding coincident surfaces when it should, you can increase the upper range of this value. Note that this parameter is useful also for finding plates coming together at an angle.

Set Overlap {Minimum|Maximum} Angle <value>

Normal - this setting determines whether to search for surfaces whose normals point in the same direction as each other (same), away from each other (opposite) or either (any). The default is ANY, but it may be useful to limit this search to opposite, as this would be the usual case for most finds.

Set Overlap Normal {ANY|opposite|same}

Tolerance - two individual facets must overlap by more than this area for a match to be found. Consider the two cylindrical curves at the interface of the shaft and the block in Figure 2. Note that some of the facets actually overlap, even though the curves will analytically be coincident. You can filter out false matches by increasing the overlap tolerance area. The default value for this setting is 0.001.

Set Overlap Tolerance <value>

Figure 2. Possible false find due to overlap (tolerance will prevent finding match)

Group - the surface pairs found can optionally be placed into a group. The name of the group defaults to "overlap_surfaces".

Set Overlap Group {on|OFF}

List - by default the command lists out each overlapping pair - this can be turned off using the command:

Set Overlap List {ON|off}

Set Overlap Display {ON|off}

Body - by default the command will not search for overlapping pairs within bodies - only between different bodies. Turn this setting on to search for pairs within bodies. Note however that this will slow the algorithm down.

Imprint - If on, Cubit will imprint the overlapping surfaces that it finds together. This will often force imprints that just imprinting bodies together will miss. For each pair of overlapping surfaces, the containing body of one surface is imprinted with the individual curves of the other surface, until the resulting surfaces no longer overlap.

---

## Geometric Primitives

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/primitive_geometry/primitive_geometry.htm

**Contents:**
- Geometric Primitives
- General Notes

The geometric primitives supported within CUBIT are pre-defined templates of three-dimensional geometric shapes. Users can create specific instances of these shapes by providing values to the parameters associated with the chosen primitive. Primitives available in CUBIT include the brick, cylinder, torus, prism, frustum, pyramid, and sphere. Each primitive, along with the command used to generate it and the parameters associated with it, are described next. For some primitives, several options can be used to generate them, and are described as well.

The following Primitives can be generated with CUBIT:

---

## Geometry/Mesh Comparison Tool

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/geometry_mesh_comparison_tooll.htm

**Contents:**
- Geometry/Mesh Comparison Tool

The Geometry/Mesh Comparison Tool tries to find geometry and mesh that do not correspond. The typical use is to import a geometry file and then import a mesh file that is associated with the geometry. The comparison tool will locate mesh that does not correspond to the geometry. The tool will also show geometry that does map to any mesh.

The user selects the volumes for the comparison, then selects the mesh entities for the comparison. A default comparison tolerance value of 1e-6 will be used unless otherwise specified. No additional setup is required. Select the "Compare" button to generate results.

Unassociated entities will be displayed in one of two categories:

1) Mesh elements not associated with any volume

2) Partially meshed volumes

Clicking on the labels in the tree will cause the entities to be drawn in the graphics window. If "Draw Without Refreshing" is selected, the draws will be additive. If "Draw Without Refreshing" is not selected, the previous draw will be removed when the current drawn entities are shown.

The underlying Cubit command for the tool is the following:

Compare volume <id range> {block <id range> | hex <id range> | tet <id range> [tolerance <value>]

The command will create three types of groups that contain non-corresponding mesh and/or geometry. The group named "mesh_with_no_volume" contains hexes or tets that cannot be associated with any volume. The groups named "No_meshed_Volume_*" contain the curves of a volume (for display purposes) that is completely void of any hexes or tets. Lastly, the groups named "Partially_meshed_Volume_*" contain hexes or tets, faces or tris, and curves of volumes that could only be partially associated with mesh. The group is created with these entities so that the user can see the partially meshed regions of the volume.

---

## Geometry Accuracy

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/geometry_accuracy.htm

**Contents:**
- Geometry Accuracy
  - Detailed Discussion:

The accuracy setting of the ACIS solid model geometry can be controlled using the following command:

[set] Geometry Accuracy <value = 1e-6>

Some operations like imprinting can be more successful with a lower accuracy setting (i.e., 0.1 to 1e-5). However, it is not recommended to change this value. Be sure to set it back to 1e-6 before exporting the model or doing other operations as a higher setting can corrupt your geometry.

Most geometric modelers use double precision numbers for the coordinate values of a point in three-dimensional space. The maximum number of base ten digits that one can expect from a double precision number is 15. However, if one wants to work with the numbers, such as take their square root to find distances between points, then the precision is cut in half to 7. Moreover, if your numbers are not close to the origin, then you lose more precision for each order of magnitude that a point is away from (0,0,0). Hence, if you make a part with coordinate aligned analytics such as planes, sphere, cylinders, lines and circles, then you may expect tolerances to have 6 significant digits or with luck even more. However, once one introduces NURB curves, which are used to find piecewise polynomial approximations of intersections which are not lines, circles or conic sections, then one cuts the accuracy in half again to around three significant digits. In other words, the accuracy of a CAD model is a lot less than most people would expect.

In addition to tolerances in 3D geometric position, there are also tolerances in the parameter space of curves and surfaces, and there are tolerances in the derivatives of curves and surfaces. NURBs, or rational piecewise polynomials, may fail to even have derivatives. However, most CAD programs try to make sure that the first and second derivatives of their curves and surfaces exist at least on the interior of their domains. Hence, Gaussian integration and Romberg integration, which depend of the continuity of derivatives work but only up to the second derivative and only with low accuracy.

Changing the tolerance in ACIS to a number smaller than 1E-6 will not make parts read into ACIS more accurately. Making the ACIS tolerance a larger number might make some things work on low accuracy data. However, if you change the ACIS tolerance to a larger number, then you are using ACIS in a non-tested mode. It is almost always better to scale your part, or change the units that you are using, instead of changing the ACIS tolerance. In general, all parts in ACIS should be within 10,000 to the origin. CAD systems used to model larger things such as bridges, mines, and skyscrapers need to use even less accurate tolerances. Which is to say that one does not measure a long suspension bridge in microns.

To accommodate different tolerances and low accuracy approximations of curves from different CAD systems, ACIS measures the accuracy of each curve and vertex when it is read in and marks any curves that do not lie on their surfaces to 1E-6 as a tolerant curve, and any vertex that does not lie on its curves to 1E-6 as a tolerant vertex, and these tolerances are used internally in ACIS to make such things as Booleans work with low accuracy data. In general, expect parts that were not made with ACIS to have errors as large as 1E-3. To deal with parts that are very large, scaling them down, performing the operation in question and then scaling the results back up may help. Also moving things closer to the origin may help. ACIS is a unitless geometric modeler and the units that you use need to fit into these numerically sweet spots.

---

## Geometry Attributes

**URL:** https://coreform.com/cubit_help/geometry/attributes/geometry_attributes.htm

**Contents:**
- Geometry Attributes

Each geometric topological entity has specific information attached to it. These attributes specify aspects of the entity such as the color that entity is drawn in and the meshing scheme to be used when meshing that entity. This section describes those geometry attributes that are not described elsewhere in this manual.

---

## Geometry

**URL:** https://coreform.com/cubit_help/geometry/geometry.htm

**Contents:**
- Geometry

CUBIT usually relies on the ACIS solid modeling kernel for geometry representation; there is also mesh-based geometry. Other solid model kernels are planned. Geometry is imported or created within CUBIT. Geometry is created bottom-up or through primitives. CUBIT imports ACIS SAT files. CUBIT can also read STEP, IGES, and FASTQ files and convert them to the ACIS kernel. SolidWorks, AutoCAD, and some other commercial CAD systems can write SAT files directly.

Once in CUBIT, an ACIS model is modified through booleans. Without changing the geometric definition of the model, the topology of the model may be changed using virtual geometry. For example, virtual geometry can be used to composite two surfaces together, erasing the curve dividing them.

---

## Geometry Booleans

**URL:** https://coreform.com/cubit_help/geometry/booleans/geometry_booleans.htm

**Contents:**
- Geometry Booleans

CUBIT supports boolean operations of intersect, subtract, and unite for bodies.

An automatic function associated with webcutting operations is regularizing geometry which can be turned off or back on with the following command:

Set Boolean Regularize [ON | off]

---

## Geometry Cleanup and Defeaturing

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/cleanup_and_defeaturing.htm

**Contents:**
- Geometry Cleanup and Defeaturing

Frequently, models imported from various CAD platforms either provide too much detail for mesh generation and analysis, or the geometric representation is deficient. These deficiencies can often be overcome with small changes to the model. Several tools are provided in CUBIT for this purpose.

The following describes the features available in CUBIT for clean up and defeaturing

---

## Geometry Creation

**URL:** https://coreform.com/cubit_help/geometry/geom_creation/geom_creation.htm

**Contents:**
- Geometry Creation

There are three primary ways of creating geometry for meshing in CUBIT. First, CUBIT provides many geometry primitives for creating common shapes (spheres, bricks, etc.) which can then be modified and combined to build complex models. Secondly, geometry can be imported into CUBIT. Finally, geometry can be defined by building it from the "bottom up", creating vertices, then curves from those vertices, etc. Two of these three methods for creating geometry in CUBIT will be described in detail in this section.

All of these geometry creation commands have been expressed in the GUI's command panels. To navigate to the volume creation command panels, for example, select "Mode-Geometry", then "Entity-Volume", then "Action-Create", as shown below. Other geometry creation command panels are available for each geometry type.

---

## Geometry Decomposition

**URL:** https://coreform.com/cubit_help/geometry/decomposition/geometry_decomposition.htm

**Contents:**
- Geometry Decomposition

Geometry decomposition is often required to generate an all-hexahedral mesh for three-dimensional solids, as fully automatic all-hex mesh generation of arbitrary solids is not yet possible in CUBIT. While geometry booleans can be used for decomposition (and are the basis of the underlying implementation of advanced decomposition tools described here), CUBIT has a webcut capability specially tuned for decomposition. It is also useful to split periodic surfaces to facilitate quad and hex meshing.

---

## Geometry Deletion

**URL:** https://coreform.com/cubit_help/geometry/geometry_deletion.htm

**Contents:**
- Geometry Deletion

Geometry can be deleted from the model using the following command:

Delete [Body | Volume | Surface | Curve | Vertex] <id_range> [keep_lower_geometry]

Any type of Body can be deleted, whether it is based on solid model geometry or another representation. Other entities (Surface, Curve, Vertex) can be deleted when they are "free", i.e. when they are not contained in an entity of higher topological order (Body, Surface or Curve, respectively); this type of geometry is often created from the lowest order topology up.

The optional keep_lower_geometry keyword, valid when deleting curves, surfaces, or volumes, destroys the specified entity while retaining its lower-order (child) geometry as free entities:

---

## Geometry Imprinting and Merging

**URL:** https://coreform.com/cubit_help/geometry/imprint_merge/geometry_imprint_merge.htm

**Contents:**
- Geometry Imprinting and Merging

Geometry is created and imported in a manifold state. The process of converting manifold to non-manifold geometry is referred to as "geometry merging", since it involves merging multiple geometric entities into single ones. When importing mesh-based geometry, the merging step can be automatic. Imprinting is a necessary step in the merging process, which ensures that entities to be merged have identical topology.

---

## Geometry Orientation

**URL:** https://coreform.com/cubit_help/geometry/geometry_orientation.htm

**Contents:**
- Geometry Orientation
- Adjusting Orientation

The orientation of surface and curve geometry is the direction of the normal and tangent vectors respectively.

Each surface has a forward (or top) side. The evaluation of the surface normal at any point on the surface will return a vector at that point, orthogonal to the surface and directed towards the forward side of the surface. The mesh faces generated on each surface will have the same normal direction as their owning surface.

Each curve has a forward direction and a corresponding start and end vertex. The direction of the curve is from start to end vertex. The evaluation of the tangent vector of the curve at any point along the curve will result in a vector that is both tangent to the curve and pointing in the forward direction of the curve (towards the end vertex along the path of the curve.) The mesh edges created on each curve will be oriented in the same direction as their owning curve. The exported nodes and edges of a curve mesh will be written in the order they occur along the path of the curve.

Higher-dimension geometry has uses lower-dimension geometry with an associated sense (forward or reversed) for each lower-dimension entity. For example, a volume as a sense for each surface used to bound the volume. If the surface normal points outside the volume, then the volume uses the surface with a forward sense. If the surface normal points into the interior of the volume, the volume uses the surface with a reversed sense. Similarly a surface is bounded by a set of curves forming a loop such that the direction of the loop and the sense of each curve results in a cycle that is counter-clockwise around the surface normal.

By default, a surface is oriented so that its normal points OUT of the volume of which it is a part. For a merged surface (a surface which belongs to more than one volume) or a free surface (a surface that belongs to no volume, also known as a sheet body), the orientation of the surface is arbitrary. The orientation of a surface influences the orientation of any elements created on that surface. All surface elements have the same orientation as the surface on which they are created. The following commands are available to adjust the normal-direction for a surface:

Surface <id_range> Normal Opposite

Surface <id_range> Normal Volume <id>

The orientation of a surface can be flipped from its current orientation by using the "Opposite" keyword. The orientation of a merged surface can be set to point OUT of a specific volume by specifying that volume in the "Volume" keyword.

Occasionally, volumes will be created "inside-out". The command:

Reverse {Body|Volume|Surface} <id_range>

will turn a given volume, surface, or body inside out. This should be equivalent to reversing the normals on all the surfaces. This shouldn't be encountered very often, as it is a very rare condition.

The following commands are available to adjust the tangent direction of a curve:

Curve <id_range> Tangent Opposite

Curve <id_range> Tangent {Forward|Reverse} Surface <id>

Curve <id_range> Tangent {Start|End} Vertex <id>

The first command reverses the tangent direction of the curve. The second command sets the tangent direction such that it is used by a specific surface with a specified sense. The third command sets the tangent direction of the curve such that the curve starts or ends with the specified vertex. For the latter two forms of the command, the curve must be adjacent to the specified surface or vertex.

The below command can be used to change the orientation of multiple curves at once. With the direction option, the curve will be oriented along the specified direction. With the location option, the vertex closest to the give location becomes the start vert in the oriented curve. The curve orientation can be reversed using the opposite argument. Also, a vertex id can be specified to make it the start vertex in the oriented curve.

Curve <id_range> Orient Sense {direction (options)|location (options)|vertex <id_range>} [Opposite]

The above command is useful in changing the orientation of multiple curves at once using various options described. This becomes helpful, e.g., when bias is applied on multiple curves. By default, bias depends on the orientation of the curve, i.e., bias begins at start vertex.

---

## Geometry Simplification

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/healing/spline_removal.htm

**Contents:**
- Geometry Simplification

Spline geometry of the surfaces and curves of an entity can be replaced with geometrically equivalent analytic surfaces and curves. The following command attempts to do this:

Healer Simplify {volume <ids>|body <ids>} [{simplifytol} <value>] [keep]

Use simplifytol to specify a tolerance for the simplification operation. The default tolerance is 1e-6. Note: Even if the spline entity is within this tolerance to the analytic form, simplification still may not be possible.

The keep option will retain the original body and generate a new body containing analytic surfaces.

Execute Filter Curve Geometry_type Spline

---

## Geometry Transforms

**URL:** https://coreform.com/cubit_help/geometry/transforms/geometry_transforms.htm

**Contents:**
- Geometry Transforms

Bodies can be modified in CUBIT using transform operations, which include align, copy, move, reflect, restore, rotate, and scale. With the exception of the copy operation, transform operations in CUBIT do not create new topology, rather they modify the geometry of the specified bodies. ACIS, Mesh Based Geometry and Virtual Geometry representations may be transformed. If the geometric entity has been meshed, the nodes of the mesh will be transformed along with the geometry. To transform the nodes of a mesh as they are written to the Exodus II mesh file without modifying their location within CUBIT, see Transforming Mesh Coordinates.

---

## Groups

**URL:** https://coreform.com/cubit_help/geometry/groups/geometry_groups.htm

**Contents:**
- Groups

There are several utilities in CUBIT which use groups as a means of visualizing output. These utilities are described elsewhere, but listed here for reference:

---

## Groups in Graphics

**URL:** https://coreform.com/cubit_help/geometry/groups/groups_in_graphics.htm

**Contents:**
- Groups in Graphics

In the GUI version of CUBIT, groups may be picked with the mouse.

When displaying a group containing hexes, only the outside skin of the hexes will be displayed.

---

## Healing

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/healing/healing.htm

**Contents:**
- Healing

Healing is an optional module that detects and fixes ACIS models.

It is possible to create ACIS models that are not accurate enough for ACIS to process. This most often happens when geometry is created in some other modeling system and translated into an ACIS model. Such models may be imprecise due to the inherent numerical limitations of their parent systems, or due to limitations of data transfer through neutral file formats. This imprecision can also result when an ACIS model is created at a different tolerance from the current tolerance settings. This imprecision leads to problems such as geometric errors in entities, gaps between entities, and the absence of connectivity information (topology). Since ACIS is a high precision modeler, it expects all entities to satisfy stringent data integrity checks for the proper functioning of its algorithms. Therefore, if such imprecise models must be processed by an ACIS based system, "healing" of such models is necessary to establish the desired precision and accuracy.

The following sections describe how to use the Healing capability in ACIS and CUBIT to analyze and heal defective ACIS geometry.

---

## Importing 2D Exodus Files

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_import/importing_2d_exodus2_files.htm

**Contents:**
- Importing 2D Exodus Files

CUBIT has a limited capability to create ACIS Geometry from 2D ExodusII finite element mesh files. (For a more general capability, see the Import Mesh Geometry command, which will create Mesh-Based Geometry).

To import a 2D Exodus II file and create ACIS geometry, the following command can be used:

Import Free Mesh '<filename>' {Time <t> | Step <step#> | Last}

CUBIT can create ACIS geometry from 2D Exodus II data files (4, 8, or 9 node QUAD or SHELL element types) that do not have enclosed voids (holes surrounded by mesh) and which were originally generated with CUBIT and exported to ExodusII with the Nodeset Associativity option set to on. The Nodeset Associativity command records the topology of the geometry into special nodesets which allow CUBIT to reconstruct a new solid model from the mesh even after it has been deformed. The new solid model of the deformed geometry can be remeshed with standard techniques or meshed with a sizing function that can also be imported into CUBIT from the same ExodusII file. CUBIT's implementation of the paving and triadvance algorithms can generate a mesh following a sizing function to capture a gradient of any variable (element or nodal) present in the ExodusII file.

In order for this feature to be effective, the following commands must be issued when the mesh is exported and later imported:

nodeset associativity on

set associativity complete on

The first command ensures that the geometry will be correctly recovered from the mesh, while the second ensures that boundary condition and material IDs will be recovered.

---

## Importing Abaqus Files

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_import/importing_abaqus.htm

**Contents:**
- Importing Abaqus Files

The command to import a mesh from an Abaqus format file is:

Import Abaqus [Mesh Geometry] '<input_filename>' [Feature Angle <angle>] [Nobcs]

Including the keyword Mesh Geometry will instruct CUBIT to create mesh-based geometry. This will provide the user with the ability to remesh geometric entities. If the user does not import with the Mesh Geometry flag, he will have to tell CUBIT to draw the mesh after the import is done in order to view it.

The Feature Angle is used when building the surface topology to determine when to split a surface into two surfaces. If the angle between two neighboring element normals is less than Feature Angle, then the two elements will be placed on separate surfaces. If the keyword Feature Angle is not supplied, the default 135 degrees is used. For a description of importing mesh geometry see Importing Exodus II Files.

The Abaqus importer can import the following Abaqus file formats: flat file, part-independent, and part-dependent.

It should be noted that CUBIT sometimes cannot successfully generate mesh-based geometry for complex models. If this occurs, import the mesh without the Mesh Geometry flag, and draw the mesh to view it.

To list Abaqus cards supported by Cubit:

List Abaqus Import Cards

This command will list out all supported Abaqus cards that CUBIT can interpret.

Table 1. Supported Element Types

B21 B31 T2D2 T3D2 SPRINGA SPRING1 SPRING2

See http://www.simulia.com/ for more information on the ABAQUS file format.

---

## Importing ACIS Files

**URL:** https://coreform.com/cubit_help/geometry/import/importing_acis.htm

**Contents:**
- Importing ACIS Files
- Import Options
- Case-Insensitive Entity Names
- Importing ACIS files at startup

The command used to read an ACIS file is:

Import Acis '<acis_filename>' [No_bodies][No_surfaces] [No_curves][No_vertices][Group {'<name>'|<id>}] [Binary|Ascii] [Show_Each] [Sort] [XML '<xml_filename>'] [Attributes_On] [Separate_Bodies] [merge_gloabally] [Heal]

The import ACIS command is the primary mechanism for generating geometry within CUBIT. ACIS parts can be generated and saved with CUBIT, but in most cases are developed within a 3rd party CAD package and exported for use in CUBIT. CUBIT provides the capability to import ACIS solid models and make modifications to them so they can be meshed. CUBIT incorporates the commercial ACIS libraries developed and maintained by Spatial Inc. for reading and writing ACIS format files. IGES and STEP format files can also be imported and exported to/from CUBIT using the Spatial's libraries.

It is possible to include free entities (vertices, curves and surfaces) in the file. The default operation is to read all entities in the file whether they are included as part of a body or are free. By using any of the options no_bodies, no_surfaces, no_curves, or no_vertices, the user may exclude certain types of free entities.

The group option of the import command will allow the user to create a group for each set of imported geometry. The newly created group can later be accessed using the name or id specified with the group option.

The import capability of ACIS files supports both the ASCII format (.sat) and binary format (.sab). When importing, the filename extension will determine the default file type, be it ASCII or binary. A (.sat) extension will default to ASCII, while a (.sab) extension will default to binary. If you use a different file extension you can specify the type with the [binary|ascii] option. Binary files can be significantly faster but are not guaranteed to be upward compatible, nor cross-platform compatible. Therefore, it is recommended that models be archived in ASCII format.

Normally the numerical IDs of the geometric entities contained in the ACIS model are used directly within CUBIT. The sort option provides the capability to compress the IDs read from the ACIS file. The sort option does the same thing as the compress ids sort command, but combines it with the import command to remove a step in the process.

The show_each option is a graphics option that applies to how the volumes are shown as they are imported. If there are multiple volumes in the file, the graphics display will be updated between each volume during import.

The xml option will read assembly information and other metadata from an XML file in the DART metadata XML format. See the metadata documentation and the Analyst's Home Page for details.

The attributes_on option will enable attribute support for the file. Attributes include properties like entity color, entity id, and meshing scheme. Including the attributes option will only affect the current import. The settings will be restored to their previous settings after importing.

To retain any possible merge information when importing an ACIS file use the attribute_on command.

The separate_each option creates a separate body for each volume that is imported, preventing multi-volume bodies from being imported.

When importing, the use may specify the scope of the merge using merge_globally. The default behavior is to merge within the scope of the file being imported. With the merge_globally option, imported entities will merge with anything, including entities already in the Cubit session that have merge attributes on them.

Use the heal option to heal the entities when importing.

Entity names in Cubit are case-insensitive. This means that there is no difference between 'myvolume' and MyVolume'. When importing entity names as attributes any names that are case-sensitive duplicates will be made unique. This is done by appending one or more underscores, '_', followed by a number 1 to 9 or a letter A to Z. For example, two names 'myvolume' and 'MyVolume' encountered in that order will result in the names 'myvolume' and MyVolume_1'. Case-sensitivity can be toggled on/off with the command:

[Set] Case Sensitive Names [on|OFF]

ACIS files can also be imported using the "-solid" option when starting CUBIT from the UNIX command prompt. (See Execution Command Syntax for details.) Note that the filename must be enclosed in single or double quotes. This command will create as many bodies within CUBIT as there are bodies in the input file.

See also Exporting ACIS Files.

---

## Importing and Exporting Metadata

**URL:** https://coreform.com/cubit_help/geometry/metadata/metadata_io.htm

**Contents:**
- Importing and Exporting Metadata
- Importing Metadata
- Exporting Metadata
- Importing and Exporting DART Artifacts

Metadata can be imported from and exported to a file. In most cases metadata will be imported and exported with a data file such as a SAT file or a genesis file. CUBIT is also compatible with DART artifacts, including artifact dependency tracking.

Parts and assemblies can be created and associated with geometry by importing a DART Metadata file along with a geometry file, using the XML option of the import command. At this time the only two geometry formats which support metadata import are STEP and ACIS:

Import {Step|Acis} "<filename>". . . [XML "<xml_filename>"]

To successfully associate the contents of the geometry file with the parts described in the metadata, the XML file must follow the DART Metadata 3.0 XML schema found at https://dart.sandia.gov/wiki/display/SAW/DartMetadataPlugin, and the geometry file must contain extra DART data. A suitable STEP file and a corresponding metadata file can be exported from Pro/E using the Pro/E (Creo) extension, see the Metadata plugin page for details. A SAT file and corresponding metadata file can be obtained by exporting them from CUBIT using the XML option of the export command.

Some export commands include an XML option. Including this option in the export command instructs CUBIT to write out a DART metadata file, in addition to the traditional data file. The metadata file includes the data required to enable interoperability with other DART-compliant applications.

The only geometry export command which supports the XML option is ACIS export:

Export Acis “<acis_filename>” [XML “<xml_filename>”]

When an ACIS file exported with metadata, the specified XML file includes a description of the assembly hierarchy as it appears in CUBIT.

Metadata can also be written to an XML file when exporting mesh. The only mesh export command which supports the XML option is genesis export:

Export {Genesis|Mesh} “<mesh_filename>” [XML '<xml_filename>']

The XML file generated during mesh export includes the same information in a geometry metadata file, but also includes mesh-related data such as mappings between parts and element blocks, and includes any block, nodeset, or sideset names or descriptions which have been defined.

The DART project has defined a specific way to package data files with corresponding metadata files. A correctly packaged set of data files with a corresponding metadata file is called an artifact. An artifact’s metadata file is always located in the same directory as the primary data file, and is always named artifact.dta.

Within the DART environment, dependencies between artifacts may be tracked by placing tracking information into metadata files. CUBIT supports automated artifact dependency tracking. Tracking information in an input metadata file is automatically reflected in any output metadata file written by CUBIT.

If input is correctly packaged as an artifact, CUBIT can automatically locate and read the metadata file corresponding to a particular input data file. To have CUBIT do this, select the “Import as Artifact” checkbox in the Open File dialog.

CUBIT can also package output as an artifact. To do so, select the “Export as Artifact” checkbox in the export dialog box.

When importing or exporting artifacts using the command line, include the XML option in the import or export command, specifying the xml file called artifact.dta in the same directory as the main data file.

For dependency tracking purposes, it may be necessary to import an artifact’s metadata file by itself. For example, it may be necessary to import an artifact consisting of an IGES file. Since the Import IGES command does not support the XML option, the metadata file must be imported separately. To do so, use the command:

Import XML “<xml_filename>”

When working with correctly packaged artifacts, the XML filename will always be artifact.dta.

---

## Importing a Mesh

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_import/mesh_import.htm

**Contents:**
- Importing a Mesh

ExodusII finite element data files can be imported into CUBIT. Several options for importing the mesh are available, (including mesh transformations):

---

## Importing Coreform Cubit into Python

**URL:** https://coreform.com/cubit_help/python/importing_cubit_into_python.htm

**Contents:**
- Importing Coreform Cubit into Python

Python users are able to import Coreform Cubit into Python and make calls into Coreform Cubit via CubitInterface and the other Python classes described in this section. Below is a simple Python script. The key parts are ensuring the Coreform Cubit libraries are on the path and ensuring the cubit.init() call is made first.

Python scripts that run inside Coreform Cubit have a special module name. This module name can be used to differentiate code that run in and out of Coreform Cubit:

---

## Importing Exodus II Files

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_import/importing_exodus2_files.htm

**Contents:**
- Importing Exodus II Files
- Common Options
  - Specifying a Portion of the Mesh to be Imported
  - Combine Genesis IDs Option
  - Combine Genesis Names and Nodes IDs Options
  - Unique Genesis IDs Option
  - Genesis Collision Fail Option
  - Block_Offset, Sideset_Offset, Nodeset_Offset Options
  - Unique Node and Element IDs Option
  - Element and Node ID Collision Fail Option

The commands to import meshes from an Exodus II format file are:

Import Mesh '<exodusII_filename>' No_Geom [Block <block_ids>] [block_name <names>] [{genesis_collision_fail|COMBINE_GENESIS_IDS|combine_genesis_names|unique_genesis_ids}] [block_offset <value>] [sideset_offset <value>] [nodeset_offset <value>] [{node_id_collision_fail|UNIQUE_NODE_IDS}] [{element_id_collision_fail|UNIQUE_ELEMENT_IDS}] [node_offset <value>] [element_offset <value>]] [nodal_var{<string>|all_nodal_vars}] [element_var<string>|all_element_vars}] [group_name '<free_elements>'] [[Time <time>|Step <step>|Last] [Scale <value>]]

Import Mesh '<exodusII_filename>' [Block <block_ids>] [block_name <names>] [{genesis_collision_fail|COMBINE_GENESIS_IDS|combine_genesis_names|unique_genesis_ids}] [block_offset <value>] [sideset_offset <value>] [nodeset_offset <value>] [{node_id_collision_fail|UNIQUE_NODE_IDS}] [{element_id_collision_fail|UNIQUE_ELEMENT_IDS}] [node_offset <value>] [element_offset <value>]] [{Group|Body|Volume|Surface|Curve|Vertex} <id_range> | Preview]

Import Mesh Geometry '<exodusII_filename>' [Block <id_range>|ALL] [block_name <names>] [{genesis_collision_fail|COMBINE_GENESIS_IDS|combine_genesis_names|unique_genesis_ids}] [block_offset <value>] [sideset_offset <value>] [nodeset_offset <value>] [{node_id_collision_fail|UNIQUE_NODE_IDS}] [{element_id_collision_fail|UNIQUE_ELEMENT_IDS}] [node_offset <value>] [element_offset <value>]] [nodal_var{<string>|all_nodal_vars}] [element_var<string>|all_element_vars}] [Use [NODESET|no_nodeset] [SIDESET|no_sideset] [Feature_Angle <angle>] [Surface_Feature_Angle <angle>] [LINEAR|Gradient|Quadratic|Spline|Acis] [Deformed {Time <time>|Step <step>|Last} [Scale <value>] ] [MERGE|No_Merge] [Merge_nodes <tolerance>] [{midnode_correction|NO_MIDNODE_CORRECTION}]

Import Mesh '<exodusII_filename>' Lite [{genesis_collision_fail|COMBINE_GENESIS_IDS|combine_genesis_names|unique_genesis_ids}] [block_offset <value>] [sideset_offset <value>] [nodeset_offset <value>] [{node_id_collision_fail|UNIQUE_NODE_IDS}] [{element_id_collision_fail|UNIQUE_ELEMENT_IDS}] [node_offset <value>] [element_offset <value>]]

Import Mesh Geometry (options)

Import Free Mesh (2D)

Export [ Genesis | Mesh ] '<filename>'

List Import Mesh NodeSet Associativity

List [Export Mesh] NodeSet Associativity

[Set] Import Mesh NodeSet Associativity [ON|off]

[Set] [Export Mesh] NodeSet Associativity [on|OFF]

Transforming Mesh Coordinates

Set Import Mesh [Vertex] [Curve] [Surface] Tolerance <distance>

Set Import Mesh NodeSet Order [On|Off]

List Import Mesh NodeSet Order

The Block option in the Import Mesh command indicates that only the specified element block should be imported from the Exodus II file. The blocks are specified by ID. The block_name option can be used to import only the named blocks. Multiple blocks can be imported by making a comma separated list of names. The block and block_name options can be used together to specify some blocks by ID and others by name. If the block or block_name options are not specified, then the entire mesh file is read. These options are not yet supported for lite imports, which currently imports the entire mesh.

The combine_genesis_ids option, is used to combine blocks where the IDs in the session and the file being imported are identical. This can occur when importing into an active session where Cubit IDs have already been assigned. The default behavior is to combine genesis entities based on IDs. If two entities have differnet IDs, but the same names, they will not be combined, and the import will fail.

The combine_genesis_names option, is used to combine blocks where the names in the session and the file being imported are identical. This can occur when importing into an active session where names have already been assigned. If two entities have different names, but identical IDs, they will not be combined, and the import will fail.

The combine_node_ids option is only available in the 'lite' form of the 'import mesh' command. This option combines nodes, where the ids in the session and the file being imported are identical, regardless of location (coincidence).

The unique_genesis_ids option is used to renumber genesis entities from the genesis file in the case that ID overlap exists when importing into Cubit. The incoming genesis entities are kept unique and are not combined with genesis entities already in the session. In case of colliding IDs, a report displayed in the command window showing the original and new IDs. This renumbering can occur when importing into an active session where Cubit IDs have already been assigned. If an entity being imported has the same name as one already in the session, the entity being imported will be renamed with a number suffix '_N'.

The genesis_collision_fail option allows the user to prevent the genesis file import if any incoming genesis entity IDs or names are already used by genesis entities in the session. This can occur when importing into an active session where Cubit IDs have already been assigned.

The block_offset, sideset_offset, and nodeset_offset options may be used to modify the IDs of genesis entities being imported. The provided value will be added to the ID in the file.

The unique_node_ids, and unique_element_ids options are used to automatically renumber nodes and elements from the genesis file in the case that ID overlap exists when importing into Cubit. If there are no overlaps, the IDs in the file will be preserved. This can occur when importing into an active session where Cubit IDs have already been assigned.

The node_id_collision_fail, and element_id_collision_fail options allows one to prevent the genesis file import if any incoming node or element IDs are already used by mesh entities in the session. This can occur when importing into an active session where Cubit IDs have already been assigned.

The node_offset, and element_offset options may be used to modify the IDs of nodes and elements being imported. The provided value will be added to the ID in the file.

The nodal_var and element_var options allow nodal and element variable information respectively to be imported from the Exodus file. To import a specific varible, a name can be specified. Using the *_all option imports all variable information. By default, no variable information is imported.

The command to import a free mesh from an Exodus II format file without mesh-based geometry is:

Import Mesh '<exodusII_filename>' No_Geom [group_name '<free_elements>'] [[Time <time>|Step <step>|Last] [Scale <value>]]

When a free Exodus II mesh is imported into Cubit, it contains no geometric or topological information. Previously, the user could either associate that mesh with existing geometry, or build mesh-based geometry to fit the mesh. A third option, as of Cubit 11.1, allows the user to retain the disassociated mesh as a free mesh inside Cubit.

A free mesh may be modified as described in the Free Mesh section of the documentation. This includes limited access to smoothing, renumbering, transformations, refinement, mesh quality, and other mesh centric operations.

When an Exodus II File is imported as a free mesh, Cubit will automatically create a group called "free_elements" to contain the free mesh elements. The 'group_name' option can be used to give the group a different name.

Deformation information can be read in via the Time/Step/Last and Scale parameters.

Note: The Import Mesh <filename> No_Geom command is not to be confused with the Import Free Mesh command which applies only to 2D Exodus II Files.The term "Free Mesh" in both places of the documentation refers to the same thing - a mesh without geometry. However, in the case of all other import mesh commands, the imported free mesh ends up associated with geometry. The Import Mesh <filename> No_Geom is the only way to import a free mesh that remains disassociated from geometry.

The command to import a free mesh from an Exodus II format file and associate it with existing geometry is:

Import Mesh '<exodusII_filename>' [{Group|Body|Volume|Surface|Curve|Vertex} <id_range> | Preview]

The user can import a mesh from an Exodus II file and associate the mesh with matching geometry. The resulting mesh may then be manipulated normally. For example, the mesh may be smoothed or portions of it deleted and remeshed. The user can save their work by exporting the geometry and mesh, and then restore the geometry and mesh later. In some cases, saving and restoring can be faster or more reliable than replaying journal files.

Saving and importing a mesh may be useful for teams working on creating a conforming mesh of a large assembly so that they can pass information to one another. For example, a team member can export the mesh on the surfaces between two parts, and another team member import the mesh for use on an adjoining part of the assembly.

As of cubit version 7.0, any higher order elements, block definitions, nodesets, and sidesets are retained on import.

Meshes can be imported into Cubit that contain nodeset associativity data used for defining finite element boundary conditions. If an exported Cubit mesh is going to be imported back onto the same geometry, then before exporting the user should issue the following command:

set export mesh nodeset associativity on

This causes extra nodeset data to be written, which associates every node to a geometric entity, resulting in an import which is more reliable. When importing, if the user does not want to use the nodeset associativity data that exists in a file, then before importing the following command should be used:

set import mesh nodeset associativity off

The user may wish to turn geometry associativity off if, for example, the geometry is no longer identical as a result of curves being composited, or Cubit names changed due to a ACIS version changes.

Although there are some exceptions, Cubit requires that the mesh be imported onto the same geometry from which it was exported.

Since merge information is not stored with the ACIS representation, care should be taken that the geometry is merged the same way on export and import of the mesh. If not, importing the mesh one block at a time in successive commands may increase the chance of a successful import, at the cost of more memory and time.

Between exporting and importing a mesh, the geometry may be modified slightly by compositing entities. Mesh import will, however not be successful if entities are partitioned or a body is webcut. In some cases mesh import may be successful on modified geometry if the new vertices match up exactly with nodes of the mesh, and the new curves match up exactly with edge chains of the mesh. Unless this criteria is met, associating the mesh with the geometry will be unsuccessful.

To change the tolerance with which imported mesh must line up with geometry issue the command:

Set Import Mesh [Vertex] [Curve] [Surface] Tolerance <distance>

The Block option in the Import Mesh command indicates that only the specified element block should be imported from the Exodus II file. In the same manner, the Volume and other geometry options provide a way to import the nodes and element on the indicated geometry. If neither a block nor a geometry entity is specified, then the entire mesh file is read.

If a block is specified without specifying a geometry entity, associativity or proximity is used to determine which volume the block elements should be associated with. If a block and a volume are specified, the block elements are associated with the specified volume, provided they actually match. If a volume is specified without a block, associativity data is used to find a block corresponding to the given volume.

If the Import mesh NodeSet Order flag is on, the nodesets will be read in a manner which allows them to be associated with existing geometry. This means the nodesets are assumed to be in ascending order. If the flag is set to false, the goemetry nodesets in imported mesh files are assumed to be in random order. This value is on by default, and should not need to be changed by the user.

Cubit's mesh generation tools require an underlying geometry representation. In most cases, the ACIS solid modeling engine, compiled with Cubit, is used to represent the geometry. However, in some cases, an ACIS representation is not available, and a previously developed finite element mesh is the only available representation of the model. In order to utilize Cubit's mesh generation tools, the import mesh geometry command provides an option for creating geometry directly from the finite element mesh.

The import mesh geometry command will create a new volume for every block defined in the Exodus II file. It will also create curves, surfaces and vertices at appropriate locations on the model based on dihedral angles (also called feature angles) and assigned nodesets and/or sidesets. The mesh used to construct the geometry will be owned by the new geometric entities. This means that the mesh can be deleted, remeshed, or smoothed using any of Cubit's meshing tools by simply using the new geometry definition. Cubit will assign appropriate intervals to the new curves as well as determine an acceptable meshing scheme for surfaces and volumes.

The command to import a finite element mesh from an ExodusII format file and generate geometry from the mesh is:

Import Mesh Geometry '<exodusII_filename>' [Block <id_range>|ALL] [Use [NODESET|no_nodeset] [SIDESET|no_sideset] [Feature_Angle <angle>] [Surface_Feature_Angle <angle>] [LINEAR|Gradient|Quadratic|Spline|Acis] [Deformed {Time <time>|Step <step>|Last} [Scale <value>] ] [MERGE|No_Merge] [Merge_nodes <tolerance>]

Type the name of file to import in single quotation marks. The file must reside in the current directory. For information on changing the current directory, see Cubit environment commands. To list all the files in the current directory, type ls at the command prompt.

Use this option to select the specific blocks to be imported from the Exodus II file. If no blocks are entered, then all blocks will be read and imported from the file. Standard ID parsing can also be used in this argument to select a range of blocks. For example "1 to 5" or "1, 5 to 10 except 6".

Each unique block selected to be imported will define a new body in the geometric model. Figure 1 shows a simple example of the geometry generated from the 3D finite element mesh.

Figure 1. Example of mesh based geometry (right) created from a finite element mesh (left)

Blocks may be composed of 1D, 2D or 3D elements. For blocks composed of 2D elements (i.e. QUAD4, SHELL etc.), a sheet body will be created. One dimensional elements (i.e.. BEAM, TRUSS, etc.) will define curves. Where a block may be composed of more than one disconnected sets of elements, one body will be created for each continuous region of elements assigned to the same block. Where possible, the ID of the new body will be the same as the block ID. Since IDs must be unique, if a body ID is already in use, the next available ID will automatically assigned by the program.

Use the nodeset and sideset options to use any nodeset and sideset information in the Exodus II file in constructing geometry. Recall that nodesets and sidesets are generic boundary condition data assigned to nodes, edges or faces of the finite elements. It is useful to group mesh entities belonging to unique boundary conditions into geometric entities. This permits the user to remesh a particular region of the model without having to reassign boundary conditions.

If the nodeset and sideset arguments are given, geometric entities will be generated for each unique set of nodes, edges or element faces assigned to a nodeset or sideset. The default is to use any nodeset and sideset information available in the file. Figure 2 shows an example of how nodeset and sideset information might be used to generate geometry.

Figure 2. Example of geometry created from mesh entities assigned to nodesets (3) and sidesets (1 and 2).

Upon import, nodesets and sidesets are automatically created with the appropriate geometric entities assigned to them. The IDs of the new geometric entities, if generated from boundary condition data, will be the same as the nodeset and sideset IDs. Where doing so would conflict with existing geometric IDs, the program will automatically select the next available ID.

Use this option to specify the angle at which surfaces will be split by a curve or where curves will be split by a vertex. 180 degrees will generate a surface for every element face, while 0 degrees will define a single, unbroken surface from the shell of the mesh. The default angle is 135 degrees.

Figure 3. Example use of Feature Angle

Figure 3 shows an example of the use of different feature angles. On the left is a simple two-element hex mesh. Specifying a feature angle greater than 120 degrees would create the geometry in the center image. Using a feature angle less than 120 degrees and greater than 90 degrees would define the geometry on the right.

It is possible to independently control the feature angle for surfaces and curves. If Surface_Feature_Angle is specified, it controls the angle at which surfaces will be split by a curve, while Feature_Angle controls the angle at which curves will be split by a vertex. If Surface_Feature_Angle is not specified, Feature_Angle will control the angle for both surfaces and curves.

This argument allows the option of using a higher-order approximation of the surface when remeshing/refining the resulting geometry. Default is to use the original mesh faces themselves as the curve and surface geometry representation. If the finite element model to be imported is to represent geometry with curved surfaces, it may be useful to select this option. If selected, it will use a 4th order B-Spline approximation to the surface [Walton,96]. Figure 4 shows the effect of the smooth curve and surface option.

Figure 4. Effect of Smooth Curve and Surface Option for remeshing of mesh-based geometry

In this figure the top image is the original finite element mesh imported into Cubit. In this example both models have been remeshed with the same element size. The difference is that the figure on the right uses the smooth curve and surface option. While this option can improve the surface representation, it should be noted that memory requirements and meshing times can sometimes be affected.

If importing the Exodus II file using the command line, other options for surface representations are also available.

[LINEAR|Gradient|Quadratic|Spline|Acis]

The method used from the GUI is either Linear or Spline. The Gradient and Quadratic methods are still somewhat experimental and may not be as general purpose as the Spline representation. The Acis option will attempt to create ACIS geometry from the mesh. This option is an alpha feature and can only be used if developer commands have been turned on. For more detail see: Acis Geometry From Mesh

The deformed option permits the user to import time-dependant deformation information from the Exodus file. For this option, any vector data in the Exodus II file is assumed to be deformation information. If selected, deformations will be applied to the nodes upon import. Enter a specific time step value, integer step, or the last time available in the file. If time-dependant data is available in the Exodus II file, selecting the down arrow in the edit field will display the available time steps in the file. Default time is the last time step.

Figure 5. Example of remeshing of a deformed finite element mesh

Figure 5 shows an example of using Mesh-Based Geometry for a large deformation analysis. In this case, the analysis [Attaway et. al.,98] began and continued until mesh quality became unacceptable. At that point, the mesh was imported into Cubit and geometry re-created from the computed deformations. The finite element mesh could then be removed, remeshed or improved and written back to an Exodus II file. After remapping [Wellman,99] the appropriate analysis variables back to the mesh, the analysis could then be restarted. This process was repeated multiple times until the desired results were achieved.

Note: Care should be taken when using large deformations, as inverted elements (negative Jacobians) may produce unpredictable results with the resulting geometric representation.

Also available is an optional scale factor. This applies the indicated scale to all deformations. Default is 1.0.

This option allows the user to either merge or not merge the resulting volumes. The default option is to merge adjacent volumes. This results in non-manifold topology, where neighboring volumes share common surfaces. Using the no_merge option, adjacent volumes will generate distinct/separate surfaces.

The merge_nodes option will allow the user to specify a different tolerance for merging nodes on import. The default value is 1e-6.

Note: Care should be taken when setting import merge tolerances. Setting a tolerance too low will not merge adjacent nodes. Setting the tolerance too high can produce undesirable results, and severely tangle the mesh.

When importing a mesh in Cubit, the software performs quality checks on the elements. By default, if any elements fall below the specified quality threshold, Cubit notifies the user. This quality assessment applies to imported mesh-based geometry that uses high-order tetrahedral elements (tet10).

For TET10 elements, the node constraint smart command evaluates element quality using a designated quality metric, typically the default normalized inradius. If the quality of an element falls below a defined threshold (default: 0.15) and straightening the edge of the TET10 would improve the quality, Cubit automatically performs midnode correction. This correction can also be enabled during the import process.

By default, the midnode correction option is set to no_midnode_correction, meaning that the mesh will be imported without modifying midnode locations. However, users have the flexibility to choose the midnode_correction option when importing mesh-based geometry. Enabling this option allows Cubit to straighten high-order edges if the mesh quality metric falls below the designated threshold and if it results in improved quality.

The command to import a lite mesh from an Exodus II format file is:

Import Mesh '<exodusII_filename>' lite

When an Exodus II mesh is imported into Cubit using the lite option, it contains no geometric or topological information.

The lite mesh import may be an option for users wanting to quickly view the mesh without gaining all the abilities to modify the mesh.

More information on how a lite mesh may be viewed or modified is described in the Lite Mesh section of the documentation.

---

## Importing Facet Files

**URL:** https://coreform.com/cubit_help/geometry/import/importing_facet.htm

**Contents:**
- Importing Facet Files
- Facet File Format
- Feature Angle
- Smooth Curves and Surfaces
- Merge
- Make elements
- Stitch
- Improve

CUBIT provides the capability to import a model composed of facets to create geometry. The command to import facets from a file is:

Import [Facets|AVS] ''<filename>" [Feature_Angle <angle>] [LINEAR||Spline] [MERGE|No_merge] [Make_elements] [Stitch] [Improve]

Import STL ''<filename>" [Feature_Angle <angle>] [Surface_Feature_Angle <angle>] [LINEAR|Gradient|Quadratic|Spline] [MERGE|No_merge] [Make_elements] [Stitch]

Import OBJ ''<filename>" [Feature_Angle <angle>] [Surface_Feature_Angle <angle>] [Make_elements]

Facets are simply triangles that have been stitched together to form surfaces. Faceted geometry representations are commonly used for graphics, bio-medical, geotechnical and many other applications that output a discrete surface representation. Upon import, the resulting geometry representation is Mesh-Based Geometry. Figure 1. shows an example of a faceted model and the resulting geometry created in CUBIT.

Figure 1. Example of faceted model and the resulting solid model created in CUBIT from the facets.

For convenience, the import facet command currently supports three different formats, facet, AVS and STL

The format for the ASCII facet file is as follows

n m id1 x1 y1 z1 id2 x2 y2 z2 id3 x3 y3 z3 . . . idn xn yn zn fid1 id<1> id<2> id<3> [id<4>] fid2 id<1> id<2> id<3> [id<4>] fid3 id<1> id<2> id<3> [id<4>] . . . fidm id<1> id<2> id<3> [id<4>]

n = number of vertices m = number of facet id<i> = vertex ID of vertex i x<i> y<i> z<i> = location of vertex i fid<j> = facet ID of facet j id<1> id<2> id<3> = IDs of facet vertices [id<4>] = optional fourth vertex for quads

As noted above, the facets can be either quadrilaterals or triangles. Upon import, the facets serve as the underlying representation for the geometry. By default, the facets are not visible once the geometry has been imported. To view the facets, use the following command:

draw surf <id range> facets

The feature angle option is used to specify the angle at which surfaces will be split by a curve or where curves will be split by a vertex. 180 degrees will generate a surface for every facet, while 0 degrees will define a single, unbroken surface from the shell of the mesh. The default angle is 135 degrees. This feature is identical to the feature angle option available when importing Exodus II files.

For the stl format, it is possible to independently control the feature angle for surfaces and curves. If Surface_Feature_Angle is specified, it controls the angle at which surfaces will be split by a curve, while Feature_Angle controls the angle at which curves will be split by a vertex. If Surface_Feature_Angle is not specified, Feature_Angle will control the angle for both surfaces and curves.

This option permits the use of a higher order approximation of the surface when remeshing/refining the resulting geometry. Default is to use the original facets themselves as the curve and surface geometry representation. If the facet model to be imported is to represent geometry with curved surfaces, it may be useful to apply this option. If the Spline option is selected, it will use a 4th order B-Spline approximation to the surface [Walton,96]. More information on using smooth approximation of the facets is available in Importing an Exodus II File.

This option allows the user to either merge or not merge the resulting surfaces. The default option is to merge adjacent surfaces. This results in non-manifold topology, where neighboring surfaces share common curves. The no_merge option, adjacent surfaces will generate distinct/separate curves.

This option creates mesh elements from each of the facets on the facet surface.

The stitch option is used with the facet or avs format files to try to merge vertices and triangles that are close. Figure 2 shows an example of where this might be employed. The model on the left contains facets that are not connected between the red and blue groups. In this case, the surfaces will not be water-tight, even though the vertices on the boundary between the two groups may be coincident. The stitch option attempts to eliminate the extra edge and vertex between the groups to form the model on the right. This option can be useful when importing facet files for 3D meshing. CUBIT's 3D meshing algorithms require a water-tight (closed) set of surfaces.

Figure 2. Example use of the stitch option on import.

The improve option will collapse short edges on the boundary of the triangulation that are less than 30% the length of the average edge length in the model. In some cases, short edges are the result of discrete boolean operations on the triangulation which may result in edges that are of negligible length. This option is particularly useful for boundaries where multiple surfaces come together at an edge. Figure 3. shows an example of where the improve option improved the quality of the triangles at the boundary. This option is especially useful if the facets themselves will be used for the FEA mesh.

Triangles near a boundary that have not been used the improve option

The same set of triangles where improve option has collapsed edges

Figure 3. Example use of the improve option

---

## Importing FASTQ Files

**URL:** https://coreform.com/cubit_help/geometry/import/importing_fastq.htm

**Contents:**
- Importing FASTQ Files

CUBIT can read a FASTQ file and convert it into an ACIS model:

Import Fastq '<fastq_filename>'

Note that the filename must be enclosed in single or double quotes.

FASTQ is an older, 2d meshing tool; (Blacker 88.) FASTQ files are a series of commands much like a CUBIT journal file. All FASTQ commands are fully supported except for the "Body" command (it is unnecessary and ignored), the "corn" (corner) line type, and some of the specialized mapping primitive "Scheme" commands. Standard mapping, paving, and triangle primitive scheme commands are handled. The pentagon, semicircle, and transition primitives are not handled directly, but are meshed using the paving scheme. The FASTQ input file may have to be modified if the Scheme commands use any non-alphabetic characters such as `+', `(`, or `)'. Circular lines with non-constant radius are generated as a logarithmic decrement spiral in FASTQ; in CUBIT they will be generated as an elliptical curve.

Since a FASTQ file by definition will be defined in a plane, it must be projected or swept to generate three dimensional geometry. CUBIT supports sweeping options to convert imported FASTQ geometries into volumetric regions.

---

## Importing Fluent Files

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_import/importing_fluent_files.htm

**Contents:**
- Importing Fluent Files

The command to import a mesh from a fluent format file is:

Import Fluent [Mesh Geometry] '<input_filename>' [Feature Angle <angle>] [nobcs]

Including the keyword Mesh Geometry will instruct CUBIT to create mesh-based geometry. This will provide the user with the ability to remesh geometric entities. If the user does not import with the Mesh Geometry flag, he will have to tell CUBIT to draw the mesh after the import is done in order to view it.

The Feature Angle is used when building the surface topology to determine when to split a surface into two surfaces. If the angle between two neighboring element normals is less than Feature Angle, then the two elements will be placed on separate surfaces. If the keyword Feature Angle is not supplied, the default 135 degrees is used. For a description of importing mesh geometry see Importing Exodus II Files.

It should be noted that CUBIT sometimes cannot successfully generate mesh-based geometry for complex models. If this occurs, import the mesh without the Mesh Geometry flag, and draw the mesh to view it.

---

## Importing Geometry

**URL:** https://coreform.com/cubit_help/geometry/import/geometry_import.htm

**Contents:**
- Importing Geometry
- Other Formats

Internally, CUBIT represents geometry as either ACIS solid model geometry or mesh-based geometry. CUBIT can import ACIS geometry in the native "sat" file format. CUBIT can also import STEP and IGES files and internally converts them into ACIS solid model geometry. For compatibility with Sandia legacy applications, CUBIT can import FASTQ input decks to create ACIS geometry, as well. CUBIT also contains experimental support for using SGM for representing geometry.

If you have geometry that has been created in another format, such as in SolidWorks, you will need to translate that geometry into something that Cubit can read. Many solid modeling packages have an Export ACIS .sat command, which is probably the easiest way of translating your model. If you do not have that option, there are some other possibilities.

---

## Importing IGES Files

**URL:** https://coreform.com/cubit_help/geometry/import/importing_iges.htm

**Contents:**
- Importing IGES Files
- Import Options

The ACIS IGES translator provides bi-directional functionality for data translation between ACIS and the IGES (Initial Graphics Exchange Specification) format.

The commands to import IGES files are:

Import Iges '<iges_filename>' [No_bodies] [No_surfaces] [No_curves] [No_vertices] [Group {'<name>'|<id>}] [Nofreesurfaces] [HEAL|noheal] [Logfile ['filename'] [Display]] [Show_Each] [Sort]

It is possible to include free entities (vertices, curves and surfaces) in the file. Default operation is to read all entities in the file whether they are included as part of a body or are free. By using any of the options no_bodies, no_surfaces, no_curves, or no_vertices, the user may exclude certain types of free entities.

The group option of the import command will allow the user to create a group for each set of imported geometry. The newly created group can later be accessed using the name or id specified with the group option.

The nofreesurfaces option will automatically convert free surfaces to bodies. By default this option is off.

By default, bodies are automatically healed when imported - if this causes problems, you can disable this option by using the noheal argument.

The logfile option specifies a file where informational messages generated during import of the STEP file will be written. The display option will display the file.

The show_each option is a graphics option that applies to how the volumes are shown as they are imported. If there are multiple volumes in the file, the graphics display will be updated between each volume during import.

Normally the numerical IDs of the geometric entities contained in the ACIS model are used directly within CUBIT. The sort option provides the capability to compress the IDs read from the ACIS file. The sort option does the same thing as the compress ids sort command, but combines it with the import command to remove a step in the process.

Note that the IGES import and export functionality might not be available on all 64-bit platforms.

See also Exporting IGES Files.

---

## Importing I-DEAS Files

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_import/importing_ideas.htm

**Contents:**
- Importing I-DEAS Files

The command to import a mesh from an I-DEAS format file is:

Import Ideas [Mesh Geometry] '<input_filename>' [Feature Angle <angle>] [Nobcs]

Including the keyword Mesh Geometry will instruct CUBIT to create mesh-based geometry. This will provide the user with the ability to remesh geometric entities. If the user does not import with the Mesh Geometry flag, he will have to tell CUBIT to draw the mesh after the import is done in order to view it.

The Feature Angle is used when building the surface topology to determine when to split a surface into two surfaces. If the angle between two neighboring element normals is less than Feature Angle, then the two elements will be placed on separate surfaces. If the keyword Feature Angle is not supplied, the default 135 degrees is used. For a description of importing mesh geometry see Importing Exodus II Files.

It should be noted that CUBIT sometimes cannot successfully generate mesh-based geometry for complex models. If this occurs, import the mesh without the Mesh Geometry flag, and draw the mesh to view it.

To see more information on the I-DEAS file format, visit their website at www.siemens.com.

---

## Importing MCNP Models

**URL:** https://coreform.com/cubit_help/geometry/import/importing_mcnp.htm

**Contents:**
- Importing MCNP Models
- Import Options

MCNP (Monte Carlo N‑Particle) is a general‑purpose radiation transport code that simulates how particles move through matter.

CUBIT can read an MCNP input file and convert its constructive solid geometry — cells, surfaces, and lattices — into an ACIS solid model geometry. This makes it possible to take an existing MCNP model and turn it into CAD geometry that can be cleaned up, meshed, and exported for radiation-transport workflows such as DAGMC. The conversion is based on the open-source mcnp2cad translator that has been converted to use native CUBIT functionality.

The command used to import an MCNP file is:

Import MCNP '<filename>' [verbose] [debug] [debug_output] [debug_input] [extra_effort] [skip_mats] [skip_merge] [skip_imps] [skip_nums] [skip_graveyard] [skip_imprint] [uwuw_names] [tol <value>]

A log of the conversion is always written to a file named mcnp_import.log in the current working directory.

By default the importer tags the generated geometry with the information needed by downstream neutronics workflows and cleans up the result by imprinting and merging. The options below, most of which begin with skip_, turn individual steps off.

Note: The command import cf_mcnp is a deprecated alias for import mcnp and will be removed in the next release.

See also Exporting DAGMC Models.

---

## Importing Meshed Based Geometry Files (MBG)

**URL:** https://coreform.com/cubit_help/appendix/alpha/importing_mbg_files.htm

**Contents:**
- Importing Meshed Based Geometry Files (MBG)

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Import mbg ''<filename>"

MBG is created in Cubit when one meshes a volume or imputs the mesh from a previously meshed volume with the import mesh geometry command. Optionaly there one may create geometry with the "set dev on" option.

In order to create, import and export MBG one needs to set the geometry engine to facet with the following command "set geom eng facet".

The following commands create a brick and export and import it as a MBG file: set geometry engine facet set dev on brick x 10 export mbg "brick.mbg" overwrite reset import mbg "brick.mbg"

set geometry engine facet

export mbg "brick.mbg" overwrite

import mbg "brick.mbg"

---

## Importing Nastran Files

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_import/importing_nastran.htm

**Contents:**
- Importing Nastran Files

The command to import a mesh from an Nastran format file is:

Import Nastran [Mesh Geometry] '<input_filename>' [Feature Angle <angle>] [Nobcs]

Including the keyword Mesh Geometry will instruct CUBIT to create mesh-based geometry. This will provide the user with the ability to remesh geometric entities. If the user does not import with the Mesh Geometry flag, he will have to tell CUBIT to draw the mesh after the import is done in order to view it.

The Feature Angle is used when building the surface topology to determine when to split a surface into two surfaces. If the angle between two neighboring element normals is less than Feature Angle, then the two elements will be placed on separate surfaces. If the keyword Feature Angle is not supplied, the default 135 degrees is used. For a description of importing mesh geometry see Importing Exodus II Files.

It should be noted that CUBIT sometimes cannot successfully generate mesh-based geometry for complex models. If this occurs, import the mesh without the Mesh Geometry flag, and draw the mesh to view it.

See http://en.wikipedia.org/wiki/Nastran for more information on the NASTRAN file format.

---

## Importing Patran Files

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_import/importing_patran.htm

**Contents:**
- Importing Patran Files

The command to import a mesh from an Patran format file is:

Import Patran '<neutral_filename>'

Import Patran Mesh Geometry '<neutral_filename>' [Use [Feature_Angle <angle>] [Linear|Gradient|Quadratic|Spline] ]

See Importing Exodus II Files for a description of the import options.

For more information on the Patran file format, see their website at www.mscsoftware.com.

---

## Importing SGM Files

**URL:** https://coreform.com/cubit_help/geometry/import/importing_sgm.htm

**Contents:**
- Importing SGM Files
- Import Options

CUBIT contains experimental support for importing SGM and STEP files using the Scalable Geometric Modeler (SGM) to represent the geometry.

The commands to import SGM files are:

Import SGM '<filename>' [restore_ids] [read_colors]

The Import SGM command can import either .sgm files or .step files. If given a .sgm file, the restore_ids option may be used to restore ids as they were in a previous SGM session. Restoration of IDs is not supported if a model was previously imported into SGM. The read_colors option is available if one wants to read colors found in the file. If read_colors is not given, colors will be automatically assigned by CUBIT based on the ID of the volumes.

Other CUBIT capabilities are limited when it comes to working with models imported into SGM. Visualization, list commands, and machine learning classification will work, but meshing, export and other operations are not yet supported.

---

## Importing STEP Files

**URL:** https://coreform.com/cubit_help/geometry/import/importing_step.htm

**Contents:**
- Importing STEP Files
- Import Options
- Import Settings
- Exporting a STEP file from Pro/Engineer

The ACIS STEP translator provides bi-directional functionality for data translation between ACIS and the file format standard STEP AP203.

STEP AP203 is an international standard which defines a neutral file format for representation of configuration control design data for a product.

The command used to import a STEP file are:

Import Step '<step_filename>' [No_bodies][No_surfaces] [No_curves] [No_vertices] [HEAL|Noheal] [COLOR|nocolor] [Logfile ['filename'] [Display]] [Show_Each] [Group {'<name>'|<id>}] [Sort] [XML '<xml_filename>']

By default, names on bodies in STEP files are not read in. To change this, the following command is available:

[set] Read Step Body Names [on|OFF]

To export a STEP file from Pro/ENGINEER, from the Export STEP Dialog, Press Options.

In the file step_config.pro add the following:

STEP_EXPORT_FORMAT AP203_CD.

Also be sure your export option is set to Solids. If the geometry has problems in CUBIT, you may need to increase the geometry accuracy in Pro/ENGINEER.

See also Exporting STEP Files.

---

## Imprinting Geometry

**URL:** https://coreform.com/cubit_help/geometry/imprint_merge/imprint.htm

**Contents:**
- Imprinting Geometry
- Regular Imprinting
- Tolerant Imprinting
- Mesh-Based Imprinting
- Imprint Settings

To produce a non-manifold geometry model from a manifold geometry, coincident surfaces must be merged together (See Geometry Merging); this merge can only take place if the surfaces to be merged have like topology and geometry. While various parts of an assembly will typically have surfaces, which coincide geometrically, an imprint is necessary to make the surfaces have like topology. There are three types of imprinting:

To preview which surfaces can or should be imprinted, or to force imprints that the regular imprint command misses, the Find Overlap command can be used.

The commands used to imprint bodies together are:

Imprint [Volume|BODY] <range> [with [Volume|BODY] <range>] [Keep]

A body can also be imprinted with curves, vertices or positions, and surfaces can be imprinted with curves. It is useful to imprint bodies or surfaces with curves to eliminate mesh skew, generate more favorable surfaces for meshing, or create hard lines for paving. Imprinting with a vertex or position can be useful to split curves for better control of the mesh or to create hard points for paving. Impriting a vertex onto a volume allows for a tolerance to be specified, snapping the vertex to the closest location on the volume that is within tolerance.

Imprint Body <body_id_range> [with] Curve <curve_id_range> [Keep]

Imprint Body <body_id_range> [with] Vertex <vertex_id_range> [tolerance <value>] [Keep]

Imprint {Volume|Body} [with] Position <coords> [position <coords> ... ]

Imprint Surface <surface_id_range> [with] Curve <curve_id_range> [Keep]

An Imprint All will imprint all bodies in the model pairwise; bounding boxes are used to filter out imprint calls for bodies which clearly don't intersect.

Normal imprinting may be ineffective for some assembly models that have tolerance problems, generating unwanted sliver entities or missing imprints altogether. Tolerant imprinting is useful for dealing with these tolerance challenged assemblies. To determine coincident and overlap entities, tolerant imprinting uses the merge tolerance. The commands also include an optional tolerance value that will be used for the purposes of the single command. Specifying an optional tolerance value will not change the default, system tolerance value.

A limitation of tolerant imprinting is that it cannot imprint intersecting surfaces onto one another, as normal imprinting can. Tolerant imprinting imprints only overlapping entities onto one other.

Imprint Tolerant {Body|Volume} <range> [tolerance <value>]

Tolerant imprinting can also be used to imprint curves onto surfaces, provided that the tolerance between surface and curve(s) falls within the merge tolerance. The 'merge' option will merge the owning volume of the specified surface with all other volumes that share any curves with this surface.

Imprint Tolerant Surface <id> with Curve <id_range> [merge] [tolerance <value>]

Imprint Tolerant Surface <id> <id> with Curve <id_range> [merge] [tolerance <value>]

Imprint Tolerant Surface <id> <id> [tolerance <value>]

The second form of the command imprints the specified bounding curves of one surface onto another surface and vice versa. Any specified curves that are not bounding either of the two specified surfaces will not be imprinted. The 'merge' option will merge all the volumes sharing any curve of these two surfaces, after the imprint.

It is recommended that normal imprinting be used when possible and tolerant imprinting be used only when normal imprinting fails.

Another form of the imprint command,

Imprint Mesh {Body | Volume} <id_list>

uses coincident mesh entities and virtual geometry to create imprints. See the Partitioned Geometry section for more information on this command.

After imprint operations, an effort is made to remove sliver entities: sliver curves and surfaces. Previously, all curves in participating bodies less than 0.001 were removed. Newer versions of Cubit changed this because there might be times when the user wants sliver curves/surfaces to be generated during an imprint operation. In order to give the user more control over the cleanup of these sliver entities after imprint operations, a command was implemented so that the user can set an 'imprint sliver cleanup tolerance'. The default tolerance for curves is the merge tolerance 0.0005. The default tolerance for surfaces is a suitable tolerance chosen internally based on the bounding box of the entity. Sliver surfaces are removed whose maximum gap distance among the long edges is smaller than the tolerance and who have at most three long edges. A long edge is an edge whose length is greater than the specified tolerance.

Set {Curve|Surface} Imprint Cleanup Tolerance <value>

---

## Intersect

**URL:** https://coreform.com/cubit_help/geometry/booleans/intersect.htm

**Contents:**
- Intersect

The intersect command generates one or more new volumes composed of the space that is shared by the volumes being intersected. There are two forms of the command. The first form is:

Intersect {Volume|[Body]} <range> [Keep] [Preview]

In this form, all volumes in the range will be intersected, and the resulting intersection volume(s) will contain all intersections of all input volumes. The original volumes will be deleted. The second form is:

Intersect {Volume|[Body]} <id> [With {Volume|[Body]} <range>] [Keep] [Preview]

In this form, the first volume is intersected with all volumes in the range specified using the with keyword. Intersections between volumes in the range are not included in the output. The original volume will be deleted and the other volumes updated with the intersection results.

The keep option results in the original volumes used in the intersect being kept.

If the Preview option is included in the command, the input volumes will not be modified. The computed intersection volume will be drawn as a red, shaded solid. For best results change the graphics mode to transparent or hidden line so the intersection is visible. Otherwise the intersection volume will be hidden by the volumes being intersected.

---

## List Geometry

**URL:** https://coreform.com/cubit_help/environment_control/listing_information/list_geometry.htm

**Contents:**
- List Geometry

The following commands list information about the geometry of the model.

List Names [Group|Body|Volume|Surface|Curve|Vertex|All]

List {Group|Body|Volume|Surface|Curve|Vertex} <range> [Ids]

List {geom_list} [Geometry|Mesh [Detail]]

List {Group|Body|Volume|Surface|Curve|Vertex} <range> {X|Y|Z}

The first command lists the names in use, and the entity type and id corresponding to each name. Specifying all lists names for all types; other options list names for a specific entity type. The names for an individual entity can be obtained by listing just that entity. Sample output from the list names surface command is shown below. This output shows that, for example, Surface 2 has the name ` BackSurface '.

______Name______ __Type__ Id _Propagated_ BackSurface Surface 2 No BottomSurface Surface 3 No FrontSurface Surface 1 No LeftSurface Surface 4 No RightSurface Surface 5 No TopSurface Surface 6 No

The second command provides information on the number of entities in the model and their identification numbers. If a range is given then detailed information is given on each entity in that range, unless the ids option is also given. If the ids option is used, just a list of ids is printed. This list can be very useful for large models in which several geometry decomposition operations have performed. Sample output from the list surface command is shown below.

CUBIT> list surface ids The 6 surface ids are 1 to 6.

CUBIT> list surf ids The 108 surface ids are 192 to 266, 268 to 271, 273 to 301.

List Surface [range] Ids' Examples

The <range> can be very general using the general entity parsing syntax. Using a <range> gives a brief synopsis of the local connectivity of the model, e.g. one can list the ids of the surfaces containing vertex 2; as shown in the listing below.. An intermediately detailed synopsis can be obtained by placing the range of entities in a group, then listing the group.

CUBIT> list surface in vertex 2 ids The 3 entity ids are 1, 5, 6.

CUBIT> group "v2_surfs" equals surface in vertex 2 CUBIT> list v2_surfs Group Entity 'v2_surfs' (Id = 3) It owns/encloses 3 entities: 3 surfaces. Owned Entities: Mesh Scheme Interval: Edge _____Name____ Type______Id +is meshed Count Size FrontSurface Surface 1 map+ 1 H 0.1 TopSurface Surface 6 map+ 1 H 0.1 RightSurface Surface 5 map+ 1 H 0.1

Using 'List' for Querying Connectivity.

The third command provides detailed information for each of the specific entities. This information includes the entity's name and id, its meshing scheme and how that scheme was selected, whether it is meshed and other meshing parameters such as smooth scheme, interval size and count. The entity's connectivity is summarized by a table of the entity's subentities and a list of the entity's superentities. Also, the nodesets, sidesets, blocks, and groups containing the entity are listed.

Specifying geometry will additionally list the extent of the entity's geometric bounding box, the geometric size of the entity, and depending on entity type, other information such as surface normal. See also the list {entities} x command below. If multiple volumes, surfaces, or curves are selected, it will list the total volume, area, or length of all entities, and the total geometric bounding box. If multiple volumes are selected, the centroid listed will be the composite centroid of the all of the volumes.

If a volume is recognized as a primitive (cylinder, brick, etc.), specifying geometry will list data for defining the primitive.

Specifying mesh will additionally list the number of mesh entities of each type interior to the entity and on bounding subentities. Mesh detail will list the ids of the mesh entities as well, following the format of the list ids command above.

The fourth command lists the entities sorted by either the x, y, or z coordinate of their geometric center. For example, in a large, basically cylindrical model centered around z-axis, it is useful to list the surfaces of a volume sorted by z to identify the source and target sweeping surfaces.

---

## Merge Tolerance

**URL:** https://coreform.com/cubit_help/geometry/imprint_merge/merge_tolerance.htm

**Contents:**
- Merge Tolerance
- Finding Nearly Coincident Entities

The default absolute merge tolerance used in CUBIT is 5.0e-4. This means that points which are at least this close will pass the geometric correspondence test used for merging. The user may change this value using the following command:

Merge Tolerance <val>

If the user does not enter a value, the current merge tolerance value will be printed to the screen. There is no upper bound to the merge tolerance, although in experience there are few cases where the merge tolerance has needed to be adjusted upward. The lower bound on the tolerance, which is tied to the accuracy of the solid modeling engine in CUBIT, is 1e-6.

These commands find vertex-vertex, vertex-curve and vertex-surface pairs whose separation is within the specified tolerance range. If a tolerance range isn't specified the default will be from merge tolerance to 10*merge tolerance. It is useful for determining if you need to expand merge tolerance to accomodate sloppy geometry.

Find Near Coincident Vertex Vertex {Body|Volume} <id_range> [low_tol <value>] [high_tol <value>]

Find Near Coincident Vertex Curve {Body|Volume} <id_range> [low_tol <value>] [high_tol <value>]

Find Near Coincident Vertex Surface {Body|Volume} <id_range> [low_tol <value>] [high_tol <value>]

---

## Merging Geometry

**URL:** https://coreform.com/cubit_help/geometry/imprint_merge/merging.htm

**Contents:**
- Merging Geometry
- Merge geometry automatically
- Test for merging in a specified group of geometry
- Force merge specified geometry entities
- Preventing geometry from merging
- Other Merge Commands

The steps of the geometry merging algorithm used in CUBIT are outlined below:

Thus, in order for two entities to merge, the entities must correspond geometrically and topologically, and if both are meshed must have topologically equivalent meshes. The geometric correspondence usually comes from constructing the model that way. The topological correspondence can come from that process as well, but also can be accomplished in CUBIT using Imprinting.

If both entities are meshed, they can only be merged if the meshes are topologically identical. This means that the entities must have the same number of each kind of mesh entity, and those mesh entities must be connected in the same way. The mesh on each entity need not have nodes in identical positions. If the node positions are not identical, the position of the nodes on the entity with the lowest ID will be used in the resulting merged mesh.

There are several options for merging geometry in CUBIT.

Merge All [Group|Body|Surface|Curve|Vertex] [group_results][tolerance <value>]

All topological entities in the model or in the specified bodies are examined for geometric and topological correspondence, and are merged if they pass the test.

If a specific entity type is specified with the Merge all, only complete entities of that type are merged. For example, if Merge all surface is entered, only vertices which are part of corresponding surfaces being merged; vertices which correspond but which are not part of corresponding surfaces will not be merged. This command can be used to speed up the merging process for large models, but should be used with caution as it can hide problems with the geometry.

Merge {Group|Body|Surface|Curve|Vertex} <id_range>[With {Group|Body|Surface|Curve|Vertex} <id_range>] [group_results] [force] [tolerance<value>]

All topological entities in the specified entity list, as well as lower order topology belonging to those entities, are examined for merging. This command can be used to prevent merging of entities which correspond and would otherwise be merged, e.g. slide surfaces.

Merge Vertex <id> with Vertex <id> Force

Merge Curve <id> with Curve <id> Force

Merge Surface <id> with Surface <id> Force

This command results in the specified entities being merged, whether they pass the geometric correspondence test or not. This command should only be used with caution and when merging otherwise fails; instances where this is required should be reported to the CUBIT development team.

Body <id_range> Merge [On | Off]

Volume <id_range> Merge [On | Off]

Surface <id_range> Merge [On | Off]

Curve <id_range> Merge [On | Off]

Vertex <id_range> Merge [On | Off]

These commands provide a method for preventing entities from merging. If merging is set to off for an entity, merging commands (e.g. "merge all") will not merge that entity with any other.

Set Merge Test BBox {on|OFF}

Set Merge Test InternalSurf {on|OFF|spline}

---

## Mesh-Based Geometry

**URL:** https://coreform.com/cubit_help/geometry/model_definitions/mesh_based_geometry.htm

**Contents:**
- Mesh-Based Geometry
- Creating Mesh-Based Geometry Models
- Improving Mesh-Based Geometry Models for Meshing
- Meshing Mesh-Based Models
- Exporting Mesh-Based Geometry

In contrast to the ACIS format, Mesh-Based Geometry (MBG) is not a third party library and has been developed specifically for use with CUBIT. Most of CUBIT's mesh generation tools require an underlying geometric representation. In many cases, only the finite element model is available. If this is the case, CUBIT provides the capability to import the finite element mesh and build a complete boundary representation solid model from the mesh. The solid model can then be used to make further enhancement to the mesh. While the underlying ACIS geometry representation is typically non-uniform rational b-splines (NURBS), Mesh-Based Geometry uses a facetted representation. Mesh-Based Geometry can be generated by importing either an Exodus II format file or a facet file.

Many of the same operations that can be done with traditional CAD geometry can also be done with mesh-based geometry. While all mesh generation operations are available, only some of the geometry operations can be used. For example, the following can be done with geometric entities that are mesh-based:

Some operations that are not yet available with mesh-based geometry include:

Mesh based geometry models can be created in one of two ways

While both of these methods create geometry suitable for meshing, there are some significant differences:

Exodus II contains a mesh representation that may include 3D elements, 2D elements, 1D elements and even 0D elements. It may also contain deformation information as well as boundary condition information. The import mesh geometry command is designed to decipher this information and create a complete solid model, using the mesh faces as the basis for the surface representations. Exodus II is most often used when a solid model that has previously been meshed requires modification or remeshing. Importing an Exodus II file will generate both geometry and mesh entities, assigning appropriate ownership of the mesh entities to their geometry owners. Deleting the mesh and remeshing, refining or smoothing are common operations performed with an Exodus II model.

The facet file formats supported by CUBIT are most often generated from processes such as medical imaging, geotechnical data, graphics facets, or any process that might generate discrete data. Importing a facet file will generate a surface representation only defined by triangles. If the triangles in the facet file form a complete closed volume, then a volume suitable for meshing may be generated. In cases where the volume may not completely close or may not be of sufficient quality, a limited set of tools has been provided. In addition to the standard meshing tools provided in CUBIT, it is also possible to use the triangle facets themselves as the basis for an FEA mesh.

In many cases, the triangulated representations that are provided from typical imaging processes are not of sufficient quality to use as geometry representations for mesh generation. As a result, CUBIT provides a limited number of tools to assist in cleaning up or repairing triangulated representations.

1. Using tolerance on STL files

Stereolithography (STL) files, in particular, can be problematic. The import mechanism for STL provides a tolerance option to merge near-coincident vertices.

2. Using the stitch option on AVS and facet files

The stitch option on the import facets|avs command provides a way to join triangles that otherwise share near-coincident vertices and edges. This is useful for combining facet-based surfaces to generate a water-tight model.

3. Using the improve option on facet files.

The improve option on the import facets command will collapse short edges on the boundary of the triangulation. This option improves the quality of the boundary triangles.

4. Smoothing faceted surfaces.

Individual triangles in a faceted surface representation may be poorly shaped. Just like mesh elements may be smoothed, facets may also be smoothed in CUBIT using the following command

Smooth <surface_list> Facets [Iterations <value>] [Free] [Swap]

To use this command, the surface cannot be meshed. Facet smoothing consists of a simple Laplacian smoothing algorithm which has additional logic to make sure it does not turn any of the triangles in-side out. It also determines a local surface tangent plane and projects the triangle vertices to this plane to ensure the volume will not "shrink". The iterations option can be used to specify the number of Laplacian smoothing operations to perform on each facet vertex (The default is 1).

The free option can be used to ignore the tangent plane projection. Used too much, the free option can collapse the model to a point. One of two iterations of this option may be enough to clean up the triangles enough to be used for a finite element mesh.

The swap option can be used to perform local edge swap operations on the triangulation. The quality of each triangle is assessed and edges are swapped if the minimum quality of the triangles will improve.

5. Creating a thin offset volume

Offset surfaces may be generated from an existing facet-based surface. This would be used in cases where a thin membrane-like volume might be required where only a single surface of triangles is provided. This command may be accomplished by using the standard create body offset command

The result of this command is a single body with an inside and outside surface separated by a small distance which is generally suitable for tet meshing. This command is currently only useful for small offsets where self-intersections of the resulting surface would be minimal. It is most useful for bodies that may be initially composed of a single water-tight surface.

6. Creating volumes from surfaces

A mesh-based geometry volume can be created from a set of closed surfaces. This can be accomplished in the same manner as the standard create body surface command

Create Body Surface <surface_id_range>

This command is limited to surfaces that match triangles edges and vertices at their boundary. The command will internally merge the triangles to create a water-tight model that would generally be suitable for tet meshing.

Mesh-Based models may be meshed just like any other geometry in CUBIT by first setting a scheme, defining a size and using the mesh command. This standard method of mesh generation can be somewhat time consuming and error prone for complex facet models with thousands of triangles. CUBIT also provides the option of using the facets themselves as a surface triangle mesh, or as the input to a tetrahedral mesher. This may be accomplished with one of two options:

Mesh <entity_list> From Facets

This command will generate triangular finite elements for each facet on the surface. If the entity_list is composed of one or more volumes, then the tetrahedral mesh will automatically fill the interior. This method is useful when further cleanup and smoothing operations are needed on the triangles after import.

Import Facets <filename> Make_elements

The make_elements on the import facets command will generate the triangular finite elements on the surface at the time the facets are read and created. This option is useful if no further modifications to the facets are necessary.

Creating triangular finite elements in this manner can greatly speed up the mesh generation process, however it is limited to non-manifold topology. If the triangular elements are to be used for tetrahedral meshing (i.e. all edges of the triangulation should be connected to no more than two triangles)

Mesh-Based geometry models and their mesh may be exported by one of the following methods:

Exporting to an Exodus II file saves the finite element mesh along with any boundary conditions placed on the model. It will not save the individual facets that comprise the mesh-based geometry surface representation. Importing an Exodus II file saved in this manner will regenerate the surfaces only to the resolution of the saved mesh.

CUBIT also provides the option to save just the surface representation to a facet or STL file. The following commands can be used for saving facet or STL files:

Export Facets 'filename' <entity_list> [Overwrite]

Export STL [ASCII|Binary] 'filename' <entity_list> [Overwrite]

These commands provide the option of saving specific surfaces or volumes to the facet file. If no entities are provided in the command, then all surfaces in the model will be exported to the file. The overwrite option forces a file to overwrite any file of the same name in the current working directory.

---

## Metadata Attributes

**URL:** https://coreform.com/cubit_help/geometry/metadata/metatdata_attributes.htm

**Contents:**
- Metadata Attributes
- Part and Assembly Metadata Attributes
- Viewing Part and Assembly Metadata Attribute Values
- Modifying Metadata Attributes
- Viewing and Modifying Global Metadata

Each part and assembly has several attributes, including its name and description. In addition, there are several attributes which do not describe any particular part or assembly. The “global” attributes describe the assembly tree as a whole, or the metadata as a whole.

These sections describe how to view and edit metadata attributes.

Each part and assembly has several attributes. Some attributes apply to both parts and assemblies, while other attributes apply to only parts. The attributes are listed in the following table:

Attribute Description

Name of Part or Assembly

Description of Part or Assembly

The name of the file containing the original version of this entity. Often a reference to a PDM system.

The unit system of this part or assembly.

The name or description of the material of which this part is composed.

Material_Specification

The formal specification number of the material of which this part is composed.

The density of the material of which this part is composed. Setting it to a non-positive value will clear the attribute, as if there were no value assigned.

The volume of the region enclosed by this part. The material_volume is not calculated from the volumes associated with the part. It will often differ from the actual volume enclosed by this part's associated geometric volumes, and can also be manually set to any non-negative value. Setting it to a non-positive value will clear the attribute, as if there were no value assigned.

Elemental_Composition

A string value describing the composition of the material, typically expressed as percentages of given elements.

The easiest way to view a part or assembly’s metadata attribute values is to select the item in the entity tree. The item’s metadata attributes are listed in the property page.

A part or assembly’s metadata attribute values can also be viewed using the Metadata List command:

Metadata List [<attribute_name>] {Part|Assembly} “<path>”

The attribute_name should be one of the attribute names in the table above. If no attribute name is included in the command, all metadata attributes are listed.

Metadata attributes can also be listed based on a volume.

Metadata List [<attribute_name>] Volume <id>

This volume-based command works just like the part-based command, but lists the metadata for the part with which the volume is associated.

A part or assembly’s metadata attributes can be modified in the property page. Simply select the part or assembly in the entity tree, then click in the appropriate text field in the property page.

A part or assembly’s metadata attributes can also be modified using the Metadata Modify command:

Metadata Modify <attribute> “new value” {Part|Assembly} “<path>”

where attribute is one of the attributes listed in the table above. The specified attribute value will be changed to new_value.

There is also a volume-based version of the Metadata Modify command:

Metadata Modify <attribute> “new_value” Volume <id>

The volume-based command works just like the part-based command, operating on the part with which the volume is associated. Note that if the specified volume is not associated with a part, a new part will be created and associated with the volume.

There are several attributes which do not describe any particular part or assembly. These “global” attributes describe the metadata as a whole:

The level of sensitivity of the metadata. Usually one of the following:

Classification_Category

The classification category. Usually one of the following:

Sigma 1 through Sigma 15

Global metadata values can be viewed using the Metadata List command:

Metadata List <attribute_name>

Global metadata values can be modified using the Metadata Modify command:

Metadata Modify <attribute_name> “new_value”

For both commands, attribute_name should be one of the attribute names in the table above.

---

## Move Command

**URL:** https://coreform.com/cubit_help/geometry/transforms/move.htm

**Contents:**
- Move Command
- Moving Other Geometric Entities
- Moving Bodies Relative to Other Geometric Entities
- Moving Merged Entities
- Move Undo

The move command moves a body, volume, free surface, free curve or free vertex by a specified offset. The command syntax is:

Vertex <id_range> [Move [X <dx>] [Y <dy>] [Z <dz>]] [Copy] [Preview]

Vertex <id_range> Move <direction_options< [Distance <val>] [Copy] [Preview]

{Body|Volume|Surface|Curve|Vertex|Group} <id_range> [Move [X <dx>] [Y <dy>] [Z <dz>]] [Copy [Nomesh]] [Preview]

{Body|Volume|Surface|Curve|Vertex|Group} <id_range> Move <direction_options> [Distance <val>] [Copy [Nomesh]] [Preview]

where <dx> <dy> <dz> and <distance> represent relative offsets in the major axis directions. If the copy option is specified, a copy is made and the copy is moved by the specified offset. The nomesh option will copy and move only the geometry.

These forms of the Move command will only work on free surfaces and free curves. To move a curve or surface that is part of a higher-order entity, the Move {entity} ... command is used.

It is also possible to move bodies by specifying one of its child entities. For example, a body can by moved by specifying one of its curves. However, if a lower-order entity is moved, the parent body and all related entities will also be moved. The commands for moving bodies using a child entity are given below. Alternatively, the tweak command can be used to move curves and surfaces without moving the parent body.

Move {Vertex|Curve|Surface|Volume|Body|Group} <id_range> [Midpoint] Location <x> [<y> [<z>]] [Include_Merged] [Preview]

Move {Vertex|Curve|Surface|Volume|Body|Group} <id_range> Location [Midpoint] [X <val>] [Y <val>] [Z <val>] [Except [X] [Y] [Z]] [Include_Merged] [Preview]

Move {Vertex|Curve|Surface|Volume|Body|Group} <id_range> Normal to Surface <id> Distance <val> [Include_Merged] [Preview]

Move {Vertex|Curve|Surface|Volume|Body|Group} <id_range> [Midpoint] General Location <location_options> [Except [X] [Y] [Z]] [Include_Merged] [Preview]

The first form of the command will move the entity to an absolute location. If moving a group, the centroid of the group is moved to that location. The second form will move the entity by a relative distance in any of the xyz axis directions. "Except" is used to preserve the x, y, or z plane in which the center of the entity lies. The third form of the command will move the body along an axis defined by the outward-facing surface normal of another surface. The fourth form of the command uses general location parsing to move the entity.

It is also possible to move bodies relative to other geometric entities in the model. The following command takes as arguments two geometric entities. The first entity is the one to move. The second entity is where it will be moved. In both cases, the midpoints of the specified entity are used to determine the distance and direction of the move. In the case of groups, centroids are used. "Except" is used to preserve the x, y, or z plane in which the center of the entity lies.

Move {Vertex|Curve|Surface|Volume|Body|Group} <id_range> [Midpoint] Location {Vertex|Curve|Surface|Volume|Body|Group} <id> [Midpoint] [Except [X] [Y] [Z]] [Include_Merged] [Preview]

The easiest way to move merged entities is by adding the include_merged keyword to the command. All entities that are merged with the specified entities will move together.

The only other way that merged entities can be moved is by including each of the merged entities in the entity list.

The Undo option allows a user to reverse the most recent move. This command will only work for the Move {entity} commands, and not the {Entity} Move commands. The syntax is:

---

## Partitioned Curves

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/partitioned_geometry/partition_curve.htm

**Contents:**
- Partitioned Curves

There are four methods for specifying locations at which to partition curves:

Partition Create Curve <curve_id> {Fraction <fraction_list> | Position <xpos> <ypos> <zpos> | [with] <vertex_list> | <node_list> }

The first two forms of the command create additional vertices and use those vertices to split a curve. The third form of the command uses existing vertices to split the curve. The fourth form of the command uses existing nodes to split the curve.

Using the fraction option, vertices are created at the specified fractions along the curve (in the range [0,1].) Subsequently, the curve is split at each vertex, resulting in n+1 new curves, where n is the number of fraction values specified.

Using the position option, vertices are created at the closest location along the curve to each of the specified position. Subsequently, the curve is split at each vertex, resulting in n+1 new curves, where n is the number of positions specified.

If the node option is used, meshed curves may be partitioned. The specified nodes must lie on the curve to be partitioned. The curve is split at each node specified, and any other mesh entities are divided appropriately amongst the curve partitions.

---

## Partitioned Geometry

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/partitioned_geometry/partitioned_geometry.htm

**Contents:**
- Partitioned Geometry

Partitioning provides a method to introduce additional topology into the model, to better constrain meshing algorithms. This is accomplished by splitting, or partitioning, existing curves or surfaces.

---

## Partitioned Surfaces

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/partitioned_geometry/partition_surface.htm

**Contents:**
- Partitioned Surfaces
- Partitioning with Vertices and Nodes
  - Partitioning with Hard Points
  - Partitioning with Polylines
- Partitioning with Curves
- Partitioning with Mesh Edges
- Partitioning with Faces or Triangles

There are several forms of the command to partition a surface. A surface may be partitioned using hard points, curves, polylines, mesh edges, mesh faces or mesh triangles.

There are two methods of partitioning a surface using vertices and nodes. The first method is to create a set of hard points using nodes, vertices, or coordinates that constrain the mesh to particular points on the surface. The syntax is:

Partition Create Surface <id> Vertex <id_list> [Individual]

Partition Create Surface <id> Node <id_list> [Individual]

The second method is to define a polyline using a set of vertices or coordinates. This method splits the surface using a polyline defined by the a list of positions specified as either coordinate triples, or existing vertices. The polyline is projected to the surface to define the curve for splitting the surface. If only one position is specified a zero-length curve with a single vertex will be created The syntax is identical to above WITHOUT the individual option.

Partition Create Surface <id> Vertex <id_list>

Partition Create Surface <id> Position <x> <y> <z> [[Position] <x> <y> <z> ...]

In the following simple example, the surface is partitioned using both methods. On the left half of the object, the surface is partitioned using the individual option (vertices 11 12 15 13). On the right half, a polyline is used (vertices 9 10 16 14). All of the free vertices can then be deleted, leaving the virtual curves shown in the second picture. Vertices 19 20 21 and 22 are all zero-length curves. The small 'v' in parentheses is to indicate that it is virtual geometry. The resulting mesh is shown in the third picture. Notice that the polyline constrains the entire curve to the mesh, while the hardpoints constrain only that individual point.

Figure 1. Partitioning a Surface Using Vertices

This form of the command splits the existing surface into several surfaces by creating curves that approximate the projection of the specified existing curves onto the surface. The syntax is:

Partition Create Surface <id> Curve <id_list>

Meshed surfaces may be partitioned with mesh edges. The specified mesh edges must be owned by the surface to be partitioned. The shape of the curve(s) used to split the surface is specified by a set of mesh edges.

If the split location is specified by a series of mesh edges, and the specified mesh edges form a closed loop, the node option may be used to control which node the vertex is created at.

Partition Create Surface <id> Edge <id_list> [Node <node_id>]

Surfaces may also be partitioned by specifying a list of triangles or faces (quads). The boundary of the list will automatically be detected and new curves and vertices created at the appropriate locations. Curves are created from the mesh edges and used to split the surface. The surface mesh is split and assigned to the appropriate surface partitions.

Partition Create Surface <id> Face|Tri <id_list>

---

## Partitioned Volumes

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/partitioned_geometry/partition_volume.htm

**Contents:**
- Partitioned Volumes

To partition a volume by giving a center and radius:

Partition Create Volume <id> Center [Location] {options} Radius <val>

This command splits the existing volume into two volumes. All volume elements that lie within the specified radius of the specified center location are identified, and the exterior faces of these elements are used to create a surface and partition the volume. The center can be specified with any of the location options.

Figure 1 shows an example of a partitioned volume. A cube that has been map meshed is partitioned using a center at one of its vertices. The result is two distinct volumes with a surface separating the two. The interface surface is composed of the faces of the interior hex elements.

Figure 1. A partitioned volume

This command may be useful for separating small regions of a meshed volume so that remeshing or mesh improvement may be performed locally.

---

## Parts, Assemblies, and Metadata

**URL:** https://coreform.com/cubit_help/geometry/metadata/geometry_metatdata.htm

**Contents:**
- Parts, Assemblies, and Metadata
- Overview of Parts, Assemblies and Metadata

A geometric model may be organized into a hierarchy of assemblies, sub-assemblies, and parts. These parts and assemblies can be assigned certain attribute values. The parts, assemblies, and associated attributes are referred to as DART Metadata, or simply metadata. Metadata can be imported from files, or can be created within CUBIT. Metadata can be exported to both mesh and geometry files.

Although useful in its own right, the primary purpose of CUBIT’s metadata capabilities is to enable interoperability with the set of applications participating in the DART project (see the Sandia Analysis Workbench Wiki page at https://dart.sandia.gov/wiki/display/SAW/DartMetadataPlugin). DART interoperability enables CUBIT to preserve assembly relationships and material data through the analysis process.

This section describes the procedures for importing, manipulating and exporting metadata within CUBIT.

---

## Persistent Attributes

**URL:** https://coreform.com/cubit_help/geometry/attributes/persistent_attributes/persistent_attributes.htm

**Contents:**
- Persistent Attributes

Typical data assigned to topological entities during a meshing session might include intervals, mesh schemes, group assignments, etc. By default, most of this data is lost between CUBIT sessions, and must be restored using the original CUBIT commands. Using CUBIT's persistent attributes capability, some of this data can be saved with the solid model and restored automatically when the model is imported into CUBIT.

---

## Propagated Groups

**URL:** https://coreform.com/cubit_help/geometry/groups/propagated_groups.htm

**Contents:**
- Propagated Groups

Creating propagated groups is a mechanism for joining groups of elements that meet specific criteria. For hex groups it might be grouping hexes from a hex mesh using sweep-type criteria. For surface elements, it might be grouping faces or tris into sidesets based on angle criteria.

---

## Propagated Hex Groups

**URL:** https://coreform.com/cubit_help/geometry/groups/propagated_hex_groups.htm

**Contents:**
- Propagated Hex Groups
- Propagated Hex Group Starting on a Surface
  - Ending at a Surface
  - Number of Times
  - Ending at a Surface with Multiple
  - Number of Times with Multiple
  - Ending at Surface with Direction
  - Number of Times with Direction
- Propagated Hex Group Starting on a Face
  - Ending at a Surface

Note: the first examples below are based on first executing these commands:

brick width 10 volume 1 size 1 mesh volume 1

Starting on a surface can end at a surface or can end after the number of times the user specifies.

Group ['name' | <id>] Add Hex Propagate Surface <id> Target Surface <id>

group 2 add hex propagate surface 1 target surface 2

Group ['name' | <id>] Add Hex Propagate Surface <id> Times <number>

group 2 add hex propagate surface 1 times 4

Result: Group 2 will be created containing 400 hexes.

Both methods, ending at surface or number of times, can be used with the "multiple" option which will create several groups depending upon the multiple number specified.

Group ['name' | <id>] Add Hex Propagate Surface <id> Target Surface <id> Multiple <number>

group 2 add hex propagate surface 1 target surface 2 multiple 2

Group ['name' | <id>] Add Hex Propagate Surface <id> Times <number> Multiple <number>

group 2 add hex propagate surface 1 times 10 multiple 5

Result: Two groups will be created and stored with their respective ids of multiple 5, these two groups will be stored in the parent group, Group 3, and Group 3 will be stored in the grand parent group, Group 2.

If number of times is specified and the direction is ambiguous, the surface direction or the node direction can be specified to direct the propagation. If the end surface is specified, only a node direction can be specified to direct the propagation. When specifying the node direction, the node has to be picked such that when the hexes are propagated, the picked node lies in these propagated hexes. If that node is never reached while propagating, the direction is not found and zero hexes will be included in the specified group.

Note: for the examples below, the result can be seen by executing these commands:

brick x 10 vol 1 size 1 brick width 10 body 2 move 10 volume all size 1 merge all mesh volume all

Group ['name' | <id>] Add Hex Propagate Surface <id> Times <number> Direction Node <id>

group 2 add hex propagate surface 6 target surface 12 direction node 1530

Note: The direction command and the multiple command can be combined (i.e. group 2 add propagate surface 6 times 4 multiple 2 direction node 1530)

Group ['name' | <id>] Add Hex Propagate Surface <id> Times <number> Direction [surface <id> | node <id>]

group 2 add hex propagate surface 6 times 4 direction surface 4

group 2 add hex propagate surface 6 times 4 direction node 1530

Result: group 2 will be created containing 400 hexes.

When starting on a face, the propagation method can end at a surface, end at a face or can end after the number of times the user specifies:

Group ['name' | <id>] Add Hex Propagate [Source] Face <id range> Target Surface <id>

group 2 add hex propagate face 1 11 21 target surface 2

Group ['name' | <id>] Add Hex Propagate [Source] Face <id> Target Face <id>

group 2 add hex propagate face 1 target face 1721

Note: Ending at a face requires starting at one face at one time, but ending at surface allows multiple start faces

Group ['name' | <id>] Add Hex Propagate [Source] Face <id range> Times <number>

group 2 add hex propagate face 2 times 4

Result: Group 2 will be created containing 4 propagated hexes (4 layers of 1 hex)

All of these methods, ending at surface, end at a face or number of times, can be used with the "multiple" option which will create a grandparent (top-level), parent (mid-level, contained within the grandparent) and child (bottom level, contained within the parent) groups. The child groups will contain each hex layer (specified number of layers per child group), all organized into a single parent group, which is organized underneath the group ID given to the command. Subsequent propagation commands could then be executed adding to the grandparent group, but creating a new parent and child groups. This way multiple propagation "sets" can be stored in one grandparent group, if desired.

Group ['name' | <id>] Add Hex Propagate [Source] Face <id> Target Surface <id> Multiple <number>

group 2 add hex propagate face 1 target surface 2 multiple 1

Group ['name' | <id>] Add Hex Propagate [Source] Face <id> Target Surface <id> Multiple <number>

group 2 add hex propagate face 1 target face 1721 multiple 1

Group ['name' | <id>] Add Hex Propagate [Source] Face <id> Times <number> Multiple <number>

group 2 add hex propagate face 1 times 10 multiple

Result: Two groups will be created and stored with their respective ids, these two groups will be stored in the parent group, Group 3, and Group 3 will be stored in the grand parent group, Group 2.

If the end surface or end face is ambiguous, a node direction can be specified to direct the propagation. When specify the node direction, the node has to be picked such that when the hexes are propagated, the picked node lies in these propagated hexes. If that node is never reached while propagating, the direction is not found and zero hexes will be included in the specified group.

Group ['name' | <id>] Add Hex Propagate [source] Face <id> Target Face <id> Direction Node <id>

group 2 add hex propagate face 1721 target face 1 direction node334

Group ['name' | <id>] Add Hex Propagate [Source] Face <id range> Target Surface <id> Direction Node <id>

group 2 add hex propagate face 1 target surface 2 direction node 334

Note: The direction command and the multiple command can be used together (i.e. group 2 add propagate face 1721 end face 1 multiple 2 direction node 334)

If number of times is specified and the direction is ambiguous, a surface direction or a node direction can be specified to direct the propagation. The node direction has the same condition as when ending at a surface or face and that is it must lie in the propagated hexes.

Group ['name' | <id>] Add Hex Propagate [Source] Face <id> Times <number>Direction [surface <id> | node <id>]

group 2 add hex propagate face 110 times 4 direction surface 2

group 2 add hex propagate face 1 times 4 direction node 269

Result: group 2 will be created contained 4 hexes

Note: The direction command and the multiple command can be used together. (i.e. group 2 add propagate face 1721 times 4 multiple 2 direction surface 1)

A special naming convention can be used for the propagated hex groups, best described by an example.

The following command will create a hierarchy of logically named groups, as follows.

group 'W1P1T1' add propagate surf 1 end surf 2 multiple 1

The hierarchy looks like this:

Where W1P1 is contained within W1, and W1P1T1, W1P1T2, etc., are contained within W1P1.

The software simply looks for numerical numbers in the group name and parses out the correct grandparent, parent and child names from the substrings. There must be exactly 3 substrings in the group name, each ending with an integer for the command to work properly.

A subsequent command:

group 'W1P2T1' add propagate surf 3 end surf 5 multiple 1

will add a parent group to W1, called W1P2, and the subsequent child groups, resulting in the following hierarchy:

---

## Reduce Bolt Core

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_bolt_core.htm

**Contents:**
- Reduce Bolt Core
  - Optional Arguments
  - Examples

The Reduce Bolt command is intended to prepare a volume identified as a bolt for analysis by simplifying its geometry, fitting to overlapping geometry, creating blocks and groups, etc. For the core option of the reduce command, a cylindrical geometry surrounding the bolt will be webcut from the surrounding geometry. The core geometry is often used to define a higher resolution hex mesh than the surrounding geometry to better capture potential failure conditions. The core option can also manage corresponding "insert" volumes surrounding the shaft of the bolt. The reduce bolt core command is similar to the reduce bolt fit_volume command except that the core option adds the ability to define a core region surrounding the bolt.

Figure 1. Example before and after of the Reduce Bolt Core command

Reduce volume {<ids>} bolt core [insert volume {<ids>}] [c1 <value>] [c2 <value>] [c3 <value>] [diameter {<value>|auto}] [align_axis] [tight_fit] [adjust_hole_diameter] [simplify_hole] [remove_key] [merge] [webcut [{Head|Shank|BOTH}]] [mesh] [mesh_size <value>] [bolt_block_id {<value>|Default}] [bolt_block_name {<string>|Default}] [increment_bolt_block_id] [head_block_id {<value>|Default}] [head_block_name {<string>|Default}] [increment_head_block_id] [shank_block_id {<value>|Default}] [shank_block_name {<string>|Default}] [increment_shank_block_id] [plug_block_id {<value>|Default}] [plug_block_name {<string>|Default}] [increment_plug_block_id] [insert_block_id {<value>|Default}] [insert_block_name {<string>|Default}] [increment_insert_block_id] [core_top_block_id {<value>|Default}] [core_top_block_name {<string>|Default}] [increment_bolt_core_top_id] [core_bottom_block_id {<value>|Default}] [core_bottom_block_name {<string>|Default}] [increment_core_bottom_block_id] [preview]

The dimensions of the core geometry are defined relative to the bolt that it surrounds. Two core volumes are normally generated where the cylindrical core geometry is subtracted from the top and bottom volumes as illustrated in figure 1. In addition to generating the core volumes, the bolt can be automatically webcut into three parts: head, shank and plug. If an insert volume is present, it can be automatically modified to remove overlap and merged to the shank and hole surfaces. In addition the diameter of the bolt shank can be altered, the hole fit to the shank diameter and the the allen key cavity optionally removed. The resulting volumes can in turn be hex meshed and assigned to blocks.

An example of the reduce bolt core operation is illustrated in figures 2 and 3. In this example, an "insert" volume is present that is overlapping the hole geometry. The resulting geometry from the operation is shown in figure 3.

Figure 2. Bolt and insert geometry prior to reduce bolt core operation showing nearby volumes.

Figure 3. Bolt, insert and core volumes after the reduce operation

The reduce bolt core operation also provides the option to assign the resulting volumes to blocks and mesh the volumes at a specified size. Figure 4 illustrates the resulting default blocks and mesh denerated from the example shown in figure 3.

Figure 4. Example blocks and mesh automatically generated from the Reduce Bolt Core command

The following outlines the options for the reduce bolt fit_volume command.

volume ids: Specify the ids of the volumes to be reduced. The Geometry Power Tool classification diagnosic can be used for identifying volumes as "bolts".

insert {volume <ids>}: An insert is a cylindrical shaped volume which may be surrounding the shaft of the bolt. The top of the insert is usually flush with the lower volume (light grey volume in figure 1). When using the insert option with the ID of the insert volume, the reduce command will automatically simplify the insert geometry, removing any fillets, rounds or small features on the insert. Any overlap or gap between the shaft and surrounding geometry will be removed so that the insert will fit flush with the shaft and bolt hole. The tight_fit and adjust_hole_diameter options cannot be used when including an insert. If the insert option is not used, any existing insert geometry that may be present at the bolt shaft will be ignored.

c1 <value>, c2 <value>, c3 <value>: Dimensions relative to the bolt defining the size of the core geometry as illustrated in Figure 1.

diameter {<value>|auto}: Use the diameter option to alter the diameter of the bolt shank to a specific diameter indicated by <value>. The auto option will change the diameter of the bolt to exactly match the diameter of its hole. If the diameter option is not used, the existing diameter of the bolt will be used.

align_axis: Use this option if the center line of the bolt does not exactly match its hole center line. This option will automatically transform and rotate the bolt volume so that the center line of the hole and bolt are aligned and the bolt head is in contact with the upper volume.

tight_fit: This option is normally used when the bolt shaft is overlapping the lower geometry as shown in figure 2. The tight_fit option will perform a boolean subtract operation to ensure that the bolt exactly fits the shaft geometry to the lower volume, removing any gaps and overlaps surrounding or below the bolt. Figure 3 shows the result of the tight_fit option. This option cannot be used if an insert volume is also specified. See figure 4. for an example illustrating the tight_fit option.

adjust_hole_diameter: This option is normally used to adjust the diameter of the surrounding hole to match that of the bolt shaft, removing any gap or overlap. In contrast to the tight_fit option, only the hole diameter is tweaked without removing any existing void space below the bolt. This option cannot be used if an insert volume is also specified. See figure 4 for an example illustrating the the adjust_hole_diameter option.

simplify_hole: Bolt holes can sometimes include a fillet at the lip of the hole and/or a conical shape indentation at its base. The simplify_hole option will automatically remove these features from the hole leaving a flat base and sharp corner at the lip. Simplify_hole is usually used with the adjust_hole_diameter to ensure the shank fits flush with the hole surfaces and the hole is simplified. Simplify_hole has no effect on the lower volume if the tight_fit option is used. It can however simplify the upper volume if it contains any fillets or chamfers at its lip.

remove_key: The bolt geometry can often include a hexagonal shaped hole at the top of the bolt that fits an allen key. By default, this key hole will not be removed. Including the remove_key will ensure this hole is removed from the bolt geometry. If the mesh option is used, a hex mesh can be generated in most cases either with or without the key removed. Hex meshing will most likely be unsuccessful if the diameter of the key hole exceeds that of the bolt shaft. As a consequence, remove_key option may be necessary to facilitate meshing.

webcut [{Head|Shank|BOTH}]: The bolt can be cut into up to 3 different volumes as shown in figure 1. Using the optional Head or Shank options a single webcut can be executed separating just the head from the shank or just the shank from the plug respectively. If no arguments are used to the webcut option, or the both option is used, both webcuts will be performed resulting in three volumes. The location of the webcut on the shank will be where the bolt exits the lower volume.

merge: When the merge option is used. the plug portion of the bolt will be imprinted and merged with the hole surface(s) in the lower volume. In addition, the plug, shaft and head will be merged together. If an insert volume is specified, the exterior insert surface will be imprinted and merged with the hole surface(s) and the bolt plug will be imprinted and merged with the interior surface(s) of the insert. If the merge option is not used, all volumes created from the reduce command will not be imprinted or merged.

mesh: This option will attempt to generate a swept mesh on the bolt and insert geometries as part of the reduce command. If the allen key hole is present in the bolt head, a webcut will be performed on the bolt geometry to facilitate meshing. If meshing is unsuccessful, consider using the remove_key option.

mesh_size <value>: Specifies the mesh size to be used with the mesh option. If not specified, an automatic size will be determined.

Block ID and name assignment:When the webcut option is used, the resulting volumes may be assigned to a block. The following options may be used to assign to blocks based on an ID or a block name:

If webcut is not used, the resulting reduced bolt volume may still be assigned to a block id using either the bolt_block_id {<value>|Default} or bolt_block_name {<string>|Default} options.

Each of the block ID specifications for bolt, plug, shaft and head also have a corresponding optional increment argument. When assigning new webcut volumes to blocks, the block ID can be automatically generated by incrementing from a specified block_id. For example, if head_block_id is defined as 100, and the increment_head_block_ids option is used, each new head volume generated will be assigned to a new unique block id starting with 100, followed by 101, 102, 103, etc.

If an insert volume is specified, insert_block_id, insert_block_name and increment_insert_block_id may also be used in a similar manner to set up block information on the insert volume.

preview: optional argument to display a preview of the reduce bolt fit_volume operation without execution of the reduction. This option will display the reduced bolt geometry in blue with the surrounding volumes displayed in wireframe.

The following figures illustrate variations on the core option for the reduce bolt command.

reduce volume 2 bolt core insert volume 1 c1 0.936345 c2 0.936345 c3 3.4749 simplify_hole remove_key merge

reduce volume 2 bolt core c1 1 c2 1 c3 4 diameter 2 adjust_hole_diameter simplify_hole remove_key webcut merge

reduce volume 2 bolt core insert volume 1 c1 1 c2 1 c3 4 diameter 2 simplify_hole remove_key webcut merge mesh mesh_size 0.3 head_block_ID 10 shank_block_ID 20 plug_block_ID 30 insert_block_ID 40 core_top_block_ID 50 core_bottom_block_ID 60

Figure 5. Examples of using the reduce bolt core command where (a) is the original geometry. In (b), an insert volume is included and the dimensions of the core are specified. Figure (c) does not include the insert and modifies the dimensions of core using the c1, c2 and c3 options. In addition, the diameter of the bolt shaft has been modified from its original diameter and the bolt cut into head, shank and plug volumes. Figure (d) again includes the insert and also specifies a mesh and custom mesh size to be used. In addition, note that block IDs for each of the resulting volumes have been specified. The resulting block IDs are also illustrated in figure (d).

---

## Reduce Bolt Fit_Volume

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_bolt_fit.htm

**Contents:**
- Reduce Bolt Fit_Volume
  - Optional Arguments
  - Examples

The Reduce Bolt command is intended to prepare a volume identified as a bolt for analysis by simplifying its geometry, fitting to overlapping geometry, creating blocks and groups, etc. The fit_volume option can also modify the surrounding hole geometry or optional insert which may be at the bolt shaft. In addition to simplifying the bolt and insert geometry, this operation can remove any overlap and fit the shaft geometry to its surrounding volume or insert. See also the reduce bolt core option which adds the ability to generate a core region surrounding the bolt.

Figure 1. Example before and after of the Reduce Bolt Fit_Volume command. Also shows optional insert geometry at the bolt shaft.

Reduce {volume <ids>} bolt fit_volume [insert {volume <ids>}] [diameter {<value>|auto}] [align_axis] [tight_fit] [adjust_hole_diameter] [simplify_hole] [remove_key] [merge] [webcut [{Head|Shank|BOTH}]] [mesh] [mesh_size <value>] [bolt_block_id {<value>|Default}] [increment_bolt_block_id] [bolt_block_name {<string>|Default}] [head_block_id {<value>|Default}] [increment_head_block_id] [head_block_name {<string>|Default}] [shank_block_id {<value>|Default}] [increment_shank_block_id] [shank_block_name {<string>|Default}] [plug_block_id {<value>|Default}] [increment_plug_block_id] [plug_block_name {<string>|Default}] [insert_block_id {<value>|Default}] [increment_insert_block_id] [insert_block_name {<string>|Default}] [preview]

CAD representations of a bolt assembly can often define overlapping volumetric regions or leave gaps between the bolt and its surrounding geometry. It may also include an optional insert, a cylindrical part surrounding the bolt shaft which can also overlap the bolt and surrounding geometry. The fit_volume option is intended to manage this overlap or gap by adjusting the hole or insert diameter and/or removing void space below the bolt.

In addition to removing overlap or gap, the bolt can be automatically webcut into three parts: head, shank and plug as shown in figure 1. The resulting webcut volumes can in turn be assigned to blocks and the diameter of the shank can be altered. The plug can also be merged or contiguously meshed with the fastened geometry.

The following outlines the options for the reduce bolt fit_volume command.

volume ids: Specify the ids of the volumes to be reduced. The Geometry Power Tool classification diagnosic can be used for identifying volumes as "bolts".

insert {volume <ids>}: An insert is a cylindrical shaped volume which may be surrounding the shaft of the bolt. The top of the insert is usually flush with the lower volume (light grey volume in figure 1). When using the insert option with the ID of the insert volume, the reduce command will automatically simplify the insert geometry, removing any fillets, rounds or small features on the insert. Any overlap or gap between the shaft and surrounding geometry will be removed so that the insert will fit flush with the shaft and bolt hole. The tight_fit and adjust_hole_diameter options cannot be used when including an insert. If the insert option is not used, any existing insert geometry that may be present at the bolt shaft will be ignored.

diameter {<value>|auto}: Use the diameter option to alter the diameter of the bolt shank to a specific diameter indicated by <value>. The auto option will change the diameter of the bolt to exactly match the diameter of its hole. If the diameter option is not used, the existing diameter of the bolt will be used.

Figure 2. Bolt geometry prior to reduce operation showing nearby volumes.

Figure 3. Bolt after reduce operation using fit_volume, webcut and block assignment options.

align_axis: Use this option if the center line of the bolt does not exactly match its hole center line. This option will automatically transform and rotate the bolt volume so that the center line of the hole and bolt are aligned and the bolt head is in contact with the upper volume.

tight_fit: This option is normally used when the bolt shaft is overlapping the lower geometry as shown in figure 2. The tight_fit option will perform a boolean subtract operation to ensure that the bolt exactly fits the shaft geometry to the lower volume, removing any gaps and overlaps surrounding or below the bolt. Figure 3 shows the result of the tight_fit option. This option cannot be used if an insert volume is also specified. See figure 4. for an example illustrating the tight_fit option.

adjust_hole_diameter: This option is normally used to adjust the diameter of the surrounding hole to match that of the bolt shaft, removing any gap or overlap. In contrast to the tight_fit option, only the hole diameter is tweaked without removing any existing void space below the bolt. This option cannot be used if an insert volume is also specified. See figure 4 for an example illustrating the the adjust_hole_diameter option.

simplify_hole: Bolt holes can sometimes include a fillet at the lip of the hole and/or a conical shape indentation at its base. The simplify_hole option will automatically remove these features from the hole leaving a flat base and sharp corner at the lip. Simplify_hole is usually used with the adjust_hole_diameter to ensure the shank fits flush with the hole surfaces and the hole is simplified. Simplify_hole has no effect on the lower volume if the tight_fit option is used. It can however simplify the upper volume if it contains any fillets or chamfers at its lip.

remove_key: The bolt geometry can often include a hexagonal shaped hole at the top of the bolt that fits an allen key. By default, this key hole will not be removed. Including the remove_key will ensure this hole is removed from the bolt geometry. If the mesh option is used, a hex mesh can be generated in most cases either with or without the key removed. Hex meshing will most likely be unsuccessful if the diameter of the key hole exceeds that of the bolt shaft. As a consequence, remove_key option may be necessary to facilitate meshing.

webcut [{Head|Shank|BOTH}]: The bolt can be cut into up to 3 different volumes as shown in figure 1. Using the optional Head or Shank options a single webcut can be executed separating just the head from the shank or just the shank from the plug respectively. If no arguments are used to the webcut option, or the both option is used, both webcuts will be performed resulting in three volumes. The location of the webcut on the shank will be where the bolt exits the lower volume.

merge: When the merge option is used. the plug portion of the bolt will be imprinted and merged with the hole surface(s) in the lower volume. In addition, the plug, shaft and head will be merged together. If an insert volume is specified, the exterior insert surface will be imprinted and merged with the hole surface(s) and the bolt plug will be imprinted and merged with the interior surface(s) of the insert. If the merge option is not used, all volumes created from the reduce command will not be imprinted or merged.

mesh: This option will attempt to generate a swept mesh on the bolt and insert geometries as part of the reduce command. If the allen key hole is present in the bolt head, a webcut will be performed on the bolt geometry to facilitate meshing. If meshing is unsuccessful, consider using the remove_key option.

mesh_size <value>: Specifies the mesh size to be used with the mesh option. If not specified, an automatic size will be determined.

Block ID and name assignment:When the webcut option is used, the resulting volumes may be assigned to a block. The following options may be used to assign to blocks based on an ID or a block name:

If webcut is not used, the resulting reduced bolt volume may still be assigned to a block id using either the bolt_block_id {<value>|Default} or bolt_block_name {<string>|Default} options.

Each of the block ID specifications for bolt, plug, shaft and head also have a corresponding optional increment argument. When assigning new webcut volumes to blocks, the block ID can be automatically generated by incrementing from a specified block_id. For example, if head_block_id is defined as 100, and the increment_head_block_ids option is used, each new head volume generated will be assigned to a new unique block id starting with 100, followed by 101, 102, 103, etc.

If an insert volume is specified, insert_block_id, insert_block_name and increment_insert_block_id may also be used in a similar manner to set up block information on the insert volume.

preview: optional argument to display a preview of the reduce bolt fit_volume operation without execution of the reduction. This option will display the reduced bolt geometry in blue with the surrounding volumes displayed in wireframe.

The following figures illustrate variations on the fit_volume option for the reduce bolt command. The original CAD geometry is pictured on the left with results on the right.

reduce volume 2 bolt fit_volume adjust_hole_diameter simplify_hole remove_key merge

reduce volume 2 bolt fit_volume tight_fit remove_key merge

reduce volume 2 bolt fit_volume remove_key adjust_hole_diameter simplify_hole webcut merge

reduce volume 2 bolt fit_volume remove_key adjust_hole_diameter simplify_hole webcut merge mesh

Figure 4. Example of four different variations of syntax for the reduce bolt fit_volume command on a single bolt. In this case, the bolt (volume 2) overlaps the cyan colored lower volume. Note the difference between the adjust_hole in figures (b), (d) and (e) and tight_fit (c) options. In both cases, volume overlap is removed, however adjust_hole_diameter only adjusts the hole diameter to match the bolt shaft, but tight_fit also removes any void space below the bolt. Also note in figure (d), three separate volumes are created from the bolt geometry when the webcut option is used. In figure (e), the bolt has been meshed with default sizing using Cubit's sweep tool

reduce volume 1, 2 bolt fit adjust_hole_diameter simplify_hole remove_key webcut merge mesh head_block_ID 10 increment_head_block_ID shank_block_ID 20 increment_shank_block_ID plug_block_ID 30

Figure 5. Example of using the reduce bolt fit_volume command to reduce multiple bolts with a single command while specifying blocks. In this case the block IDs are specified for head, shank and plug volumes. Note that the increment_head_block_ID and increment_shank_block_ID options are used, but the increment_plug_block_ID option is not. The result is that the block IDs on the heads (block 10, 11) and shanks (blocks 20, 21) are incremented with each new bolt, while the block defined on all plugs will remain the same (block 30) without incrementing.

reduce volume 2 bolt fit_volume insert volume 1 simplify_hole webcut merge mesh

Figure 6. Example of using the reduce bolt fit_volume command with the insert option. In this case, volume 1 is specified as the insert and volume 2 is the bolt. Note that both the bolt and insert volumes have been simplified and the insert volume imprinted and merged with both the hole surfaces and the bolt plug.

---

## Reduce Bolt Patch

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_bolt_patch.htm

**Contents:**
- Reduce Bolt Patch
  - Optional Arguments
  - Sideset Naming Convention
    - Default Naming Format:
    - Naming Examples:
    - Alternative Naming Format:
    - Naming Examples:
      - Overriding the Default:
  - Export Patch Data Command
    - Command Options and Arguments

The Reduce Bolt command generates a proxy representation of a bolt for analysis. It replaces the bolt geometry with two concentric circular surfaces centered on the bolt axis, separating the connected volumes where sidesets are automatically applied.

Figure 1. Example of the Reduce Bolt Patch command. The Shigley frustum is used to calculate the diameter of the sidesets positioned between the volumes.

reduce {volume <ids>|upper surface <ids> lower surface <ids>} {bolt|hole} patch [contact upper {surface <ids>}] [contact lower {surface <ids>}] [radius {<value>|Factor <value>|SHIGLEY [angle {<value>}] [grip {AUTO|bolt|washer}]}] [mesh] [mesh_size <value>] [mesh_scheme <string>] [no_simplify_hole] [{FILL|no_fill}] [{DELETE|no_delete}] [array_name <string>] [sideset_naming_convention <value>] [upper_patch_sideset_id {<value>|Default}] [increment_upper_patch_sideset_id] [start_upper_sideset_id {<value>|Default}] [upper_patch_sideset_name {<string>|Default}] [lower_patch_sideset_id {<value>|Default}] [increment_lower_patch_sideset_id] [start_lower_sideset_id {<value>|Default}] [lower_patch_sideset_name {<string>|Default}] [name_patch_surfaces] [preview]

Figure 2. Example of before and after where the reduce bolt patch command has been applied to two bolts. This example uses the mesh and default fill and delete options.

The following outlines the options for the reduce bolt patch command.

You can input either the ID of the bolt to be reduced or the IDs of holes intended for fasteners if no bolt volume is present. Choose between the bolt or hole options based on your specific needs.

volume <ids>: Specify the ids of the volumes to be reduced. The Geometry Power Tool classification diagnosic can be used for identifying volumes as "bolts".

upper surface <ids> lower surface <ids>: Specify hole IDs for fastener reduction, including at least one surface from both upper and lower holes. Cubit checks axis alignment and matches multiple holes if specified. For more than two fastened volumes, Cubit supports up to three; designate the topmost with >upper surface and the rest with lower surface.

contact upper {surface <ids>} contact lower {surface <ids>}: In rare cases, the reduce patch command may not auto-identify upper and lower contact surfaces. If this occurs, you can manually specify these surfaces to resolve the issue. Note: This option is only available for a single bolt or hole set.

radius {<value>|Factor <value>|SHIGLEY [angle {<value>}] [grip {AUTO|bolt|washer}]}

radius <value>: The Reduce Bolt Patch command allows you to directly set the radius by specifying a floating-point value. Use this option to set an absolute value for the sideset radius on the contact surfaces. This value determines the radius of the resulting imprinted circle where the sideset is defined.

radius factor <value>: The radius factor option allows you to define the radius of the resulting imprinted circle as a multiple of the shank bolt’s radius. If no bolt is present and only the hole is specified, the radius will be a multiple of the upper hole’s radius.

radius shigley angle <value>: The radius shigley angle option is the default method for determining the radius. It employs a Shigley angle, as outlined in SAND2008-0371 (Figure 1). If no radius specification is provided, the Shigley angle defaults to 30 degrees to compute the radius. This radius is determined by the intersection of the frustum with the surface between the upper and lower volumes.

grip {AUTO|bolt|washer}: Use this option in combination with the SHIGLEY radius method. It specifies whether the Shigley cone calculation is based on the bolt head or the washer outer radius.

The circular patch size can vary based on several factors, such as the thickness of the upper volume, the radius of the bolt head, and the length of the bolt. For more comprehensive details, refer to SANDIA REPORT SAND2008-0371, “Guideline for Bolted Joint Design and Analysis: Version 1.0.”

Note: The radius shigley angle option is applicable only when a bolt is specified. If no bolt is present and only holes are specified, and no radius is given, the radius factor option becomes the default. In such cases, a default factor of 2.5 will be used to compute the radius.

The Reduce Bolt Patch command imprints concentric circular patches onto the surfaces of the upper and lower volumes. If the surfaces on the upper and lower volume do not extend beyond the specified radius, the resulting surfaces will be clipped accordingly.

mesh: Option to specify whether to include meshing as part of the command.

mesh_size <value>: Optionally specify a target mesh size when using the mesh

mesh_scheme <string>: Specify a target meshing scheme. The following meshing schemes can be used for this operation:

FILL|no_fill: The FILL|no_fill option controls hole treatment. By default setting, FILL removes the hole entirely, along with any features like fillets. The no_fill option retains the hole but simplifies it, removing fillets and creating an annulus centered on the hole's axis. The annulus diameter is set by one of the radius options.

no_simplify_hole: The reduce surface patch command, coupled with the no_fill option, is designed to streamline the meshing process by automatically eliminating chamfers, blends, and conical elements from hole geometries. However, the no_simplify_hole switch overrides this behavior, preserving all existing features of the hole's geometry. This can be particularly useful in scenarios where the default simplification process might lead to command failure due to complex hole configurations. Activating this option allows for the continuation of the operation without the standard simplification step.

Sideset IDs and name assignment: The following options may be used to assign the resulting circular surfaces based on an ID or a sideset name:

Optional increment and start_id arguments are available for both upper and lower sideset ID specifications. When used, these options automatically generate incrementing sideset IDs. For example, if lower_patch_sideset_id is set to 100 and increment_lower_patch_sideset_id is used, new bolt patches will have unique sideset IDs starting from 100 (e.g., 101, 102, 103). If both upper_patch_sideset_id and start_upper_sideset_id (or their lower counterparts) are used with increment, the new patches may be added to the existing sideset and a new, incrementing sideset, effectively adding the same patch to two different sidesets.

Default Naming: Sidesets are automatically named to reflect the connections between components. For instance, for clamped volumes with names "PartA" and "PartB" generates sideset names such as "PartA_to_PartB_123" and "PartB_to_PartA_123." These names encapsulate the parts involved and a unique identifier for the fastener's volume, "_123" in this case. In this example, the name "PartA_to_PartB_123" signifies the sideset on PartA that denotes its interface with PartB, and similarly, "PartB_to_PartA_123" is assigned to PartB to mark its connection with PartA. When blocks are designated and the clamped volumes are assigned, the naming convention defaults to using block names rather than volume names.

array_name + "_" + [NameA] + "_" + [NameB] + "_" + [Volume ID of Bolt]

where NameA designates the name of the volume or block the sideset is attached to and NameB designates the volume or block the sideset is in contact with.

If array_name is set to "Connect", the volume ID of the bolt is 3, and the clamped volume names are "PartA" and "PartB" the resulting sideset names for the resulting sidesets would be:

Alternative Default Naming: Activating the option with sideset_naming_convention set to 1 changes the naming scheme. Sidesets begin with a "Bolt_Patch" prefix (assuming no array_name is given), then add "_Lower" or "_Upper" to indicate their position relative to the bolt's bearing surface, and conclude with a numeric identifier for the bolt volume. This convention offers an alternative to the default, which is applied automatically without needing explicit selection.

array_name + "_" + [Volume ID of Bolt] + "_Upper/Lower"

If array_name is set to "Connect" and the volume ID of the bolt is 3, the resulting sideset names for the upper and lower portions would be:

This naming applies to surfaces as well when the name_patch_surfaces option is activated. In cases where a single bolt connects more than two volumes, the naming includes the individual connections. For example, a bolt fastening three volumes would yield names such as:

Here, the first number represents the index of the connection at the same bolt, and the second number is the volume ID of the bolt.

Be aware that these default naming conventions can be superseded by the explicit naming options, upper_patch_sideset_name and upper_patch_sideset_name, provided in the previous section of this documentation.

This section outlines the use of the export patch data command, which allows users to save or preview information derived from the reduce bolt patch process. This command facilitates the generation of data necessary for Morph input decks or simulation purposes, including the creation of a .csv file. Below is the detailed syntax for utilizing this command.

Export Patch Data <filename> [{csv|morph|BOTH}] [surface <ids>] [lower name <name>] [upper name <name>] [sideset_naming_convention <value>] [full] [overwrite]

Export Patch Data [surface <ids>] [lower name <name>] [upper name <name>] [sideset_naming_convention <value>] [full] preview

The command is available in two variations: one for writing the output to a file and another for previewing the morph patch data in the output window. Both variations require the prior use of the name_patch_surfaces option within the reduce bolt patch command to identify and process the surfaces correctly.

**Examples:**

Example 1 (unknown):
```unknown
array_name + "_" + [NameA] + "_" + [NameB] + "_"
  + [Volume ID of Bolt]
```

Example 2 (unknown):
```unknown
Connect_PartA_to_PartB_3
```

Example 3 (unknown):
```unknown
Connect_PartB_to_PartA_3
```

Example 4 (unknown):
```unknown
array_name + "_" + [Volume ID of Bolt] +
  "_Upper/Lower"
```

---

## Reduce Bolt Spider

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_bolt_spider.htm

**Contents:**
- Reduce Bolt Spider
  - Optional Arguments
  - Examples

The Reduce Bolt command is intended to prepare a volume identified as a bolt for analysis by replacing the bolt geometry with a set of mesh edges or beams and generating blocks containing the mesh. There are currently three different options for the spider command as illustrated in figures 1 to 3.

Figure 1. Example before and after of the Reduce Bolt Spider Wagon_Wheel command

Figure 2. Example before and after of the Reduce Bolt Spider J2G command

Figure 3. Example before and after of the Reduce Bolt Spider Countersink command

Reduce {volume <ids>|{upper surface <ids>lower surface <ids>}} bolt spider {wagon wheel|j2g|countersink} [diameter <value>] [mesh] [mesh_size] [spider_block_id {<value>|Default}] [spider_block_name {<string>|Default}] [increment_spider_block_id] [rebar_block_id {<value>|Default}] [rebar_block_name {<string>|Default}] [increment_spider_block_id] [upper_spider_block_id {|Default}] [increment_upper_spider_block_id] [upper_spider_block_name {|Default}] [lower_spider_block_id {|Default}] [increment_lower_spider_block_id] [lower_spider_block_name {|Default}] [preview] [preview]

The spider options will also simplify the surrounding geometry at a bolt hole, including removing any blends or chamfers. It will also simplify the hole so in the lower volume to which the bolt is fastened will fit exactly to the bolt geometry or specified diamater.

The spider options will not, by default, generate the beam mesh as shown in figures 1 to 3, but instead define blocks to which the beam elements will be added when the mesh is generated or the mesh option is used. The following describes the options for the reduce bolt spider command.

Bolt holes can be defined by specifing the cylindrical bolt volume or by specifying the upper and lower surfaces of the bolt holes. The latter is helpful if bolt volumes don't exist in the model but the holes do.

volume ids: Specify the ids of the volumes to be reduced. The Geometry Power Tool classification diagnosic can be used for identifying volumes as "bolts".

upper/lower bolt hole surface ids: Specify the upper and lower surfaces of the bolt hole. Multiple upper/lower pairs can be specified.

{wagon wheel|j2g|countersink}: One of these three methods must be specified for the spider option.

diameter <value>: Use the diameter option to alter the diameter of the resulting hole. If no value is specified for diameter, the existing diameter of the bolt will be used.

mesh: This option can be used to generate the beam mesh as part of the reduce operation. Since the resolution of the beam mesh depends on the nodes defined on the hole geometry, the surfaces of the hole will also be meshed using a mapped meshing scheme. Use the mesh_size option to control the resolution of the beam mesh. When the hole surfaces are meshed, the beam elements will also be generated and assigned to the existing spider and rebar blocks. Note that if the mesh option is not used, an empty spider and rebar block will be generated.

mesh_size: Use the mesh_size option to control the resolution of the beam mesh. If no mesh_size has been defined, if a mesh size has been defined on the bolt volume, it will be used, otherwise an automatic default size will be computed and used for meshing.

When building new blocks for each bolt volume, the block IDs can be automatically generated by incrementing from a specified block_id. The increment_spider_block_id and increment_rebar_block_id options are used for this prupose. For example, if rebar_block_id is defined as 100, and the increment_rebar_block_ids option is used, each new rebar generated will be assigned to a new unique block id starting with 100, followed by 101, 102, 103, etc.

Upper and lower portions of the resulting spider can be placed into separate blocks with the upper_spider_* and lower_spider_* options. (Default is to put the spider joint into a single block.) Names and ids of these upper and lower blocks can be controlled with *_upper_* and *_lower_* forms of the block name/id parameters detailed in the preceeding paragraph.

preview: optional argument to display a preview of the spider operation without execution of the reduction. This option will display the proposed beam mesh with the surrounding volumes displayed in wireframe.

The following figure illustrates the spider option for the reduce bolt command.

reduce volume 1 2 bolt spider J2G mesh mesh_size 3.0 spider_block_ID 10 increment_Spider_Block_ID rebar_block_ID 20

Figure 4. Examples of using the reduce bolt spider j2g command where (a) is the original geometry of two bolts overlapping the lower volume (cyan color). In (b), the spider j2g option has been used which replaces the bolts with a beam mesh. Note that the bolt hole has been modified to fit the shaft of the original bolts. In this case, the rebar blocks are comprised of the central nodes from which the beam elements radiate. Since the increment_rebar_block_id option is used, block 10 is defined where volume 1 existed and block 11 at volume 2. For the spider block, since the increment_spider_block_id was not used, all beam elements were placed into block 20. Note that since the mesh option was used, the hole surfaces were meshed and the spider block beam elements were generated. Otherwise, a subsequent mesh operation performed on the lower (cyan) volume would also generate the beam elements and assign them to their appropriate blocks.

---

## Reduce (Simplify)

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_bolt_simplify.htm

**Contents:**
- Reduce (Simplify)

The simplest form of the Reduce command. This option will simplify and defeature volumes without affecting the surrounding geometry.

Figure 1. Example before and after of the Reduce command

Reduce volume {<ids>} [preview]

The reduce command without additional options will perform simplification and defeaturing operations on the given volumes. This includes automatic chamfer, blend, cavity and small surface removal. While intended primarily for the bolt and fastener use case, it can also be useful for other volume types, however results may vary depending on complexity of the geometry.

volume ids: Specify the ids of the volumes to be reduced. The Geometry Power Tool classification diagnosic can be used for identifying volumes as "bolts".

preview: optional argument to display a preview of the reduce operation without execution of the reduction. This option will display the reduced volume in blue with the surrounding volumes displayed in wireframe.

---

## Reduce Slot Surface

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_slot.htm

**Contents:**
- Reduce Slot Surface

The Reduce Slot Surface is used to decompose slot surfaces in Electromagnetic (EM) modeling for easier application of boundary conditions.

Figure 1.Example preview of slot surfaces, shown in blue (right) constructed from the original geometry (left).

Reduce Surface <ids> slot [radius {<value>|Factor <value>|SHIGLEY [angle {<value>}]}] [inner {curve <ids>}] [outer {curve <ids>}] [hardware volume <ids>] [[create] skin] [group <string>] [group_edges <string>] [group_inner_edges <string>] [group_outer_edges <string>] [group_inner_surfaces <string>] [group_outer_surfaces <string>] [name <string>] [name_edges <string>] [name_inner_edges <string>] [name_outer_edges <string>] [name_inner_surfaces <string>] [name_outer_surfaces <string>] [make_free_curves] [preview]

The Reduce Surface Slot command is engineered for the preparation of models for electromagnetic (EM) simulations, facilitating the creation of slots—pathways allowing EM radiation to traverse. This command is versatile, designed for compatibility with both Cubit quad and tri meshers and the Morph mesher. It plays a vital role in generating surface meshes essential for EM simulations.

Prerequisites and Best Practices:

Before invoking the Reduce Surface Slot command, adhere to these best practices to ensure optimal model preparation:

Defeaturing and Simplification: Simplify the model by defeaturing or removing unnecessary details that may complicate splitting procedure in the reduce slot command.

Enclosure Integrity: Verify that the enclosure region is fully closed. Use the remove surface commands as necessary to seal any gaps or holes.

Imprint and Merge: For mismatched mating surfaces above and below the slot pathways, perform an imprint and merge operation to ensure that the upper and lower slot surfaces align perfectly.

Figure 2.Slot Preparation Workflow: Identification and division of slot surfaces via the reduce surface slot command. The images display the distinct meshing results with Cubit or Morph.

Common Steps for Cubit and Morph Workflows:

Adjust Options: Customize the command settings according to the provided command syntax description.

Invoke the Command: Execute the Reduce Surface Slot command to begin the process of defining and splitting the slot surfaces. It's also worth noting that achieving the desired outcome may require some trial and error, with a preview option available to visualize the slot pathways before finalizing.

For Cubit, the focus is on direct mesh generation:

Mesh Preparation: Unlike Morph, Cubit does not require specific naming of surfaces and curves for mesh generation.

Quad Meshes on Slot Surfaces: Explicitly generate quad meshes on the slot surfaces using Cubit commands for assigning intervals, setting schemes and meshing.

Tri Meshes for Remaining Surfaces: Apply tri meshers for the rest of the model, setting mesh size, scheme, and then meshing directly in Cubit.

For Morph, the emphasis is on preparing data for meshing in an external process:

Surface and Curve Naming: Important for Morph, where naming conventions are essential for the mesher to recognize and process the model correctly. Names can be explicitly identified in the command or the default naming convention may be used.

Export Patch Data: Utilize the export slot data command to provide Morph with the necessary information for quad and tri mesh generation.

Command Syntax Description:

hardware volume ids: Identifies the volumes of fasteners that intersect with the slot surface. The centroid of each fastener, as it appears on the slot surface, guides the determination of cut locations. This parameter is optional; in its absence, the command automatically seeks out holes, inferring potential fastener centroids based on the centers of these holes.

radius: Specifies the distance from the centers of fasteners on the slot surface to where cuts will be made. The radius can be defined using one of three methods:

group: Used to create and name a group containing all resulting decomposed surfaces. The options group_edges, group_inner_edges, group_outer_edges, group_inner_surfaces and group_outer_surfaces are used to create and name groups of cutting curves, inner curves, and outer curves, respectively.

name: Similar to the group option, but individual names are assigned to the resulting decomposed surfaces and curves. The names of decomposed surfaces, side curves, inner curves, outer curves, inner surfaces and outer surfaces can be defined using the respective options. If not specified, a default naming convention will be used. Note that these names will be used in the Morph input deck and can be written using the export slot data command

make_free_curves: A specialized option to generate free curves at the boundaries of the decomposed slot surfaces. Grouping and naming options also apply to the free curves.

create skin: This function constructs a sheet body through a lofting process that spans from inner to outer curves. It is applicable to any slot surface, offering significant utility when dealing with multiple surfaces that do not form coplanar paths. This feature is particularly valuable for defining surfaces for quad meshing, effectively outlining the electromagnetic (EM) pathway. An alternative to having this command create a skin surface is for the user to create a skin surface and tweaking nearby surfaces to match the skin surface. If done this way, the tweak operation will preserve any bolt holes, and a reduce surface slot operation can be performed afterwards.

preview: Displays a blue preview of the slot paths without performing the actual cutting operations as well as a wire frame outline of the owning volume

The Export Slot Data command is used to list or export the information required for a Morph input deck. It can either provide a preview in the output window or export the data to a text file if a filename is specified. This command assumes the use of default naming conventions. The syntax is as follows:

Export Slot Data [surface ] [full] [free_curves] [overwrite]

Export Slot Data [surface ] [full] [free_curves] preview

There are two different forms of the command. The first form exports the data to a file, while the second form provides a preview in the output window.

---

## Reduce Spring

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_spring.htm

**Contents:**
- Reduce Spring
  - Examples

The Reduce Spring command is intended to prepare a volume identified as a spring for analysis by creating one or more free curves that follow the spring's path at the middle of its cross-section. The new curve(s) can be meshed with beam elements and used in place of 3D elements to represent the spring.

Figure 1. Example before and after of the Reduce Spring command

Reduce Volume <ids> Spring [combine] [mesh [size {<value>}]] [keep] [block_id {<value>|Default}] [increment_block_id] [block_name {<string>|Default}] [preview]

volume ids: Specify the ids of the volumes to be reduced. The Geometry Power Tool classification diagnosic can be used for identifying volumes as "springs".

combine: By default, the curves resulting from the reduce spring command will be based upon the initial surface geometry of the spring. This may result in multiple curves of varying lengths connected by vertices. The combine option reduces the spring to a single free curve. This is helpful if the default operation would otherwise result in short curves that would produce unacceptable beam elements.

mesh: Use the mesh option to automatically mesh the resulting curve(s) with beam elements. The optional size argument can be used to specify a target length for the beam elements along the curve(s). If a size is not specified, an automatic size is assigned.

keep: Optionally retain the initial spring geometry after the reduce command is completed. If keep is not used, the spring volume will be deleted when a valid set of mid-curves has been produced.

Block ID and name assignment:When the block_id or block_name options are used, the resulting curves and mesh may be assigned to a block. The block may be defined by either a block_name or block_id. If the block does not yet exist, a new one will be created. The Default option will automatically select an id or name.

increment_block_id:When reducing multiple spring volumes in a single reduce command, it may be desirable to change the block ID assignment with each spring. When assigning new curves or beam elements to blocks, the block ID can be automatically generated by incrementing from a specified block_id. For example, if block_id is defined as 100, and the increment_block_ids option is used, each new set of mid-curves and their associated beam elements generated for a unique spring volume will be assigned to a new block id starting with 100. The next spring volume will be block 101, followed by 102, 103, etc.

The following figure illustrates the spring option for the reduce command.

reduce volume 1 spring combine mesh size 0.001 block_ID Default

Figure 2. Example of using the reduce spring command where (a) is the original geometry of a spring. In (b), the spring option has been used which in this case replaces the spring volume with a single free curve meshed with beam elements. A new block is generated and assigned the resulting curve and beam elements and the original spring geometry is deleted leaving only the free curves in place of the volume.

---

## Reduce Thin Volumes

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_thin_volumes.htm

**Contents:**
- Reduce Thin Volumes

The Reduce Thin Volumes commands simplifies a 3D thin volume into a connected set of sheet bodies. The reduce thin commands are frequently used with the intention of generating shell finite elements. Note that these commands will perform similar geometric operations to the surface copy and midsurface commands, but will also keep track of thickness and loft; attributes necessary for building a full representation for shell finite element analysis. The resulting sheet bodies will also automatically generate blocks with these attributes and will maintain their association to their original 3D parent geometry.

The Thin Auto version (illustrated in figure 1) automatically reduces a set of 3D thin volumes into a connected set of sheet bodies based on an internal geometric reasoning algorithm resulting in sheet bodies that are connected at shared (merged) curves. It will also automatically build thickness, loft and block information. The copy and midsurface versions of the command are more prescriptive, and offer more control so that specific required reductions can be performed. The copy option can be used to prescribe a few required reductions in an assembly prior to automatically reducing the remainder with the reduce thin auto command.

Figure 1. Reducing a set of 3D thin volumes. Merged curves are highlighed.

Reduce Volume <volume ids> Thin Auto [Sort] [Preview]

Reduce Volume <volume ids> Thin Copy <surface ids> loft factor <values> thickness <values>...[Combine] [Delete] [Preview]

Reduce Volume <volume id> Thin Midsurface surface <id1, id2> loft factor <value> thickness <value> [Combine] [Delete] [Preview]

To use the Thin Auto command, the 3D thin volumes must be touching so that if the user imprinted and merged them, they would be connected at merged surfaces. This routine traverses the set of 3D volumes, finding the best 2D reductions that preserve connections between the 3D volumes. This routine also creates shell element blocks containing the resulting 2D shell surfaces. Each block also is attributed with appropriate thickness and loft factor values corresponding to the parent 3D volumes. These thickness and loft factor values are the first and second block attributes respectively. Finally the command creates an internal association between the original 3D parent volume and the 2D reduction so that the user is able to visually inspect and validate the reduction. See the draw shell volume command below for more details.

volume ids: Specify the ids of the 3D volumes to be reduced. These volumes should not already be imprinted and merged. However, users should be certain that the volumes do indeed imprint and merge successfully since the routine does this internally to ultimately connect the resulting 2D shell surfaces. If a user wants to prescribe a specific reduction solution, it can be done manually using the Reduce Thin Copy command. To include the manually reduced volumes in the auto operation, the parent 3D volumes (not the generated 2D reductions) should be specified along with the other 3D volumes being reduced.

sort: If the sort option is specified, the surfaces of all 2D reductions containing the same base name will be added to the same block. This is done so that copies of the same volume remain together. These volumes should be identical in nature, with the same thickness. For example, if the user has a repeated part in the model with the base name 'bracket', all 2D reductions with that base name, like 'bracket@A', 'bracket@B', 'bracket@C',... will have all their surfaces added to the same block. If the sort option is not used, the surfaces of each 2D reduction will be in their own block. In either case, the next available block id is used.

It is also important to note that only 3D thin volumes that have two logical sides can be automatically reduced. For example, a piece of sheet metal, bent or pressed into most shapes has two logical sides. 3D thin volumes with t-junctions do not have two logical sides. See figure 2 below for some examples.

Figure 2. Logical sides of thin volumes.

Thin Copy and Midsurface

Using this form of the command, the user defines the reduction by specifying the surfaces the thin 3D volume will be reduced to. Unlike the auto form, nothing is done to make adjacent reductions contiguous. Each surface must be specified with a corresponding loft factor and thickness value. The combine option reduces a volume into a multi-surface sheet body. Otherwise, each surface will result in a single-surface sheet body. delete option deletes the original 3D thin volume(s).

Note that sheet bodies created using the \textbf{reduce thin midsurface} option, are currently not supported in the auto option. If the intention is to initially prescribe a few reductions prior to using the auto command, avoid using the midsurface command.

To visually inspect that the 2D reductions correctly approximate the original 3D thin volumes, the command below can be used. The 3D volume is drawn in wireframe mode, 2D reduction in shaded mode, and the element block of the 2D reduction in shaded or optionally transparent mode.

Draw Shell Volume <ids> [Color<color_spec>] [Transparent] [Add]

To export information to a csv file detailing the reductions, the command below can be used:

Export Shell Data <string> [Volume<ids>] [Brief] [Overwrite]

By default, the following columns are written for each 3D volume specified. If no volumes are specified, the data for all 3D thin volumes reduced are exported. For each 3D thin volume, the following columns of data are exported:

If the brief option is used, only the following columns of data are exported:

---

## Reduce Thin Volumes with Reinforcement Learning

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce_thin_rl.htm

**Contents:**
- Reduce Thin Volumes with Reinforcement Learning
- Syntax:
- Preparation
- Strategies
- Arguments

The Reduce Thin Volumes RL command, similar to the Reduce Thin Volumes Auto simplifies a 3D thin volume into a connected set of sheet bodies. The reduce thin volume commands are frequently used with the intention of generating shell finite elements. In contrast to the auto option, the RL option uses machine learning methods to build a persistent knowledge base to improve its choice of reduce operations. If an assembly has not yet been learned, the method may initially predict a relatively poor solution. As the RL method is run, it builds training data, effectively learning the most suitable reduce solutions for a given configuration of thin volumes. In general, the more diverse problems encountered, the better the outcomes of the RL predictions.

When generating a shell model of a 3D set of thin volumes, the user often must navigate many tools to reduce the volumes and then establish connections. The sequence of commands to build such a model, for anything other than a trivial case, can become unwieldy. Figures 1-3 show one such example where multiple different solutions can be generated for this simple idealized model of the thin volumes. It should be apparent that some solutions may be acceptable, while others are not. The RL tool assists in developing a knowledge base of assembly states and how best to resolve them when encountered.

The RL option can be used to generate a sequence of Cubit commands, which can be exported to a journal file. The user can then validate the result, edit and annotate the journal for archival purposes. The commands generated for reduction will be of the form reduce thin copy or reduce thin midsurface. Note that these commands will perform similar geometric operations to the surface copy and midsurface commands, but will also keep track of thickness and loft; attributes necessary for building a full representation for shell finite element analysis. The resulting sheet bodies will also automatically generate blocks with these attributes and will maintain their association to their original 3D parent geometry.

Reduce Volume <volume ids> Thin RL [Number Iterations <value>] [Initialize Random [<value>]] [Stopping Criteria <value>] [Learning Interval <value>] [Journal Result <string>] [Delete] [Preview]

Similar to the Reduce Thin Auto, to use the Reduce Thin RL command, for best results, the 3D thin volumes should be touching so that if the user imprinted and merged them, they would be connected at merged surfaces. This may involve using checking for gaps and overlaps and resolving prior to using this tool. Some cleanup and defeaturing of the volumes may also be necessary, such as removing chamfers, rounds or other small features that may not be relevant to the final FEA model.

Predict Mode: This mode is normally used when sufficient training data has been established. By setting the argument Number Iterations = 1, the RL method will build the sequence of reduce commands based on predictions made from the existing training data.

Learning Mode: This is normally used when working with a new assembly that may be significantly different than previous models encountered. The user will typically run the RL methods for multiple iterations (Number Iterations > 1), allowing the method to gather information about the state space of the assembly. Depending on the complexity of the assembly, this may take anywhere from a few minutes to several hours to gather sufficient data. At each iteration, a single average reward value is computed and displayed at the command line that represents the completeness of the resulting solution. This value is a heuristic measurement of how well the resulting sheet bodies connect as well as other factors including potential introduction of small curves and narrow surfaces.

To operate in learning mode, RL will use various measures to determine when to terminate learning:

User Influenced Learning: The RL tool provides an ideal method for efficiently establishing a lot of training data in a short amount of time. The learning, however is built on internal predefined heuristics that generally apply to most assembly states. The user can over-ride these preferences by adding their own training data. The most convenient way to do that is through the Cubit Geometry Power Tool, using the Thin Volumes diagnostic. This diagnostic will display the current predicted confidence value for a given reduce command in the solution window. This can be influenced by the user by using the maximize or minimize confidence right-click options. These options are also available from the Cubit command line using the Learn series of commands.

Number Iterations <value>: Maximum number of RL iterations to perform before termination. Default is 100.

Initialize Random {<value>}: Used to initialize the state to random reduce solutions. Normally the state is initialized by predicting the best solution based on the current training data. Random initialization can be used for maximum exploration of the state space, and is most useful for models that have not been seen before. It can also be used to experiment with known solutions to see if alternative solutions can be derived. The options <value> is a seed that can be used to guide the internal random number generator.

For maximum exploration of the state space in learning mode, the Initialize Random may also used. Normally, the starting point for the RL method will be a prediction based on the current knowledge base (training data). The Initialize Random options, ignores any current

Stopping Criteria <value>: A value between zero and one. The RL method terminates if the average reward meets or exceed this value. Default value is 0.999.

Learning Interval <value>: Integer value that indicates how often to update the machine learning model. For example, a learning interval of 5 will update the training model with information it has learned at every fifth RL iteration. Following the update, the state rewards will be reinitialized based on predictions from the ML model to begin the next iteration. Default for learning interval is 100. If the default is used, normally the ML model is only updated after the final iteration.

Journal Result "<string>": If a filename is provided using this option, a journal file with that name will be written to the current working directory with the resulting sequence of commands from the best RL iteration. The resulting journal file will be annotated with comments indicating reward values and success or failure of connections.

Delete: Parent volumes will be deleted after the sheet bodies have been generated. This is generally not recommended as the association between 3D solid thin volumes and their resulting child sheet body(s) is maintained behind the scenes in Cubit. Visualization and management of sheet data, such as block attributes is maintained through this association, as well as the Export Shell Data command.

Preview: If the preview option is used, the final best solution will not be executed, but rather a graphical preview of the result will be displayed. The preview will also include visual cues for connections that have been maintained and those that do not. In addition, if the journal result is used, the journal file will also be produced. This option is often used to preview and validate the result, prior to running the resulting journal once the solution is established as acceptable.

---

## Reducing Geometry

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/reduce/reduce.htm

**Contents:**
- Reducing Geometry

The reduce options provide automatic defeaturing and simplification solutions for specific classes of geometry. These options are most often used as methods for rapidly modifying geometry representing fasteners and springs to representations that can be readily used in analysis. For example, the CAD representation of a bolt may include threads, fillets, chamfers, cavities and may also overlap surrounding geometry. The reduce option can automatically defeature, webcut and modify surrounding geometry as well as mesh and apply boundary conditions according to a designated recipe. A limited number of reduce recipes are currently supported for bolts, including the following:

The reduce command is often used in conjunction with the Geometry Power tool and the machine learning classification methods. The classification tool can group volumes according to commonly recognized shapes such as bolt, nut, washer, spring, etc.

---

## Reflect Command

**URL:** https://coreform.com/cubit_help/geometry/transforms/reflect.htm

**Contents:**
- Reflect Command

The reflect command mirrors the body about a plane normal to the vector supplied. The reflect command will destroy the existing body and replace it with the new reflected body, unless the copy option is used.

{Body|Volume|Surface|Curve|Vertex|Group} <range> [Copy] Reflect <x-comp> <y-comp> <z-comp>

{Body|Volume|Surface|Curve|Vertex|Group} <range> [Copy] Reflect {X|Y|Z}

---

## Regularizing Geometry

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/regularizing.htm

**Contents:**
- Regularizing Geometry

The regularize command removes unnecessary topology, which in effect reverses the imprint operation. This can help clean up the model from extra features that are unnecessary for the geometric definition of the model. The following command regularizes the model:

Regularize Body|Group|Volume|Surface|Curve|Vertex <range>[keep {curve <ids>|vertex <ids>}]

The keep option allows the user to specify curves and vertices that should not be removed during the regulairze operation.

If you are frequently using web-cutting or other boolean operations to decompose your geometry, it may be convenient to always generate regularized geometry. To set creation of regularized geometry during boolean operations use the following command:

Set Boolean Regularize [ON | off]

---

## Removing Curves

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/removing_geometric_features/removing_curves.htm

**Contents:**
- Removing Curves

At times you may find that you have an extraneous sliver/short curves in your model. The following command detects curves having a length less than the supplied lengthlimit in the specified bodies or volumes and replaces them with vertices. If no lenghtlimit is specified, a default value of 0.001 is used.

Remove Sliver Curve {Body|Volume} <id_range> [lengthlimit <double>] [Exclude Curve <id_range>]

It is recommended that curves approaching the size of features in the model not be remove with this command, only those substantially smaller, so as to preserve model integrity. For larger curves, try regularizing or compositing. The Exclude Curve option prevents specified curves from getting removed. Lengthlimit default = 0.001.

---

## Removing Geometric Features

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/removing_geometric_features/removing_geometric_features.htm

**Contents:**
- Removing Geometric Features

Cubit has the ability to remove surfaces, curves, and vertices in an effort to simplify the model for meshing. For example, surface removal extends adjacent surfaces to those being removed to fill in the gap where the removed surfaces were. Curve removal replaces a short, sliver curves with a vertex. And vertex removal can be facilitated with tweaking if it is connect to two curves of the same geometric type.

---

## Removing Partitions

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/partitioned_geometry/removing_partitions.htm

**Contents:**
- Removing Partitions

There are two commands used to remove partitions:

Partition Merge {Curve|Surface|Volume} <id_list>

The command combines existing partitions where possible. This command is similar to the composite create command. The difference is that this command is special-cased for partitions, and will result in more efficient geometric evaluations. If all the partitions of a real solid model entity are merged, such that there is only one partition remaining, the virtual geometry will be removed, and the original solid model geometry will be restored to the model.

The CUBIT delete command can also be used for removing partitions. See Deleting Virtual Geometry for a description of its use.

---

## Removing Surfaces

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/removing_geometric_features/removing_surfaces.htm

**Contents:**
- Removing Surfaces
- Remove Sliver Surface

The remove surface command removes surfaces from bodies. By default, it attempts to extend the adjoining surfaces to fill the resultant gap. This is a useful way to remove fillets and rounds and other features such as bosses not needed for analysis. See Figure 1 for an example of this process. The syntax for this command is:

Remove Surface <id_range> [Blend_Chain] [Cavity] [EXTEND|Noextend] [Keepsurface] [Keep] [TOGETHER|Individual|connected_sets]

The noextend qualifier prevents the adjoining surfaces from being extended, leaving a gap in the body. This is sometimes useful for repairing bad geometry - the surface can be rebuilt with surface from curves or a net surface, etc.., then combined back onto the body.

The keep option will retain the original body and put the results of the remove surface in a new body. The keepsurface option will retain the surface which was removed.

By default, the TOGETHER option removes the surfaces in a single call to the solid modeler. The individual option will remove surfaces one-by-one instead of as a group. If one removal fails, the rest are still attempted. Without the individual option, no surface is removed unless they are all able to be removed together. The connected_sets option sorts the surfaces into sets of connected surfaces, operating on each set separately, allowing the remove operation to succeed on some sets if it fails on others.

The blend_chain option will not only remove the selected surface but will also remove any surfaces belonging to the same blend chain. A blend is a non-planar surface such as a fillet that has a constant radius of curvature in at least one of its principal parametric directions. The blend chain includes all connected surfaces that share a common radius of curvature.

The cavity option can be used to remove all surfaces defining a hole or cavity. A cavity is defined as the collection of surfaces bounded by curves where the exterior angle is greater than 180 degrees. Designating the cavity option will automatically include all surfaces that are part of the cavity to which the surface belongs. If the surface does not belong to a cavity, this option will be ignored.

This command is identical to the Tweak Surface Remove command.

Figure 1. Remove Surface Example

This command uses the ACIS remove surface capability on surfaces that have area less than a specified area limit. When ACIS removes a surface it extends the adjoining surfaces and intersects them to fill the gap. If it is not possible to extend the surfaces or if the geometry is bad the command will fail. The syntax for this command is:

Remove Slivers Body <id_range> [EXTEND|Noextend] [Keepsurface] [Keep] [Arealimit <double>] [Exclude Surface <id_range>]

Default Arealimit = 0.1

The noextend, keepsurface and keep options operate as for the remove surface command. The arealimit option allows the user to set the area below which surfaces will be removed. The Exclude Surface option prevents specified surfaces from getting removed.

ACIS can also convert a very thin, skinny surface into a tolerant (thick) curve, replacing the thin surface. If the width (in the thin direction) of the surface is less than lengthlimit the surface will be converted into a tolerant curve.

Remove Sliver Body <id_range> [Lengthlimit <double>] [Exclude Surface <id_range>]

It is recommended a surface with width approaching the size of small features not be removed with this commmand. The Exclude Surface option prevents specified surfaces from getting removed. Lengthlimit default = 0.001.

---

## Removing Vertices

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/removing_geometric_features/removing_vertices.htm

**Contents:**
- Removing Vertices

At times you may find that you have an extraneous vertex in your model. This would be a vertex connected to two and only two curves. This stray vertex can cause unwanted mesh artifacts, due to the fact that a mesh node MUST lie on this vertex, thereby disallowing the possibility of movement for better quality. Fortunately there is a relatively easy way of getting rid of this stray vertex using the tweak surface command.

Tweak Surface <id> Replace With Surface <same_id>

Note that you are replacing a surface with itself. In doing so, the geometry engine will do an intersection check on that surface, and should realize that the vertex doesn't need to be there.

---

## Rotate Command

**URL:** https://coreform.com/cubit_help/geometry/transforms/rotate.htm

**Contents:**
- Rotate Command
- Rotating Merged Entities

The rotate command rotates a body about a given axis without adding any new geometry. If the Angle or any Components are not specified they are defaulted to be zero. The commands to rotate a body or bodies are:

Body <range> [Copy] Rotate <angle> About {X|Y|Z} [Preview]

Body <range> [Copy] Rotate <angle> About <x-comp> <y-comp> <z-comp> [Preview]

Rotate {Body|Volume|Surface|Curve|Vertex|Group} <id_range> about {X|Y|Z|<xval> <yval> <zval>} Angle <val> [Include_Merged] [Preview]

Rotate {Body|Volume|Surface|Curve|Vertex|Group} <id_range> About Vertex <id> Vertex <id> Angle <val> [Include_Merged] [Preview]

Rotate {Body|Volume|Surface|Curve|Vertex|Group} <id_range> About Normal of Surface <id> Angle <val> [Include_Merged] [Preview]

Rotate {Body|Volume|Surface|Curve|Vertex|Group} <id_range> About Origin <xval> <yval> <zval> Direction <xval> <yval> <zval> Angle <val> [Include_Merged] [Preview]

If the copy option is specified, a copy is made and rotated the specified amount.

The easiest way to rotate merged entities is by adding the include_merged keyword to the command. All entities that are merged with the specified entities will rotate together.

The only other way that merged entities can be rotated is by including each of the merged entities in the entity list.

---

## Scale Command

**URL:** https://coreform.com/cubit_help/geometry/transforms/scale.htm

**Contents:**
- Scale Command

The scale command resizes an entity (body, volume, surface, or curve) by a scaling factor. The scaling factor may be a constant, or may differ in the x, y, and z directions. The entity chosen will be scaled about the point or vertex indicated. If no point or vertex is entered, it will be scaled about the origin. Any mesh on the object will be scaled too, unless the nomesh keyword is used.

The command to scale entities is:

{Body|Volume|Surface|Curve} <id_range> Scale {<scale> | x <val> y <val> z <val>} [About {<x> <y> <z> | Vertex <id>}] [Nomesh] [Copy [Repeat <value>] [Group_Results]] [Preview]

If the copy option is specified, a copy of the entity is made and scaled the specified amount. Use the repeat option to create multiple copies.

---

## Section Command

**URL:** https://coreform.com/cubit_help/geometry/decomposition/section.htm

**Contents:**
- Section Command

This command will cut a body or group of bodies with a plane, keeping geometry on one side of the plane and discarding the rest. The syntax for this command is:

Section {Body|Group} <id_range> [With] {Xplane|Yplane|Zplane} [Offset <value>] [NORMAL|Reverse] [Keep]

Section {Body|Group} <id_range> With Surface <id> [NORMAL|Reverse] [Keep]

In the first form, the specified coordinate plane is used to cut the specified bodies. The offset option is used to specify an offset from the coordinate plane. In the second form, an existing (planar) surface is used to section the model. In either case, the reverse keyword results in discarding the positive side of the specified plane or surface instead of the other side. The keep option results in keeping both sides; the section command used with this option is equivalent to webcutting with a plane.

---

## Seeded Mesh Groups

**URL:** https://coreform.com/cubit_help/geometry/groups/seed.htm

**Contents:**
- Seeded Mesh Groups

It is also possible to automatically group surface mesh elements based on feature angles. Given a seed element, the algorithm will loop over all adjacent elements and create groups of elements whose surface normals are similar, or which fall within a certain radius. The command syntax is:

Group {<'name'>|<id>} {Add|Equals|Remove|Xor} Seed <mesh_entities> {Feature_angle <angle> [Divergence]|Depth <number>}

The seed element may be a quad, tri, or node element. There are two methods of angle comparison for this command. The feature angle option will compare angles of the each element to its adjacent elements by comparing surface normals. In the case of nodes, the seed node surface normal will be the average of the adjacent faces or tris. Nodes will be added if their attached faces meet the angle requirements. The divergence option will compare angles to the original seed element's surface normal. The depth option will add elements within a certain radius.

The following figures illustrate the use of the seed method to create mesh groups using the feature angle and divergence methods.

CUBIT> group 'mygroup1' add seed face 269 feature_angle 45

CUBIT> group 'mygroup2' add seed face 269 feature_angle 45 divergence

The seed method of creating groups is particularly useful for creating groups on free meshes for the purpose of assigning nodesets and sidesets.

The GUI command panel for this command is found by selecting

"Mode-Meshing", "Entity-Group", "Action-Manage Groups", then "Create with Seed." The command panel is shown below:

---

## Separating Multi-Volume Bodies

**URL:** https://coreform.com/cubit_help/geometry/decomposition/separating_multi_volume_bodies.htm

**Contents:**
- Separating Multi-Volume Bodies

The separate and split commands are used to separate a body with multiple volumes into a multiple bodies with single volumes. The commands are:

Separate {Body|Volume} <id_range|all>

Split {Body|Volume} <id_range|all>

Only very rarely will either of these commands be needed. They are provided for the occasional instance that a multi-volume body is found. These commands are interchangeable.

Another related command allows the user to control the separation of bodies after webcutting. In most instances the user will want to separate bodies after webcutting. One reason to possibly have this option turned off is to be able to keep track of all the volumes during a webcut. Setting this option to "off" keeps all volumes in the same body. But the more common approach is to name the original body and allow naming to keep track of volumes. This setting is on by default. The syntax is:

Set Separate After Webcut [ON|Off]

---

## Separating Surfaces from Bodies

**URL:** https://coreform.com/cubit_help/geometry/decomposition/separate_surface.htm

**Contents:**
- Separating Surfaces from Bodies

The separate surface command is used to separate a surface from a sheet body or a solid body. The command is:

Separate Surface <range>

Separating a surface from a solid body will create a "hole" in the solid body. Thus the solid body will become a sheet body. The newly separated surface will be also sheet body, but it will have a different id. Multiple surfaces can be separated from a body at the same time, but each separated surface will result in a distinct sheet body, as if the command had been performed on each surface individually.

---

## Simplify Geometry

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/simplify.htm

**Contents:**
- Simplify Geometry
- Feature Angle
- Automatically Compositing Curves
- Respecting Vertices, Curves and Surfaces
- Respecting Imprints
- Other Options

Simplifying topology by compositing individually selected surfaces is often a tedious and time-consuming task. The simplify command addresses the tedium by automatically compositing surfaces and curves based on selected criteria between neighboring entities. Figure 1 shows a typical example of simplify command usage (‘simplify volume 1 angle 15’).

Figure 1. Typical Simplify command usage

The command syntax and discussion items are shown below.

Simplify {Volume|Surface|Curve} <range> [Angle< value >] [Respect {Surface <id_range> | Curve <id_range> | Vertex <id_range>| Imprint | Fillet}] [Preview]

Feature angle is defined as the angle between the normals of adjacent surfaces at the shared curve. At each facet point along the curve, a normal is computed for each surfaces. If at any point the angle between the two normals is greater than the feature_angle, the surfaces are not composited. If all angles between normals are less than feature_angle, the two surfaces are composited (assuming any other specified criteria are met). Feature angle is always used as the criteria and if an angle is not specified the value is set to 15 degrees.

Figure 2. Feature Angle

The simplify command can also be used to automatically composite curves using an angle tolerance. Curves will be composited together only if they are explicitly specified in this command, and not as the result of two surfaces being composited.

Surfaces, curves, and vertices can be specified to prevent geometry features from automatically being composited. Figure 2 show an example of respecting a surface (‘simplify vol 1 angle 15 respect surf 289’).

Figure 3. Respecting a surface

For complex geometries, it is often useful to preview the simplify command and then add any respected geometry to the command respect lists.

Curves created by imprints can automatically be respected by the simplify command. Figure 3 shows an example of geometry with split fillets.

Figure 4. Respecting imprint geometry

Notice that in the split curves are respected by the Simplify command (‘simplify vol 1 angle 40 respect imprint’).

The preview option shows what curves are respected without compositing any surfaces. It should also be pointed out that multiple respect specifications can be chained together. For example:

Simplify volume 1 angle 15 respect curve 1 respect imprint respect fillet preview

---

## Specifying Solver-Specific Element Types

**URL:** https://coreform.com/cubit_help/finite_element_model/export/solver_specific_elem.htm

**Contents:**
- Specifying Solver-Specific Element Types

CUBIT allows the user to specify solver specific element types on export. This can provide better automation of processes by averting the need to hand edit files to change element types. CUBIT typically exports predefined element types for each solver. The solver_element command overrides those predefined types. The command syntax is as follows: [create] solver_element <solver string> <new element string> from <exodus element string> block <ids> solver_element <solver string> <new element string> from <exodus element string> list [block <ids>] solver_element [<solver string>] For example, a user creating an axisymmetric model for Abaqus might want to specify that Exodus QUAD elements should be replaced by CGAX4H on export. The commands: block 1 element type quad create solver_element "abaqus" "CGAX4H" from "QUAD" creates a global mapping for all QUAD elements in the model on export not just the elements in block 1. The block version of the command creates the mapping for a specific block rather than globally. For example, the commands: block 2 edge 2 block 2 element type bar2 block 2 solver_element "abaqus" "SPRINGA" from "bar2" will replace the default B21 element type with SPRINGA for bar elements in block 2. Note: This command currently only supports Abaqus export.

CUBIT typically exports predefined element types for each solver. The solver_element command overrides those predefined types. The command syntax is as follows:

[create] solver_element <solver string> <new element string> from <exodus element string>

block <ids> solver_element <solver string> <new element string> from <exodus element string>

list [block <ids>] solver_element [<solver string>]

For example, a user creating an axisymmetric model for Abaqus might want to specify that Exodus QUAD elements should be replaced by CGAX4H on export. The commands:

block 1 element type quad create solver_element "abaqus" "CGAX4H" from "QUAD"

creates a global mapping for all QUAD elements in the model on export not just the elements in block 1.

The block version of the command creates the mapping for a specific block rather than globally. For example, the commands:

block 2 edge 2 block 2 element type bar2 block 2 solver_element "abaqus" "SPRINGA" from "bar2" will replace the default B21 element type with SPRINGA for bar elements in block 2. Note: This command currently only supports Abaqus export.

Note: This command currently only supports Abaqus export.

---

## Splitting Geometry

**URL:** https://coreform.com/cubit_help/geometry/decomposition/splitting_geometry/splitting_geometry.htm

**Contents:**
- Splitting Geometry

The Split command divides curves or surfaces into multiple entities. The command results are similar to imprinting. However, vertex and/or curve creation is not necessary for the split command.

---

## Split Curve

**URL:** https://coreform.com/cubit_help/geometry/decomposition/splitting_geometry/split_curve.htm

**Contents:**
- Split Curve

The Split Curve command will split a curve without the need for geometry creation (unlike imprinting). The syntax is shown below.

Split Curve <id> [location on curve options] [Merge] [Preview]

To split a curve, simply specify a location or a location on curve (see location specification). Using the Preview keyword will draw the splitting location on the curve. The Merge keyword will merge any topology that contains the newly created vertex.

---

## Split Periodic Surfaces

**URL:** https://coreform.com/cubit_help/geometry/decomposition/splitting_geometry/split_periodic.htm

**Contents:**
- Split Periodic Surfaces

Solids which contain periodic surfaces include cylinders, torii and spheres. Splitting periodic surfaces can in some cases simplify meshing, and will result in curves and surfaces being added to the volume. The command used to split periodic surfaces is:

Split Periodic Body <id_range|all>

This command splits all periodic surfaces in a body or bodies.

---

## Split Surface

**URL:** https://coreform.com/cubit_help/geometry/decomposition/splitting_geometry/split_surface.htm

**Contents:**
- Split Surface
- Split Across
- Split Extend
- Split (Automatically)
- Split Skew

The Split Surface command divides one or more surfaces into multiple surfaces. The command results are similar to imprint with curve. However, curve creation is not necessary for splitting surfaces. Three primary forms of the command are available.

The first form splits a single surface using locations while the second splits by extending a surface hard-line until it hits a surface boundary. The split automatic splits either a single surface or a chain of surfaces in an automatic fashion.

Two forms of Split Across are available:

Split Surface <id> Across [Pair] Location <options multiple locs> [Preview [Create]]

Split Surface <id> Across Location <multiple locs> Onto Curve <id> [Preview] Create]]

This command splits a surface with a spline projection through multiple locations on the surface. See Location, Direction, and Axis Specification for a detailed description of the location specifier. Figure 1 shows a simple example of splitting a single surface into two surfaces. A temporary spline was created through the three specified locations (Vertex 5 6 7), and this curve was used to split the surface.

split surface 1 across location vertex 5 6 7

Figure 1 - Splitting Across with Multiple Locations

The Pair keyword will pair locations to create multiple surface splitting curves (each defined with two locations). An even number of input locations is required. Figure 2 shows an example:

split surface 1 across pair vertex 5 7 6 8

Figure 2 - Splitting Across with Pair Option

The Preview keyword will show a graphics preview of the splitting curve. If the Create keyword is also specified, a free curve (or curves) will be created - these are the internal curves that are used to imprint the surfaces.

The Onto Curve format of the command takes one or more locations on one side of the surface and projects them onto a single curve on the other side of the surface. Figure 3 shows an example:

split surface 1 across vertex 5 6 onto curve 4

Figure 3 - Splitting Across with Onto Curve

The Split Extend function can be called with the following command:

Split Surface <id_list> Extend [Vertex <id_list> | AUTO] [Preview [Create]]

With the following settings:

Set Split Surface Extend Normal {on|OFF}

Set Split Surface Extend Gap Threshold <val>

Set Split Surface Extend Tolerance<val>

This command splits a surface by extending a surface hard-line until it hits a surface boundary. Figure 4 shows a simple example of extending a curve. The hard-line curve was extended from the specified vertex until it hit the surface boundary.

split surface 1 extend vertex 2

Figure 4 - Splitting by Extending Hard-line

split surface 1 extend auto

Figure 5 - Splitting by Extending with Auto Option

The preview keyword will show a graphics preview of the splitting curve. If the create keyword is also specified, a free curve (or curves) will be created - these are the internal curves that are used to imprint the surfaces.

set split surface normal on split surface 1 extend vertex 2

Figure 6 - Splitting by Extending a Hard Line with Normal Setting ON

Cubit uses the gap threshold to decide whether or not to extend a hard-line when the user specifies auto. If the distance between a vertex on a hard-line and the curve it will hit is greater than the gap threshold, then Cubit will not extend that hard-line. The default value is INFINITY, and can be set to any value. To reset the value back to INFINITY, set the gap threshold to -1.0. Note: This setting only applies when using the keyword auto. An example of using the gap threshold is shown in Figure 7:

set split surface gap threshold 2.0 split surface 1 extend auto

Figure 7 - Extending Hard-lines with Gap Threshold = 2.0. (Notice Vertex 1 was not extended because it exceeded the gap threshold)

The tolerance setting can be used to avoid creating short curves on the surface boundary. If Cubit tries to extend a hard-line that comes within tolerance of a vertex, it will instead snap the extension to the existing vertex. An example of this is shown in Figure 8:

set split surface tolerance 1.0 split surface 1 extend vertex 2

Figure 8 - Extending Hard-lines with Tolerance (Notice the extension snapped to Vertex 3)

This form of the command splits a single surface or a chain of surfaces in an automatic fashion. It is most convenient for splitting a fillet or set of fillets down the middle - oftentimes necessary to prepare for mesh sweeping. These surfaces cannot have multiple curve loops.

Split Surface <id_list> [Corner Vertex <id_list>] [Direction Curve <id>] [Segment|Fraction|Distance <val> [From Curve <id>]] [Through Vertex <id_list>] [Parametric <on|OFF>] [Tolerance <val>] [Preview [Create]]

The volume shown in Figure 9 was quickly prepared for sweeping by splitting the fillets and specifying sweep sources as shown (with the sweep target underneath the volume). The surface splits are shown in blue.

Figure 9 - Splitting Fillets to Facilitate Sweeping

Each surface is always split with a single curve along the length of the surface (or multiple single curves if the Segment option is used). The splitting curve will either be a spline, arc or straight line.

The Split Surface command analyzes the selected surface or surface chain to find a logical rectangle, containing four logical sides and four logical corners; each side can be composed of zero, one or multiple curves. If a single surface is selected (with no options), the logical corners will be those closest to 90 and oriented such that the surface will be split parallel to the longest aspect ratio of the surface. If a chain of surfaces is selected, the logical corners will include the two corners closest to 90 on the starting surface of the chain and the two corners closest to 90 on the ending surface of the chain (the split will always occur along the chain).

In Figure 10, the logical corners selected by the algorithm are Vertices 1-2-5-6. Between these corner vertices the logical sides are defined; these sides are described in Table 1. The default split occurs from the center of Side 1 to the center of Side 3 (parallel to the longest aspect ratio of the surface), and is shown in blue.

Figure 10 - Split Surface Logical Properties

Table 1. Listing of Logical Sides for Figure 10

Figure 11 shows a surface along with 2 possibilities for its logical rectangle and the resultant splits.

Figure 11 - Different Possible Logical Rectangles for Same Surface

Table 2 shows various surfaces and the resultant split based on the automatically detected or selected logical rectangle. Note that surfaces are always traversed in a counterclockwise direction.

(split is always along the chain)

(notice triangular surfaces along the chain)

(note side 1 of the logical rectangle is collapsed; side 3 is from vertex 2 to 3)

(note side 2 of the logical rectangle is collapsed)

(selected automatically)

If a chain of surfaces are split, the surfaces will always be split along the chain. The command will not allow disconnected surfaces.

For a single surface, the split direction logic is a bit more complicated. If no options are specified, the surface aspect ratio determines the split direction - the surface will be split parallel to the longest aspect ratio side through the midpoint of each curve. This behavior can be overridden by the order the Corner vertices are selected (the split always starts on the side between the first two corners selected), the Direction option, the From Curve option, or the Through Vertex list.

Table 3 shows examples of the various split orientation methods. These options are explained in more detail in the sections below.

Table 3 - Split Orientation Methods

Corner Vertex 4 1 2 3

(split always starts on side 1 of the logical rectangle)

From Curve 1 Fraction .75

From Curve 1 Distance 7.5

The Corner option allows you to specify corners that form logical rectangle the algorithm uses to orient the split on the surface. When analyzing a surface to be split, the software automatically selects the corners that are closest to 90. The Preview option displays the automatically selected corners in red. Sometimes incorrect corners are chosen, so you must specify the desired corners yourself. The split always starts on the side between the first two corners selected and finishes on the side between the last two corners selected. Figure 12 shows a situation where the user had to select corners to get the desired split.

Figure 12 - Selecting the Desired Corners

The split can be directed to the tip of a triangular shaped surface by selecting that corner vertex twice (at the start or end of the corner list) when specifying corners, creating a zero-length side on the logical rectangle. A shortcut exists whereas if you specify only 3 corner vertices, the zero-length side will be directed to the first corner selected. If you specify only 2 corner vertices, a zero-length side will be directed to both the first and second corner you select. Table 4 shows these examples. Note the software will automatically detect triangle corners based on angle criteria - the corner selection methods for zero-length sides explained in this section need only be applied if the angles are outside of the thresholds specified in the Set Split Surface Auto Detect Triangle settings.

Table 4 - Selecting Corners to Split to Triangle Tips

4-1-2 (shortcut method)

1-2 or 2-1 (shortcut method)

The Direction option allows you to conveniently override the default split direction on a single surface. Simply specify a curve from the logical rectangle that is parallel to the desired split direction. If Corners are also specified, the Direction option will override the split orientation that would result from the specified corner order. The Direction option is not valid on a chain of surfaces. Figure 13 shows an example.

Figure 13 - Direction Specification Overrides Corner Order

Segment|Fraction|Distance

The Segment option allows you to split a surface into 2 or more segments that are equally spaced across the surface. The Fraction option allows you to override the default 0.5 fractional split location. The Distance option allows you to specify the split location as an absolute distance rather than a fraction. By specifying a From Curve, you can indicate which side of the logical rectangle to base the segment, fraction or distance from (versus a random result). Table 5 gives examples of these options.

Table 5 - Segment, Fraction, Distance Examples

Table 6 - Through Vertex Examples

By default, split locations are calculated in 3D space and projected to the surface. As an alternative, split locations can be calculated directly in the surface parametric space. In rare instances, this can result in a smoother or more desirable split. The command option Parametric {on|Off} can be used to split the given surfaces in parametric space. Alternatively, the default can be overridden with the Set Split Surface Parametric {on|OFF} command.

A single absolute tolerance value is used to determine the accuracy of the split curves. A smaller tolerance will force more points to be interpolated. The tolerance is also used when detecting an analytical curve (e.g., an arc or straight line) versus a spline. A looser tolerance will result in more analytical curves. The default tolerance is 1.0. The command option Tolerance <val> can be used to split the given surfaces using the given tolerance. Alternatively, the default tolerance can be overridden with the Set Split Surface Tolerance <val> command.

It is recommended to use the largest tolerance possible to increase the number of analytical curves and reduce the number of points on splines, resulting in better performance and smaller file sizes. The Preview option displays the interpolated curve points. Table 7 shows the effect of the tolerance for a simple example.

Table 7 - Effect of Tolerance on Split Curve

The Preview keyword will show a graphics preview (in blue) of the splitting curve (or curves) and the corner vertices (in red) selected for the logical rectangle. The curve preview includes the interpolated point locations that define spline curves. Note that if no points are shown on the interior of the curve, it means that the curve is an analytical curve (line or arc). If the Create keyword is also specified, a free curve (or curves) will be created - these are the internal curves that are used to imprint the surfaces. Table 8 shows some examples.

Table 8 - Graphics Preview

This section describes the settings that are available for the automatic split surface command. To see the current values, you can enter the command Set Split Surface, optionally followed by the setting of interest (without specifying a value).

Set Split Surface Tolerance <val>

This sets the default tolerance for the accuracy of the split curves. See the Tolerance section for more information.

Set Split Surface Parametric {on|OFF}

This sets the default for whether surfaces are split in 3D (default) or in parametric space. See the Parametric section for more information.

Set Split Surface Auto Detect Triangle {ON|off}

Set Split Surface Point Angle Threshold <val>

Set Split Surface Side Angle Threshold <val>

The split surface command automatically detects triangular shaped surfaces as explained in the section on Corners. This behavior can be turned off with the setting above. Two thresholds are used when detecting triangles - the Point Angle threshold and the Side Angle threshold, specified in degrees. Corners with an angle below the Point Angle threshold are considered for the tip of a triangle (or the collapsed side of the logical rectangle). Corners within the Side Angle threshold of 180 are considered for removal from the logical rectangle. In order for a triangle to actually be detected, corners for both the point and side criteria must be met. The default Point Angle threshold is 45, and the default Side Angle threshold is 27. Figure 14 provides an illustration.

Figure 14 - Triangle Detection Settings

The Split Skew function can be called with the following command:

Split Surface <id_list> Skew [Preview] [Create]

This command will split a surface or list of surfaces in a logical way to reduce the amount of skew in a quadrilateral mesh. This function uses the control skew algorithm to determine where to make these logical splits. Users should note that Split Skew can only be utilized effectively on surfaces that lend themselves to a structured meshing scheme. These surfaces cannot have multiple curve loops. Figure 15 shows a simple example of a surface being split.

Figure 15. Split Skew applied to an L-shaped surface

---

## Stitching Sheet Bodies

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/stitch.htm

**Contents:**
- Stitching Sheet Bodies

The stitch command stitches together the specified sheet bodies into either a larger sheet body or a solid volume(s). The tolerance value can be used when these sheet bodies don't line up exactly along the edges. This is common for IGES and STEP models. Only manifold stitching is performed, i.e., edges will be shared with no more than two surfaces.

Stitch {Body|Volume} <id_range> [Tolerance <value>] [No_simplify] [No_tighten_gaps] [Restricted]

This command has three stages to it:

When the stitch operation completes, a print statement lets the user know if the resulting body is not a closed, solid body.

The user can choose to omit the second and third options of stitching with the no_simplify and no_tighten_gaps options respectively. This may be necessary in very large or complex models, where the regular approach fails, or takes an inordinate amount of time.

The restricted option limits the stitching operation to the boundary curves of the specified sheet bodies or volumes. All non-boundary curves are ignored by the stitch algorithm. This functionality is intended as a performance enhancement.

---

## Subtract

**URL:** https://coreform.com/cubit_help/geometry/booleans/subtract.htm

**Contents:**
- Subtract
- Remove Overlap

The subtract operation subtracts one body or set of bodies from another body or set of bodies. The order of subtraction is significant - the body or bodies specified before the From keyword is/are subtracted from bodies specified after From. The new body retains the original body's id. If any additional bodies are created, they will be given the next highest available ids.

The keep option simply retains all of the original bodies. Alternatively, the keep_tool option retains only the new body and the "tool" body -- i.e., the body specified before the From keyword.

The imprint option imprints the subtracted bodies onto the resultant body.

The command syntax is:

Subtract [Volume|BODY] <range> From [Volume|BODY] <range> [Imprint] [Keep|Keep_Tool]

Figure 1. The Command Panel interface for boolean subtract operations on bodies.

The Remove Overlap command is a simplified form of the subtract operation above. This command takes exactly two volumes as arguments and uses the modify argument to define the volume where material is to be removed.

Remove Overlap Volume <id1> <id2> modify [Volume <id> | Smaller | Larger]

The Smaller and Larger options are an alternate method of specifying which volume from <id1> or <id2> where material will be removed. When these argument are used, the geometric volume is measured for both volumes and the smaller or larger volume repectively is used as the modify entity. When both volumes have exactly the same volume, the smaller or larger entity ID is used.

---

## Trimming and Extending Curves

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/trim_and_extend.htm

**Contents:**
- Trimming and Extending Curves
- Trimming a Curve
- Extending a Curve

Curves can be trimmed or extended with the following command:

Trim Curve <id> AtIntersection {Curve|Vertex <id>} Keepside Vertex <id> [near]

Curves can be trimmed or extended where they intersect with another curve or at a vertex location. When trimming to another curve, the curves must physically intersect unless they both are straight lines in which case the near option is available. With the near option the closest intersection point is used to the other line - so it is possible to trim to a curve that lies in a different plane. When trimming to a vertex, if the vertex does not lie on the curve, it is projected to the closest location on the curve or an extension of the curve if possible.

The Keepside vertex is needed to determine which side of the curve to keep and which side to throw away. This vertex need not be one of the curve's vertices, nor does it need to lie on the curve. However, if it is not on the curve it will be projected to the curve and that location will determine which side of the curve to keep.

If the curve is part of a body or surface, it is simply copied first before trimming/extending. If it is a free curve a new curve is created and the old curve is removed. The figures below show several examples of trimming/extending curves.

Figure 1. Trimming a Curve to an Intersecting Curve

Figure 2. Trimming a Curve to a Non-Intersecting Curve Using the Near Option

Figure 3. Trimming a Curve to a Vertex

Figure 4. Extending a Curve to An Intersecting Curve

Figure 5. Extending a Curve to a Non-Intersecting Vertex Using the Near Option

---

## Tweaking Curves

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/tweaking_geometry/tweak_curve.htm

**Contents:**
- Tweaking Curves
- Create a Chamfer or Fillet
- Tweaking a Curve Using an Offset Distance
- Removing a Curve
- Tweaking a Curve Using Target Surfaces, Curves, or Plane
- Tweaking a Pair of Curves to a Corner

The following options of the Tweak Curve command are available. Command syntax and description follow below.

The Tweak Curve Chamfer or Fillet command is used to fillet or chamfer a curve. The radius value is the radius of the fillet arc or chamfer cut distance. The command syntax is:

Tweak Curve <id_range> {Fillet|Chamfer} Radius <value> [Keep] [Preview]

In addition to creating chamfers of a single cut distance, the chamfer can be specified be two values. The syntax is:

Tweak Curve <id_list> Chamfer Radius <val1> [<val2>] [Keep] [Preview]

Figure 1 shows a brick ('br x 10') chamfered with two different cut distances ('Tweak Curve 1 2 Chamfer Radius 2 4').

Figure 1 Chamfer with two different distances

Individual curves can also be filleted with different start and finish radius values. The syntax is:

Tweak Curve <id> Fillet Radius <val1> [<val2>] [Keep] [Preview]

Figure 2 shows a brick ('br x 10') filleted with different start and end radius values (‘Tweak Curve 1 2 Chamfer Radius 2 4’).

Figure 2. Fillet with two different radii

For all Tweak Fillet and Tweak Chamfer variations, the keep option prevents the destruction of the original geometry after the operation and the preview option temporarily displays the new geometry configuration without actually changing the geometry.

Tweaking curves a specified distance offsets the existing curves and extends the attached surfaces to meet them. A positive offset value will enlarge the surface while a negative value will decrease the area of the attached surface. Different offset values can be specified for each curve. The keep option prevents the destruction of the original geometry after the operation. The preview option temporarily displays the new geometry configuration without actually changing the geometry. Figure 3 shows an example of offsetting a curve a specified distance.

Figure 3 Offsetting a set of curves a specified distance

Tweak Curve <id_list> Remove [Keep] [Preview]

Similar to the Tweak Curve Remove command, the tweak curve remove function removes a specified curve from a sheet body. Figure 4 shows a simple example of removing a curve from a sheet body.

Figure 4. Removing a curve from a sheet body

The keep option prevents the destruction of the original geometry after the operation. The preview option temporarily displays the new geometry configuration without actually changing the geometry.

Use Tweak Curve Target to offset a curve to a specified surface, plane or curve. Figure 5 shows an example of tweaking a curve to several surfaces.

Figure 5 Tweaking a curve to multiple target surfaces

Similarly, a target plane can be specified using the Plane specification syntax. The Tweak Curve syntax is:

Tweak Curve <id_list> Target {Surface >id_list> [Limit Plane (options)] [EXTEND|Noextend] | Plane (options)} [Max_area_increase <val>] [Keep] [Preview]

Tweak Curve <id_list> Target Curve <id_list > [EXTEND|Noextend] [Max_area_increase <val>] [Keep] [Preview]

If a target surface is supplied, the user can also use a limit plane if he wishes. A limit plane is a plane that the tweak will stop at if the tweaked curve does not completely intersect the target surface. The limit plane must be used with the extend option. See the help for Specifying a Plane for the options available to define a plane.

It should be noted that if the source and target surfaces are from the same body the resulting geometry will be automatically stitched. Single target surfaces are automatically extended so that the tweaked body will fully intersect the target. Unfortunately, extending multiple target surfaces can sometimes result in an invalid target, so the option is given to tweak to non-extended targets with the noextend option. In this case, the tweaked body must fully intersect the existing targets for success. If you experience a failure when tweaking to multiple targets or the results are unexpected, it is recommended to try the noextend option (NOTE: Tweaking to multiple targets is only implemented in the ACIS geometry engine). If a value for the max_area_increasekeyword is given, Cubit will not perform the tweak if the resulting surface area increases by more than the specified amount. The keyword expects a percentage to be entered (i.e. '50' for 50%). It is recommended to always preview before using the tweak target commands.

For all tweak target variations, the keep option prevents the destruction of the original geometry after the operation and the preview option temporarily displays the new geometry configuration without actually changing the geometry.

Although it may not be intuitive curves can also serve as the target geometry. Figure 6 shows an example of extending a curve to another curve.

Figure 6 Tweaking a curve to a target curve

Notice that the source curve actually extends to the target curve as if the target were a surface.

When creating mid-surface geometry it is often useful to extend surfaces to form a corner. To handle this specific but common case use the tweak corner command.

Tweak Curve <id> <id> Corner [Preview]

Figure 7 shows a typical tweak corner example. Notice that surfaces are extended/trimmed to intersect at a corner.

Figure 7. Tweaking two curves to a corner

The preview option temporarily displays the new geometry configuration without actually changing the geometry.

---

## Tweaking Geometry

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/tweaking_geometry/tweaking_geometry.htm

**Contents:**
- Tweaking Geometry

The tweaking commands modify models by moving, offsetting or replacing surfaces, curves, or volumes while extending the adjoining surfaces to fill the resulting gaps. This is useful for eliminating gaps between components, simplifying geometry or changing the dimensions of an object.

---

## Tweaking Surfaces

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/tweaking_geometry/tweak_surface.htm

**Contents:**
- Tweaking Surfaces
- Tweaking a Surface Using an Offset
- Tweaking a Surface by Moving
- Tweaking Surfaces to Target Surfaces
- Removing a Surface
- Tweaking a Conical Surface
- Tweaking Doublers to Target Surfaces
- Removing Holes and Slots from Sheet Bodies
- Removing Fillets from Sheet Bodies
- Changing the Taper of Surfaces

The following options of the Tweak Surface command are available. Command syntax and examples follow below.

Tweak Surface <id_list> Offset <val> [Surface <id_list> Offset <val>] [Surface <id_list> Offset <val> ...] [Keep] [Preview]

The Tweak Offset form of the command offsets an existing set of surfaces and extends the attached surfaces to meet them. A positive offset value will offset the surface in the positive surface normal direction while a negative value will go the other way. Different offsets may be specified for each surface. Figure 1 shows a simple example of offsetting. Note that you can also offset whole groups of surfaces at once. The keep option will retain the original surfaces and curves.

Figure 1. Tweak Offset

The Tweak move form of the command simply moves the given surfaces along a vector direction. The direction can be specified either absolutely or relative to other geometry entities in the model (from entity centroid to location). Note that when moving a surface for tweak, the surface is moved and the surface and the adjoining surfaces are extended or trimmed to match up again. So, for example, moving a vertically oriented planar surface in the vertical direction will have no effect. In this example, if you move the surface 10 in the x and 5 in the y the effect will be to move it simply 10 in the x. You can also use this form of the command to move a protrusion around - just be sure to specify all of the surfaces on the protrusion for moving. The last form of the command can be used to move a surface along another surface's normal.

Tweak Surface <id_range> Move {Vertex|Curve|Surface|Volume|Body} <id> Location {Vertex|Curve|Surface|Volume|Body} <id> [Except [X][Y][Z]] [Keep] [Preview]

Tweak Surface <id_range> Move {Vertex|Curve|Surface|Volume|Body} <id> Location <x_val> <y_val> <z_val> [Except [X][Y][Z]] [Keep][Preview]

Tweak Surface <id_range> Move <dx_val> <dy_val> <dz_val> [Keep] [Preview]

Tweak Surface <id_range> Move Direction <options> Distance <val> [Keep] [Preview]

Tweak Surface <id_range> Move Normal To Surface <id> Distance <val> [Except [X][Y][Z]] [Keep][Preview]

The Tweak target form of the command actually replaces the given surfaces with a copy of the new surfaces, then extends and trims surfaces to match up. This can be useful for closing gaps between components or performing more complicated modifications to models. The command syntax is:

Tweak {Curve|Surface} <id_list> Target {Surface <id_list> [Limit Plane (options)] [EXTEND|noextend] | Plane (options)} [keep] [preview]

Tweak Surface <id_list> Replace [With] Surface <id_list> [Keep] [Preview]

The plane option allows a plane to be specified instead of target surface(s). If a target surface is supplied, the user can also use a limit plane if he wishes. A limit plane is a plane that the tweak will stop at if the tweaked surface does not completely intersect the target surface. The limit plane must be used with the extend option. See the help for Specifying a Plane for the options available to define a plane.

Single target surfaces are automatically extended so that the tweaked body will fully intersect the target. Unfortunately, extending multiple target surfaces can sometimes result in an invalid target, so the option is given to tweak to unextended targets with the noextend option. In this case, the tweaked body must fully intersect the existing targets for success. If you experience a failure when tweaking to multiple targets or the results are unexpected, it is recommended to try the noextend option (NOTE: Tweaking to multiple targets is only implemented in the ACIS geometry engine). It is recommended to always preview before using the tweak target commands.

Figure 2 shows a simple example.

Figure 2. Tweak Surface Target (Viewed directly from the side)

The Tweak remove command allows you to remove surfaces from a model by extending the adjacent surfaces to fill in the resulting gaps. It is identical to the Remove Surface command. See Removing Surfaces for a description of the command options.

Tweak Surface <id_list> Remove [Blend_Chain] [Cavity] [EXTEND|Noextend] [Keepsurface] [Keep] [Preview]

The Tweak cone form of the command is used to replace a conical projection with a flat circular surface. This command is useful for simplifying bolt holes. The command syntax is.

Tweak Surface <id_range> Cone [Preview]

The following is a simple example illustrating the use of the tweak surface cone command.

Figure 3. Conical bolt hole before and after tweaking

The Tweak Doubler form of the command takes a specified surface and creates drop-down surfaces either normal to the doubler surface or by a user specified vector to a target surface. This can be helpful in creating surfaces for weld elements between midsurfaced geometry. The resulting surfaces do not create a bounding volume, and do not imprint themselves onto the target surface. The command syntax is:

Tweak Surface <id_list> Doubler Surface <id_list> {[Limit Plane (options)] [EXTEND|noextend]} [Internal] [Direction (options)] [Thickness] [Preview]

The plane option allows a plane to be specified instead of target surface(s). If a target surface is supplied, the user can also use a limit plane if he wishes. A limit plane is a plane that the tweak will stop at if the tweaked surface does not completely intersect the target surface. The limit plane must be used with the extend option. See the help for Specifying a Plane for the options available to define a plane.

Single target surfaces are automatically extended so that the tweaked body will fully intersect the target. Unfortunately, extending multiple target surfaces can sometimes result in an invalid target, so the option is given to tweak to unextended targets with the noextend option. In this case, the tweaked body must fully intersect the existing targets for success. If you experience a failure when tweaking to multiple targets or the results are unexpected, trying the noextend option is recommended.

If the doubler surface has a thickness property value, you can propagate that thickness value to the newly created drop-down surfaces by using the thickness flag.

It is recommended to always preview before using the tweak doubler commands.

NOTE: This function only works for ACIS geometry.

Figure 3. Extending a doubler surface to target

The internal option will also include internal curves when the surface is extended (see Figure 4c). The direction option will create a skewed surface along the given direction (see Figure 4d).

Figure 4. Explanation of tweak doubler options (a) Original surfaces (b) No option flags used (c) Internal option used - notice internal curves dropped down (d) Direction flag - notice skew

The Tweak Hole/Slot Idealize command takes a specified sheet body(s) and searches for either holes or slots (or both) which meet the user's input parameters. This can be helpful in removing small holes or slots quickly and efficiently from midsurfaced bodies where such level of detail isn't required. The command syntax is:

Tweak Surface <id_list> Idealize {[Hole Radius <val>] [Slot Radius <val> Length <val>]} [Exclude Curve <id_list>] [Preview]

Below is a diagram showing the different parameters available for input by the user.

Figure 5. Input parameters for tweak surface idealize command

#Hole Removal Example tweak surface 13 idealize hole radius 6

Figure 6. Example of hole removal using tweak surface idealize command

The exclude option allows the user to specify individual curves that should not be deleted, even if they meet the search criteria for removal. Figure 7 shows another hole removal example where several curves were excluded.

Figure 7. Example of hole removal using exclude option

Note: This feature is for ACIS geometry

It is recommended to always preview before using the tweak command. Preview will highlight all curves slated to be removed if the command is executed.

The Tweak Fillet Idealize command takes a specified sheet body(s) and searches for either internal or external fillets (or both) which meet the users' radius parameter. This can be helpful in removing fillets quickly and efficiently from midsurfaced bodies where such level of detail isn't required. The command syntax is:

Tweak Surface <id_list> Idealize Fillet Radius <val> {[Internal] [External]} [Exclude Curve <id_list>] [Preview]

#Fillet Removal Example tweak surface 13 idealize fillet radius 6 internal

Figure 8. Example of fillet removal using tweak surface idealize command

Note: This feature is for ACIS geometry

It is recommended to always preview before using the tweak command. Preview will show the result if the command is executed.

Figure 9. Preview of the tweak surface idealize command

The taper or angle of a surface can be made shallower or steeper using the taper surface command. Several surfaces can be tapered at once to get a smooth transition. The command syntax is:

taper Surface <id_list> angle <val> {from plane <options> | about curve <id> | about vertex <id_1><id_2>} [keep] [preview]

Figure 10. taper surface 1 7 6 angle -20 from plane surface 3

The keep and preview options are helpful when figuring out the correct command setup.

The from plane form of the command is the most basic form of the command. The plane normal defines the direction used to set the angle for the surface. The origin of the plane determines how a surface is tapered. If the plane intersects the middle of a surface, the surface will be rotated in on the top and out on the bottom. If it intersects the bottom, the top of the surface will be rotated in and the bottom will stay fixed. If it intersects the top, the bottom of the surface will rotate out and the top will stay fixed.

Figure 11. A cube with one surface tapered 20 degrees with a plane in the middle, bottom, and top.

The about curve form of the command can be used to rotate a surface about a curve. The axis of rotation is determined using the tangent direction of the curve at its starting point. That axis crossed with the normal of the surface at the starting point determine the direction used to set the surface angle. In order to work, the curve must be part of one of the surfaces being changed. Since the direction is based on the curve sense, the final direction is not always obvious. Running the command with the preview option first can help determine what angle to apply.

The about vertex form of the command is similar to the about curve form. The axis of rotation is a vector from the first vertex to the second. That axis crossed with the normal of the surface at the starting point determine the direction used to set the surface angle. In order to work, the vertices must be part of one of the surfaces being changed.

---

## Tweaking Vertices

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/tweaking_geometry/tweak_vertex.htm

**Contents:**
- Tweaking Vertices
- Tweaking a Vertex With a Chamfer
- Tweaking a Vertex With a Non-Equal Chamfer
- Tweaking a Vertex With a Fillet Radius

The Tweak Vertex command can be used to do the following:

Tweak Vertex <id_range> Chamfer Radius <value>[Keep] [Preview]

This form of the command creates a chamfered corner at the specified vertex. Can be use on volumes or free surfaces. The 'keep' option creates another volume on which the tweak is applied; the original volume remains unmodified.

Figure 1. Tweak Vertex Chamfer

Tweak Vertex <id_range> Chamfer Radius <value> [Curve <id> Radius <value> Curve <id> Radius <value> Curve <id>] [Keep] [Preview]

This next form of the command creates a non-equal chamfered corner at the specified vertex. Can only be used on vertices of volumes. The 'keep' option creates another volume on which the tweak is applied; the original volume remains unmodified.

Tweak Vertex <id_range> Fillet Radius <value> [Keep] [Preview]

This command replaces a vertex with a filleted radius. The command can only be used on free surfaces. The 'keep' option creates another volume on which the tweak is applied; the original free surface remains unmodified.

Figure 2. Tweak Vertex Fillet

---

## Tweak Remove Topology

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/tweaking_geometry/tweak_remove_topology.htm

**Contents:**
- Tweak Remove Topology
  - Example

The Tweak Remove Topology command removes curves and surface from a model and replaces them with new topology. The reconstruction of the new topology and the stitching of it into the model is done using real solid modeling kernel operations. This command is intended to be used on small curves and surfaces in the model. The command tries to find small curves/surfaces neighboring the specified topology and includes these neighbors in the removal process. Thus, the command can often be used to remove networks of small features just by specifying a single curve or surface.

Tweak Remove_Topology {Surface <id_range> | Curve <id_range> | Surface <id_range> Curve <id_range>} Small_curve_size <val> Backoff_distance <val>

The small_curve_size is input by the user, and is used to calculate the small curves and surfaces. The backoff_distance value specifies how far away from the original topology cuts are made to cut out the old topology and stitch in the new topology. The removed topology is replaced by simplified topology where possible often resulting in a dimension reduction of the original topology. Extraneous curves that are introduced during the cutting and stitching process are regularized out if possible using the solid modeling kernel regularize functionality or are composited out using virtual geometry if the regularization is not possible.

Note: This command is currently only implemented for ACIS and Catia models.

reset set attribute on import acis "test10.sat" separate body all set attribute off Auto_clean Volume 1 Split_narrow_regions Narrow_size 2.2 tweak remove_topology curve 19 small_curve_size .21 backoff 1.5

Figure 1. Tweak Remove Topology command

---

## Tweak Volume Bend

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/tweaking_geometry/tweak_volume.htm

**Contents:**
- Tweak Volume Bend

Entity bending bends a solid model around a given axis. In any bending operation, some material is stretched while other material is compressed, but the topology of the model is maintained. The command syntax is:

Tweak {Volume|Body} <id_list> Bend Root <location_options> Axis <direction_vector> Direction <direction_vector> Radius <val> angle <val> [Preview] [Keep] [Center_bend] [Location <options>]

Root and axis determine location for the bend. Direction determines direction of the bend. Radius and angle determine how much to bend. Center_bend will bend both sides of the volume around the bend location instead of one side. Location can be used to select only specific parts of a volume to bend.

Figure 1. Bending a volume

#Ex: Bend parts of a body specified by the location option create brick width 11 height 1 create brick width 1 depth 10 height 10 create brick width 1 depth 10 height 10 create brick width 1 depth 10 height 10 move body 2 general location position -3 5 0 move body 3 general location position 0 5 0 move body 4 general location position 3 5 0 subtract body 2 from body 1 subtract body 3 from body 1 subtract body 4 from body 1 tweak volume 1 bend root 0 0 0 axis 1 0 0 direction 0 0 -1 radius 1 angle 3.14 location vertex 39 47

---

## Unite

**URL:** https://coreform.com/cubit_help/geometry/booleans/unite.htm

**Contents:**
- Unite

The unite operation combines two or more bodies into a single body. The original bodies are deleted and the new body is given the next highest body ID available, unless the keep option is used. The commands are:

Unite [Volume|BODY] <range> [With [Volume|BODY] <range>] [Keep]

Unite Body {<range> | All} [Keep]

Unite Body {<range> | All} [Include_mesh]

The second form of the command unites multiple bodies in a single operation. If the all option is used, all bodies in the model are united into a single body. If the bodies that are united do not overlap or touch, the two bodies are combined into a single body with multiple volumes.

The unite command allows sheet bodies to be united with solid bodies. To disable this capability you can turn the following setting off:

Set Unite Mixed {ON|Off}

---

## Unmerging

**URL:** https://coreform.com/cubit_help/geometry/imprint_merge/unmerging.htm

**Contents:**
- Unmerging

The unmerge command is used to reverse the merging operation. This is often in cases where further geometry decomposition must be done.

Unmerge {all|<entity_list> [only]}

Un-merging an entity means that the specified geometric entity and all lower-order (or child) entities will no longer share non-manifold topology with any other entities. For example, if a body is unmerged, that body will no longer share any surfaces, curves, or vertices with any other body.

[Set] Unmerge Duplicate_mesh {On|OFF}

If any meshed geometry is unmerged, the mesh is kept as necessary to keep the mesh of higher-order entities valid. For example, if a surface shared by two volumes is to be unmerged and only one of the volumes is meshed, the surface mesh will remain with whichever surface is part of the meshed volume.

When unmerging meshed entities, the default behavior of the code is that the placement if the mesh is determined by the following rules:

If unmerge duplicate_mesh is turned on, the rules described above are overwritten and whenever a meshed entity is unmerged the mesh is always copied such that both entities remain meshed.

To get back to the default behavior, turn unmerge duplicate_mesh off.

---

## Using CUBIT Attributes

**URL:** https://coreform.com/cubit_help/geometry/attributes/persistent_attributes/using_attributes.htm

**Contents:**
- Using CUBIT Attributes

A typical scenario for using CUBIT attributes would be as follows.

Construct geometry, merge, assign intervals, groups, etc. (i.e. normal CUBIT session)

Enable automatic use of attributes using the command:

Export acis file (see Export Acis command).

Enable automatic reading and actuating of attributes:

Import ACIS file (see Import Acis command)

Used in this manner, geometry attributes allow the user to store some data directly with the geometry, and have that data be assigned to the corresponding CUBIT objects without entering any additional commands.

---

## Using Geometry Merging to Verify Geometry

**URL:** https://coreform.com/cubit_help/geometry/imprint_merge/merging_to_verify_geometry.htm

**Contents:**
- Using Geometry Merging to Verify Geometry

Geometry merging is often used to verify the correctness of an assembly of volumes. For example, groups of unmerged surfaces can be used to verify the outer shell of the assembly (see Examining Merged Entities.) There is other information that comes from the Merge all command that is useful for verifying geometry.

In typical geometric models, vertices and curves which get merged will usually be part of surfaces containing them which get merged. So, if a Merge all command is used and the command reports that vertices and curves have been merged, this is usually an indication of a problem with geometry. In particular, it is often a sign that there are overlapping bodies in the model. The second most common problem indicated by merging curves and vertices is that the merge tolerance is set too high for a given model. In any event, merged vertices and curves should be examined closely.

---

## Validating/Analyzing Geometry

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/validating_geometry.htm

**Contents:**
- Validating/Analyzing Geometry

Detailed checks of geometry and topology can be performed using the validate command:

Validate {Body|Volume|Surface|Curve|Vertex|Group} <id_range> [level val=<value=20>] [verbose]

Healer Analyze Body <id_range> [level val=<value=20>] [verbose]

These two commands traverse the given entity's topological tree structure, checking for bad data or invalidities along the way. Both commands do exactly the same thing. More extensive diagnostics can be ran by specifying a higher check level. The check levels are value multiples of 10 between 0 and 70 inclusive. Use the level option of the command to specify the level (how extensive) of the validation. The verbose option prints additional details of any problems.

where value is one of the following:

20 = Level 10 checks plus slower error checks (default)

30 = Level 20 checks plus D-Cubed curve and surface checks

40 = Level 30 checks plus fast warning checks

50 = Level 40 checks plus slower warning checks

60 = Level 50 checks plus slow edge convexity change point checks

70 = Level 60 checks plus face/face intersection checks

Validate {Volume|Surface|Curve|Vertex} <range> Mesh

The Validate {...} mesh command performs a connectivity check of the mesh elements to determine the validity of the mesh.

The validate command can also check for consistent surface normals and return a list of offending surfaces. The syntax for the command is as follows:

Validate [Body] <body_id> Normal [Reference [Surface] <surface_id>] [Reverse]

Using the "reference" keyword, a reference surface is compared to the normal consistency of all other specified surfaces. Inconsistent surfaces can be reversed using the "reverse" keyword.

---

## Virtual Geometry

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/virtual_geometry.htm

**Contents:**
- Virtual Geometry

The Virtual Geometry module in CUBIT provides a way to modify the topology of the model without affecting the underlying ACIS geometry representation and without making changes to the actual solid model. Virtual Geometry includes the capability to composite or partition geometry as well as creates new virtual geometric entities. Virtual Geometry operations are most often used as a tool for adjusting the geometry to allow mapping, sub-mapping or sweeping mesh generation schemes to be applied.

The advantage to using Virtual Geometry is that all operations are reversible. With standard geometry modification commands, changes are made to the underlying geometry representation and cannot be changed once effected. With virtual geometry, the original solid model topology can be easily restored. This is useful when geometry modifications are made in order to apply a particular meshing scheme. Virtual geometry can be applied and later removed once the part has been meshed.

---

## Web Cutting

**URL:** https://coreform.com/cubit_help/geometry/decomposition/web_cutting/web_cutting.htm

**Contents:**
- Web Cutting
- General Notes

The term "web cutting" refers to the act of cutting an existing body or bodies, referred to as the "blank", into two or more pieces through the use of some form of cutting tool, or "tool". The two primary types of cutting tools available in CUBIT are surfaces (either pre-existing surfaces in the model or infinite or semi-infinite surfaces defined for web cutting), or pre-existing bodies.

The various forms of the web cut command can be classified by the type of tool used for cutting. These forms are described below, starting with the simplest type of tool and progressing to more complex types.

The primary purpose of web cutting is to make an existing model meshable with the hex meshing algorithms available in CUBIT. While web cutting can also be used to build the initial geometric model, the implementation and command interface to web cutting have been designed to serve its primary purpose. Several important things to remember about web cutting are as follows:

The Decomposition Tutorials and the Power Tools Tutorial contain some examples that demonstrate the use of web cutting operations.

---

## Web Cutting by Sweeping Curves or Surfaces

**URL:** https://coreform.com/cubit_help/geometry/decomposition/web_cutting/sweeping_curves_or_surfaces.htm

**Contents:**
- Web Cutting by Sweeping Curves or Surfaces
- Web Cutting by Sweeping a Surface Along a Trajectory
- Web Cutting by Sweeping a Surface About an Axis
- Web Cutting by Sweeping a Curve(s) Along a Trajectory
- Web Cutting by Sweeping a Curve(s) About an Axis

Webcutting with sweeping creates a swept tool body in the same step as the web cut operation. There are 4 general ways to web cut with sweeping:

This command allows one or more surfaces to be swept, creating a volume that is used for the web cut. If more than one surface is specified, the surfaces must contain coincident curves. The surfaces are swept along a direction and some distance or perpendicular and some distance or along a curve. For best results the curve to sweep the surface along should intersect one of the surfaces. The through_all option will sweep the surfaces along the trajectory far enough so as to intersect all input bodies. The stop surface <id> option is used to identify a surface at which the sweep will stop. If using this option when sweeping along a curve, the sweep will stop at the first place possible. The up_to_next option indicates that the user wants to web cut with only the first water tight volume that forms as a result of the intersection between sweep and union of all blank bodies. The [Outward|Inward] options specify a sweeping direction that is either INTO the volume or OUT from the volume.

Webcut {Volume|Body|Group} <range> Sweep Surface <id_range> {Vector <x> <y> <z> [Distance <distance>] | Along Curve <id>} [Through_all | Stop Surface <id> | Up_to_next ] [webcut_options]

Webcut {Volume|Body|Group} <id> Sweep Surface <id_range> Perpendicular {Distance <distance> | Through_all | Stop Surface <id>} [OUTWARD|Inward] [webcut_options]

sweeping a surface in a direction

along a curve to a stop surface

Figure 1. Examples of web cutting with swept surfaces

This command allows a one or more surfaces to be swept, creating a volume that is used for the web cut. If more than one surface is specified, the surfaces must contain coincident curves. The surface is swept about a user-defined axis or about one of the x y z coordinate axes and a specified angle. The stop surface <id> option is used to identify a surface at which the sweep will stop. The up_to_next option indicates that the user wants to web cut with only the first water tight volume that forms as a result of the intersection between sweep and union of all blank bodies. For these 2 options to work correctly the user must specify an angle large enough for the rotation to traverse the stop surface or the up_to_next surface.

Webcut {Volume|Body|Group} <id> Sweep Surface <id_range> {Axis <xpoint ypoint zpoint xvector yvector zvector> | Xaxis | Yaxis | Zaxis } Angle <degrees> [Stop Surface <id> | Up_to_next] [webcut_options]

This command allows a curve(s) to be swept, creating a surface that is used for the web cut. If multiple curves are specified, they must share vertices and form a continuous path. The curve(s) is swept along a direction and some distance or along another curve. If sweeping a curve(s) along another curve, for best results the curve(s)-to-swept and the curve to sweep along should intersect at some point. The stop surface <id> option is used to identify a surface at which the sweep will stop. If using this option when sweeping along a curve, the sweep will stop at the first place possible. The through_all option will sweep the curve(s) along the trajectory far enough so as to intersect all input bodies. For the web cut to be successful, the swept curve(s) must completely traverse a portion of a blank body(s), cutting off a complete piece of the blank body(s). Option through_all should not be used when defining the web cut with a vector and a distance or along a curve.

Webcut {Volume|Body|Group} <id> Sweep Curve <id_range> {Vector <x> <y> <z> [Distance <distance>| Along curve <id>] } [Through_all | Stop Surface <id>] [webcut_options]

This command allows a curve to be swept, creating a surface that is used for the web cut. If multiple curves are specified, they must share vertices and form a continuous path. The curve(s) is swept about a user-defined axis or about one of the x y z coordinate axes and a specified angle. For the web cut to be successful, the swept curve(s) must completely traverse a portion of a blank body(s), cutting off a complete piece of the blank body(s). The stop surface <id> option is used to identify a surface at which the sweep will stop. For this option to work correctly the user must specify an angle large enough for the rotation to traverse the stop surface.

Webcut {Volume|Body|Group} <id> Sweep Curve <id_range> {Axis <xpoint ypoint zpoint xvector yvector zvector> | Xaxis | Yaxis | Zaxis } Angle <degrees> [Stop Surface <id>] [webcut_options]

---

## Web Cutting Options

**URL:** https://coreform.com/cubit_help/geometry/decomposition/web_cutting/webcut_options.htm

**Contents:**
- Web Cutting Options

The following options can be used with all web cut commands:

[NOIMPRINT|Imprint [include_neighbors] ]: In its default implementation, web cutting results in the pieces not being imprinted on one another; this option forces the code to imprint the pieces after web cutting. The include_neighbors option will also imprint adjacent bodies.

[NOMERGE|Merge]: By default, the pieces resulting from an imprint are manifold; specifying this option results in a merge check for all surfaces in the pieces resulting from the web cut.

[Group_results]: The various pieces resulting from the previous command are placed into a group named `webcut_group'.

[Preview]: This option will preview the web cutting plane without executing the command.

---

## Web Cutting using a Tool or Sheet Body

**URL:** https://coreform.com/cubit_help/geometry/decomposition/web_cutting/tool_body.htm

**Contents:**
- Web Cutting using a Tool or Sheet Body

Any existing body in the geometric model can be used to cut other bodies; the command to do this is:

Webcut {blank} tool [body] <id> [webcut_options]

This simply uses the specified tool body in a set of boolean operations to split the blank into two or more pieces.

Another form of the command cuts the body list with a temporary sheet body formed from the curve loop. This is the same sheet as would be created from the command Create Surface Curve <id_list>.

Webcut {Body|Group} <id_range> [With] Loop [Curve] <id_range> NOIMPRINT|Imprint] [NOMERGE|Merge] [group_results]

Webcut {Volume|Body|Group} <id_range> [With] Bounding Box {Body|Volume|Surface|Curve|Vertex <id_range>} [Tight] [[Extended] {Percentage|Absolute} <val>] [{X|Width} <val>] [{Y|Height} <val>] [{Z|Depth} <val>]] NOIMPRINT|Imprint] [NOMERGE|Merge] [group_results]

The final form of this command cuts a body with the bounding box of another entity. This bounding box may be tight or extended.

Figure 1. Cylinder cut with bounding box of prism.

---

## Web Cutting with an Arbitrary Surface

**URL:** https://coreform.com/cubit_help/geometry/decomposition/web_cutting/arbitrary_surface.htm

**Contents:**
- Web Cutting with an Arbitrary Surface

An arbitrary "sheet" surface can also be used to web cut a body. This sheet need not be planar, and can be bounded or infinite. The following commands are used:

Webcut {blank} with sheet {body|surface} <id> [webcut_options]

Webcut {blank} with sheet extended [from] surface <id> [webcut_options]

In its first form, the command uses a sheet body, either one that is pre-existing or one formed from a specified surface. Note that in this latter case the (bounded) surface should completely cut the body into two pieces. Sheet bodies can be formed from a single surface, but can also be the combination of many surfaces; this form of web cut can be used with quite complicated cutting surfaces.

Extended sheet surfaces can also be used; in this case, the specified surface will be extended in all directions possible. Note that some spline surfaces are limited in extent, and so these surfaces may or may not completely cut the blank.

---

## Web Cutting with a Planar or Cylindrical Surface

**URL:** https://coreform.com/cubit_help/geometry/decomposition/web_cutting/planar_or_cylindrical_surface.htm

**Contents:**
- Web Cutting with a Planar or Cylindrical Surface
- Coordinate Plane
- Planar Surface
- Plane from 3 Points
- Plane Normal to Curve
- General Plane Specification
- Cylindrical Surface
- Cone Surface

The commands used to web cut with a planar or cylindrical surface in CUBIT are:

In the command's simplest form, a coordinate plane can be used to cut the model, and can optionally be offset a positive or negative distance from its position at the origin.

Webcut {Volume|Body|Group} <id_range> [With] Plane {xplane|yplane|zplane} [Offset <val>] [rotate <theta> about x|y|z <xval> <yval> <zval> [center <xval> <yval> <zval>]] webcut_options

The cutting plane can be rotated about a user-specified axis using the rotate option. The center of rotation can be moved by using the center option.

An existing planar surface can also be used to cut the model; in this case, the surface is identified by its ID as the cutting tool.

Webcut {Volume|Body|Group} <id_range> [With] Plane Surface <surface_id> webcut_options

Any arbitrary planar surface can be used by specifying three vertices that define the plane, and can optionally be offset a positive or negative distance from this plane.

Webcut {Volume|Body|Group} <id_range> [With] Plane Vertex <vertex_1> [Vertex] <vertex_2> [Vertex] <vertex_3> [Offset <value>] webcut_options

The plane to be used for the web cut can be previewed with the preview option in the general webcut options.

The next command allows a user to specify an infinite cutting plane by specifying a location on a curve. The cutting plane is created such that it is normal to the curve tangent at the specified location.

Webcut {Volume|Body|Group} <id_range> [With] Plane Normal To Curve <curve_id> {Position <xval><yval><zval> | Close_To Vertex <vertex_id>} webcut_options

Webcut {Volume|Body|Group} <id_range> [With] Plane Normal To Curve <curve_id> {Fraction <f> | Distance <d>} [[From] Vertex <vertex_id>] webcut_options

The position on the curve can be specified as:

The point on the curve can be previewed with the Draw Location On Curve command and the plane to be used for the web cut can be previewed with the preview option in the general webcut options.

A webcut plane can be defined using the general plane specification options in the Specifying a Plane section of the documentation.

Webcut {Volume|Body|Group} <id_range> [With] General Plane {options} webcut_options

Finally, a semi-infinite cylindrical surface can be used by specifying the cylinder radius, and the cylinder axis. The axis is specified as a line corresponding to a coordinate axis, the normal to a specified surface, two arbitrary points, or an arbitrary point and the origin. The "center" point through which the cylinder axis passes can also be specified.

Webcut {Volume|Body|Group} <range> [With] Cylinder Radius <val> Axis {x|y|z|normal of surface <id>| vertex <id_1> vertex <id_2>| <x_val> <y_val> <z_val>>} [center <x_val> <y_val> <z_val>] webcut_options

A semi-infinite cone surface can be used by specifying the cone outer radius, and the cone inner radius. The axis is specified as a location first of where the outer radius is applied and the second location of where the inner radius is applied.

Webcut {Volume|Body|Group} <ids> [With] cone radius <val> <val> location {options} location {options} [Imprint] [Merge] [group_results] [preview]

---

## Web Cutting with Offset Surfaces

**URL:** https://coreform.com/cubit_help/geometry/decomposition/web_cutting/offset_surface.htm

**Contents:**
- Web Cutting with Offset Surfaces

One or more existing surfaces of the model can be used to web cut a body by first offsetting those surfaces a specified distance. The offset surface (or, when the Loft option is used, a lofted volume built between the original surfaces and their offsets) becomes the cutting tool. This form is convenient for decompositions that follow the shape of an existing surface, such as creating a boundary-layer region a fixed distance from a wall. The following command is used:

Webcut {Body|Volume|Group} <id> Offset_tool Surface <id_range> Offset <distance> [Loft] [{Inward|Outward}] [webcut_options]

The surfaces named after Offset_tool are offset by the value given with Offset. If a single surface or a pair of surfaces is specified, the operation reduces to a sheet-extended web cut from the resulting offset surface. If three or more offset surfaces are specified and they do not form a single connected sheet, the result may be unpredictable.

The [Outward|Inward] options set the offset direction. Outward offsets the surfaces a positive distance (away from the body); Inward offsets them a negative distance (into the body). If neither keyword is given, the sign of the specified distance determines the direction.

The [Loft] option builds a lofted volume between the original surfaces and their offset copies and uses that volume as the cutting tool. This is useful for carving out a boundary-layer volume of uniform thickness; the surfaces of the resulting boundary volume are automatically assigned default meshing schemes (mapping or paving as appropriate). Loft is only valid together with the Inward keyword.

The remaining trailing options — imprinting (including Tolerant_Imprint and include_neighbors), merging, group_results, and preview — behave as described under Web Cutting Options.

This command currently web cuts a single body or volume at a time.

original surface and its offset

Figure 1. A surface offset a fixed distance into the body and the volume that results from the web cut.

Figure 2. Using the Loft option with Inward to create a boundary-layer volume of uniform thickness.

---

## What if Healing is Unsuccessful?

**URL:** https://coreform.com/cubit_help/geometry/cleanup_and_defeaturing/healing/what_if_unsuccessful.htm

**Contents:**
- What if Healing is Unsuccessful?

The ACIS healing module is under continued development and is improving with every release. However, there will often be situations where healing is unable to fully correct the geometry. This might be okay, as meshing is rarely affected by the small inaccuracies healing addresses. However, boolean operations on the geometry can fail if the bad geometry must be processed by the operation (i.e., a webcut must cut through a bad curve or vertex).

Here are some possible methods to fix this bad geometry:

Contact support@coreform.com if you need further help with fixing bad geometry.

---

## Working With Parts and Assemblies

**URL:** https://coreform.com/cubit_help/geometry/metadata/working_with_parts.htm

**Contents:**
- Working With Parts and Assemblies
- Identifying Parts and Assemblies
- Creating Parts and Assemblies
- Deleting Parts and Assemblies
- Associating Parts with Volumes
- Viewing All Assembly Information at Once
- Metadata in the GUI

Each part and assembly has a name and an optional description. Other attributes may also be assigned, such as a material specification or a link to an entry in a PDM system. See Metadata Attributes.

The relationship between the geometric model and the assembly is determined by associating parts with volumes. A single part can be associated with any number of volumes, including zero volumes. A volume, however, can be associated with only one part.

As volumes are modified, CUBIT automatically maintains the appropriate relationships with parts. If a volume is associated with a part, and that one volume is split into multiple volumes through a webcut or some other operation, each of the resulting volumes is automatically associated with the original volume’s part. Copying a volume will also result in the new volume being associated with the same part as the original volume.

A part or assembly is identified by its assembly path. An assembly path is much like a directory path in a file system. It consists of the name of each ancestor in the assembly tree, separated by a forward slash. For example, a part named “p1” contained within the top-level assembly “a1” would be identified by the path “/a1/p1”. If the part “p2” is part of the assembly “a2”, and “a2” is a sub-assembly of “a1”, then “p2” has the path “/a1/a2/p2”.

More than one part or assembly may have the same name. To differentiate between parts or assemblies with the same name and path, each part also has an instance number. If two entities have the same name, they will not have the same instance number. For example, two parts named “p1” may be “p1 instance 1” and “p1 instance 2”.

Instance numbers may be incorporated into assembly paths by placing the instance number in angled braces after a part or assembly name. For example, “p1 instance 3” is identified in a path as “p1<3>”. Other examples of instance numbers in assembly paths include “/a1<1>/a2<1>/p1<3>” and “/a1/a2<1>/p1”. Assembly paths are always allowed to incorporate instance numbers, but are only required to include as many instance numbers as it takes to avoid ambiguity. Note that some commands do accept ambiguous paths, selecting a random entity which matches the path.

Most commands which accept assembly paths also allow the path to be followed by an “instance” command option (for example, metadata list part “/a1/p1” instance 3). The instance option always refers to the instance number of the last item in the path (p1 in the example).

Parts and assemblies can be created using the following commands:

Metadata Create {Assembly|Part} “<absolute_path>” [Instance <instance>]

If the instance option is not included, CUBIT will assign an appropriate instance number to the new entity. If the instance option IS included, an entity with the specified name and instance number must not already exist or the command will fail.

Note that the path must be absolute, identifying each ancestor of the new entity. Any ancestors of the new entity which do not already exist are automatically created.

To delete a part or an assembly, use the Metadata Remove command:

Metadata Remove {Part “<path>” | Assembly “<path>" [propagate]}

This will remove the specified part or assembly. If the propagate option is specified when removing an assembly, all contained parts and subassemblies will be removed automatically before the assembly itself is removed. Otherwise, assemblies will only be removed if they have no contents.

It is also possible to remove all parts and assemblies that have no association with geometric volumes in the model:

This can be extremely useful when importing geometry which has been simplified with metadata which has not been simplified. For example, eMatrix currently writes out the full assembly hierarchy even when exporting a simplified representation of the geometry.

The relationship between the geometric model and the assembly is determined by associations between parts and volumes. As stated previously, a part may be associated with any number of volumes, while a volume may be associated with only one part. The easiest way to associate a volume with a part is to use the entity tree in the user interface. Drag a volume in the tree onto a part in the tree, and the volume and part are now associated. Since a volume can only be associated with one part at a time, any previous association between that volume and a part is removed.

Part-to-volume associations can be created on the command line using the Metadata Modify Path command:

Metadata Modify Path “<part_path>” Volume <ids>

The specified volume or volumes will be associated with the part specified by part_path. Any volumes already associated with the specified part will retain their association with the part.

Associations can be removed using the Metadata Remove command:

Metadata Remove Volume <ids>

After the Metadata Remove command has been issued, the specified volumes are no longer associated with any part.

The set of volumes associated with a given part can be modified using the Metadata Replace command:

Metadata Replace Part “<part_path>” Volume <ids>

When the Metadata Replace command is issued, all associations the part may have had with any volumes are removed. New associations are then created with the specified volume or volumes.

Once an assembly tree is created, all assemblies, parts, and part-to-volume associations can be viewed using the command:

It is also possible to view all parts, their properties, and their volume associations using a spreadsheet application such as Microsoft Excel. This is done by generating a file using the command:

Export Part_List "<filename>" [OverWrite]

This command writes an XML file in a format that Excel can convert to a spreadsheet. To do this, simply import the XML file into Excel as an XML List. The data can then be sorted and filtered by any of the parts' properties.

The Export Part_List command is particularly useful for identifying parts which are not correctly associated with parts. Among the fields that can be filtered is the is-part field. This field is FALSE for each volume that is not associated with a part. Filtering on this value will show a list of all volumes that are not associated with any part. The volume-ids field will show the ID of each unassociated volume, and the volume-name field will show each unassociated volume's name, if any.

It is equally easy to identify parts that are not associated with volumes. Display only those rows with a blank value in the volume-ids field to see a list of parts that have no associated volume.

Similar methods can be used to identify missing materials information. Fields can also be sorted to group the parts by material.

Metadata may be displayed and manipulated in the GUI. The tree view includes a category for metadata. The category is labelled "Assemblies" in the tree view. Users are able to drag volumes into parts on the tree. Also, selecting an Assembly or Part on the tree will cause the attributes for the entity to be displayed in the property page where further data manipulation is enabled.

---
