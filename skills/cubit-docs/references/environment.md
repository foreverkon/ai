# Coreform-Cubit-Docs-Skill_Docs - Environment

**Pages:** 91

---

## APREPRO Journaling

**URL:** https://coreform.com/cubit_help/appendix/aprepro/aprepro_journaling.htm

**Contents:**
- APREPRO Journaling
- APREPRO Comments
- Significant Figures
- Loops and Journaling
- Multi-line Strings

When using APREPRO, statements can be echoed to a journal file. To do so, use the following command:

[set] Journal [Graphics|Names|Aprepro|Errors] [on|off]

Simply typing "journal aprepro" without an argument will display the current aprepro journaling setting.

if aprepro journaling is ON, or

if aprepro journaling is off. The default is ON.

Comments are also journaled. This is useful for documenting aprepro definitions and descriptions.

Comments on the same line as a command get split into two separate lines in the journal file.

When journal aprepro is ON, numbers are journaled exactly as they are entered. The maximum number of significant digits is determined by the command input.

When journal aprepro is off, numeric results of aprepro statements are journaled according to the maximum number of significant digits hard-coded into CUBIT, using the value of DBL_DIG.

Loops are not journaled as loops, per se. For example, the APREPRO expression:

Multi-line strings are currently not journaled (both definitions and when they are expanded). For example,

Note that bri x 10\n mesh vol 1 was not journaled as {line}

---

## Assembly Tool

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/assembly_tool.htm

**Contents:**
- Assembly Tool
- Metadata Attributes
- Another View

In Cubit versions prior to 15.4 assembly data was managed on the model tree. Beginning with Cubit version 15.4 a power tool for assemblies is available.

A detailed, command-based discussion of assemblies and metadata can be found here.

Figure 1 - Assembly Power Tool

Like all other power tools in Cubit, the user is encouraged to experiment with the various options found in context menus. The context menus are specific to the entity type selected.

Figure 2 - Assembly Context Menu

Users have access to the following attributes:

At the top of the tool is a pull down menu. This allows the user to change from the full assembly view to a parts view.

Figure 3 - Pull down Menu

---

## Automatic Journal File Creation

**URL:** https://coreform.com/cubit_help/environment_control/recording_and_playback/automatic_creation.htm

**Contents:**
- Automatic Journal File Creation
- Controlling Automatic Journal File Creation
- Recording Graphics Commands
- Recording Entity IDs and Names
- Recording APREPRO Commands
- Recording Errors

By default, CUBIT automatically creates a journal file each time it is executed. The file is created in the current directory, and its name begins with the word "cubit", followed by a number starting with cubit01.jou and continuing up to a maximum of cubit999.jou. It is recommended that the user keep no more than around 100 journal files in any directory, to avoid using up disk space and causing confusion. To that end, when the journal name increments to more than cubit99.jou, a warning will be given on startup telling the user that there are at least 99 journal files, and to please clean out unused files. If the user has up through cubit999.jou, then the user is warned that there are too many journal files in the current directory, and cubit999.jou will be re-used, destroying the previous contents.

When starting cubit, the choice of journal file name will depend on the existence of other cubitXX.jou files. Cubit will fill in gaps, starting with the lowest number. For example, if there are already journal files with names cubit01.jou, cubit02, jou, and cubit04.jou, then Cubit will use cubit03.jou as the current journal file.

Journal file names end with a ".jou" extension, though this is not strictly required for user-generated journal files. If no journaling is desired, the user may start CUBIT with the -nojournal command line option or use the command :

[Set] Journal {Off | On}

Turning journaling back on resumes writing commands to the same journal file.

Most CUBIT commands entered during a session are journaled; the exceptions are commands that require interactive input (such as Zoom Cursor), some graphics related commands, and the Playback command.

All graphics related commands may be enabled or disabled with the command:

Journal Graphics {On | Off}

The default is Journal Graphics Off .

When an entity is specified in a command using its name, the command may be journaled using the entity name, or by using the corresponding entity type and id. The method used to journal commands using names is determined with the command:

Journal Names {On | Off}

The default is Journal Names On .

If an entity is referred to using its entity type and id, the command will be journaled with the entity type and id, even if the entity has been named.

APREPRO commands may be echoed to the journal file using the following command

[set] Journal [Graphics|Names|Aprepro|Errors] [on|off]

See APREPRO Journaling for more information.

The default mode for CUBIT is to not journal any command that does not execute successfully. To turn this mode off and echo all commands to the journal file, regardless of the success status, use the following command:

Journal Errors {On|OFF}

If a command did not execute successfully and the journal errors status is ON, then the unsuccessful command will be written as a comment to the file. For example an unsuccessful command might look like the following in the journal file

## create brick x 10 x 10 z 10

Since CUBIT recognizes this as erroneous syntax, it will issue an error when the command is issued, but will still write the command to the journal file as a comment, prefixing the command with "##".

This option may be useful when tracking or documenting program errors.

---

## Beams and Shells with the Geometry Power Tool

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/beams_and_shells.htm

**Contents:**
- Beams and Shells with the Geometry Power Tool
- Background
- Thin Volumes
  - Thin Volume Solutions
  - Deleting Reduced Solutions
  - Machine Learning Confidence
- Sheets
  - Sheet Attributes
  - Sheet Solutions
- Right-Click Menu Options

This page describes the beam and shell modeling tools that are part of Cubit's Geometry Power Tool. Geometry simplification is often required when modeling assemblies comprised primarily of thin volumes. Shell finite elements are often used rather than full 3D hex or tet elements. The task for analysts in this case is to reduce the 3D set of thin volumes to a set of connected sheet bodies where a mesh of triangles or quadrilaterals can be applied. This procedure can be managed with the Geometry Power Tool if the Beam and Shell diagnostic is selected.

The Geometry Power Tool in Cubit provides a series of diagnostic checks on your model used to defeature or simplify a CAD model prior to meshing. Clicking the Analyze button will perform the selected diagnostic tests and display an expanding tree listing geometric entities that are identified by each test. Once identified, suggested solutions can be easily previewed and executed.

The Beam and Shell diagnostics work best in conjunction with the machine learning models. As such, it is recommended that if using these tools, that the Load ML Models button first be selected using the procedure described in the page Machine Learning with the Geometry Power Tool.

Figure 1. Thin Volumes diagnostic displayed with Solution window. Reduce solutions show for volume in figure 3.

Figure 2. Sheets diagnostic displayed with Solution window. Solutions for connections at one of the sheets are displayed.

Figure 3. Two reduce options for the same volume

This diagnostic manages the reduction of thin volumes to their 2D or sheet body equivalent. Its primary use is to preview and execute custom reduction operations on selected thin volumes when using the Show Solutions checkbox. The default mode for this diagnostic is to simply list all active volumes. If the machine learning models have been loaded, this diagnostic will be limited to volumes identified as "thin" for its classification category. Figure 1 shows the power tool with an example of a simple 3 volume assembly, where volumes are listed in ascending order based on their geometric volume.

This diagnostic will list all volumes defined as sheet bodies. It is most useful when used with the reduce thin operations, as sheet bodies will automatically be grouped based on their 3D thin volume parent. If a sheet body was not created with a reduce thin command, it will be grouped under a generic "orphan" category.

Additionally, when using the sheets diagnostic, three new columns for data entry will appear which are used for displaying and updating the thickness, loft and block for the selected sheet body. When using a reduce thin operation, the thickness and loft values for the new sheet body will be computed and displayed. Blocks will also automatically be created containing the new sheet body with the thickness and loft assigned as attributes.

Clicking on the entries for thickness, loft or block for a given sheet or volume will permit editing of these values. Once edited, the appropriate commands will be issued to update the block attributes. Changing the block ID will also update or create a new block if necessary.

Sheet attributes can also be exported in the form of a spread sheet by right-clicking on the sheet bodies or volumes that should be exported and selecting "Export Sheet Data..."

Custom solutions displayed will be tweak or imprint/merge operations that will attempt to connect nearby sheet bodies. For example, when selecting a solution for tweak, a preview similar to figure 4 may be displayed. Double-clicking will execute the tweak, extending the surfaces to touch as shown in figure 5.

Draws the selected sheets in the current graphics display mode (usually smooth shade) and its parent volumes in wire frame. If right-clicking the "sheet" or "thin volume" categories in the diagnostic window, all sheets and their parents will be displayed.

Draws the sheets similar to above, but also displays the sheet as a 3D transparent volume extrusion, where the thickness of the extrusion is defined by the current assigned thickness attribute. The transparent extruded volume will also reflect the current loft attribute for the assigned block. Note that this is similar this is similar to using the command line draw shell volume. This tool is useful for visually validating the currently assigned loft and thickness values.

Selecting this tool will highlight or locate all curves from the selected sheets that are merged with a neighbor. This is useful for checking that the intended connections have been made. Note that this option will only select merged curves on sheet bodies that are children of neighboring 3D thin volumes. (It is assumed that sheet bodies on the same parent volume will be merged)

Similar to the previous option, but finds connections that have not yet been made and highlights the closest curve. This is useful for identifying sheet bodies that are not yet connected but should be.

Deletes child sheet bodies from a parent 3D thin volume and removes its association.

Brings up a file-picker dialog and exports the current sheet attribute data to a .csv file. If right-clicking the "Sheets" or "Thin Volumes" category headers, all sheet data will be exported. Otherwise, only the selected sheets will be exported.

Available when right-clicking on a reduce command in the solution window. If the machine learning models are loaded, a confidence value will be displayed next to each thin volume reduce command in the custom solution window. This indicates a suitability score (0 to 1), with the solutions ordered highest confidence to lowest. In many cases choosing the highest confidence predicted by the ML supervised learning tool is sufficient, however since the predictions are based only on existing training data, or models it has seen before, it is possible that the highest confidence solution is not desirable. If this occurs, the maximize or minimize confidence right-click menu options can be used.

Selecting one of these options will effectively add or replace existing training data to augment the machine learning model. Executing one of these commands will trigger retraining, the ML model will be reloaded and a new predicted confidence displayed. Subsequent operations that use the same or similar reduction will now be updated to reflect the new confidence prediction.

The primary use case for maximize and minimize confidence is following reinforcement learning. If the RL methods are unable to identify the best solution for a given situation, the user can interveen and provide their own preferences to the learning model.

---

## Colors

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/colors.htm

**Contents:**
- Colors
- Specifying Colors in Commands
- User-Defined Colors
- Assigning Colors
- Assigning Global Colors

There are multiple ways to refer to a color in a command. They are

The first option uses the name of a pre-defined color as listed in the Available Colors Appendix. This option may not be used for user-defined colors. An example of a pre-defined color assignment is given below:

color volume 1 lightblue

The second option is used with user-defined colors only. Include the name of the user-defined color in quotes. Pre-defined colors will not work with this command.

color volume 1 user "mycolor"

The third option allows you to identify a pre-defined color by its ID. The color IDs are also listed in the Available Colors appendix. This option is rarely used.

The fourth option allows you to specify a color by R, G and B values ranging between 0.0 and 1.0. This option can be used to specify colors not found on the color table.

color volume 1 rgb 0.7 0.4 0.35

The fifth option allows you to specify a color by R, G, B, and A values ranging between 0.0 and 1.0. This option allows you to specify an Alpha component allowing for transparency. 1.0 is opaque and 0.0 is transparent. This option can be used to specify colors not found on the color table.

color volume 1 rgba 0.7 0.4 0.35 0.4

The default option is used to set an entity's color to its default value. The default color may also be specified in drawing commands, but the command's behavior will be the same as if the color option had not been included at all.

color volume 1 default

The seventh option refers to the current highlight color.

draw curve 1 tangent color highlight

CUBIT has a palette of 92 pre-defined colors, listed in the Appendix under Available Colors. Users may also define their own colors in addition to those defined by CUBIT. Each color is defined by a name and by its RGB components, which range from 0 to 1. Adding user defined colors to the color table is an alternative to using RGB or RGBA color specifications.

To define an additional color, use either of the commands

Color Define "<name>" RGB <r g b>

Color Define "<name>" R <r> G <g> B <b>.

This is done with the command

Color Release "<color_name>"

Color names can be listed with the command

They are also listed in the appendix of this manual, along with their RGB definitions. To view a chart of color names and IDs, including those for user-defined colors, use the command

Colors may be assigned to all geometric entities, and to some other objects as well. To assign a color to an entity or other object, use one of the following commands.

Color Axis Labels {<color_name>| id <color_id> | rgb <r> <g> <b> }

Color Background {<color_name>| id <color_id> | rgb <r> <g> <b>} [<color_name2>|id <color_id2>| rgb <r> <g> <b>]

Color Block <block_id_range>{<color_name> | id <color_id> | rgb <r> <g> <b>}

Color Body <body_id_range> [Geometry|Mesh] {<color_name>| id <color_id> | rgb <r> <g> <b> | Default}

Color Curve <curve_id_range> [Geometry|Mesh] {<color_name>| id <color_id> | rgb <r> <g> <b> | Default}

Color Group <group_id_range> [Geometry|Mesh] {<color_name>| id <color_id> | rgb <r> <g> <b> | Default}

Color Highlight {<color_name>| id <color_id>| rgb <r> <g> <b>}

Color Lines <color_spec>

Color NodeSet <id_range> { <color_name> | id <color_id> | rgb <r> <g> <b> | Default }

Color SideSet <id_range>{ <color_name> | id <color_id> | rgb <r> <g> <b> | Default }

Color Surface <surface_id_range> [Geometry|Mesh] {<color_name>|| rgb <r> <g> <b> Default}

Color Title {<color_name>|id <color_id>| rgb <r> <g> <b> }

Color Volume <volume_id_range> [Geometry|Mesh] {<color_name>| id <color_id> | rgb <r> <g> <b> | Default}

Including the Mesh keyword will change the color of the mesh belonging to the specified entity, without changing the color of the entity geometry itself. Conversely, including the Geometry keyword will change the geometry color without changing the mesh color. Including both keywords is identical to including neither keyword.

Colors are inherited by child entities. If you explicitly set the color for a volume, for example, all of its surfaces will also be drawn in that color. Once you assign a color to an entity, however, it will remain that color and will no longer follow color changes to parent entities. To make an entity follow the color of its parent after having explicitly set another color, use Default as the color name in the color command.

Colors can also be assigned to nodesets, sidesets, and element blocks. These colors do not take effect, however, unless the nodeset, sideset, or element block is drawn with a Draw command.

The background color and the color used to draw highlighted entities can be changed to any color.

By default, the axes are labeled with a white X, Y, and Z, indicating the three primary coordinate directions. If the background is changed to white, these labels are impossible to read; the color used to draw axis labels can be changed to any color. Changing the axis label color will change the text color for both the model axis and the triad (corner axis).

When several entity types are labeled, it can become difficult to determine which labels apply to which entities. To help distinguish which entities are being referred to by the labels, you may want to change the color of labels for specific entity types.

When a meshed surface is drawn in a shaded graphics mode, the mesh edges are not drawn in the same color as the surface. This is to prevent confusion between mesh edges and geometric curves, and to make the mesh edges more visible. The color used to draw mesh edges in this situation is known as the line color, and is gray by default; this color can be changed to any color.

Colors may be assigned globally also. To assign a global color, use one of the following commands. Global color assignment is useful if one desires all entities to appear the same.

Color Global {<color_name>| id <color_id> | rgb <r> <g> <b> | default}

Color Global Surface {<color_name>| id <color_id> | rgb <r> <g> <b> | default} Curve {<color_name>| id <color_id> | rgb <r> <g> <b> | default} Vertex {<color_name>| id <color_id> | rgb <r> <g> <b> | default}

The first command assigns the desired color to all geometry entities. The color may be enter by color name or color id. The default option resets colors to the default value.

The second command assigns the desired colors to surfaces, curves and vertices. All three value must be entered. For example, users my select global colors for surface and vertex and specify that curves have default colors.

---

## Command Line Entity Specification

**URL:** https://coreform.com/cubit_help/environment_control/entity_selection_and_filtering/cl_entity_specification.htm

**Contents:**
- Command Line Entity Specification
- Types of Entity Range Input
- Precedence of "Except" and "In"
- Placement in CUBIT Commands

CUBIT identifies objects in the geometry, mesh, and elsewhere using ID numbers and sometimes names. IDs and names are used in most commands to specify which objects on which the command is to operate.

These objects can be specified in CUBIT commands in a variety of ways, which are best introduced with the following examples (the portion of each command which specifies a list of entities is shown in blue):

General ranges: Surface 1 2 4 to 6 by 2 3 4 5 Scheme Pave

Combined geometry, mesh, and genesis entities: Draw Sideset 1 Curve 3 Hex 2 4 6

Geometric topology traversal: Vertex in Volume 2 Size 0.3

Mesh topology traversal: Draw Edge in Hex 32

Genesis entity traversal: Draw Block in Hex 32

All keyword: ListBlock all

Expand keyword: my_curve_group expand Scheme Bias Factor 1.5

Except keyword: List Curve 1 to 50 except 2 4 6

In addition to the examples above, there is an extended parsing capability that allows entities to be specified by a general set of criteria. See Extended Entity Specification for details. The following is a simple example of an extended entity specification:

By Criteria: Draw Curve With Length > 3

The types of entity range input available in CUBIT can be classified in 4 groups:

Entity IDs can be entered individually (volume 1), in lists (volume 1 2 3), in ranges (volume 3 to 7), and in stepped ranges (volume 3 to 7 step 2). The word all may also be used to specify all entities of a given type.

An ID range has the form <start_id> to <end_id>. It represents each ID between start_id and end_id, inclusive.

A stepped ID range has the form <start_id> To <end_id> {Step|By} <step>. It represents the set of IDs between start_id and end_id, inclusive, which can be obtained by adding some integer multiple of step to start_id. For example, 3 to 8 step 2 is equivalent to 3 5 7.

The various methods of specifying IDs can be used together. For example:

draw surface 1 2 4 to 6 vertex all

Topological traversal is indicated using the "in" and "common_to" identifiers, can span multiple levels in a hierarchy, and can go either up or down the topology tree. For example, the following entity lists are all valid:

volume in vertex 2 4 6

surface common_to volume 2 3

curve common_to surface 2 3

curve 1 to 3 in body 4 to 8 by 2

If ranges of entities are given on both sides of the "in" identifier, the intersection of the two sets results. For example, in the last command above, the curves that have ids of 1, 2 or 3 and are also in bodies 4, 6 and 8 are used in the command.

Topology traversal is also valid between entity types. Therefore, the following commands would also be valid:

draw node in surface 3

draw surface in edge 362

draw hex in face in surface 2

draw node in hex in face in surface 2

draw edge in node in surface 2

draw face common_to volume 1 2

Entity lists can be entered then filtered using the "except" identifier. This identifier and the ids following it apply only to the immediately preceding entity list, and are taken to be the same entity type. For example, the following entity lists are valid:

curve all except 2 4 6

curve 1 2 5 to 50 except 2 3 4

curve all except 2 3 4 in surface 2 to 10

curve in surface 3 except 2 (produces empty entity list!)

Entity names can also be used to specify the exclusion list. For example:

curve all except pivot_1

When using mulitple names to specify the exclusion list it is necessary to use the "in" keyword with parentheses. For example:

curve all except curve in (pivot_1 top_left)

In the above example, all curves are in the entity list except the curve named "pivot_1" and the curve named "top_left".

Groups in CUBIT can consist of any number of geometry entities, and the entities can be of different type (vertex, curve, etc.). Operations on groups can be classified as operations on the group itself or operations on all entities in the group. If a group identifier in a command is followed immediately by the `expand' qualifier, the contents of the group(s) are substituted in place of the group identifier(s); otherwise the command is interpreted as an operation on the group as a whole. If a group preceding the `expand' qualifier includes other groups, all groups are expanded in a recursive fashion.

For example, consider group 1, which consists of surfaces 1, 2 and curve 1. Surfaces 1 and 2 are bounded by curves 2, 3, 4 and 5. The commands in Table 1, illustrate the behavior of the `expand' qualifier.

Table 1. Parsing of group commands; Group 1 consists of Surfaces 1-2 and Curve 1; Surfaces 1 and 2 are bounded by Curves 2-5.

The `expand' qualifier can be used anywhere a group command is used in an entity list; of course, commands which apply only to groups will be meaningless if the group id is followed by the `expand' qualifier.

Several keywords take precedence over others, much the same as some operators have greater precedence in coding languages. In the current implementation, the keyword "Except" takes precedence over other keywords, and serves to separate the identifier list into two sections. Any identifiers following the "Except" keyword apply to the list of entities excluded from the entities preceding the "Except". Table 2 shows the entity lists resulting from selected commands.

Table 2. Precedence of "Except" and "In" keywords; Group 1 consists of Surfaces 1-2 and Curve 1.

In the first command, the entities to be excluded are the contents of the list "[Curve] 1 in Group 1", that is the intersection of the lists "Curve 1" and "Curve in Group 1"; since the only curve in Group 1 is Curve 1, the excluded list consists of only Curve 1. The remaining list, after removing the excluded list, is all curves except Curve 1.

In the second command, the excluded list consists of the intersection of the lists "Curve 2 3 4" and "Curve in Surf 2 to 10"; this intersection turns out to be just Curves 2, 3 and 4. The remaining list is all curves except those in the excluded list.

In general, anywhere a range of entities is allowed, the new parsing capability can be used. However, there can be exceptions to this general rule, because of ambiguities this syntax would produce. Currently, the only exception to this rule is the command used to define a sideset for a surface with respect to an owning volume.

---

## Command Line Help

**URL:** https://coreform.com/cubit_help/environment_control/session_control/command_line_help.htm

**Contents:**
- Command Line Help

In addition to the documentation you are currently viewing, CUBIT can give help on command syntax from the command line. For help on a particular command or keyword, the user can simply type help <keyword>. If the user is uncertain of the keyword, an asterisk * may be added to the end of the entered characters and help for all keywords that start with the entered characters will be printed. In addition, if the user has typed part of a command and is uncertain of the syntax of the remainder of the command, they can type a question mark ? and help will be printed for the sequence of keywords currently entered. It is important to note that if the user has typed the keywords out of order, then no help will be found. If the user is not sure of the correct order of the keywords, the ampersand & key will search on all occurrences of whatever keywords are entered, regardless of the order. The results of this type of command are shown in the following listing.

CUBIT>help degenerate*

Help for words: degenerate*.

set Block Mixed Element Output { OFFSET | Degenerate }

set Degenerates [on|off]

CUBIT> volume 3 label ? Completing commands starting with: volume, label. Help not found for the specified word order.

CUBIT> volume 3 label & Help for words: volume & label Label Volume [ on | off | name [only|id] | id | interval | size | scheme | merge | firmness ]

CUBIT> label volume 3 ? Completing commands starting with: label, volume. Label Volume [on|off|name [only|ids]|ids|interval|size|scheme|merge|firmness]

---

## Command Line View Navigation: Zoom, Pan and Rotate

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/zoom_pan_rotate.htm

**Contents:**
- Command Line View Navigation: Zoom, Pan and Rotate
- Rotation
- Panning
- Zooming

Commands used to affect camera position or other functions are listed below. All rotation, panning, and zooming operations can include the Animation Steps qualifier, makes the image pass smoothly through the total transformation. Animation also allows the user to see how a transformation command arrives at its destination by showing the intermediate positions.

Rotate <degrees> About [Screen | Camera | World] {X | Y | Z} [Animation Steps <number_steps>]

Rotate <degrees> About Curve <curve> [Animation Steps <number_steps>]

Rotate <degrees> About Vertex <vertex_1> Vertex <vertex_2> [Animation Steps <number_steps>]

Rotation of the view can be specified by an angle about an axis in model coordinates, about the camera's "At" point, or about the camera itself. Additionally rotations can be specified about any general axis by specifying start and end points to define the general vector. The right hand rule is used in all rotations.

Plain degree rotations are in the Screen coordinate system by default, which is centered on the camera's At point. The Camera keyword causes the camera to rotate about itself (the camera's From point). The World keyword causes the rotation to occur about the model's coordinate system. Rotations can also be performed about the line joining the two end vertices of a curve in the model, or a line connecting two vertices in the model.

Pan [{Left|Right} <factor1>] [{Up|Down} <factor2>] [Screen | World ] [Animation Steps <number_steps>]

Panning causes the camera to be moved up, down, left, or right. In terms of camera attributes, the From point and At point are translated equal distances and directions, while the perspective angle and up vector remain unchanged. The scene can also be panned by a factor of the graphics window size.

Screen and World indicate which coordinate system <factor> is in. If Screen is indicated (the default), <factor> is in screen coordinates, in which the width of the screen is one unit. If World is indicated, <factor> is expressed in the model units.

Zoom Screen <factor> [Animation Steps <number_steps>]

Zoom <x_min> <y_min> <x_max> <y_max> [Animation Steps <number_steps>]

Zoom {Group | Body | Volume | Surface | Curve | Vertex | Hex | Tet | Face | Tri | Edge | Node} <id_range> [Animation Steps <number_steps>] [Direction {options}]

Zoom cursor [click|drag][animation steps <number>]

Zoom Screen will move the camera <factor> times closer to its focal point. The result is that objects on the focal plane will appear <factor> times larger.

Zooming on a specific portion of the screen is accomplished by specifying the zoom area in screen coordinates; for example, Zoom 0 .25 .25 will zoom in on the bottom left quarter of the screen.

Zooming on a particular entity in the model is accomplished by specifying the entity type and ID after entering Zoom. The image will be adjusted to fit bounding box of the specified entity into the graphics window, and the specified entity will be highlighted. You can specify a final direction to look at when zooming by using the direction option.

To center the view on all visible entities, use the Zoom Reset command.

The GUI tool bar buttons for controlling zoom in, zoom out, and zoom reset are as follows:

---

## Command Line Workspace

**URL:** https://coreform.com/cubit_help/environment_control/gui/input_window.htm

**Contents:**
- Command Line Workspace
- Command Window
  - Entering Commands
  - Command Mode
  - Python Statements
  - Repeating Commands
  - Focus Follows Cursor
- Error Window
- History Window
- Docking and Undocking the Input Window

The Command Line Workspace is the interface for command interaction between the user and the CUBIT application. The user can enter commands into this window as if they were using the command line version of CUBIT. Journaled commands will be echoed to this screen, even if they were not typed in manually. Thus, if the user wants to know what the command sequence for a particular action on the GUI is, they can watch for the "Journaled Command:" line to appear. In addition, this screen will contain important informational and error messages. The command window has the following three tabs:

The command line workspace emulates the environment in the command line version of Cubit. Commands can be entered directly by typing at the CUBIT> or >>> prompt. This window also prints out error messages, informational messages, and journaled commands.

To enter commands in the command line workspace, the command window must be active. Activate the command window by clicking anywhere inside the window. Commands are typed in at the CUBIT> or >>> prompt. Cubit commands are accepted with the CUBIT> prompt and Python statements are accepted at the >>> prompt. If you do not remember the specific Cubit command sequence you can type help and the name of the command phrase. The input window will show all of the commands that contain that word or phrase. Alternatively, if you know how a command starts, but do not remember all of the options, you can type ? at the end of the command to show all possible command completions. See Command Syntax for an explanation of command syntax rules.

The command window can be in either a Cubit command mode or a Python statement mode. Switching modes can be done with #!cubit to switch to the Cubit command mode or with a #!python to switch to the Python statement mode. A convenience button is also available in the lower right corner of the command window to switch modes with a click of the mouse button.

The Python interpreter in Cubit works as though you were entering lines at the Python command prompt. This means a blank line is interpreted as the end of a block. If you want to add whitespace for clarity, you could add a # mark for a comment on any white line that is in a loop or a class.

A second python script can be included and executed by either using the play Cubit command or by using a Python import statement.

The interface between cubit and Python is the 'cubit' object. Among many methods, this object has a method called cmd which takes as an argument a Cubit command string. Thus the following command can be issued in the Command window at the >>> prompt, which will create a cube with sides 10 units long.

cubit.cmd("create brick x 10")

The following script is a simple example that illustrates using loops, strings, and integers in Python.

%>for i in range(4): . . x=i*3 . . for j in range(4): . . y=j*3 . . for k in range(4): . . z=k*3 . . mystr="create vertex x "+str(x)+" y "+str(y)+" z "+str(z) . . cubit.cmd(mystr)

This simple script will create a grid of vertices four wide. Scripts can be more advanced, even creating customized windows and toolbars. For a complete list of python/cubit interface commands see the Appendix.

Use the Up and Down arrow keys on the keyboard to recall previously executed commands.

Commands can be repeated in other ways as well.

Beginning with version 13.0, Cubit includes a 'focus follows cursor' option for the command window. The option can be enabled and disabled from the Tools/Options/General options panel. The setting is persistent between sessions and is disabled by default.

Please note, the focus follows cursor behavior is available only in the command window. All other windows or widgets require the user to click the mouse in order to grab focus.

The error window is located in the Command Line Workspace under the Error tab. If there are errors, a warning icon will appear on the tab. The icon will disappear when you open the window to view errors. The error window only displays the error output, which can make it easier to find and read the error output. The command that caused the error will be printed along with the error information. If the command was from a journal file, the file name and number will be printed next to the command.

The history window lists the last 100 commands. The number of commands listed can be configured in the options dialog on the History page. You can re-run the commands in the history window using the context menu. You can also clear the history using the context menu.

The command window can be undocked by clicking and dragging the left edge. If it is floating it can be redocked by double-clicking the solid blue bar. By default, it will always be redocked in the bottom of the application window. To change the size of the floating window, click and drag the edge of the window. To change the height of the docked window, click and drag the top edge or right edge.

---

## Command Panels

**URL:** https://coreform.com/cubit_help/environment_control/gui/control_panel/control_panel.htm

**Contents:**
- Command Panels

The Command Panels provide a graphical means of accessing almost all of the CUBIT functionality. The main CUBIT Command Panel is divided into seven modes. Each of these modes pertains to a major component of the CUBIT application. To view information about each of the tools in the Control Panel select the help icon on each panel to access context specific help.

Figure 1. The CUBIT Control Panel

A brief description of the functionality of the Control Panel window follows.

Control Panel Functionality

---

## Command Panel Functionality

**URL:** https://coreform.com/cubit_help/environment_control/gui/control_panel/control_panel_functionality.htm

**Contents:**
- Command Panel Functionality
- ID Input Entry Methods
- Right-Click Context Menu for ID Input Fields
- Value Fields
- Advancing Pickwidgets

The Command Panel is arranged first by mode on the top row of buttons. Modes are arranged by task.

All of the geometry related tasks, for instance, can be found under the Geometry mode. When a mode is selected, a second row of buttons becomes available. The second row of buttons shown depends on the selected mode. For example, if Geometry is selected, the second row of buttons will contain operations that can be performed on geometry, such as creation, modification, decomposition, boolean, merging, deleting, and so forth.

Selecting an operation will cause a row of geometry entity buttons to be displayed. Specific, entity-based operations will be shown after selecting the entity type, as shown below.

Note: This hierarchy is different than previous versions of Cubit. In previous versions the second row of buttons was geometry entity types, such as volume, surface, curve, vertex, and group. If a user wishes to use the 'classic' hierarchy for geometry, an option can be selected in Tools/Options/Command Panels.

The 'classic' hierarchy's button hierarchy for creating a solid brick is the following:

For all other modes, such as mesh, analysis groups, and so forth, the 'classic' button hierarchy remains.

All command panels are constructed similarly. Each abstracts a set of Cubit commands. Options are selected using check boxes, radio buttons, combo boxes, edit fields, and other standard GUI widgets. Each command panel includes an Apply button. Pressing the Apply button will generate a command to Cubit. Nothing happens until and unless the Apply button is pressed.

Note: The edit fields are free form, which means the user may enter any valid string into the fields. Any string that is valid for the command line is valid for the command panel edit fields.

Where possible, default values are placed into edit fields. At any time, with the cursor placed over a blank portion of the command panel, the user may right-click to select Reset Data which will clear all fields and replace default values.

The ID Input Fields provide a location where Geometric IDs, required for the current command, can be entered. IDs can be entered in several ways:

Simple Keyboard entry

ID numbers can be entered directly in the field. Each ID must be separated with a space. Select the field first before typing.

IDs can be entered automatically by selecting entities directly in the Graphics Window. The current entity available for selection is based on the current entity selection mode. In some cases, not all entities of the current entity selection mode will be available for picking. The program may automatically filter the applicable entities based on the context of the current command

Geometry Tree selection

IDs may be entered by selecting the corresponding geometric entity from the geometry tree. To select multiple entities use the <ctrl> key.

A range of IDs may be typed into the field. For example:

will automatically enter all IDs from 1 to 5 inclusive in the field. Keywords such as all and except can also be used. Any range that can be entered directly on a CUBIT command line can also be used in the ID input field. See Command Line Entity Specification for a description of the syntax.

As Part of Other Entities

Syntax can be entered in the ID Input field that will specify an entity based upon its topological relationship to other entities For example, if a Vertex Selection Type Button was highlighted, entering

will automatically enter all vertices in surface 1 into the Input Field. CUBIT has a rich set of syntax rules for specifying entities based upon topology relationships. See Command Line Entity Specification for a description.

Entities that are part of groups may be specified in the ID Input Field. For example, if the Vertex Selection Type Button is highlighted, entering:

will automatically enter all vertices in the picked group into the active ID Input Field.

Entities can be dragged and dropped into the ID Input Field from the Tree View window.

When the right mouse button is selected while in an ID Input Field, the following menu options will appear:

Integer and real values pertinent to the command are entered in this window. Input placed in parenthesis { } will be evaluated when the command is executed. For example:

is valid input. Additionally, any APREPRO syntax is valid in the Value Field, including mathematical functions and boolean operations. See the section, APREPRO for a description of syntax.

Some command panels have several id input fields such as the Mesh>Hex>Create panel. A convenience feature implemented for such panels is an advancing pickwidget feature. Pressing the middle mouse button after selecting an entity will advance to the next id input field.

---

## Command Recording and Playback

**URL:** https://coreform.com/cubit_help/environment_control/recording_and_playback/recording_and_playback.htm

**Contents:**
- Command Recording and Playback

Sequences of CUBIT commands can be recorded and used as a means to control CUBIT from ASCII text files. Command or "journal" files can be created within CUBIT, or can be created and edited directly by the user outside CUBIT.

---

## Command Syntax

**URL:** https://coreform.com/cubit_help/environment_control/session_control/command_syntax.htm

**Contents:**
- Command Syntax

Throughout this document, each function or process will have a description of the corresponding CUBIT command; in this section, general conventions for command syntax will be described. The user can obtain a quick guide to proper command format by issuing the <keyword> help command; see Command Line Help for details.

CUBIT commands are described in this manual and in the help output using the following conventions. An example of a typical CUBIT command is:

Volume <range> Scheme Sweep [Source [Surface] <range>] [Target [Surface] <range>] [Rotate {on | OFF}]

The commands recognized by CUBIT are free-format and abide by the following syntax conventions.

Numeric: A numeric parameter may be a real number or an integer. A real number may be in any legal C or FORTRAN numeric format (for example, 1, 0.2, -1e-2). An integer parameter may be in any legal decimal integer format (for example, 1, 100, 1000, but not 1.5, 1.0, 0x1F).

String: A string parameter is a literal character string contained within single or double quotes. For example, 'This is a string'.

Filename: When a command requires a filename, the filename must be enclosed in single or double quotes. If no path is specified, the file is understood to be in the current working directory. After entering a portion of a filename, typing a '?' will complete the filename, or as much of the filename as possible if there is more than one possible match.

A filename parameter must specify a legal filename on the system on which CUBIT is running. The filename may be specified using either a relative path (../cubit/mesh.jou), a fully-qualified path (/home/jdoe/cubit/mesh.jou), or no path; in the latter case, the file must be in the working directory (See Environment Commands for details.) Environment variables and aliases may also be used in the filename specification; for example, the C-Shell shorthand of referring to a file relative to the user's login directory (~jdoe/cubit/mesh.jou) is valid.

Toggle: Some commands require a "toggle" keyword to enable or disable a setting or option. Valid toggle keywords are "on", "yes", and "true" to enable the option; and "off", "no", and "false" to disable the option.

* an action keyword or "verb" followed by a variable number of parameters. For example:

Here Mesh is the verb and Volume 1 is the parameter.

* or a selector keyword or "noun" followed by a name and value of an attribute of the entity indicated. For example:

Volume 1 Scheme Sweep Source 1 Target 2

Here Volume 1 is the noun, Scheme is the attribute, and the remaining data are parameters to the Scheme keyword.

The notation conventions used in the command descriptions in this document are:

---

## Controlling Playback of Journal Files

**URL:** https://coreform.com/cubit_help/environment_control/recording_and_playback/controlling_playback.htm

**Contents:**
- Controlling Playback of Journal Files

The following commands control the playback of Journal Files:

Sleep <duration_in_seconds>

The playback of a journal file can be interrupted in three ways. Pressing ctrl-c while the journal file is playing will halt playback of the journal file. (This only works in the command line version of CUBIT. See Interrupting Running Tasks for more information ). Alternately, if the stop or pause commands are encountered in the journal file and CUBIT is reading commands from a terminal (as opposed to a redirected file), playback of the journal file will halt after that command.

The sleep command pauses execution for the specified number of seconds. It can be used to build a delay into journal files during presentations.

In the command line version of CUBIT you can resume playback of a journal file with the resume command. If playback was interrupted because ctrl-c was pressed, it will resume at the next command after the one that was interrupted. If playback stopped because of a stop or pause command in the journal file, it will resume at the next line after the stop or pause command. If the file was paused because of a sleep command in the file, it will resume automatically after the specified duration.

If journal files that are playing back contain playback commands themselves, there may be multiple current journal files. The where lists all current journal files and where the journal files have paused. Each line contains the stack position (a number), the filename and the current line in the file. Unless CUBIT is running in batch mode, the first line is always <stdin>. This just means that CUBIT will return to the command prompt after the top-most journal file has completed.

The remaining portion of any active journal file may be skipped by specifying the stack position (first number on each line of the output from the where command) of the file where you want to resume. Any remaining commands in active journal files with lower stack positions will be skipped.

The next command steps through interrupted journal files line-by-line. The argument to the next command is the number of lines to read before halting playback again. If no number is specified, the command will advance one line.

Journal playback can also be set to stop automatically when it encounters an error during playback. The command syntax is:

Set Stop Error {On|OFF}

Setting the stop error to "on" will cause the file to halt for each error. The setting is turned off by default.

---

## Coreform Cubit® User Documentation

**URL:** https://coreform.com/cubit_help/cubit_users_manual.html

**Contents:**
- Coreform Cubit® User Documentation

Introduction - A quick overview of some of the main features and goals of the Coreform Cubit Mesh Generation Toolkit, licensing and activation, system requirements, and where to go for help.

Environment Control - A description of the Coreform Cubit user environment, including using the graphical user interface, session control, command line syntax, journal files, graphics, entity picking, saving and restoring etc..

Geometry - A description of Coreform Cubit's geometry features including building geometry from scratch, manipulating geometry in Coreform Cubit, importing and exporting geometry formats, etc...

Mesh Generation - A description of Coreform Cubit's mesh generation capabilities, including how to mesh geometry, meshing and smoothing schemes, setting sizes and intervals, importing a mesh, etc...

Finite Element Model - How to set up the finite element model for analysis, including defining boundary conditions, material properties, exporting the finite element model, etc.

Boundary Layer Meshing - How to set up boundary layers.

Python API - How to access the Python API for Coreform Cubit. Describes the most common Python API functionalities, with comprehensive documentation available in the appendix.

Immersive Topology Environment for Meshing (ITEM) - A description of Coreform Cubit's interactive meshing wizard including how to use the wizard, and a guide to geometry clean-up, setting up the finite element model, mesh generation in ITEM, etc.

Step-By-Step Tutorials

Official Coreform Cubit Web Page

---

## CUBIT Application Window

**URL:** https://coreform.com/cubit_help/environment_control/gui/application_window.htm

**Contents:**
- CUBIT Application Window
- Context Sensitive Help in the GUI
- Customizing the Application Window

The default CUBIT Application Window is shown in the following image.

Figure 1. The CUBIT Application Window

Graphics Window- The current model will be displayed here. Graphical picking and view transformations are done here.

Power Tools - Geometry tree hierarchy view, geometry analysis and repair tool, meshing tool, meshing quality tool, and ITEM Wizard.

Property Editor - The Property Editor lists attributes of the current entity selection. Some of these properties can be edited from the window.

Command Panel - Most Cubit commands are available through the command panels. The panels are arranged topologically, by mode.

Command Line Workspace - The command line workspace contains both the cubit command and error windows. The command window is used to enter cubit commands and view the output. The error window is used to view cubit errors.

Drop Down Menus - Standard file operations, Cubit setup and defaults, display modes, and other functionality is available in the pull-down menus.

Toolbars - The most commonly used features are available by clicking toolbar icons.

The Graphical User Interface has a context-sensitive help system. To obtain help using a specific window or control panel, press F1 when the focus is in the desired window. It may be necessary to click inside a text box to switch focus to a particular window. If no context specific help is available, it will open the cubit help documentation where you can search for a particular topic.

All windows in the CUBIT Application can be Floated or Docked. In the default configuration, all windows are docked. When a window is docked the user can click on the area indicated below.

Figure 2. A docked window. Click and drag to float.

By dragging with the left mouse button held down, the window will be un-docked from the Application Window. Dragging the window to another location on the Application Window and releasing the mouse button will cause it to dock again in a new location. The bounding box of the window will automatically change to fit the dimensions of the window as it is dragged. Releasing the mouse button while the window is not near an edge will cause the window to Float. To stop the window from automatically docking, hold the CONTROL key down while dragging.

Figure 3. A Floating Window

When a window is floating, as shown in Figure 3, it is possible to dock it by clicking the title bar of the window and dragging it to its new docked location.

Note: Double clicking on the title bar of an floating window will cause the window to redock in its last docked position.

---

## Defeature Tool

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/defeaturingtool.htm

**Contents:**
- Defeature Tool
- Command Syntax:
- Preserving Critical Geometric Entities
- Sample Journal File:
- Figures

The Defeature Tool is capable of removing small irrelevant curves and surfaces. These small curves and surfaces are one of the main sources of low quality elements and meshing failures. Sliver surfaces and curves generally exist at fillets, chamfers, and sliver surfaces at misalignments in imprinted assembly models.

Figure 1 - Defeature Power Tool

Defeaturing small curves and surfaces involves three main steps:

Step 1 requires specifying volume ids (e.g. all) and a tolerance (e.g. 0.6) as shown in Figure 1. Clicking “Analyze” button will automatically find small curves and surfaces in the volumes specified. Figure 2 shows the highlighted small curves and surfaces with the label information. Figure 3 shows a zoom view of a small surface.

In Step 2 the user is allowed to deselect entities by unchecking entities from the list “Entities to be Defeatured”. Users can also use “Highlight”, “Draw”, and “Locate” buttons to examine the automatically detected entities (see Figure 2).

In Step 3 actual defeaturing is performed by clicking the “Execute” button (see Figure 5). Figure 4 shows the zoom view of a defeatured volume. Defeatured volumes are created in a new user specified group (by default in “defeature_group”) as shown in Figure 6. Only the volumes that have small curves and surfaces will be defeatured. Also, by default old original volumes are deleted and new defeatured volumes (child entities) will use the corresponding old ids. Please use the option “Keep Originals” if you want to have both old original and new defeatured volumes.

Set tolerant mesh mbg only

This command forces the mesh to associate with new defeatured volume. Currently, this command must be called before calling the defeature command below.

Defeature curve_length <value> [Curve <ids>] [Curve <ids>] surface_prox2d <value> [Surface <ids> ] [group <id>] [keep]

curve_length <value>: Curves with length less than or equal to <value> are automatically detected as candidate for defeaturing if auto_identify is specified. Otherwise, [Curve <ids>] must be specified.

surface_prox2d <value>: Surfaces with narrow region between opposing bounding curves are automatically detected as candidate for defeaturing if auto_identify is specified. The 2d proximity <value> specified in detecting surfaces containing narrow regions. If auto_identify is not specified, then [Surface <ids>] must be specified.

group <id>: Defeatured volumes are added to the group id specified.

keep: If keep argument is specified original entities are kept along with new defeatured volumes. If keep argument is not specified, then original entities are deleted and new defeatured volumes and its subentities (surfaces, curves, and vertices) will use the ids of original volumes.

Mesh Tolerant Fix [Volume|Surface|Curve|Vertex] <range>

Mesh Tolerant Free [Volume|Surface|Curve|Vertex] <range>

Example for fixing geometric entities:

mesh tolerant fix surf all

mesh tolerant fix curve all

Defeature curve_length .2 curve 31 29 27 26 24 32 13 30 17 28 22 25

surface_prox2d .2 surface 13 14 15 16 12

Even though the defeature tool is mainly intended to driven by the GUI, it can be used via command line. Without the GUI, it will be harder to provide the list of small curves and surfaces to the defeature command. Here is a sample journal file:

# import simple assembly

import acis 'assembly11a.sat'

# perform any ACIS based operations such as webcutting and imprinting first

# enable the developer only command

# force the mesh to associate with defeatured MBG volumes

set tolerant mesh mbg only

# create a new group to store defeatured volumes

group 'defeatured_vols' add volume all

# perform actual defeaturing by specifying the volume ids, tolerance, and small curve/surf ids.

# defeatured volumes will be placed in the user specified group id and original entities can be

# kept along with new defetured volume using “keep” option.

defeature volume all curve_length 0.3 curve 107 103 102 100 88 85 82 80 9 6 4 2 214 212 211 210 203 200 199 197 188 187 185 183 170 167 164 162 234 232 227 225 254 253 252 251 249 248 243 242 272 271 270 269 265 264 259 258 288 287 286 285 281 280 275 274 304 303 302 301 297 296 291 290 312 311 307 306 surface_prox2d 0.3 surface 47 48 50 51 41 43 40 42 2 4 1 3 111 112 118 120 121 122 124 126 128 129 130 132 134 135 136 138 140 141 142 144 81 82 83 84 88 89 90 91 94 95 96 97 100 101 102 103 group 2 keep

# del any old original volumes if you don’t want it anymore

# enable visibility of only defeatured vols

vol all in group 2 vis on

# set scheme to tetmesh

vol all in group 2 scheme tetmesh

vol all in group 2 size 1

# mesh defeatured vols

mesh vol all in group 2

# disable developer only command

Figure 1: Specify Volume ID and Tolerance before clicking “Analyze”

Figure 2: Use “Highlight”, “Draw”, and “Locate” to visualize small curves and surfaces

Figure 3: Zoom view of a small curve and surface

Figure 4: Zoom view of defeatured volume

Figure 5: Click Execute button to Defeature automatically/manually selected entities

Figure 6: New defeature_group contains defeatured volumes in MBG format

---

## Drawing a Location, Direction, or Axis

**URL:** https://coreform.com/cubit_help/environment_control/location_direction_specification/drawing_locations_and_directions.htm

**Contents:**
- Drawing a Location, Direction, or Axis

Some commands require you to specify a location on a curve (i.e., webcutting with a plane normal to a curve). This location can be previewed with the following options:

Draw Location On Curve <curve id> {Fraction <f> | Distance <d> | Position <xval><yval><zval> | Close_To Vertex <vertex_id>} [[From] Vertex <vertex_id> (optional for 'Fraction' & 'Distance')]

Some commands require a specified axis (such as webcut with a cylinder) and it is sometimes advantageous to view an axis before modifying geometry. To draw a preview of an axis use the following command:

Some commands require a specified location or point (such as create curve spline) and it is sometimes advantages to view a location before modifying or creating geometry. To draw a preview of a location use the following command:

Draw Location {options} [color <color_name>] [no_flush]

Some commands require a direction. To draw a preview of a direction, use the following command:

Draw Direction {options} [from] [location {options}] [color <color_name>] [length <value>]

The optional color argument draws the direction vector in the named color (the default is red), and the optional length argument sets the length of the drawn vector in model units (otherwise a default screen-relative length is used).

---

## Drawing, Locating, and Highlighting Entities

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/drawing_and_highlighting.htm

**Contents:**
- Drawing, Locating, and Highlighting Entities
- Drawing Other Objects
  - Displaying Entity Orientation
  - Displaying Sheet Volume Thickness
  - Volume Sources and Targets
  - Model Axis
  - Surface Isoparameter Lines
  - Surface Overlap
  - Volume Overlap
  - Geometry Preview

In order to effectively visualize the model, it is often necessary to draw an entity by itself, or several entities as a group. This is easily done with the command

Draw {Entity specification} [Color <color_spec>] [Zoom] [Add|Remove]

where Entity specification is an entity list as described in Command Line Entity Specification. This command clears the display before drawing the specified entity or entities. Specification of a color will draw those entities in that color. This will not permanently change the color of the entity. The zoom option will zoom in on the selected entities after drawing them in the graphics window. If the add option is specified, the display is not cleared, and the given entity is added to what is already drawn on the screen. Likewise, if the remove option is specified, all currently-drawn entities remain on the screen except for those designated for removal, which are removed.

The entities specified in this command are drawn regardless of their visibility setting (see Geometry and Mesh Entity Visibility for more details about visibility).

Entities may also be drawn by selecting them with the mouse and then typing Ctrl-D while the mouse is in the graphics window. This will clear the screen and then draw only those entities that are currently selected.

Entities can be highlighted using the command

Highlight {Entity specification}

This command highlights the specified entities in the current display with the current highlight color. Highlighting can be removed using the command

Graphics Clear Highlight

To return to the normal display of the entire model, type Display.

The Locate command will label and point to the specified entity or location in the graphics window. The command syntax is:

Locate <entity_list> [<string>]

Locate location <options> [<string>]

For example, suppose you have an idless reference to a curve of:

Curve ( at 5 5 0 ordinal 1 )

You can find the curve with the following command:

locate location 5 5 0

Supplying an optional string will draw the text as the label instead of the entity type and id.

Additionally, the visibility of individual entities, or sets of entities, can be controlled with the following visibility commands.

{Vertex|Curve|Surface|Volume|Body|Group} <range> [Geometry|Mesh] Visibility {on|off}

Edge [Visibility] {on|off}

{Mesh|Geometry} [Visibility]{on|off}

In addition to the common geometry, mesh and genesis entities, other objects may be drawn with variations of the Draw command. As with the other Draw commands, typing Display after drawing these objects will restore the scene to its normal display.

The normal to one or more surfaces, mesh faces, or mesh triangles may be drawn with the command

Draw {Surface | Face | Tri} <id_range> Normal [Length <length>] [Face | Tri] Color <color> [Add]

Surface normal command colors the surfaces using two different colors. The surface exposed to the positive half space (i.e, along the direction of normal), will always be colored black. The surace exposed to the negative half space will be colored using the specified <color>.

If the Face or Tri qualifier is included in the Draw Normal command, the normals for all faces or tris that belong to the specified surface are drawn.

Arrow representing the normal will be displayed if "Length" is specified

The forward, or tangent, direction of a curve can be drawn with the command:

The forward, or tangent, direction of a curve can be drawn with the command:

Draw Curve <id_range> Tangent [Length <length>][Color <color_spec>]

If a color is not specified, the tangent is drawn in the same color as the curve.

For volumes that can be identified as a sheet, an offset 3D volume can be displayed.

Draw Volume <ids> Thickness <value> [Loft <value>] [Include_Normal] [Color <color>] [Transparent] [Add]

Above figures show example sheet volumes (left) and the same sheet volumes displayed with their thickness (right) using the command:

draw volume all thickness 4 loft 0.5 color white transparent add

The thickness value is a positive floating number that indicates the thickness of the offset volume in a direction normal to the sheet volume. The loft option should be a value between 0 and 1 indicating where the preview volume will be displayed with respect to the sheet volume. A loft value of 0 will display the volume offset in the direction of the sheet volume surface normal. A value of 1 will reverse the direction of the offset. A value of 0.5 will display the volume centered on the sheet volume (as shown in the figure above). A color using one of Cubit's standard color keywords should also be specified. The transparent option can also be used to display the offset volume in transparent mode. Transparency can also be useful when using the add option so that both the sheet volumes and their offset volumes can be visualized together. The include_normal will display an arrow at the center of the sheet volume's surfaces indicating the normal direction of each surface

Once the source and target surfaces have been set on a volume that will be meshed with the sweep algorithm, the source and target may be visually identified with the command

Draw Volume <volume_id_range> [Source][Target] [Length <size>]

If the Source keyword is included, the normal of the source surface or surfaces will be drawn in green into the specified volume. If the Target keyword is included, the normal of the target surface or surfaces will be drawn in red into the specified volume.

The model axis may be drawn with the command

Draw Axis [Length <length>]

The axis is drawn as three lines beginning at the model origin, one line in each of the three coordinate directions. The length of those lines is determined by the length parameter, which defaults to 1.

Isoparameter lines may be drawn on surfaces in the model using the command

Draw Surface <surface_id_range> Isoparametric [Number <number>| [u <number>] [v <number>]]

If you specify the Number of lines, then the number of u- and v-parameter lines will be equal. You may specify instead a number of lines for each of the u and v parameters. The u-parameter lines will be drawn in red and the v-parameter lines will be drawn in blue.

The overlapping regions between two surfaces may be drawn with the command

Draw Surface <id> <id>Overlap [Add]

This command will draw the curves of each of the surfaces in green, and the portion of the surfaces that overlap in red. The Add keyword will draw the overlapping surfaces on top of the current graphics display. Without the Add keyword, the display will only show the specified surfaces and their overlapping regions.

The overlapping region between two volumes may be drawn with the command

Draw Volume <id> <id> Overlap [Add]

This command will draw the input volumes in transparent mode and draw the volume(s) of intersection as red, shaded solids. The Add keyword will draw the results on top of the current graphics display. Without the Add keyword, the display will only show the specified volumes along with the intersection volume(s).

Several options are available for previewing geometry without actually generating it. This is typically used in conjunction with webcutting and surface creation. The following Draw commands can be used for previewing geometry:

Draw Location On Curve

---

## Drawing Locations, Lines and Polygons

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/drawing_lines_and_polygons.htm

**Contents:**
- Drawing Locations, Lines and Polygons
- Drawing Locations
- Drawing Lines
- Drawing Polygons
- Buffered Drawing
- Example

In some cases it may be useful to simply draw a location, line or polygon to the screen to help visualize some aspect of the model. Locations, Lines and polygons are not geometry or mesh entities and are only visible until a refresh or display command is issued.

Draw Location {options}... [color <color_name>][no_flush]

Draw Line Location {options} Location {options} ... [color <color_name>][no_flush]

Draw Polygon Location {options} Location {options} Location {options} ... [color <color_name>][no_flush]

The optional no_flush argument for both the draw location, draw line and draw polygon commands may also be used when many simultaneous draw commands are being issued. This prevents the graphics from being drawn after each command is issued, which can be very inefficient. Instead the draw commands are buffered and sent all at once to be drawn. The following command:

The following is a simple example that will draw the figure below using cubit commands

---

## Drop Down Menus

**URL:** https://coreform.com/cubit_help/environment_control/gui/drop_down_menus/drop_down_menus.htm

**Contents:**
- Drop Down Menus
- Cubit (Mac Only)
- File
- Edit
- View
- Display
- Tools
- Help

The Cubit Drop-Down Menus, located at the top of the Cubit Application Window provide access to capabilities such as file management, checkpoints, display manipulation, journaling, system setup, component management, window management, and help.

This menu contains the Preferences dialog box, also called the Options dialog box on other platforms. It also contains the About Cubit menu and the Quit Cubit option. It is only available on Mac computers.

This menu provides common file operations, including importing and exporting of geometry and meshimport and export. A list of recently saved or imported files is also provided, allowing a quick way to import current or recent work. Non-Mac users can also exit and reset the program from this menu (These options are found under the Cubit tab for Mac Users).

This menu only provides a way to enable the Undo feature of the system. If Undo is enabled, one level of Undo is available to the user.

The View Menu lists all available toolbars and windows in the current CUBIT session. Selecting a toolbar or window will make it visible. Deselecting a toolbar or window will hide it. You can also hide an undocked window or toolbar by clicking on the small "x" in the upper right corner. For more information on docking and undocking toolbars, see CUBIT Application Window.

The Display Menu controls display options for the graphics window. These options are explained below:

The Tools Menu contains access to GUI-specific tools and options. These options are explained below.

---

## Entity Labels

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/entity_labels.htm

**Contents:**
- Entity Labels

Most entities may be labeled with text that is drawn at the centroid of the entity.

Mesh entities can be labeled with their ID number or their Element ID. Element ID labels are only valid after putting the mesh entities into a block.

Geometric entities can be labeled with their ID number or with other information.

Labels for groups of entity types can be turned on or off.

The following commands will accomplish this.

Label [On|Off|Name [Only|ID]|ID|Interval|Size|Merge|Firmness]

Label All [On|Off|Name [Only|ID]|ID|Interval|Size|Merge|Firmness]

Label Body [On|Off| Name [Only|ID] |ID|Interval|Size| Merge |Firmness]

Label Curve [On|Off|Name [Only|ID] |ID| Interval| Size| Merge| Firmness]

Label {Hex|Tet|Face|Tri|Edge} [On|Off|ElementId]

Label Element [On|Off]

Label Geometry [On|Off|Name [Only|ID] |ID| Interval| Size| Merge| Firmness]

Label Node [On|Off|ElementId|SphereId]

Label Surface [On|Off|Name [Only|ID] |ID| Interval| Scheme| Size| Merge| Firmness]

Label Vertex [On|Off|Name [Only|ID] |ID|Interval| Size| Merge| Firmness]

Label Volume [On|Off|Name [Only|ID] |ID |Interval| Size |Scheme |Merge |Firmness]

The meaning of each of each label type is listed below. Note that some label types don't make sense for every entity type.

On - The same as IDs.

Name - Name of the entity, if the entity has been named. Default name otherwise.

Name Only - If the entity has been named, use the name as the label. Otherwise, don't use a label.

Name IDs - If the entity has been named, use the name as the label. Otherwise, use the ID as the label.

Interval - The number of intervals set on the entity.

Firmness - Same as interval, but followed by a letter indicating the firmness of the interval setting (see the Mesh Generation chapter for description of firmness settings.)

Merge - Whether or not the entity is mergeable. Note that this is sometimes not clear, because, for example, a curve may show that it isn't mergeable because one of its owning surfaces may be unmergeable, while another owning surface may be mergeable.

Size - The mesh size set on this entity.

ElementId - The Global Element Id of each element. Will only be labeled for hexes, tets, tris, etc. which are in a block.

SphereId - The id of the sphere element associated with this node, if there is one. A sphere element is only associated with a node if the node (or it's geometry owner) is put into a block.

Note: Three dimensional entity types such as body will have their labels displayed in the center of the entity. Thus, in the smooth shade and hidden line graphics modes the labels will be hidden

The GUI includes command panels to manipulate the labels settings for any given entity type. The command panel for the Volumes labels settings is shown below as an example:

---

## Entity Selection

**URL:** https://coreform.com/cubit_help/environment_control/entity_selection_and_filtering/entity_selection_and_filtering.htm

**Contents:**
- Entity Selection

CUBIT Entity specification is a means of selecting objects or groups of objects. Entities can be selected from the command line using entity specification parameters, or directly in the graphics window using the mouse. This chapter describes these methods of entity selection.

---

## Environment Commands

**URL:** https://coreform.com/cubit_help/environment_control/session_control/environment_commands.htm

**Contents:**
- Environment Commands
- Working Directory
- File Manipulation
- CPU Time
- Comment
- History
- Handling Errors
- Determining the CUBIT Version
- Echoing Commands
- Digits Displayed

The working directory is the current directory where journal files are saved. To list the current directory type

The current path will be echoed to the screen. By default, the current directory is the directory from which CUBIT was launched. The command to change the current directory is

The new path may be an absolute reference, or relative to the current directory. The <TAB> key will complete unique file references.

A helpful addition is the ability to do a directory listing of a directory. The command for this is

Note also that you can delete files from the command line. The command for this is

Delete File ['<file_name>']

The file name may include the wildcard character *, but not the wildcard character ?, since the ? is used for command completion. File deletion from the command line can also be disabled. If deletions are set to off files cannot be deleted from the cubit command line.

Set Deletions [ON|Off]

The mkdir command is used to create a new directory. The syntax for this command is:

Mkdir "<directory_name>"

This creates a new directory with the specified name and path. The command accepts an absolute path, a relative path, or no path. If a relative path is specified, it is relative to the current working directory, which can be seen by typing 'pwd' at the cubit command prompt. If no path is specified, the new directory is created in the current working directory.

The command succeeds if the specified directory was successfully created, or if the specified directory already exists. The command fails if the new directory's immediate parent directory does not exist or is not a directory.

At times it is important to see how much cpu time is being used by a command. One function available to do this is the timer command. The syntax for this command is:

The start option will start a CPU timer that will continue until the stop command is issued. The elapsed time will be printed out on the command line. If no arguments are given, the command will act like a toggle.

This keyword allows you to add comments without affecting the behavior of CUBIT.

Comment ['<text_to_print>'] [<aprepro_var>] [<numeric_value>]

The comment command can take multiple arguments. If an argument is an unquoted word, it is treated as an aprepro variable and its value is printed out. Quoted strings are printed verbatim, and numbers are printed as they would be in a journal string. For example:

CUBIT> #{x=5} CUBIT> #{s="my string"} CUBIT> comment "x is" x "and s is" s User Comment: x is 5 and s is my string Journaled Command: comment "x is" x "and s is" s

This command allows you to display a listing of your previous commands.

History <number_of_lines>

For example, if you type history 10, the most recent 10 commands will be echoed to the input window.

[set] Logging Errors {Off | On File '<filename>'[Resume]}

This setting will allow users to echo error messages to a separate log file. The resume option will allow output to be appended to existing files instead of overwriting them. For more information on CUBIT environment settings see List Cubit Environment.

Expect Error {Stop ["message"] | <count> [less] [more]}

Use this command to expect and ignore a specific number of errors, so to not increment Cubit's error count. Wrap the command(s) generating the errors with expect error 5 and expect error stop, where 5 is the number of expected errors. Use the less or more options for approximating the number of errors, when how many generated is not stable. Example: expect error 5 less if you always expect less then five errors. The message option is useful for printing a note regarding the expected errors.

To determine information on version numbers, enter the command Version. This command reports the CUBIT version number, the date and time the executable was compiled, and the version numbers of the ACIS solid modeler and the VTK library linked into the executable. This information is useful when discussing available capabilities or software problems with CUBIT developers.

By default, commands entered by the user will be echoed to the terminal. The echo of commands is controlled with the command:

[Set] Echo {On | Off}

CUBIT uses all available precision internally, but by default will only print out a certain number of digits in order for columns to line up nicely. The user can override that with the "set digits" command:

Set Digits [<num_to_list=-1>]

If the digits are set to -1, then the default number of digits for pretty formatting are used. If the digits are set to a specific number, such as 15, more digits of accuracy can be displayed. This may be useful when checking the exact position and size of geometric features.

The number of digits used for listing positions, vectors and lengths can be listed using the following command:

Coordinates and lengths will be listed with up to 6 digits.

For this platform, max digits = 15. Coordinates and lengths will be listed with up to 15 digits.

To reset digits to default, use 'set digits -1'

The number of coordinate and length digits listed will vary depending on the context.

---

## Environment Control

**URL:** https://coreform.com/cubit_help/environment_control/environment_control.htm

**Contents:**
- Environment Control

The CUBIT user interface is designed to fill multiple meshing needs throughout the design to analysis process. The user interface options include a full graphical user interface, a modern command line interface as well as no-graphics and batch mode operation. This chapter covers the interface options as well as the use of journal files, control of the graphics, a description of methods for obtaining model information, and an overview of the help facility.

---

## Environment Variables

**URL:** https://coreform.com/cubit_help/environment_control/session_control/environment_variables.htm

**Contents:**
- Environment Variables

CUBIT can interpret the following environment variables. These settings are only applicable to the Command Line Version of CUBIT and do not apply to the Graphical User Interface. See also the CUBIT_STEP_PATH and CUBIT_IGES_PATH environment variables. See also the CUBIT_DIR, HOMEDRIVE and HOMEPATH settings.

Specifies path and name to use for journal file. The specified path may contain the following %-escape sequences:

%a - abbreviated weekday name %A - full weekday name %b - abbreviated month name %B - full month name %d - date of the month [01,31] %H - hour (24-hour clock) [00,23] %I - hour (12-hour clock) [01,12] %j - day of the year [1,366] %m - month number [1,12] %M - minute [00,59] %n - replaced with the next available number between 01 and 999. %p - "a.m." or "p.m." %S - seconds [00,61] %u - weekday [1,7], 1 is Monday %U - week of year [00,53] %w - weekday [0,6], 0 is Sunday %y - year without century [00,99] %Y - year with century (e.g. 1999) %% - a '%' character

The default value is "cubit%n.jou". This creates journal files in the current directory named "cubit00.jou", "cubit01.jou", "cubit02.jou", etc. To keep the same naming scheme but create the files the /tmp directory, set CUBIT_JOURNAL to "/tmp/cubit%n.jou"

To create journal files in directories according to the day of the week, first create directories named "Mon", "Tues", etc. CUBIT will not create them for you. Next set CUBIT_JOURNAL to "%a/%n.jou". This will create journal files named "01.jou" through "999.jou" in the appropriate directory for the current day of the week.

---

## Execution Command Syntax

**URL:** https://coreform.com/cubit_help/environment_control/session_control/execution_command_syntax.htm

**Contents:**
- Execution Command Syntax
- Passing Variables into a CUBIT Session

Cubit is available as a GUI application, a command line application or as a module that can be loaded in Python. The GUI application can be accessed by running bin/claro and the command line application can be accessed by running bin/cubit. On Linux, an additional cubit script is provided which can start either bin/claro or bin/cubit depending on whether the -nogui option is given. Cubit can be loaded into Python if the bin folder is given to sys.path or if it is given in the PYTHONPATH environment variable.

When running in batch mode, it is strongly recommended to run cubit.

The applications can be run as rollows:

bin/cubit [options and args] [journalFile(s)]

bin/claro [options and args] [journalFile(s)]

Input journalFiles or scripts can be given after all other options are given. These scripts can be in either Cubit syntax or in Python syntax. The syntax is Python if the script has a .py file extension. For .jou files or files with other extensions, the #!cubit or #!python comments in the file indicate how to interpret the syntax.

Command options for the command line are:

cubit -help (Print this summary) -Include <$val> (Specify a journal file) -workingdir <$val> (Directory to use as working directory) -input $val (Playback commands in file $val) -solidmodel <$val> (Read .sat, .cub or .exo from file $val) -nogeom (Read .exo from -solidmodel $val without creating geometry) -lite (Read .exo from -solidmodel $val in lite mode) -fastq <$val> (Read FASTQ file $val) -initfile <$val> (Read $val as initialization file instead of $HOME/.cubit) -batch (Batch Mode - No Interactive Command Input) -nographics (Do not display graphics windows) -nogui (Do not display graphical user interface) -noinitfile (Do not read .cubit file) -noecho (Do not echo commands to console) -nojournal (Do not write journal file) -nodeletions (Do not allow file deletions) -journalfile <$val> (Name of journal file, will be overwritten) -restore [$val] (Name of restore file (default = cubit_geom.save.sat)) -maxjournal [$val] (Maximum number of journal files to write) -warning [$val] (Warning Messages On/Off) -information [$val] (Informational Messages On/Off) -debug <$val> (Set specified flags on, e.g. 1,3,7-9 enables 1,3,7,8,9)) -display <$val> (Specify display to be used for graphics window) -driver <$val> (Specify the type of driver to be used for graphics display) -nooverwritecheck (Do not perform file export overwrite check) -nobanner (Suppress printing of startup information) -version (Prints version information) -log <$val> (Copy all output to specified file) -python_version <version> (The major version of python to use: 2 or 3 APREPRO variable pair (Quoted name value pair)

Each of these is optional. If specified, the quantities in square brackets, [$val], are optional and the quantities in angle brackets, <$val>, are required.

Options are summarized in more detail below:

Print a short usage summary of the command syntax to the terminal and exit.

Set the working directory to be used at startup. Journal files will be written to this directory.

Use the file specified by <$val> as the initialization file instead of the default set of initialization files. See Initialization Files

Do not read any initialization file. This overrides the default behavior described in Initialization Files

Read the ACIS solid model geometry or .cub file information from the file specified by <$val> prior to prompting for interactive input.

Specify that there will be no interactive input in this execution of CUBIT. CUBIT will terminate after reading the initialization file, the geometry file, and the input_file_list.

Run CUBIT without graphics. This is generally used with the -batch option or when running CUBIT over a line terminal.

Run CUBIT without the graphical user interface.

Sets the location where the CUBIT graphics system will be displayed, analogous to the -display environment variable for the X Windows system. Unix only.

Sets the <type> of graphics display driver to be used. Available drivers depend on platform, hardware, and system installation. Typical drivers include X11 and OpenGL.

Do not create a journal file for this execution of CUBIT. This option performs the same function as the Journal Off command. The default behavior is to create a new journal file for every execution of CUBIT.

Write the journal entries to <file>. The file will be overwritten if it already exists.

Only create a maximum of <$val> default journal files. Default journal files are of the form cubit#.jou where # is a number in the range 01 to 999.

Turn off the ability to delete files with the delete file '<filename>' command.

Turn off the file overwrite check flag. Files that are written may then overwrite (erase) old files with the same name with no warning. This is typically useful when re-running journal files, in order to overwrite existing output files. See the set File Overwrite Check [ON|off] command.

Restore the specified filename (or "cubit_geom") mesh and ACIS files, e.g. cubit_geom.save.g and cubit_geom.save.sat.

Do not echo commands to the console. This option performs the same function as the Echo Off command. The default behavior is to echo commands to the console.

Set to "on" the debug message flags indicated by <$val>, where <$val> is a comma-separated list of integers or ranges of integers, e.g. 1,3,8-10.

Turn {on|off} the printing of information messages from CUBIT to the console.

Turn {on|off} the printing of warning messages from CUBIT to the console.

Allows the user to specify a journal file from the command line.

Read the mesh and geometry definition data in the FASTQ file <file> and interpret the data as FASTQ commands. See T. D. Blacker, FASTQ Users Manual Version 1.2, SAND88-1326, Sandia National Laboratories, (1988). for a description of the FASTQ file format.

Input files to be read and executed by CUBIT. Files are processed in the order listed, and afterwards interactive command input can be entered (unless the -batch option is used.)

The input files can be in either Cubit syntax or in Python syntax.

Copies all output to the specified file.

The major version of python to use: 2 or 3.

APREPRO variable-value pairs to be used in the CUBIT session. Values can be either doubles or character type (character values must be surrounded by double quotes.). Command options can also be specified using the CUBIT_OPT environment variable. (See Environment Variables .)

To pass an aprepro variable into a CUBIT Session, start cubit with the variable defined in quotes i.e. cubit "some_var=2.3"

---

## Extended Command Line Entity Specification

**URL:** https://coreform.com/cubit_help/environment_control/entity_selection_and_filtering/extended_entity_specification.htm

**Contents:**
- Extended Command Line Entity Specification
- Extended Parsing Syntax
- Keywords
- Functions
- Precedence

In addition to basic entity specification, entities may be specified using an extended expression. An extended expression identifies one or more entities using a set of entity criteria. These criteria describe properties of the entities one wishes to operate upon.

The most common type of extended parsing expression is in the following format:

{Entity_Type} With {Criteria}

Entity_Type is the name of any type of entity that can be used in a command, such as Curve, Hex, or SideSet. Criteria is a combination of entity properties (such as Length), operators (such as >=), keywords (such as Not), and values (such as 5.3) that can be evaluated to true or false for a given entity. Here are some examples:

surface with is_meshed = false

node with x_coord > 10 And y_coord > 0

These are the keyword defined by extended parsing

These keywords are used the same way as in basic entity specification. For example:

draw surface 1 to 5 step 2 curve 1 to 3 in body 4 to 8 by 2

draw hex in face in surface 2

draw face common_to volume 1 2

draw node in hex in face in surface 2 curve 1 2 5 to 50 except 2 3 4

draw volume 10 include similar

Not flips the logical sense of an expression - it changes true to false and false to true. For example:

draw surface with not is_meshed

The "of" operator is used to get an attribute value for a single entity, such as "length of curve 5". Only attributes that return a single numeric value may be used in an "of" expression. There must be only one entity specified after the "of" operator, but it can be identified using any valid entity expression. An example of a complete command which includes the "of" operator is:

list curve with length < length of curve 5 ids

These logic operators determine how multiple criteria are combined.

draw surface with length > 3 or with is_meshed = false

These relational operators compare two expressions. You may use = or == for "equals". <> means "not equal". For example:

draw surface with x_max <= 3

draw volume with z_max <>12.3

In the case of = or == you may include a tolerence parameter for these relational operators rather than needing to write a more lengthy inequality with >= and <=. For example:

draw curve with length = 5 tolerance 1e-3

These arithmetic operators work in the traditional manner.

draw surface with length * 3 + 1.2 > 10

Parentheses are used to group expressions and to override precedence. When in doubt about precedence, use parentheses.

draw surface with length > 3 and ( with is_meshed = false or x_min > 1 )

The following functions are defined. Not all functions apply to all entities. If a function does not apply to a given entity, the function returns 0 or false.

The length of a curve or edge

The area of a surface.

The volume of a volume.

Works for curves with an exterior angle greater than (>), less than (<), or equal to (=) a given angle in degrees. This is used if you want to do some operation, such as refinement, on all the reentrant curves or curves with surfaces that form a certain angle.

Radius of an arc or blend surface.

Compares the normal of a surface to a vector.

draw surface with normal 1 0 0

The given vector is normalized to a unit vector for comparison. The two vectors are compared using the magnitude of the difference between them. A default tolerance of 1e-6 is used unless specified.

draw surface with normal 1 0 0 tolerance 0.001

Compares the element type of a block.

select block with type "tetra10"

The element type needs to be in quotes. The generic element type can be used to select any order of that element type. For example:

hex => hex8, hex20, hex27

Whether a Volume has a duplicate (exact copy of itself at the same location)

Whether a geometric entity has been meshed or not

Whether a geometric entity is defined using a NURBS representation. Otherwise the entity has an analytic representation.

Whether a geometric surface is a blend. Blends have a constant principal radius of curvature and meet two or more adjoining surfaces at an angle of approximately 180 degrees. "Fillets" are examples of blend surfaces.

Whether a geometric surface is a chamfer. Chamfers are thin surfaces bounded by surfaces where the exterior angle is approximately 45 or 225 degrees.

Whether a geometric surface is planar.

Whether a geometric surface is periodic, such as a sphere or torus.

A geometric entity is a sheetbody if it is a collection of surfaces that do not form a solid.

The number of elements owned by this geometric or exodus entity. Only elements of the same dimension as the geometric entity are counted (number of hexes in a volume, number of faces on a surface, etc.). For an exodus entity, all contained mesh entities are counted.

The topological dimension of an entity (3 for volumes, 2 for surfaces, etc.).

The x, y, or z coordinate of the entity's bounding box center point projected onto the entity.

The x, y, or z coordinate of the minimum extent of the entity's bounding box

The x, y, or z coordinate of the maximum extent of the entity's bounding box

Whether a geometry entity has a merge flag on. All geometric entities have one set by default.

A flag that specifies whether an entity is virtual geometry. An entity is virtual if it has at least one virtual (partition/composite) topology bridge.

An entity "has_virtual" if it is virtual itself, or has at least one child virtual entity

An entity "is_real" if it has at least one real (non-virtual) topology bridge.

Used to specify geometry entities with a specified number of parent entities. May be used to find "free curves" where num_parents=0 or non-manifold curves where num_parents>2.

Used to specify geometry entities without parent entities. May be used to find free curves and vertices where num_parents=0 or free surfaces that do not form a solid (sheet bodies).

Used to specify elements which have been assigned to a block. This is also useful to find elements NOT assigned to a block by using "not block_assigned".

Used to specify geometry entities which have been assigned a specified scheme. The scheme name is specified with the keyword string used when setting the scheme. Wildcards can also be used when specifying the scheme name. For example, draw surface with has_scheme '*map' will draw surfaces with scheme map or submap.

Used with the include keyword. Compares a list of geometry entities and adds additional entities that are classified as similar. Implemented for curves, surfaces and volumes. Similar is defined as the same geometric length, area or volume using a tolerance of 0.1 percent, as well as the same number of child entities. For example, "draw volume 10 include similar" will draw all volumes with the same geometric volume and number child surfaces as volume 10.

Used with the include keyword. Compares a list of surface entities and adds additional adjacent surfaces that are part of the same cavity. Implemented only for surfaces. A cavity is defined as the collection of surfaces bounded by curves where the exterior angle is greater than 180 degrees. For example, "draw surface 10 include cavity" will draw surface 10 along with the cavity to which it belongs.

Used with the include keyword. Compares a list of surface entities and adds additional adjacent surfaces that are part of the same hole. Implemented only for surfaces. A hole is a special case of a cavity that includes at least one cylindrical surface. For example, "draw surface 10 include hole" will draw surface 10 along with the hole to which it belongs.

Used with the include keyword. Compares a list of surface entities and adds additional adjacent surfaces that are part of the blend_chain. Implemented only for surfaces. A blend_chain is defined as the collection of attached surfaces that have the same minimum radius of curvature. For example, "draw surface 10 include blend_chain" will draw surface 10 along with the blend_chain to which it belongs.

Used with the include keyword. Compares a list of surface entities and adds additional adjacent surfaces that are part of the chamfer_chain. Implemented only for surfaces. A chamfer_chain is defined as the collection of attached surfaces that have the same width and are bounded by exterior angles of 135 and/or 225 degrees. For example, "draw surface 10 include chamfer_chain" will draw surface 10 along with the chamfer_chain to which it belongs.

Used with the include keyword. Compares a list of curve or surface entities and adds additional adjacent entities that are continuous. Implemented for curves and surfaces. For surfaces, continuous is defined as the collection of attached surfaces that are bounded by curves where the exterior angle is approximately 180 degress (tolerance = 15 degrees). For curves, continuous is defined as the collection of attached curves that are bounded by vertices where the angle is approximately 180 degrees (tolerance = 15 degrees). For example, "draw surface 10 include continuous" will draw surface 10 along with other surfaces within the same continuous collection.

Used with the include keyword. It will include additional geometry entities of the same dimension that are within a small distance of the specified entities. Implemented for curves, surfaces and volumes. The distance tolerance is automatically defined relative to the size of the entity(s). An example use case would be, "draw volume 10 include nearby" which will draw volume 10 along with volumes that are within a small distance of volume 10.

For complicated expressions, which entities are referred to is influenced by the order in which portions of the expression are evaluated. This order is determined by precedence. Operators with high precedence are evaluated before operators with low precedence. You may always include parentheses to determine which sub-expressions are evaluated first. Here all operators and keywords listed from high to low precedence. Items listed together have the same precedence and are evaluated from left to right.

(, ) Expand Not *, / +, - <, >, <=, >=, <>, = And, Or Except In Of With

Because of precedence, the following two expressions are identical:

curve with length + 2 * 2 > 10 and length <= 20 in my_group

expand(curve with (((length + (2*2)) > 10 )and( length <= 20 ))) in ( my_group expand )

---

## Extended Selection Dialog

**URL:** https://coreform.com/cubit_help/environment_control/entity_selection_and_filtering/extended_selection_dialog.htm

**Contents:**
- Extended Selection Dialog
- Accessing the Dialog
  - Launch the Dialog
  - Load Existing Filters
  - Use a Filter
  - Dragging from Target Entities to Source Selection
- Creating Parameterized Filters
- Writing Custom Python Filters
  - The Selection Filter Class
  - A Sample Filter that includes Additional User Interface

Selecting entities in the graphics window can sometimes be complicated. The Extended Selection Dialog leverages the combination of Python and the CubitInterface class to give users a very powerful mechanism for creating and managing custom selection filters.

The dialog is accessible any time a geometry entity is selected in the graphics window. Consider this workflow:

When the dialog is first shown, no filters are available.

Load existing filters by:

The very first time this dialog is shown, the path to the filters folder will be blank and no filters will be shown in the filter list. Press the "Browse" button and select the folder that contains the custom filters. This folder can be anywhere on the file system. Cubit will remember the location and use it during subsequent sessions. The folder may be changed at any time.

A list of custom filters, written in Python, will be shown. Select any given filter to examine its contents. Check all filters to be included in the menu for Extended Filters. Then press "OK".

At this point, all of the filters selected in the Locate and Load Filters dialog will be available for use in the Extended Selection dialog.

Use the pull down menu to select a filter. Click on an entity in the Source Selection list. Geometric entities that fit the filter criterion will be shown in the Target Entities list.

Depending on the nature of the selection filter it may be useful to 're-seed' the Source Selection with an item from Target Entities. Simply drag an item or items from Target Entities into the Source Selection list.

Parameterized filters will require a user interface which will be added into the extended selection filter dialog. The user interface can be made using Qt's Designer, which is a free tool that ships with the Qt toolkit. The Qt Designer tool produces an XML file that will be read by Cubit and automatically included in the Extended Selection Filter dialog.

For example, if we wanted to create a selection filter that would select all entities of a certain type within a certain radius of a source entity, we would require a user interface that captures the desired radius and the desired entity type to be selected. An image of that user interface is shown below. The image was copied directly from Qt Designer.

Notice two input fields: 1) a Line Edit to capture the desired selection radius and 2) a Combo Box that contains "Volumes", "Surfaces", "Curves", "Vertices" to specify the target entity selection type. The extended selection filter that contains this custom interface is shown below. The example shows a selection of all curves within 1 unit of the source selection.

The class CubitInterface is used by the GUI to drive Cubit and access its database. You can read about the Python Interface used by Cubit for more details. Suffice to say, all of the functions and data included in CubitInterface are available to Python programmers.

Extended Selection custom filters are written in Python. Follow the instructions below, save the filters on the file system, then load the filters as explained above.

A Simple Example Filter

This first example shows a filter that will return a list of first generation children of the selected entities. No user input is required and no additional user interface is necessary.

As mentioned above, the custom Python filters must implement a class and that class must be derived from the SelectionFilter class. The SelectionFilter class is available in the Cubit SDK. The SDK is available to any user.

In order to include user input into an extended selection dialog, two additional things must happen:

Qt UI objects supported by the extended selection filter include:

As the example Python code shows, the Qt objects are referenced by name. These code snippets below are not complete. Complete examples and a video tutorial are available from www.csimsoft.com.

---

## Geometry, Mesh, and BC Entity Visibility

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/visibility.htm

**Contents:**
- Geometry, Mesh, and BC Entity Visibility

The visibility of geometry, mesh, BC and Genesis entities can be turned on or off, either individually or globally. After visibility is turned off, the associated entities will remain invisible until visibility is turned on again.

The command to control global visibility is:

{Mesh|Geometry|BC} { [Visibility] [on|off] }

This command sets the global visibility on or off for all mesh, geometry, or BC entities, respectively. Turning off BC visibility also affects Genesis entities such as blocks, sidesets, and nodesets. Global visibility settings take precedence over the visibility set on individual entities. By default, Mesh and Geometry visibility is on, and BC visibility is off.

Global visibility of geometry, mesh, and BC entities can also be controlled from these tool bar buttons in the GUI (from left to right):

The command to control the individual visibility of geometry entities is:

{ {Body|Curve|Surface|Volume|Vertex} <range> } [Mesh][Geometry] Visibility [On|Off]

If the Mesh keyword is included, only the visibility of the mesh belonging to the specified geometric entity is affected. Similarly, if the Geometry keyword is included, only the visibility of the geometry is affected. If neither keyword is included, the command is identical to including both keywords.

Invisibility of geometry is inherited; visibility is not. For example, if a volume is invisible, its surfaces are also invisible unless they also belong to some other visible volume. As another case, if the volume is visible, but a surface is set to invisible, the surface will not follow its parent's visibility setting, but will remain invisible.

If vertex visibility is turned on, the vertices of the geometry become visible. The default for vertex visibility is off. The default for all other geometry entities is on.

The commands to control visibility of edges and nodes are:

Edge [Visibility] [On|Off]

Node [Visibility] [On|Off]

These commands set the global visibility on or off for all edges or nodes, respectively. If edge visibility is off, mesh edges will not be drawn when mesh faces are drawn. Edge visibility is on by default; node visibility is off by default. Face visibility is always on when mesh visibility is on.

The command to control the individual visibility of genesis entities is:

{Block|Nodeset|Sideset} <range> visibility [{on|off}]

Genesis entities and boundary conditions are best viewed with geometry and mesh visibility off and BC visibility on.

Entity visibility for individual geometry and Genesis entities can also be controlled via context (right-click) menus in the Tree and in the graphics window.

Entities that are not visible can still be drawn temporarily using the "draw" command to display one or more specific entities.

---

## Geometry Power Tools

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/repair_and_analysis.htm

**Contents:**
- Geometry Power Tools
- Suggested Usage
- Geometry Analysis Tools
  - Small Features
  - Bad Angles
  - Traits
  - Assembly Checks
- Geometry Repair Tools
- Context (Right Click) Menu
  - Test Categories

Figure 1. Geometry power tools panel

Figure 2. Geometry power tools options panel

The geometry power tools, shown in Figure 1. are located on the Tree View window under the blue geometry tab. The Geometry Power Tool provides several diagnostic tests to identify and repair problems in your CAD model prior to meshing including machine learning-based diagnostics and solutions.

Diagnostic tests include:

This tool analyzes geometry for various characteristics that may affect meshing outcomes and aid in simplification and defeaturing. It also contains a powerful toolkit of geometry modification methods to fix these problems. Many of the common geometry clean-up tools are available from this tool without the need to search through the command panels for relevant operations.

The geometry power tool includes a window that lists results from geometry analysis in a tree format. In addition, a solution window can be displayed that will display specific suggested geometry solutions for the currently selected entity.

Figure 3. Geometry entity context menu in power tool.

Figure 4. Entitiy-specific solutions displayed in geometry power tool.

The geometry power tools, contain various diagnostic tests that can be run on geometry to diagnose potential problems for mesh generation and defeaturing. To display a list of tests, click on the Options... button. The panel shown in Figure 2. will appear. Select or deselect the desired options from the window before performing an analysis. To avoid long analysis times, select only tests that are relevant for your current problem scope. Cubit will also save the current test selections between runs. The geometry analysis tests are summarized below:

Figure 5. Bad Angle at Vertex Example

Figure 6. Tangential Intersection Example

Figure 7. Close Loop Example

Figure 8. Chamfer Examples

Figure 9. Blend Examples

Figure 10. Hole Example

Figure 11. Cavity Example

Figure 12. Cone Example

For assemblies of volumes, it is important to identify if volumes will be connected (imprinted and merged) are in contact, or separated by some distance. The Assembly Checks provide diagnostics and solutions to validate and resolve these interactions.

The Gaps, Overlaps and Misalignments diagnostics normally identify undesirable conditions that must be resolved prior to imprint and merge. Once resolved, the Volume Contacts and Mergable Geometry can be used to validate connections before and after imprinting and merging.

The Options panel also provides a way to estimate or manually set an imprint tolerance. Entities closer than this tolerance will be considered mergable when used with the tolerant imprint command. When the Tolerant Imprint checkbox is selected in the Options panel, the diagnostic tests that identify gaps, overlaps and misalignments will also use the specified tolerance when computing issues.

Figure 13. Volume Gap Example

Figure 14. Volume Overlap Example

Figure 15. Volume Misalignment Example

The split surface tool is used to split a surface into two surfaces. This is useful for blend surfaces, for example, where splitting a surface may facilitate sweeping. To select a surface for splitting, click on the surface in the tree view. To select multiple surfaces in the window, hold the CTRL key* while selecting surfaces (surfaces must be attached to each other). Then press the split surface button to bring up the Control Panel window with the ids of selected surfaces in the text input window. The split surface menu is located on the Control Panel under Geometry-Surface-Modify. You must press the Apply button for the command to be executed. You can also bring up the Split Surface menu by selecting surfaces in the tree view and selecting Split from the right click menu.

*Note: For Mac computers, use the command key (or apple key) to select multiple entities

The healing function in Cubit is used to improve ACIS geometry that has been corrupted during file import due to differences in tolerances, or inherent limitations in the parent system. These errors may include: geometric errors in entities, gaps between entities, and the absence of connectivity information (topology). To heal a volume, select the volume in the geometry repair tree view. Then press the heal button. You may also press the heal button without a geometry selected in the window, and enter it later. The Control Panel window will come up under the Geometry-Volume-Modify option with the selected volume id highlighted. If no entity is selected, or if another entity type is selected, the input window will be blank. You can also open the healing control panel by selecting Heal from the right click menu in the geometry power tools window.

The tweak command is used to eliminate gaps between entities or simplify geometry. The tweaking commands modify geometry by offsetting, replacing, or removing surfaces, and extending attached surfaces to fill in the gaps. Tweaking can be applied to surfaces, and it can be applied to curves with a valence no more than 2 at each vertex. It can also be applied to some vertices. To tweak a surface, select the surface in the tree view. The Geometry-Surface-Modify control panel will appear with the selected surface id in the input window.

Tweaking is available for curves. Tweaking a curve creates a blended or chamfered edge between two orthogonal surfaces. The curve option is located on the Geometry-Curve-Modify panel under the Blend/Chamfer pull-down option.

Tweaking is also available for some vertices. Tweaking a vertex creates a chamfered or filleted corner between three orthogonal surfaces. The vertex option is located on the Geometry-Vertex-Modify panel under the Tweak pull-down menu.

Note: Only curves with valence 2 or less at each vertex are candidates for tweaking. Any other curve will cause the Geometry-Surface-Modify menu to appear.

The merge command is used to merge coincident surfaces, curves, and vertices into a single entity to ensure that mesh topology is identical at intersections. Unlike other buttons on the geometry repair panel, the merge button acts as an "Apply" button itself. All geometry that is listed under "mergeable entities" will be merged.

The remove button is used to simplify geometry by removing unnecessary features. To use the remove feature, click on the surface(s) in the Tree View. Right click and select the Remove Option, or click the Remove icon on the toolbar. The Control Geometry-Surface-Modify control panel will appear, with the surface ids in the input window. The Remove control panel can also be accessed from the right-click menu in the Geometry Power Tools window. Select options and press apply.

Regularize Entity Button

The regularize button is used to remove unnecessary topology. Regularizing an entity will essentially undo an imprint command.

The remove slivers button is used to remove surfaces with less than a specified surface area. When ACIS removes a surface it extends the adjoining surfaces to fill the gap. If it is not possible to extend the surfaces or if the geometry is bad the command will fail.

The auto clean button is used to perform automatic cleanup operations on selected geometry. These automatic cleanup operations include forcing sweepable configurations, automatically removing small curves, automatically removing small surfaces, and automatically splitting surfaces.

The composite button is used to combine adjacent surfaces or curves together using virtual geometry . Virtual geometry is a geometry module built on top of the ACIS representation. Surfaces may be composited to simplify geometry in order to facilitate sweeping and mapping algorithms by removing constraints on node placement. It is important to note that solid model operations such as webcut, imprint, or booleans, cannot be applied to models that have virtual geometry. Both curves and surfaces may be composited.

Collapse Angle Button

The collapse angle button uses virtual geometry to collapse small angles. This is accomplished by partitioning and compositing surfaces in a way so that the small angle gets merged into a larger angle. Pressing the collapse button on the geometry power tools will open the collapse menu under Geometry-Vertex-Modify control panel. This panel can also be opened by selecting Collapse from the right click menu in the Geometry Tools window.

Collapse Surface Button

Pressing this button will open the collapse surface panel on the main control panel. The collapse surface function uses virtual geometry to eliminate small surfaces on the model to improve mesh quality. It is most useful for blend surfaces.

Collapse Curve Button

Pressing this button will open the collapse curve panel on the main control panel. The collapse curve command is used to eliminate small curves using virtual geometry.

Reset Graphics Button

The reset graphics button will refresh the graphics window display.

Note: Pressing most of the geometry tool buttons on the panel will only bring up applicable command panels on the Control Panel. You must press the Apply button on the Control Panel to execute the command.

The following right click menu options are available from the geometry power tool's main window when a geometry entity or category is selected. Figure 3. shows an example of a context menu. Specific options depend on the type of entity or category.

Each of the following menu options are available based on the category and entity type selected. In each case they will open the relevant command panel pre-populated with the entity selected. Select multiple entities prior to selecting the context menu item below to execute the command on multiple entities simulaneously.

---

## Graphical User Interface

**URL:** https://coreform.com/cubit_help/environment_control/gui/gui.htm

**Contents:**
- Graphical User Interface

The graphical user interface (GUI) can improve user productivity. It provides an easy way to control CUBIT without learning command syntax. Many geometry commands are faster and easier with the GUI. The underlying GUI components are constructed using a cross-platform development environment. As such, the GUI will behave similarly across all platforms supported by Cubit, yet each GUI will make use of platform specific widgets.

The GUI is built on top of the CUBIT command line. This means that GUI actions are translated to a CUBIT command-line string and journaled. Users familiar with command-line syntax can enter the same text in the GUI command-line window. Journal files can be created and played back in both environments with the same results. Although many things are faster and easier in the GUI, experienced users often use a combination of command line text and GUI button operations.

The discussion of the Graphical User Interface and its features is based on the basic windows contained within the CUBIT GUI Application Window. These are outlined in the subtopics listed above.

---

## Graphics Camera

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/graphics_camera.htm

**Contents:**
- Graphics Camera
- Changing Camera Attributes Directly

One way to change what is visible in the graphics window is to manipulate the camera used to generate the scene. A scene camera has attributes described below, and depicted graphically in Figure 1. The values of these camera attributes determine how the scene appears in the graphics window.

These view settings may be accessed in the GUI via the Display/View Point menu.

Position (From) - The location of the camera in model coordinates.

View Direction (At) - The focal point of the camera in model coordinates.

Up Direction (Up) - The point indicating the direction to which the top of the camera is pointing. The Up point determines how the camera is rotated about its line of sight.

Projection - Determines how the three-dimensional model is mapped to the two-dimensional graphics window.

Perspective Angle - Twice the angle between the line of sight and the edge of the visible portion of the scene.

Figure 1: Schematic of From, At, Up, and Perspective Angle

The camera can be moved to one of several predefined orientations using the command

View {Front | Back | Top | Bottom | Right | Left | Iso}

At any time, the camera can be moved back to its original position and view using the command

To see the current settings of these attributes, use the command

The current value of the view attributes will be printed to the terminal window, along with other useful view information such as the current graphics mode and the width of the current scene in model coordinates.

Camera Attributes can be changed using the Rotate, Zoom and Pan commands, or directly as follows.

Camera attributes are most easily modified using interactive mouse manipulation (see Mouse-Based View Navigation) or using the rotate, pan and zoom commands. However, the camera attributes can also be modified directly with the following commands:

At {Body|Volume|Surface|Curve|Vertex|Hex|Tet|Wedge|Tri|Face|Node}<id_list>

Graphics Perspective <On|Off>

Graphics Perspective Angle <degrees>

If graphics perspective is on, a perspective projection is used; if graphics perspective is off, an orthographic projection is used. With a perspective projection, the scene is drawn as it would look to a real camera. This gives a three-dimensional sense of depth, but causes most parallel lines to be drawn non-parallel to each other. If an orthographic projection is used, no sense of depth is given, but parallel lines are always drawn parallel to each other.

In a perspective view, changing the perspective angle changes the field of view by changing the angle from the line of sight to the edge of the visible scene. The effect is similar to a telephoto zoom with a camera. A smaller perspective angle results in a larger zoom. This command has no effect when graphics perspective is off.

The GUI tool bar button for changing the graphics perspective mode is as follows:

---

## Graphics Clipping Plane

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/clipping_plane.htm

**Contents:**
- Graphics Clipping Plane
- Examples

The graphics clipping plane feature allows the user to temporarily cut parts of the model away to help visualize the interior of a geometry or mesh. The command syntax is:

Graphics Clip {On|Off} [ Plane <plane> | [Location <location>] [Direction <direction>]]

Graphics Clip Manipulation {On|Off}

Figure 1. Graphics Clipping Plane

The second command turns on/off the visibility of manipulation widget in the graphics window. The clipping plane is still active, but the controls are hidden. The normal mouse-based view navigation controls apply.

brick x 10 sphere rad 1 graphics clip on location -2 0 0 rotate -45 about y #shows the sphere inside the brick

brick x 10 cylinder rad 2 z 12 subtract 2 from 1 mesh vol 1 quality vol 1 draw mesh graphics clip on #shows the mesh quality on interior elements

Figure 2. Viewing mesh quality of interior elements

---

## Graphics Lighting Model

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/lighting_model.htm

**Contents:**
- Graphics Lighting Model

For shaded graphics display modes, the lighting model controls the intensity of the highlights and shadows for objects displayed in the graphics window. CUBIT offers two commands for controlling the lighting model.

Graphics Ambient Intensity {<intensity> | <r g b>}

Graphics Light Intensity {<intensity> | <r g b>}

The ambient intensity is the light available in the environment. There is no particular direction to the light source. In contrast, the light intensity is the effect of a simulated light source placed at the viewer's line of sight. The light intensity affects the intensity of the highlights and shadows, while the ambient intensity affects the brightness of the objects in the overall scene.

An intensity value from 0 to 1 can be used, where 0 represents no light and 1 represents maximum. Alternatively r g b color components can be used. This changes the color of the directional or ambient light source, affecting the resulting color of the objects in the model.

The GUI Options panel for manipulating these settings is found under Tools/Options and is shown below:

---

## Graphics Modes

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/graphics_modes.htm

**Contents:**
- Graphics Modes
- Displaying Using the Element Facets
- Displaying Composite Surface Lines

By default, the scene is viewed as a smoothshaded model. That is, only curves and edges are drawn, and surfaces are transparent. Surfaces can be drawn differently by changing the graphics mode:

Graphics Mode {Wireframe | Hiddenline | Smoothshade | Transparent } [Geometry | Mesh | Highlight]

The GUI tool bar buttons for manipulating the graphics modes are as follows:

Examples and a brief description of each mode are shown below

This determines what pattern is used to draw lines behind surfaces (e.g. dotted, dashed, etc.; click here for a list of valid line patterns).

There is another option that is similar to a graphics mode, set with the command

Graphics Use Facets [On|Off]

This command determines how shaded and filled surfaces are drawn when they are meshed. If Graphics Use Facets is on, the mesh facets (element faces) are used to render the model. This is particularly helpful for curved surfaces which may cut through some of the mesh faces. A comparison of graphics facets on and off is shown below.

Figure 1. A meshed cylinder shown with graphics facets off (left) and graphics facets on (right); note how geometry facets on the curved surface obscure mesh edges when facets are off.

Composite surfaces are surfaces that have been joined together using virtual geometry. By default, the underlying surfaces are marked with dashed lines. To toggle this setting so that underlying surfaces are not shown, use the following command:

Graphics Composite {On|Off}

Figure 2. A part shown with (a) composite surfaces displayed (b) composite surfaces not displayed

The GUI tool bar button for toggling the display of graphics composites is as follows:

---

## Graphics Window

**URL:** https://coreform.com/cubit_help/environment_control/gui/graphics_window/graphics_window.htm

**Contents:**
- Graphics Window

Figure 1. Graphics Window

The graphics window is used to view and select entities. Select one of the options below:

---

## Graphics Window Control

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/graphics_window_control.htm

**Contents:**
- Graphics Window Control

The graphics display windows present a graphical representation of the geometry and/or the mesh. The quality and speed of rendering the graphics, the visibility, location and orientation of objects in the window, and the labeling of entities, among other things, can all be controlled by the user.

Unless the -nographics option was entered on the command line, a graphics window with a black background and an axis triad will appear when CUBIT is first launched. The geometry and mesh will appear in this window, and can be viewed from various camera positions and drawn in various modes (wire frame, hidden line, smooth shade, etc.). This section will discuss methods for manipulating the graphics with the mouse and for controlling the appearance of entities drawn in the graphics window.

All geometry, mesh, and simulation objects created in CUBIT are put into the view automatically. Visibility, color and various other attributes of entities in the view can be controlled individually. In addition, CUBIT can also optionally show entities in a temporary view mode independent of their visibility. Drawing of items in temporary mode can be added to the regular view mode to customize the appearance. The overall view is controlled by various attributes like graphics mode, camera position, and lighting, to further enhance the graphics functionality.

The graphics view relies on OpenGL to render the scene which leverages the graphics hardware of the system. CUBIT requires the graphics hardware to support OpenGL version 3.2 or newer. If OpenGL 3.2 is not available, CUBIT will attempt to fall back to a software based implementation bundled with CUBIT. This software based approach may not perform as well as a hardware-based approach.

The following items discuss the various graphics capabilities available in CUBIT:

---

## Graphics Window Size and Position

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/graphics_window.htm

**Contents:**
- Graphics Window Size and Position
- Using Multiple Windows

By default in the command line version, CUBIT will create a single graphics window when it starts up (to run CUBIT without a graphics window, include -nographics on the command line when launching CUBIT.) The graphics window position and size is most easily adjusted using the mouse, like any other window on an X-windows screen. However, the size of the graphics window can also be controlled using the following commands:

Graphics WindowSize <width_in_pixels> <height_in_pixels>

Graphics WindowSize Maximum

Graphics WindowSize Minimum

After using the Graphics WindowSize Maximum and Graphics WindowSize Minimum commands, the previous window size can be restored by using the command

Graphics WindowSize Restore

The position of the graphics window can also be controlled using the Graphics WindowLocation command.

Graphics WindowLocation <x> <y>

The <x> and <y> coordinates refer to the distance in pixels from the upper left hand corner of the monitor.

In addition, on Unix workstations, the graphics window size and position can be controlled by placing the following line in the user's .Xdefaults file:

cubit.graphics.geometry XxY+xpos+ypos

where the X and Y are window width and height in pixels, respectively, and xpos and ypos are the offsets from the upper left hand corner.

You can use up to ten graphics windows simultaneously, each with its own camera and view. Each window has an ID, from 1 to 10, shown in the title bar of the window. Commands that control camera attributes apply to only one window at a time, the active window. Currently, the display lists of all windows are identical.

The following commands are used to create, delete, and make active additional graphics windows. These commands are also valid in the GUI (by typing at the command line prompt.)

Graphics Window Create [ID]

Graphics Window Delete <ID>

Graphics Window Active <ID>

---

## GUI Basic Tutorial Step 10

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_10.htm

**Contents:**
- GUI Basic Tutorial Step 10
- Step 10: Defining Boundary Conditions

Let us assume that we need to define one material type for the entire mesh, and a single node-based boundary condition on all surfaces. This is accomplished by identifying an Element Block and a Nodeset, respectively; the id numbers assigned to these entities are assigned by the user, usually by some convention meaningful to the analysis to be done. The element block and nodeset are identified from the Materials and Properties button on the control panel.

Create a nodeset by following the steps below

---

## GUI Basic Tutorial Step 11

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_11.htm

**Contents:**
- GUI Basic Tutorial Step 11
- Step 11: Exporting the Mesh

Finally, the mesh needs to be written to an Exodus II file. This is easily done:

---

## GUI Basic Tutorial Step 1

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_01.htm

**Contents:**
- GUI Basic Tutorial Step 1
- Step 1: Beginning Execution

Type "cubit" from a UNIX prompt or select cubit from the start menu if you are running on a PC with Windows. The CUBIT Application Window will appear as illustrated below:

CUBIT Application Window

The use of each window in the CUBIT program is described briefly below

---

## GUI Basic Tutorial Step 2

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_02.htm

**Contents:**
- GUI Basic Tutorial Step 2
- Step 2: Creating the Brick

Now you may begin generating the geometry to be meshed. You will create a brick of width 10, depth 10 and height 10. The width and depth correspond to the x and y dimensions of the object being created. The "width" or x-dimension is screen-horizontal and the "depth" or y-dimension is screen-vertical. The height or z-dimension is out of the screen.

The brick should appear in your Graphics window as shown below.

If you would like to change the rendering mode of your model, you may click on one of the view buttons in the Display Tools tool bar.

---

## GUI Basic Tutorial Step 3

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_03.htm

**Contents:**
- GUI Basic Tutorial Step 3
- Step 3: Creating the Cylinder

Now you must form the cylinder which will be used to cut a hole in the brick.

The brick and the cylinder should appear in your display window as shown below:

---

## GUI Basic Tutorial Step 4

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_04.htm

**Contents:**
- GUI Basic Tutorial Step 4
- Step 4: Adjusting the Graphics Display

The geometry is drawn in the graphics window in perspective mode, by default from a viewing direction of the +z axis. This view can now be adjusted to verify the proper orientation of the geometry just created.

The following button clicks apply for 3-button mice (these are the default GUI settings):

Mouse button behavior can be customized from the Tools-Options menu for use with non 3-button mice.

Use the mouse buttons to make the display look like the figure below.

View from Different Perspective

---

## GUI Basic Tutorial Step 5

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_05.htm

**Contents:**
- GUI Basic Tutorial Step 5
- Step 5: Forming the Hole

Now the cylinder can be subtracted from the brick to form the hole in the block.

You can also select the brick or cylinder interactively. Place the cursor in the Subtract Volume ID(s) field and click. This field is known as a Pick Widget. Clicking in a pick widget automatically sets the graphics pick mode for the entity type expected by the pick widget. Move the cursor to the graphics window and, using the left mouse button, select an entity. The id of the selected entity will be echoed into the pick widget field. Holding the control key while selecting entities in the graphics window will select multiple entities.

Notice that both original volumes are deleted in the Boolean operation and replaced with a new volume, with an id of 1. The result of this operation is a single volume, a brick with a hole through it, as shown below.

Brick after Subtracting Cylinder

We have now completed creating the geometry, and are ready to generate a mesh.

---

## GUI Basic Tutorial Step 6

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_06.htm

**Contents:**
- GUI Basic Tutorial Step 6
- Step 6: Setting Interval Sizes

The volume shown in Step 5 will be meshed by sweeping a surface mesh from one side of the brick to the other. Before generating any mesh, the user must specify the size of the elements to be generated. In this example, one element size will be specified for the volume as a whole and a smaller size will be specified for around the hole. A direct interval setting will be specified for the sweep direction.

To set the interval size for the overall volume, do the following:

Since the brick is 10 units in length on a side, this specifies that each straight curve is to receive approximately 10 mesh elements.

In order to better resolve the hole in the middle of the top surface, we set a smaller size for the curve bounding this hole.

Note: There is not a separate interval action panel for curves. The interval and mesh actions for curves are grouped together in one panel.

Finally, we would like to generate exactly 5 element layers in the sweep direction. This is accomplished by setting the intervals on one of the curves in the sweep direction.

---

## GUI Basic Tutorial Step 7

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_07.htm

**Contents:**
- GUI Basic Tutorial Step 7
- Step 7: Surface Meshing

Now all necessary intervals have been set, the meshing can proceed. Begin by meshing the front surface (with the hole) using the paving algorithm. This is done in two steps. First, set the scheme for that surface to Pave, then issue the command to Mesh.

Place the cursor into the Surface ID(s) field. Select the front surface of the object by selecting anywhere within the region indicated. The id of Surface 11 will be echoed in the field.

A mesh should be generated on surface 11 using the paving algorithm. The result is shown below.

Surface Meshed with Paving

---

## GUI Basic Tutorial Step 8

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_08.htm

**Contents:**
- GUI Basic Tutorial Step 8
- Step 8: Volume Meshing

The volume mesh can now be generated. Again, the first step is to specify the type of meshing scheme that should be used and the second step is to issue the order to mesh. In certain cases, the scheme can be determined by CUBIT automatically. For sweepable volumes, the automatic scheme detection algorithm also identifies the source and target surfaces of the sweep automatically.

To instruct the code to automatically determine the meshing scheme, and in this case the source and target surfaces, do the following:

The final meshed body will appear in the Graphics Window, as shown below:

Smooth Shade View of Volume Mesh

---

## GUI Basic Tutorial Step 9

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/step_09.htm

**Contents:**
- GUI Basic Tutorial Step 9
- Step 9: Inspecting the Model

The type, quality, and speed of rendering the image can be controlled in CUBIT by selecting one of the buttons in the Display icon group. These icons appear by default in the icon bar above the graphics window. They can be used to change the display mode to wire frame, hidden line, true hidden line, transparent or smooth shade.

For example, the following two figures result from selecting the Hidden Line and Wire Frame Mode buttons respectively.

Hidden Line View of Mesh

Wire Frame View of Mesh

Although CUBIT automatically computes limited quality metrics after generating a mesh and warns the user about certain cases of bad quality, it is still a good idea to inspect a broader set of quality measures. To do this, use the Command Window to enter the command:

CUBIT> quality volume 1 Allmetrics

The results of the quality are displayed in the Command Window. For an explanation of each quality metric along with acceptable ranges, see Mesh Quality Assessment. For the purposes of this tutorial, you can assume the quality metrics shown are in an acceptable range.

---

## Hardcopy Output

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/hardcopy_output.htm

**Contents:**
- Hardcopy Output
- Screen Capture Programs

CUBIT's Graphical User Interface provides the capability to print the contents of the graphics window directly to a printer. Use File/Export/Screen Shot to access this functionality.

In addition, a command line option is provided for dumping the contents of the graphics window to postscript or image files.

The command for generating hardcopy output files is:

Hardcopy '<filename>' {jpg | png | bmp | pnm | tiff | eps} [Window <window_id>]

Each of these options saves the view in the specified window (or the current window), to the specified file, in the format indicated. The file can then be sent to a printer or inserted into another document.

It should also be noted that many commercial applications are available for capturing screen images. In many cases, these applications may be more convenient for interactively capturing and saving a portion of the screen than the Hardcopy command discussed above. On UNIX platforms, the XV utility written by John Bradley is a good choice. In some cases this utility or its equivalent may be included with your system software. For Windows users, the Print Screen button will send a copy of the screen to the clipboard which can then be pasted into a paint program.

---

## Idless Journal Files

**URL:** https://coreform.com/cubit_help/environment_control/recording_and_playback/idless_journalfiles.htm

**Contents:**
- Idless Journal Files

Journal files can also be created without reference to entity IDs. The purpose of this command is to enable journal files created in earlier versions of CUBIT to be played back in newer versions of CUBIT. Using the "IDless" method, commands entered with an entity ID will be journaled with an alternative way of referring to the entity. Changes in CUBIT or ACIS often lead to changes in entity IDs. For example, a webcut may result in volume 3 on the left and volume 4 on the right. In another version of CUBIT, those entity IDs may be swapped (4 on the left and 3 on the right). Playing an IDless journal file makes the actual ID of an entity irrelevant. The syntax for this command is:

[set] Journal IDless {on|off|reverse}

The on option will enable idless journaling, and commands will be journaled without entity IDs. For example, "mesh volume 1" may be journaled as "mesh volume at 3.42 5.66 6.32 ordinal 2".

Selecting the off option will cause commands to be journaled in the traditional manner (i.e., as they are entered).

The reverse option allows you to convert idless journal files back into an ID-based journal file where the new journal file will reflect current numbering standards for IDs.

If you issue the command Journal IDless without any additional options, then the current status of ID journaling is printed. At startup, this should be "off".

The most likely scenario for converting older journal is to use the record command during playback. The following is an example.

journal idless on record "my_idless.jou" playback "my_journal.jou" record stop journal idless off

To record an idless journal file back into an id-based journal file you might use the following sequence.

journal idless reverse record "new_id_based.jou" playback "my_idless.jou" record stop journal idless off

Note: IDless conversions of APREPRO expressions are partially supported.

When IDless mode is set to ON, APREPRO functions such as Vx(id), that take an ID as an argument, are converted to use (x, y, z, ord) as arguments such as Vx(x, y, z, ord), where (x, y, z) is the center point coordinates and ord is the ordinal value. The ordinal values, 1..n, identifies each entity in a set of n entities that have a common center point. An entity's ordinal value is based on its creation order with respect to the other entities within the same set.

When IDless mode is set to REVERSE (using the above example) Vx(x, y, z, ord) will be converted to Vx(id). Outside these APREPRO functions, APREPRO expressions are not modified when converting a journal file to or from its IDless form. Hence, expressions reduced to an entity ID, such as in the command "volume {x} size 10," are not modified. Therefore, when moving a journal file from one version of CUBIT to another, it may be necessary to manually update IDs in APREPRO expressions.

---

## Initialization Files

**URL:** https://coreform.com/cubit_help/environment_control/session_control/initialization_files.htm

**Contents:**
- Initialization Files

CUBIT can execute commands on startup, before interactive command input, through initialization files. This is useful if the user frequently uses the same settings.

$(cubit install directory)/.cubit.install $HOME/.cubit $(current working directory)/.cubit

The $(cubit install directory) is determined by the location the program is installed. On Linux and Windows, it'll be the bin directory of the installation and on macOS it'll be the Cubit.app/Contents/MacOS directory.

$HOME is an environment variable pointing to the location of the user's home directory. On Windows, the HOMEDRIVE and HOMEPATH environment variables will be used instead of the HOME environment variable.

The $(current working directory) is determined by where the user starts the program itself.

If the -initfile <filename> option is used on the command that starts cubit, then the other init files are skipped and only the specified filename is played back.

These files are typically used to perform initialization commands that do not change from one execution to the next, such as turning off journal file output, specifying default mouse buttons, setting geometric and mesh entity colors, and setting the size of the graphics window.

---

## Interrupting Running Tasks

**URL:** https://coreform.com/cubit_help/environment_control/session_control/interrupting_running_tasks.htm

**Contents:**
- Interrupting Running Tasks

Many operations in the command line version of CUBIT can be interrupted using <Control>-C. Pressing <Control>-C will attempt to interrupt the running process as soon as feasible, returning the user back to the command line. Not all operations may be interrupted, and many can only be interrupted at certain stages. Any current tasks are canceled as soon as it is feasible to do so, including playback of journal files. The playback of a journal file is always stopped, even if the current running task cannot be interrupted. The journal file will stop at the next opportunity, when the current task is completed. Interrupted journal files may be resumed at the next command. See the section titled Controlling Playback of Journal Files for more information on controlling playback of journal files.

The GUI has a cancel button that can be used to interrupt the current command. The cancel button will turn red when a command can be interrupted. The cancel button has an 'x' on it, and is located on the status bar, which is at the bottom of the application.

---

## Journal File Creation and Playback

**URL:** https://coreform.com/cubit_help/environment_control/recording_and_playback/creation_and_playback.htm

**Contents:**
- Journal File Creation and Playback
- Recording a Session
- Replaying a Session

Command sequences can be written to a text file, either directly from CUBIT or using a text editor. CUBIT commands can be read directly from a file at any time during CUBIT execution, or can be used to run CUBIT in batch mode. To begin and end writing commands to a file from within CUBIT, use the command

Once initiated, all commands are copied to this file after their successful execution in CUBIT.

To replay a journal file, issue the command

Playback '<filename>'

Journal files are most commonly created by recording commands from an interactive CUBIT session, but can also be created using automatic journaling or even by editing an ASCII text file.

Commands being read from a file can represent either the entire set of commands for a particular session, or can represent a subset of commands the user wishes to execute repeatedly.

Two other commands are useful for controlling playback of CUBIT commands from journal files. Playback from a journal file can be terminated by placing the Stop command after the last command to be executed; this causes CUBIT to stop reading commands from the current journal file. Playback can be paused using the Pause command; the user is prompted to hit a key, after which playback is resumed.

Journal files are most useful for running CUBIT in batch mode, often in combination with the parameterization available through the APREPRO capability in CUBIT. Journal files are also useful when a new finite element model is being built, by saving a set of initialization commands then iteratively testing different meshing strategies after playing that initialization file.

---

## Journal File Editor

**URL:** https://coreform.com/cubit_help/environment_control/gui/journal_file_editor.htm

**Contents:**
- Journal File Editor
- Journal Editor Toolbar
- Other Functionality Available in the Journal Editor

Figure 1. The Journal File Editor

The Journal File Editor can be used to create a new Python or Cubit command script. By default, a new journal file will be in Cubit command syntax. Enter the commands in the order you want them executed. You can play the commands all at once using the play button on the toolbar. You can also play a few commands at a time. Select the commands you want to play. Then, right click and select the "Play Selected" menu item. If you have a Cubit script, you can convert it to a Python script by hitting the Python toolbar button. If you have a few lines you want to convert to Python, select them, and right click to get the popup menu and choose "Translate Selected to Python"

The Journal File Editor can also be used to edit an existing journal file. Use the File > Open menu item to open the file you want to edit. You still have all the command play options with an existing journal file.

You can import commands entered in the Command Line Workspace. The File > Import menu gives the option to import commands from the history tab. Only the current commands shown in the history tab will be imported. Some of the commands you previously entered might not show up if you have the recommended text trimming turned on. Text trimming improves the application's performance for speed and memory. It will trim off the oldest text in the window when a size limit is reached. To get all the command from your current session, make sure that command journaling is turned on.

The Journal File editor can be used to edit multiple files at the same time. Each document is displayed in its own tab. The tab shows the journal file's syntax and name. If you close the Journal File Editor with unsaved data, it will prompt you to save changes for each of the modified journal files you have open.

The Journal Editor's Toolbar provides quick access to several important functions.

The context ('right-click') menu in the journal editor includes several additional functions, including:

---

## Key Press Commands for the GUI

**URL:** https://coreform.com/cubit_help/environment_control/gui/graphics_window/key_press_commands.htm

**Contents:**
- Key Press Commands for the GUI

Several commands have a key press shortcut. These commands will be executed with respect to the currently selected entities; see the following table:

List information about the current entity to the output window.

Toggle the visibility of the selected entity (make invisible or visible).

Echo entity id to command line.

Select the next entity.

Select the previous entity.

Toggle picking of vertices.

Toggle picking of curves.

Toggle picking of surfaces.

Toggle picking of volumes.

Toggle picking of groups.

Toggle picking of mesh nodes

Toggle picking of mesh edges.

Toggle picking of mesh faces.

Toggle picking of mesh hexes.

Refresh graphics window

Activate/inactivate graphics clipping plane

---

## Listing Information

**URL:** https://coreform.com/cubit_help/environment_control/listing_information/listing_information.htm

**Contents:**
- Listing Information

The List commands print information about the current model and session. There are five general areas: Model Summary, Geometry, Mesh, Special Entities, and CUBIT Environment. The descriptions of these areas includes example output based on the model generated by a journal file listed below. The model consists of a 1x2x3 brick meshed with element size 0.1.

Journal File Used for List Examples

brick x 1 y 2 z 3 body 1 size 0.1 mesh volume 1 block 1 volume 1 nodeset 1 surface 1 sideset 1 surface 2 group "my_surfaces" add surface 1 to 3 surface 2 name "BackSurface" surface 3 name "BottomSurface" surface 1 name "FrontSurface" surface 4 name "LeftSurface" surface 5 name "RightSurface" surface 6 name "TopSurface"

---

## List Cubit Environment

**URL:** https://coreform.com/cubit_help/environment_control/listing_information/list_cubit_environment.htm

**Contents:**
- List Cubit Environment
- Message Output Settings
- Logging Output to a File
- Default Block Creation
- Journaling Settings
- Exodus Export Title
- Listing Current Settings
- Graphical Display Information
- Memory Usage Information

The user may list information about the current CUBIT environment such as message output settings, memory usage, and graphics settings.

There are several major categories of CUBIT messages.

By default, Info, Warning, Error, and Echo messages are printed, and Debug messages are not printed. Information, Error, Warning, Debug, and Echo message printing can be turned on or off (or toggled) with a set command. Debugging output can also be redirected to a file. Current message printing settings can be listed.

List {Echo|Info|Errors|Warning|Debug}

Set {Info|Warning} [On|Off] [logging]

[Set] Debug <index> [On|Off]

[Set] Debug <index> File <'filename'>

[Set] Debug <index> Terminal

Message flags can also be set using command line options:

-information {on|off}

Debug flags can be enabled from the command line with

where <setting> is a comma-separated list of integers or ranges of integers denoting which flags to turn on. E.g., to set debug flags 1, 3, and 8 to 10 on, the syntax is -debug 1,3,8-10.

Output from CUBIT can be redirected to a log file, and the current state of logging can be listed.

[Set] Logging {Off|On File <'filename'> [Resume]}

If logging is enabled, by default any output to the console or command window will also go into the logging file. The resume option will append to the logfile, if it exists, instead of emptying the file. If the logfile doesn't already exist, it will be created.

Output of information and warning messages to the logging file can be controlled independent of console output settings by adding the logging option to the set {info|warning} [on|off] logging command.

Set Default Block {ON|off|Volume|Surface|Curve]}

The set Default Block command will toggle whether or not default blocks are written during the export operation if no other blocks have been specified. The List Default Block command lists the geometric entity types for which blocks will automatically be generated at export.

The List Journal command lists which types of CUBIT commands will be journaled and the file to which the journaled commands are being written.

Title "<title_string>"

The List Title command will list the title to be written to an Exodus file on export. To assign a title to an Exodus file, use the Title command.

The List Settings command lists the value of all the message flags, journal file and echo settings, as well as additional information. The first section lists a short description of each debug flag and its current setting. Other message settings are listed next, followed by some flags affecting algorithm behavior.

List view prints the current graphics view and mode parameters; See Graphics Window .

Users are encouraged to use Unix commands such as `top' to check total CUBIT memory use. Developers may check internal memory usage with the following command:

List Memory [`<object type>']

Without an object type, the command prints memory use for all types of objects.

**Examples:**

Example 1 (swift):
```swift
CUBIT> list settings
Debug Flag Settings (flag number, setting, output to, description):
 1  OFF  terminal           Debug Graphics toggle for some debug options.
 2  OFF  terminal           Whisker weaving information
 3  OFF  terminal           Timing information for 3D Meshing routines.
 4  OFF  terminal           Graphics Debugging (DrawingTool)
 5  OFF  terminal           FastQ debugging
 6  OFF  terminal           Submapping graphics debugging
 7  OFF  terminal           Knife progress whisker weaving information
 8  OFF  terminal           Mapping Face debug / Linear Programming debug
 9  OFF  terminal           Paver Debugging
.
.
.
echo              = On
info              = On
journal           = On
journal graphics  = Off
journal names     = On
journal aprepro   = On
journal file      = 'cubit11.jou'
warning           = On
logging           = Off
recording         = Off
keep invalid mesh = Off
default names     = Off
default block    = Volumes
catch interrupt   = On
name replacement character = '_', suffix character = '@'
Matching Intervals is fast, TRUE;
multiple curves will be fixed per iteration.
Note in rare cases 'slow', FALSE, may produce better meshes.
Match Intervals rounding is FALSE;
intervals will be rounded towards the user-specified intervals.
```

---

## List Model Summary

**URL:** https://coreform.com/cubit_help/environment_control/listing_information/list_model_summary.htm

**Contents:**
- List Model Summary

The following commands print identical summaries of the model: the number of entities of each geometric, mesh, and special type

The following output is generated from the list model command.

Model Entity Totals: Geometric Entities: 0 assemblies 0 parts 2 groups 1 bodies 1 volumes 6 surfaces 12 curves 8 vertices Mesh Entities: 6000 hexes 0 pyramids 0 tets 7876 faces 0 tris 9854 edges 7161 nodes Special Entities: 1 element blocks 1 sidesets 1 nodesets

Journaled Command: list model

---

## List Special Entities

**URL:** https://coreform.com/cubit_help/environment_control/listing_information/list_special_entities.htm

**Contents:**
- List Special Entities

List {special_type} <range>

Special entities include (element) blocks, sidesets and nodesets (representing boundary conditions). Like the list geometry and list mesh commands, if no range is specified then the number of entities of the given type is summarized. Otherwise, listing a special entity prints the mesh and geometry it contains.

(Some special entities are of interest mainly to developers and are not described here, e.g. whisker sheets, and whisker hexes.)

---

## Location, Direction and Axis Specification

**URL:** https://coreform.com/cubit_help/environment_control/location_direction_specification/location_direction_axis.htm

**Contents:**
- Location, Direction and Axis Specification

Many commands require that a location or a direction be specified. Although entering the three floating point numbers required to uniquely define a vector is perfectly acceptable, it may be more convenient to specify the direction or location with respect to existing entities in the model. For example, the following commands might be used for creating straight curves using location and direction specification described here:

Create Curve [From] Location {options} Location {options}

Create Curve [From] Location {options} Direction {options} Length <val>

---

## Machine Learning with the Geometry Power Tool

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/machine_learning.htm

**Contents:**
- Machine Learning with the Geometry Power Tool
- Geometry Analysis Tools
  - Reduce for Simulation
  - Fasteners
    - Procedure for Using the Fasteners Diagnostic Tool
    - Bolt Categorization Methods
  - Beams and Shells
  - Slot Surfaces
  - Tetmesh Poor Quality Predictions
  - Part Classification

This page describes the machine learning tools that are part of Cubit's Geometry Power Tool for tet mesh quality prediction and part classification.

The Geometry Power Tool in Cubit provides a series of diagnostic checks on your model used to defeature or simplify a CAD model prior to meshing. Clicking the Analyze button will perform the selected diagnostic tests and display an expanding tree listing geometric entities that are identified by each test. Once identified, suggested solutions can be easily previewed and executed.

This new capability enhances the Geometry Power Tool using state-of-the-art machine learning (ML) methods to predict meshing outcomes, suggest solutions as well as classify certain common part types.

Enable Machine Learning:

Use the following procedure to access the new ML capabilities:

Figure 1. Navigation to Power Tool and Options panel.

Figure 2. Options panel without ML models loaded

Figure 3. Options panel after loading ML models.

The following describe the additional diagnostics available when ML is enabled in the Geometry Power Tools.

This diagnostic category leverages machine learning to pinpoint geometric entities crucial for targeted physics simulations. It facilitates the examination, visualization, and contextual simplification into proxy geometry or boundary conditions suitable for simulation. This is achieved through the reduce command suite within Cubit. Supported categories include:

The "Fasteners" category builds upon the "bolt" section found in the Part Classification tool, streamlining the management of connections within assemblies. This diagnostic is especially useful given the tedious nature of managing fastener connections and the varying proxy requirements for simulation across different physics.

Below is an illustration of the Geometry Power Tool, showcasing the three categories and sample geometry with highlighted clamped members and associated bolts.

Figure 2. Fasteners diagnostic shows clamped members with their associated bolts.

Geometry simplification is often required when modeling assemblies comprised primarily of thin volumes. Shell finite elements are often used rather than full 3D hex or tet elements. The task for analysts in this case is to reduce the 3D set of thin volumes to a set of connected sheet bodies where a mesh of triangles or quadrilaterals can be applied. This procedure can be managed with the Geometry Power Tool if the Beam and Shell diagnostic is selected. See Beams and Shells with the Geometry Power Tool for details.

The Slot Surfaces diagnostic is a new addition to the geometry power tool for preparing slot surfaces in Electromagnetic (EM) modeling. A slot surface is used to identify potential pathways where EM radiation can potentially exit. This diagnostic will help manage slot surfaces and prepare them for the application of boundary conditions and analysis. This diagnostic utilizes Machine Learning (ML) to predict the most likely slot surfaces. See Slot Surface Preparation with the Geometry Power Tool for details.

The solid model used as the basis for a tetrahedral mesh may contain small features or angles that can lead to poor mesh quality or very small elements. This diagnostic will provide a list of entities (vertices, curves, surfaces) that are predicted to result in poor quality tet elements sorted by their predicted mesh quality metric. This allows the user to quickly focus on regions of the model that will result in the worst mesh quality and apply geometry operations to improve the meshing outcome without having to mesh.

Three different mesh quality metrics are used for the basis of the predictions: Scaled Jacobian, In-radius and Deviation. Entities identified by these diagnostics will be sorted according to their ML-predicted metric starting with the worst quality entity. The three edit fields at the top of the Options panel control the quality limit. For example, a Scaled Jacobian Limit of 0.2 will identify all geometry entities predicted to have nearby tet elements whose Scaled Jacobian is less than 0.2. For our purposes, "nearby tets" are defined as those within two edge lengths of the geometric entity.

Context Menus: To display all entities in a specific category, select the diagnostic category title and use the right click context menu to choose Draw. Expanding the list will display individual entities that can be visualized using standard draw tools such as Zoom To, Fly In, Draw Owning Volume, Draw with Neighbors, etc. When one or more entities are selected in the list, a context menu also provides access to selected command panel options. When multiple entities are selected, the context menu can be used to invoke command panels to operate on multiple entities simultaneously.

This diagnostic provides the ability to classify volumes according to several common part types. When selected, characteristic geometric features of each volume will be computed and ML methods will be used to determine the part classification. Each volume will be placed into a list based on its most probable categorization. Volumes in each classification will be ordered based upon a Confidence metric. A confidence of 1.0 indicates a 100% confidence of categorization. Confidence values closer to 0.5 are less likely to be categrized correctly, but ML indicated a higher probablility than other part types. The current part categories are illustrated below showing a few examples from each category. In addition to these Cubit's classify command can manage custom creation and editing of part categories.

Note that the Other Parts category simply includes parts that cannot be categorized with sufficient confidence in any of the other categories.

Context Menus: To display all volumes in a specific category, select the part category title and use the right click context menu and choose Draw. Expanding the list will display individual volumes that can be visualized using standard draw tools such as Zoom To, Fly In, Draw Overlapping Volumes, Draw Nearby Volumes, etc. The context menu also provides access to command panel options such as Delete or Reduce. When multiple volumes are selected, the context menu can be used to invoke command panels to operate on multiple volumes simultaneously.

To view the volume features or the confidence values computed by ML, use the right click context menu when a part/volume is selected and choose either List ML Features or List ML Predictions menu option.

This diagnostic provides the ability to classify surfaces. Surface categories provided with Cubit are currently limited to two categories: slots and non_slots. The limited categories are intended to be exemplars for additional user customized categires that can be defined using Cubit classify command. Similar to part classification, when selected, characteristic geometric features of each surface will be computed and ML methods will be used to determine its categorization. Each surface will be placed into a list based on its most probable categorization. Surfaces in each classification will be ordered based upon a Confidence metric. A confidence of 1.0 indicates a 100% confidence of categorization. Confidence values closer to 0.5 are less likely to be categrized correctly, but ML indicated a higher probablility than other part types.

Once entities have been identified, custom solutions may be displayed by checking the Show Solutions check box above the list of entities. When checked, the Solution window will appear as shown in Figure 4. When an entity is selected in the upper window, an ordered list of solutions will appear in the Solution window. Each solution has an associated metric prediction so that the solution predicted by ML to provide the best possible meshing result will appear at the top of the list.

Figure 4. Geometry Power Tool showing Scaled Jacobian quality predictions as well as an ordered list of possible solutions.

For example, in Figure 4. Surface 1786 is selected which has a predicted minimum Scaled Jacobian metric at the surface of 0.0164. In most cases this metric would be unacceptable for analysis. To correct for this, the first solution in the list is a Replace Surface command that is predicted to result in a Scaled Jacobian of 0.2623. Selecting the solution will display a preview of the operation and double clicking will execute the solution. Other solutions may also be previewed and considered, however those with lower predictions would most likely be avoided.

Context Menus: A context menu is available when selecting a solution. This also provides an option for execution of the solution as well as additional visualization options. It also provides direct access to the appropriate command panel if further customization of the command is desired.

Controlling Solution Predictions: When selecting an entity from one of the metric categories (Scaled Jacobian, In-Radius, Deviation), the predicted value and ordering of the solutions will be based on the corresponding category. Note that solutions may also be generated for other diagnostics (ie. small curves, close loops, blend surfaces, etc.). When ML has been enabled, solutions will also be ordered these categories based upon the predicted tetmesh outcome. The metric used for ordering solutions can be customized using the Options panel shown in Figure 3. Use the Show Solution Predictions check box to toggle the use of ML-predictions to order solutions. When solution predictions are enabled, a drop-down selector will allow selection of one of the three metrics to prioritize solutions.

When selecting a volume from a classification category, selected solutions will also be displayed. Custom solutions based upon a specific part type are still in development and will expand in future versions of the geometry power tool. In particular, the reduce family of commands are available when one or more volumes classified as a "bolt" or "spring" are selected.

---

## Miscellaneous Graphics Options

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/miscellaneous_graphics.htm

**Contents:**
- Miscellaneous Graphics Options
- Silhouette Lines
- Line Width
- Highlight Line Width
- Text Size
- Point Size
- Graphics Status
- Graphics Scale
- Model Axis
- Corner Axis (Triad)

In addition to the commands discussed above, there are several other graphics system options in Cubit that can be controlled by the user.

Some shapes, such as cylinders, are drawn with silhouette lines; these lines don't represent true geometric curves, but help visualize the shape of a surface. Silhouette lines can be turned on or off with the command

Graphics Silhouette [On|Off]

The pattern used to draw silhouette lines can be set using the command

Graphics Silhouette Pattern [Solid | Dashdot | Dashed | Dotted | Dash_2dot | Dash_3dot | Long_dash | Phantom]

This option controls the width of the lines used in the wireframe, shaded, transparent, hiddenline and truehiddenline displays. The default is 1 pixel wide. The command to set the line width is

Graphics LineWidth <width_in_pixels>

This option controls the width of the lines used when highlighting an entity. Setting this to a width greater than the global line width often makes it easier to locate highlighted entities. If this setting has not been changed, the line width set in the command above is used. After using this command, it is necessary to refresh the graphics by either typing "display" or clicking the Refresh Graphics button. The command to set the highlighting line width is

Highlight LineWidth <width_in_pixels>

This option controls the size of text drawn in the graphics window. The size given in this command is the desired size relative to the default size. After using this command, it is necessary to refresh the graphics by either typing "display" or clicking the Refresh Graphics button. The command to set the text size is

Graphics Text Size <size>

This option controls the size of points drawn in the graphics window, such as vertices or heads of vectors; alternatively, the size of points representing nodes or vertices can be set independently of the global point size. The commands to set the point sizes are

Graphics Point Size <size>

Graphics [Node|Vertex] Point Size <size>

All graphics commands can be disabled or re-enabled with the command

While graphics are off, changes in the model will not appear in the graphics window, and all graphics commands will be ignored. When graphics are again turned on, the scene will be updated to reflect the current state of the model.

A graphical scale can be drawn in the graphics window within the viewing area to obtain a bearing on model or part sizes. The command to turn the graphical scale on and off is:

Graphics Scale [On|Off]

The model axis may be drawn in the scene at the model origin. The axis is controlled with the command

Graphics Axis [Type <AXIS | Origin>] [On|Off]

The command is used to specify whether the model axis is visible, and to determine how the axis is drawn. If you include Type Axis , the axis will be drawn as three orthogonal lines; if you include Type Origin, the axis will be drawn as a circle at the model origin.

By default, an axis appears in the corner of the graphics window. This corner axis, also called the triad, can be disabled or re-enabled with the command

Graphics Triad [On | Off]

Many of the graphic options can be reset back to default values with the command:

The graphic options set to defaults are:

In addition, this command also:

The shrink graphics attribute allows you to view the elements shrunken about their centroid. This is useful for viewing 3D meshes, permitting viewing of interior elements. It may also be useful for visually inspecting the mesh for missing elements. To use the shrink option use:

graphics shrink <value> draw hex <range> draw tet <range> etc...

where value is a number between 0 and 1. One (1) will shrink the elements to a point, while zero (0) will not shrink the elements. The following figures illustrate the effect of element shrink on a hex mesh.

Figure 1. Top: shrink=0.2, Bottom: shrink=0.5

The graphics tolerance commands change the way that facets are drawn in the graphics window. It does not affect the underlying geometry, just the graphics display. It can be useful to change the facet tolerance on large models if the refresh speed is slow.

Graphics Tolerance [ [ANGLE|Distance] <val>|Default ]

Specifying an angle will change the maximum allowable angle between neighboring facets. The distance option will set a maximum distance between adjacent facets. Increasing either of these numbers will result in coarser facets. The default option will return values to their default settings.

The GUI Options panel for manipulating these settings is found under Tools/Options and is shown below:

---

## Model Tree

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/geometry_tree.htm

**Contents:**
- Model Tree
- Drag and Drop
- Picked Group
- Right-Click Menu Functions

The tree works directly with the graphics window and picking. Selecting an entity in the tree will select the same entity in the graphics window. Selecting an entity in the graphics window will highlight the tree entry if that entry is currently visible. If an entity's visibility is turned off, the icon next to that entity in the geometry tree will disappear.

If the tree entry is not visible the user may press the Find button located at the bottom of the tree. The first occurrence of the selected entity will be shown on the tree.

Virtual entities have a small (v) after the name to indicate that they are virtual entities.

Figure 1. Geometry Tree Window

The Tree View window supports drag and drop of geometric entities into existing boundary condition sets. To create boundary conditions, see the Materials and Properties menu on the main control panel, or right-click on one of the boundary condition labels and select the "Create New" option from the context menu. Geometric entities or groups can be added to blocks, nodesets, or sidesets by dragging and dropping inside the tree view window.

The current selections in the graphics window can be added to a "picked group" by selecting the "Add to Picked Group" from the Right click menu. Selections can also be added to the picked group by dragging and dropping onto the group from the geometry tree window. The picked group can be substituted into any commands that use groups. To remove an item from the picked group, use the "Remove from Group" option in the right click menu in the geometry tree or from the graphics window.

Figure 2. Picked Group

The geometry tree's context menu is sensitive to the type of item and the number of items selected. Functions that apply to the item type and number of selected items are available from the context menu. These include the following:

---

## Mouse Based View Navigation: Zoom, Pan and Rotate

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/mouse_based_zoom_pan_rotate.htm

**Contents:**
- Mouse Based View Navigation: Zoom, Pan and Rotate
- Changing the View Transformation Button Bindings
- Saving and Restoring Views

The mouse can be used to navigate through the scene using various view transformations. These transformations are accomplished by clicking a mouse button in the graphics window and dragging, sometimes while holding a modifier key such as Shift or Control. When run with graphics on, CUBIT is always in mouse mode; that is, mouse-based transformations are always available, without needing to enter a CUBIT command.

Mouse-based view transformations are accomplished by placing the pointer in the graphics window and then either holding down a mouse button and dragging, or by clicking on a location in the graphics window. Some functions also require one or more modifier keys to be held down; the modifier keys used in CUBIT are Shift and Control . Each of the available view transformations has a default binding to a mouse button-modifier key combination. This binding can be changed by the user if desired. Transformations and button mappings are summarized in the following table.

Note: These settings are applicable only to the UNIX command line version of CUBIT. For a description of the Graphical User Interface Mouse Operations see GUI View Navigation.

The bindings are based on the following mouse button definitions:

Figure 1. Default Mouse Function Mappings for the Command Line

Table 1. Mouse Function Bindings for Zoom, Pan, and Rotate

The default mapping of functions to mouse buttons, described in the Default Mouse Function Mappings table above, can be modified. There are two ways to assign a function to a button/modifier combination.

First, you can use the command

Mouse Function <function_id> Button <1|2|3> [Shift][Control]

Type Help Mouse Function to see a list of function IDs that may be used in this command.

Second, you can assign functions interactively. To do so, first put the pointer into a graphics window and then hit the F key. On-screen instructions will lead you through the rest of the process.

The GUI Options panel for managing the mouse bindings can be found at Tools/Options/Mouse, and is as follows:

After performing view transformations, it may be useful to return to a previous view. A view is restored by setting the graphics camera attributes to a given set of values. The following keys, pressed while the pointer is in the graphics window, provide this capability:

V - Restores the view as it was the last time Display was entered.

F1 to F12 - These function keys represent 12 saved views. To save a view, hold down the Control key while pressing the function key. To restore that view later, press the same function key without the Control key.

Note: In the Graphical User Interface version the F1, F2 and F3 keys are used as an alternate form of dynamic viewing, therefore the ability to save views is not currently supported in the GUI.

You can also save a view by entering the command

View Save [Position <1-12>] [Window <window_id>]

The current view parameters will be stored in the specified position. If no position is specified, the view can be restored by pressing V in the graphics window. If a position is specified, the view can be restored with the command

View Restore Position <1-12> [Window <window_id>]

These commands are useful in as entries in a .cubit startup file. For example, to always have F1 refer to a front view of the model, the following commands could be entered into a .cubit file:

Graphics Autocenter On

The first three commands set the orientation of the camera. The fourth command ensures that the model will be centered each time the view is restored. The final command saves the view parameters in position 1. The view can be restored by pressing F1 while the cursor is in a graphics window.

Additionally, you can change the 'gain' on the mouse movements by changing the mouse gain setting, via the command:

where a value of 3 would be 3X as sensitive to mouse movements, and a value of 0.5 would be half as sensitive.

Set ReverseZoom {on|off}

Another user preference, the direction of 'zooming' obtained by using the mouse can be 'flipped', by toggling the reversezoom setting.

---

## Options Panel

**URL:** https://coreform.com/cubit_help/environment_control/gui/drop_down_menus/options_menu.htm

**Contents:**
- Options Panel
- Command Panels
- Display Preferences
- General Preferences
- Geometry Defaults
- History Preferences
- Label Defaults
- Layout Preferences
  - Cubit Layout Settings
- Mesh Defaults

To change program preferences in the Graphical User Interface select: Tools > Options. On a Mac OS, the equivalent panel is called Preferences, and is available from Cubit > Preferences The options panel includes a series of Tabs, containing categories of global settings to customize the Cubit environment. The following categories are available:

This menu controls how command panels are displayed and managed, including which style of button hierarchy is displayed.

This menu controls entity display features for the graphics window which include the following:

This menu controls general program options including the following:

This menu controls the geometry defaults.

The user can also change the default geometry engine to one of the following:

The faceting tolerance can also be controlled from this menu to change the way facets are drawn in the graphics window.

This menu controls the input window history and journal file options. These include:

This menu controls the geometry and mesh entity labels in the graphics window.

This menu option controls input window formatting and control panel docking options.

Also included in the layout preferences is a list of available windows with a checkbox to show/hide each window.

This menu controls the layout of Cubit specific buttons and tabs on the GUI.

This menu controls mouse button controls. Pressing the Emulate Command Line Settings button will cause all of the settings to simulate mouse controls in the command line version of CUBIT. For a detailed description of mouse settings see the View Navigation-GUI page.

Post Processor Executable Directory - Option to browse for post processor executable directory.

This menu controls quality defaults for different quality metrics. For a description of the different quality metrics see the respective pages:

---

## Part Classification with Machine Learning

**URL:** https://coreform.com/cubit_help/environment_control/entity_selection_and_filtering/ml_part_classification.htm

**Contents:**
- Part Classification with Machine Learning
  - Syntax:
  - Predefined Fixed Part Classification Categories
- Discussion
  - Predicting Part and Surface Classification
  - Categorizing Entities into New Categories
  - Training
  - Listing Categories
  - Resetting Categories
  - User Training Data

Predicting Part Classification Categorizing Parts into New Categories Training Listing Categories Resetting Categories User Training Data Reclassification Volume Selection by Category

In a complex assembly containing tens or hundreds of volumes and surfaces, it is sometimes useful to classify or identify entities according to a predefined category. Cubit uses machine learning methods to categorize volumes or surfaces into one of a predefined set of categories. Custom categories, defined by the user, can also be set up used for classification. The classify command is primarily used to identify and control part classification using the Cubit command line. In addition, the machine learning tools encapsulated in the geometry power tool in Cubit's graphical user interface provides an extensive set of tools for classifying and applying geometric solutions.

classify {volume|surface <ids>} [confidence] [features [importance]]

classify {volume|surface <ids>} "<string>" [export_acis]

classify reset ["<string>"]

classify user path ["<string>"]

classify aggregate [model "<string>" category "<string>"]

reclassify {volume <ids>} "<string>"

Cubit currently provides the following set of predefined categories for classification:

Part and Surface classification uses machine learning methods to identify entities based on characteristic geometric features of the volume or surface. These methods utilize a fixed set of training data which has been provided with your Cubit installation. This training data may be augmented by the user to refine the existing categories or add new categories. When using any of the above classify commands for the first time, a short pause may occur while the fixed training data from the Cubit installation and the user training data are loaded into the program.

The command classify {volume|surface <ids>} is used to identify a volume or surface based upon the set of categories from both fixed and user training data. When executed, various geometric features of the specified entity(s) are computed and a prediction made as to the most likely categorization based upon the existing training data. Depending upon the number of entities to classify and the complexity of the surfaces or volumes, this command may take a few seconds to complete. The result will be a string printed to the output window of the predicted category, such as:

Volume 1 (Solid) is "spring"

The optional confidence argument may be used to list the confidence values for each of the existing categories for both fixed and user defined. The confidence is a numerical value from 0 to 1 computed by the machine learning method indicating the confidence level of the classification for each category. The highest numerical value of confidence is selected as the predicted category.

The features and importance arguments are primarily used for diagnostics to examine the resulting geometric features and their relative significance to the prediction. The features are a list of about 50 scalar values that are computed for each surface or volume that are used in the machine learning methods and the importance is the relative weight given to each feature when making the prediction.

If the existing set of fixed categories is insufficient, users can create new categories to augment the fixed categories. In addition, if a predicted category for a given surface or volume is incorrect or insufficient, training data for the fixed categories may also be added. To add training data to a category, use the classify {volume|surface <ids>} "<string>" command, where <string> is either an existing category name or a new category. Use quotation marks to distinguish the category name. For example:

classify volume 1 "spring"

When executed, the features of the given surface or volume will be computed and written to disk as a new set of training data. User training data defined in this way is written to an application directory which is persistent so it can be used in subsequent runs of Cubit.

In most cases the more examples of a category that can be provided, the more accurate will be subsequent predictions. For example, if a single volume of new category "widget" is added, all volumes that are identical to the initial example will most likely be predicted as "widget", however small variations of the volume may not. For this reason, providing as many varying examples of a "widget" as possible is advantageous when setting up a new category. Providing identical examples of the same volume to the classify command is also not detrimental, as duplicates are automatically identified and filtered out. Note that when categorizing a new surface or volume, the output window will indicate whether new training data was added or whether the volume represents duplicate data.

The export_acis option can be used to automatically write an acis .sat file of the specified volume(s). If used, the file(s) will be written to the user training directory titled with the name of the category. Each acis file will contain a single volume and named using the category name and a unique incremented integer ID. While primarily used for debugging, they can also be used as a visual representation of the current user categories. (Not currently supported for surfaces)

Whenever new training data is added, the classification models must be retrained. Although retraining happens automatically any time training data is added or deleted when ussing Cubit commands, the train command is useful for forcing a retrain should additional training data be added manually to the training directories on disk. In addition to rerunning the training process, it will print to the output window the number of supporting volumes used for each category when computing classification predictions.

All existing classification categories may be printed to the output window using the classify list command. For user defined categories or fixed categories that have been augmented, a (U) will follow the name of the category.

In addition to the category names, the classify list command will also print the path to both the fixed training data and the user training data on disk.

To remove an existing user defined category use the command classify reset ["<string>"] where <string> is a a category name in quotations. This will remove all user training data for the given category from disk and retrain the classification models without the category. If a fixed category is specified, the user-defined training data defined in the category will be removed, keeping only the fixed data. If this command is used without a category, all user training data will be removed.

When a new category is created or a fixed category is added to, the resulting training data is written to a default application directory that is specific to a platform. For example, for Mac and Linux OS the directory will be located at:

/Users/<user_name>/Library/Application Support/Cubit/ml

To display both the current user training data directory and the fixed training data directory, use the classify list command. While the fixed training data directory canot be changed, it may be worthwhile to change the user training directory. To change the user training directory, use the command classify user path "<path string>" where <path string> is the full path to a writable directory on disk in quotes. Changing the user training directory may be useful to temporarily use training data from another source or to ignore all user training data without removing it.

Using the command, classify user path without a path specification will set the user training data directory back to its default for the platform.

To add (aggregate) user-defined classification training data to Cubit's existing data, use the Classify Aggregate command. If a specific model and category are not specified, all user-defined data will be aggregated.

At times, it may be necessary to remove a surface or volume from its current category classification, or move the surface or volume from one category to another. Use the reclassify {volume|surface <ids>} "<string>" command to update the training data for one or more volumes where <string> is the name of a category. If the training data for the given volume is currently present in another category, it will be removed from its current category and added to the new specified category. If no category is specified, it will be removed from its current category without adding it to another category. Training data from the fixed training data cannot be removed or modified.

It may be useful to identify all surfaces or volumes based on their predicted classification category. To do so, use the syntax with category "<string>" in conjunction with other Cubit commands that accept IDs. A few example uses this syntax might include:

group "mysprings" add volume with category "spring"

draw volume with category "bolt"

delete volume with category "insert"

In the first example, a group named mysprings is created and all volumes with the predicted category of spring added to it. The second example would draw all volumes that are classified as bolt, and the third example would delete all volumes that are classified as insert.

Note that in order to identify surfaces or volumes based on their predicted category, features for all surfaces or volumes in the model will be computed. For assemblies with hundreds or thousands of parts, this may be time consuming. Also note that a similar capability is available in the geometry power tool machine learning tools which will list the predicted category for each volume in the model in separate drop-down lists and build cubit groups from each category if requested.

---

## Power Tools

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/tree_view.htm

**Contents:**
- Power Tools

The power tools contain useful tools to help users through the mesh generation process. The Immersive Topology Environment for Meshing, also known as ITEM. This panel contains a wizard-like environment which guides the user through the mesh generation process through a series of panels and diagnostics. The geometry repair and analysis tools contains diagnostics and tools for analyzing and repairing geometry, although many of these can now be found in the ITEM environment as well. The mesh quality and meshing power tools aid in mesh generation and verification. The geometry and mesh comparison tool identifies correlation between existing geometry and mesh. The defeaturing tool assists users with defeaturing geometry in a more automated fashion. The assemblies tool help users manage assemblies, parts and related metadata.

Figure 1. Power Tools Window

To familiarize yourself with the power tools environment (excluding ITEM), we recommend that you try the power tools tutorial.

To familiarize yourself with ITEM wizard, we recommend that you try the ITEM tutorial.

---

## Property Editor

**URL:** https://coreform.com/cubit_help/environment_control/gui/property_editor.htm

**Contents:**
- Property Editor
- Editing Entity Attributes from the Property Editor
  - General Attributes
  - Geometry Attributes
  - Meshing Attributes
  - Boundary Condition Attributes

The Property Editor is a window that lists properties about the current entity selection. Some of the properties, like CUBIT ID, entity type, or geometry engine, are listed for reference only. Other attributes, like name, or mesh intervals, color, mesh scheme, or smooth scheme can be edited from the window. The Property Editor is located on the left panel in the GUI. The highlighted entity/entities in the graphics window are listed in the property editor window. The Property Editor also lists information about selected mesh entities, boundary conditions, and assemblies. Selecting an object from the Tree View will also open the object in the property editor.

Figure 1. Property Editor Window

The row of buttons on the top of the editor are shortcuts to common commands. These include:

The Property Editor provides a convenient way to change attributes on entities. . Some of the fields cannot be changed, some can be edited from an input field, and others are edited by selecting from a list, or by opening the corresponding window from the Control Panel.

If multiple entities are selected, the attributes that are similar to both entities will be shown. Changing an attribute from the property editor will change that attribute on both entities. If multiple entities are selected the total volume, surface area, and length of all entities will be shown.

Below is a summary of properties listed for each attribute type.

---

## Right Click Commands for the GUI Graphics Window

**URL:** https://coreform.com/cubit_help/environment_control/gui/graphics_window/right_click_commands.htm

**Contents:**
- Right Click Commands for the GUI Graphics Window
  - With Entity Selected
    - Entity Selections
    - Entity Visualization
    - Entity Operations
  - Without Entity Selected

Clicking the Right mouse button in the graphics window will bring up a menu. One of two menus will appear, depending on whether an entity is currently selected.

When an entity is selected, the options available will depend upon the type of entity selected. The following describes the menu options and when they are available.

---

## Saving and Restoring a Cubit Session

**URL:** https://coreform.com/cubit_help/environment_control/session_control/saving_and_restoring.htm

**Contents:**
- Saving and Restoring a Cubit Session
- CUBIT File Method
  - New
  - Open '<filename>'
  - Save
  - Import
  - Export

There are currently two ways to save or restore a model in CUBIT. A file can be saved with either the Exodus or CUBIT File method. The method of choice is determined by a set command. The CUBIT method is the default.

Set Save [exodus|CUBIT] [Backups <number>]

The CUBIT file is a binary cross-platform-compatible file for the storage of a Cubit model that is compact in size and efficient to access. It includes both the geometry and the associated mesh, groups, blocks, sidesets, and nodesets. Mesh and geometry are restored from the Cubit file in exactly the same state as when saved. For example, element faces and edges are persistent, as well as mesh and geometry ids. The Graphical User Interface version of CUBIT also provides a toolbar with direct access to file operations using the CUBIT File method described here.

By default, the CUBIT file is written in an HDF5-based format that uses either the .cub or the .cub5 extension. The older binary format is supported for read-only backward compatibility. CUBIT detects the format automatically when a file is opened or imported, so both HDF5 and legacy binary .cub files can be read without setting any additional options.

Creates a new blank model with default name, closing the current model. The New command essentially acts like the reset command.

Opens an existing Cubit file (*.cub5 or legacy *.cub), closing the current model.

A default file name is assigned when CUBIT is started (in very much the same way the journal files are assigned on startup) in the form cubit01.cub with incrementing digits on subsequent sessions. The current model filename is displayed on the title bar of the CUBIT window. Typing save at any time during your session will save the current model to the assigned Cubit file. The Cubit file includes the geometry and the mesh. Groups, blocks, sidesets and nodesets are also saved within it. To change the name of the current model, or to save the model's current geometry to a different file, use the save as command. Note that 'save cub5 <filename>' is a valid command that is retained for backward compatibility.

save as 'filename' [Journal] [Overwrite]

The optional Journal keyword stores the session's current journal stream inside the saved file.

The set file overwrite command can be toggled on and off to allow overwriting when using the save as command. The command defaults to prohibiting overwrites.

set file overwrite [On|OFF]

Issuing the save command with no arguments as follows:

will create a backup file of the current session using the name of the last saved file. The backup files are appended with .1, .2, etc. The user can set the total number of backups created per model with the following command (the default number of backups is 99,999):

set save backups [CUBIT][exodus] <number>

As soon as the number of model backups reaches the maximum, the lowest numbered backup file will be removed upon subsequent backup creation.

To check on the status of a 'set' command, type in the command in question without any options. For example, to check which save method is currently toggled, type:

Imports and appends a Cubit file (*.cub5 or legacy *.cub) to an existing model.

import cubit 'filename.cub' [merge_globally]

In addition to saving an entire model, one can use the export command to save only a portion of a model. The geometry and associated mesh, groups, blocks, sidesets and nodesets are exported. Only bodies or free surfaces, free curves, or free vertices can be exported to a Cubit file.

export cubit 'filename.cub' entity-list

---

## Saving Graphics Views

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/saving_graphics_views.htm

**Contents:**
- Saving Graphics Views

The current graphics view can be saved and restored using the following commands:

View Save Position <n>

View Restore Position <n>

When you save a view, you save the camera settings in effect at the time the command is issued. When you restore the view, the camera is returned to the saved position, orientation, and field of view.

If autocenter is on at the time you save the view, then restoring the view will automatically adjust the camera settings to center on the entire model and fit the entire model on the screen, a lot like "zoom reset." You turn autocenter on by typing "graphics autocenter on."

Example of how to save a top view:

graphics autocenter on

Use this command to restore that view:

view restore position 3

The view will then be looking down the y-axis, with the x-axis to the top and the z-axis to the right. The model will be centered in the view and zoomed so that everything just fits into the graphics window. This is true even if the model is not centered on the origin.

If autocenter is off when the "view save" command is issued, the camera is not adjusted to fit the scene into the graphics window. Instead, it is placed exactly where it was at the time the "save" command was issued.

Note that many graphics commands, such as "at", "from", and "up", do not change what appears in the graphics window until a "display" command is issued. They do, however, take immediate effect internally, and they do affect what is saved by the "view save" command.

In the command line version of CUBIT, you can save a view by holding down the shift key and pressing one of the function keys (F1-F12). Each function key corresponds to a different saved view. A total of 12 views can be saved. A view can be restored at a later time by pressing the appropriate function key WITHOUT holding down the shift key.

It may be useful to save views in your cubit file so that they are available every time you run CUBIT. Use CUBIT to save front, top, and side views in positions 1, 2, and 3. If views are saved in your cubit file, it is convenient to add a "view reset" command after the views have been saved. Then the graphics will initially appear as they would if the view commands had not been included in your cubit file.

---

## Selecting Entities in the GUI

**URL:** https://coreform.com/cubit_help/environment_control/gui/graphics_window/selecting_entities.htm

**Contents:**
- Selecting Entities in the GUI
- Pre-Selection
- Polygon, Circle and Box Select

Geometry, mesh entities, and boundary conditions can be selected with the left mouse button directly in the graphics window. Before selecting any entity, however, the correct selection mode must be chosen. This dictates which entity types will be available for selection in the graphics window. The Select Toolbars, which are located above the graphics window by default, are used to change the entity selection modes.

Figure 1. The Selection Toolbars for Geometry and Mesh Entities

Figure 2. The Selection Toolbar for Boundary Conditions

Figures 1 and 2 shows the selection toolbars. Selecting one of the entity selection modes will only permit selection of that particular entity type within the graphics window. These selections will not override a Pick Widget in the command panel.

If both volume and surface entities are picked on the select toolbar, a single click will select the surface while a double click will select the volume. More detailed information on selecting and specifying entities can be found in Entity Selection and Filtering .

When the mouse cursor is over an entity type that has been selected from the Pick toolbar, that entity will become highlighted. This is called pre-selection and is used as a graphical guide to show which entity will be picked when the mouse button is clicked.

Graphics pre-selection may slow down your graphics speed for large models. You can disable pre-selection from the Tools->Options dialog box.

The polygon/circle/box selection feature allows you to select entities by drawing a box, circle or polygon on the screen. To create a box or circle selection, press and hold the <CTRL> button* while clicking and dragging the left mouse button. Release the left mouse to complete the box or circle select. To create a polygon selection, press and hold the <CTRL>* button while clicking and dragging the left mouse button. Click the left mouse button to create another side for the polygon. Press either of the other buttons to close the polygon and complete the selection. Only entities that are in active selection mode will be selected. To change between the polygon, circle or box method, press the Toggle Between Polygon/Box/Circle Select button on the Select Toolbar. Clicking the Toggle Selected Enclosed/Extended button will toggle between Enclosed Selection and Extended Selection. Enclosed selection will only select entities that are fully enclosed within the bounding box, circle or polygon. Extended selection will select entities that are either fully OR partially enclosed within the bounding box. Toggling the the Select X-Ray will select entities that are hidden behind other entities. X-ray selection will only apply to smoothshade and hiddenline graphics modes.

*Note: For Mac computers use the command (or apple) button for polygon or box select.

---

## Selecting Entities with the Mouse

**URL:** https://coreform.com/cubit_help/environment_control/entity_selection_and_filtering/selecting_with_mouse.htm

**Contents:**
- Selecting Entities with the Mouse
- Entity Selection
- Query Selection
- Multiple Selected Entities
- Information About the Selection
- Picked Group
- Substituting Selection into Other Commands
- Select Commands

The following discussion is applicable only to the command line version of CUBIT. See GUI Entity Selection for a description of interactive entity selection with the Graphical User Interface. Also refer to Extended Selection Dialog to learn how to use Python scripts to create extensive selection capabilities.

Many of the commands in CUBIT require the specification of an entity on which the command operates. These entities are usually specified using an object type and ID (see Entity Specification) or a name. The ID of a particular entity can be found by turning labels on in the graphics and redisplaying; however, this can be cumbersome for complicated models. CUBIT provides the capability to select with the mouse individual geometry or mesh entities. After being selected, the ID of the entity is reported and the entity is highlighted in the scene. After selecting the entities, other actions can be performed on the selection. The various options for selecting entities in CUBIT are described below, and are summarized in Table 1:

Table 1. Picking and key press operations on the picked entities

Details of selecting entities with a mouse are outlined in the following items:

Selecting entities typically involves two steps:

1. Specifying the type of entity to select

Clicking on the scene can be interpreted in more than one way. For example, clicking on a curve could be intended to select the curve or a mesh edge owned by that curve. The type of entity the user intends to select is called the picking type. In order for CUBIT to correctly interpret mouse clicks, the picking type must be indicated. This can be done in one of two ways. The easiest way to change the picking type is to place the pointer in the graphics window and enter the dimension of the desired picking type and an optional modifier key. The dimension usually corresponds to the dimension of the objects being picked:

Table 2. Picking Modes in Graphics Window

If a Shift modifier key is held while typing the dimension, the picking type is set to the mesh entity of corresponding dimension, otherwise the geometry entity of that dimension is set as the picking type. For example, typing 2 while the pointer is in the graphics window sets the picking type so that geometric surfaces are picked; typing Shift-1 sets the picking type so that mesh edges are picked. To differentiate between picking "tris" or "quads" use "pick face" or "pick tri"

The picking type can also be set using the command

where entity_type is one of the following: Body , Volume , Surface , Curve , Vertex , Hex , Tet , Face , Tri , Edge , Node , or DicerSheet .

2. Selecting the entities

To select an object, click on the entity (this command can be mapped to a different button and modifiers, as described in the section on Mouse-Based View Navigation). Clicking on an entity in this manner will first de-select any previously selected entities, and will then select the entity of the correct type closest to the point clicked. The new selection will be highlighted and its name will be printed in the command window.

If the highlighted entity is not the object you intended to selected, press the Tab key to move to the next closest entity. You can continue to press tab to loop through all possible selections that are reasonably close to the point where you clicked. Shift-Tab will loop backwards through the same entities.

To select an additional entity, without first clearing the current selection, hold down the control key while clicking on an object. You can select as many objects as you would like. By changing the picking type between selections, more than one type of entity may be selected at a time. When picking multiple entities, each pick action acts as a toggle; if the entity is already picked, it is "unpicked", or taken out of the picked entities list.

To select entities using rubberband, hold the control key, click and drag to enclose the entities to select. Different rubberband shapes are available to use: box, circle and polygon. A toolbar button is provided to toggle between the different shapes.

When an entity is selected, its name, entity type, and ID are printed in the command window. There are several other actions which can then be performed on the picked entity list. These actions are initiated by pressing a key while the pointer is in the graphics window. Table 1 summarizes the actions which operate on the selected entities.

There is a special group whose contents can be altered using picking. This group is named picked , and is automatically created by CUBIT. Other than its relationship to interactive picking, it is identical to other groups and can be operated on from the command line. Like other groups, both geometric and mesh entities can be held in the picked group. Table 1 lists the graphics window key presses used with the picked group.

Note: It is important to distinguish between the current selection and the picked group contents. Clicking on a new entity will select that entity, but will not add it to the picked group. De-selecting an entity will not remove an entity from the picked group.

There are three ways to use mouse-based selection to specify entities in commands.

1. The Selection Keyword

You may refer to all currently selected entities by using the word selection in a command; the picked type and ID numbers of all selected entities will be substituted directly for selection . For example, if Volume 1 and Curve 5 are currently selected, typing

is identical to typing

Color Volume 1 Curve 5 Blue

Note that the selection keyword is case sensitive, and must be entered as all lowercase letters.

2. Echoing the ID of the Selection

Typing an e into a graphics window will cause the ID of each selected entity to be added to the command line at the current insertion point. This is a convenient way to use entities of which you don't already know the name or ID.

As an added convenience, the picking type can be set based on the last word on the command line using the ` key. Note that this is not the apostrophe key, but rather the left tick mark, usually found at the upper-left corner of the keyboard on the same key as the tilde (~). For example, a convenient way to set the meshing scheme of a cylinder to sweep would be as follows:

Volume (hit `, select cylinder, hit e) Scheme Sweep Source Surface (hit `, select endcap, hit e) Target (select other endcap, hit e)

The result will be something similar to

Volume 1 Scheme Sweep Source Surface 1 Target 2

Notice that you must use the word Surface in the command, or ` will not select the correct picking type.

3. Using the Picked Group in Commands

Like other groups, the picked group may be used in commands by referring to it by name. The name of the picked group is picked. For example, if the contents of the picked group are Volume 1 and Volume 2, the command

Draw Volume 1 Volume 2

Note that picked is case sensitive, and must be entered as all lowercase letters.

Creating and Modifying Selections

The following commands may be used to create a new selection or modify the current seelction.

Select <entity_list> [add|remove]

This command selects the specified entities. If the add option is specified, the entities are added to the current selection. If the remove option is specified, the entities are removed from the current selection. If neither is specified, the current selection is replaced with the specified entities.

This command clears the selection.

Select Seed {face <ids>|tri <ids>} feature_angle <angle>

This command creates a new selection based on a seed face and feature angle. It finds all the neighboring faces with a feature angle that is less than the specified angle and adds them to the selection.

Rubberband Selection Control

The following commands control the behavior of rubberband selection.

Select Occluded {on|off}

When turned on, the selection will include entities that are occluded, or hidden behind other entities, in the current graphics view.

Select Partial {on|off}

When turned on, the selection will include all entities that touch the rubberband. When turned off, the selection will include only entities that lie completely within the rubberband region.

Select Rubberband Shape {box|polygon|circle}

Choose the rubberband shape to be box, polygon, or circle. If polygon is selected, the shape of the polygon is defined by the left mouse button clicks in the graphics windows. To end defining the polygon shape and make the selection, click the right mouse button.

---

## Select Visible Surfaces

**URL:** https://coreform.com/cubit_help/environment_control/entity_selection_and_filtering/select_visible.htm

**Contents:**
- Select Visible Surfaces
- Shared Options:
- Commands

The following commands select surfaces based on their visibility within a model. The rendering visibility of a surface, such as by turning visibility off or using a graphics clipping plane, does not affect these commands.

All the following command have these optional parameters that can be specified.

This value is the confidence level used to filter selected surfaces. Surface with a confidence value below the threshold will not be selected. The confidence value is calculated based on the visible amount of a surface compared to it percentage of total surface area in a model. If only a little of a surface is seen but that surface comprises a large percentage of the total surface area of the model then the calculated confidence value will be low.

This option causes the confidence value of all seen surfaces to be printed out.

This option excluded surface that are part of a hole from the selection. Surfaces with a surface area below the <exclude cavity max area>] value will not be selected.

select visible surfaces [threshold <threshold>] [exclude [holes] <exclude cavity max area>] [verbose]

This command selects all surfaces visible on the screen.

This command selects all surfaces visible around the current camera location.

select visible cavity volume <id> [threshold <threshold>] [exclude [holes] <exclude cavity max area>] [verbose]

This command selects all surface visible from the centroid of the specified volume.

This command selects all surfaces visible from three location along the bath between the centroid of the two specified surfaces.

The command selects all the surfaces visible from the combined centroid of the provided surfaces.

This command behaves differently depending on the number of locations provided.

With one location specified this command behaves like the “select visible cavity” command.

With two locations specified this command behaves like the “select visible cavity surface <ids> path“.

With three or more location specified this command behaves like the “select visible cavity surface <ids>” command.

select visible exterior [threshold <threshold>] [exclude [holes] <exclude cavity max area>] [verbose]

This command selects all the surfaces visible on the exterior of the model.

---

## Session Control

**URL:** https://coreform.com/cubit_help/environment_control/session_control/session_control.htm

**Contents:**
- Session Control

This section provides an overview to session control in CUBIT. This includes information on starting and exiting a CUBIT session, running CUBIT in batch mode, initialization files, how to enter commands, file manipulation, changing the working directory, memory manipulation and more. Much of your ability to use CUBIT effectively depends on mastery of concepts in this section. Even experienced users will find it useful to review this section periodically.

---

## Slot Surface Preparation with the Geometry Power Tool

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/slot_surfaces.htm

**Contents:**
- Slot Surface Preparation with the Geometry Power Tool
- Background
- Slot Surfaces
- Solutions Window
- Right-Click Menu Options
  - Export Slot Data
  - List Slot Data
  - Reduce Slot Surface

This page describes the slot surfaces diagnostic tool that is part of Cubit's Geometry Power Tool. The Slot Surfaces diagnostic is a new addition to the geometry power tool for preparing slot surfaces in Electromagnetic (EM) modeling. A slot surface is used to identify potential pathways where EM radiation can potentially exit. This diagnostic will help manage slot surfaces and prepare them for the application of boundary conditions and analysis. This diagnostic utilizes Machine Learning (ML) to predict the most likely slot surfaces.

The Geometry Power Tool in Cubit provides a series of diagnostic checks on your model used to defeature or simplify a CAD model prior to meshing. Clicking the Analyze button will perform the selected diagnostic tests and display an expanding tree listing geometric entities that are identified by each test. Once identified, suggested solutions can be easily previewed and executed.

The Slot Surfaces diagnostics work best in conjunction with the machine learning models. As such, to use this diagnostic the Load ML Models button must first be selected using the procedure described in the page Machine Learning with the Geometry Power Tool.

Figure 1. Example volume showing slot surface highlighted.

Figure 2. Slot Surfaces diagnostic displayed with Solution window.

The Slot Surfaces diagnostic is only available when the ML Models have been previously loaded in the Options panel. Once the ML models are loaded, select the Slot Surfaces diagnostic from the list of diagnostic tools. When this diagnostic is selected, the analyze button will identify all surfaces that are identified as slots. The surfaces will be separated into two groups: simple and complex.

---

## Specifying an Axis

**URL:** https://coreform.com/cubit_help/environment_control/location_direction_specification/specifying_axis.htm

**Contents:**
- Specifying an Axis
- Last
- Specify a direction and a location
- Specify a surface
- Specify a curve
- Option to revolve an axis about an axis
- Previewing an Axis

Some commands require a specified axis (such as webcut with a cylinder) and it is sometimes advantageous to view an axis before modifying geometry. An axis is simply a vector with a specified origin. The following options determine an axis specification:

The last option recalls the last axis used in an axis command. The last axis does not carry over from CUBIT session to CUBIT session.

Direction {options} [Origin [Location] {options}] [Length <val>] [Angle <val>]

To specify an axis simply specify a vector (a direction) and an origin (a location). Notice that the command requires the axis direction first because the origin defaults to 0 0 0 when not specified. An example of specifying an axis to draw a location using the swing command is as follows:

draw location 1 0 0 swing about axis direction z ang 45

Figure 1 - Swinging a point about the z-axis

The location 1 0 0 was swung 45 degrees about an axis defined by a vector in the z direction and an origin at 0 0 0.

If a surface is specified, it must be a cone type surface. The axis of the cone surface is used. If a non-cone type surface is specified, an error will result.

If a curve is specified, it must be an arc, helix, or spline of constant curvature. All other curve types will result in an error.

[Revolve [About] Axis {options} Angle <val>]

To revolve one axis around another use the revolve keyword. The following example revolves the first axis (defined by the y-axis and origin) around the second axis (defined by the z-axis and origin) by 45 degrees and draws the result.

draw axis direction y revolve axis direction z angle 45

Figure 2 - Revolving an axis about another axis

Sometimes it is helpful to preview an axis before using it in a command. An axis may be previewed using the Draw command. The options for previewing an axis are the same as the ones described above.

---

## Specifying a Direction

**URL:** https://coreform.com/cubit_help/environment_control/location_direction_specification/specifying_direction.htm

**Contents:**
- Specifying a Direction
- Vector (XYZ values)
- Last Direction Used
- Positive or Negative X,Y,Z Direction Vectors
- On Curve Tangent
- On Surface Normal
- From Location
- Rotate
- Cross
- Reverse

Some commands require a specified a direction or vector for the command. A direction is basically a xyz vector in the model. The following options determine a direction specification:

[Vector] <xval yval zval>

The most basic way to specify a direction is to just give the vector x-y-z components of the direction. The given vector need not be a unit vector. The following three commands simply draw a direction in the x-direction (1, 0, 0) as the Vector keyword is optional and unit vectors are not required:

draw direction vector 1 0 0 draw direction 1 0 0 draw direction 10 0 0

The last option recalls the last direction used in a command. For example, if the following command is entered after the above vector commands a direction location would be drawn in the x-direction (1, 0, 0).

Last directions do not carry over from CUBIT session to CUBIT session. The last direction defaults to (1, 0, 0) if no direction has been used during the session.

The x|y|z|nx|ny|nz options assign the x direction, y direction, z direction, negative x direction, negative y direction and negative z direction respectively.

[On] | [Tangent] [At] Curve <id> {location on curve options}

The curve option simply finds a tangent vector on a curve. Note that the on, tangent and at keywords are optional, as well as the location on the curve. If no location is specified, the tangent at the start vertex of the curve is found. See the section above, Specifying a Location on a Curve, for details on how to specify where along the curve the tangent vector is found.

draw direction curve 1 draw direction on curve 1 draw direction tangent at curve 1 draw direction tangent at curve 1 distance 3 draw direction tangent at curve 1 fraction .5 draw direction tangent at curve 1 distance 2 reverse

Figure 1 - Tangents to a Curve

[On] | [Normal] [At] Surface <id> [Location {options}]

The surface option simply finds a normal vector on a surface. Note that the "on", "normal" and "at" keywords are optional, as well as the location on the surface. If no location is specified, the normal vector at the center of the surface is found. If a location is specified, the location is projected to the surface, then the normal vector is found.

draw direction on surface 1 draw direction on surface 1 location 1 2 0

[From] {Location {options} | Node|Vertex <id>} [Project] {Location {options} | [Entity] {Node|Vertex|Curve|Surface} <id>}

The from location option finds a direction that is from one location to another or from a location to an entity. If the second specification is an entity, the first location is projected to the entity to find the direction.

draw direction from vertex 1 vertex 2 draw direction from location on curve 1 fraction .5 surface 3

Note that when using an entity for the second specification, the Project and Entity keywords are generally optional. However, it is sometimes necessary to remove ambiguity from the previous location specification. For example, the following will not parse correctly:

draw direction location on curve 1 distance 2 surface 3

In this case, the location on the curve is parsed as a distance 2.0 from surface 3. Instead, the desired behavior is to find the location on curve 1 as a distance of 2.0 along the curve from the start of the curve, and project it to surface 3 to find the direction. The following commands (all equivalent) achieve this behavior:

draw direction location on curve 1 distance 2 project surface 3 draw direction location on curve 1 distance 2 entity surface 3 draw direction location on curve 1 distance 2 project entity surface 3

The rotate option allows you to rotate the direction about another vector. You can string together as many rotations as necessary. For example:

draw direction 1 0 0 rotate about z 135 rotate about curve 1 angle 50

Options that can be used with rotate are as follows:

{Ax|X|Ay|Y|Az|Z [Angle] <angle>} | { {[About] | Towards} Direction {options} Angle <val> } [Rotate (options)] [Origin (location)]

Ax, Ay, Az (or X,Y,Z) angles can be entered in any order. The optional specification of another rotate keyword in the options indicated that multiple nested rotations are permitted.

[Cross [With] Direction {options}]

The cross option allows you to find the vector cross product of the direction with another direction.

This keyword simply reverses the direction specification.

Sometimes it is helpful to preview a direction before using it in a command. A direction may be previewed using the Draw command. The direction options are described above. See Specifying a Location for a list of location options.

Draw Direction {direction_options} [Location (location_options)]

---

## Specifying a Location

**URL:** https://coreform.com/cubit_help/environment_control/location_direction_specification/specifying_location.htm

**Contents:**
- Specifying a Location
- Position (XYZ values)
- Last Location Used in a Command
- Node or Vertex
- On a Curve
- On a Surface
- On a Plane
- Center
- Extrema
- Fire Ray

Some commands require a specified location or point (such as create curve spline) for the command. A location is basically an x-y-z position in the model. The following options determine a location specification:

[Position] <xval yval zval>

The most basic way to specify a location is to just give the xyz values of the location. In this case the following two commands both draw a location at the coordinates (1, 2, 3), as the Position keyword is optional:

draw location position 1 2 3 draw location 1 2 3

The last option recalls the last location used in a command. For example, if the following command is entered after the above position commands a location would be drawn at the position (1, 2, 3).

Last locations do not carry over from CUBIT session to CUBIT session. The last location defaults to (0, 0, 0) if no location has been used during the session.

[At] {Node|Vertex} <id_list>

Referring to a node or vertex simply returns the coordinates of that node or vertex. The command can also handle multiple locations where multiple locations are needed to complete the command string. The following draws a location at the coordinates of Vertex 5:

draw location vertex 5

Various options are available to specify a location on a curve. See the section Specifying a Location On a Curve for details.

[On] Surface <id_list> [Close_To | At Location {options} | CENTER]

If a surface is used to specify a location without other options, the geometrical center of the surface is found (the center keyword is optional - the default). Otherwise, you can specify another general location and that location is projected to the surface. For example, the following command will draw the location that is position (5,0,0) projected to surface 1:

draw location on surface 1 location 5 0 0

Any valid location options listed on this page can be used to specify the location that is projected to the surface.

[On] Plane <options> [Close_To | At Location {options}]

A location can be defined at the closest point on a plane to a location. See Specifying a Plane for plane options.

Center Curve <id_list>

Finds the center of an arc - an error is returned if the curve is not an arc.

Extrema {Curve|Surface|Volume|Body|Group} <range> [Direction] {options} [Direction {options}] [Direction {options}]

The extrema option returns the location of the maximum value, on the specified entity or group, in the specified direction. For example, the following places a vertex on a surface at the point of maximum y-axis value.

create vertex location extrema surf 1 direction y

The fire ray command allows a user to identify a location, or set of locations, on an object by firing a ray at the object and determining the intersections. A ray can be fired at a list of bodies, volumes, surfaces, curves, or vertices. The fire ray command is:

Fire Ray Location {options} Direction {options} At {Body|Volume|Surface|Curve|Vertex} <ids> [Maximum Hits <val>] [Ray Radius <val>]

The location options are described on this page. The direction options are described under Specifying a Direction. The user can specify the maximum number of hits that he wishes to receive back from the command. If this value is omitted, the command will return all intersections found. When firing a ray at a curve, a ray radius must be used. The ray radius is the distance from the curve the ray must be to be considered a "hit." If no ray radius is used, the geometry engine default is used.

Between {Location <options> Location <options> } | {Location <options> Project {Curve|Surface} <range>} [Stop] [Fraction <val>]}

The between option finds a location that is between two locations or a location and an entity. An optional fraction can be given to specify the fractional distance from the first location to the second location or entity. For example, the following will draw a location at (5, 0, 0):

draw location between location 0 0 0 location 10 0 0

The following will draw a location at (2.5, 0, 0) - 25% of the distance from (0, 0, 0) to (10, 0, 0):

draw location between location 0 0 0 location 10 0 0 fraction .25

The second item can be an entity:

draw location between location 0 0 0 vertex 2 draw location between location 0 0 0 surface 1

In the second case, location (0, 0, 0) is projected to surface 1, then the location that is between (0, 0, 0) and the projected location is found.

Of course, any valid location can be used in the command. In the following example a location at the top center of the brick is found:

brick x 10 draw location between location bet vert 3 vert 2 location bet vert 8 vert 5

The first location is between vertices 3 and 2, and the second location is between vertices 8 and 5.

Note: you can "swing" a location about an axis, "rotate" a direction about another direction, "revolve" an axis about another axis and "spin" a plane about an axis. The only reason Cubit needs to use different keywords for each entity type is because the Cubit command language does not support expressions (as in using parentheses). The keyword stop is also used in the location/direction/axis/plane parsing as a partial workaround to this limitation. Using this stop keyword will aid in parsing out extended location specifications. Insert a stop after the first location to let the parser know that where the specifications begin and end.

Move [All] { <xval yval zval> | {Dx|X|Dy|Y|Dz|Z} <val> | Direction {options} Distance <val> }

Any location can be optionally moved either a xyz distance or a certain distance in a given direction. As many moves as desired can be strung together. For example, the following will return a location at (5, 0, 0):

draw location 0 0 0 move 5 0 0

These examples add another move that basically moves the location (5, 0, 0) in a direction 45 degrees up and to the right a distance of 10 (all three commands are equivalent - see sections on directions and rotations):

draw location 0 0 0 move 5 0 0 move {10*sind(45)} {10*sind(45)} 0 draw location 0 0 0 move 5 0 0 move direction 1 1 0 distance 10 draw location 0 0 0 move 5 0 0 move direction 1 0 0 rotate about 0 0 1 angle 45 dist 10

Swing [All] [About] Axis {options} Angle <ang>

Any location can be "swung" (rotated) about an axis by a certain angle. (See the section on specifying an axis for the axis syntax). As with moves, multiple swings can be strung together. The following example rotates the location (2.5, 5, 5) thirty degrees about an axis defined by Curve 11. Note that the right-hand rule is used to determine the direction of the swing about the axis.

draw location 2.5 5 5 swing about axis curve 11 angle 30

Figure 1 - Swinging a Location

Location {options} Location {options}...

Multiple location specifications can be used in a single command. For example, the following command uses several locations to create a spline curve at points (0,0,0), (1,2,3), (4,5,6), and (7,8,9).

create curve spline location 0 0 0 location 1 2 3 location 4 5 6 location 7 8 9

Sometimes it is advantageous to preview a location before using it in a command. A location can be previewed with the Draw command. All of the options that can be used to specify locations in a command can be used to preview locations as well. See above for a description of these options. The command syntax is:

Draw Location {options}

---

## Specifying a Location on a Curve

**URL:** https://coreform.com/cubit_help/environment_control/location_direction_specification/specifying_location_on_curve.htm

**Contents:**
- Specifying a Location on a Curve
- Center
- Start, Midpoint, or End
- Fraction
- Distance
- {Close_To|At} Location
- Extrema
- Segment
- Crossing
- Previewing a Location on a Curve

Some commands require you to specify a location on a curve (i.e., webcutting with a plane normal to a curve). The following are the options for specifying a location (or locations in the case of the segment option) on a curve:

The center option helps in identifying the location at the center of a given arc. Example: create vertex center curve 3

{ MIDPOINT | Start | End |

These options simply specify the location that is the midpoint, start or end point of a curve. By default, the midpoint is the understood location unless another location is specified.

Fraction <val 0.0 to 1.0> [From Vertex <id> | Start|End] |

The fraction option simply finds the location that is a fractional distance along the curve. By default, the fraction references the start of the curve; however, you can optionally specify which vertex to reference from.

Distance <d> [From {Vertex|Curve|Surface} <id> | Start | End ] |

The distance option not only can find a location that is a certain distance along the curve from the start or end of the curve, but can also find a location (or locations if there is more than one solution) on a curve that is a specified distance from another curve or a surface. If the From Curve option is used both curves must lie in the same plane.

draw location on curve 13 distance 7 from curve 2

Figure 1 - Location on a Curve a Distance from Another Curve

{{Close_To|At} Location {options} | Position <xval><yval><zval> |{Node|Vertex} <id>} |

These options take a location closest to the location on the curve.

Extrema [Direction] {options} [Direction {options}] [Direction {options}]

The extrema option finds the maximum value location along a curve in a specified direction. For example:

create vertex location on curve 1 extrema ny

Creates a vertex on curve 1 at the location where the y axis value of the curve is at a minimum.

The segment option finds locations spaced evenly along the curve such as to break the curve into equal length "segments" (of course the curve is not modified). You must specify a minimum of two segments (if two segments were specified a location would be found at the center of the curve). The following example results in 4 locations:

draw location on curve 1 segment 5

create vertex on curve 1 segment 5

Figure 2 - Five Segments on a Curve

Crossing {Curve|Surface} <id_list> [Bounded|Near]}

The crossing option finds locations at the intersection of the curve and another curve or surface. By default, the curve(s) and surface are extended to infinity and the intersections are calculated; if the bounded option is specified only intersections that lie on the bounded entities will be returned. The near option is valid only for two linear curves. If near is specified the nearest location between the two linear curves will be returned.

A location on a curve can be previewed with the Draw command. All of the options that can be used for specifying a location on a curve can be used to preview a location on a curve. See above for a description of these options. The command syntax is:

Draw Location On Curve <curve id> {options}

---

## Specifying a Plane

**URL:** https://coreform.com/cubit_help/environment_control/location_direction_specification/specifying_plane.htm

**Contents:**
- Specifying a Plane
- Location and Normal Vector
- Location and Two Vectors on the Plane
- Two Locations and Vector on the Plane
- Three Points on the Plane
- Plane defined by a Surface
- Plane Normal to a Curve
- Plane Defined by a Non-linear curve
- Plane Defined by a two linear curves
- Normal Vector and Coefficient

Some commands require a specified plane (such as sweep curve target) for the command. The following options determine a plane specification:

The following options apply to all of the plane specifications listed above:

{Location|Vertex|Node} <origin> Direction <normal>

The first way to specify a plane is to specify a starting point and a direction vector:

draw plane location 1 2 3 direction 0 1 1 draw plane vertex 1 direction tangent at curve 1

Figure 1. Specifying a plane with a location and surface normal

To see the options for location specification, see Specifying a Location. Direction options can be found at Specifying a Direction.

{Location|Vertex|Node} <origin> Direction <vec on plane> Direction <vec on plane>

It is also possible to select an origin point and 2 direction vectors on the plane.

Figure 2. Specifying a plane with a point and 2 in-plane vectors

{Location|Vertex|Node} <2 locations> Direction <vector on the plane>

You can also specify 2 locations and 1 direction on the plane to define the plane.

draw plane vertex 1 2 direction 0 1 1

Figure 3. Specifying 2 locations and 1 direction on the plane

{Location|Vertex|Node} <3 locations>

A plane can be defined by three locations, vertices, or nodes. The locations are specified using Location Specification.

draw plane vertex 1 2 3 draw plane vertex 1 2 location 3 4 5

Figure 4. A plane specified by three points

Surface <id> [At Location <loc>]

The surface option uses and existing surface to define the plane. If it is not a planar surface, the optional location specifier can be used to find the tangent plane of a specific point on the surface.

draw plane surface 1 at location 4 0 0

Figure 5. Specifying a Tangent plane to a Surface

[Normal To] Curve <id> [loc on curve options]

The Normal to Curve option allows you to define a plane by using an existing curve. The direction of the curve will define the surface normal of the new plane. The optional location argument specifies which point to use on the curve if it is not a straight curve. If no location is specified the plane will originate at the midpoint of the curve. See Specifying a Location on a Curve for more information on location options.

brick x 10 cylinder radius 3 z 12 subtract body 2 from 1 webcut body 1 xplane draw plane normal to curve 30

Figure 6. Draw Plane Normal to Curve

cylinder height 12 radius 3 draw plane arc curve 2

Linear Curve <id> <id>

brick x 10 draw plane linear curve 2 3

Direction <Normal> Coefficient <val>

The direction and coefficient option allows you to specify a plane based on a vector and an offset from the origin. The Coefficient argument specifies how far to offset the plane from the origin

draw plane direction 1 2 3 coefficient 3

X|Xplane|Yz|Zy|Y|Yplane|Zx|Xz|Z|Zplane|Xy|Yx

A plane can be defined from any coordinate plane or combination thereof. The coordinate planes will pass through the origin unless optional specifiers are included.

draw plane xplane webcut volume 1 plane xz

The last option will return the plane most recently used in a command. Last locations do not carry over from CUBIT session to CUBIT session. The last location defaults to (0, 0, 0) if no location has been used during the session.

The following options apply to all of the plane specification methods described above.

A offset value will offset the plane in the direction of the surface normal.

The move option will displace the plane in the specified directions by the specified distance. The direction options are outlined on Specifying a Direction.

The location option will move the plane to a specified location without rotating it. See Specifying a Location for location options.

The spin option will rotate the plane around an axis. See Specifying an Axis for axis options.

Draw Plane (options) [Graphics | {[Intersecting] {Body|Volume} <id_range>] [ [Extended] {Percentage|Absolute} <val>]}] [Color 'color_name']

Draw Cylinder Radius <val> Axis {x|y|z|Vertex <id_1> Vertex <id_2> | <xyz values>} [Center <x_val> <y_val> <z_val>] [[Intersecting] Body <id_range>] [Extended Percentage|Absolute <val>] [Color 'color_name']

The cylinder is defined by a radius and the cylinder axis. The axis is specified as a line corresponding to a coordinate axis, the normal to a specified surface, two arbitrary points, or an arbitrary point and the origin. The center point through which the cylinder axis passes can also be specified.

By default, the commands draw the cylinder just large enough to just intersect the bounding box of the entire model. Optionally, you can give a list of bodies to intersect for this calculation. You can also extend the length of the cylinder by either a percentage distance or an absolute distance of the cylinder length. The default color is blue, but you can specify a different one. See the Appendix of the CUBIT Users Guide for available colors in CUBIT.

---

## Starting and Exiting a CUBIT Session

**URL:** https://coreform.com/cubit_help/environment_control/session_control/starting_and_exiting.htm

**Contents:**
- Starting and Exiting a CUBIT Session
- Starting the Session
- Windows File Association
- Exiting the Session
- Resetting the Session
- Abort Handling

The following commands are used to control CUBIT execution.

Cubit contains both a GUI and a command line version of the application. Additionally, Cubit can be imported into a Python session with Cubit functions being available. If you have not yet installed CUBIT, instructions for doing so can be found in Licensing and Activation. For details on how to start the application and a list of startup options see the Execution Command Syntax section of this document. CUBIT can also be run with initialization files or in batch mode.

Windows users have the option to associate .cub, .sat, and .jou files with CUBIT. This means that double-clicking on one of these files will open it automatically in CUBIT. This option is available during the installation process

The CUBIT session can be discontinued with either of the following commands

A reset of CUBIT will clear the CUBIT database of the current geometry and mesh model, allowing the user to begin a new session without exiting CUBIT. This is accomplished with the command

Reset [Genesis | Block | Nodeset | Sideset | QA_Records]

A subset of portions of the CUBIT database to be reset can be designated using the qualifiers listed. Advanced options controlled with the Set command are not reset.

QA Records are stored in exodus, genesis, or cub files. If your file contains an excessive amount of qa records and you don't need them, it is beneficial to reset them for faster file I/O.

You can also reset the number of errors in the current Cubit session, using the command

which will set the error count to the specified value, or zero if the value is left blank.

In the event of a crash, Cubit will attempt to save the current mesh as "crashbackup.cub" in the current working directory just before it exits. To disable saving of the crashbackup.cub file set an environment variable CUBIT_NO_CRASHSAVE equal to true. Or, use the following command:

Set Crash Save [On|Off]

This command will turn on or off crashbackup.cub creation during a crash on a per-instance basis. To minimize the effects of unexpected aborts, use Cubit's automatic journaling feature, and remember to save your model often.

---

## Toolbars

**URL:** https://coreform.com/cubit_help/environment_control/gui/toolbars.htm

**Contents:**
- Toolbars
- File
- Display
- Select

The CUBIT toolbars provide an effective way for accessing frequently used commands.

Below is a brief description of each of the available toolbars. To view a description of the function of each tool, hold the mouse over the tool in the CUBIT Application to display tool tips.

Users may customize and share toolbars.

Provides CUBIT (*.cub) file operations. This toolbar also includes Journal File operations.

Figure 1. File Toolbar

From left to right, the tool buttons are as follows:

Controls the display mode, checkpoint undo, zoom, perspective clipping plane, and curve valence display options in the Graphics Window.

Figure 2. Display Toolbar

From left to right, the tool buttons are as follows:

Controls the Entity Selection Mode for picking or selecting entities.

Figure 3. Select Toolbars

---

## Toolbar Customization

**URL:** https://coreform.com/cubit_help/environment_control/gui/toolbar_customization.htm

**Contents:**
- Toolbar Customization
- Menu
- Importing an Existing Toolbar
- Creating a New Toolbar
- Creating a Command Panel Button
    - Use the definition dialog
    - Use the context menu on a command panel
    - Drag a command panel onto the toolbar
- Creating a Journal File Button
- Creating a Python Script Button

For many years Cubit has provided users with the ability to create custom tool buttons. These custom buttons launch pre-defined journal or Python scripts. With the release of Cubit 15.4 this capability has been expanded.

From this dialog a user may import an entire package containing multiple toolbars or a single toolbar. In this example we will import an entire package containing multiple toolbars.

The new toolbar and buttons will be displayed as the last toolbar on the GUI. It is a docking window so it can be moved and placed anywhere on the GUI.

Press the Add button in the Buttons area

A user may define 4 different types of toolbar buttons

A Command Panel Button enables users to launch a command panel with the push of a button. A command panel button can be defined one of three ways:

To find the Command Panel ID:

All command panels include a context menu which can be accessed by clicking on an empty place in the command panel and using the mouse to show the menu.

A Journal File Button will launch a journal file when pressed. The journal file may reside anywhere on the file system. A journal file button is defined by:

The "Basic" too button has been available to users for many years. It contains a set of commands that execute when the user presses the button.

A user may want to share a toolbar, or a set of toolbars, with another user. This is easily accomplished.

---

## Training CAD Operations with Machine Learning

**URL:** https://coreform.com/cubit_help/environment_control/entity_selection_and_filtering/ml_regression.htm

**Contents:**
- Training CAD Operations with Machine Learning
  - Syntax:
- Regression Models
  - Mesh Quality
  - Suitability
- Predicting CAD Operation Outcomes
- Adding New CAD Operation Training Data
- Training CAD Operations
- Listing Regression Models
- Resetting Regression Models

Regression Models Predicting CAD Operation Outcomes Assigning new CAD Operation Training Data Training CAD Operations Listing Regression Models Resetting Regression Models User Training Data

predict copy_surface {volume <ids> surface <ids>} [features [importance]]

predict midsurface {volume <ids> surface <ids>} [features [importance]]

learn copy_surface {volume <ids> surface <ids>} label <value> [export_acis]

learn midsurface {volume <ids> surface <ids>} label <ids> [export_acis]

learn train [<string>]

learn reset ["<string>"]

learn user path ["<string>"]

Mesh quality models are mostly used for driving defeaturing of CAD models. They are currently used in Cubit's Geometry Power Tool diagnostics to predict where potential mesh quality issues will appear on the FE mesh before meshing and to provide a recommendation for CAD operations that can be used to resolve the issue based on a predicted mesh quality outcome.

Learn copy_surface volume <id> surface <ids>

Learn midsurface volume <id> surface <ids>

Learn copy_surface volume <id> surface <ids> label <value>

Learn midsurface volume <id> surface <ids> label <value>

Learn Train ["<string>"]

Learn List ["<string>"]

Learn Reset ["<string>"]

Learn User Path ["<path_string>"]

To display both the current user training data directory and the fixed training data directory, use the Learn List command. While the fixed training data directory cannot be changed, it may be worthwhile to change the user training directory. To change the user training directory, use the command Learn user path "<path_string>" where <path_string>> is the full path to a writable directory on disk in quotes. Changing the user training directory may be useful to temporarily use training data from another source or to ignore all user training data without removing it.

Using the command, Learn User Path without a path specification will set the user training data directory back to its default for the platform. Changing the user path using the Learn command will also change the path for the Classify command.

**Examples:**

Example 1 (typescript):
```typescript
/Users/<user_name>/Library/Application Support/Cubit/ml
```

---

## Undo Button

**URL:** https://coreform.com/cubit_help/environment_control/gui/drop_down_menus/undo.htm

**Contents:**
- Undo Button
- Limitations

Cubit has an undo capability. To enable the Undo feature click on the "Enable Undo" button on the Toolbar.

Alternatively to turn undo on and off, the following command may be used in the command line: undo {on|off}

The Undo capability is implemented for geometry commands including webcutting, geometry creation, transformations, and booleans. Multiple undos are also allowed. The commands will be undone in reverse order of their execution.

---

## Updating the Display

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/updating_display.htm

**Contents:**
- Updating the Display
- Prevent Graphics From Updating

Among the most common graphics-related commands is:

This command clears all highlighting and temporary drawing, and then redraws the model according to the current graphics settings. The GUI tool bar button for executing this command is:

Two related commands are:

Graphics Flush redraws the graphics without clearing highlighting or temporary drawing. Graphics Flush is useful when a previously executed command modified the graphics and didn't update the screen and the user wishes to update the display. The Graphics Clear command clears the graphics window without redrawing the scene, leaving the window blank.

NOTE: Although most changes to the model are immediately reflected in the graphics display, some are not (for graphics efficiency). Typing Display will update the display after such commands. Ctrl-R will also update the display as long as the mouse is in the graphics window.

For especially large models, it may take excessively long to update the display after an action has been performed. To prevent the graphics from automatically updating, use the following command:

This command prevents the graphics window from being updated until the next time the Display command is issued.

NOTE: The Plot command is synonymous to the Display command, and either can be used with identical results.

---

## Viewing Curve Valence

**URL:** https://coreform.com/cubit_help/environment_control/gui/graphics_window/curve_valence.htm

**Contents:**
- Viewing Curve Valence

To view your model based on a color-coded curve valence scale, click on the curve valence button on the Display Toolbar. Curve valence refers to the number of surfaces attached to each curve. Curves with exactly two surfaces attached are shown in blue. Curves with exactly one surface are shown in red. Curves with more than two attached surfaces are shown in white.

This tool is useful for quickly visualizing merged/unmerged topology. Merged curves will usually have a valence > 2, while unmerged curves typically have a valence of 2. Curves with a valence of 1 may indicate a floating surface.

---

## View Navigation in the GUI

**URL:** https://coreform.com/cubit_help/environment_control/gui/graphics_window/view_navigation.htm

**Contents:**
- View Navigation in the GUI
- Rotations
- Zooming
- Panning

There are two different default paradigms for view navigation: Cubit command line and Cubit GUI. The user is allowed to customize the mouse settings as desired. Mouse settings in the GUI are modified by accessing the Tools pull-down menu, then select Options. The Mouse Settings dialog is shown below (See Mouse-Based Navigation for the command line version).

Figure 1. Mouse Settings Dialog

Where the cursor is in the graphics window will dictate how the view will be rotated. If the cursor is outside of an imaginary circle, shown in Figure 2, the view will be rotated in 2d, around an axis normal to the screen. If it is inside the circle, as in Figure 3, the rotations will be in 3d, about the current view spin center. The spin center can be changed to any x-y-z location. The most common way is by zooming to an entity, which changes the spin center to the centroid of that entity. The "view at" command will change the spin center without zooming:

Figure 2. With the mouse pointer outside the circle the view is rotated about an axis normal to the screen

Figure 3. With the mouse pointer inside the circle the view is rotated about the current spin center

To zoom, press the appropriate buttons or keys and move the cursor vertically, as shown in Figure 4. The wheel on a wheel mouse will also zoom.

Figure 4. Move the mouse pointer vertically to zoom in and out

To pan, press the appropriate buttons or keys and move the cursor horizontally or vertically, as shown in Figure 5.

Figure 5. Move the mouse pointer horizontally or vertically to pan the view

---
