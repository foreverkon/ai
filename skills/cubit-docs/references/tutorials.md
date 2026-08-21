# Tutorials

## CL Basic Tutorial Step 10

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_10.htm

**Contents:**
- CL Basic Tutorial Step 10
- Step 10: Defining Boundary Conditions

Let us assume that we need to define one material type for the entire mesh, and a single node-based boundary condition on all surfaces. This is accomplished by identifying an Element Block and a Nodeset, respectively; the id numbers assigned to these entities are assigned by the user, usually by some convention meaningful to the analysis to be done. The element block and nodeset are identified using the commands:

cubit> block 100 volume 1

cubit> nodeset 100 surface all in volume 1

---

## CL Basic Tutorial Step 11

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_11.htm

**Contents:**
- CL Basic Tutorial Step 11
- Step 11: Exporting the Mesh

Finally, the mesh needs to be written to an ExodusII file. This is easily done:

cubit> export genesis `brick_with_hole.g'

The filename and extension are arbitrary and, like the block and nodeset numbers, are usually named according to a convention meaningful to the analysis.

---

## CL Basic Tutorial Step 1

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_01.htm

**Contents:**
- CL Basic Tutorial Step 1
- Step 1: Beginning Execution

Type "cubit" from a UNIX prompt to begin execution of CUBIT. A CUBIT console window will appear which tells the user which CUBIT version is being run and the most recent revision date. An example of the UNIX output window is shown below. This window echoes the commands and relays information about the success or failure of attempted actions.

Some things to notice are:

---

## CL Basic Tutorial Step 2

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_02.htm

**Contents:**
- CL Basic Tutorial Step 2
- Step 2: Beginning Execution

Now you may begin generating the geometry to be meshed. You will create a brick of width 10, depth 10 and height 10. The width and depth correspond to the x and y dimensions of the object being created. The "width" or x-dimension is screen-horizontal and the "depth" or y-dimension is screen-vertical. The height or z-dimension is out of the screen. The command to create this object is:

cubit> create brick width 10 depth 10 height 10 (OR)

cubit> create brick x 10

The cube should appear in your display window as shown below:

---

## CL Basic Tutorial Step 3

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_03.htm

**Contents:**
- CL Basic Tutorial Step 3
- Step 3: Creating the Cylinder

Now you must form the cylinder which will be used to cut the hole from the brick. This is accomplished with the command:

cubit> create cylinder height 12 radius 3

At this point you will see both a brick and a cylinder appear in the CUBIT display window, as shown below:

---

## CL Basic Tutorial Step 4

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_04.htm

**Contents:**
- CL Basic Tutorial Step 4
- Step 4: Adjusting the Graphics Display
  - Command Line
  - Mouse

The geometry is drawn in the graphics display in perspective mode by default from a viewing direction of the +z axis. This view can now be adjusted to verify the proper orientation of the geometry just created. The orientation of the geometry can be adjusted using the command line or interactively with the mouse.

You can adjust the orientation of the object from the command line. For example, the from command can be used as follows

To interactively change the orientation, activate your graphics window by placing your cursor in the window or by clicking at the top of it (this will vary depending upon your window settings in your operating system).

Use the mouse buttons to make the display look the figure below:

View from a Different Perspective

---

## CL Basic Tutorial Step 5

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_05.htm

**Contents:**
- CL Basic Tutorial Step 5
- Step 5: Forming the Hole

Now, the cylinder can be subtracted from the brick to form the hole in the block. Issue the following command:

cubit> subtract 2 from 1

Note that both original volumes are deleted in the Boolean operation and replaced with a new volume (with an id of 1) which is the result of the Boolean operation Subtract .

The result of this operation is a single body, a brick with a hole through as shown below:

Brick after Subtracting the Cylinder

We have now completed creating the geometry, and are ready to generate a mesh.

---

## CL Basic Tutorial Step 6

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_06.htm

**Contents:**
- CL Basic Tutorial Step 6
- Step 6: Setting Interval Sizes

The volume shown in Step 5 will be meshed by sweeping a surface mesh from one side of the brick to the other. Before generating any mesh, the user must specify the size of the elements to be generated. In this example, one element size will be specified for the volume as a whole and a smaller size will be specified for around the hole. A direct interval setting will be specified for the sweep direction.

To set the interval size for the overall volume, enter the command

cubit> volume 1 size 1.0

Since the brick is 10 units in length on a side, this specifies that each straight curve is to receive approximately 10 mesh elements.

In order to better resolve the hole in the middle of the top surface, we set a smaller size for the curve bounding this hole. To find the id number of the curve bounding the hole, the user can either pick the curve (See Selecting Entities with the Mouse) or turn curve labels on and regenerate the view. To do the latter, use the command

cubit> label curve on

The default size of the labels can sometimes be too small to read. To change the text size, use the graphics text size command:

cubit> graphics text size 2

The result is shown in the figure below. Then the interval size can be set for the appropriate curve:

Geometry with Curve Labeling Turned on

cubit> curve 16 interval size 0.78

Finally, we would like to generate exactly 5 element layers in the sweep direction. This is accomplished by setting the intervals on curve 11:

cubit> curve 11 interval 5

---

## CL Basic Tutorial Step 7

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_07.htm

**Contents:**
- CL Basic Tutorial Step 7
- Step 7: Surface Meshing

Now that all the necessary intervals have been set, the meshing can proceed. Begin by meshing the front surface (with the hole) using the paving algorithm. This is done in two steps. First, set the scheme for that surface to Pave; then, issue the command to Mesh. Since the surface to be paved is number 11, issue the command:

cubit> surface 11 scheme pave

With the meshing scheme specified, we proceed to mesh the surface:

cubit> mesh surface 11

The results are shown below:

Surface Meshed with Paving

---

## CL Basic Tutorial Step 8

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_08.htm

**Contents:**
- CL Basic Tutorial Step 8
- Step 8: Surface Meshing

The volume mesh can now be generated. Again, the first step is to specify the type of meshing scheme to be used and the second step is to issue the order to mesh. In certain cases, the scheme can be determined by CUBIT automatically. For sweepable volumes, the automatic scheme detection algorithm also identifies the source and target surfaces of the sweep automatically.

To instruct the code to automatically determine the meshing scheme and in this case the source and target surfaces, enter the command:

cubit> volume 1 scheme auto

To view the results of auto scheme selection, certain data about the volume can be listed:

The results of this command are shown below; note that the scheme, and in this case the source and target surfaces, are reported toward the top of the list output.

Output from Listing Volume 1

With the scheme set, the mesh command may be given:

The final meshed body will appear in the display window, as shown below:

---

## CL Basic Tutorial Step 9

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/step_09.htm

**Contents:**
- CL Basic Tutorial Step 9
- Step 9: Inspecting the Model

The type, quality, and speed of rendering the image can be controlled in CUBIT by using several graphics mode commands, such as Wire Frame, Hidden Line, Transparent and Smooth Shade. For example:

cubit> graphics mode wireframe

The wire frame display is illustrated below:

Wire Frame View of Mesh

cubit> graphics mode hiddenline

The hidden line display is illustrated below:

Hidden Line View of Mesh

cubit> graphics mode transparent

The transparent display is shown below.

Transparent View of Mesh

cubit> graphics mode smoothshade

The smooth shade display is shown below. For detailed information on the viewing mode options, See Graphics Modes.

Smooth Shade View of Mesh

Although CUBIT automatically computes limited quality metrics after generating a mesh and warns the user about certain cases of bad quality, it is still a good idea to inspect a broader set of quality measures. To do this, enter the command:

cubit> quality volume 1

The results of the quality output are shown below. For an explanation of quality metrics along with acceptable ranges, see Mesh Quality Assessment. For the purposes of this tutorial, you can assume the quality metrics shown below are in an acceptable range.

Quality Table from Volume 1's Hex Mesh

---

## Command Line Basic Tutorial

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/command_line/overview.htm

**Contents:**
- Command Line Basic Tutorial
- Overview

This tutorial demonstrates the use of CUBIT to create and mesh a brick with a through-hole. The primary steps in performing this task are:

Each of these steps is described in detail in the following sections. The geometry in this tutorial is a brick with a cylindrical hole in the center, shown in the figure below. This figure also shows the curve and surface identification (ID) numbers, which are referenced in the command lines shown with each step. The final meshed body is shown in the next figure.

Geometry for Cube with Cylindrical Hole

Generated Mesh for Cube with Cylindrical Hole

---

## Decomposition Tutorial

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/decomposition.htm

**Contents:**
- Decomposition Tutorial
- Creating Sweepable Volumes Through Webcutting
- Why use sweeping?
- What makes a volume sweepable?
  - Basic Sweep Groups
  - Points to consider when determining whether a volume is sweepable
  - Basic Sweep Paths
- What are some good strategies for decomposing my model?

Most volumes require some measure of decomposition before they can be meshed with a hexahedral meshing scheme. The most common hexahedral meshing tool is the sweeping algorithm. Sweeping is the process of creating a hexahedral mesh by extruding a quadrilateral surface mesh from a source surface onto a topologically similar target surface by way of a linking surface. The surface mesh can be meshed with any surface meshing scheme (i.e. structured or unstructured mesh), but the most common surface meshing scheme for the sweeping algorithm is the pave scheme. In fact, the sweeping algorithm is sometimes called the "pave-sweep" algorithm. Most volumes aren't automatically sweepable, which is why geometry decomposition is so important to the meshing process. Decomposition usually involves a series of webcutting, boolean, and virtual geometry operations that break up a larger model into sweepable regions. Studies have shown that this step in the meshing process is the most time consuming for the analyst. The goals of this tutorial are for the user to learn to:

Of all the hexahedral meshing schemes in the Cubit toolkit, sweeping is considered the most reliable at producing high quality elements. Although decomposing a model into sweepable volumes can be time-consuming, and sometimes falls into the realm of trying to fit a square peg into a round hole, the pave-sweep algorithm has a high rate of success, and it sometimes the only way to get a hexahedral mesh on a model.

Recognizing sweepable topologies can be an art form. Sweepable volumes can be comprised of many different topologies. We typically classify sweeping problems into three groups, based on the number of source/target surfaces.

One-to-one: A volume with a one source surface and one target surface.

Many-to-one: A volume with multiple source surfaces and one target surface

Multisweep (or Many-to-Many): A volume with multiple target surfaces

In addition to the different topologies, sweepable volumes can be classified by the sweep direction. These include: top-to-bottom, inside-to-outside, and around (rotational). Be sure to consider all the possibilities for sweep directions when you begin decomposing a model. And keep in mind that sweep paths must be compatible with adjacent volumes. To be compatible, overlapping surfaces must have the same scheme (i.e. both must be a linking surface or a paved surface). The volume below is meshed three different times with the three different sweep directions. Notice the difference in element sizes and orientations between the meshes. See if you can pick out the different source and target surfaces in each example. As an exercise, try to mesh this model with each of the different sweep paths.

Recognizing when a volume is sweepable is a difficult task of itself, but being able to come up with viable webcutting, compositing, and boolean strategies to make a volume sweepable is even more difficult, and can only be achieved through practice. Here are some general principles to follow when decomposing a model.

The following is a compilation of several different decomposition problems of varying difficulty. You can download the example files here.

---

## Example 1. Sweeping multiple adjacent volumes

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/example01.htm

**Contents:**
- Example 1. Sweeping multiple adjacent volumes
- Suggested webcut
- Final mesh

Figure 1. Exterior view

Figure 2. Interior view

The final mesh is created at a size of 0.15 for all volumes.

---

## Example 2. Interlocking rings

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/example02.htm

**Contents:**
- Example 2. Interlocking rings
- Suggested webcuts
- Final mesh

CUBIT> webcut body 1 plane surface 5

CUBIT> webcut body 2 sheet extended from surface 4

CUBIT> webcut body 3 plane surface 12

CUBIT> webcut body 4 sheet extended from surface 10 CUBIT> imprint all CUBIT> merge all

There are five volumes that result from the webcutting. Two of them are automatically sweepable. Two of them must have their schemes set explicitly, and one of them is meshed using the tetprimitive scheme.

Source and target are set automatically using autoscheme

CUBIT> volume 1 3 scheme auto

Must have source and target set explicitly

CUBIT> volume 2 scheme sweep source 17 target 7 CUBIT> volume 4 scheme sweep source 29 target 18

Use the tetprimitive scheme

CUBIT> curve in volume 5 interval 6 CUBIT> volume 5 scheme tetprimitive CUBIT> volume all size 0.5 CUBIT> mesh volume all

The final mesh is created at a size of 0.5 for all volumes.

---

## Example 3. Webcutting using the sweep option

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/example03.htm

**Contents:**
- Example 3. Webcutting using the sweep option
- Suggested webcuts
- Final mesh

CUBIT> webcut volume 1 with sheet extended from surface 27

CUBIT> webcut volume 1 with plane surface 30

CUBIT> webcut vol all sweep surf 26 vector -1 0 0 through_all

Now Volume 3 (red) has only 1 target surface.

CUBIT> imprint all CUBIT> merge all CUBIT> volume all size 0.05 CUBIT> mesh volume all

The final mesh is created at a size of 0.05 for all volumes.

---

## Example 4. Using the Loft command

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/example04.htm

**Contents:**
- Example 4. Using the Loft command
- Suggested webcuts
- Final mesh

Webcuts created from sweeping surfaces (not recommended)

Webcuts using loft command (recommended)

CUBIT> webcut body 2 loop curve 6

CUBIT> webcut body 2 sheet extended from surface 1

CUBIT> create surface from surface 10 CUBIT> create surface from surface 4 CUBIT> create body loft surface 19 20

CUBIT> webcut body 3 tool body 7 CUBIT> delete body 5 6 7

CUBIT> webcut body 2 3 plane yplane CUBIT> imprint all CUBIT> merge all CUBIT> volume all size 0.15 CUBIT> mesh volume all

The final webcut model consists of a central shaft which can be swept top to bottom, and a surrounding casing which can be swept around. This is possible because the shared surface is a linking surface for both types of sweeps. The final mesh is created with a size of 0.15

---

## Example 5. Multiple sweep directions

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/example05.htm

**Contents:**
- Example 5. Multiple sweep directions
- Suggested webcuts
- Final mesh

CUBIT> webcut volume all with plane yplane offset 20

CUBIT> webcut volume all with plane yplane offset -20 CUBIT>imprint all CUBIT>merge all

All of the volumes in this model are now one-to-one sweepable. However, the source and target surfaces for the main block portions must be set explicitly

CUBIT>volume 8 scheme Sweep source surface 94 target surface 90 rotate off

CUBIT>volume 10 scheme sweep source surface 71 target surface 73 rotate off

CUBIT>volume 12 scheme Sweep source surface 97 target surface 100 rotate off

CUBIT>volume all size 2

CUBIT>mesh volume all

In this model it is possible to have different sweep directions since the surfaces which overlap are both linking surfaces. The final mesh is created with a mesh size of 2 and is shown below.

---

## Example 6. Employing Symmetry

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/example06.htm

**Contents:**
- Example 6. Employing Symmetry
- Suggested webcuts
- Final mesh

One technique for creating a symmetric mesh on a symmetric model is to mesh only half of the volume, then copy the mesh onto the other half. The following example employs this technique. This model at first appears quite simple, but it actually requires a good deal of webcutting to get a reasonable mesh that is not highly skewed.

CUBIT> webcut body 1 with plane xplane offset 0

CUBIT> webcut body 1 with cylinder radius 2.75 axis y

CUBIT> webcut body 1 3 with plane yplane offset 0

CUBIT> webcut body 1 with plane yplane offset -15

CUBIT> webcut body 1 6 4 with plane surface 64

CUBIT> webcut body 1 with plane surface 67

CUBIT> webcut body 5 with plane zplane offset 1.5

CUBIT> webcut body 11 with plane zplane offset -1.5

CUBIT> create vertex on curve 540 distance 2 from vertex 368

CUBIT> webcut body 4 with plane vertex 409 vertex 410 vertex 630

CUBIT> create vertex on curve 1093 distance 3 from vertex 646

CUBIT> webcut body 14 with plane vertex 570 vertex 569 vertex 647

This wedge shape webcut is a method of controlling skew in the final mesh.

CUBIT> unite body 5 11 12

CUBIT> unite body 4 13

CUBIT> delete vertex all

CUBIT> vol all size .5

CUBIT> surf 229 size .25

CUBIT> volume 5 scheme sweep source 229 target 230

CUBIT> volume 4 scheme sweep source surface 526 target 528

CUBIT> volume 14 scheme sweep source 543 target 541

CUBIT> mesh volume 14

CUBIT> webcut body 6 with plane surface 524

CUBIT> unite body 16 17

CUBIT> webcut body 8 with plane surface 524

CUBIT> webcut body 18 with plane surface 540

CUBIT> webcut volume 9 with plane zplane offset -3 rotate 5 about x

This is another effort to prevent skew in the final mesh

CUBIT> mesh volume 5 (swept around)

CUBIT> mesh volume 4 (mapped)

CUBIT> mesh volume 14 (swept top to bottom)

CUBIT> volume 15 scheme map

CUBIT> curve all in volume 15 size 0.5

CUBIT> mesh volume 15

CUBIT> volume 18 scheme tetprimitive

CUBIT> volume 18 interval 3

CUBIT> mesh volume 18

CUBIT> volume 9 scheme sweep source surface 579 601 target surface 592 rotate off

CUBIT> mesh volume 20

CUBIT> volume 6 scheme sweep source 569 target 570

CUBIT> volume 3 scheme sweep source 224 target 226

CUBIT> surf 224 226 scheme map

CUBIT> volume 19 scheme sweep source 543 target 586

CUBIT> mesh volume 19

CUBIT> volume 17 scheme sweep source 545 583 582 target 239

CUBIT> mesh volume 17

CUBIT> volume 8 scheme sweep source 574 597 601 target 241

CUBIT> volume 7 1 size 2

CUBIT> volume 7 1 scheme auto

CUBIT> volume 10 scheme sweep source 270 target 267

CUBIT> mesh volume 7 1

CUBIT> mesh volume 10

CUBIT> body all copy reflect x

The entire mesh is copied and reflected around the x axis during the last step. The advantage of symmetry in this example is that it cuts the decomposition in half, and it also ensures a perfectly symmetrical mesh.

---

## Example 8. Sweeping volumes with narrow angles and surfaces

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/decomposition/example08.htm

**Contents:**
- Example 8. Sweeping volumes with narrow angles and surfaces
- Suggested webcuts
- Final mesh

Narrow angles are a challenge for sweeping algorithms. In the next example, a well-placed webcut shaves off the end of the small angle to create an additional surface for the sweeping algorithm.

CUBIT> webcut volume 1 with sheet extended from surface 16

CUBIT> webcut volume 5 with plane surface 50

CUBIT> webcut volume 4 with plane surface 47

CUBIT> webcut volume 3 with sheet extended from surface 36

CUBIT> webcut volume 2 with plane surface 25

CUBIT> unite volume 3 9 7

CUBIT> webcut volume 5 with sheet extended from surface 13

CUBIT> webcut volume 5 with sheet extended from surface 69

CUBIT> webcut volume 4 with sheet extended from surface 13

CUBIT> webcut volume 4 with sheet extended from surface 69

CUBIT> webcut volume 5 with plane vertex 23 vertex 25 vertex 31

CUBIT> webcut volume 4 with plane vertex 23 vertex 25 vertex 31

CUBIT> webcut volume 16 with plane vertex 18 vertex 9 vertex 33

CUBIT> webcut volume 17 with plane vertex 18 vertex 9 vertex 33

CUBIT> webcut volume 6 with plane normal to curve 26 distance 0.6 from vertex 25

CUBIT> delete volume 20

CUBIT> webcut volume 8 with plane normal to curve 33 distance 0.6 from vertex 31

CUBIT> delete volume 8

CUBIT> unite volume 3 21 6

CUBIT> imprint volume all CUBIT> merge volume all CUBIT> volume all size 0.3 CUBIT> volume all scheme auto

CUBIT> volume 2 scheme sweep source 13 target 69

CUBIT> volume 2 sweep smooth auto

CUBIT> unmerge volume all

CUBIT> webcut volume 2 3 with plane zplane

CUBIT> webcut volume 3 with sheet extended from surface 154

CUBIT> webcut volume 23 with sheet extended from surface 153

CUBIT> webcut volume 11 with plane zplane noimprint nomerge

CUBIT> imprint volume all

CUBIT> merge volume all

CUBIT> volume 11 scheme sweep source surface 221 target surface 222 rotate off

CUBIT> volume 11 sweep smooth auto

CUBIT> volume 28 scheme sweep source surface 222 target surface 221 rotate off

CUBIT> volume 28 sweep smooth auto

CUBIT> volume 22 scheme sweep source surface 176 target surface 179 rotate off

CUBIT> volume 22 sweep smooth auto

CUBIT> volume 2 scheme sweep source surface 173 target surface 170 rotate off

CUBIT> volume 2 sweep smooth auto

CUBIT> volume 24 scheme sweep source surface 204 target surface 202 rotate off

CUBIT> volume 24 sweep smooth auto

CUBIT> volume 25 scheme sweep source surface 205 target surface 207 rotate off

CUBIT> volume 25 sweep smooth auto

CUBIT> volume 26 scheme sweep source surface 214 target surface 216 rotate off

CUBIT> volume 26 sweep smooth auto

CUBIT> volume 27 scheme sweep source surface 217 target surface 219 rotate off

CUBIT> volume 27 sweep smooth auto

CUBIT> volume 3 scheme sweep source surface 197 187 target surface 200 rotate off

CUBIT> volume 3 sweep smooth auto

CUBIT> volume 23 scheme sweep source surface 212 193 target surface 210 rotate off

CUBIT> volume 23 sweep smooth auto

CUBIT> volume all scheme auto

CUBIT> volume all size 0.2

CUBIT> mesh volume all

The final mesh is shown below.

---

## GUI Basic Tutorial

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/gui/overview.htm

**Contents:**
- GUI Basic Tutorial
- Overview

This tutorial demonstrates the use of CUBIT to create and mesh a brick with a through-hole. The primary steps in performing this task are:

The geometry for this tutorial is a brick with a cylindrical hole in the center, shown in the figure below. This figure also shows the curve and surface identification (ID) numbers, which are referenced in the command lines options shown with each step. The final meshed body is shown in the next figure.

Geometry for Brick with Cylindrical Hole

Generated Mesh for Brick with Cylindrical Hole

---

## Power Tools GUI Tutorial

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/overview.htm

**Contents:**
- Power Tools GUI Tutorial
- Overview

This tutorial demonstrates using the Power Tools on the CUBIT GUI for geometry decomposition and cleanup. The following features will be covered:

Each of these steps is described in detail in the following sections. For this tutorial you will need to have a basic understanding of the CUBIT GUI functionality, including how to select entities, maneuver in the graphics window, operate the Control Panel, and use toolbars. If you have not already done so, we recommend completing the Basic Tutorial first. The following image shows the geometry that will be used for this tutorial.

NOTE: Many of the steps in this tutorial include operations on specific entities which are identified by ID. When the solid modeling kernal is updated in Cubit the ID space may change. As such, you may not be able to rely on the IDs specified in this tutorial. Please look at the associated graphics to determine which entity/ID is being referred to.

---

## Power Tools GUI Tutorial Step 10

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_10.htm

**Contents:**
- Power Tools GUI Tutorial Step 10
- Step 10: Compositing Surfaces

Composite surfaces are adjacent surfaces that have been merged into one surface. Composite surfaces are created using Virtual Geometry, which is a built-in geometry kernel that sits on top of the existing geometry, and does not change the underlying geometry definition. Virtual geometry has the added advantage of being reversible. It can be removed after meshing. The general purpose for using composite surfaces is to deconstrain the mesh. For example, compositing two surfaces will remove the requirement that nodes be placed on the curve between the surfaces. Composite surfaces will be used in this example to facilitate the sweeping algorithm.

No volumes are listed as automatically meshable. In the graphics window, red indicates that the volume scheme has not been set. Green indicates that the scheme has been set.

The Geometry-Surface-Modify-Composite menu will open on the Control Panel.

The two surfaces should appear merged.

Repeat these steps with the opposite side.

Check to see that the surfaces have been composited and that your graphics window looks like the following image.

Finally, surfaces 11, 25, and 35 (shown below) need to be composited.

Use the command panel to choose surfaces for the composite command.

Press the apply button and check the results in the graphics window.

---

## Power Tools GUI Tutorial Step 11

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_11.htm

**Contents:**
- Power Tools GUI Tutorial Step 11
- Step 11: Meshing the Model

Use the Mesh Power Tools to apply schemes to the remaining volumes.

All of the schemes have now been set with a sweeping algorithm. The model is ready to be meshed. All volumes should appear green in the graphics window.

Select Volume as the entity, and Intervals as the Action.

The graphics window should appear as follows, with the mesh size increments highlighted on all of the curves in the model.

There is no need to press the Apply Scheme button since the scheme have already been set in the Meshing Tools.

The final mesh should look like this:

Congratulations! You have just completed the Power Tools Tutorial. Click on the arrow to return to the Tutorial home.

---

## Power Tools GUI Tutorial Step 1

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_01.htm

**Contents:**
- Power Tools GUI Tutorial Step 1
- Step 1: Import the Geometry

Begin by opening a new session of CUBIT. To complete this tutorial, you will need to download the ACIS file that contains the geometry definition.

Your graphics window should now appear as follows:

---

## Power Tools GUI Tutorial Step 2

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_02.htm

**Contents:**
- Power Tools GUI Tutorial Step 2
- Step 2: Analyze the Geometry

Many geometries that are imported from other solid modeling software contain inconsistencies or small gaps that can cause meshing to fail. These problems are the result of differences in tolerances, file transfer loss, or inherent limitations in the parent system. In other instances, the geometry has no inconsistencies, but may be unsuitable for meshing because of topology such as small angles, overlap, or features smaller than the desired meshing size. The geometry analysis tool will analyze the volumes and return a list of suspected problems. To see a list of analysis options, click the "Show Options" box below the Analyze button.

Many of these problems can be fixed using the tools on the Power Tools menu. These include Split Surface, Heal, Tweak, Remove, Merge, Composite, Collapse Angle, Collapse Curve, and Collapse Surface. Many of these tools will be demonstrated in this tutorial.

After the Analyze Button is pushed, display area will appear as shown above. There are four suspected problems with this geometry: Curves with Small Angles, Blend Surfaces, Close Loops, and Badly Defined Geometry. The numbers in parentheses indicate the number of occurrences of this problem in the model. Clicking on the + sign by each label will list the CUBIT entities by ID with this problem. Clicking on the + sign by each entity will cause that entity's children or parents to be listed (depending on the entity and the type of geometry test). See documentation on Geometry Repair for more information about the display window. Clicking on the name of an entity will highlight that entity in the graphics window.

Observe that this vertex is highlighted in the graphics window.

The graphics window should look like this:

The image should now be reset to the previous graphics state.

You can experiment with some of the other options in the top half of the right click menu. They are:

The graphics window may also be reset by pressing the reset graphics button on the menu.

---

## Power Tools GUI Tutorial Step 3

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_03.htm

**Contents:**
- Power Tools GUI Tutorial Step 3
- Step 3: Healing the Geometry

The Geometry Repair Tool does not execute any geometry clean-up commands directly, but directs you to the place on the Control Panel where this function can be executed. The following menu will appear on the Control Panel. Notice that the id of the owning body has already been pasted into the input window.

The output window on the CUBIT GUI should appear with the following message. You may have to scroll to see the whole thing. The percentage before and after healing are 97% to 100%. Healing has been successful.

Run the geometry analysis test again to guarantee that all bad geometry has been removed.

---

## Power Tools GUI Tutorial Step 4

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_04.htm

**Contents:**
- Power Tools GUI Tutorial Step 4
- Step 4: Mesh Power Tools

Volume 1 will appear under the "No Scheme Set" heading.

The graphics window should look like this with Volume 1 highlighted in red. Using this graphics feature, all volumes that are meshable will be highlighted in green, and all volumes that are not currently meshable will be highlighted in red.

---

## Power Tools GUI Tutorial Step 5

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_05.htm

**Contents:**
- Power Tools GUI Tutorial Step 5
- Step 5: Splitting Filleted Surfaces

A blend surface is a transitional surface that connects two orthogonal planes, also known as a fillet. Blend surfaces can be problematic in meshing because there is no clear transition between the two orthogonal surfaces, making sweeping or mapping algorithms difficult. The Split Surface function divides these blend surfaces (or any surface) into two distinct surfaces.

The graphics window should look like this:

The Geometry-Surface-Modify-Split Menu will appear on the Control Panel. Make sure the Surface id is input in the window.

The blue line shows where the surface will be split.

The surface should now appear split.

---

## Power Tools GUI Tutorial Step 6

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_06.htm

**Contents:**
- Power Tools GUI Tutorial Step 6
- Step 6: Web Cutting

Web cutting is this process of dividing volumes into sweepable regions by cutting with a plane. For this exercise, you will use the curves that were just created with the split surface command to cut the volume.

In order to visualize the process more clearly, switch to the isometric view.

The web cutting menu is located under Geometry-Webcut-Volume on the Control Panel.

The following image shows the entity ids that will be used to webcut the volume. Select entities with the mouse by clicking on them.

A blue preview plane should appear in the following position. Check to make sure that your model looks the same.

The volume has now been split into two volumes. Volume 2 is shown in yellow.

Repeat these steps with the other side of the part. The Volume and Curve ids will remain the same.

The final webcut volume should look like this:

---

## Power Tools GUI Tutorial Step 7

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_07.htm

**Contents:**
- Power Tools GUI Tutorial Step 7
- Step 7: Removing Small Surfaces

Some surfaces are too small for analysis and should be removed from the model. In this example, Surface 15 and Surface 17 may fall into that category, assuming that the distance between curves on these surfaces is smaller than the desired final mesh size. You can remove these surfaces by extending adjacent surfaces until they intersect.

You will notice that a new category has appeared labeled Overlapping Surfaces. This is because there are two new surfaces created for each of the webcuts that overlap a surface on the original body. This can be removed using the Imprint/Merge function which will be explained in Step 9.

The Control Panel will appear under the Geometry-Surface-Modify- Remove heading. The Surface id should appear in the input window.

The small surface no longer appears.

Surface 15 is shown highlighted in the following image.

Reset the Zoom to show the entire model.

---

## Power Tools GUI Tutorial Step 8

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_08.htm

**Contents:**
- Power Tools GUI Tutorial Step 8
- Step 8: Tweaking Surfaces

Tweaking is the process of deleting, moving, or offsetting, surfaces and extending or trimming adjacent surfaces to fill in the gaps. Tweaking is useful for eliminating gaps between components, simplifying geometry or changing the dimensions of an entity. Tweaking will be used in this example to decrease the radius of the upper cylinder.

Begin by reanalyzing the geometry.

There should be 1 entry under the "Close Loops" category for Surface 38. A close loop (pronounced KLOS) is a surface which has two loops that are within some small distance of each other at their closest points. The parameter for distance is the square of the shortest edge length parameter.

The Geometry-Surface-Modify-Tweak will open on the Control Panel as shown below.

Surface 16 is shown highlighted below.

The offset value is a percentage of the current size. Entering -0.9 will decrease the radius by 10 percent.

The graphics window should now look like this. Notice that the radius of the cylinder has shrunk inward, increasing the gap between the edges on Surface 41.

---

## Power Tools GUI Tutorial Step 9

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/power_tools/step_09.htm

**Contents:**
- Power Tools GUI Tutorial Step 9
- Step 9: Imprint/Merge

Imprinting is the process of projecting curves from one surface onto an overlapping surface. Merging is the process of taking two overlapping surfaces and merging them into one surface shared by two volumes, creating non-manifold geometry. Both imprinting and merging are necessary to make adjacent volumes have identical meshes at their intersection. Imprinting and merging is almost always necessary after webcutting.

You will not notice any visible changes in the graphics window after imprint/merge operations, but results of the operations will be printed in the output window. Confirm that both surfaces have been merged by reading the output in the graphics window (You may have to scroll to see all of the results)

You can return to the Power Tools menu to see that the Close Loops and Overlapping Surfaces are gone.

The display window will now read "Nothing Found" to indicate that are no geometry tests that fail.

---

## Step-By-Step Tutorials

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/step_by_step_tutorials.htm

**Contents:**
- Step-By-Step Tutorials
- Additional Tutorials

The following activity demonstrates the basics of using CUBIT to generate and mesh a geometry. By following these steps, you will become familiar with the basics of the command-line and GUI interfaces without stopping for detailed explanations. All the commands introduced in this tutorial are documented in subsequent chapters on this manual.

Here are a few tips for the examples in the tutorial:

cubit> <Your commands go here>

If you do not have the Graphical User Interface (GUI) version of CUBIT, follow the steps in the right column below, otherwise, proceed through the steps on the left:

ITEM Tutorial - A tutorial on the new ITEM wizard.

Power Tools GUI Tutorial - A tutorial on geometry decomposition and cleanup using the Power Tools on the new CUBIT GUI.

Decomposition Tutorial - A series of webcutting hints and suggestions for creating sweepable volumes on various models.

Geometry Cleanup Process Flow - A flowchart on geometry cleanup and defeaturing.

---
