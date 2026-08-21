# Coreform-Cubit-Docs-Skill_Docs - Fe Model

**Pages:** 16

---

## Boundary Condition Sets

**URL:** https://coreform.com/cubit_help/finite_element_model/non_exodus/sets.htm

**Contents:**
- Boundary Condition Sets
- *** ABAQUS Parameters ***
- *** NASTRAN Parameters ***

Create bcset [id] [name <'name'>] [After bcset <id>] [{Add|Remove} {bc_type} <id-range | <with name 'name'> >] [analysistype {STATIC|heat|dynamic|modal}] [modal_max_frequency <value>]

Modify bcset {id_list|'name'|all} [name <'name'>] [After bcset <id>] [{Add|Remove} {bc_type} <id-range | <with name 'name'> >] [analysistype {STATIC|heat|dynamic|modal}]

Modify bcset {id_list|'name'|all} [max_step_increments <value>] [nonlinear_geometry <on|OFF>][perturbation <on|OFF>][stabilize <on|OFF>] [steadystate <on|OFF>][modal_max_frequency <value>]

Modify bcset {id_list|'name'|all} [initial_step_size <value>] [step_period <value>][min_step_size <value>] [max_step_size <value>][min_step_temperature_change <value>]

Modify bcset {id_list|'name'|all} [mass_scaling <on|OFF>] [mass_scaling_dt <value>][mass_scaling_factor <value>] [mass_scaling_type <'uniform'|'BELOW_MIN'|'set_equal_dt'>]

Modify bcset {id_list|'name'|all} [restart <on|OFF>][restart_overlay <on|OFF>] [{restart_frequency|restart_num_intervals} <value>]

Modify bcset {id_list|'name'|all} [output_field <on|OFF>] [output_field_frequency <value>] [output_history <on|OFF>] [output_history_frequency <value>]

Modify bcset {id_list|'name'|all} [el_file <on|OFF>][el_file_frequency <value>] [node_file <on|OFF>][node_file_frequency <value>]

Modify bcset {id_list|'name'|all} [el_print <on|OFF>][el_print_frequency <value>] [node_print <on|OFF>][node_print_frequency <value>]

Modify bcset {id_list|'name'|all} {displacement_output <on|OFF> {PLOT|print|punch|punchprint} {group <ALL|none|<id>> }}

Modify bcset {id_list|'name'|all} {oload <on|OFF> {PLOT|print|punch|punchprint} {group <ALL|none|<id>> }}

Modify bcset {id_list|'name'|all} {mpcforces <on|OFF> {PLOT|print|punch|punchprint} {group <ALL|none|<id>> }}

Modify bcset {id_list|'name'|all} {spcforces <on|OFF> {PLOT|print|punch|punchprint} {group <ALL|none|<id>> }}

Modify bcset {id_list|'name'|all} {stress <on|OFF> {PLOT|print|punch|punchprint} {group <ALL|none|<id>> } {CENTER|cubic|sgage|corner} {VONMISES|maxs}}

Modify bcset {id_list|'name'|all} {element_strain_energy <on|OFF> {PLOT|print|punch|punchprint} {group <ALL|none|<id>> } {AVERAGE|amplitude|peak}}

CUBIT can create BC sets, which is a group of previously defined loads, restraints and contact pairs. A BCSet is used to define a load case (analysis step) when writing out 3rd party analysis decks. A BCSet can be a static analysis set, a thermal analysis set, a modal analysis set, or a dynamic analysis set by specifying the analysistype. The After keyword can be used to define the order that the BCSets will be written when the model is exported.

Several solver-specific parameters can be set for a BCSet. For ABAQUS, parameters associated with *STEP, *STATIC, *DYNAMIC, *FREQUENCY, *HEAT TRANSFER, *MASS SCALING, *RESTART, *OUTPUT, *EL FILE, *NODE FILE, *EL PRINT, and *NODE PRINT can be modified. For Nastran, output requests can be defined for Displacement, Reaction Loads, MPC Forces, SPC Forces, Stress, and Element Strain Energy.

---

## CFD Boundary Conditions

**URL:** https://coreform.com/cubit_help/finite_element_model/non_exodus/cfd.htm

**Contents:**
- CFD Boundary Conditions

CUBIT can export models to the Fluent mesh format and CNGS unstructured mesh format for CFD analysis. CUBIT also supports defining the below CFD boundary conditions. Only the region on which the BC acts can be defined in CUBIT. The data associated with each boundary condition (pressure, velocity, mass values, etc.) is not defined within CUBIT and must be assigned using a CFD model editor, such as Fluent.

create cfd_bc [id] {axis|exhaustfan|fan|inletvent|intakefan|interface| interior|massflowinlet|outflow|outletvent|periodic|periodicshadow| porousjump|pressurefarfield|pressureinlet|pressureoutlet|radiator| supersonicinflow|supersonicoutflow|symmetry|velocityinlet|wall} [name <'name'>] [{add|on} {sideset|surface} <entity_list>

The following shows the commands for modifying, deleting, and lising CFD boundary conditions.

modify cfd_bc [id] [name <'name'>] [{add|remove} {sideset|surface} <entity_list>

delete cfd_bc {<ids>|'<string>'}

---

## Cubit Boundary Conditions

**URL:** https://coreform.com/cubit_help/finite_element_model/non_exodus/boundary_condition.htm

**Contents:**
- Cubit Boundary Conditions

In CUBIT, boundary conditions are applied to sidesets or nodesets. Sidesets and nodesets can contain geometry or mesh. This means that models can be remeshed without worrying about losing boundary condition data if the boundary condition is applied to a geometry-based sideset/nodeset.

The sideset/nodeset used by a boundary condition will be visible to the user, and the user can modify the sideset/nodeset separately from the boundary condition. Sidesets/nodesets can be assigned to (or removed from) a boundary condition at any time.

Boundary conditions are broken into four groups: Restraints, loads, contact, and cfd. Each restraint that is created will belong to a restraint set, each load will belong to a load set, and each contact definition will belong to a contact set. A boundary condition set consists of any number of restraints, contact pairs, and loads. CFD boundary conditions do not belong to boundary condition sets.

Table 1: Overview of boundary condition entities available in Cubit

---

## CUBIT Initial Conditions

**URL:** https://coreform.com/cubit_help/finite_element_model/non_exodus/cubitinitialconditions.htm

**Contents:**
- CUBIT Initial Conditions

In CUBIT, initial conditions can be applied to nodesets. CUBIT supports the following types of initial conditions: displacement, velocity, acceleration, temperature, and generic field. For now, initial conditions are only supported by CUBIT's Abaqus exporter. The commands to create an initial condition are:

Create initialcondition [id] type temperature [name <'name'>] [{add|on} nodeset <entity_list>] [value <val>]

Create initialcondition [id] type displacement [name <'name'>] [{add|on} nodeset <entity_list>] [dof {1|2|3|4|5|6} {value <value>|off}]

Create initialcondition [id] type velocity [name <'name'>] [{add|on} nodeset <entity_list>] [dof {1|2|3|4|5|6} {value <value>|off}]

Create initialcondition [id] type acceleration [name <'name'>] [{add|on} nodeset <entity_list>] [dof {1|2|3|4|5|6} {value <value>|off}]

Create initialcondition [id] type field [name <'name'>] [{add|on} nodeset <entity_list>] [variable <n> value <val>

For most of the initial conditions, only two pieces of data are required: a list of nodesets this IC is applied to, and an initial value. Optionally, a name can be specified for the initial condition. To modify an initial condition, replace the word “create” with the word “modify.” If modifying an IC, the IC’s ID must be passed in so CUBIT knows which IC you are modifying. Example:

Modify initialcondition 3 value 1.23

Use this command to list the information about a set of initial conditions:

List initialcondition <id_list>

Use this command to delete a set of initial conditions:

Delete initialcondition <id_list>

---

## Defining Materials and Media Types

**URL:** https://coreform.com/cubit_help/finite_element_model/exodus/materials.htm

**Contents:**
- Defining Materials and Media Types
- Custom Material Commands

Materials can be defined in CUBIT and assigned to element blocks. If an element block is exported without a material assigned to it, a default material (with properties for common steel) will be exported for it.

Create Material [id] [Name <'name'>] [Elastic_modulus <value>] [Poisson_ratio <value>] [Shear_modulus <value>] [Density <value>] [Specific_heat <value>] [Conductivity <value>] [User constants <value ...>] [DepVar <value>]

Modify Material <id_list|'name'|all> [Name <'name'>] [Elastic_modulus <value>] [Poisson_ratio <value>] [Shear_modulus <value>] [Density <value>] [Specific_heat <value>] [Conductivity <value>] [User constants <value ...>] [DepVar <value>]

Create Media [id] [Name <'name'>] [Fluid|Porous|Solid]

Modify Media <id_list|'name'|all> [Name <'name'>] [Fluid|Porous|Solid]

Materials can be created with any number of the following material properties:

Any properties that are not initialized by the user will have a default value of 0.

Materials and media types can be listed and deleted using the following commands:

List Material <id_list|'name'|all>

Delete material <id_list|'name'|all>

List Media <id_list|'name'|all>

Delete Media <id_list|'name'|all>

Materials and media can be added to an existing block using the following command:

Block <id> Material <id|'name'>

Block <id> Media <id|'name'>

The Cubit SDK allows custom material properties to be defined using the MaterialInterface. The following versions of the material commands allow users to create materials with custom properties that have already been defined using the SDK.

Create {material|media} 'material_name' property_group 'group_name' [id <requested_id>] [description 'string']

Modify {material|media} 'material_name' [property_group 'group_name'] [id <requested_id>] [description 'string'] [rename 'new_name'] [scalar_properties ('property_name' <property_value>)...] [vector_property 'property_name' <val1> <val2>...] [matrix_property 'property_name' <val1> <val2>...] [clear properties 'property_name1' 'property_name2'...]

A scalar property has a single value associated with it. The scalar properties defined by Cubit are:

Vector properties are given in the command as a list of values. The vector properties defined in Cubit are:

Matrix properties are also given as a list of values. The number of columns in the matrix is defined by the specific property, and Cubit automatically divides the given values into rows and columns based on the column count. For example, if a matrix property has 2 columns, the value list "2 33.1 3 18.9" is interpreted as the matrix:

Cubit defines the following matrix properties:

A property group is a collection of material properties. Its main purpose is to help define what properties a material should have, even if a value is not given for the property. Cubit defines the following property groups:

Table 1. Property groups defined in CUBIT

---

## Element Block Specification

**URL:** https://coreform.com/cubit_help/finite_element_model/exodus/block_specification.htm

**Contents:**
- Element Block Specification
- Creating Element Blocks
- Assigning a Name or Description to an Element Block
- Defining the Element Type
- Node Constraints for High Order Elements
- Default Element Blocks
- Duplicate Block Elements
- Assigning Attributes to Blocks
- Displaying Element Blocks
- Deleting Element Blocks

Element blocks are the method CUBIT uses to group related sets of elements into a single entity. Each element in an element block must have the same basic and specific element type.

The preferred method for defining blocks is to use geometric entities such as volumes, surfaces or curves. Blocks can also be defined using mesh entities. If a block is defined at a geometric entity, each of the elements owned by the geometry are automatically assigned to the block. Deleting or remeshing the geometry automatically changes the set of elements grouped into the block. If mesh entities are used to specify a block, deleting the mesh will also delete the elements from the block.

Some important notes regarding Element Blocks are as follows:

Element blocks are defined with the following Block commands.

Block <block_id> [ADD|Remove] {Vertex | Node} <range>

Block <block_id> [ADD|Remove] {Curve | Edge} <range>

Block <block_id> [ADD|Remove] {Surface | Face | Tri} <range>

Block <block_id> [ADD|Remove] {Volume | Hex | Tet | Pyramid | Wedge} <range>

Block <block_id> [ADD|Remove] Group <range>

These commands define blocks based on a list of geometric or mesh entities. A block can only hold entities of the same dimensionality. For example, a block defined to hold vertices and nodes cannot also hold hexes. The above commands reflect this restriction. This restriction also applies when adding entities using groups. When creating a block using a group containing entities of different dimensionality the behavior is undefined.

Adding geometric entities to a block effectivily adds all mesh entities of the same dimensionality contained in the geometric entity to the block. For example, adding a volume to a block adds all hexes, tets, pyramids and wedges contained in the volume to the block. Removing geometry entities works in the same manner. Thus the following commands:

Creates block 1 containing all of the hexes, tets, pyramids and wedges in volume 1 except for hex 1.

When a mesh entity, or a meshed geometric entity is put into a block, it is assigned a Global Element ID which is exported to the exodus file for tracking during analysis.

The following commands can be used to assign a name or description to an element block. Assigning a name to a block can be more intuitive than using traditional integer IDs, and the name and description are preserved in DART metadata-enabled applications (like SIMBA). This command is also available for nodesets and sidesets.

Block<ids> Name "<new_name>"

Block<ids> Description "<description>"

Each block must have a specific element type associated with it. To assign an element type to a block, use the following command:

Block <block_id_range> Element Type <type>

Available element types are defined by the Exodus II file format specification (Schoof, 95). CUBIT supports the following element types:

Curves: BAR BAR2 BAR3 BEAM BEAM2 BEAM3 TRUSS TRUSS2 TRUSS3 SPRING

Surfaces: QUAD QUAD4 QUAD5 QUAD8 QUAD9 SHELL SHELL4 SHELL8 SHELL9 HEXSHELL TRI TRI3 TRI6 TRI7 TRISHELL TRISHELL3 TRISHELL6 TRISHELL7

Volumes: HEX HEX8 HEX9 HEX20 HEX27 TETRA TETRA4 TETRA8 TETRA10 TETRA14 TETRA15 PYRAMID PYRAMID5 PYRAMID13 PYRAMID18 WEDGE WEDGE6 WEDGE12 WEDGE15 WEDGE16 WEDGE20 WEDGE21

If the element type is not assigned for an element block, it will be assigned a default type depending on which type of geometry entity is contained in the block. The default values used for element type are:

Volume: 8-node hexahedral elements (HEX8) will be generated for hex meshes. TETRA4 will be generated for tet meshes.

Surface: 4-node shell elements (SHELL4) will be generated for quad meshes and TRISHELL3 for tri meshes.

Curve: 2-node bar elements (BAR2) will be generated.

Node: 1-node elements (SPHERE) will be generated.

Higher order nodes are moved to curved geometry by default. To change this, use the following command:

set Node Constraint {on|off|SMART [tet quality {distortion|NORMALIZED INRADIUS}][threshold <value=0.15>]]}

On means higher order mid-nodes snap to curved geometry. Off means the mid-nodes retain their positions. “smart” means higher order mid-nodes will only snap to geometry if they do not cause quality problems after being moved. Nodes that cannot be moved without causing quality problems are placed at the average location of the element nodes: for edges, this means on the line containing the edge; for 2d elements, this usually means on the plane containing the element.

When the smart option is used, the tet quality and threshold options can also be used. Tet quality indicates the quality metric that will be used for determining whether mid-nodes will be projected or straightened. This option is currently only valid for high order tets (TETRA10) and tris (TRI6). Normalized Inradius or Distortion metrics may be selected as criteria for projections. The threshold value indicates the quality value at which mid-nodes will not be projected. For example, if Normalized Inradius falls below the threshold value, the element edge will be straightened. Those with metrics above the threshold will be projected.

This setting also has an effect when moving nodes with the node <range> move command. If nodes are associated with geometry, they will snap to that geometry after that are moved when node constraint is set to on.

When exporting an ExodusII file, if the user has not specified any Element Blocks, by default element blocks will be written for any meshed volumes. This default behavior can be changed, to write surface, volume, or no meshes by default. This option can be set using the command

Set Default Block [ON|off|Volume|Surface|Curve]

Default behavior, ON, is for the blocks to automatically be written based on their owning geometry. When the OFF setting is used, only the mesh contained in blocks created by the user will be exported. Mesh not in an element block at export time, will not be exported. The export will still succeed and no error will be thrown. If Volume is specified, only elements contained in volumes will have default blocks specified. Similarly, the Surface or Curve argument indicates that only surfaces or curves containing elements will use default blocks, respectively.

When default blocks are used, the IDs for the resulting blocks will be the ID of the owning geometry.

By default, any given element cannot be included in more than one block. However, when using the following command, an element may be included in more than one block. Please note, since material properties are assigned to blocks, using this command to allow duplicate block elements may result in an element being assigned to multiple materials.

Set Duplicate Block Elements {on|OFF}

Cubit stores only a single Global Element ID (GID) for each element. If an element is placed into more than one block, when the model is exported to Exodus, new additional GIDs will be assigned to the element for each additional block that an element is in. These additional GIDs are exported to the exodus file, but Cubit currently only stores and tracks the first GID assigned.

It may be necessary to associate attributes with a specific element block. Attributes are generally integer or floating point values that represent some physical property in the region occupied by the block, such as material properties or shell thickness. To assign the number of attributes for an element block, use the following command:

Block <id_range> Attribute Count <0-20>

CUBIT will store up to 20 attributes per block. Specify the maximum number of attributes to be stored on the block with this command. Once this command has been executed, individual attributes may be set using the following command:

Block <id_range> Attribute Index <index> <value>

The index is an integer from 1 to the maximum count specified in the Block Attribute Count command. The value may be any valid floating point number.

To assign a value to all attributes of an element block, use the command:

Block <block_id_range> Attribute <value>

Text attributes can also be assigned to a block. Each text attribute is defined by a pair of strings. The first string defines the attribute "Label" and the second string defines the attribute "Value."

Block <id_range> Attribute <'Label string'> <'Value string'>

The Value string of a text attribute can be edited by reissuing the command and giving a new Value string. Text attributes can be removed individually by specifying a Label string, or all attributes can be removed.

Block <id_range> Attribute Remove {<'Label String'>|All}

Blocks can be viewed individually with CUBIT by employing the following command:

Draw Block <block_id_range> [Color <color_spec>] [add] [thickness [offset [scale <val>] | include_normal]]

For blocks that are of type SHELL and TRISHELL or one of its variants including the [thickness] keyword and parameters will result in the blocks being color-coded by shell thickness with a corresponding color bar. Blocks can be drawn with their specified thickness, so they visually have a thickness. This thickness can also be scaled in the draw command. Arrows defining the shell normal direction will be displayed as well as a legend showing the thickness values.

Block colors can also be changed using the following command:

Color Block <block_id_range> {color|Default}

All Nodesets, Sidesets and Blocks may be deleted from the model using the following command:

To remove only Blocks, the following may be used:

To remove a specific block, use:

Delete Block <block_id_range>

The block renumber command gives the user the ability to renumber blocks to fit the user's needs. The command is:

Block <id_range> renumber start_id <id> [uniqueids]

The id_range must include existing entities or the command will fail.

The start_id plus the number of entities must specify a new id space that does not overlap with the existing block ids. In other words, if the current block numbers are 100, 105, 106, and 109, a start_id of 102 would suggest new block numbers of 102, 103, 104, and 105. This would cause an id space conflict and the command will fail.

If the user specifies the uniqueids option, then the new entity id space must not conflict with the existing id space of all blocks, nodesets, and sidesets.

block ids: 100, 105, 106, 109

block all renumber start 20

block 20 renumber start 24

block ids: 21, 22, 23, 24

To renumber the elements within a block, see the renumber command

After a mesh has been defined within a volume, it may be useful to use the existing mesh edges as the basis for an element block. Such an element block might be composed of bars or truss type elements that might propagate through a solid medium such as rebar placed in reinforced concrete. Although the Block <id> Edge <range> command could be used for this task, it would prove extremely tedious defining the individual edges to add to the block. To make this process easier, the following command can be used:

Rebar Start <x> <y> <z> Direction <x> <y> <z> [Length <value>] Block <id> [Element Type {bar|bar2|bar3|BEAM|beam2|beam3|truss|truss2|truss3}]

The Rebar command allows the user to specify a starting location for a set of edges and an initial direction. The program will find the closest existing node in the mesh to Start <x> <y> <z> and begin propagating through the mesh in the specified Direction <x> <y> <z>, adding edges to the block as it propagates through the mesh. The edge that is attached to the last node and is within a fixed 30 degrees of the specified direction is added to the block. The Propagation of the edges continues until either the optional Length value is reached or an edge does not meet the Direction criteria. Also required with this command is a block ID. An Element Type can also be specified.

Similarly, you can use the following command which will use the 30 degree cone described above to gather edges from a surface into a single block using the Cartesian x, y, and/or z vectors.

Rebar Surface <range> [x] [y] [z] Block <id> [Element Type {bar|bar2|bar3|BEAM|beam2|beam3|truss|truss2|truss3}] [Propagate]

Another method for generating rebar blocks include the Diagonal/Orthogonal option. This command can only be used on surfaces that have been meshed with the mapping scheme. This command will create a block of edges from the mapped mesh by starting in one corner and gathering edges orthogonally, or creating new edges diagonally based on the option specified, using the parametric coordinate system dictated by the mapping scheme on the surface. The spacing option dictates how many edges are skipped over before starting the next set of rebar edges.

Rebar Surface <range> {Diagonal|Orthogonal} [Spacing <int>] [Block <id> [Element Type {bar|bar2|bar3|BEAM|beam2|beam3|truss}]

CUBIT> rebar surf 1 diagonal spacing 2 block 2

CUBIT> rebar surf 1 orthogonal spacing 3 block 3

A final rebar option allows the user to create or group rebar edges into a specified block using nodes. Edges are created, or gathered, using the ordered list of nodes specified in the command.

Rebar Node <range> [Target Block <id>] [Element Type {bar|bar2|bar3|BEAM|beam2|beam3|truss}]

CUBIT> rebar node 113 105 97 89 81 73 65 57 49 target block 1

A related command for creating curve geometry directly from mesh edges is the Create Curve from Mesh command. See Curve creation for more details.

The block creation tool also allows the user to create a special block of bar elements that can be used as part of the boundary specification. This command creates bar type elements directly without creating any underlying geometry.

The command for creating this type of block is:

Block <id> Joint [Vertex <id> | Node <id> ] Spider {Surface|Curve|Vertex|Face|Tri|Node} <range> [preview] [Element Type {BAR|bar2|bar3|beam|beam2|beam3|truss|truss2|truss3}]

The joint node is the starting location of the bar elements and the spider location is the terminating location of the bar elements. You can specify the joint node as either a node or a vertex. Optionally, if no joint node is specified, a joint node will automatically be created at the centroid of the nodes on the specified terminating location. You can specify the terminating location as either a node, vertex, geometric surface or the face of a mesh entity.

Some analysis codes refer to these bar elements as tied contacts or rigid bar elements. They can be used to tie models together or to enforce specific kinds of boundary conditions. For example, in the figure below a block of beam elements is used to tie a node at the center of the circle to every node on the edge of the circle. This arrangement can be used to enforce circularity but still allow for displacement of the entire circle. This may occur if there are additional structures above the cylinder that are being excluded from the current finite element model. The beam elements were created by a series of commands of the form

block 10 joint node 1 spider node 2 element type beam

The preview option can be included to draw the location of the beam blocks on the screen without actually executing the command.

If geometry (surfaces, curves, or vertices) is specified to define the spider, the spider will be 'tied' to that geometry, meaning:

Figure 1. Beam elements created with the Spider command

Properties for blocks that are beam types (beam, beam2, beam3) have additional commands to define a cross-sectional area. The following command can be used to change the type of cross-sectional area of a beam block:

Block <id> beam_type {CIRCLE|box|rectangle|pipe|ibeam|general}

The dimensions are set by listing them after the keyword beam_dimensions:

Block <id> beam_dimensions <values>

The order in which the values need to be specified are described in the chart below.

If the solver used is to integrate over the section during the simulation, turn section_integration on using the following command:

Block <id> section_integration {ON|off}

The beam normal vector is a vector normal to the plane of motion and tangent to the first bending axis. This vector can be set using the following command:

Block <id> beam_normal <x><y><z>

Order to Specify Dimensions

Spring blocks that will be exported to Abaqus can contain additional properties related to Abaqus springs. Users can specify the spring type, stiffness, and DOFs associated with Abaqus springs. The spring type mapping to Abaqus elements is in the following table.

CUBIT Block Spring Type

The spring type is set using the spring_type keyword. In order to use this command, the block must already have an element type of “SPRING.” If a DOF is associated with a spring, the spring_dof_1 keyword is used to specify the DOF on the first node and spring_dof_2 is used to specify the DOF on the second node (SPRING2 only).

Block <id> [spring_type {NODE_TO_NODE | node_to_node_fixed_axis | node_to_ground}] [stiffness <k>] [spring_dof_1 <n>] [spring_dof_2 <n>]

Sphere elements are created in CUBIT by inserting either nodes or vertices into a block.

Block <id> {node|vertex} <id_range>

The command above causes CUBIT to internally create a sphere element and associate it to the inserted node, or to the node associated to the inserted vertex.

brick x 10 vol all size 5 mesh vol all create vertex 0 0 10 #{sph_vtx_id=Id("vertex")} mesh vertex {sph_vtx_id} #{sph_nd=Id("node")} block 1 volume 1 block 2 vertex {sph_vtx_id} block 3 joint node {sph_nd} spider surf 1 locate sphere all

The example commands above will generate the model illustrated in the figure below.

Figure 2. A sphere element created and connected to a solid mesh with 2d elements.

You can interact with sphere elements in Cubit with the commands below:

locate sphere <id_range>

draw sphere <id_range>

highlight sphere <id_range>

list sphere <id_range>

CUBIT is a 3d mesh generator by default. Element types, by default, are respectively TRISHELL and SHELL for triangle and quad elements. If a 2d mesh is desired, blocks types must be explicitly set to TRI or QUAD.

create brick x 10 surface 1 scheme trimesh mesh surface 1 block 1 surface 1 block 1 element type tri export mesh "mymesh.exo"

Sideset 1 will be based on the TRI and QUAD elements in blocks 1 and 2, with the side numbering referring to the edges of the triangles and quads.

The Set Block Mixed Output command controls the behavior of blocks containing different element types when exporting in a file format that doesn't support blocks with mixed element types. If DEGENERATE, all elements will be exported in one block, but tets and pyramids will be written as degenerate hexes, and triangles will be written as degenerate quads. If OFFSET (set by default), then new element blocks will be created separating the types. Hex and Quad blocks retain the block id, whereas tets, triangle, pyramids and wedges get put into other blocks. The ids of the other blocks are based on the block id plus the offset for that type. Those values are set using the offset commands.

Set Block Mixed Element Output { OFFSET | Degenerate }

Set Block Triangle Offset <value>

Set Block Tetrahedron Offset <value>

Set Block Pyramid Offset <value>

Block <id> Material <id|'name'>

If a material is assigned to an element block, the material properties will be associated with the block's elements when the mesh is exported. If no material is assigned to a block, a default material will be used during export.

Cubit has basic support for Superelements. Importing mesh with Superelements is supported using either the lite, no_geom or geometry options. When using the geometry option to construct Mesh-Based geometry, superelements do not have geometry created, but continue to exist as free elements. Superelements are visually represented as a point cloud since there is no connecting topology. Cubit does not have the ability to create these elements. Importing and exporting these elements is supported.

---

## Exodus Boundary Conditions

**URL:** https://coreform.com/cubit_help/finite_element_model/exodus/model_definitions.htm

**Contents:**
- Exodus Boundary Conditions
- Element Blocks
- Nodesets
- Sidesets
- Element Types

Sandia's finite element analysis codes have been written to transfer mesh definition data in the ExodusII file format (citation Schoof, 95). The ExodusII database exported during a CUBIT session is sometimes referred to as a Genesis database file; this term is used to refer to a subset of an Exodus file containing the problem definition only, i.e., no analysis results are included in the database.

The ExodusII database contains mechanisms for grouping elements into Element Blocks, which are used to define material types of elements. ExodusII also allows the definition of groups of nodes and element sides in Nodesets and Sidesets, respectively; these are useful for defining boundary and initial conditions. Using Element Blocks, Nodesets and Sidesets allows the grouping of elements, nodes and sides for use in defining boundary conditions, without storing analysis code-specific boundary condition types. This allows CUBIT to generate meshes for many different types of finite element codes.

Element Blocks (also referred to as simply, Blocks) are a logical grouping of elements all having the same basic geometry and number of nodes. All elements within an Element Block are required to have the same element type. Access to an Element Block is accomplished through a user-specified integer Block ID. Typically, Element Blocks can also be assigned material properties to associate material properties with a group of elements.

Nodesets are a logical grouping of nodes accessed through a user-specified Nodeset ID. Nodesets provide a means to reference a group of nodes with a single ID. They are typically used to specify load or boundary conditions on portions of the CUBIT model or to identify a group of nodes for a special output request in the finite element analysis code.

Sidesets are another mechanism by which constraints may be applied to the model. Sidesets represent a grouping of element sides and are also referenced using an integer Sideset ID. They are typically used in situations where a constraint must be associated with element sides to satisfactorily represent the physics (for example, a contact surface or a pressure.

The basic elements used to discretize geometry were described in the mesh generation chapter. Within each basic element type, several specific element types are available. These specific element types vary by the number of nodes used to define the element, and result in different orders of accuracy of the element. The element types available for each basic element type defined in CUBIT are summarized in the following table.

Table 1. Element Types Defined in CUBIT

For a description of the node and side numbering conventions for each specific element type, see the Appendix. Element types can be set for individual Element Blocks, either before or after meshing has been performed.

---

## Exodus II File Specification

**URL:** https://coreform.com/cubit_help/finite_element_model/exodus/exodus2_file_specification.htm

**Contents:**
- Exodus II File Specification
- Exodus II Manual
- Element Block Definition Examples
  - Multiple Element Blocks
  - Surface Mesh Only
  - Two-dimensional Mesh

The full Exodus II manual is available from the web.

Multiple element blocks are often used when generating a finite element mesh. For example, if the finite element model consists of a block which has a thin shell encasing the volume mesh, the following block commands would be used:

Block 100 Volume 1 Block 100 Element Type Hex8 Block 200 Surface 1 To 6 Block 200 Element Type Shell4 Block 200 Attribute 0.01 Mesh Volume 1 Export Genesis `block.g'

This sequence of commands defines two element blocks (100 and 200). Element block 100 is composed of 8-node hexahedral elements and element block 200 is composed of 4-node shell elements on the surface of the block. The "thickness" of the shell elements is 0.01. The finite element code which reads the Genesis file (block.g) would refer to these blocks using the element block IDs 100 and 200. Note that the second line and the fourth line of the example are not required since both commands represent the default element type for the respective element blocks.

If a mesh containing only the surface of the block is desired, the first two lines of the example would be omitted and the Mesh Volume 1 line would be changed to, for example

CUBIT also provides the capability of writing two-dimensional Genesis databases similar to FASTQ. The user must first assign the appropriate surfaces in the model to an element block. Then a Quad* type element may be specified for the element block. For example

Block 1 Surface 1 To 4 Block 1 Element Type Quad4

In this case, it is important for users to note that a two-dimensional Genesis database will result. In writing a two-dimensional Genesis database, CUBIT ignores all z-coordinate data. Therefore, the user must ensure that the Element Block is assigned to a planar surface lying in a plane parallel to the x-y plane. Currently, the Quad* element types are the only supported two-dimensional elements. Two-dimensional shell elements will be added in the near future if required.

---

## Finite Element Model

**URL:** https://coreform.com/cubit_help/finite_element_model/finite_element_model.htm

**Contents:**
- Finite Element Model

This chapter describes the techniques used to complete the definition of the finite element model. The definitions of the basic items in an Exodus database are briefly presented, followed by a description of the commands a user would typically enter to produce a customized finite element problem description, and how to export the finite element model.

---

## Global Element IDs

**URL:** https://coreform.com/cubit_help/finite_element_model/element_ids.htm

**Contents:**
- Global Element IDs
- Cubit Mesh Entity ID Spaces
- Global Element IDs
  - Interacting with GlobalElement IDs

All mesh entities have an ID associated with them which is unique within the corresponding mesh entity ID space. For example, a hex will have an id which can be used in commands such as "list hex 17". However, this ID is only unique amoungst the hexahedra in the Cubit session. There could also be a tet, quad, tri, edge, node, etc. with ID 17.

Whenever a hex, tet, quad, tri, etc. gets put into an element block, it is assigned another ID which is called the Global Element ID. The Global Element ID is unique amoungst all element which have been put into any block. Starting in Cubit 14.0, it is exported to the Exodus file format so that downstream analysis applications can map elements back to the corresponding Cubit hex, quad, etc. In Cubit 14.0, Global Element are not supported by the other exporters, but will be in future releases.

After a hex, quad, etc. is placed into an element block, you can see which ID was assigned to it with the list command. For example:

reset bri x 10 mesh vol all block 1 hex all list hex 1

The resulting output will contain the following:

CUBIT> list hex 1 Hex 1 Global Element ID = 1

In this simple example, the Hex ID is the same as the Global Element ID, but this will not always be true.

These Global Element IDs are exported as the global id in the Exodus file. If during an analysis run, a particular element needs to be identified back in the Cubit session, they can be found with any of the following commands:

List element <id_range>

Draw element <id_range>

Highlight element <id_range>

List element <id_range>

Users can control the assigned Global Element ID with the renumber command.

---

## Miscellaneous Boundary Condition Commands

**URL:** https://coreform.com/cubit_help/finite_element_model/non_exodus/miscellaneous.htm

**Contents:**
- Miscellaneous Boundary Condition Commands
- Delete
- List
- Draw
- Highlight

The BC delete keyword combination is used to delete boundary conditions. The current list of all entities that can be deleted using this command were shown in Table 1. Cubit currently has no ‘undo’ command to ‘undelete’ a boundary condition deletion.

Delete {bc_type} [<id-range>|All]

Delete Boundary Conditions

Every set (and boundary condition within them) can be deleted at once by typing delete boundary conditions. This command will delete all boundary conditions from your model.

The List keyword combination is used to list boundary conditions. The current list of all entities that can be listed using this command was shown in Table 1. Cubit’s parser can evaluate boundary conditions given the entities they act on. For example, "List pressure in surface 1" will list all pressures that act on Surface 1.

List {bc_type} [<id-range>]

List Boundary Conditions

Every set (and boundary condition within them) may be listed at once by typing list boundary conditions. CUBIT will list the number of sets and individual boundary conditions in your model. This command will list the total number of each type of set and boundary condition, including boundary conditions that are not a part of a BC set.

Draw {bc_type} {<id-range>|all}[Add]

The draw keyphrase allows a CUBIT user to draw any type of boundary condition. This command will clear the graphics window of every part of the model except for the selected boundary condition. Using the add keyword will permit multiple boundary conditions to be drawn at the same time. Any combination of boundary conditions and entities that were valid for delete and list are also valid for draw.

Highlight {bc_type} {<id-range>|All}

The highlight keyphrase allows a CUBIT user to highlight any boundary condition. Highlighting a boundary condition will turn it bright orange and the vectors defining it will thicken. The highlight command is similar to the draw command.

---

## Nodeset and Sideset Specification

**URL:** https://coreform.com/cubit_help/finite_element_model/exodus/nodesets_and_sidesets.htm

**Contents:**
- Nodeset and Sideset Specification
- Creating Nodesets and Sidesets
  - Useful hint:
- Assigning Names and Descriptions to Nodesets and Sidesets
- Grouping Faces on a Surface into a Sideset
  - Grouping elements in voids and enclosures
- Deleting Nodesets and Sidesets
- Renumbering Nodesets and Sidesets
- Transfer Nodesets and Sidesets
- Displaying Nodesets and Sidesets

Boundary conditions such as constraints and loads are applied to the finite element model using nodesets or sidesets, also known as Genesis entities. Rather than attempting to maintain specific boundary condition information, such as load, temperature, constraint, etc., Genesis entities are the generic vehicle for the user to set up boundary conditions on the model. Nodes, elements and element faces are instead grouped together and assigned unique IDs. Node, element and face IDs assigned to Genesis entities can then be written to the Exodus II mesh file. Once imported to the intended analysis application, the nodeset and sideset IDs can be appropriately interpreted as specific physical boundary conditions.

The preferred method for creating Genesis entities is to assign vertices, curves, surfaces or volumes to a specific nodeset or sideset ID. Any mesh entity owned by the geometric entity in a nodeset or sideset is automatically assigned to the same nodeset or sideset. This allows greatest flexibility in generating and updating the finite element mesh. For example, if a surface belongs to a specific sideset, remeshing the surface will automatically delete any old faces from the sideset and add the faces of the new mesh.

In some cases, the geometric model does not provide enough resolution to define the desired boundary conditions. In this case, the model may be partitioned using CUBIT's virtual geometry features. Where this may not be feasible, mesh entities can also be added directly to the desired nodeset or sideset. Where individual mesh entities have been added to nodesets or sidesets, deleting the mesh will also remove these elements from the Genesis entity. If the geometry is remeshed, the new mesh entities must also be added once again to the nodesets or sidesets.

Nodesets can be created from groups of nodes categorized by their owning volumes, surfaces, curves or vertex. Individual nodes may also be added to a nodeset. Nodes can belong to more than one nodeset.

Sidesets can be created from groups of element sides or faces categorized by their owning surfaces or curves or by their individual face IDs. Element sides and faces can also belong to more than one sideset.

Nodesets and Sidesets are created in CUBIT by assigning the appropriate geometry or mesh entities in the model to a nodeset or sideset ID. The following commands can be used:

Nodeset <nodeset_id> [ADD|Remove] {Curve | Surface | Volume | Vertex | Node} <range>

Sideset <sideset_id> [ADD|Remove] Group <id_range>

Sideset <sideset_id> [ADD|Remove] {Curve|Surface|Edge|Face|Tri} <id_range>

Sideset <sideset_id> [Add] Edge <id_range> [wrt {{Tri|Face} <id_range> | all } ]

Sideset <sideset_id> [Add] Face <id_range> [wrt {Hex <id_range> | all} ]

Sideset <sideset_id> [Add] Tri <id_range> [wrt {Tet <id_range> | all} ]

Sideset <sideset_id> [Add] Surface <id_range> [wrt {{Volume|Surface} <id_range> | all} ] [FORWARD|Reverse|Both]

Sideset <sideset_id> [Add] Curve <id_range> [wrt {Surface <id_range> | all} ]

Like element blocks, Nodesets and Sidesets are given arbitrary, user-defined ID numbers. If there are no user-defined Nodesets or Sidesets, none are written to the Exodus II file.

With Sidesets, direction is often important. For surfaces, the direction may be specified using the Forward, Reverse, or Both options. The Forward option will write a sideset in relation to hexes in the surface's forward volume, which is the volume that the surface's normal points away from. The Reverse option will write a sideset in relation to hexes in the surface's reverse volume, which is the volume that the surface's normal points into. The Both option will allow sidesets to be written in relation to the hexes that lie in volumes on both sides of the surface. The default is Forward. The user can additionally specify the volume from which the hexes should be taken in relation to by using the wrt Volume option.

Direction is equally important for curves in Sidesets. The wrt Surface option allows the user to indicate which surface's faces will be included in the Sideset. The wrt All option will include all faces attached to the curve. The default is wrt All.

When creating nodesets and sidesets it is often userful to use the Extended Command Line Entity Specification. Here is an example that creates a nodeset which includes all the nodes on the exterior of the geometry:

# Create the geometry Create brick x 10 Create cylinder height 10 radius 2 Move volume 2 z 10 # Merge the geometry Merge volume all # Mesh the geometry Mesh volume all # Create a nodeset that includes only those nodes # located on the exterior of the geometry Nodeset 1 add surface in volume all with not is_merged

The following commands remove nodes from the nodeset that belong to a surface. Continuing from the previous example:

# Remove surface 2 from the nodeset Nodeset 1 remove surface 2 # Remove nodes from the nodeset # that belong to the curves that bound surface 2 Nodeset 1 remove node in curve in surface 2

Nodes can also be added or removed based upon their coordinates. Here is an example that removes all the nodes with a z coordinate equal to 15. Continuing from the previous example:

# Remove the nodes with a z coordinate equal to 15 Nodeset 1 remove node in surface all with z_coord = 15

Nodesets and sidesets can be assigned names and descriptions. Using names and descriptions is often more intuitive than using traditional integer IDs. When exporting a mesh as a DART artifact, names and descriptions are included in the metadata, making them available to DART metadata-enabled applications such as SIMBA. To give a name or description to nodeset or sideset, use one of the following commands:

{Nodeset|Sideset} <ids> Name "<new_name>"

{Nodeset|Sideset} <ids> Description "<description>"

This command can also be used to define names and descriptions for Element Blocks.

SideSet <sideset_id> Surface <id_range> Patch Maximum <x> <y> <z> Minimum <x> <y> <z>

SideSet <sideset_id> Surface <id_range> Patch Center <x> <y> <z> Radius <value> [Filter] [Partition]

SideSet <sideset_id> Surface <id_range> Patch Center <x> <y> <z> Outer_radius <value> Inner_radius <value> [Filter] [Partition]

SideSet <sideset_id> Surface <id_range> Patch Cylinder <axis_specification> Radius <rad> [Filter] [Partition]

SideSet <sideset_id> Surface <id_range> Patch Cylinder <axis_specification> Outer_radius <rad> Inner_radius <rad> [Filter] [Partition]

These commands place only the faces meeting the specified criteria into the sideset.

Normally, these commands place the individual elements into the sideset. If the mesh on the surface is deleted, the elements will be removed from the sideset. If the surface is then remeshed, new elements will NOT automatically be added to the sideset. This is usually the intended behavior.

If the filter option is included, only a single connected set of elements is added to the sideset. If the shape of the surface is such that multiple disconnected sets of elements fall within the specified spherical or cylindrical region, the filter option will limit the faces added to the sideset to the one set closest to center.

Using the partition option changes this behavior. The partition option causes the surface to be split, based on the faces included in the patch. The newly created patch surface will be added to the sideset instead of the individual elements. If the mesh is deleted and a new mesh is generated, the new mesh on the patch surface will automatically be included in the sideset, just as occurs with other geometric entities assigned to sidesets.

Note that the sideset patch commands work with both triangular and quadrilateral faces.

Sideset Start <id> Enclosure {Volume|Hex|Tet} <range>

All Nodesets, Sidesets and Blocks may be deleted from the model using the following command:

To remove only nodesets or sidesets, the following may be used:

To remove a specific nodeset or sideset, use:

Delete Nodeset <nodeset_id_range>

Delete Sideset <sideset_id_range>

The nodeset and sideset renumber commands give the user the ability to renumber these entities to fit the user's needs. The command is:

{Nodeset|Sideset} <id_range> renumber start_id <id> [uniqueids]

sideset ids: 1, 2, 4, 6, 10

sideset all renumber start 30

sideset ids: 30, 31, 32, 33, 34

The id_range must specify existing nodesets or sidesets, respectively, or the command will fail.

The new ids to be assigned cannot contain the id of an existing nodeset (when renumbering nodesets), or an existing sideset (when renumbering sidesets).

For example, given sidesets with ids 100, 105, 106, and 109, the command

sideset all renumber start_id 102

would attempt to renumber the sideset ids to 102, 103, 104, and 105. Since sideset 105 already exists, the command will fail.

When the uniqueids option is specified, the new ids to be assigned cannot contain the id of an existing nodeset OR an existing sideset OR an existing block. For example, given sidesets with ids 100, 105, 106, and 109, and given blocks with ids 201, 202, and 203, the command

sideset all renumber start_id 200 uniqueids

would attempt to renumber the sideset ids to 200, 201, 202, and 203. While this does not conflict with existing sideset ids, it does conflict with the existing block ids and so the command will fail.

The capability shown in the below figure automates the transfer of sidesets and nodesets from the source mesh (e.g. design domain model) to the target mesh (e.g. topology optimized shape). Transfer of sidesets and nodesets was a user-intensive, error-prone, bottleneck as users were required to go through the painful step of manually selecting elements to define equivalent sidesets on the target mesh.

The commands to automatically transfer nodesets and sidesets are given below:

transfer nodeset <ids> onto {tri <ids> |face <ids> |tet <ids> |hex <ids> } [tolerance <value> ]

transfer sideset <ids> onto {tri <ids> |face <ids> |tet <ids> |hex <ids> } [tolerance <value> ] [log]

tri <ids> and face <ids> : if the target mesh is a surface mesh, use tri or face option.

tet <ids> and hex <ids>: this option can be used and the boundary skin mesh of the volumetric mesh will be extracted automatically to associate skin elements and nodes to the sidesets and nodesets, respectively.

tolerance <value>: The tolerance option must be used only if the default smart local tolerance doesn’t give the desired results.

log : The log option outputs the area of sidesets in source and target meshes and the ratio of the areas. The below table shows an example output. For example, the area_ratio can be used to adjust the pressure boundary conditions to maintain same forces.

Log output of transfer sideset command

#!python import cubit cubit.init(['cubit','-nojournal’]) # STEP 1: import the source mesh as mesh based geometry (MBG); delete mesh and blocks cubit.cmd('import mesh geometry "design_domain_mesh.exo" feature_angle 135.00 merge ') cubit.cmd('del mesh') cubit.cmd('del block all’) # STEP 2: import the target mesh as a free mesh cubit.cmd('import mesh "optimized_mesh.exo" no_geom’) # STEP 3: transfer sideset and nodeset from the source mesh to the target mesh cubit.cmd('transfer sideset all onto tet all’) cubit.cmd('transfer nodeset all onto tet all’) # STEP 4: export optimized mesh with sidesets cubit.cmd('export mesh \'optimized_mesh_with_bc.exo\' block all sideset all nodeset all')

Nodesets and Sidesets can be viewed individually through CUBIT by employing the following commands:

Draw NodeSet <nodeset_id_range> [Color <color_spec>] [add]

Draw SideSet <sideset_id_range> [Color <color_spec>] [add]

Nodeset and Sideset colors can also be changed using the following commands:

Color NodeSet <nodeset_id_range> {color|Default}

Color SideSet <sideset_id_range> {color|Default}

Nodesets can be used to store geometry associativity data in the Exodus II file. This data can be used to associate the corresponding mesh to an existing geometry in a subsequent CUBIT session. This functionality can be used either to associate a previously-generated mesh with a geometry (See Importing an Exodus II File), or to associate a field function with a geometry for adaptive surface meshing (See Adaptive Meshing).

The commands to control and list whether associativity data is written or read from an Exodus II files are the following:

List Import Mesh NodeSet Associativity

List [Export Mesh] NodeSet Associativity

List [Export Mesh] NodeSet Associativity Complete

set Import Mesh NodeSet Associativity [ON|off]

[set] [Export Mesh] NodeSet Associativity [on|OFF]

[set] [Export Mesh] NodeSet Associativity Complete [On|OFF]

Associativity data is stored in the Exodus II file in two locations. First, a nodeset is written for each piece of geometry (vertices, curves, etc) containing the nodes owned for that geometry. Then, the name of each geometry entity is associated with the corresponding nodeset by writing a property name and designating the corresponding nodeset as having that property. Nodeset numbers used for associativity nodesets are determined by adding a fixed base number (depending on the order of the geometric entity) to the geometric entity id number. The base numbers for various orders of geometric entities are shown in the following table. For example, nodes owned by curve number 26 would be stored in associativity nodeset 40026.

Table 1. Nodeset ID base numbers for geometric entities

Instead of storing just the nodes owned by a particular entity, nodes for lower order entities are also stored. For example, the associativity nodeset for a surface would contain all nodes owned by that surface as well as the nodes on the bounding curves and vertices.

By default, distribution factors on nodesets or sidesets are written with a constant value of "1" at each node. It is also possible to vary the distribution factor for each node in a nodeset or sideset, using an equation to control the value of the distribution factor at each node. To do so, an equation must first be defined using the command:

Create Equation "<expression>" name "<name>"

where expression is any mathematical expression which evaluates to a single number, and name is the name by which this equation will be known. The expression is written using aprepro syntax, with a few differences from the use of APREPRO in its usual context.

x - The x-coordinate of the current node y - The y-coordinate of the current node z - The z-coordinate of the current node n - The CUBIT ID of the current node. This is the ID of the node in CUBIT, which may not be the same as the node's ID in the Exodus II file.

For example, to define an equation which varies from -10 to 10 based on the sine of the node's x_coordinate:

Create Equation "10*sin(x)" Name "my_equation"

Once an equation has been defined, it can be applied to a nodeset or sideset:

Nodeset <id> Distribution Equation "<equation_name>"

Sideset <id> Distribution Equation "<equation_name>"

For example, to apply the equation created earlier to nodeset 10:

Nodeset 10 Distribution Equation "my_equation"

When nodeset 10 is written to an Exodus II file, "my_equation" will be evaluated once for each node in the nodeset, with the values of x, y, z, and n set to appropriate values for the node. The result is used as the distribution factor for that node.

Here is a complete example that writes out the distribution factors 0.0, 0.5, and 1.0 for the 3 nodes on the curve:

# Create a straight line from (0,0,0) to (1,0,0) create vertex 0 0 0 create vertex 1 0 0 create curve vertex 1 2 # Mesh with 3 nodes curve 1 interval 2 mesh curve 1 # Create a block and a nodeset block 1 curve 1 nodeset 1 curve 1 # Define an equation and apply it to the nodeset create equation "x" name "simple_eq" nodeset 1 distribution equation "simple_eq" # Write the mesh export mesh "temp.g" overwrite

Here is another complete example that varies the distribution factors for sideset 20 from zero to 1, depending on the node's x-coordinate. The sideset is applied to sides of HEX20 elements, so each element side has 8 different distribution factors.

# Mesh a cube brick x 10 mesh volume 1 # Create a block of 20-noded hexes block 1 volume 1 block 1 element type hex20 # Apply a sideset to be used for a variable pressure sideset 20 surface 1 # Define an equation and apply it to the sideset create equation "(x+5)/10" name "zero_to_one" sideset 20 distribution equation "zero_to_one" # Write the mesh export mesh "temp.g" overwrite

Note that distribution equations only affect Exodus II output. Equations are currently ignored for other mesh file types.

See APREPRO in the appendix.

The below commands can be used to set the behavior of bc (boundary contitions of nodesets/sidesets/blocks) propagation when a geometric entity is copied. The default OFF option specifies that any bc containing the copied geometry and/or mesh of the copied geometry will not be contained in a bc. The use_original option will add the new, copied geometry and/or mesh into the existing bc. The on option will create new bcs, containing the copied geometry and/or mesh, mirroring the original bcs.

set copy_nodeset_on_geometry_copy [on | OFF| use_original]

set copy_sideset_on_geometry_copy [on | OFF| use_original]

set copy_block_on_geometry_copy [on | OFF| use_original]

---

## Node and Nodeset Repositioning

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/node_nodeset_repositioning.htm

**Contents:**
- Node and Nodeset Repositioning

A capability to reposition nodesets and individual nodes is provided. This capability will retain all the current connectivity of the nodes involved, but it cannot guarantee that the new locations of the moved nodes do not form intersections with previously existing mesh or geometry. This capability is provided to allow the user maximum control over the mesh model being constructed, and by giving this control the user can possible create mesh that is self-intersecting. The user should be careful that the nodes being relocated will not form such intersections.

The user can reposition nodes appearing in the same nodeset using the NodeSet Move command. Moves can be specified using either a relative displacement or an absolute position. The command to reposition nodes in a nodeset is:

Nodeset <nodeset_list> Move <delta_x> <delta_y> <delta_z>

Nodeset <nodeset_list> Move To <x_pos> <y_pos> <z_pos>

The first form of the command specifies a relative movement of the nodes by the specified distances and the second form of the command specifies absolute movement to the specified position.

Individual nodes can be repositioned using the Node Move command. Moves are specified as relative displacements. The command syntax is:

Node <range> Move <delta_x> <delta_y> <delta_z>

Node <range> Move {[X <val>] [Y <val>] [Z <val>]}

Node <range> Move Normal to Surface <id> distance <val>

Node <range> Move Closest Surface <id> distance <val>

Nodes can also be repositioned using a location or direction specification. See Location, Direction, and Axis Specification for details on the location and direction specification. The command syntax is:

Node <range> Move Location <options>

Node <range> Move Direction <options>

If node constraint is set to on then nodes will snap to geometry that they are associated with after the move. This only happens with the node move command and not with nodeset move. This behavior can be turned off with

set node constraint off

See also Transforming Mesh Coordinates.

---

## Using Contact Surfaces

**URL:** https://coreform.com/cubit_help/finite_element_model/non_exodus/contact.htm

**Contents:**
- Using Contact Surfaces
- The Contact Region
- The Contact Pair
- Auto-Contact Tool

To define contact between two entities, Cubit requires each entity to be defined as a separate contact region. Each region can be made up of multiple 1D or 2D entities.

Create Contact Region [id] [Name <'name'>] [{Add|On} {Sideset|Surface|Curve|Face|Tri|Edge} <entity_list>]

Modify Contact Region {id_list|'name'|All} [Name <'name'>] [{Add|Remove} {Sideset|Surface|Curve|Face|Tri|Edge} <entity_list>]

create contact pair [id] [name <'name'>] [primary contact region <id|'name'>] [secondary contact region <id|'name'>] [friction <value>] [tolerance <value>] [tied {on|OFF}] [General <on|OFF> [Exterior <on|OFF>]]

modify contact pair {id_list|'name'|all} [name <'name'>] [primary contact region <id|'name'>] [secondary contact region <id|'name'>] [friction <value>] [tolerance <value>] [tied {on|OFF}] [General <on|OFF> [Exterior <on|OFF>]]

A contact pair is composed of two contact regions. One region will be the ‘primary’ surface, and the other will be the ‘secondary.’ 2D contact regions can not be mixed with 1D contact regions. The friction coefficient can also be included. The tolerance keyword is currently unused. Use the tied keyword to specify that the contact is to define tied contact between the two contact regions, essentially “gluing” the parts together. Currently, this option is only available when using the Abaqus Exporter.

The General keyword can be used to specify general (i.e. global) contact without specifying surfaces/curves to use as contact pairs. Currently, this keyword is only valid when exporting to Abaqus. If the Exterior keyword is used with the General keyword, then Abaqus will consider all exterior surfaces when determining contact regions. If the Exterior keyword is omitted, then the user must provide a primary contact region and/or a secondary contact region.

With the auto-contact tool, Cubit can search for contact pairs and automatically set up all of the necessary contact regions and contact pairs.

Create Contact Autoselect [{Volume|Surface|Curve} <ids>] [Primary Volume <id>] [Maxgap <value>] [Curve_Contact]

The optional geometry list can be used to limit Cubit’s search to only a subset of entities. If this list is omitted, all bodies in the model will be searched. The optional primary volume keyword can be used to tell Cubit which volume should be used as the primary contact region. If this keyword is omitted, the user will not have control over which volume is the primary region. The maxgap keyword can be used to control how Cubit searches for contact regions. This value is used as the maximum amount of gap that can exist between two surfaces and be identified as a contact region. If this keyword is omitted, the geometry tolerance is used. The curve_contact keyword can be used to indicate the model requires curve contact as opposed to surface contact.

---

## Using Loads

**URL:** https://coreform.com/cubit_help/finite_element_model/non_exodus/loads.htm

**Contents:**
- Using Loads
- Forces
- Using Pressure
  - Value
  - Pressure and Total Force
  - Top and Bottom
- Using Heat Flux
  - Top and Bottom Values
- Using Convection
  - Surrounding

Create Force [id] [Name <'name'>] [ {Add|On} {Nodeset|Surface|Curve|Vertex|Face|Tri|Edge|Node} <entity_list>] [Force Value <val>] [Moment Value <val>] [Direction { direction_options}]

Create Force [id] [Name <'name'>] [ {Add|On} {Nodeset|Surface|Curve|Vertex|Face|Tri|Edge|Node} <entity_list>] [ Vector <val> <val> <val> <val> <val> <val>]

Modify Force {id_list|'name'|all} [Name <'name'>] [ {Add|Remove} {Nodeset|Surface|Curve|Vertex|Face|Tri|Edge|Node} <entity_list>] [Force Value <val>] [Moment Value <val>] [Direction { direction_options}]

Modify Force {id_list|'name'|all} [Name <'name'>] [ {Add|Remove} {Nodeset|Surface|Curve|Vertex|Face|Tri|Edge|Node} <entity_list>] [ Vector <val> <val> <val> <val> <val> <val>]

A CUBIT user has the ability to create forces on 0D, 1D, and 2D entities. A force can be created using the direction syntax (see Specifying Direction). If the vector keyword is used, the first three values are the force components, and the last three values are the moment components.

The use of the force and moment keywords specify the type of load. If both a force and a moment are to be applied, first create one of them, then modify it to add the other. Note that every instance of a force or moment keyword must have an accompanying value keyword.

Regarding force and moment keywords, the following detail may be helpful:

A user may create a force and moment at the same time, but can only specify a direction once. If the force and moment have the same unit vector, it will be successful. If a users wants to create a force in the direction 1,2,3 and a moment in the direction 1,0,0, the user will have to create one, then add the other by modifying it.

Create Pressure [id] [Name <'name'>] [{Add|On} {Sideset|Surface|Curve|Face|Tri|Edge} <entity_list>] [Magnitude <value>] [TOP|Bottom] [PRESSURE|Totalforce]

Modify Pressure {id_list|'name'|all} [Name <'name'>] [{Add|Remove} {Sideset|Surface|Curve|Face|Tri|Edge} <entity_list>] [Magnitude <value>] [TOP|Bottom] [PRESSURE|Totalforce]

Cubit users can create pressure boundary conditions on 1D and 2D entities. Positive surface pressures acting on solid elements are defined as pointing into the face of the elements. Pressures are always normal to the face. For shells and independent surfaces, a ‘left-hand-rule’ is employed. Point your left thumb at the surface in question. If the direction your fingers curl matches the direction of ascending vertex numbering, the direction of the pressure vectors will match the direction of your thumb.

The value variable is the magnitude of the pressure boundary condition. If the user leaves this value blank, CUBIT will assign the pressure magnitude to zero (possibly a trivial case) and issue a warning. Typing a negative value will not flip the direction of the pressure arrows on the display; instead, the pressure magnitude will be negative.

The pressure and totalforce keywords are used to modify the pressure boundary condition. The pressure keyword is the default. All pressures applied with this keyword present (or with both of these keywords absent from the command string) are pure pressures. If the user enters the totalforce keyword, the pressure magnitude is divided by the area of the surface the pressure is acting on (or the length of the curve, for a curve pressure). In effect, the user is entering a force that is treated and exported as a pressure.

Create Heatflux [id] [Name <'name'>] [{Add|On} {Sideset|Surface|Curve|Face|Tri|Edge} <entity_list>] [Value <value>]

Create Heatflux [id] [Name <'name'>] [{Add|On} {Sideset|Surface|Face|Tri} <entity_list>] [Top <value> Bottom <value>]

Modify Heatflux {id_list|'name'|All} [Name <'name'>] [{Add|Remove} {Sideset|Surface|Curve|Face|Tri|Edge} <entity_list>] [Value <value>]

Modify Heatflux {id_list|'name'|All} [Name <'name'>] [{Add|Remove} {Sideset|Surface|Face|Tri} <entity_list>] [Top <value> Bottom <value>]

A CUBIT user may apply heat flux boundary conditions to 1D and 2D entities, including thin-shell elements.

Heat fluxes can be applied to thin-shell elements as well. The same rules apply to thin-shell heat fluxes as to thin-shell temperatures: thin-shell heat fluxes can only be applied to surfaces and heat flux boundary conditions cannot contain regular and thin-shell heat flux values (see journal below). However, thin-shell heat flux commands do not contain gradient or middle keyword options. Only top and bottom keywords are supported.

Create Convection [id] [Name <'name'>] [{Add|On} {Sideset|Surface|Curve|Face|Tri|Edge} <entity_list>] [Surrounding {<value>| Top <value> Bottom <value>} Coefficient {<value>| Top <value> Bottom <value>}]

Modify Convection [id] [Name <'name'>] [{Add|On} {Sideset|Surface|Curve|Face|Tri|Edge} <entity_list>] [Surrounding {<value>| Top <value> Bottom <value>} Coefficient {<value>| Top <value> Bottom <value>}]

A Cubit user can apply convection boundary conditions to 1D and 2D entities. Convection is a transport of thermal energy that is proportional to the difference between the surface temperature and the temperature of the surroundings.

The surrounding keyword specifies the temperature surrounding the entity with the convection boundary condition.

The coefficient keyword is a convection coefficient, in units of energy per length times time times temperature (i.e., [energy]/([length]*[time]*[temperature]) ).

---

## Using Restraints

**URL:** https://coreform.com/cubit_help/finite_element_model/non_exodus/restraints.htm

**Contents:**
- Using Restraints
- Displacements/Accelerations/Velocities
  - Fixed or Free
  - Displacement Combinations
- Temperature
  - Top, Gradient, Middle, Bottom

A CUBIT user has the ability to create displacement boundary conditions on most geometric entities found within Cubit.

Create Displacement [id] [Name <'name'>] [{Add|On} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [DOF {All|{[1][2][3][4][5][6]}} Fix <value>] [SmallestCombine|Average|LargestCombine|OVERWRITE]

Modify Displacement {id_list|'name'|all} [name <'name'>] [{Add|Remove} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [DOF {All|{[1][2][3][4][5][6]}} {Fix <value>|Free}] [SmallestCombine|Average|LargestCombine|OVERWRITE]

Create Acceleration [id] [Name <'name'>] [{Add|On} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [DOF {All|{[1][2][3][4][5][6]}} Fix <value>] [SmallestCombine|Average|LargestCombine|OVERWRITE]

Modify Acceleration {id_list|'name'|all} [name <'name'>] [{Add|Remove} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [DOF {All|{[1][2][3][4][5][6]}} {Fix <value>|Free}] [SmallestCombine|Average|LargestCombine|OVERWRITE]

Create Velocity [id] [Name <'name'>] [{Add|On} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [DOF {All|{[1][2][3][4][5][6]}} Fix <value>] [SmallestCombine|Average|LargestCombine|OVERWRITE]

Modify Velocity {id_list|'name'|all} [name <'name'>] [{Add|Remove} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [DOF {All|{[1][2][3][4][5][6]}} {Fix <value>|Free}] [SmallestCombine|Average|LargestCombine|OVERWRITE]

A number of required and optional keywords make the BC create displacement command one of the more complicated of the boundary condition commands. These keywords will be examined individually in detail.

The dof keyword is the heart of this command. It specifies how to constrain the entity in question. The keyword is an abbreviation for ‘degree of freedom’. Typing the optional keyword all tells CUBIT that the entered command will encompass all six degrees of freedom. The degrees of freedom (1 - 6) are defined below in Table 2.

Table 2: CUBIT definitions of the six degrees of freedom.

CUBIT will allow displacement commands to be applied upon between one and all six of the degrees of freedom. The degrees of freedom do not need to be entered in any order. The command strings ‘ 1 2 3 4 5 6 ‘ ‘2 6 1 4 3 5’ and ‘all’ will end with the same result.

The fix and free keywords tell CUBIT whether an entity’s displacement defined by the dof keyword is to be enforced with a finite value or not. If the displacement is fixed, the entity will be constrained in the pre-specified degrees of freedom. A decimal number entered after the fix keyword will be the value of the enforced degree(s) of freedom. CUBIT allows the user to leave this value blank if the enforced displacement is to be zero, for convenience. However, entering ‘0’ is still permitted. If a user wishes to remove a displacement from an entity, he or she should just delete it rather than trying to set all of the degrees of freedom to free.

The SmallestCombine, Average and LargestCombine keywords deal with displacement combinations. These keywords only apply when a user is modifying an existing displacement boundary condition.

The SmallestCombine keyword will compare the existing displacement values with the current (residing on the command line) displacement values. The keyword will modify the displacement to the match the displacements dictated by the boundary condition that has the smallest absolute value. If the boundary condition with the smallest absolute value is the existing value, the displacement boundary condition will be unchanged. If the current boundary condition has a smaller absolute value than the existing displacement, the displacement boundary condition will be changed to incorporate the new values.

The Average keyword will average the existing displacement values with the current (residing on the command line) displacement values. Note that these averages are not continually updated (i.e., they are not weighted). If a user created a displacement boundary condition and constrained a degree of freedom to 10.0 and then constrained the same degree of freedom to 20.0 with the Average keyword, the new displacement value would be 15.0. But if a user constrained the same degree of freedom to 30.0, while using the Average keyword, the new displacement value would be 22.5 ([15+30]/2), not 20.0 ([10+20+30]/3).

The LargestCombine keyword will compare the existing displacement values with the current (residing on the command line) displacement values. The keyword will modify the displacement to the match the displacements dictated by the boundary condition that has the largest absolute value. If the boundary condition with the largest absolute value is the existing value, the displacement boundary condition will be unchanged. If the current boundary condition has a larger absolute value than the existing displacement, the displacement boundary condition will be changed to incorporate the new values.

When none of these keywords are specified, CUBIT will combine displacements in its default mode, Overwrite. The Overwrite keyword overwrites the entity’s previous displacement boundary condition(s) with the displacement values specified in the command.

CUBIT can create temperature boundary conditions on most geometric and mesh entities. The temperature boundary condition can also be applied to thin-shell elements.

Create Temperature [id] [Name <'name'>] [{Add|On} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [Value <val>]

Create Temperature [id] [Name <'name'>] [{Add|On} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [{ Top <val> Bottom <val> | [Middle <val>] [Gradient <val>] } ]

Modify Temperature {id_list|'name'|all} [name <'name'>] [{Add|Remove} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [Value <val>]

Modify Temperature {id_list|'name'|all} [name <'name'>] [{Add|Remove} {Nodeset|Volume|Surface|Curve|Vertex|Hex|Tet|Face|Tri|Edge|Node} <entity_list>] [{ Top <val> Bottom <val> | [Middle <val>] [Gradient <val>] } ]

---
