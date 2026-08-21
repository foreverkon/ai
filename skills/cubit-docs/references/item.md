# Coreform-Cubit-Docs-Skill_Docs - Item

**Pages:** 18

---

## Blend Surfaces

**URL:** https://coreform.com/cubit_help/item/clean_up/blend_surfaces.htm

**Contents:**
- Blend Surfaces

Blend surfaces are common in solid model meshing problems. A blend surface, also known as a fillet or chamfer, is problematic for sweeping algorithms which have trouble assigning vertex types on blend surfaces. While blend surfaces present a challenge for meshing applications, there are many tools within ITEM to help guide the user through possible solutions.

Diagnostic: Blend surfaces are detected by looping over the curves on a surface and examining the angles, surface normals, and curvature of curves and adjacent surfaces.

Solutions: The current solution to blend surfaces is to remove the surface and attempt to extend adjacent surfaces to fill in the gap. An example of blend surfaces that have been removed is shown below. This is useful for models which can be simplified without losing important topology.

Figure 1. A volume which has been simplified by removing blend surfaces.

---

## Determining an Appropriate Merge Tolerance

**URL:** https://coreform.com/cubit_help/item/clean_up/merge_tolerance.htm

**Contents:**
- Determining an Appropriate Merge Tolerance
- Opening the Merge Tolerance Panel
- Estimating Merge Tolerance with Small Feature Size
- Fine Tuning the Merge Tolerance
- Setting the Merge Tolerance

Determining the appropriate merge tolerance for a model can be essential for creating conformal meshes on some models. The merge tolerance is a value that identifies at which distance different entities can be considered the same entity. Many entities will fail to merge because of widespread geometry tolerance or alignment problems that are either too difficult, time-consuming or even impossible to resolve. Specifying a merge tolerance that is larger than these small discrepancies allows the user to account for geometry that is misaligned. But specifying a merge tolerance that is too large can combine features the user wishes to keep, and possibly corrupt the model. The ideal merge tolerance should be smaller than the smallest feature, but larger than the biggest gap or misalignment that cannot be resolved. Since it is not always a simple task to determine either of these features, the ITEM workflow provides a diagnostic tool designed to guide the user to find the small misalignments that may lead to merge problems. It then presents possible solutions to fix these problems, or the ability to change the merge tolerance to ignore them.

To open the merge tolerance tool from the ITEM Wizard, click on Prepare Geometry->Connect Volumes->Imprint and Merge. Then click on the button with three dots next to the Merge Tolerance input field.

Figure 1. How to open the merge tolerance panel

Figure 2. The Merge Tolerance Diagnostic Panel

Since the merge tolerance must be smaller than the smallest feature in the mesh, the best place to start is by finding the smallest feature and using that value to create an estimate for the merge tolerance. To find the smallest feature, click on the small button with three dots next to the input box for Small Features.

Note: The small feature checks will not find misalignments between different volumes- it will only list vertex-vertex pairs and vertex-curve pairs on the same volume. The small feature size is used on the merge tolerance panel to find an initial estimate for the merge tolerance.

After determining the smallest feature size, click on the Estimate Merge Tolerance button to come up with a rough estimate for the merge tolerance. It is important to note that this is only an estimate. After an initial estimate is made, it can be fine tuned using the Fine Tune Merge Tolerance tool.

In the fine tune merge tolerance area, the user may search for vertex-vertex, vertex-curve, and vertex-surface pairs that are within user-specified ranges. This includes checks between entities on different volumes. This allows the user to determine if the merge tolerance he/she has determined will capture all of the merges he/she intends. The user can check/uncheck which pairs to search for and what range to look in. The results from the search will show up in the window below and the user can select the results, right click on it, and choose Draw with Volumes to zoom into that pair of features. For vertex-vertex pairs there may be tweak solutions presented to the user in the list box below for fixing the problems.

The Apply button next to Estimated Merge Tolerance edit field is used to take the estimated merge tolerance and use it to set the merge tolerance in CUBIT by issuing the Merge Tolerance <val> command.

---

## Determining the Small Feature Size

**URL:** https://coreform.com/cubit_help/item/clean_up/small_features.htm

**Contents:**
- Determining the Small Feature Size
- Why doesn’t the list include small gaps between volumes?

The smallest feature size is a value that represents the size of the smallest detail in the volume that the user wants to include in the final mesh. Any details that are smaller than this size should be removed from the model before completing the other steps of the meshing process. Small details can result from a variety of different reasons. Sometimes the model contains excessive detail that the user does not need. Other times, small features such as extra curves are created during import to account for a mismatching topology. Still other times, the small features are the result of webcutting or other decomposition methods. Ideally there should be a minimum threshold at which the user decides to keep all features above the given size, and remove the rest. The smallest feature size is used for other diagnostic tools, so selecting an appropriate feature size is important for other steps in the mesh generation process.

After the Find Small Features button is pressed, Cubit lists the 10 closests vertex-vertex and vertex-curve pairs. The pairs are listed in the display window from smallest to largest. To see more pairs, change the search parameter in the input box. To visualize each pair, the user can right click on a feature and select the Draw Pair with Volumes option. After determining the smallest feature size the user can enter it in the edit field at the bottom of the panel and it will be used in later calculations. The user can also right click on one of the pairs in the list and choose Use as smallest feature to populate the edit field at the bottom of the panel.

The smallest feature check is only searching over vertex-vertex and vertex-curve pairs in the same volume. Small gaps and misalignments are not included in this list. The purpose of the small feature diagnostic panel is to search for features that need to be removed prior to meshing. A feature is an entity such as a small curve or sliver surface that exists on a single volume which must be resolved by the mesh. A gap or misalignment is two entities that should be coincident, but are not, due to translation or other problems. Gaps and misalignments may not hinder mesh generation on a given volume, but they do prevent proper imprinting and merging.

The imprint/merge, merge tolerance, and overlapping volume panels contain diagnostics that check for misalignment problems. The purpose of those diagnostics is to enable imprinting and merging of a volume with small misalignments.

Note: The smallest feature size is used as a metric on the merge tolerance page, but it is only used to get an initial estimate for the merge tolerance. Small feature size and merge tolerance represent different metrics, and should not be confused.

In Figure 1, the small feature size diagnostic finds small features with lengths of 0.707, 0.15 and 0.25. The user may decide that the smallest feature he or she wishes to keep is the one at the 0.25 size. If he sets the small feature size to 0.25, the other features will be flagged as small curves and surfaces on the Small Features page. They can then be removed using tweaking and other geometry clean-up commands. If he sets the small feature size to 0.707, none of the features will be flagged as small features.

In addition to the features shown, this model contains two vertices that are slightly misaligned due to geometry translation problems. The nearly coincident vertices are not listed on the small features list because the vertices lie on different volumes. To find these near coincident vertices, the user would use the merge tolerance panel.

Figure 1. Small Features and Overlap on a Model

---

## Forced Sweepability

**URL:** https://coreform.com/cubit_help/item/clean_up/forced_sweep.htm

**Contents:**
- Forced Sweepability

In some cases, decomposition alone is not sufficient to provide the necessary topology for sweeping. The forced sweepability capability attempts to force a model to have sweepable topology given a set of source and target surfaces. The source-target pairs may have been identified manually by the user, or defined as one the solutions from the sweep suggestion algorithm described above. All of the surfaces between source and target surfaces are referred to as linking surfaces. Linking surfaces must be mappable or submappable in order for the sweeping algorithm to be successful. There are various topology configurations that will prevent linking surfaces from being mappable or submappable.

Diagnostics: The first check that is made is for small curves. Small curves will not necessarily introduce topology that is not mappable or submappable but will often enforce unneeded mesh resolution and will often degrade mesh quality as the mesh size has to transition from small to large. Next, the interior angles of each surface are checked to see if they deviate far from 90 multiples. As the deviation from 90 multiples increases the mapping and submapping algorithms have a harder time classifying corners in the surface. If either of these checks identify potential problems they are flagged and potential solutions are generated.

Solutions: If linking surface problems are identified ITEM will analyze the surface and generate potential solutions for resolving the problem. Compositing the problem linking surface with one of its neighbors is a current solution that is provided. ITEM will look at the neighboring surfaces to decide which combination will be best. When remedying bad interior angles the new interior angles that would result after the composite are calculated in order to choose the composite that would produce the best interior angles. Another criterion that is considered is the dihedral angle between the composite candidates. Dihedral angles close to 180 are desirable. The suggested solutions are prioritized based on these criteria before being presented to the user. Figure 1 shows an example of a model before and after running the forced sweepability solutions. The top and bottom of the cylinder were chosen as the source and target surfaces respectively.

Figure 1. Non-submappable linking surface topology is composited out to force a sweepable volume topology

---

## How to Use the ITEM Wizard

**URL:** https://coreform.com/cubit_help/item/how_to.htm

**Contents:**
- How to Use the ITEM Wizard
- The ITEM Workflow
- Using an ITEM Panel
  - Task panels that link to other ITEM panels
  - Task Panels that Link to Control Panels
  - Set-up Panels
  - Diagnostic Panels
- Undo Button
- Magic Mesh Button
- Getting Help

The Immersive Topology Environment for Meshing (ITEM) is a wizard-like environment that guides the user through the mesh generation process from geometry definition to export. ITEM was designed to provide a step-by-step set of tools to help new users generate a mesh with very little previous knowledge of the CUBIT program. But ITEM is also flexible enough to accomodate advanced users who want to use a more iterative approach, or who just want to use ITEM for a specific tool or panel.

The main ITEM task page is shown below. To access this page, click on the "wizard hat" icon from the Power Tools window.

The main item tasks are shown both in the text window, and also along the sidebar. The icons in the sidebar are available from any of the ITEM panels. It is acceptable to jump to different tasks during the process, although beginning users may just want to follow the steps in order. To get to the main task page, click on the Task icon on the sidebar during any step in the process.

Many meshing tasks require an iterative approach to the mesh generation process. For your convenience, if you do click on one of the task buttons from a different panel, it will take you to the last visited panel in that section. For example, if you are on the mesh generation page, and you click on the prepare geometry section, it will take you to the last page you visited in the prepare geometry section.

There are two help links at the bottom of the main task page. The first link will open this document which describes the general ITEM process and how to use the panels. This page is only accessible from the main task page. The second link opens the main ITEM documentation which describes each process in the ITEM mesh generation process in detail. This document can be accessed from any of the ITEM panels.

To proceed through the ITEM panels you must either click on a task or click on the "Done" button at the bottom of each page. There is no "Back" button on the ITEM interface. But in most cases, clicking the "Done" button works like a "Back" button.

The item panels are designed to be self-explanatory, with plenty of documentation on each page, and access to more help if needed. However, it does help to be generally familiar with the main types of panels.

In other cases, the list of tasks is a presents a list of choices, from which you will only select one option. The Import Geometry Page shown below is such an example. It gives a list of different geometry import/creation options and you just select one of the alternatives.

Prepare Geometry ITEM Panel

Import Geometry ITEM Panel

A few of the ITEM task panels will provide links to existing control panel topics. Clicking on a link from one of these panels will NOT open a new panel, but will open the corresponding control panel. The Define Boundary Conditions page is an example of this type of panel.

Define Boundary Conditions Panel

A set-up panel is used to provide input or set-up options for your model. The most prominent set-up panel is the Set-up FEA Model page which is used to define mesh budget, element type, and element size. Another set-up page is the Define Metrics page under the Validate Mesh task. This panel is used to define quality metrics for your model. These panels provide useful information for the diagnostics used in other panels.

Setup FEA Model Panel

The Small Features Panel shows an example diagnostic panel in ITEM.

Remove Small Features Diagnostic Panel

The Undo button allows you to reverse the most recent command. To enable the Undo button, click on the "Enable Undo" option from the Edit menu. The undo button works by saving information about your model after each step. For large or complex models, this can be time consuming, so you may need to disable the undo feature. Additionally, not all commands are enabled for undo. Many of the graphics and meshing commands, and various default settings are not included. Within ITEM, many commands are bundled into a single button click. Clicking undo will attempt to reverse all of the executed commands. See the command line window for the results of the undo command.

If for any reason, Cubit is unable to complete these steps without further user intervention, the process will stop and the user will directed to continue with the ITEM workflow. For simple geometries, executing the magic mesh button at this phase of the workflow may be all that is necessary to completely define a good quality mesh. For other more complex geometry, considerable user intervention may be required.

The magic mesh button may be executed at any time during the ITEM workflow by selecting the button at the top right corner of the ITEM panel. Once the user has visited the various panels of the ITEM interface to provide user intervention, the automatic execution of the appropriate operations will not longer be attempted.

There are several ways to get help from within the ITEM interface. Most of these have already been discussed, but they are listed here again for reference:

---

## ITEM Tutorial

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/item/overview.htm

**Contents:**
- ITEM Tutorial
- Overview

This tutorial will demonstrate the use of the Immersive Topology Environment for Meshing (ITEM) to create a finite element mesh. ITEM is a wizard-like environment that guides a user through a typical mesh generation process from import to export. Each page in the ITEM workflow is linked to other pages, and one can easily move around in the environment by clicking on links on each page. Most of the pages contain diagnostic tools that search the model for specific geometry or mesh-related issues. Clicking on a entity in the ITEM output window will then generate specific command suggestions to resolve the problem. The following topics are included in this tutorial:

---

## ITEM Tutorial Step 1

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/item/step01.htm

**Contents:**
- ITEM Tutorial Step 1
- Step 1: Import Geometry

In most cases, clicking the Done button also acts like a "Back" button. Clicking Done will return the user to the previous page while preserving any changes made on that page.

---

## ITEM Tutorial Step 3

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/item/step03.htm

**Contents:**
- ITEM Tutorial Step 3
- Step 3: Remove Small Features

In addition to setting the small feature size, the smallest feature size panel of itself is a useful tool for visualizing and grouping small features. Sometimes it is useful just to have a list of the smallest features and a means of quickly visualizing and grouping them.

---

## ITEM Tutorial Step 4

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/item/step04.htm

**Contents:**
- ITEM Tutorial Step 4
- Step 4: Connect Volumes

The next step in the mesh generation process is to merge all shared curves and surfaces. This is necessary so that adjacent volumes can shared boundary meshes. For most geometries, this step presents no major complications. But in many cases, misalignments, tolerance problems, or other cleanup operations can prevent proper merging. The ITEM panel is designed to guide users through imprint/merge problems.

No problems should appear on the list, signifying that imprinting and merging has most likely been successful. There are several diagnostic tools on this page that help to determine if imprint/merging has been successful. These include:

All of these diagnostics could be run at any time but the results are most meaningful after an imprint/merge operation.

---

## ITEM Tutorial Step 5

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/item/step05.htm

**Contents:**
- ITEM Tutorial Step 5
- Step 5: Build a Meshable Topology

The next step in the mesh generation process can be one of the most challenging. Building a meshable topology involves decomposing an assembly into meshable parts. For sweeping, this means decomposing it into volumes composed of many-to-one and one-to-one sweepable parts. Each decomposed volume is further constrained because it needs to be able to share boundary meshes on merged surfaces. Since the number of possible decomposition strategies are numerous, it is not yet possible to automatically decompose most models. Instead, the ITEM framework seeks to provide possible decomposition options to the user, which they can be easily executed (and if necessary, quickly undone).

---

## ITEM Tutorial Step 6

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/item/step06.htm

**Contents:**
- ITEM Tutorial Step 6
- Step 6: Meshing the Geometry

The actual mesh generation process is usually quite iterative. Rare is the case where meshing succeeds perfectly on the first try, even when all volumes are "meshable". Even if it does succeed, it is usually constrained by areas of poor quality elements. ITEM was designed to help users navigate the iterative mesh generation process. When meshing fails, the mesh generation panel helps to explain common error messages and suggest possible strategies for getting a model to mesh.

The mesh density didn’t adequately capture the mesh features. To decrease the mesh size, return to the setup panel.

---

## ITEM Tutorial Step 8

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/item/step08.htm

**Contents:**
- ITEM Tutorial Step 8
- Step 8: Define Boundary Conditions

Exodus boundary conditions are specified as generic blocks, nodesets, and sidesets. Clicking on a boundary condition type on the ITEM panel will open the corresponding command panel.

---

## ITEM Tutorial Step 9

**URL:** https://coreform.com/cubit_help/step_by_step_tutorials/item/step09.htm

**Contents:**
- ITEM Tutorial Step 9
- Step 9: Export the Exodus Model

Cubit primarily supports the Exodus format for mesh export. But there are also limited export abilities for other formats as well. For a list of export capabilities see Exporting the Finite Element Model

Congratulations on completing the ITEM tutorial. Click on the arrow to return to the main tutorial page.

---

## Recognizing Nearly Sweepable Regions

**URL:** https://coreform.com/cubit_help/item/clean_up/source_target.htm

**Contents:**
- Recognizing Nearly Sweepable Regions

The purpose of geometry operations such as decomposition is to transform an unmeshable region into one or more meshable regions. However, even the operations suggested by the decomposition tool can degenerate into guesswork if they are not performed with a specific purpose in mind. Without a geometric goal to work toward, it can be difficult to recognize whether a particular operation will be useful.

Incorporated within the proposed ITEM environment are algorithms that are able to detect geometry that is nearly sweepable, but which are not fully sweepable due to some geometric feature or due to incompatible constraints between adjacent sections of geometry. By presenting potential sweeping configurations to the user, ITEM provides suggested goals to work towards, enabling the user to make informed decisions while preparing geometry for meshing.

Unlike the decomposition solutions presented in the previous section, the purpose of recognizing nearly sweepable regions is to show potential alternative source-target pairs for sweeping even when the autoscheme tool does not recognize the topology as strictly sweepable. When combined with the decomposition solutions and the forced sweepability capability described later, it provides the user with an additional powerful strategy for building a hexahedral mesh topology.

Diagnostics: In recognizing nearly sweepable regions, the diagnostic tool employed is once again the autoscheme tool described in [White, 00]. Volumes that do not meet the criteria defined for mapping or sweeping are presented to the user. The user may then select from these volume for which potential source-target pairs are computed.

Solutions: The current algorithm for determining possible sweep configurations is an extension of the autoscheme algorithm described in [White, 00]. Instead of rejecting a configuration which does not meet the required sweeping constraints, the sweep suggestion algorithm ignores certain sweeping roadblocks until it has identified a nearly feasible sweeping configuration. The suggestions are presented graphically, as seen in Figure 1. In most cases, the source-target pairs presented by the sweep suggestion algorithm are not yet feasible for sweeping given the current topology. The user may use this information for further decomposition or to apply solutions identified by the forced sweepability capability described next. The sweep suggest algorithm also provides the user with alternative feasible sweep direction solutions as shown in Figure 1. This is particularly useful when dealing with interconnected volumes where sweep directions are dependent on neighboring volumes.

Figure 1. (a) ITEM displays the source and target of a geometry that is nearly sweepable. The region is not currently sweepable due to circular imprints on the side of the cylinder. (b) Alternative feasible sweep directions are also computed.

---

## Resolving Problems with Conformal Assemblies

**URL:** https://coreform.com/cubit_help/item/clean_up/conformal.htm

**Contents:**
- Resolving Problems with Conformal Assemblies
- Resolving Misaligned Volumes with Manage Gaps/Overlaps Tool
- Resolving Misaligned Volumes with Near Coincident Vertex Checks
- Correcting Merge Problems

Where more than a single geometric volume is to be modeled, a variety of common problems may arise that must be resolved prior to mesh generation. These are typically a result of misaligned volumes defined in the CAD package or problems arising from the imprint and merge operations in the meshing package. ITEM addresses some of the same problems by allowing the option for user interaction as well as full automation using the CAD geometry representation. The proposed environment utilizes two main diagnostics to detect potential problems: the misalignment check, and the overlapping surfaces check. Associated with both of these are solutions that are specific to the entity and from which the user may preview and select to resolve the problem.

The Manage Gaps/Overlaps Tool within the geometry cleanup area of ITEM allows the user to quickly search an assembly for gaps and overlaps between assembly components. The search criteria for gaps is a tolerance specified by the user and defines the maximum gap between components to look for. A gap angle can also be specified which specifies how "parallel" two entities must be to be considered in the gap check. The overlap check simply asks Cubit to see if any of the volumes are overlapping and doesn't require a tolerance from the user. The results are displayed in a list of pairs of volumes. The user can right-click on these pairs and tell Cubit to draw the pair. A useful graphical depiction of the gap or overlap will be displayed. When the user clicks on a pair in the list a set of solutions for fixing the gap or overlap will also be displayed below in a separate list. The user can select a solution and click the "Execute" button to execute it. The gap solutions are either a surface "tweak" operation and the overlap solution can be either a tweak operation or a Boolean operation to remove the overlap. This tool provides a powerful way to quickly work through the assembly and fix gaps and overlaps.

When pairs of vertices are found that are slightly out of tolerance, the current solution is to move one of the surfaces containing one vertex of the pair to another surface containing the other vertex in the pair. Moving or extending a surface is known as tweaking.

Figure 1. Example of a solution generated to correct misaligned volumes using the tweak operator

The result of this procedure will be a list of possible solutions that will be presented to the users. They can then graphically preview the solutions and select the one that is most appropriate to correct the problem.

The merge operation is usually performed immediately following imprinting and is also subject to occasional tolerance problems. In spite of correcting misalignments in the volume, the geometry kernel may still miss merging surfaces that may occupy the same space on adjacent volumes. If volumes in an assembly are not correctly merged, the subsequent meshes generated on the volumes will not be conformal. As a result, it is vital that all merging issues be resolved prior to meshing. The ITEM environment provides a diagnostic and several solutions for addressing these issues.

An overlapping surface check is performed to diagnose the failed sharing of topology between adjacent volumes. In contrast to the misalignment check, the check for overlapping surfaces is performed after the imprinting and merging operations. The overlapping surface check will measure the distance between surfaces on neighboring volumes to ensure that they are greater than the merge tolerance apart. Pairs of surfaces that failed to merge and that are closer than the merge tolerance are flagged and displayed to the user as potential problems.

A test for nonmanifold curves and vertices is also performed after imprinting and merging to find geometry that was not merged correctly. The test for nonmanifold curves is looking for curves that are merged, but do not share merged surfaces. Similarly, the test for nonmanifold vertices is looking for merged vertices that do not share any merged curves. Another test for floating volumes is performed to identify volumes that are not attached to any other entities.

If imprinting and merging has been performed and a subsequent overlapping surface check finds overlapping surface pairs, the user may be offered three different options for correcting the problem: force merge, tolerant imprint of vertex locations and tolerant imprint of curves.

If the topology for both surfaces in the pair is identical, the force merge operation can generally be utilized. The merge operation will remove one of the surface definitions in order to share a common surface between two adjacent volumes. Normally this is done only after topology and geometry have been determined to be identical, however the force merge will bypass the geometry criteria and perform the merge. Figure 2 shows a simple example where the bounding vertices are identical but the surface definitions are slightly different so that the merge operation fails. Force merge in this case would be an ideal choice.

Figure 2. Example where the merge operation will fail, but force merge will be successful

The force merge operation is presented as a solution where a pair of overlapping surfaces are detected and if any of the following criteria are satisfied:

Individual vertices may need to be imprinted in order to accomplish a successful merge. The solution of imprinting a position x,y,z onto surface A or B is presented to the user if the following criteria is met

Figure 3. Curve on surface A was not imprinted on surface B due to tolerance mismatch. Solution is defined to detect and imprint the curve

In some cases one or more curves may not have been correctly imprinted onto an overlapping surface which may be preventing merging. This may again be the result of a tolerance mismatch in the CAD translation. If this situation is detected a tolerant imprint operation may be performed which will attempt to imprint the curve onto the adjacent volume. Figure 3 shows an example where a curve on surface A is forced to imprint onto surface B using tolerant imprint, because it did not imprint during normal imprinting. The solution of a curve of surface A to be imprinted onto surface B may be presented to the user if all 3 of the following conditions are satisfied:

---

## Setting up the Finite Element Model

**URL:** https://coreform.com/cubit_help/item/set-up.htm

**Contents:**
- Setting up the Finite Element Model

Once the geometry to be meshed has been imported or created, the first step to defining the mesh is to set up the model. Basic parameters that are needed through the rest of the ITEM workflow are defined at this stage. Subsequent diagnostics and workflow may change based on how the model is initially set up.

Either a hexahedral or tetrahedral element shape may be selected. The meshing algorithm used to mesh the volumes will change based on this setting. Specific element characteristics such as the order of the element (i.e. TET10, HEX20) may be specified at a later time. The steps that will be displayed in the workflow will change based on the element type that is selected.

The number of elements or average size of the elements is an important aspect of defining your analysis model. Geometric features that are considerably smaller than the average element size, in most cases should be ignored since the mesh resolution will not be able to adequately capture them. Defining the element size at this point in the workflow permits subsequent diagnostic tests and operations to have a relative measure of what is “small”. More detailed sizing attributes such as biasing and geometry-adaptive sizing may be defined later in the ITEM workflow.

One of three different mechanisms may be used to define the size, element budget, element size and mesh density. Each of these values is dependent on the other. As a result, changing one value will automatically change the other.

Element Budget: This value is an approximate number of elements that should be generated in the entire model. The element budget for hexahedra, Nhex, is related to the element size, esize, by the following relationship:

Where Vmodel is the geometric volume of the solid model. The element budget for tetrahedra vs. hexahedra is approximately 1:7. That is, for an equivalent edge length, a tetrahedral mesh will contain roughly seven times as many elements as a hexahedral mesh.

Element Size: Element budget and mesh density are indirect methods for setting the element size, esize. This value can also be set explicitly. It represents the approximate average edge length of elements in the model. This size will determine the relative definition of small for subsequent diagnostic tests and will be used to set the mesh size the meshing algorithms will use.

Mesh Density: The mesh density is represented by an integer between 1 and 10, where 1 is the finest resolution and 10 is the coarsest. It is a heuristic measure of how fine of a mesh will be generated and permits the user to indirectly set an element size without explicitly defining a real value. In most cases, the mesh density, md is related to the element size, esize by the following heuristic relationship:

---

## Small details in the model

**URL:** https://coreform.com/cubit_help/item/clean_up/small_details.htm

**Contents:**
- Small details in the model
- Small Curves
- Small and Narrow Surfaces

The small feature removal area of ITEM focuses on identifying and removing small features in the model that will either inhibit meshing or force excessive mesh resolution near the small feature. Small features may result from translating models from one format to another or may be intentional design features. Regardless of the origin small features must often be removed in order to generate a high quality mesh.

ITEM will recognize small features that fall in four classifications:

These operations may involve either real, virtual or a combination of both types of operations to remove these features. A virtual operation is one in which does not modify the CAD model, but rather modifies an overlay topology on the original CAD model. Real operations, on the other hand directly modify the CAD model. Where real operations are provided by the solid modeling kernel upon which CUBIT is built, virtual operations are provided by CUBIT's CGM (Tautges, 00) module and are implemented independently of the solid modeling kernel. The following describes the diagnostics for finding each of the four classifications of small features and the methods for removing them.

Diagnostic: Small curves are found by simply comparing each curve length in the model to a user-specified characteristic small curve size. A default epsilon (e) is automatically calculated as 10 percent of the user specified mesh size, but can be overridden by the user.

Solutions: ITEM provides three different solutions for eliminating small curves from the model. The first solution uses a virtual operation to composite surfaces. Two surfaces near the small curve can often be composited together to eliminate the small curve as shown in Figure 1(a).

The second solution for eliminating small curves is the collapse curve operation. This operation combines partitioning and compositing of surfaces near the small curve to generate a topology that is similar to pinching the two ends of the curve together into a single point. The partitioning can be done either as a real or virtual operation. Figure 1(b) illustrates the collapse curve operation.

The third solution for eliminating small curves is the remove topology operation. This operation can be thought of as cutting out an area around the small curve and then reconstructing the surfaces and curves in the cut-out region so that the small curves no longer exist. (Clark, 07) provides a detailed description of the remove topology operation. This operation has more impact on the actual geometry of the model because it redefines surfaces and curves in the vicinity of a small curve. The reconstruction of curves and surfaces is done using real operations followed by composites to remove extra topology introduced during the operation. Figure 1(c) shows the results using the remove topology operation.

Figure 1. Three operators used for removing small curves (a) composite; (b) collapse curve; (c) remove topology

ITEM also addresses the problem of small and narrow surfaces. Both are dealt with in a similar manner and are described here.

Diagnostic: Small surfaces are found by comparing the surface area with a characteristic small area. The characteristic small area is defined simply as the characteristic small curve length squared or e2.

Narrow surfaces are distinguished from surfaces with narrow regions by the characteristic that the latter can be split such that the narrow region is separated from the rest of the surface. Narrow surfaces are themselves a narrow region and no further splits can be done to separate the narrow region. Figure 2 shows examples of each. ITEM provides the option to split off the narrow regions, subdividing the surface so the narrow surfaces can be dealt with independently.

Narrow regions/surfaces are also recognized using the characteristic value of e. The distance, di from the endpoints of each curve in the surface to the other curves in the surface are computed and compared to e. When di<e other points on the curve are sampled to identify the beginning and end of the narrow region. If the narrow region encompasses the entire surface, the surface is classified as a narrow surface. If the region contains only a portion of the surface, it is classified as a surface with a narrow region.

Figure 2. Two cases illustrating the difference between surfaces with narrow regions and narrow surfaces

Solutions: ITEM provides four different solutions for eliminating small and narrow surfaces from the model. The first solution uses the regularize operation. Regularize is a real operation provided by the solid modeling kernel that removes unnecessary/redundant topology in the model. In many cases a small/narrow surface's definition may be the same as a surface next to it and therefore the curve between them is not necessary and can be regularized out. An example of regularizing a small/narrow surface out is shown in Figure 3.

Figure 3. When the small surface’s underlying geometric definition is the same as a neighbor the curve between them can be regularized out.

The second solution for removing small/narrow surfaces uses the remove operation. Remove is also a real operation provided by the solid modeling kernel. However, it differs from regularize in that it doesn't require the neighboring surface(s) to have the same geometric definition. Instead the remove operation removes the specified surface from the model and then attempts to extend and intersect adjacent surfaces to close the volume. An example of using the remove solution is shown in Figure 4.

Figure 4. The remove operation extends an adjacent surface to remove a small surface

Figure 5. Composite solution for removing a narrow surface

Figure 6. Remove topology solution for removing a narrow surface

Figure 7.Remove topology solution for removing a network of narrow surfaces

---

## Validating the Mesh in ITEM

**URL:** https://coreform.com/cubit_help/item/validating.htm

**Contents:**
- Validating the Mesh in ITEM

Advancements in the mesh generation algorithms have significantly reduced the amount of quality problems seen in the initially generated mesh. Further, ITEM generally relies on the most robust meshing algorithms available in CUBIT, specifically sweeping for hexahedral mesh generation (Scott,05) and the MeshGems (George,91) meshing software (See http://www.distene.com). However, some problems can still exist, and therefore ITEM has integrated quality diagnostics and solution options.

Diagnostics: After the mesh has been generated, the user may choose to perform element quality checks. ITEM utilizes the Verdict (Stimpson,07) library where a large number of mesh quality metrics have been defined and available as a modular library. If no user preference is specified, ITEM uses the Scaled Jacobian distortion metric to determine element quality. This check will warn users of any elements that are below a default or user-specified threshold, allowing various visualization options for displaying element quality.

Solutions: If the current element quality is unacceptable, ITEM will present several possible mesh improvement solutions. The most promising solutions are provided through ITEM's interface to two smoothers: mean ratio optimization and Laplacian smoothing. These are provided as part of the Mesquite (Brewer,03) mesh quality improvement tool built within CUBIT. The user has the option of performing these improvements on the entire mesh, subsets of the mesh defined by the element quality groups, or on individual elements. The Laplacian smoothing scheme allows the users to smooth just the interior nodes or to simultaneously smooth both the interior and boundary nodes in an attempt to improve surface element quality.

---
