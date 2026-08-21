# Meshing

## Additional Interval Constraints

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/additional_interval_contraints.htm

**Contents:**
- Additional Interval Constraints
- Curve Minimum | Maximum
- Loop Minimum | Maximum
- Manual Constraints
  - General Constraints
  - Sets of Curves with the Same Intervals
  - Even

The user may set additional constraints on intervals.

Beware that these constraints will only be respected if the "match intervals" or "mesh" command actually includes all of the relevant entities. For example, setting a loop minimum on a surface, but then meshing the other surfaces containing its curves first, may result in the loop minimum being violated. Manual constraints are only respected if all of the curves in the constraint are part of the current interval matching problem, i.e., if at least one surface containing each curve is in the problem.

Rather than specifying a hard interval count, which may overconstrain the interval matcher, the user can specify an upper and lower bound that is acceptable. Typical uses are sweeping a complex assembly where the normal compromises lead to too many (or few) intervals on specific curves, or thin layers.

{Group|Body|Volume|Surface} <range> {Interval | Size | Periodic Interval} {[Lower]|Upper} Bound {On|Off|<bound>}

Curve <range> {Interval | Size} {[Lower]|Upper} Bound {On|Off|<bound>}

The user can specify the minimum and maximum number of intervals on a loop. This is mostly used for small loops, such as holes drilled in a plate, to ensure they have at least 4 or 6 intervals. If no entties are specified, then the setting is applied globally to all current and future loops in the model.

set [{group|volume|surface|curve} <range>] interval loop minimum {<count>|default}

set [{group|volume|surface|curve} <range>] interval loop maximum {<count>|default}

list [{group|volume|surface|curve} <range>] interval loop [minimum] [maximum] [default]

Curve <curve_id_range> Interval {Equal_to|Greater_than_equal|Less_than_equal} [Curve] <curve_id_range> [ Extra <intervals>]

Curve <curve_id_range> Interval {Equal_to|Greater_than_equal|Less_than_equal} Extra <intervals>

These sets a constraint that the interval matcher resolves when it is run. E.g., the command "curve 2 3 greater_than_equal curve 4 5 extra 4" stores the inequality constraint "c2 + c3 >= c4 + c5 + 4" in the interval matcher. While this can resolve quality issues, it is also an easy way to make the interval matching problem infeasible.

Interval same is a two way constraint that is resolved immediately. If the user subsequently changes the interval on a curve in the set, then the other curves are changed immediately. One problems is if the user hard sets an interval on one curve and then sets a size on another, the hard set interval on the other curve is not changed.

Curve <range> Interval {Same|Different}

List Curve [ <curve_id_range> ] Interval Same

Specifying that curves have the "same" intervals stores them in a set. More curves may be added to an existing set, and sets merged, by future commands. The current contents of the affected sets are printed after each command. A curve may be removed from a set by specifying that its intervals are "different."

The user can also constrain the parity of intervals on curves:

{Curve|Surface|Volume} <range> Interval {Even | Odd}

If Even is specified, then during subsequent interval setting commands and during interval assignment, curves are forced to have an even number of intervals. If the current number of intervals is odd, then it is increased by one to be even. If Odd is specified then intervals may be either even or odd. Setting intervals to even is useful in problems where adjoining faces are paved one by one without global interval assignment.

---

## Align Mesh

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/align_mesh.htm

**Contents:**
- Align Mesh

At times it is desirable to have identical meshes on two different surfaces or curves. The align mesh command will attempt to assign correspondence between nodes on surfaces or curves and move the nodes on one surface or curve to match the configuration on the other. The command syntax is:

Align Mesh Surface <id> [CloseTo] Surface <id> [Tolerance <tol>]

Align Mesh Curve <id> [CloseTo] Curve <id> [Tolerance <tol>]

Align Mesh Node <id> [CloseTo] Node <id> [Tolerance <tol>]

This command aligns the first node with the second node, within the limits of the geometric entities that own the nodes. This is also done without respect for element quality.

And example of this is given as follows:

---

## Automatic Mesh Quality Assessment

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/automatic_mesh_quality_assessment.htm

**Contents:**
- Automatic Mesh Quality Assessment

CUBIT performs an automatic calculation of mesh quality which warns users when a particular meshing scheme or other meshing operation has created a mesh whose quality may be inadequate. These warnings are supplied in case the user forgets to manually check the mesh quality.

CUBIT automatically calculates the SHEAR quality of hexahedral and quadrilateral elements and the SHAPE quality of tetrahedral and triangular elements. The SHEAR metric measures element skew and ranges between zero and one with a value of zero signifying a non-convex element, and a value of one being a perfect, right-angled element. The SHAPE metric also ranges between zero and one with a value of zero signifying a degenerate or inverted element and a value of one signifying a perfect, equilateral element. The quality of the mesh is then defined to be the minimum value of the shear metric for hexahedral and quadrilateral elements and the shape metric for tetrahedral and triangular elements, with the minimum taken over the elements in the mesh.

If the quality of the mesh is zero, the code reports "ERROR: Negative Jacobian Element Generated" to the command window. By default, if the quality of the mesh is positive but less than a certain threshold, the code reports "WARNING: Poorly-Shaped Element Generated" to the command window. Also reported in this case is the ID of the offending element, the value of its shear (or shape) metric, and the value of the threshold to which it was compared. The default value of the threshold parameter is 0.2. Users may change the threshold value by issuing the command

Set Quality Threshold <double=0.2>

The user may also change what type of message is printed in the case of a poor quality, but positive Jacobian mesh. This message can be printed as a warning (the default) or an error or can be turned off completely using the command

Set Print Quality { WARNING|Error|Off }

The above commands only affect the message generated for meshes with a quality greater than zero and less than the given threshold value; an error will always be generated for meshes with a quality of zero (that is, for meshes containing negative Jacobian elements).

---

## Automatic Scheme Selection

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/automatic_scheme_selection.htm

**Contents:**
- Automatic Scheme Selection
- Default Scheme Selection
- Auto Scheme Selection General Notes
- Scheme Firmness
- Surface Auto Scheme Selection
- Volume Auto Scheme Selection

For volume and surface geometries the user may allow CUBIT to automatically select the meshing scheme. Automatic scheme selection is based on several constraints, some of which are controllable by the user. The algorithms to select meshing schemes will use topological and geometric data to select the best quad or hex meshing tool. Auto scheme selection will not select tet or tri meshing algorithms. The command to invoke automatic scheme selection is:

{geom_list} Scheme Auto

Specifically for surface meshing, interval specifications will affect the scheme designation. For this reason it is recommended that the user specify intervals before calling automatic scheme selection. If the user later chooses to change the interval assignment, it may be necessary to call scheme selection again. For example, if the user assigns a square surface to have 4 intervals along each curve, scheme selection will choose the surface mapping algorithm. However if the user designates opposite curves to have different intervals, scheme selection will choose paving, since this surface and its assigned intervals will not satisfy the mapping algorithm's interval constraints. In cases where a general interval size for a surface or volume is specified and then changed, scheme selection will not change. For example, if the user specified an interval size of 1.0 a square 10X10 surface, scheme selection will choose mapping. If the user changes the interval size to 2.0, mapping will still be chosen as the meshing scheme from scheme selection. If a mesh density is not specified for a surface, a size based on the smallest curve on the surface will be selected automatically.

If the user does not set a scheme for a particular entity and chooses to mesh the entity, CUBIT will automatically run the auto scheme selection algorithm and attempt to set a scheme. In cases where the auto scheme selection fails to choose a scheme, the meshing operation will fail. In this case explicit specification of the meshing scheme and/or further geometry decomposition may be necessary.

The default scheme selection in CUBIT, unless otherwise set, will attempt to set a quadrilateral or hexahedral meshing scheme on the entity. If tet or tri meshing will always be the desired element shape, the following command can be used:

Set Default Element [Tet|Tri|HEX|QUAD|None]

Setting the default element to tet or tri will bypass the auto scheme selection and always use either the triadvance or tetmesh schemes if the scheme has not otherwise been set by the user. The default settings of quad or hex will use the automatic scheme selection.

Previous functionality of CUBIT used a default scheme of map and interval of 1 for all surface and volume entities. For backwards compatibility and if this behavior is still desired, the none option may be used on the set default element command.

In general, automatic scheme selection reduces the amount of user input. If the user knows the model consists of 2.5D meshable volumes, three commands to generate a mesh after importing or creating the model are needed. They are:

volume all size <value>

volume all scheme auto

The model shown in the following figure was meshed using these three commands (part of the model is not shown to reveal the internal structure of the model).

Figure 1. Non-trivial model meshed using automatic scheme selection

Meshing schemes may be selected through three different approaches. They are: default settings, automatic scheme selection, and user specification. These methods also affect the scheme firmness settings for surfaces and volumes. Scheme firmness is completely analogous to interval firmness.

Scheme firmness can be set explicitly by the user using the command

{geom_list} Scheme {Default | Soft | Hard}

Scheme firmness settings can only be applied to surfaces and volumes.

This may be useful if the user is working on several different areas in the model. Once she/he is satisfied with an area's scheme selection and doesn't want it to change, the firmness command can be given to hard set the schemes in that area. Or, if some surfaces were hard set by the user, and the user now wants to set them through automatic scheme selection then she/he may change the surface's scheme firmness to soft or default.

Surface auto scheme selection (White, 99) will choose between Pave, Submap, Triprimitive, and Map meshing schemes, and will always result in selecting a meshing scheme due to the existence of the paving algorithm, a general surface meshing tool (assuming the surface passes the even interval constraint).

Surface auto scheme selection uses an angle metric to determine the vertex type to assign to each vertex on a surface; these vertex types are then analyzed to determine whether the surface can be mapped or submapped. Often, a surface's meshing scheme will be selected as Pave or Triprimitive when the user would prefer the surface to be mapped or submapped. The user can overcome this by several methods. First, the user can manually set the surface scheme for the "fuzzy" surface. Second, the user can manually set the "vertex types" for the surface. Third, the user can increase the angle tolerance for determining "fuzziness." The command to change scheme selection's angle tolerances is:

[Set] Scheme Auto Fuzzy [Tolerance] {value} (value in degrees)

The acceptable range of values is between 0 and 360 degrees. If the user enters 360 degrees as the fuzzy tolerance, no fuzzy tolerance checks will be calculated, and in general mapping and submapping will be chosen more often. If the user enters 0 degrees, only surfaces that are "blocky" will be selected to be mapped or submapped, and in general paving will be chosen more often.

When automatic scheme selection is called for a volume, surface scheme selection is invoked on the surfaces of the given volume. Mesh density selections should also be specified before automatic volume scheme selection is invoked due to the relationship of surface and volume scheme assignment.

Volume scheme selection chooses between Map, Submap and Sweep meshing schemes. Other schemes can be assigned manually, either before or after the automatic scheme selection.

Volume scheme selection is limited to selecting schemes for 2.5D geometries, with additional tool limitations (e.g. Sweep can currently only sweep from several sources to a single target, not multiple targets); this is due to the lack of a completely automatic 3D hexahedral meshing algorithm. If volume scheme selection is unable to select a meshing scheme, the mesh scheme will remain as the default and a warning will be reported to the user.

Volume scheme selection can fail to select a meshing scheme for several reasons. First, the volume may not be mappable and not 2.5D; in this case, further decomposition of the model may be necessary. Second, volume scheme selection may fail due to improper surface scheme selection. Volume schemes such as Map, Submap, and Sweep require certain surface meshing schemes, as mentioned previously.

---

## Automatic Specification of Interval Size

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/automatic_specification.htm

**Contents:**
- Automatic Specification of Interval Size
- Automatic Interval Size Specification
- Maximum Spanning Angle on Arcs

In addition to specifying intervals explicitly based on a known count or size, CUBIT is able to compute interval sizes automatically based on characteristics of the model geometry. The following automatic interval size setting command can be used:

{geom_list} Size Auto [Factor <factor> ] [Individual] [Propagate]

Vertices are not valid in the geom_list for this command. Automatic interval size assignment works by examining the geometric characteristics of the entities in the geom_list and assigning a heuristic size to the entities and their child entities. The factor may be a floating point number between 1.0 and 10.0, where 1.0 represents a fine interval size and 10.0 represents a coarse size. Figure 1 shows an example of different auto size specification on a CAD model.

(a) auto size factor = 7.0

(b) auto size factor = 5.0

(c) auto size factor = 1.0

The user may assign the interval size to be the arc length of the smallest curve contained in the specified entity or entities using the following command:

{geom_list} Size Smallest Curve

Vertices are not allowed in the geom_list for this command. This command assigns a soft interval firmness.

An automatic interval size with an auto size factor of 5 will automatically be computed and applied to any curve for which the following is true:

1) Intervals have not been explicitly defined by the user for a curve or its owning entities.

2) An Interval size has not been explicitly defined by the user for a curve and it is not possible to determine an interval size from its owning entities.

This automatic interval size is based upon all the geometry in the model. The automatic interval size specifications can be overridden easily by specifying another auto size factor or an explicit interval size.

If an auto size factor of 5 is undesirable for most meshing operations, the default factor may be changed by using the following command:

Set Auto Size Default <value>

where value is a number from 1 to 10. This will be the default auto size factor used when either a factor has not been specified on the size auto command or when an automatic interval size specification is used.

In previous versions of CUBIT a default interval of 1 was assigned to all entities. If this behavior is still desired, the following command may be used to enforce this condition:

Set Default Autosize [ON|off]

On many CAD models, arcs or small holes require that a finer mesh be specified around these entities in order to maintain reasonable mesh quality. To facilitate this, the user may specify the maximum angle an element edge may span on an arc. To change or list the maximum arc span, use the following commands

Set Maximum Arc_Span <angle>

List Maximum Arc_Span

The angle parameter must be a positive value less than 360. The maximum arc span setting will only be used if there is not already a user defined interval set on the arc, and if the interval setting produces mesh edges which exceed the maximum spanning angle. Figure 2 shows the effect of three different maximum arc_span settings on a small hole using the pave scheme.

Figure 2. Maximum arc_span settings of 90, 45 and 15 degrees respectively.

Default arc span setting: In addition to setting an automatic size factor, if there are otherwise no user-defined interval sizes defined on an arc and no maximum arc_span has been set by the user when a tetrahedral mesh or triangle mesh is defined, a maximum spanning angle of 60 degrees will be used. Removing the use of the arc_span setting can be accomplished with the following:

Set Maximum Arc_Span Default

Note that once interval sizes have been defined when the entity has been meshed, it may be necessary to reset the interval settings (reset {geom_list}) to use a new maximum arc span setting when remeshing.

---

## Bias, Dualbias

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/bias_dualbias.htm

**Contents:**
- Bias, Dualbias

Summary: Meshes a curve with node spacing biased toward one or both curve ends.

Curve <range> Scheme Bias

Curve <range> Scheme Bias {Factor|First_Delta|Fraction} <double> [Start Vertex <range>] [preview]

Curve <range> Scheme Dualbias {Factor|First_Delta|Fraction} <double> [preview]

Curve <range> Scheme Bias Fine Size <double> {Coarse Size <double> | Factor <double>} [Start Vertex <range>] [preview]

Curve <range> Scheme Dualbias Fine Size <double> {Coarse Size <double> | Factor <double>} [preview]

Curve <range> Scheme Multi_bias Start <size> [Fraction <value> <size>]... End <size> [Start Vertex <id>][Respect_intervals][preview]

Curve <range> Reverse Bias

Set Maximum Interval <int>

See also Surface Sizing Function Type Bias

See also Curve Scheme Stretch

The main differences between scheme bias and stretch are the following: scheme stretch does not use strict geometric series for node placement. If you specify scheme bias or dualbias using the "fine size" form, the interval count will be hard-set to a value that fills in the curve.

When using the command 'curve <range> scheme bias' with no additional parameters, an auto setting will be enabled by default for tet and tri meshing. This scheme honors sizes at a curve's vertices and that vertex size will be used to create a biased edge mesh. For example, two volumes with different sizes set on the volumes are merged. The size at the vertices (averaged from sizes on the parent entities) will be used to create the biased edge mesh.

A user can set a size on a vertex with the following command:

Vertex <id> Size <size>

The Bias and DualBias schemes space the curve mesh unequally, placing more nodes towards (or away from) the ends of the curve according to a geometric progression. The ratio of successive edges is the "factor," which may be greater than or less than one. For bias, the series starts at the first vertex of the curve, or the "start vertex" if specified. For dualbias, the series starts at both ends of the curve and meets in the middle.

The command behaves differently depending on which set of parameters are specified. There are three basic variables: the interval count, the bias factor, or the first edge size. The curve length is a given, fixed quantity. The user can specify any two of these variables, and the third will be automatically determined.

If the "{Factor|First_Delta|Fraction}" form is specified, then the interval count is taken as a given. The interval count is whatever was specified previously by an interval count or size command (see Interval Assignment). If "Factor" is specified, then the first edge size will be automatically chosen so that the geometric progression of edges "fit" onto the curve. If "first_delta" is specified, then the first edge length is exactly that absolute value, and the "factor" is automatically chosen. If "fraction" is specified, then the first edge length is the curve length times that fraction, and again the "factor" is automatically chosen.

If the "fine size" is specified, then the first edge length is exactly that absolute value. If the "factor" is specified, then the interval count is automatically chosen. If an approximate coarse size is specified, then this also determines the factor, and again the interval count is automatically chosen. If a surface sizing function type bias is used, then the curves of the surface are sized using similar formulas.

If no start or end vertex is specified, the curve's start vertex is used as the starting point of the bias. (A curve's start vertex can be identified by listing the curve from the "CUBIT>" prompt.)

The maximum interval setting allows the user to set a maximum number of intervals on any bias curve. This value is doubled for a curve with a dualbias scheme. It can be easy to accidentally specify a very large number of intervals and this setting allows the user to place an upper limit the number of intervals.

The preview option will allow the user to preview mesh size and distribution on the curve before meshing.

The following figure shows the result of meshing edges with equal, bias and dualbias schemes.

The multi-bias scheme allows several biases to be created on a single curve by specifying desired sizes at multiple locations along the curve (see Figure 1 below). The "start" and "end" sizes must be specified, and any number of fraction-size pairs may be specified, where the fraction value is between 0 - 1. If "Start Vertex" is given, the specified vertex is considered to have the fraction value of 0, with the opposite vertex having the fraction value of 1. If "respect_intervals" is not specified, the scheme will choose an appropriate number of intervals for the curve based on the given sizes.

Figure 1. Curve with scheme multi_bias.

If the "respect_intervals" option is given, the multi-bias scheme will try to get as close to the desired sizes as possible, but will always respect the number of intervals set on the curve and adjust sizing as necessary (see Figure 2).

Figure 2. Same curve as in Figure 1, but with the respect_intervals option. Note the areas of relatively dense mesh correspond to the dense mesh in the original.

---

## Bias Sizing Function

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/bias_sizing_function.htm

**Contents:**
- Bias Sizing Function

Surface <id> Sizing Function Type Bias Start Curve <id_range> {Finish Curve <id_range>| Factor <val>}

The Bias sizing function for surfaces is similar to biasing curves. Indeed, setting a bias sizing function for a surface will bias the boundary curves, as well as control paving to follow the bias inside the surface. You first specify the size of a couple of bounding curves (the start curves), then specify the bias sizing function for the surface.

Recall that for biasing curves, you specify the start and end vertex. For the bias sizing function, you specify the start curves, from which to bias away. The sizes of these curves should already be set before setting the surface sizing function since their average size is taken to be the starting size (almost). If the start curve sizes change, then you should set the surface sizing function again.

You can either supply a geometric factor, or the set of finish curves whose sizes you want to match at that distance. A geometric factor. It automatically sizes and biases or dualbiases the non-start curves, including any finish curves. These curves need not be perpendicular to the starting curves. The interval count and scheme are soft-set, so they won't be changed if they are already hard-set. If the size of the start curves or finish curves are changed, then the sizing function command should be re-issued.

The sizing function value at a point is defined in terms of the straight-line distance from the point to the closest starting curve. So, it works best if all the starting curves have the same size, and the surface is relatively flat. But, starting curves need not be parallel to one another. Similarly, the non-start curves need not have any particular orientation wrt the start curves.

The bias sizing function was designed to easily set the sizes of a sequence of adjoining surfaces: assign a size to the curve you want to bias away from, then set the bias sizing function of the first surface, with its finish curves being the start curve of the second surface, etc. See the last example below.

Here are some example journal files and resulting pictures:

# bias_sz_fn_demo.jou brick x 100 y 10 z 10 color vol 1 red surface 1 scheme pave surface all except 1 visibility off # label curve interval # graph text 2 display

# mesh 1 curve 4 size 2 surface 1 sizing function type bias start curve 4 factor 1.3 mesh surface 1 # see figure 1

Figure 1. Surface with bias sizing function factor > 1.

# mesh 2 delete mesh surface 1 sizing function type bias start curve 4 factor {1/1.1} mesh surface 1 # see figure 2

Figure 2. Surface with bias sizing function factor < 1

# mesh 3 reset cyl rad 6 z 1 cyl rad 4 z 1 sub 2 from 1 section body 1 yplane section body 1 xplane surf all except 19 vis off color vol 1 red display

# finish curve mesh surf 19 scheme qtri base scheme pave surface 19 size 0.7 curve 26 size 0.07 surface 19 sizing function type bias start curve 26 finish curve 25 mesh surface 19 pause # see figure 3

Figure 3. Surface with bias sizing function start and finish curve. Scheme qtri, base scheme pave.

# dual bias mesh delete mesh curve 25 26 size 0.02 curve 25 26 scheme equal surface 19 sizing function type bias start curve 26 25 factor 1.3 mesh surface 19 zoom curve 12 pause # see figure 4

Figure 4. Close up of surface with dual bias sizing function start and finish curve. Scheme qtri, base scheme pave.

# funny face reset prism sides 5 z 1 radius 1 cylinder radius 0.1 z 1 body 2 move -0.4 0 0 subtract 2 from 1 cylinder radius 0.1 z 1 body 3 move 0.2 0 0 subtract 3 from 1 prism sides 6 radius 0.2 z 1 body 4 move 0 -0.4 0 subtract 4 from 1 surface all except 34 visibility off color vol 1 red display surface 34 scheme pave curve 23 19 size 0.01 surface 34 sizing function type bias start curve 19 23 factor 1.3 mesh surface 34 # see figure 5

Figure 5. Bias away from two round holes.

# bias surface chain reset cylinder radius 1 z 1 cylinder radius 0.2 z 1 cylinder radius 0.4 z 1 cylinder radius 0.8 z 1 imprint body all delete body 2 3 4 section body 1 xplane section body 1 yplane surface all except 42 43 44 45 vis off color volume 1 red surface all scheme pave curve 55 interval 36 surface 43 sizing function type bias start curve 55 factor 1.3 surface 44 sizing function type bias start curve 57 factor 1.3 # curve 57 had its size determined by a prior bias sizing function surface 45 sizing function type bias start curve 58 factor 1.3 surface 42 sizing function type bias start curve 55 factor 1.3 mesh surface 42 43 44 45 display highlight curve in surface 42 43 44 45 # see figure 6

Figure 6. A chain of biased surfaces. Only one curve's intervals were explicitly set.

---

## Boundary Layer Meshing

**URL:** https://coreform.com/cubit_help/boundary_layer_meshing/boundary_layer_meshing.htm

**Contents:**
- Boundary Layer Meshing
  - Intersection Types
  - Current Limitations
  - Underlying Cubit Commands
  - Sample Journal Files
    - Example 1
    - Example 2

Boundary layer meshing is best accessed via the GUI.

To create a boundary layer:

Figure 1 - Settings Panel

First row(a) -- the height of the first layer in the boundary layer

Growth Factor(b/a) -- the factor by which each layer grows

Number of Layers -- the number of layers that make up a boundary layer

Internal Continuity -- continuity flag for boundary layers. If on, all intersections are a side type.

For 2D boundary layers:

For 3D boundary layers:

Figure 2 - Association Panel

For 2d boundary layers, a curve/surface pair is given to create a boundary layer starting from a curve and growing out on the given surface.

For 3d boundary layers, a surface/volume pair is given to create a boundary layer starting from a surface and growing out on the given volume.

In some cases, the user may want to adjust the intersection types. This could be because the automatic intersection type is not desired, or because it is not workable due to ambiguity.

The four intersection types are:

These intersection types may be set on a vertex/surface basis and on a curve/volume basis.

Figure 3 - Intersections Type Panel

Not all combinations of intersection types and topology are supported for 3d cases. An end, corner, or reversal may not span multiple curves in a single volume. A possible workaround is to composite the curves to make a single curve.

Not all meshing schemes may be used in combination with boundary layers. In cases where it is not supported, the boundary layer will be ignored in mesh generation. It is supported with the following schemes:

Create Boundary_layer <id>

Delete Boundary_layer <id>

Modify Boundary_layer <id> add Curve <id_range> Surface <id>

Modify Boundary_layer <id> remove Curve <id_range> Surface <id>

Modify Boundary_layer <id> add Surface <id_range> Volume <id>

Modify Boundary_layer <id> remove Surface <id_range> Volume <id>

"*** Only three of the four parameters should be specified ***

"*** (Height, Growth, Layer, or Depth) ***

Modify Boundary_layer <id> uniform Height <double> Growth <double> Layers <double> Depth <double>

Modify Boundary_layer <id> continuity {yes | no}

set boundary_layer intersection volume <id> curve <ids> type {end, side, corner, reversal, default}

set boundary_layer intersection surface <id> vertex <ids> type {end, side, corner, reversal, default}

Boundary_layer visibility {on|off}

[set] Boundary_layer <color>

The boundary_layer visibility command toggles the display of boundary layers in the graphics window. The [set] boundary_layer <color> command sets the color used to draw all boundary layers; <color> is any of the recognized Cubit color names.

create surface rectangle width 10 height 3

create surface circle radius 5 zplane

create volume loft surface 1 2

create boundary_layer 1

modify boundary_layer 1 uniform height 0.1 growth 1.2 layers 4

modify boundary_layer 1 add surface 4 volume 3 surface 5 volume 3 surface 6 volume 3 surface 7 volume 3

set boundary_layer intersection volume 3 curve 10 type side

set boundary_layer intersection volume 3 curve 12 type side

set boundary_layer intersection volume 3 curve 14 type side

set boundary_layer intersection volume 3 curve 16 type side

create surface rectangle width 2

cylinder radius 0.1 z 0.1

cylinder radius 0.02 z 0.1

section volume 2 xplane reverse

section volume 3 xplane

create volume loft surface 12 8

volume 5 scale 0.3 0.3 1

volume 5 rotate -10 about z

volume 5 move x 0.55 y -0.1

volume 2 5 move x -0.25

surf all scheme trimesh

group "profile" add curve in surface 30 29

create boundary_layer 1

modify boundary_layer 1 uniform height 0.002 growth 1.2 layers 6

modify boundary_layer 1 add curve in group with name "profile" surface 28

curve in group with name "profile" size 0.02

surface 28 sizing function linear neighbor 2

---

## Building a Sweepable Topology

**URL:** https://coreform.com/cubit_help/item/clean_up/meshable_topology.htm

**Contents:**
- Building a Sweepable Topology

The hex meshing problem presents a number of additional challenges to the user that tetrahedral meshing does not. Where a good quality tetrahedral mesh can generally be created once small features and imprint/merge problems have been addressed, the hexahedral meshing problem poses additional topology constraints which must be met.

Although progress has been made in automating the hex meshing process, the most robust meshing algorithms still rely on geometric primitives. Mapping [Cook, 82] and sub-mapping [Whiteley, 96] algorithms rely on parametric cubes and sweeping[Knupp, 98; Scott, 05] relies on extrusions. Most real world geometries do not automatically fit into one of these categories so the topology must be changed to match the criteria for one of these meshing schemes. ITEM addresses the hex meshing topology problem through four primary diagnostic and solution mechanisms.

---

## Centroid Area Pull

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/centroid_area_pull.htm

**Contents:**
- Centroid Area Pull

Applies to: Surface Meshes

Summary: Attempts to create elements of equal area

Surface <range> Smooth Scheme Centroid Area Pull [Free]

This smooth scheme attempts to create elements of equal area. Each node is pulled toward the centroids of adjacent elements by forces proportional to the respective element areas (Jones, 74).

The free option allows the nodes on the boundary (curves) to be moved during the smooth operation.

---

## Circle

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/circle.htm

**Contents:**
- Circle

Summary: Produces a circle-primitive mesh for a surface

Surface <range> Scheme [Sector] Circle [Interval <int>] [fraction <double>]

The Circle scheme is used in regions that should be meshed as a circle. A "circle" consists of a single loop of bounding curves containing an even number of intervals. Thus, the circle scheme can be applied to circles, ellipses, ovals, and regions with "corners" (e.g. polygons). The bounding curves should enclose a convex region. Non-planar bounding loops can also be meshed using the circle primitive provided the surface curvature is not too great. The mesh resembles that obtained via polar coordinates except that the cells at the "center" are quadrilaterals, not triangles. See Figure 1 for an example of a circle mesh. Radial grading of the mesh may be achieved via the optional [intervals] input parameter. The Fraction option has the range 0 < fraction < 1 and defaults to 0.5. Fraction determines the size of the inner portion of the circle mesh relative to the total radius of the circle. The sector option was added to revert to legacy behavior which is not recommended.

Figure 1. Circle Primitive Mesh

---

## Coincident Node Check

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/coincident_node_check.htm

**Contents:**
- Coincident Node Check

The ability to check for coincident nodes in the model is available in CUBIT. It uses an efficient octal hash tree to make the comparisons. The command is:

Quality Check Coincident Node [ In ] [Group|Body|Volume|Surface|Curve|Vertex <id_range> ] [ Merge [Delete] ] [ HIGHLIGHT|Draw [color <number>]] [List] [Into Group [names|id] ]

If no entity list is given, the command works on all the nodes in the model. If an entity list is given, then it compares the nodes on those entities with the rest of the nodes in the model. By default the command highlights the coincident nodes in the graphics window and lists the total number of coincident nodes found. You can also have it clear the graphics and draw the nodes, and/or list the coincident node ids. Optionally, the coincident nodes found can be placed in a group.

If the model being operated on is from an imported universal file (i.e., no geometry exists in the model), you can merge the coincident nodes with the merge option. In this case delete allows you to delete the extra nodes (recommended). If you do not delete them they are placed into an output group.

You can control the tolerance used to check between nodes with the following setting (default = 1e-8):

set Node Coincident Tolerance [<value>]

---

## Collapsing Mesh

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/collapsing_mesh_edges.htm

**Contents:**
- Collapsing Mesh
- Collapsing Mesh Using Quality Metrics
- Collapsing Mesh Manually
- Collapsing and Swapping Mesh Using Quality Metrics
- Removing Overconstrianed Tets

CUBIT currently offers several options for modifying an existing finite element mesh. Triangle and tetrahedral meshes sometimes contain low quality elements that can be removed by the following operations.

The following first two commands collapse triangles, while the third collapses tetrahedra. Collapses are performed only if the collapse operation does not cause worse quality in the surrounding, surviving mesh; otherwise the collapse is not performed. The collapse operation removes the element by consolidating two neighbor nodes of the specified mesh entity into one, to either node location or their midpoint. The specified metric is used to determine quality, the default being Scaled Jacobian. The Interior option of the Collapse Tet command limits the collapse to the interior of the volume mesh, so that the triangle surface mesh is not modified.

Collapse Edge <ids> [SCALED JACOBIAN|Aspect Ratio|Shape|Shape and Size]

Collapse Tri <ids> [SCALED JACOBIAN|Aspect Ratio|Shape|Shape and Size]

Collapse Tet <ids> [Interior] [Altitude|Aspect Ratio|Aspect Ratio Gam|Distortion|Inradius|Jacobian|Normalized Inradius|Node Distance|SCALED JACOBIAN|Shape|Shape and Size|Timestep]

Figure 1. Before and After Triangle/Edge Collapse

The following command collapses triangles containing the given edge, with no regard for quality.

Meshedit Collapse edge <id> [keep node <id>] [compress_ids]

This command only works on triangle surface meshes. If volumetric elements, or quads, are attached to the edge, the command fails. The keep node option control which node to collapse to. The option compress_ids compresses holes in the mesh id space caused by the collapse.

Combining nodes to collapse tetrahedra can be done with the following command. The first node specified is merged into (deleted) the second node. If the first node cannot be moved due to geometry constraints (it's owned by a vertex), the operation fails. This command is behind a developer flag so set dev on must be issued before use.

Mesh quality can also be improved by swapping edges. The improve tri command uses both edge collapse and edge swap operations to improve triangle mesh quality. The operation that produces better quality, based on the specified metric, is used. Also how close the mesh approximates the geometry is considered. The command will fail if the triangles are in 3D mesh elements.

Improve Tri <ids> [SCALED JACOBIAN | Aspect Ratio | Shape | Normalized Inradius]

Figure 2. Before and After Improve Tri Command

Cubit offers commands to remove overconstrained tetrahedra - tets containing two triangles on the same surface and all four corner nodes on surfaces, curves, or vertices. These tets are not amenable to smoothing, leaving removal as the only viable solution to improve quality.

Remove Overconstrained {Tet <ids> | Tet Volume <ids>} [preview]

The tets are deleted and the two back sides become surface triangles. If the tets have mid-edge nodes, the back mid-edge nodes are snapped to the surface. If this removal operation generates worse quality (aspect ratio) than in the tet removed, the operation is not performed. Figure 3 shows before and after image of removing overconstrained tets. If volumes are specified, the overconstrained tets are found automatically. The preview option draws the tets that will be removed.

Figure 3. Before and After Removing Overconstrained Tets

---

## Condition Number

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/condition_number.htm

**Contents:**
- Condition Number

Applies to: Triangular or Quadrilateral Surface Meshes, Tetrahedral or Hexahedral Volume Meshes. Does not apply to Mixed Element Meshes.

Summary: Optimizes the mesh condition number to produce well-shaped elements.

Surface <surface_id_range> Smooth Scheme Condition Number [beta <double=2.0>] [cpu <double=10>]

The condition number smoother is designed to be the most robust smoother in Cubit because it guarantees that if the initial mesh is non-inverted then the smoothed mesh will also be non-inverted. The price exacted for this capability is that this smoother is not as fast as some of the other smoothers.

Condition Number measures the distance of an element from the set of degenerate (non-convex or inverted) elements. Optimization of the condition number increases this distance and improves the shape quality of the elements. Condition number optimization requires that the given mesh contain no negative Jacobians. If the mesh contains negative Jacobians and this command is issued, Cubit automatically calls the Untangle smoother and attempts to remove the negative Jacobians. If successful, condition number smoothing occurs next; the resulting mesh should have no negative Jacobians. If untangling is unsuccessful, condition number smoothing is not performed.

There is no "fixed/free" option with this command; boundary nodes are always held fixed.

The command above only sets the smoothing scheme; to actually smooth the mesh one must subsequently issue the command "smooth surface <surface_id_range>" or "smooth volume <volume_id_range>".

Stopping Criteria: Smoothing will proceed until the objective function has been minimized or until one of two user input stopping criteria are satisfied. To input your own stopping criterion use the optional parameters 'beta' and 'cpu' in the command above. The value of beta is compared at each iteration to the maximum condition number in the mesh. If the maximum condition number is less than the value of beta, the iteration halts. In Cubit condition number ranges from 1.0 to infinity, with 1.0 being a perfectly shaped element. Thus the smaller the maximum condition number, the better the mesh shape quality. The default value of the beta parameter is 2.0. The value supplied for the "cpu" stopping criterion tells the code how many minutes to spend trying to optimize the mesh. The default value is 10 minutes. Optimization may also be halted by using "control-C" on your keyboard.

To view a detailed report of the smoothing in progress issue the command "set debug 91 on" prior to smoothing the surfaces or volumes. You will get a synopsis of whether or not untangling is needed first and whether the stopping criteria have been satisfied. In addition the following printout information is given for each iteration of the conjugate gradient numerical optimization:

Iteration=n, Evals=m, Fcn=value1, dfmax=value2, time=value3 ave_cond=value4, max_cond=value5, min_jsc=value6

n is the iteration count, m is the number of objective function evaluations performed per iteration, value1 is the value of the objective function (this usually decreases monotonically), value2 is the norm of the gradient (does not always decrease monotonically), and value3 is the cumulative cpu time (in seconds) spent up to the current iteration. The minimum possible value of the objective function is zero but this is attained only for a perfect mesh. ave_cond, max_cond, and min_jsc are the average and maximum condition number, and the minimum scaled jacobian. ave_cond generally decreases monotonically because it is directly related to value1.

---

## Constant Sizing Function

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/constant_sizing_function.htm

**Contents:**
- Constant Sizing Function

Surface <id> Sizing Function [Type] Constant

Volume <id> Sizing Function [Type] Constant

The Constant sizing function specifies that a constant element size be used over the interior of the surface or volume. The value used as the constant size is the interval size that has been set for the entity. For example, the following commands will cause the mesh size to be smaller on the interior than on the surface's bounding curves.

reset brick x 10 surface 1 scheme pave curve in surface 1 interval 5 surface 1 size 0.5 surface 1 sizing function constant mesh surface 1

Figure 1. Constant Sizing Function

---

## Controlling Mesh Quality

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/controlling_mesh_quality.htm

**Contents:**
- Controlling Mesh Quality
- Skew Control
- Propagate Curve Bias
- Adjust Boundary

If the quality of a model after meshing isn't acceptable, there are two options available to improve that quality. The user can ask for more smoothing, or delete the mesh and start over. There are some commands that the user can invoke before meshing the model which can help to improve mesh quality. Some of them are discussed here.

The philosophy behind the skew control algorithm is one of subdividing surfaces into blocky, four-sided areas which can be easily mapped. The goal of this subdivide-and-conquer routine is to lessen the skew that a mesh exhibits on submapped regions. By controlling the skew on these surfaces, the mesh of the underlying volume will also demonstrate less skew.

The commands for skew control are:

Control Skew Surface <surface_id_range> [Individual]

Delete Skew Control Surface {surface_list} [Propagate]

The keyword Individual is deprecated. Its purpose is to specify that surfaces should be processed without regards to the other surfaces in the given list. This is not necessary, and could lead to problems with the final mesh. When the command is entered, the algorithm immediately processes the surfaces, inserting vertices and setting interval constraints on the resulting subdivided curves. In this way, the mesh is more constrained in its generation, and the resulting skew on the model can be lessened. The only surfaces that can utilize this algorithm are those that lend themselves to a structured meshing scheme, although future releases might lessen this restriction.

The user also has the ability to delete the changes that the skew control algorithm has made. This is done by using the delete skew control command.

When the user requests the deletion of the skew control changes on a given surface, every curve on that surface will have the skew control changes deleted, even if a given curve is shared with another surface on which skew control was performed. If the user wishes to propagate the deletion of skew control to all surfaces which are affected by one (or more) particular surfaces, the keyword propagate should be used.

When a bias mesh scheme is applied to a curve, this sometimes creates skewing of the surface mesh that is attached. Sometimes the user will want to ensure that the same bias is applied to curves on attached surfaces so that this skewing is minimized. The command for doing this is:

Propagate Curve Bias [Surface|Volume|Body|Group <id_list>]

This command will search out all simply mappable surfaces in the input list, find which curves of those have a bias scheme set, and will propagate that bias across the mappable surfaces.

Adjust Boundary {Surface|Group} <id_range> [Angle <double>]

This command can be used to improve element quality for mapped or submapped surface meshes. Often, due to vertex positions, the curve meshing for a surface will lead to a poor quality surface mesh. This command can be used to adjust the curve meshes in an attempt to generate a better quality surface mesh. The command works by looking at the angle the mesh edges leave the boundary. In a perfect mapped or submapped mesh, the mesh edges will be orthogonal to the boundary, or will go off at 90 degree angles. The adjust boundary command looks at the deviation of the mesh edges, and if it is greater than the prescribed angle deviation, it will move the node location such that it is 90 degrees, if possible. The deviation angle by default is 5 degrees and can be changed by the user through the [Angle <double>] option in the command. In order to modify the curve meshes, the surface meshes are first deleted then later remeshed after the curve meshes have been repositioned and fixed. This command assumes that the volumes attached to the surface have not been meshed, if they have been, the command will return an error message. It should be noted that this command, while useful, may not always work due to interval constraints (i.e., you may need to change the intervals on the surface), or if the surfaces are not very blocky.

---

## Copying a Mesh

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/duplication/copying.htm

**Contents:**
- Copying a Mesh

Applies to: Curves, Surfaces, Volumes

Summary: Copies the mesh from one entity to another

Curve <range> Scheme Copy source Curve <range> [Source Percent [<percentage> | auto]] [Source [combine|SEPARATE]] [Target [combine|SEPARATE]] [Source Vertex <id_range>] [Target Vertex <id_range>]]

Surface <id> Scheme Copy Source Surface <id> Source Curve <id> Target Curve <id> Source Vertex <id> Target Vertex <id> [Nosmoothing] [mirror]

Volume <range> Scheme Copy [Source Volume] <id> [[Source Surface <id> Target Surface <id>] [Source Curve <id> Target Curve <id>] [Source Vertex <id> Target Vertex <id>]][Nosmoothing]

Copy Mesh Curve <id> Onto Curve <curve_id_range> [Source Node <starting node id> <ending node id>] [Source Percent [<percentage>|auto]] [Source Vertex <id_range>] [Target Vertex <id_range>]

Copy Mesh Surface <surface_id> Onto Surface <surface_id> Source Vertex <id> Target Vertex <id> Source Curve <id> Target Curve <id> [interior (pair vertex <id> <id>) ...] [smooth] [mirror] [preview]

Copy Mesh Volume <volume_id> Onto Volume <volume_id> [Source Vertex <vertex_id> Target Vertex <vertex_id> [Source Curve <curve_id> Target Curve <curve_id>] [Nosmoothing]

Set Morph Smooth {on | off}

If the user desires to copy the mesh from a surface, volume, curve, or set of curves that has already been meshed, the copy mesh scheme can be used. Note that this scheme can be set before the source entity has been meshed; the source entity will be meshed automatically, if necessary, before the mesh is copied to the target entity. The user has the option of providing orientation data to specify how to orient the source mesh on the target entity. For example, when copying a curve mesh, the user can specify which vertex on the source (the source vertex) gets copied to which vertex on the target (the target vertex). If you need to reference mesh entities for the copy, use the Copy Mesh commands. If no orientation data is specified, or if the data is insufficient to completely determine the orientation on the target entity, the copy algorithm will attempt to determine the remaining orientation data automatically. If conflicting, or inappropriate, orientation data is given, the algorithm attempts to discard enough information to arrive at a proper mesh orientation.

Curve mesh copying has certain options that allow the copying of just a section of the source curves' mesh. These options are accessed through the extra keyword options. The percent option allows the user to specify that a certain percentage of the source mesh be copied--in this context the auto keyword means that the percentage will be calculated based on the ratio of lengths of the source and target curves. The combine and separate keywords relate to how the command line options are interpreted. If the user wishes to specify a group of target curves that will each receive an identical copy of a source mesh, then the target separate option should be used (this is the default). If, however, the user wishes the source mesh to be spread out along the range of target curves, then the target combine option should be used. The source curves are treated in a similar fashion.

Surface mesh copying with multiple holes in the surface may require matching up interior pair vertices. This will be required if the algorithm cannot match them up spatially. Interior pair vertices can be specified with the option Interior pair vertex <id> <id> ...

Volume mesh copying depends on the surface copying scheme. Because of this, the target volume must not have any of its surfaces meshed already.

An exact copy of the mesh may not always happen. Dissimilar geometry or smoothing may cause inexact copies. If the geometry is similar, the smoothing option may be turned off to get an exact copy of the mesh, by either specifying Nosmoothing or by omitting Smooth. If the geometry is dissimilar, the user may set the morph smoothing flag on, which will activate a special smoother that will match up the meshes as closely as possible.

As an example, the following copy is done with the command

copy mesh surf 23 onto surf 14 source curve 1 source vertex 1 target curve 24 target vertex 20

The source and target vertices match up, and are highlighted, while the source and target curves match up and are highlighted. Matching the source and target curves/vertices help define the orientation.

---

## Creating and Merging Mesh Elements

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/create_elements.htm

**Contents:**
- Creating and Merging Mesh Elements
- Creating Mesh Elements
  - Creating Hex and Tet Elements
  - Creating Wedge Elements
  - Creating Face and Tri Elements
  - Creating Edge Elements
  - Creating Nodes
- Merging Nodes

The following forms of the create and merge commands operate on meshed entities only. They allow low-level editing of meshes to make minor corrections to a mostly correct mesh. They are not designed for major modifications to existing meshes. Because Cubit's display routines were not designed with these type of operations in mind, these commands may cause the current display of the affected entities to take an unexpected form. An appropriate drawing command can be used to return the display to the desired view.

The delete commands for deleting individual elements are still under development, but they may be used after setting a developer flag.

The create command uses existing mesh nodes to create new mesh entities.

Create {Hex|Tet} Node <range> [Owner Volume <id>]

Using the nodes specified, this form of the command creates a new hex or tet that will be owned by the specified volume. For a hex, 8 nodes are required. The order in which the nodes are specified is very important. They should describe two opposing faces of the hex; the normal of the first face should point into the hex and the normal of the second face should point out of the hex. For example, to create the hex shown in Figure 1 below, the following command would be entered:

create hex node 1,2,3,4,5,6,7,8 owner volume 1

Figure 1. Node Numbering for the Create Hex command

To create a tet, 4 nodes are specified. The base is specified as a tri with the normal point toward the fourth node using the right hand rule. To create the tet shown in Figure 2, the following command would be entered:

create tet node 1,2,3,4 owner volume 1

Figure 2. Node ordering for Create Tet Command

Create Wedge Node <range> [Owner Volume <id>]

create wedge node 1,2,3,4,5,6 owner volume 1

Figure 3. Node ordering for Create Wedge Command

Create {Face|Tri} Node <range> [Owner {Volume|Surface} <id>]

The next form of the command creates a face or tri that will be owned by the specified volume or surface. Four nodes are specified for a face, three nodes for a tri. The nodes should be specified in the order needed to produce a face or tri with the normal in the desired direction using the right hand rule.

Create Edge Node <range> [Owner {Volume|Surface|Curve} <id>]

This form of the command creates an edge that will be owned by the specified volume, surface, or curve. Two nodes must be specified; order is unimportant.

Create Node Location <x> <y> <z> Owner {Volume|Surface|Curve|Vertex} <id>

The last form of the command creates a node at the specified location that will be owned by the specified volume, surface, curve, or vertex. The location is specified by three absolute values that represent the position of the node in 3D space.

The merge node command is used to join two mesh entities one node at a time. It should be used with care because merging nodes of different meshed entities may have unpredictable results. The syntax is:

Merge Node <id1> <id2>

The merge node command replaces the node specified as id1 with the node id2. The command is equivalent to deleting node id1 and creating node id2 in the same location. The resultant merged node takes on the characteristics of the replaced node such as position and owner. This may include some or all of the higher level mesh entities related to the merged node.

Caution should be taken when using the merge node command because other commands involving the related meshed entities may not work properly following the merge.

---

## Creating Cohesive Elements

**URL:** https://coreform.com/cubit_help/mesh_generation/cohesive.htm

**Contents:**
- Creating Cohesive Elements

Create Cohesive Elements Block <value> Surface <ids>

The Block keyword indicates the block id for the newly created block.

The Surface keyword indicates which surfaces to unmerge and insert cohesive elements..

Create Cohesive Elements Block <value> [Tri <ids>] [Face <ids>]

---

## Curvature

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/curvature.htm

**Contents:**
- Curvature

Summary: Meshes curves by adapting the interval size to the local curvature.

Curve <range> Scheme Curvature <double>

The value of <double> controls the degree of adaptation. If zero, the resulting mesh will have nearly equal intervals. If greater than zero, the smallest intervals will correspond to the locations of largest curvature. If less than zero, the largest intervals will correspond to the locations of largest curvature. The default value of <double> is zero. Straight lines and circular arcs will produce meshes with near-equal intervals. The method for generating this mesh is iterative and may sometimes not converge. If the method does not converge, either the <double> is too large (over-adaptation) or the number of intervals is too small. Currently, the scheme does not work on periodic curves.

---

## Curvature Sizing Function

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/curvature_sizing_function.htm

**Contents:**
- Curvature Sizing Function

The Curvature sizing function determines element size based on the curvature evaluation of a surface at the current location. Two surface curvature values (taken perpendicular to each other) are compared at the location of interest, and the largest is used as the sizing function for the mesh. Figure 1 shows a solid with a highly deformed surface which displays rapid change of surface curvature at several locations.

Figure 1. NURB solid with high surface curvature change

Figure 2 depicts a normal paved mesh of this surface using a common size on all bounding curves and no sizing function in the interior. The total number of quadrilateral shell elements for this case is 1988. Figure 3 shows a mesh which was generated with the curvature sizing function option. The mesh is graded denser in the regions of quickly changing curvature, such as at the tops of the hills and at the bottom of the valley. Due to the intense interrogation of the underlying geometric modeler which the curvature method relies on, this option can be very computationally expensive.

Figure 2. NURB mesh with no interior sizing function

Figure 3. NURB mesh with curvature sizing function

---

## Deleting Mesh Elements

**URL:** https://coreform.com/cubit_help/appendix/alpha/delete_elements.htm

**Contents:**
- Deleting Mesh Elements

Element deletion for owned geometry is no longer available unless the developer flag is turned on. Element deletion is still available without the developer flag for free meshes. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

The following forms of the delete commands operate on meshed entities only. They allow low-level editing of meshes to make minor corrections to a mostly correct mesh. They are not designed for major modifications to existing meshes. Because Cubit's display routines were not designed with these type of operations in mind, these commands may cause the current display of the affected entities to take an unexpected form. An appropriate drawing command can used to return the display to the desired view.

When deleting elements, the default behavior will be that the child mesh entities will be deleted when they become orphaned. For example, when a hex is deleted, if its faces, edges and vertices are no longer used by adjacent hex elements, then they will also be deleted. The no_propagate option will leave any child mesh entities regardless if they become orphaned.

The delete command removes one or more mesh entities from an existing mesh. Additional mesh entities may be deleted as well depending on the particular form of the command. Exactly which entities are removed is explained in the following descriptions.

Delete {Hex|Tet} <range> [No_Propagate]

Deletes the specified hexes or tets. All associated tris, faces, edges, and nodes are also deleted unless the no_propagate option is given.

Deletes the specified wedges. No other mesh entities are affected.

Delete {Face|Tri} <range> [No_Propagate]

Deletes the specified faces or tris. For faces, all hexes that contain the face are also deleted. For tris, all tets that contain the tri are also deleted. All associated edges and nodes are also deleted unless the no_propagate option is given.

Delete Edge <range> [No_Propagate]

Deletes the specified edges. Any associated tris, faces, hexes, and tets are also deleted. Any associated nodes are also deleted unless the no_propagate option is given.

Deletes the specified nodes. Any associated edges, tris, faces, hexes, and tets are also deleted.

---

## Edge Length

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/edge_length.htm

**Contents:**
- Edge Length

Summary: This smoother tries to make all edge lengths equal

Surface <range> Smooth Scheme Edge Length

Edge Length smoothing in Cubit is provided by MESQUITE, a mesh optimization toolkit by Argonne National Laboratory and Sandia National Laboratories. (See Brewer, et al. 2003 for more details on the MESQUITE toolkit.) This smooth scheme may be useful for lengthening the shortest edge length in paved meshes.

Interior node positions are adjusted in an optimization loop where the optimal element has an ideal shape (square) and has an area equal to the average element area of the input mesh.

NOTE: This smoother should be avoided when the mesh contains high aspect-ratio elements that the user wants to keep.

Because this smoother essentially tries to make all the edge lengths equal, it is designed to work well on meshes whose elements have aspect ratios close to 1. The farther from 1 the aspect ratio is, the less applicable this smoother will be.

---

## Equal

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/equal.htm

**Contents:**
- Equal

Summary: Meshes a curve with equally-spaced nodes

Curve <range> Scheme Equal

See Interval Assignment for a description of how to set the number of nodes or the node spacing on a curve.

---

## Equipotential

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/equipotential.htm

**Contents:**
- Equipotential

Applies to: Volume Meshes

Summary: Attempts to equalize the volume of elements attached to each node

Volume <range> Smooth Scheme Equipotential [Free]

This smoother is a variation of the Equipotential (Jones, 74) algorithm that has been extended to manage non-regular grids (Tipton, 90). This method tends to equalize element volumes as it adjusts nodal locations. The advantage of the equipotential method is its tendency to "pull in" badly shaped meshes. This capability is not without cost: the equipotential method may take longer to converge or may be divergent. To impose an equipotential smooth on a volume, each element must be smoothed in every iteration--a typically expensive computation. While a Laplacian method can complete smoothing operations with only local nodal calculations, the equipotential method requires complete domain information to operate.

The free option allows the nodes on the boundary (surfaces and curves) to be moved during the smooth operation.

---

## Exodus II-based Field Function

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/exodus2_field_function.htm

**Contents:**
- Exodus II-based Field Function
- Surface/Curve Meshing with Exodus II - based Field Functions

The ability to specify the size of elements based on a general field function is also available in CUBIT. With this capability, the desired element size can be determined using a field variable read from a time-dependent variable in an Exodus II file. Both quadrilateral and triangle elements are supported for surfaces, and both tetrahedral and hexahedral elements are supported for volumes.

A field function is a time-dependent variable in an Exodus II file. Either node-based or element-based variables may be used. Currently, field functions are imported from element and node-based Exodus II data. The mesh block containing the corresponding elements must be imported along with the field function data.

Exodus variable-based adaptive meshing is accomplished in CUBIT in several steps:

Importing a field function, and normalizing that function are done in two separate steps to allow renormalization. The following command is used to read in a mesh for the field function:

Import Sizing Function '<exodusII_filename>' Block <block_id> Variable `<variable_name>' [Time <time_val> | Step <step> | Last] [Deformed]

The block_id is the element block to be read, which can be a single block id or the word all. The variable_name is an Exodus time-dependent variable name (either element-based or nodal-based) which values are used to drive the mesh size. The timestep for the time-dependent variable can be specified as a time with a value, as a step with an index or Last to use the last timestep in the file. The Deformed keyword indicates whether to read the deformed field function mesh, which should align with the geometry being meshed and needs to be accounted for in the field function data. (For information on creating deformed geometry from EXODUSII data, see Importing 2D EXODUSII Files and Importing EXODUSII Files) .

Note that when a field function is read in, the mesh is stored in the background, and therefore the geometry is not considered meshed. Also note that if deformation is not being modeled, the geometry should be in the same state as it was when that mesh was written (see Importing a Mesh for more details on importing meshes).

Once the field function has been read in, it can be normalized before being used to generate a mesh. The normalization parameters (Min_size and Max_size) are specified in the same command that is used to specify the sizing function type for the surface or volume. The syntax of these commands are:

Surface <id> Sizing Function Type Exodus [Min_size <min_val> Max_size <max_val> Log_Map Inverse_Map Scale_Mesh_Multiplier <value>]

Volume <id> Sizing Function Type Exodus [Min_size <min_val> Max_size <max_val> Log_Map Inverse_Map Scale_Mesh_Multiplier <value>]

If normalization parameters are specified, the field function is normalized so that its range falls between the minimum and maximum values input. If an element-based variable is used for the sizing function each node is assigned a value that is the average of variables on all connected elements. Nodal variables are used directly.

The Log_Map option maps the range so that it is logarithmic, base 10.

Inverse_Map flips the mapping so that smaller and larger values in the mapping generate larger and smaller elements respectively. See figure 1 below.

Figure 1. Effect of 'inverse_map' option

Scale_Mesh_Multiplier scales the size that the field data ultimately yields.

After the sizing function normalization, the geometry may be meshed using the normal meshing command.

For example, the left image in Figure 2 depicts a plastic strain metric which was generated by PRONTO-3D [Taylor, 89] a transient solid dynamics solver, and recorded into an ExodusII data file. When the file is read back into CUBIT, the paving algorithm is driven by the function values at the original node locations, resulting in an adaptively generated mesh [Attaway, 93]. The right image in Figure 1 depicts the resulting mesh from this plastic strain objective function.

Figure 2. Plastic strain metric and the adaptively generated mesh

While adaptively meshing a surface using a field function, the curves will be meshed using the Exodus II information. To override this, curves may have their meshing scheme set to equal or some other desired scheme. While adaptively meshing a volume using a field function, the surfaces and curves will be meshed using the Exodus II information. To override this for a surface, one can set the sizing function to "none" for that surface.

---

## Explicit Specification of Intervals

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/explicit_specification.htm

**Contents:**
- Explicit Specification of Intervals

The density of mesh edges along curves is specified by setting the actual number of intervals or by specifying a desired interval size. The number of intervals can be explicitly set curve by curve, or implicitly set by specifying the intervals on a surface or volume containing that edge. For example, setting the intervals for a volume sets the intervals on all curves in that volume.

The command to specify the number of intervals at the command line is:

{Curve|Surface|Volume|Body|Group} <range> Interval <intervals>

When setting interval counts for surfaces, volumes, bodies and groups, an interval's firmness of soft is assigned to the owned curves. When setting the interval count for a curve, a firmness of hard is assigned.

The user can scale the current intervals with the following commands. Scaling is done on an entity by entity basis.

{Curve|Surface|Volume|Body|Group} <range> Interval Factor <factor>

---

## Explicit Specification of Intervals Using Interval Size

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/explicit_specification_of_intervals_using_interval_size.htm

**Contents:**
- Explicit Specification of Intervals Using Interval Size

The number of intervals along curves can be specifying by setting a desired interval size. The interval size can be explicitly set curve by curve, or indirectly set by specifying the interval size on a surface or volume containing that curve. The size for an entity is determined with the following method. If the entity has a size explicitly set then that size is used. Otherwise the entity averages the size determined for its parents. If an entity doesn't have any parents then a size is automatically calculated from all of the geometry in the model. If the auto size functionality is turned off then a default size of 1.0 is used. Some meshing algorithms may calculate a different default size.

For example, Suppose you have two volumes that share a face and corresponding curves. If the size on volume one is set to 1.0 and the size on volume two is set to 3.0 then the size for the common face will be set to 2.0. The size for the remaining faces on volume one and two will be 1.0 and 3.0 respectively. The size for the common curves will be set to 2.0.

The command to specify the interval size at the command line is:

{Curve|Surface|Volume|Body|Group} <range> [Interval] Size <interval_size>

Interval sizes set directly on an entity are given the type “user_set”. Interval sizes determined from parents or automatically calculated are give the type “calculated”.

When interval matching or meshing the interval count for each curve is computed by dividing the curve's arc length by the specified interval size. Interval counts calculated in this manner are considered to have a default firmness of soft.

The user can scale the current intervals or size with the following commands. Scaling is done on an entity by entity basis.

{Curve|Surface|Volume|Body|Group} <range> [Interval] Size Factor <factor>

---

## Finding Intersecting Mesh

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/find_intersecting_mesh.htm

**Contents:**
- Finding Intersecting Mesh
- Finding Intersecting 2D Mesh
- Facetted Representation
- Drawing Mesh Intersection
- Finding Intersecting 3D Mesh

The find mesh intersection capability finds intersecting mesh between blocks, bodies, volumes, or surfaces. This command is useful for identifying cases where the geometry does not intersect but the mesh does. The command can find intersecting 2-dimensional mesh by specifying a list of surfaces, or 3-dimensional mesh by specifying blocks, bodies, or volumes. Surfaces that have mesh between them that intersects within a tolerance of 1e-6 are located. Finding surfaces with intersecting mesh is done using the command:

Find Mesh Intersection {Block|Body|Surface|Volume} <id_list> [with {Block|Body|Surface|Volume} <id_list>] [low <value=0.0001>] [high <value>] [exhaustive] [worst <num_worst>] [draw] [log] [group<'name'>]

To find intersections between 2-dimensional mesh surfaces must be specified. If intersections are found, the surfaces containing the intersecting mesh are drawn (Figure 1) and the put into a group named 'surf_intersect', unless the user has specified another name using the group <'name'> option. Also, the ids of the intersecting surface pairs are printed to the terminal,

Figure 1. "Find mesh intersection surface all"

The draw option will draw the surfaces and intersecting mesh in wire frame mode, allowing the user to see exactly where on the surface the mesh intersection is (Figure 2).

Figure 2. "Find mesh intersection surface all draw"

Detecting mesh intersections between surfaces works entirely off of the mesh, converting the mesh into triangular facets. (The facetted representation is what you see in a shaded view in the graphics). For example, a quad is split into two triangles. Higher order 2D elements are split into multiple triangles.

The command below will draw the mesh intersection for only a pair of surfaces. The surfaces and intersecting mesh are drawn in wire frame mode, allowing the user to see exactly where on the surface the mesh intersection is.

Draw Surface <id> <id> mesh intersection [add] [include_volume]

Figure 3. Draw Mesh Intersection

With 3-dimensional entities mesh element intersections can be located by specifying entities: blocks, bodies, or volumes. If intersections are found the intersecting elements are put into a group named 'mesh_intersect' unless the user has specified another name using the group <'name'> option. Data is printed to the terminal detailing the intersections. The largest intersection value is reported for each pair of intersecting entities (blocks, volumes, or bodies). This value is the fraction of an element's volume (which element belongs to the entity in the first column) that intersects elements belonging to the entity in the second column. See Figure 5 below. The information printed in columns from left to right is:

Figure 5. "Find mesh intersection block all draw"

If the with option is used, the user specifies additional entities. The additional entities will not be reported in the first column of the output. This allows the user to focus on entities of interest without outputting too much data to the terminal. See Figure 6 below.

Figure 6. "Find mesh intersection block 1 with block all"

The low and high options set how much cumulative intersection should be detected. A low value of 0.1 would ignore elements that do not intersect more than 10% of their volume. Similarly, a high value of 0.5 would discard elements that intersect more than 50% of their volume. Both low and high can be used simultaneously. The default for the low value is 0.0001

The exhaustive option examines all elements for intersection. The default is to only examine elements with nodes on the boundary of the specified entities, anticipating that the intersections will occur mostly at boundaries.

The worst parameter limits the printout to the 'n' worst entities with elements of the highest intersections. The intersection fraction reported here is the cumulative intersection an element has with elements of all other entities in the check.

The draw option draws the intersecting elements using a color spectrum, red corresponding to high intersection and green to low. The color is according to cumulative intersection, as described in the worst option.

If the log option is specified, the output from the command will also be sent to a file named "mesh_intersection01.txt", with the number used in the file name incremented as needed. This becomes useful when you have hundreds of volumes with intersections.

---

## Free Meshes

**URL:** https://coreform.com/cubit_help/mesh_generation/freemesh.htm

**Contents:**
- Free Meshes
- Creating a free mesh
  - Disassociating a mesh from its geometry
- Creating Mesh-Based Geometry to fit a Free Mesh
- Merging a free mesh
- Free Mesh Transformation Operations
  - Extruding Mesh Elements
  - Offsetting Mesh Elements
  - Revolving Mesh Elements
- Smoothing a free mesh

A free mesh is a mesh that is not associated with any underlying geometric entities. A free mesh contains only mesh elements (hexahedra, triangles, edges, nodes, etc), and not volumes, surfaces, etc. Since there is no underlying geometry, operations on free meshes are limited. The following operations can be performed on free meshes in some capacity:

A free mesh can be created in three ways.

The command to disassociate a mesh from existing geometry is:

Disassociate Mesh [From] {Volume|Surface|Curve|Vertex} <id_range>

brick x 10 mesh volume all disassociate mesh from volume 1 delete volume 1

When a mesh is disassociated from its geometry, a group called 'disassociate elements' is created to contain the free mesh.

It is possible to create underlying mesh-based geometry to own a free mesh. It is similar in functionality to the Import Mesh Geometry command, but it does not require the extra import/export step. For example, a user would be able to read in a free mesh, fix any mesh problems, and then create the mesh-based geometry without having to write the mesh to a file first. The command syntax is:

Create Mesh Geometry {Hex|Tet|Face|Tri|Block} <range> [no_nodeset] [no_sideset] [exclude block <range>] [Feature_Angle <angle=135>] [Acis] [Keep]

The command also applies to any subset of the mesh. For example, you can create mesh geometry for a group of hexes or element blocks.

If the keep option is specified, the mesh will be duplicated so you will have two copies of the mesh: The original mesh and the new mesh that is owned by the new MBG geometry. If the keep option is not specified, the existing mesh will be reused, and duplicate elements will not be created. Elements will now be owned by the new MBG geometry. The command will check for mesh ownership and will issue a warning. Use the keep option if the mesh is already owned. The keep option is not specified by default.

By default, genesis entities will be used as criteria for building the new MBG geometry. The no_nodeset and no_sideset options can be specified to prevent this. Any genesis entities defined on the free mesh are transferred to the new MBG geometry. When the keep option is used copies of genesis entities are made on the new MBG geometry.

The exclude block option excludes specified blocks from feature angle detection. Any volumes created from these excluded blocks will have only one surface.

The Acis option will attempt to create ACIS geometry from the mesh. This option is an alpha feature and can only be used if developer commands have been turned on. For more detail see: Acis Geometry From Mesh

To merge two free meshes, the equivalence command may be used. The command syntax is:

Equivalence Node <range> [Tolerance <value>] [Preview]

All nodes in the given range that are within the specified tolerance will be merged. The merged and unchanged (unmerged) nodes are put into groups. The maximum distance between merged nodes, and the minimum distance between unmerged nodes, are listed for the user because if these values are close together it can indicate a problem with the Tolerance. Nodes within tolerance and part of the same element will not be merged. This prevents collapsing elements into degenerate forms. With the Preview option, the nodes aren't actually merged, but the ones that would have merged are drawn and grouped. For example:

br x 10 volume 1 copy move x 10 mesh volume all disassociate mesh from volume 1 2 delete volume 1 2 equivalence node all tolerance 0.05 ## merges all nodes that are within 0.05 of each other

Mesh transformations for free meshes are achieved through the use of the group transformation commands, given in Basic Group Operations. All members of a free mesh are automatically assigned to a group. These groups can then be modified using group operations. The following command sequence illustrates how transformations might be applied to a free mesh.

brick x 10 mesh volume 1 disassociate mesh from volume 1 delete volume 1 group disassociated_elements move x 10 group disassociated_elements rotate 15 about x group disassociated_elements scale 0.25 group disassociated_elements reflect 1 1 0 group 'node_group' add node 1 to 121 group node_group move z 5 ##The moved nodes do not also move the attached geometry, as one might expect.

If a group is composed of mesh entities, these commands will only operate on the nodes in the group. All nodes of the group will be moved, scaled, rotated, or reflected as specified. If there are no nodes in the group, Cubit will return an error. Including all nodes in the group will transform the whole model. Including only a subset of nodes will transform those nodes and their enclosed elements, but it will not transform the whole mesh.

Disassociated mesh elements cannot be copied using the Group copy commands. To create a copy they must be exported and reimported. Alternatively, they can be associated with mesh-based geometry, and then copied using the typical copy commands.

Mesh elements can be extruded to create new elements from existing nodes, edges, faces or triangles. There are two forms of the extrude command as follows:

Create Element Extrude {Node|Edge|Face|Tri} <element_list> Direction <options> [Distance <value>] {Layers <num_layers | {bias_first_size <value> factor <value>}} [Twist <angle> Axis <axis_options>] [flatten] [group_target]

Create Element Extrude {Node|Edge|Face|Tri} <element_list> Along Curve <curve_list> [Layers <num_layers]

In the first form of the command, a direction and distance are specified to define the extrusion. To define node spacing along the extrusion, the command takes either the layers or bias_first_size and factor parameters, but not both. Specifying a value for the layers option determines how many evenly sized elements will be created in the given distance. The bias_first_size and factor parameters define a bias that will be used along the extrusion distance. When specifying entities to be extruded which are either non-planar, or not orthogonal to the extrusion direction, the flatten parameter results in the extrusion terminating on a single plane orthogonal to the extrusion direction. The optional group_target parameter places all of the faces, tris, edges, or nodes at the end of the extrusion into a group named "extruded_target" which can be conveniently used to define a subsequent extrusion with a different set of extrusion parameters. Twist can also be specified and requires an angle of twist and a twist axis.

The figure below illustrates the new flatten, bias_first_size, factor, and group_target keywords. At the top is a set of non-planar faces to offset. On the bottom-left, each node on all of the faces are extruded the same amout resulting in a target of the extrusion with identical curvatuve to the input faces. In the bottom-middle, the flatten keyword is used, resulting in the extrusion terminating on a single plane. In the bottom-right, the bias_first_size, factor, and group_target keywords are used, resulting in a biased extrusion, and the creation of a group named "extruded_target", which contains the faces on the end of the extrusion.

In the second form, a curve is specified, along with the input entities will be extruded. Extruding along a curve supports the layers parameter, but does not currently support the distance, bias_first_size, factor, flatten, twist or group_target parameters.

#Extrude a face in a given direction: create node location 0 0 0 create node location 1 0 0 create node location 1 1 0 create node location 0 1 0 create face node 1 to 4 create element extrude face 1 direction 0 0 1 distance 3 layers 3 create element extrude face 1 direction 0 0 1 distance 3 layers 3 twist 90 axis direction 0 0 1 origin 0 0 0

#Sweep face along curve create node location 0 0 0 create node location 1 0 0 create node location 1 1 0 create node location 0 1 0 create face node 1 to 4 create vertex location position 0 0 0 create vertex location position 0 .2 1 create vertex location position 0 1 2 create vertex location position 0 3 2 create vertex location position 0 4 1 create vertex location position 0 5 0 create curve spline vertex 1 2 3 4 5 create element extrude face 1 layers 5 along curve 1

Figure 1. Extruding mesh elements along a spline

Faces and triangle elements can be used to create hexahedral and wedge elements from an offset command. The default offest direction is normal to the selected face. The Oppposite_normal option will use the reverse direction. The layers parameter determines how many elements will be created in the given direction.

Create Element Offset {Face|Tri} <element_list> [Normal_to|Opposite_normal] {Distance <value>] [Layers <num_layers>]

#Create wedge and hex elements from face and tri elements via offset create node location 0 0 0 create node location 1 0 0 create node location 1 1 0 create node location 0 1 0 create node location 2 0 1 create node location 2 1 1 create node location 1 2 0 create face node 1 to 4 create face node 3 2 5 6 create tri node 7 4 3 create tri node 7 3 6 create element offset face all tri all distance 3 layers 3 opposite_normal

Elements can be created by revolving an existing element around a given axis. The Attempt_fix parameter will try to fix any poorly formed hex elements by collapsing them into wedge elements. Angle determines the amount of rotation around the axis. The Layers option determines how many elements will be created in the given rotation. The quadratic option will result in the creation of quadratic elements. For example, it can result in HEX20 or TET10 elements being created. To further specify the element type, for the created elements, one may put them into a block.

Create Element Revolve {Edge|Face|Tri} <element_list> Axis <axis_options> Angle <angle> [Layers <num_layers>] [Attempt_fix] [quadratic]

#Revolve 2 faces around the Y-axis and collapse inner hexes to wedges create node location 0 0 0 create node location 1 0 0 create node location 1 1 0 create node location 0 1 0 create node location 2 0 0 create node location 2 1 0 create face node 1 2 3 4 create face node 2 5 6 3 create element revolve face 1 2 axis direction 0 1 0 angle 180 layers 4 attempt_fix block 1 hex all block 2 wedge all block 1 element type hex8 block 2 element type wedge6

Figure 2. Revolving free mesh elements to create hex and wedge elements

Interior nodes can be smoothed using commands such as smooth hex all, or smooth tet all in block 100. These commands will smooth only the interior node on the elements used in the command. The nodes on the boundary will remain unchanged. To smooth nodes on a boundary, the target smoothing option can be used. Targeted smoothing allows the user to smooth a group of mesh elements to a surface or curve that is not their owner. Targeted smoothing is discussed under Mesh Smoothing. The following sequence of commands illustrate the capability of smoothing a free mesh to a target surface.

sphere rad 25 webcut vol 1 plane xplane offset 18 delete vol 2 webcut volume 1 plane yplane offset 8 webcut volume 1 plane yplane offset -8 delete vol 1 3 surf 16 copy delete vol 4 surf 18 scheme pave surf 18 size 2 mesh surf 18 disassociate mesh surf 18 ##Mesh and geometry overlap refine face 1 radius 3 set developer on ## Smoothing free mesh is a developer command smooth face all scheme laplacian ##Smoothed mesh is away from surface smooth face all scheme laplacian target surface 18 ##Smoothed mesh is aligned with surface

Figure 3. Smoothing without a target (above) and smoothing to a target surface (below).

The mesh quality checks for a free mesh are the same as for other geometry-based meshes. The difference is in how you specify elements in the command. Instead of specifying volumes or surfaces you would specify groups of hexes, faces, tris, or tets. Examples are given below:

quality hex all quality face all scaled jacobian quality tet 1 to 100 draw mesh

Refinement for a free mesh is limited to refinement of mesh elements. Refinement may be accomplished by specifying groups of mesh elements which to refine using the regular refinement options. For boundary elements, the refinement scheme will use averaging methods to determine node placement, in the absence of a boundary geometry to define node placement.

A free tet mesh may be cleaned up using the Cleanup Tet command. For example

cleanup tet all #cleans up all tets cleanup tet 1 to 1000 #cleans up all tets in the range [1,1000]

It is best to specify contiguous sets of elements for this command.

Assigning boundary conditions on free meshes can be accomplished by explicitly specifying mesh elements, by creating a sideset or block from the skin of a group of elements, or by creating groups based on feature angle using the seed method. Once the group is created it is easy to assign it to a nodeset or sideset.

##Creating blocks, nodesets and sidesets on free meshes cylinder radius 3 z 12 volume 1 size 0.5 mesh volume 1 disassociate mesh from volume 1 delete volume 1 group 'mygroup1' add seed face 752 feature_angle 45 ##Groups all faces on the cylindrical surface group 'mygroup2' add seed face 752 feature_angle 45 divergence ##Groups only faces within 45 degrees of seed face sideset 1 group mygroup1 sideset 2 group mygroup2 block 1 hex all draw sideset 1 draw sideset 2 draw block 1

Figure 4. Grouping faces on free meshes using the seed method. The feature angle method is used on the left with a feature angle of 45 degrees. On the right is the result if using the divergence method.

Even though boundary conditions can be defined directly only on geometry entities, these geometry-based BCs will be maintained on the free mesh following the disassociate command. The following command line sequence illustrates this capability.

##Respecting blocks, nodesets and sidesets in mesh elements after disassociation brick x 10 mesh vol 1 sideset 1 surface 1 nodeset 1 curve 1 block 1 volume 1 disassociate mesh from volume 1 draw sideset 1 draw nodeset 1 draw block 1

The skin command takes a list of mesh elements and returns the triangles and faces on the boundary of that group. The group of elements returned from the command can be assigned to either a group, sideset, or block. Free meshes can be skinned by specifying either a list of hexahedra, a list of tetrahedra, or a list of blocks.

Typically meshes are deleted by specifying owning geometry. For free meshes, the meshes cannot be deleted in this fashion. Instead, the mesh may be deleted using the Delete mesh command. The syntax is:

This command will delete all mesh entities in the entire model. To specify groups of elements for deletion, you can use the individual deletion commands. The command to delete a group of free mesh elements is:

Delete {Node|Hex|Tet|Face|Tri} <id_range> [No_propagate]

When deleting elements, the default behavior will be that the child mesh entities will be deleted when they become orphaned. For example, when a hex is deleted, if its faces, edges and vertices are no longer used by adjacent hex elements, then they will also be deleted. The no_propagate option will leave any child mesh entities regardless if they become orphaned.

Bottom-up mesh element creation methods are available for free meshes. The difference between element creation methods for free meshes versus associated meshes is that the free meshes commands do not have a command option to associate the elements with an owning body. Otherwise the commands are identical to mesh element creation commands for associated meshes. The command syntax for free meshes is:

Create Node <x> <y> <z>

Create {Hex|Tet|Tri|Face|Edge} Node <id_range>

Free meshes can be exported as ExodusII files. All elements belonging to any block are exported. Any elements not belonging to a block will not be exported (i.e. Cubit will not assign default blocks).

---

## Generating a Finite Element Mesh from Level-set Data

**URL:** https://coreform.com/cubit_help/appendix/ato_to_mesh.htm

**Contents:**
- Generating a Finite Element Mesh from Level-set Data
- Hex Mesh Generation Using Sculpt
- Tet Mesh Generation by Remeshing Mesh Based Geometry (MBG)
- Tet Mesh Generation Using Level-set Triangulation

This documentation will describe how to generate a finite element mesh from an Exodus file that contains level-set data defined as nodal variables. This process was developed to support mesh generation for geometric designs resulting from Adaptive Topological Optimization (ATO). The output format from ATO in this case is an Exodus file containing a tetrahedral mesh with a scalar nodal variable defining a level-set that represents the bounding surfaces of the optimized volume. The process below extracts the bounding surfaces of the optimized volume by evaluating the level-set at a value of zero. These bounding surfaces are in the form of a triangulation that can then be used for generating a finite element mesh. Three methods for generating the finite element mesh will be described using a simple example model.

This section will describe the process for generating a sculpted hex mesh of the ATO design.

1. This process utilizes beta capabilities in Cubit so activate the use of beta commands.

2. Import the ATO Exodus file called “small_bracket.exo” into Cubit and use the import option that tells Cubit to import the level-set nodal variable called “LSD” (level set data).

import mesh “small_bracket.exo” nodal_var “LSD” no_geom

3. Extract the boundary surface triangulations from the level-set data. Because this creates triangles we use a variation of the “create tri …” command. We will use the “iso” option telling the command to generate the iso-surfaces from the level-set data defined by the nodal variable “LSD”. We will specify the tets to consider when doing the extraction. In this case we use “tet all” meaning all of the tets in the model. When this command is complete there will be two new blocks defined in Cubit. They will be the two blocks with the highest IDs. One of these blocks (the larger of the two block IDs) contains triangles that represent the optimized portions of the design and the other block (the smaller of the two block IDs) contains triangles on the fixed portions of the design.

create tri iso tet all nodal_var “LSD”

4. Look at the extracted iso-surface triangulations by drawing the two new blocks (blocks 3 & 4) created in step 2.

5. At this point we could smooth the new triangulations if desired but because the sculpting process will have the same effect we will skip that step here. The smoothing will be demonstrated in the next sections. We will now export the new blocks to an STL file that can then be used by the sculpt algorithm. Specify only the triangles in the new blocks. Also specify the “mesh free_mesh” options to tell the command that the triangles are not owned by geometry.

export stl “small_bracket.stl” tri in block 3 4 mesh free_mesh

6. Exit Cubit and start a Linux command prompt from which to run sculpt.

7. From the command prompt load the sierra module (this will be used later).

8. From the directory where your new stl file is launch the sculpt program. See the sculpt documentation for more details on the options for running sculpt. Here is an example of a simple sculpt command that specifies the sculpt cell size and the number of processors. The number or processors is 8 and the cell size is 0.0007.

sculpt –j 8 –cs 0.1 --stl_file “small_bracket.stl”

9. When sculpt finishes the resulting mesh will be spread across 8 files in our case since we used 8 processors. In our example the files will be named something like “small_bracket.stl_results.e.8.0” where the last number in the filename refers to which processor the file came from. To concatenate all of the files into one use the “epu” command from the Sierra suite of tools.

epu –auto small_bracket.stl_results.e.8.0

10. Start Cubit up and load the mesh file created by sculpt.

import mesh “small_bracket.stl_results.e” no_geom

This section will describe the process for generating a tet mesh by meshing a mesh based geometry (MBG) representation of the optimized part.

1. This process utilizes beta capabilities in Cubit so activate the use of beta commands.

2. Import the ATO Exodus file called “small_bracket.exo” into Cubit and use the import option that tells Cubit to import the level-set nodal variable called “LSD” (level set data).

import mesh “small_bracket.exo” nodal_var “LSD” no_geom

3. Extract the boundary surface triangulations from the level-set data. Because this creates triangles we use a variation of the “create tri …” command. We will use the “iso” option telling the command to generate the iso-surfaces from the level-set data defined by the nodal variable “LSD”. We will specify the tets to consider when doing the extraction. In this case we use “tet all” meaning all of the tets in the model. When this command is complete there will be two new blocks defined in Cubit. They will be the two blocks with the highest IDs. One of these blocks (the larger of the two block IDs) contains triangles that represent the optimized portions of the design and the other block (the smaller of the two block IDs) contains triangles on the fixed portions of the design.

create tri iso tet all nodal_var “LSD”

4. Look at the extracted iso-surface triangulations by drawing the two new blocks (blocks 3 & 4) created in step 2.

5. Export the new blocks to an Exodus file so that they are disconnected from the original tet mesh.

export mesh “small_bracket_iso.e” block 3 4

7. Load the new file that just contains the new blocks.

import mesh “small_bracket_iso.e” no_geom

8. Smooth the optimized part of the triangulation. This will be the triangles in the block with the larger id (4 in our case). We will do this by first fixing the node positions of all of the nodes in the non-optimized part of the triangulation and then smoothing the triangles in the optimized portion. When smoothing we need to use the “target free mesh” option to tell the command to project the smoothed results back to the original triangulation to try to preserve volume. We use the “iteration” option to limit the number of iterations the smoother does.

node in tri in block 3 position fixed

smooth tri in block 4 target free mesh iteration 5

9. Create mesh based geometry from the triangulation. For small models this can be done immediately with the commands below (first command creates surfaces and the second command stitches them together to form a closed volume). For larger models it may be faster to export the mesh to a file, reset Cubit, and then re-import the mesh with the “geom” option on so that mesh based geometry is generated on import. Current limitations in Cubit result in this performance difference.

create mesh geom tri all

10. Set the size and scheme on the new volume and mesh it.

volume all scheme tetmesh

This section will describe the process for generating a tet mesh using the triangulation from the level-set extraction.

1. This process utilizes beta capabilities in Cubit so activate the use of beta commands.

2. Import the ATO Exodus file called “small_bracket.exo” into Cubit and use the import option that tells Cubit to import the level-set nodal variable called “LSD” (level set data).

import mesh “small_bracket.exo” nodal_var “LSD” no_geom

3. Extract the boundary surface triangulations from the level-set data. Because this creates triangles we use a variation of the “create tri …” command. We will use the “iso” option telling the command to generate the iso-surfaces from the level-set data defined by the nodal variable “LSD”. We will specify the tets to consider when doing the extraction. In this case we use “tet all” meaning all of the tets in the model. When this command is complete there will be two new blocks defined in Cubit. They will be the two blocks with the highest IDs. One of these blocks (the larger of the two block IDs) contains triangles that represent the optimized portions of the design and the other block (the smaller of the two block IDs) contains triangles on the fixed portions of the design.

create tri iso tet all nodal_var “LSD”

4. Look at the extracted iso-surface triangulations by drawing the two new blocks (blocks 3 & 4) created in step 2.

5. Export the new blocks to an Exodus file so that they are disconnected from the original tet mesh.

export mesh “small_bracket_iso.e” block 3 4

7. Load the new file that just contains the new blocks.

import mesh “small_bracket_iso.e” no_geom

8. Smooth the optimized part of the triangulation. This will be the triangles in the block with the larger id (4 in our case). We will do this by first fixing the node positions of all of the nodes in the non-optimized part of the triangulation and then smoothing the triangles in the optimized portion. When smoothing we need to use the “target free mesh” option to tell the command to project the smoothed results back to the original triangulation to try to preserve volume. We use the “iteration” option to limit the number of iterations the smoother does.

node in tri in block 3 position fixed

smooth tri in block 4 target free mesh iteration 5

9. Sometimes we will also want to smooth the edges on the “curves” in-between the optimized and non-optimized regions. To do this we will first “un-fix” the node positions we fixed in the previous step. Then we will create a group with all of the edges in the optimized region and a group with all of the edges in the non-optimized region. Then we will intersect these two groups to get the edges that are in-between these two regions. Then we can smooth those edges. Finally, we will smooth the surfaces in the optimized region again. You may also wish to smooth the tris in the non-optimized region but this will require some more sophistication in fixing node positions so as not to lose sharp features in the model. This example shows one specific smoothing sequence. You may prefer other approaches.

node in tri in block 3 position free

group “opt_edges” add edge in tri in block 4

group “non_opt_edges” add edge in tri in block 3

group “int_edges” intersect opt_edges with non_opt_edges

smooth edge in int_edges target free mesh

node in edge in int_edges position fixed

smooth tri in block 4 target free mesh iteration 5

10. Once we get a decent surface triangle mesh we can tet mesh the interior.

---

## Generating a Mesh in ITEM

**URL:** https://coreform.com/cubit_help/item/meshing.htm

**Contents:**
- Generating a Mesh in ITEM
- ITEM Meshing Suggestions

The mesh generation panel in ITEM is different from the other panels in Cubit. Meshing errors can arise from a number of different problems. Many of these problems are caused from improper geometry preparation/cleanup. Other problems can be caused from improper interval settings, or meshing schemes. Instead of suggesting specific operations as it does on other panels, the meshing panel in ITEM will suggest several possible solutions based on the error message output. Each of these solutions may require significant user input, and may require you to revisit previous ITEM panels or Control panels. To open the appropriate Control panel, you can right click on the solution and select "Show Command Panel". For convenience, these general solutions are described here, including which ITEM panels and which Control panels they refer to. References to help topics are also included.

Figure 1. ITEM Mesh Panel

Diagnostic: This solution message appears when auto scheme selection fails. There are many reasons that auto scheme selection may have failed. Check to make sure that your volume is broken up into meshable parts. For sweepable volumes, this means that each volume should only have one target surface.

Action: Right-clicking on this solution and selecting the "Show command panel" option will open the webcutting commands on the control panel. Alternatively, you can also return to the ITEM decomposition panel for more webcutting suggestions.

Diagnostic: This solution message appears when auto scheme selection fails, interval matching fails, or interval assignments fail. Setting the schemes manually may help resolve some of these issues. It may also help to set source and target surfaces explicitly for swept meshes.

Action: The volume schemes can be set explicitly from the Volume-Mesh control panel. The "Set Source and Target" panel in ITEM can be used to aid in setting explicit source and target surfaces for swept meshes.

Diagnostic: This solution message appears for many reasons: auto scheme selection fails, interval matching fails, interval assignments fail, inconsistent edge-face ratios, odd number of intervals on a paver loop, or connectivity problems. Setting explicit intervals may be necessary

Action: The volume mesh intervals can be set explicitly from the Volume-Interval control panel. The "Set Element Sizes" panel in ITEM can be used to aid in setting explicit sizes and sizing functions for meshes.

Diagnostic: This solution message appears when auto-scheme selection fails. A model may contain small curves or surfaces that need to be composited with adjacent surfaces. Or it may just contain more detail than is needed for analysis. Compositing surfaces and curves does not affect the underlying geometry.

Action: The Remove Small Features or Force Sweep Topology panels in ITEM may suggest several possible candidates for compositing. The Surface-Modify-Composite or the Curve-Modify-Composite panels can be used to composite surfaces or curves respectively. These panels are also used to delete virtual geometry from curves or surfaces.

Removing Small and Narrow Features describes using ITEM to remove small and narrow features in your model. Forced Sweepability describes using ITEM to force sweepability using virtual geometry. Composite Curves explains how to composite curves in Cubit. Composite Surfaces explains how to composite surfaces in Cubit. Decomposition Tutorial Example 7 has an example of using composite curves to improve meshability. Power Tools Tutorial has another example of using composite geometry.

Diagnostic: This solution message appears when auto-scheme selection fails. Collapsing a surface involves splitting a surface, and compositing it with adjacent surfaces.

Action: The Remove Small Features panel in ITEM may suggest several possible candidates for collapse. The Surface-Modify-Collapse, Curve-Modify-Collapse, or Vertex-Modify-Collapse Angle panels can also be used to collapse surfaces, curves, or angles respectively.

Diagnostic: This solution message appears when auto-scheme selection fails. Removing unnecessary surfaces may improve meshability.

Action: The Remove Small Features panel in ITEM may suggest several possible candidates for removal. The Surface-Modify-Tweak panel, Surface-Modify-Remove panel, Curve-Modify-Tweak or the Volume-Modify-Remove Slivers panels are also used to remove unnecessary features in a model.

Diagnostic: This solution message appears when mesh generation creates poor quality elements, particularly if it creates inverted or "negative Jacobian" elements. In some cases, smoothing a mesh may get rid of these bad elements.

Action: Depending on the geometry type, the smoothing panel can be accessed from the Control panel under Volume-Smooth or Surface-Smooth panels. It is also helpful to use the Validate Mesh page in ITEM for assessing quality metrics.

Diagnostic: This solution message appears when mesh generation creates a poor quality mesh, due to negative Jacobians, inconsistent edge-face ratios, connectivity problems, or any other invalid mesh configuration. Mesh generation can be a very iterative process. It is sometimes necessary to delete a mesh and try different schemes, sizes, or even just change the meshing order. Sometimes you must further decompose or modify your geometry to get it to mesh.

Action: To delete a mesh, you can select it in the graphics window and choose Delete Mesh from the right-click context menu. You can also delete a mesh from any of the Mesh-Entity-Delete panels on the Control Panel.

Diagnostic: This solution message appears when mesh generation fails to assign valid vertex types on mapped or submapped surfaces.

Action:To change the vertex type on a surface, select the Surface-Mesh-Submap-Advanced or Surface-Mesh-Map-Advanced panels. From here you can assign and view vertex types.

---

## Geometry Adaptive Sizing for TriMesh and TetMesh Schemes

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/geometry_adaptive_meshgems.htm

**Contents:**
- Geometry Adaptive Sizing for TriMesh and TetMesh Schemes

The TriMesh and TetMesh schemes in Cubit are based upon third party libraries known as MeshGems that are developed and distributed by Distene. They are robust and fast triangle and tet meshing algorithms that have built in capabilities for adaptively controlling the mesh size based upon feature sizes. In most cases the sizing controls provided as part of the scheme command are sufficient to control mesh sizes. As such, the sizing functions described in this section cannot be used with the the MeshGems triangle and tet meshing algorithms. If a sizing function is assigned to a volume or surface, and the TriMesh or TetMesh scheme is selected, rather than using the MeshGems algorithm for meshing the surfaces, it will automatically revert to using the TriAdvance scheme. Any settings defined with the TriMesh or TetMesh scheme will be ignored and the sizing function will be used to determine local mesh sizes.

When using the TriMesh and TetMesh schemes, recommended practice is to mesh all surfaces and volumes simultaneously. This provides the greatest flexibility to the algorithms to determine feature sizes and their effect on neighboring surfaces and volumes. The default settings for TriMesh and TetMesh schemes will automatically provide geometry adaptive mesh sizing. These default settings can however be adjusted by using the settings on the scheme command. The scheme settings are described in the TetMesh and TriMesh sections of the documentation.

---

## Geometry Adaptive Sizing Function (Skeleton Sizing)

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/geom_adaptive_sizing_function.htm

**Contents:**
- Geometry Adaptive Sizing Function (Skeleton Sizing)
- Skeleton Sizing Behaviors
- Command Line Syntax
- Basic Arguments
  - Scaling and Accuracy Arguments:
- Advanced Arguments
  - Lattice Arguments:
  - Source Entity Arguments
- Adding User Specified Sizing Sources
- Skeleton with Other Sizing Controls

The Geometry Adaptive Sizing Function, also referred to as the Skeleton Sizing Function (Quadros 2005; Quadros 2004; Quadros 2004(2)), automatically generates a mesh sizing function based upon geometric properties of the model. This sizing scheme attempts to create a sizing function that allows unstructured meshing schemes to generate a mesh with the following properties:

The geometry adaptive sizing function can be used to create sizing information for surfaces, solids, and assemblies.

This sizing function uses geometric properties to influence mesh size. The scheme calculates or estimates:

These properties are then used to calculate a sizing function throughout the geometric entity (or entities). Regions of relatively high complexity will have a fine mesh size, while regions of relatively low complexity will have a coarse mesh size. For example, generally, a high-curvature region on a surface will have a finer mesh size than a low-curvature region on that surface

Figure 1: Overview of Computational Framework

Figure 2: Skeleton Sizing Function example in the GUI

Skeleton sizing can be specified on single or multiple surface(s)/volume(s) at a time from the GUI (Meshing Control Panel) or the command-line. The following describes how specifying sizing on entities can change skeleton sizing’s behavior:

Single surfaces/volumes – If skeleton sizing is applied to surfaces/volumes one at a time, each entity’s sizing is not influenced by the others. On the command-line, issue a separate command for each entity. In the GUI, specify only one surface or volume before selecting “Apply Size”.

Multiple surfaces – If skeleton sizing is applied on multiple surfaces together, then geometric features of a particular surface may affect its neighboring surfaces.

Multiple volumes (assembly sizing) – Skeleton sizing can be applied to assembly models so that geometric features of a volume may influence its neighbors. Volumes should first be imprinted and merged before they are specified together for skeleton sizing.

Surface <surface_id_range> Sizing Function Skeleton {[scale <1 to 10 = 7>] [time_accuracy_level <1 to 3 = 2>] [min_depth <3 to 8 = 5>] [max_depth <4 to 9 = 7>] [facet_extract_ang <1 to 30 = 10>] [min_num_layers_2d < 1 to N = 1>] [min_num_layers_1d < 1 to N = 1>] [max_span_ang_surf <5.0 to 75.0 = 45.0 degrees>] [max_span_ang_curve <5.0 to 75.0 = 45.0 degrees>] [min_size <float>] [max_size <float>] [max_gradient <float=1.5>]}

Skeleton sizing on volumes:

Volume <range> Sizing Function Skeleton {[scale <1 to 10 = 7>] [time_accuracy_level <1 to 3 = 2>] [min_depth <3 to 8 = 5>] [max_depth <4 to 9 = 7>] [facet_extract_ang <1 to 30 = 10>] [min_num_layers_3d < 1 to N = 1>] [min_num_layers_2d < 1 to N = 1>] [min_num_layers_1d < 1 to N = 1>] [max_span_ang_surf <5.0 to 75.0 = 45.0 degrees>] [max_span_ang_curve <5.0 to 75.0 = 45.0 degrees>] [min_size <float>] [max_size <float>] [max_gradient <float=1.5>]}

The options are explained below:

The skeleton sizing function is generated and stored on a background octree grid whose cells are subdivided based on the graphics facets of the model. The level of subdivision of the background grid affects how well the sizing function captures the geometric complexity of features. Reasonable defaults have been selected for the following two refinement (subdivision) parameters, but these may be overridden for use with simple (decrease parameters) or more complex (increase parameters) models.

Note: These arguments override the basic arguments. For example, time accuracy level 1 internally sets min_depth = 4 and max_depth = 6, and when min_depth is set to 4 and max_depth is set to 7 in the advanced options (recommended for models with fine features), then advanced options override the basic options. In the command-line, to override the depths set by a time_accuracy_level, specify min_depth and max_depth after it.

Skeleton sizing function gives an option to manually add sizing sources on geometric entiies such as vertices, curves, and surfaces. These sizing sources control the size and scope (region of influence via num_layers) at geometric entities. The below command gives the syntax for adding sizing sources. Please note that the below command for adding sizing sources should be called after issuing the above given skeleton sizing command. First, the skeleton sizing command automatically generates sizing sources based on the geometric factors such as proximity, surface curvature, curve length, etc. Issuing the below command creates sizing sources in addition to the automatically generated sizing sources. Finally, when the meshing command is called, the mesh sizing function is calculated using all the sizing sources.

Volume <vol_id_range> Sizing Function Skeleton add size_source {vertex|curve|surface} <id_range> size <double> num_layers <int>

Skeleton sizing function produces a smooth sizing function when called with other sizing controls available in Cubit. Skeleton sizing function behaves as SOFT firmness level. Skeleton sizing function always respects interval count specified on the curves. Skeleton sizing function respects interval size on curves and surfaces only if it is specified after calling the skeleton sizing function.

Figure 3: Skeleton sizing function with other sizing controls

---

## Geometry Decomposition

**URL:** https://coreform.com/cubit_help/item/clean_up/decompose.htm

**Contents:**
- Geometry Decomposition

Automatic decomposition has been researched and tools have been developed which have met with some limited success [Lu,99 , Staten,05]. Automatic decomposition requires complex feature detection and sub-division algorithms. The decomposition problem is at least on the same order of difficulty as the auto-hex meshing problem. Fully automatic methods for quality hexahedral meshing have been under research and development for many years [Blacker,93 , Folwell,98 , Price,95]. However, a method that can reliably generate hexahedral meshes for arbitrary volumes, without user intervention and that will build meshes of an equivalent quality to mapping and sweeping techniques, has yet to be realized. Although fully automatic techniques continue to progress [Staten,06], the objective of the proposed environment is to reduce the amount of user intervention required while utilizing the tried and true mapping and sweeping techniques as its underlying meshing engine.

Instead of trying to solve the all-hex meshing problem automatically, the ITEM approach to this problem is to maintain user interaction. The ITEM algorithms determine possible decompositions and suggest these to the user. The user can then make the decision as to whether a particular cut is actually useful. This process helps guide new users by demonstrating the types of decompositions that may be useful. It also aids experienced users by reducing the amount of time required to set up decomposition commands.

Diagnostics: The current diagnostic for determining whether a volume is mappable or sweepable is based upon the autoscheme tool described in [White,00]. Given a volume, the autoscheme tool will determine if the topology will admit a mapping, sub-mapping or sweeping meshing scheme. For volumes where a scheme cannot be adequately determined, a set of decomposition solutions are generated and presented to the user.

Solutions: The current algorithm for determining possible cut locations is based on the algorithm outlined in [Lu,99] and is described here for clarity:

This relatively simple algorithm detects many cases that are useful in decomposing a volume. Future work will include determining symmetry, sweep, and cylindrical core decompositions. These additional decomposition options should increase the likelihood of properly decomposing a volume for hexahedral meshing.

Figure 1 shows an example scenario for using this tool. The simple model at the top is analyzed using the above algorithm. This results in several different solutions being offered to the user, three of which are illustrated here. As each of the options is selected, the extended cutting surface is displayed providing rapid feedback to the user as to the utility of the given option. Note that all solutions may not result in a volume that is closer to being successfully hex-meshed. Instead the system relies on some user understanding of the topology required for sweeping.

Figure 1. ITEM decomposition tool shows 3 of the several solutions generated that can be selected to decompose the model for hex meshing

---

## Hole

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/hole.htm

**Contents:**
- Hole

Applies to: Annular Surfaces

Summary: Useful on annular surfaces to produce a "polar coordinate" type mesh (with the singularity removed).

Surface <surface_id_range> Scheme Hole [Rad_intervals <int>] [Bias <double>] [Pair Node <id> With Node <id>]

A polar coordinate-like mesh with the singularity removed is produced with this scheme. The azimuthal coordinate lines will be of constant radius (unlike scheme map) The number of intervals in the azimuthal direction is controlled by setting the number of intervals on the inner and outer bounding loops of the surface (the number of intervals must be the same on each loop). The number of intervals in the radial direction is controlled by the user input, rad_intervals (default is one).

A bias may be put on the mesh in the radial direction via the input parameter bias. The default bias of 0 gives a uniform grading, a bias less than zero gives smaller radial intervals near the inner loop, and a bias greater than zero gives smaller radial intervals near the outer loop.

The correspondence between mesh nodes on the inner and outer boundaries is controlled with the pair node "<loop node-id> with node <loop node-id>" construct. One id on the inner loop and one id on the outer loop should be given to connect the two nodes by a radial mesh line. Not choosing this option may result in sub-optimal node pairings with possible negative Jacobians. To use this option, mesh the inner and outer curve loops and then determine the mesh node ids.

Figure 1. Example of Hole Scheme

---

## HTet

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/conversion/htet.htm

**Contents:**
- HTet
- Unstructured
- Structured

Summary: Converts an existing hex mesh into a conforming tetrahedral mesh.

HTet Volume <range> {UNSTRUCTURED | structured}

Unlike other meshing schemes in this section, The HTet command requires an existing hexahedral mesh on which to operate. Rather than setting a meshing scheme for use with the mesh command, the HTet command works after an initial hex mesh has been generated.

Two methods for decomposing a hex mesh into tetrahedra are available. Set the method to be used with the optional arguments unstructured and structured. The unstructured method is the default. Figure 1 shows the difference between the two methods:

Figure 1. Left: Unstructured method creates 6 tets per hex. Right: Structured method creates 28 tets per hex

This method creates 6 tetrahedra for every hexahedra. No new nodes will be generated. The orientation of the 6 hexahedra will be based upon the element node numbering, as a result orientations may change if node numbering changes. This method is referred to as unstructured because the number of tetrahedra adjacent each node will be relatively arbitrary in the final mesh. Tetrahedral element quality is generally sufficient for most applications, however the user may want to verify quality before performing analysis.

With this approach, 28 tetrahedra are generated for every hexahedra in the mesh. This method adds a node to each face of the hex and one to the interior. Although this method generates significantly more elements, the orientation and quality of the resulting tetrahedra are more consistent. Each previously existing interior node in the mesh will have the same number of adjacent tetrahedra.

---

## Immersive Topology Environment for Meshing (ITEM)

**URL:** https://coreform.com/cubit_help/item/item.htm

**Contents:**
- Immersive Topology Environment for Meshing (ITEM)
- Guiding the user through the workflow.
- Providing the user with smart options.
- Automating geometry and meshing tasks.

The Cubit Geometry and Meshing Toolkit team at Sandia has taken on the ambitious task of reducing the time for simulation by specifically addressing the bottlenecks in the mesh generation process. It is not unusual for the meshing process to take upwards of three-quarters of the entire simulation time. With its many tools developed for a wide range of application areas, it takes time to gain enough proficiency in Cubit to quickly generate a mesh from a complex geometry. As a result, the Immersive Topology Environment for Meshing (ITEM) was developed. ITEM is a user-interactive meshing tool that guides the user through a typical mesh generation process.

With the ultimate goal of reducing the time to generate a mesh for simulation, ITEM has been developed within the Cubit Geometry and Meshing Toolkit to take advantage of its extensive tool suite. Built on top of these tools it attempts to improve the user experience by accomplishing three main tasks:

In software of any complexity where usage may be occasional or infrequent, the overhead of learning the new tool to a point of proficiency may be daunting. Given a solid model that may have been designed for manufacturing purposes, the analysts may be faced with generating a mesh. They may not be working with Cubit on a daily basis, but would like to take advantage of the powerful tools provided by the software.

To address this, ITEM provides a wizard-like environment that steps the user through the geometry and meshing process. For someone unfamiliar with the software, it provides an interactive, step-by-step set of tools for accomplishing the major tasks in the process. For those more familiar with the tools, it serves as a reminder of the major tasks, but is flexible enough to accommodate a more iterative approach, allowing them to jump between major tasks easily. Currently restricting the workflow to models requiring three-dimensional, solid elements, ITEM uses the following steps:

Solid models used for analysis may have a huge variety of different characteristics that may prevent them from being easily meshed. Questions such as, What are the problems associated with my model? What are the current roadblocks to generating a mesh on this model? and What should I do to resolve the problems, are constantly being asked by the analysts. Without an extensive knowledge of the tools and algorithms, it may be difficult to answer these questions effectively.

ITEM addresses this issue by providing smart options to the user. Based on the current state of the model, it will automatically run diagnostics and determine potential solutions that the user may consider. For example, where unwanted small features may exist in the model, ITEM will direct the user to these features and provide a range of geometric solutions to the problem. Scrolling through the solutions provides a preview of the expected result. The user can then select the solution that seems most appropriate and execute the solution to change or simplify the geometry. This diagnostic-solution approach is the basis for the ITEM design and is the common mode of user interaction while in this environment. This contrasts with the more traditional hunt-and-guess approach of providing the user with an array of buttons and icons that they may choose from and guessing what may result. ITEM, on the other hand, serves in effect, as an expert providing guidance to the user as they proceed through the geometry and meshing process.

With all of the advanced research and development that has gone into the meshing and geometry problem, a push-button solution for any arbitrary solid model may seem like the ideal objective of any meshing tool. Although for many cases, this would be the best solution, for others it may not even be desirable. A push-button solution assumes a certain amount of trust in the geometric reasoning the software chooses to provide. This may be more trust than an occasional user who is tasked with a high consequence simulation may be willing to give. Even if the user is willing to accept full automation, in many cases, the geometric complexity of the model may be beyond the capability of current algorithms to adequately resolve.

On the other hand, once the user is familiar with the characteristics of the solutions that the software provides, they may not be concerned with examining and intervening on every detail of the model creation process. Instead, in the interest of increasing efficiency, they may want the fastest solution possible. Providing the option for the user to automate as much of the geometry and meshing process as possible is another important aspect of ITEM.

For various characteristic geometric problems that are encountered in a solid model, ITEM can determine from the potential geometric solutions, which of them may be most applicable and apply that solution without any user intervention. For many configurations of geometry, a completely automated solution may be available. For others, only a portion of the process may be able to be automated. Where an adequate solution cannot be determined automatically, the smart options described above are available to help guide the user. As new advances in geometric reasoning and advanced meshing algorithms are developed, ITEM will incorporate these into the solutions for automation.

It should be clear that ITEM is not intended to be a fully automated system for meshing solid models. Instead it is intended to be a flexible environment that will guide the user through the model generation process by offering solution alternatives and providing automation should the user choose. The remainder of this document is organized according to the basic workflow used in ITEM. The objective is to describe the general problems that may be encountered in developing an analysis model and how ITEM and Cubit may be used to address the problems. In developing this environment, many new innovative tools were invented and developed to help support this new approach to mesh and model generation.

---

## Interval Assignment

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/interval_assignment.htm

**Contents:**
- Interval Assignment

"Intervals" means the number of mesh edges on a curve (or across a periodic surface). "Interval matching" is the process of assigning intervals that are close to the user-desires, and satisfy the constraints imposed by the various quad and hex meshing algorithms (e.g., equal intervals on opposite sides of a mapped surface). The desired number of intervals (goals) are set on geometric entities by either specifying the interval count or size. "Soft" user-set and auto-set mesh sizes and interval counts are goals. Any hard counts are part of the constraints. The constraints are determined by the meshing schemes, as well as the vertex types (corners) of surfaces, and the edge-types of volumes, and sweep directions. The user may set additional constraints, including upper and lower bounds.

---

## Interval Firmness

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/interval_firmness.htm

**Contents:**
- Interval Firmness
- Precedence

Before describing the methods used to set and change intervals, it is important that the user understand the concept of interval firmness. An interval firmness value is assigned to a geometry curve along with an interval count or size; this firmness is one of the following values:

hard: interval count is fixed and is not adjusted by interval size command or by interval matching

soft: current interval count is a goal and may be adjusted up or down slightly by interval matching or changed by other interval size commands.

default: default firmness setting, used for detecting whether intervals have been set explicitly by the user or by other tools

Interval firmness is used in several ways in CUBIT. Each curve is assigned an interval firmness along with an interval count or size. Commands and tools which change intervals also affect the interval firmness of the curves. Those same commands and tools which change intervals can only do so if the curves being changed have a lower-precedence interval firmness. The firmness settings are listed above in order of decreasing precedence. For example, some commands are only able to change curves whose interval firmness is soft or default ; curves with hard firmness are not changed by these commands.

More examples of interval setting commands and how they are affected by firmness are given in the following sections.

A curve's interval firmness can be set explicitly by the user, either for an individual curve or for all the curves contained in a higher order entity, using the command:

{geom_list} Interval {Default | Soft | Hard}

All curves are initialized with a firmness of default. Any command that changes intervals (including interval assignment) upgrades the firmness to at least soft.

If a size is specified multiple times for a single entity, the following precedence is used:

---

## Interval Matching

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/interval_matching.htm

**Contents:**
- Interval Matching
- Troubleshooting
- Interval Solver Version
  - IIA Solver >= Cubit 15.6
  - BBIA Solver < Cubit 15.6

Each meshing scheme in CUBIT imposes constraints on the intervals assigned to the curves bounding the surface or volume. For example, map meshing a surface requires that intervals on opposite sides are equal. Meshing any surface with quadrilaterals, regardless of scheme, requires an even number of intervals on its boundary. For connected surfaces and assemblies, these interval constraints must be resolved globally to ensure that each surface and volume will be meshable with the assigned scheme. Beyond satisfying these constraints, the number of intervals (mesh size) should be what the user wants, or as close to it as possible. The global solution technique implemented in CUBIT is referred to as "interval matching."

Interval matching is automatically performed by the mesh command before generating elements. Invoking interval matching manually is useful if the user wishes to mesh only some entities but wants to ensure it will be possible to mesh all entities later: e.g., match intervals on all the volumes, but just mesh surface 3 for now. Interval matching can also be called to check whether the assigned schemes, corners, edge types, and intervals are compatible.

The command syntax for manually matching intervals is the following:

Match Intervals {Surface|Volume|Body|Group} <range>

Here the entity list can be any mixed collection of groups, bodies, volumes, surfaces and curves. The sub-entities are automatically included, e.g., matching intervals on a volume will also match intervals on all of its surfaces as well. However, the converse is not true; going up in dimension must be done explicitly. E.g., to match the intervals on all the volumes containing a curve, then issue the command "match intervals volume in curve 1".

If the quality of the interval solution is poor, try changing the interval count on individual entities, or, e.g., changing some schemes from map to pave to provide more freedom, and rerunning interval matching.

There may be no interval solution. To improve the chances of finding a solution, at least as a test, try setting intervals to soft firmness. Even with soft intervals, a solution might not exist if the mapping corners or sweep directions do not line up right.

If there is no solution, the following command may help in determining the cause (this is not yet supported by IIA in Cubit 15.6):

Match Intervals {Surface|Volume|Body|Group} <range> [Seed Curve <range>] [Assign Groups [Only|Infeasible]] [Map|Pave]

Specifying Assign Groups will create groups that contain independent subproblems of the global problem. Specifying Assign Groups Only will group independent subproblems, but the algorithm will not attempt to solve these subproblems. Assign Groups Infeasible will put each independent subproblem with no solution into specially named groups. Often poor corner choices and surface meshing schemes will be illuminated this way. If Map or Pave is specified, then only subproblems involving mapping or paving constraints will be considered. If a Seed Curve is specified, then only those subproblems containing that curve will be considered.

For consistent results running old journal files, the user may want to use the old solver.

set interval version {<cubit version number>|default}

list interval version

Setting version >= 15.6 uses IIA (2020 solver) and enables small-loop bounds. Using a prior version uses BBIA (1997 solver). Both solvers solve the problem

but the objective f is slightly different so the solution may be different. General problems of this form are known to be difficult because the solution must be integer valued, and neither solver is guaranteed to find the global minimum.

Here x are the intervals and internal variables; b are the bounds on those variables; A and b are the constraints, including hardsets; g are the goals, the user-desired number of intervals for each curve. The objective f models the desire to minimize the maximum relative change in mesh size. In mathematical language, for the new IIA solver f is the maximum lexicographic vector of the ratio achieved:goal if achieved>goal, else goal:achieved. The older solver uses an approximation to IIA's f.

Cubit 15.6 in 2020 introduced "Incremental Interval Assignment (IIA)" based on integer linear algebra. It robustly and quickly finds an integer solutions to Ax=b, and tries to improve it by adding integer vectors from A's nullspace to satisfy the bounds and come close to the goals.

IIA solutions tend to be slightly coarser than BBIA, often one interval less, and closer to the user goals and the global optimum. IIA is faster than BBIA, dramatically faster (6000x) in some cases involving submapping and hard-sets. Please send the Cubit team any example which takes longer than 1 second.

The solution method that Cubit introduced in 1996 was to use linear programming to find a floating point solution to Ax=b, then use branch-and-bound rounding to try to find a nearby integer solution. The first part is fast and robust, the second part slow and error prone. Linear programming is limited to linear objective functions, so the goal:achieved ratio is only approximated and extreme size differences can give unexpected compromises.

For BBIA, advanced users may wish to experiment with the following:

Set Match Intervals Rounding {on|off}

Set Match Intervals Fast {on|off}

Set Match Intervals Delta <interval_difference = 0.>

If set match intervals rounding is set to on, the intervals will be rounded to the nearest integer. If the setting is off, the intervals will be rounded toward the user specified intervals.

If set match intervals fast is set to off a single curve will be fixed per branch and bound iteration. Note in rare cases this may produce better meshes, but will generally be slower. If set on, multiple curves will be fixed per iteration.

Set match intervals delta affects the convergence tolerance for the optimization. Here delta means the difference between a curve's goal and assigned intervals. A larger value makes matching intervals faster, but the quality of the solution may be worse. The default is 0.0. Hint: try 1.0.

---

## Interval Sizing Function

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/interval_sizing_function.htm

**Contents:**
- Interval Sizing Function

The Interval sizing function is similar to the Linear function, but bases edge length at a location on the squared lengths of edges bounding the surface weighted by their inverse distance from the current location. An example is shown below.

Figure 1. NURB mesh with interval sizing function, 34 by 16 density

---

## Inverse Sizing Function

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/inverse_sizing_function.htm

**Contents:**
- Inverse Sizing Function

The Inverse sizing function is also similar to the Linear function, but this method bases edge length at a location on the inverse lengths of edges bounding the surface weighted by their inverse distance from the current location (see Figure 1). The difference between the three linear sizing functions (Linear, Interval, Inverse) is sometimes subtle, but is driven by the geometry being meshed since the influence of these functions is strongly controlled by the number, positioning, and mesh density of the bounding curves relative to the interior surface area.

Figure 1. NURB mesh with inverse sizing function, 34 by 16 density

---

## Laplacian

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/laplacian.htm

**Contents:**
- Laplacian

Applies to: Curve, Surface, and Volume meshes

Summary: Tries to make equal edge lengths

{Surface|Volume} <range> Smooth Scheme Laplacian [Free] [Global]

The length-weighted Laplacian smoothing approach calculates an average element edge length around the mesh node being smoothed to weight the magnitude of the allowed node movement (Jones, 74). Therefore this smoother is highly sensitive to element edge lengths and tends to average these lengths to form better shaped elements. However, similar to the mapping transformations, the length-weighted Laplacian formulation has difficulty with highly concave regions.

Currently, the stopping criterion for curve smoothing is 0.005, i.e., nodes are no longer moved when smoothing moves the node less than 0.005 * the minimum edge length. The maximum number of smoothing iterations is the maximum of 100 and the number of nodes in the curve mesh. Neither of these parameters can currently be set by the user.

The free option allows the nodes on the boundary (surfaces and curves) to be moved during the smooth operation.

Using the global keyword when smoothing a group of surfaces will allow smoothing of mesh on shared curves to improve the quality of elements on both surfaces sharing that curve.

---

## Linear Sizing Function

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/linear_sizing_function.htm

**Contents:**
- Linear Sizing Function

The Linear class of sizing functions determines element size based on a weighted average of edge lengths for mesh edges bounding the surface being meshed. There are several variants of this class of sizing function. The Linear function bases edge length at a location on the lengths of edges bounding the surface weighted by their inverse distance from the current location. The result of this weighting is a more gradual change in mesh density during a transition between dense and coarse mesh. Figure 1 shows the same NURB surface mesh but with intervals of 34 on two curves and intervals of 16 on the remaining two bounding curves and no sizing function. It can be observed that the mesh progresses more rapidly inward from the coarser meshed curves, which locates the transition region much closer to the finer meshed curves. To combat this, the Linear function weights the sizing of new elements such that these transitions occur slower. Figure 2 displays two views of the same NURB geometry with the same bounding curve mesh density using the linear sizing function.

Figure 1. NURB mesh with no sizing function, 34 by 16 density

Figure 2. NURB mesh with linear sizing function, 34 by 16 density

---

## List Interval

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/list_intervals.htm

**Contents:**
- List Interval

List Curve <range> Interval

provides a concise summary interval values, firmness, and bounds; something like:

Listing an entity with the "mesh" keyword option may also give the intervals.

**Examples:**

Example 1 (sql):
```sql
Id Intervals Firm (Size)    [Low,High]
1  6         H+   (1.66667) [6,6]
2  10        H+   (1)
3  8         H+   (1.25)    [8,8]
4  10        H+   (1)
where Firm H:Hard, S:Soft, +:meshed, -:unmeshed E:constrained-to-be-even
```

---

## List Mesh

**URL:** https://coreform.com/cubit_help/environment_control/listing_information/list_mesh.htm

**Contents:**
- List Mesh

The following commands list mesh entity information.

List {Hex|Face|Edge|Node} <id_range>

List {Hex|Face|Edge|Node} <id_range> IDs

For both of these commands, the range can be very general, following the general entity parsing syntax. The first command provides detailed information. For an entity, the information includes its id, owning geometry, subentities and superentities. For a hex, the Exodus Id is also listed. For a node, its coordinates are listed. The second command just lists the entity ids, and is usually used in conjunction with complex ranges.

---

## Lite Meshes

**URL:** https://coreform.com/cubit_help/mesh_generation/litemesh.htm

**Contents:**
- Lite Meshes
- Creating a lite mesh
- Graphics
- Information
- Modification to lite mesh
- Exporting a lite mesh
- Equivalencing of nodes

Cubit has the ability to represent mesh using either a lightweight or heavy representation. The lightweight representation option is new for Cubit 15.3, and can be referred to as lite. The heavy representation is useful for supporting all the various mesh manipulation operations available in Cubit. While still under development, the lite representation option is intended to be a quick way to display larger meshes while supporting a smaller subset of mesh manipulation operations.

The following are supported operations with lite mesh:

The following items are not yet supported:

To use the lite mesh representation, one may import a mesh file using the 'lite' option. There is not currently another way to create lite mesh other than importing from a file. The command to import a lite mesh is:

Import mesh "<filename>" lite

Additional options for lite import can be found under the Import Mesh Lite command.

Generally, the graphical features for lite meshes is supported at the same level as for heavy meshes, including the ability to draw, pick, select, highlight, zoom among other operations. The coloring of the mesh is based on blocks, and may be adjusted by the user. Toggling visibility of all sidesets and nodesets can be done by clicking the Display Boundary Conditions toolbar button or with the bc visibility {on|off} command. Toggling visibilty of all blocks can be done by clicking the Display Mesh toolbar button or with the mesh visibility {on|off} command. The draw, zoom and select commands work on blocks, sidesets and nodesets. Also, selecting those genesis entities in the graphics window will result in them being highlighted in both the graphics window and in the tree. Selecting of nodes and elements has not yet been implemented for meshes imported in lite mode.

There are several ways to view information about the lite mesh. The tree and the property page can show information about the blocks, sidesets and nodesets. Also, the list command can print information about individual blocks, sidesets, and nodesets. The list element command will print out the ID space used by elements. The list node command will show the ID space used by nodes. Listing of individual elements and nodes is not yet supported.

Some modifications to genesis entities are supported. Blocks, sidesets and nodesets may have names assigned to them. Blocks may have their attributes modified, and materials may be assigned to blocks. Not supported is the ability to modify the contents of blocks, nodesets and sidesets.

Exporting a lightweight mesh to an Exodus file is supported. This includes writing out blocks, nodesets, sidesets, element ids, node ids, etc... Not all Exodus data is read in, and if there is some data not recognized by Cubit, it will not be exported. Field data is an example of Exodus data not recognized by Cubit, nor exported. Importing multiple Exodus files and exporting a single file is supported. Importing a single Exodus file and exporting a portion of it is supported. Distribution factors are preserved when reading/writing in lite mode.

Equivalencing of nodes in a lightweight mesh is supported using this command.

Equivalence Node <range> [Tolerance <value>] [Preview]

---

## Mapping

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/mapping.htm

**Contents:**
- Mapping

Applies to: Surfaces, Volumes

Summary: Meshes a surface/volume with a structured mesh of quadrilaterals/hexahedra.

Volume <range> Scheme Map

Surface <range> Scheme Map [Direction {Options}]

A structured mesh is defined as one where each interior node on a surface/volume is connected to 4/6 other nodes. Mappable surfaces contain four logical sides and four logical corners of the map; each side can be composed of one or several geometric curves. Similarly, mappable volumes have six logical sides and eight logical corners; each side can consist of one or several geometric surfaces. For example, in Figure 1 below, the logical corners selected by the algorithm are indicated by arrows. Between these vertices the logical sides are defined; these sides are described in Table 1.

Figure 1. Scheme Map Logical Properties

Table 1. Listing of Logical Sides

Interval divisions on opposite sides of the logical rectangle are matched to produce the mesh shown in the right portion of Figure 1. (i.e. The number of intervals on logical side 1 is equated to the number of intervals on logical side 3). The process is similar for volume mapping except that a logical hexahedron is formed from eight vertices. Note that the corners for both surface and volume mapping can be placed on curves rather than vertices; this allows mapping surfaces and volumes with less than four and eight vertices, respectively. For example, the mapped quarter cylinder shown in Figure 2 has only five surfaces.

Figure 2. Volume Mapping of a 5-surfaced volume

The mapper works on a bicubic interpolation of the points on the boundary to represent the surface. There may be times that those points may not be on the surface exactly if the surface is not suitable for bicubic interpolation. The Mapping Constraint flag tells the mapper to relax the nodes to the geometry or not.

Set Mapping Constraint {ON|off}

When on, the mapping constraint relaxes the node to the nearest point on the geometry. In some situations, the nearest point might be incorrect for the intent of the mesh. To help the mesher find the correct location, a projection direction may optionally be specified for surfaces.

Surface <range> Scheme Map [Direction {Options}]

If a projection direction is specified, the nodes are moved to the geometry in a straight line along the given direction. The direction can be specified using any of the direction options.

---

## Matching Tetrahedral Meshes

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/matching_tetrahedral_meshes.htm

**Contents:**
- Matching Tetrahedral Meshes

The intended use of this function is for importing two exodus or genesis files that have non-conforming mesh where they touch and modifying the meshes locally to make them conforming. The result is a single mesh that is stitched together at the locally modified region. This functionality is currently only available for tetrahedral meshes. Tetrahedral mesh matching will work on free mesh only. The interface where the two meshes will be matched need not be planar. A single target sideset and one or more source sidesets should be provided. The source sideset should be completely enclosed in the target sideset so that the boundaries of the two sidesets do not intersect. The two meshes need not touch exactly at the sidesets but the closer the meshes are to touching the better the results will be. Small gaps or overlaps will generally be allowed. Both of the meshes involved in the matching should be contained in defined blocks prior to issuing the command.

The syntax for the command is:

Meshmatch tet sideset <id_list> onto sideset <id>

---

## Mean Ratio

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/mean_ratio.htm

**Contents:**
- Mean Ratio

Applies to: Triangular or Quadrilateral Surface Meshes, Tetrahedral or Hexahedral Volume Meshes. Does not apply to Mixed Element Meshes.

Summary: Moves interior mesh nodes to optimize the average mean ratio metric value of the mesh.

Surface <surface_id_range> Smooth Scheme Mean Ratio [cpu <double=10>]

Volume <volume_id_range> Smooth Scheme Mean Ratio [cpu <double=10>]

CUBIT includes a mean ratio smoother provided by MESQUITE, a mesh optimization toolkit by Argonne National Laboratory and Sandia National Laboratories. (See Brewer, et al. 2003 for more details on the MESQUITE toolkit.) This smoother is similar in purpose to the Condition Number smoother. However, the Mean Ratio smoother uses a second order optimization method, and therefore it will often reach a near-optimal mesh more quickly than the Condition Number smoother. The Mean Ratio smoother requires the initial mesh to be untangled, but the smoother is guaranteed to not tangle the mesh. If the user attempts to call the Mean Ratio smoother on a tangled mesh, an untangler will first attempt to untangle the mesh before calling the Mean Ratio smoother.

The Mean Ratio smoother's optimization process terminates when one of the following three criteria is met:

The user has control over the second and the third criteria only. For criterion 2, the default is for the smoother to terminate after ten minutes even if a near-optimal mesh has not been reached. The user can change this time bound by specifying the optional "cpu" argument in the command listed above. This argument takes a single, positive number that represents the time (in minutes) that will be used as a time bound. If the user wishes to terminate the process early, criteria three allows the user to "interrupt" (for example, on some platforms, by pressing CTRL-C) the process. If the process is terminated early, the mesh will not revert to the original node positions; CUBIT will instead keep the partially optimized mesh.

---

## Measuring Number of Tets Through the Thickness

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/elements_through_thickness.htm

**Contents:**
- Measuring Number of Tets Through the Thickness

The ability to check the number of tets through the thickness is given with the following command.

Quality Surface <surf1_id> <surf2_id> num_thru_thickness

---

## Meshing Schemes

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/meshing_schemes.htm

**Contents:**
- Meshing Schemes
- Traditional Meshing Schemes
- Free Meshing Schemes
- Conversional Meshing Schemes
- Duplication Meshing Scheme
- General Meshing Information

Meshing schemes in CUBIT can be divided into four broad categories.

In addition, Cubit supports two parallel meshing applications, pCamal and Sculpt

If no scheme is selected, Cubit will attempt to assign a scheme using the automatic scheme selection methods.

Traditional meshing schemes are used to apply a mesh to an existing geometry using the methods described in Meshing the Geometry (i.e. setting a scheme, applying interval sizes, and meshing). Traditional meshing schemes are available for all geometry types.

Free meshing schemes will create a free-standing mesh without any prior existing geometry. The final mesh will have mesh-based geometry.

Conversional meshing schemes are used to convert an existing mesh into a mesh of different element type or size. For example, the THex scheme will convert a tetrahedral mesh into a hexahedral mesh.

The duplication meshing scheme is used to copy an existing mesh from one geometry onto another similar geometry.

Information on specific mesh schemes available in CUBIT is given in this section. The following sections have important meshing-related information as well, and should be read before applying any of the mesh schemes described below.

In most cases, meshing a geometric entity in CUBIT consists of three steps:

This command will match intervals on the given entity, then mesh any unmeshed lower order entities, then mesh the given entity.

After meshing is completed, the mesh quality is automatically checked (see Mesh Quality Assessment), then the mesh is drawn in the graphics window.

The following table classifies the meshing schemes with respect to their applicable geometry.

---

## Meshing the Geometry

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_the_geometry.htm

**Contents:**
- Meshing the Geometry
- Default Scheme and Interval Selection
- Continuing Meshing After a Mesh Failure

After assigning interval or sizing attributes to a geometric entity and a meshing scheme is applied, the geometry is ready to be meshed. To mesh a geometric entity, use the command:

Mesh <entity> <id_range> [GLOBAL|Individual]

The <entity> to be meshed may be any one of the following:

Body Volume Surface Curve Vertex

The Global and Individual options affect how the constraints are gathered for interval matching. With the Global option, the interval constraint equations are calculated from all entities in the entity list. The Individual option calculates the interval constraint equations from each entity individually. The Global option is the default.

If either interval settings or schemes have not already been set on the entities being meshed, CUBIT will do its best to automatically set one or both of these attributes. See Auto Scheme Selection and Auto Specification of Intervals for a description of how CUBIT chooses these attributes. In cases where the automatic scheme selection algorithm fails to select a scheme for the geometry, the meshing operation will fail. In this case explicit specification of the meshing scheme and/or further geometry decomposition may be necessary.

Frequently when meshing large assemblies containing a number of volumes, the mesh command can be applied to a group of volumes with the same mesh command. Typically, if a mesh failure is detected, the meshing operation will continue to mesh the remaining volumes specified at the command line. The following command permits the user to override this feature to discontinue meshing additional volumes and return to the command line immediately after a mesh failure is detected:

Set Continue Meshing [ON|Off]

The default for this command is ON.

Turning this setting OFF is useful when meshing assemblies where a meshing failure of one volume would adversely affect the meshing of adjoining volume(s). This occurs frequently when meshing a sweep group using the sweep scheme.

---

## Meshing Tools

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/meshing_tools.htm

**Contents:**
- Meshing Tools
- Right Click Context Menu

The meshing power tool provides a tool for determining whether a geometry can be meshed using autoscheme, or if it requires its scheme to be set explicitly. This tool is designed to help guide users through geometry decomposition process by providing a convenient way to see which geometries need further modification or decomposition prior to meshing.

Figure 1. Meshing Power Tool showing the solution window with a preview of a webcut solution.

Entity Specification- The meshing power tool works for volumes or surfaces.

Colors Button - Opens the Tools>Options dialog to change the visualization colors of surface schemes for the meshing tool

Show Webcut Solutions - When selected the webcut solutions window will be displayed and populated with custom webcut solutions based on the selected volume.

Analyze Button - The Analyze button issues the autoscheme command for all selected volumes and surfaces and populates a two lists: Scheme Set and No Scheme Set.

Auto Update Checkbox - Used with the webcut solutions, when selected, after executing a webcut, the model will automatically update to determine meshability of the active volumes.

Output Tree - The output from the meshing tool is displayed in tree format. Geometry is divided into "Scheme Set" and "Scheme Not Set" divisions. The geometry is listed under these nodes. If autoscheme was successful, its assigned scheme is also displayed.

Solutions Window - A solutions window that displays potential webcuts for a selected volume is also available. Display the solutions window by selecting the Show Webcut Solutions checkbox at the top of the panel. When a volume is selected, a list of potential webcuts will be displayed. The solutions can be previewed by selecting them and double-clicking will execute the webcut. To further customize the webcut, a right-click on the solution will provide access to the relevant webcut command panel, pre-populated with necessary parameters.

Imprint and Merge After Webcut Checkbox - Available when the Solutions window is displayed, when selected, the resulting webcut operations will also perform an imprint and merge operation.

Toggle Visibility Button - The meshing tool displays entities as red or green in the graphics window. Green means that they are currently meshable using the autoscheme. Red means that they require their scheme to be set explicitly. Turning this capability off will return the volumes and surfaces to their original colors.

Meshing Tools Buttons - Several meshing tools are available to the user from this window. Depending on the entity selected, these are also available from the right-click context menu, and they are described below.

---

## Mesh Adaptivity and Sizing Functions

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/adaptivity_and_sizing_functions.htm

**Contents:**
- Mesh Adaptivity and Sizing Functions
- Adaptive Curve Meshing
- Adaptive Surface Meshing
- Adaptive Volume Meshing

CUBIT provides several options for controlling the density of a mesh by adapting to various geometric, analysis, or user-defined properties. Interval sizes are defined automatically, explicitly, or through sizing functions. The sizing functions can be based on the physical features of the model, a previous analysis solution, or a user-specified bias. Adaptivity can apply to meshing either curves or surfaces.

CUBIT provides several ways to adaptively mesh curves. Three curve meshing schemes are provided for this purpose. They include the following schemes:

The first two schemes use characteristics of the geometric model to define element sizes. The third scheme uses a field function typically defined from a previous analysis solution. FeatureSize is an alpha feature and should be used with caution.

Adaptive surface meshing in CUBIT produces a function following mesh which sizes elements based on the value of the driving function at the spatial location at which the element is to be placed. Adaptive surface meshing is performed using the paving, triadvance or tridelaunay algorithms in combination with an appropriate sizing function. The types of sizing functions that can be used are

The Super sizing function is an alpha feature and should be used with caution.

The procedure for adaptively meshing a surface is to designate paving, triadvance or tridelaunay as the mesh scheme for that surface, assign sizing function types, and mesh the surface.

The command syntax of these commands is:

Surface < id > Scheme {Pave|TriAdvance|TriDelaunay}

Import Sizing Function '<exodusII_filename>' Block <block_id> Variable '<variable_name>' Time <time> [Deformed]

Surface <id> Sizing Function [Type] Exodus [Min <min_value> Max <max_value>]

Surface <id> Sizing Function [Type] {Constant|Curvature|Interval|Inverse|Linear|Super|None}] [Neighbor [<max_neighbors>]]

(See note below regarding 'Neighbor' parameter)

Surface <id> Sizing Function [Type] Bias Start Curve <id_range> {Finish Curve <id_range>| Factor <val>}

Adaptive volume meshing in CUBIT produces a function following mesh that sizes elements based on the value of the driving function at the spatial location at which the element is to be placed. Adaptive volume meshing is performed using the tetmesh scheme in combination with an appropriate sizing function. The types of sizing functions that can be used are constant, geometry adaptive and geometry adaptive (skeleton sizing). Other sizing functions will be added in future versions of Cubit.

The procedure for adaptively meshing a volume is to designate tetmesh as the mesh scheme for that volume, assign sizing function types, and mesh the volume.

The command syntax of these commands is:

Volume <id> scheme tetmesh Volume <id> Sizing Function [Type] {Constant|None} Mesh Surface <id>

The following sections describe details of the various volume sizing methods.

Note regarding 'Neighbor' parameter:

The maximum neighbors is the number of points used by the sizing function to compute the size at the requested point. If the number of neighbors is zero, all of the points on the boundary are used in the size calculation. If the number of neighbors is some other number, only that number of closest points are used in the calculation.

---

## Mesh Cleanup

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_cleanup.htm

**Contents:**
- Mesh Cleanup
- Cleaning Up a Tetrahedral Mesh
- Cleaning Up a Hexahedral Mesh

Once a mesh has been created or imported, Cubit has tools to both manually and automatically improve the quality of a mesh. Mesh Cleanup is the name for the automatic tools which automatically find bad elements and fixing them by both recomputing node locations (i.e. smoothing) AND redefining the local element connectivity. To automatically cleanup a mesh, use the following command:

Cleanup {Volume|Block} <id_range> [angle <value=150>]

This command will cleanup either a tet or a hex mesh as described below.

An alternative to the remesh command for tetrahedral meshes is the cleanup command. For this command the existing mesh is validated and "optimized" by the tetmesher, instead of being deleted and replaced with a different mesh.

To cleanup a tetrahedral volume mesh use the following command:

Cleanup {Volume|Block} <id_range>

A second variation of the Cleanup command allows remeshing of tetrahedra that are either part of a free mesh (not owned by a volume) or are a subset of the tetrahedra in the volume. The command is:

Cleanup Tet <id_range> [Free]

For example, the command

will gather all tetrahedra in a free mesh or single volume, generate a triangle boundary surface, and "optimize" the mesh, ignoring any volume or blocks. Without the optional free keyword, the tets will be processed volume by volume or block by block retaining the boundary between adjacent volumes or blocks.

will gather the tetrahedra in the range [200, 300], generate a triangle boundary surface, and "optimize" the mesh. If the tetrahedra in the range are disjointed, i.e., multiple, independent sets, this operation may fail. It is best to specify a contiguous set of elements.

Note: Cubit will issue an error if the tetrahedra are owned by more than one volume or mesh container.

The command to cleanup a hex mesh is:

Cleanup Volume <id_range> [angle <value=150>]

Hexahedral mesh cleanup is newer to Cubit and currently only a single type of bad element is found and fixed. The hex mesh quality configuration that is currently implemented is when a column of hex elements is on the boundary of a volume, the hexes in the column each have 2 adjacent quad faces on the boundary, and the dihedral angle between those 2 faces is greater than the specified angle tolerance. This situation is illustrated in Figure 1 where the red column of hexahedra has a good angle on the source surface, which flattens out to 180 degree angle on the target creating inverted hex elements. The angle parameter determines how large the angle can get before being cleaned up.

Figure 1. Example of hexahedral mesh with case handled by hex mesh cleanup.

Figure 2 illustrates the result of hex mesh cleanup. Internally, Cubit finds the column of hexahedra with the bad elements, as well as an adjacent column of hexahedra, and then automatically performs some hex column operations followed by smoothing to improve the quality of the elements locally.

Figure 2. The mesh from Figure 1 after hex mesh cleanup.

---

## Mesh Coarsening

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_coarsening.htm

**Contents:**
- Mesh Coarsening
- Hexahedral Coarsening
  - Extracting a Single Hex Sheet
  - Extracting multiple sheets along a curve
  - Uniform hex coarsening

CUBIT provides a limited number of options for coarsening hexahedral meshes. The options currently available for hex coarsening rely on the hex sheet extraction process described in Mesh Refinement page. Removing a sheet from a hexahedral mesh essentially means that a complete layer of hexes will be removed and the adjacent layers expanded to take its place.

The following command can be used to extract a single hex sheet.

Extract sheet { Edge <id> | Node <id_1> <id_2> }

The edge or node pair are used to define the sheet that will be extracted. Figure 3 below shows an example of extracting a hex sheet. In this example the hex sheet is specified by the node pair highlighted in the images. Note that the entire layer of hexes between the highlighted nodes has been removed and the neighboring layers have been expanded to take its place.

Figure 3. Example of Hex Sheet Extraction

Note: Also see the Mesh Refinement section for a description of hex sheet drawing.

Another option for extracting hex sheets can be done by specifying a curve at which to perform the sheet extraction operations. In this case, multiple layers of hexes can be removed by specifying a curve perpendicular to the hex layers. The command for coarsening perpendicular to a curve is as follows:

Coarsen Mesh Curve <id> Factor <value> [NO_SMOOTH|smooth]

Coarsen Mesh Curve <id> Remove {<num_edges>|edge <id_ranges>} [NO_SMOOTH|smooth]

Figure 4. Coarsening a mesh by extracting sheets perpendicular to a curve

The first option uses the Factor argument. The factor argument controls how much larger the edges will be on the curve. For example, Figure 4 shows the coarsen mesh curve command used with a factor of 2. In this case, the command attempts to make the mesh edges approximately twice the length relative to their original length along the curve.

The second option uses the Remove argument. With this option, a specified number of layers may be removed from the mesh. This may be accomplished by indicating an exact number, or by providing a list of edge IDs that correspond to the layers that will be removed.

The NO_SMOOTH|smooth option allows the user to improve the element quality after the sheet extraction process by smoothing the remaining nodes. The default for both of these commands is to not smooth. Smoothing may also be accomplished after sheet extraction by using the smooth volume command.

By applying the coarsen mesh curve command multiple times to curves that are orthogonal in the model, the effect of uniform coarsening of the mesh may be achieved.

---

## Mesh Column Operations

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_column_operations.htm

**Contents:**
- Mesh Column Operations
- Column Insertion
- Column Deletion
- Column Swapping
- Column Groups
- Drawing Columns

A single column can be inserted into the mesh by using the following command:

column open node <center node id> <orientation node ids>

For example, given the following meshed brick:

we issue the command, column open node 89 88 90 , to get this result:

Columns can be removed with neighboring columns being joined together using collapse commands. Collapse commands are of two types: interior and boundary.

For interior node collapse, the two nodes which are opposite on a face are combined together. The column associated with the face is removed. Use the following command:

column collapse node <opposite node ids>

For example, given the following meshed brick:

we issue the command, column collapse node 51 59, to get this result:

The column collapse command can be used with boundary nodes. For example, we issue the command, column collapse boundary node 13 2 11, to get this result:

Faces between two hex columns can be swapped using the following command:

column swap node <old edge node ids> <new edge node ids>

For example, given the following meshed brick:

we issue the command, column swap node 103 94 102 18, to get this result:

A group consisting of hexes that comprise a column can be created using the following command:

column { face <id> | edge <id1> <id2> | hex <id1> <id2> } group

Columns can be drawn using the following command:

draw column { face <id> | edge <id1> <id2> | hex <id1> <id2>}

---

## Mesh Cutting

**URL:** https://coreform.com/cubit_help/appendix/alpha/mesh_cutting.htm

**Contents:**
- Mesh Cutting
  - Coordinate Plane
  - Planar Surface
  - Plane from 3 points
  - Extended Surface
- Meshcut Options
- Meshcutting Scope
- Meshcutting Example

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

The term "mesh cutting" refers to modifying an existing mesh by moving nodes to a cutting entity and modifying the connectivity of the mesh so that the original mesh fits a new geometry. The behavior of mesh cutting is intended to be similar to web cutting in that the process results in a decomposition of the original geometry. The difference is that the decomposition is performed on meshed geometry and results in the creation of virtual geometry partitions. The underlying acis body remains unchanged. The user has the option to determine what is partitioned during mesh cutting: the volume, the surfaces only, or nothing.

The current scope of mesh cutting is limited to cutting hex meshed volumes with planes and extended surfaces. These cutting entities are also limited in that mesh cutting will not work if they pass through a vertex at the end of more than two curves. Mesh cutting does not work on tet meshes or surface meshes.

The steps of mesh cutting include:

The following entities with the associated commands are available for mesh cutting:

A coordinate plane can be used to cut the model, and can optionally be offset a positive or negative distance from its position at the origin.

Meshcut Volume <range> Plane {xplane|yplane|zplane} [offset <dist>]

The planar surface to be used for mesh cutting can also be previewed using the Draw Plane command.

An existing planar surface can also be used to cut the model.

Meshcut Volume <range> Plane Surface <surface_id>

The planar surface to be used for mesh cutting can also be previewed using the Draw Plane command.

Any arbitrary planar surface can be used by specifying three nodes that define the plane.

Meshcut Volume <range> Plane Node <3_node_ids>

An extended surface or "sheet" can also be used for mesh cutting. In this case, the sheet is not restricted to be planar and will be extended in all directions possible. When cutting with an extended surface mesh cutting will ignore all curves and vertices of the surface. Also, the resolution of the mesh will determine how well curved surfaces are captured with meshcutting. A surface with high curvature will not be captured accurately with a coarse mesh. Note that some spline surfaces are limited in extent and may not give an expected result from mesh cutting.

Meshcut Volume <range> Sheet [Extended From] Surface <surface_id>

Note: When cutting with surfaces extended from composite surfaces the default underlying surface approximation may result in a poor final mesh for mesh cutting. This problem can be fixed using the following command:

Composite closest_pt surface <id> gme

See the discussion on composite geometry for a more detailed description of this command.

The following options can be used with all the meshcut commands:

[PARTITION VOLUME|partition surface|no_partition]: By default, mesh cutting will create virtual partitions of the volume being cut to match the cutting entity. This option allows mesh cutting to also create only the surface partitions or create no partitions for the volume or surfaces.

[no_refine]: This option tells mesh cutting not to refine the mesh around the cutting entity.

[no_smooth]: This option tells mesh cutting not to perform the final smoothing step after the cut has been made.

The following is a list of the current scope and limitations of meshcutting.

The figures below show an example of mesh cutting. Figure 1 shows the body that will be meshed. This body is a brick with intersecting through-holes. The steps to create a mesh for this body are listed below.

Figure 1: The original, unmeshed body

Step 1: Create a starting mesh. Figure 2 below shows the starting mesh for this problem. The commands for this mesh are:

cubit> reset cubit> set dev on cubit> create brick x 10 cubit> create cylinder radius 3 z 15 cubit> subtract 2 from 1 cubit> volume 1 scheme sweep cubit> volume 1 size .75 cubit> webcut volume 1 with plane xplane offset 0 cubit> merge all cubit> mesh volume 1 3

Figure 2: The starting mesh

Step 2: Create a cutting entity. Figure 3 shows the volume that will be used to cut the mesh. The commands are:

cubit> create cylinder radius 2 z 15 cubit> rotate volume 4 about x angle 90

Figure 3: The starting mesh and cutting entity

Step 3: Cut the mesh. Figure 4 shows the new mesh after the original mesh has been cut. Also recommend smoothing the mesh:

cubit> meshcut vol 1 3 sheet surface 27 cubit> surf in vol 1 3 smooth sch condition number beta 2 cpu 0.5 cubit> smooth surface in volume 1 3 cubit> vol 1 3 smooth scheme condition number beta 2 cpu 0.5 cubit> smooth volume 1 3 cubit> draw volume 1 3

Figure 4: The mesh after meshcutting

Step 4: Final step. Figure 5 shows the quality of the final mesh. The command is:

cubit> quality volume 1 3 scaled jacobian global draw mesh

Figure 5: Quality of final mesh

---

## Mesh Deletion

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_deletion.htm

**Contents:**
- Mesh Deletion
- Automatic Mesh Deletion

Meshing a complex model often involves iteration between setting mesh parameters, meshing, and checking mesh quality. This often requires removing mesh, for only an entity or for an entity and all its lower order geometry, or sometimes for the entire model.

The command to remove all existing mesh entities from the model is:

The command for deleting mesh on a specific entity is:

Delete Mesh {geom_list} [Propagate]

These commands automatically cause deletion of mesh on higher dimensional entities owning the target geometry.

If the Propagate keyword is used, mesh on lower order entities is deleted as well, but only if that mesh is not used by another higher order entity. For example, if two surfaces (surfaces 1 and 2) sharing a single curve are meshed, and the command "delete mesh surface 1 propagate" is entered, the mesh on surface 1 is deleted, as well as the mesh on all the curves bounding surface 1 except the curve shared by surface 2. In some cases, the capability to delete individual mesh faces on a surface is needed. Deleting a mesh face involves closing a face by merging two mesh nodes indicated in the input. The syntax for this command is:

Delete Face <face_id> Node <node_id> [Node <diagonal_node_id>]

This command is provided primarily for developers' use, but also provides the user fine control over surface meshes. At the present time, this command works only with faces appearing on geometric surfaces and should be used before any hex meshing is performed on any volume containing the face to be deleted.

Set Mesh Autodelete [ON|Off]

---

## Mesh Generation

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_generation.htm

**Contents:**
- Mesh Generation
- Element Types
- Mesh Generation Process

The methods used to generate a mesh on existing geometry are discussed in this chapter. The definitions used to describe the process are first presented, followed by descriptions of interval specification, mesh scheme selection, and available curve, surface, and volume meshing techniques. The chapter concludes with a description of the mesh editing capabilities, and the quality metrics available for viewing mesh quality.

For each entity topology-type in the model geometry, CUBIT can discretize the entity using one, or several, types of basic elements, for each order entity in the geometry (vertex, curve, etc.). CUBIT uses a basic element designator to describe the corresponding entity, or entities, in the mesh, and a given geometric topology entity can be discretized with one, or several, of basic elements types in CUBIT. For example, a geometric surface in CUBIT is discretized into a number of faces, where faces is the basic element designator for surfaces. These faces can consist of two types of basic elements, quadrilaterals or triangles. The basic element designators corresponding to each type of geometric entity, along with the types of basic elements supported in CUBIT, are summarized in the table below.

For each basic element, CUBIT also supports several element type definitions, whose use depends on the level of accuracy desired in the finite element analysis. For example, CUBIT can write both linear (4-noded) and quadratic (8- or 9-noded) quadrilaterals. The element type definition is specified after meshing occurs, as part of the boundary condition specification. See Finite Element Model Definition for a description of that process and the various element types available in CUBIT.

Each mesh entity is associated with a geometric entity which "owns" it. This associativity allows the user to mesh, display, color, and attach attributes to the mesh through the geometry. For example, setting a mesh attribute on a surface affects all faces owned by that surface.

Starting with a geometric model, the mesh generation process in CUBIT consists of four primary steps:

Set interval size and count for individual entities or groups

The size or interval is always applied to a specific geometric entity. For example:

CUBIT supports numerous meshing schemes for meshing solid model entities. For example:

volume 1 scheme sweep

Generate the mesh for the model

Use the mesh command to generate the mesh on a specified geometric entity. For example:

Inspect mesh for quality and suitability for targeted analysis

CUBIT provides various quality metrics for the user to verify the suitability of the mesh for analysis. The quality command can be used to check the elements generated on a specific geometric entity. For example:

There are also mechanisms for improving mesh quality locally using smoothing and local mesh topology changes and refinement. For complex models, this process can be iterative, repeating all of the steps above.

The mesh for any given geometry is usually generated hierarchically. For example, if the mesh command is issued on a volume, first its vertices are meshed with nodes, then curves are meshed with edges, then surfaces are meshed with faces, and finally the volume is meshed with hexes. Vertex meshing is of course trivial and thus the user is given little control over this process. However, curve, surface, and volume meshing can be directly controlled by the user. Each of the steps listed are described in detail in the following sections.

---

## Mesh Grafting

**URL:** https://coreform.com/cubit_help/appendix/alpha/mesh_grafting.htm

**Contents:**
- Mesh Grafting
- Grafting Options
- Grafting Scope

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Grafting is used to merge a meshed surface with a dissimilar unmeshed surface. In the process, the location of the nodes on the meshed surface will be adjusted to fit to the bounding curves of the unmeshed surface and the connectivity of the original mesh may be changed to improve the final quality of the mesh. This allows an unmeshed volume to be attached--or grafted--onto a meshed volume. Grafting is particularly useful for models that have intersecting sweep directions (see example below).

The command syntax for grafting is:

Graft {Surface <range> | Volume <id>} onto Volume <id> [no_refine] [no_smooth]

The Graft command will check that the second volume is meshed. It then searches for surfaces on the second volume that overlap with the other volume or range of surfaces that is specified. If overlapping surfaces are found the mesh will then be adjusted on the second volume and after any needed imprinting is done the overlapping surfaces will be merged together.

[no_refine]: This option tells grafting not to modify the connectivity of the original mesh. The mesh is still adjusted to fit the boundary of the branch surface but no new elements are added.

[no_smooth]: This option tells grafting not to perform the final smoothing of the modified surface or volume mesh.

The following is a list describing the current scope and limitations of grafting:

This example shows the four basic steps of grafting:

Step 1: Partition the geometry

Figure 1 shows the model that will be meshed. The arrows in the figure show the two intersecting sweep directions. Figure 2 shows the model decomposed for grafting.

Figure 1. A model with two intersecting sweep directions.

Figure 2. The model decomposed for grafting

Step 2: Mesh the trunk volume.

Figure 3 shows the mesh of the trunk volume. At this point the mesh on the trunk surface adjacent to the branch surface is a structured mesh that does not align with the boundary of the branch surface. The trunk and branch surfaces are two separate surfaces.

Figure 3. Meshed trunk volume.

Step 3: Graft the branch onto the trunk

Figure 4 shows the trunk surface after it has been modified to fit the branch surface. At this point the two surfaces have been merged together.

Figure 4. Trunk surface after grafting.

Step 4: Mesh the branch volume.

The final mesh is shown in Figure 5.

---

## Mesh Interval Preview

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/mesh_interval_preview.htm

**Contents:**
- Mesh Interval Preview

It is sometimes useful to view the nodal locations/intervals on curves graphically before meshing (which can take considerably more time). The command to do this is:

Preview Mesh {Body|Volume|Surface|Curve|Vertex} <id_range> [Hard] [color <color>]

To clear the display of the temporary nodes, simply issue a "display" command. The purpose of the hard option is that only curves that have an interval firmness of hard will be previewed.

---

## Mesh Modification

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_modification.htm

**Contents:**
- Mesh Modification

After meshing is completed, it may be desirable to change features of the mesh without remeshing the whole volume. Mesh modification methods include tools for improving mesh quality, repositioning mesh elements, or changing mesh density. These methods can be applied on the whole model, or on small sections of the model without requiring remeshing the geometry, and without modifying the underlying geometry.

---

## Mesh Pillowing

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/pillow.htm

**Contents:**
- Mesh Pillowing

Figure 1: A single hex before (a) and after (b) a pillow operation. The far right (c) depicts a pillow operation with the front surface designated as a 'through' surface.

During a typical pillow operation, the user selects a set of elements, called a 'shrink set', to define what elements will be operated on. All elements on the outer boundary of the shrink set are then shrunk towards the center of the set. New elements are then created to fill the gap between the original boundary and the shrunk boundary. The newly created elements form the pillow around the selected shrink set. Figure 1a and 1b show an example of a pillow operation performed on a single hex. Geometry surfaces, or mesh element faces can be specified as through surfaces for the pillowing operation. This means that the pillow will extend through the selected surfaces, and no new elements will be created along them. Figure 1c shows the effect of pillowing a single hex with one surface selected as a through surface.

In some cases a shrink set may not be valid due to the geometry of a specific region. As the exterior nodes of the shrink set move towards the middle they must be able to maintain appropriate geometric associations. Nodes on vertices must move along curves, nodes on curves must move along surfaces. If there are multiple curves or surfaces along which an exterior node might travel, then the ownership is ambiguous and the pillowing will fail.

Using the optional distance keyword with a specified value allows manual control of the distance that each boundary element is shrunk towards the center of the shrink set. If no distance value is specified, an appropriate value is calculated for each element. If a distance value is specified, all newly created nodes will have their position fixed by default. This allows the user to smooth the mesh without altering the node positions of the newly created hexes. If the optional unfix_nodes keyword is used, this default behavior is changed, and any smooth operations will alter the newly created node locations. By default, a smooth operation is automatically performed following any pillow operation unless the optional no_smooth keyword is used.

Similar analogous commands are available for creating a pillow around a set of two dimensional faces.

Pillow Hex <ids> [ Through { [Surface <ids>][Face <ids>][Tri <ids>] } ] [ Distance <value> ] [ Unfix_nodes ] [ No_smooth ]

Pillow Face <ids> [ Through Curve <ids> ] [ Distance <value> ] [ Unfix_nodes ] [No_smooth]

Figure 2: Example model using pillow operations to create ordered nodes a specified distance around the boundary of a mesh.

---

## Mesh Quality Assessment

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/mesh_quality_assessment.htm

**Contents:**
- Mesh Quality Assessment

The `quality' of a mesh can be assessed using several element quality metrics available in CUBIT. Information about the CUBIT quality metrics can be obtained from the command

Quality Describe {Hex | Hexahedral | Tet | Tetrahedral | Face | Quad | Quadrilateral | Tri | Triangular}

which gives data on the quality metrics for each of the above element types. The following pages discuss the mesh quality assessment capabilities in CUBIT.

---

## Mesh Quality Command Syntax

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/mesh_quality_syntax.htm

**Contents:**
- Mesh Quality Command Syntax
- Quality Options
  - Scope
  - Draw
  - List
  - Filter

The base command to view the quality of a mesh is the following:

Quality {geom_and_mesh_list} [metric name] [quality options] [filter options]

Where the list contains surfaces and volumes and groups that have been meshed with faces, triangles, hexes, and tetrahedra; the list can also specify individual mesh entities or ranges of mesh entities.

If a specific metric name is given, only that metric or metrics are computed for the specified entities. Note that the metric given must be one which applies to the given entities. To see a list of quality metrics for individual entities see the Mesh Quality Assessment section and select the desired entity type: hexahedral, tetrahedral, quadrilateral, triangle. or edge

The metric name can also be more general than a specific metric. Four generalized options for metric name can be used:

Allmetrics: All of the metrics corresponding to the element type of the geom_and_mesh_list will be computed and reported.

Algebraic: All algebraic metrics corresponding to the element type of the geom_and_mesh_list will be computed and reported (e.g., Shape, Shear, Relative Size).

Robinson: All Robinson metrics corresponding to the element type of the geom_and_mesh_list will be computed and reported (e.g., Aspect Ratio, Skew, Taper).

Traditional: All the traditional Cubit metrics corresponding to the element type of the geom_and_mesh_list will be computed and reported (e.g., area, volume, angle, stretch, dimension).

If no metric name is supplied, the default metric is "Shape".

The quality options are:

[ Global | Individual ]

If the user specifies individual, one quality summary is generated for each entity specified on the command line. If the user specifies global, or specifies neither, then one quality summary is generated for each mesh element type.

[ Draw [Histogram] [Mesh] [Monochrome] [Add] ]

If the user specifies draw histogram, then histograms are drawn in a separate graphics window. The window contains one histogram for each quality metric. If the user specifies draw mesh, then the mesh elements are drawn in the default graphics window. A color-coded scale will appear in the graphics window. The histogram and mesh graphics are color coded by quality: a small metric value corresponds to red, a large metric value to blue and in-between values according to the rainbow. You can grab the side of color bar and resize it. The text gets smaller as the color bar width decreases. You can also grab in the middle of the color bar and move it around. It can be repositioned to the bottom or top and it will automatically change orientations. See Figure 1.

Figure 1. Quality Scale

If monochrome is specified, then the graphics are not color-coded. If add is specified, then the current display is not cleared before drawing the mesh elements.

[ List [Detail] [Id] [Verbose Errors] ] [Geometry]

If the user specifies List, then the quality data is summarized in text form. List Detail lists the mesh elements by ascending quality metric. List Id lists the ids of the mesh elements. If Verbose Errors is specified, then details about unacceptable quality elements are printed out above the summaries. If Geometry is specified, then a list of the geometric entities that own the elements will be printed.

There are several options available to filter the output of the quality command, using the following filter options :

[High <value>] [Low <value>]

Discards elements with metric values above or below value; either or both can be used to get elements above or below a specified value or in a specified range.

[Top <number>] [Bottom <number>]

Keeps only number elements with the highest or lowest metric values. For example, " Quality hex all aspect ratio top 10 " would request the elements with the 10 highest values of the aspect ratio metric.

---

## Mesh Quality Example Output

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/mesh_quality_example.htm

**Contents:**
- Mesh Quality Example Output

The typical summary output from the command quality surface 24 is shown in Figure 1. Figure 2 shows the corresponding histogram. The colored element display resulting from the command quality surface 1 draw `Skew' is shown Figure 3. A color legend is also printed to the console as shown in Figure 4.

Figure 1. Typical Summary for a Quality Command

Figure 2. Histogram output from command "Quality Surface 24 Draw Histogram"

Figure 3. Graphical output of quality metric for command "Quality Surface 24 Skew Draw Mesh"

Figure 4. Legend for command "Quality Surface 1 Skew Draw Mesh"

---

## Mesh Quality Tools

**URL:** https://coreform.com/cubit_help/environment_control/gui/tree_view/quality_tools.htm

**Contents:**
- Mesh Quality Tools
- Mesh Quality Tool Buttons
- Right-Click Context Menu Items

The mesh quality tool is located in the entity tree window under the quality tab. The Mesh Quality Tool works on meshed entities to analyze mesh quality based on selected metrics. Output from the mesh quality analysis can be visualized using color-coded scales. The mesh quality tool also contains tools to improve mesh quality including smoothing, refinement, node merging, mesh validation, deleting mesh elements, and repositioning nodes.

Figure 1. Mesh Quality Tools

Entity Type - The mesh quality tools can only be applied to mesh entities including volumes, surfaces, hexahedra, quadrilaterals, triangles, or tetrahedra.

Help Button - Opens context specific help for this topic.

Options Button - Clicking on this button will show the Tools>Option menu dialog that allows users to manually enter metric range settings. The settings are persistent between sessions. For a description of quality metrics and default ranges click on one of the following links:

Analyze Button - This button starts the quality processing based on the metrics/filters selected.

Output Window/Tree - The failed elements are shown in the tree under the heading "Poor Elements". For each metric/filter the output will be listed in a tree format with the following nodes.

The mesh elements can be sorted by quality or by numeric order. To change the way items are sorted, click on the headings. The right-click or context menu will show various remedies depending on what is selected. Performing an operation on a parent node will perform the same operation on all of the child nodes.

The buttons on the bottom of the mesh quality tool window are some of the tools you may use to improve mesh quality and include.

---

## Mesh Refinement

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_refinement.htm

**Contents:**
- Mesh Refinement
- Global Mesh Refinement
- Refining at a Geometric or Mesh Feature
- Hexahedral Refinement Using Sheet Insertion
  - Refining at a Geometric Feature
  - Refining along a path
  - Refining a Hex Sheet
  - Directional Refinement
  - Hex Sheet Drawing
- Local Refinement of Tets, Triangles, and Edges

CUBIT provides several methods for conformally refining an existing mesh. Conformal mesh refinement does not leave hanging nodes in the mesh after refinement operations, rather conformal mesh refinement provides transition elements to the existing mesh. Both local and global mesh refinement operations are provided.

The Refine Surface and Refine Volume commands provide capability for globally refining an entire surface or volume mesh. Global refinement will only be used if the entire body is included in the command. Otherwise, the command will be interpreted as local refinement (see below.) This distinction can be important because the global refinement algorithm divides each element into fewer sub-elements than local refinement. The command syntax is:

Refine Volume <range>numsplit<int>

Refine Surface <range>numsplit<int>

The numsplit option specifies how many times to subdivide an element. A value of 1 will split every triangle and quadrilateral into four pieces, and every tetrahedron and hexahedron into eight pieces. Examples of global refinement on each element are shown below.

Figure 1. Example of uniform refinement for each of the mesh entities

CUBIT also provides methods for local refinement around geometric or mesh features. Individual elements or groups of elements can be refined in this manner using the following syntax.

Refine {Node|Edge|Tri|Face|Tet|Hex} <range> [NumSplit<int = 1>|Size <double> [Bias <double>]] [Depth <int>|Radius <double>] [Sizing_Function] [Smooth]

Refine {Vertex|Curve|Surface} <range> [NumSplit<int = 1>|Size <double> [Bias <double>]] [Depth <int>|Radius <double>] [Sizing_Function] [Smooth]

To use these commands, first select mesh or geometric entities at which you would like to perform refinement. Refinement will be applied to all mesh entities associated with or within proximity of the entities. The all keyword may be used to uniformly refine all elements in the model

The following is a description of refinement options.

Defines the number of times the refinement operation will be applied to the elements in the refinement region. For uniform or global refinement, where all elements in the model are to be refined, A NumSplit value of 1 will split each triangle and quadrilateral into four elements, and each tetrahedron and hexahedraon into eight elements. A numsplit of 2 would result in 9 and 27 elements respectively. For uniform refinement, the total number of elements obeys the following:

where NE is the final number of elements, NI is the initial number of elements and Dim is 2 or 3 for 2D and 3D elements respectively.

In cases where only a portion of the elements are selected for refinement, the elements at the boundary between the refined and non-refined elements will be split to accommodate a transition in element size. The transition pattern will vary depending on the local features and surrounding elements. For non-uniform refinement of hexahedron, for a numsplit of 1, each element in the uniform refinement zone will be subdivided into 27 elements rather than 8. This affords greater flexibility in transitioning between the refined and unrefined elements.

The Size and Bias options are useful when a specific element size is desired at a known location. This might be used for locally refining around a vertex or curve. The Bias argument can be used with the Size option to define the rate at which the element sizes will change to meet the existing element sizes on the model. Figure 2 shows an example of using the Size and Bias options around a vertex. Valid input values for Bias are greater than 1.0 and represent the maximum change in element size from one element to the next. Since refinement is a discrete operation, the Size and Bias options can only approximate the desired input values. This may cause apparent discontinuities in the element sizes. Using the default smooth option can lessen this effect. It should also be noted that the Size option is exclusive of the NumSplit option. Either NumSplit or Size can be specified, but not both.

Figure 2. Example of using the Size and Bias options at a Vertex.

The Depth option permits the user to specify how many elements away from the specified entity will also be refined. Default Depth is 1. Figure 3 shows an example of using the depth option when refining at a node.

Figure 3. Example of using the Depth option at a node to control how far from the node to propagate the refinement.

Instead of specifying the number of elements to describe how far to propagate the refinement, a real Radius may be entered. The effects of the Radius are similar to that shown in Figure 3, except that the elements whose centroid fall within the specified Radius will be refined. Transition elements are inserted outside of this region to transition to the existing elements.

Refinement may also be controlled by a sizing function. CUBIT uses sizing functions to control the local density of a mesh. Various options for setting up a sizing function are provided, including importing scalar field data from an exodus file. In order to use this option, a sizing function must first be specified on the surface or volume on which the refinement will be applied. See Adaptive Meshing for a description of how to define a sizing function.

The default mode for refinement operations is to NOT perform smoothing after splitting the elements. In many cases, it may be necessary to perform smoothing on the model to improve quality. The smooth option provides this capability.

Controlling Regularity of Triangle Refinement

The default behavior of triangle refinement is to attempt to maximize element quality using the basic one->four template. This can sometimes result in an irregular pattern, where one or more edges are swapped. To enforce regularity of the triangle refinement pattern, regardless of quality, the folowing setting may be used.

Set Triangle Refine Regular {on|OFF}

Several tools for refining a hexahedral mesh using sheet insertion and deletion are available in CUBIT.

The following commands offer additional controls on refinement with respect to one or more geometric features of the model.

An existing hexahedral mesh can be refined at a geometric feature using the following command:

Refine Mesh Volume <id> Feature {Surface | Curve | Vertex | Node} <id_range> Interval <integer>

This command refines the mesh around a given feature by adding sheets of hexes. These sheets can be generalized as planes for surfaces, cylinders for curves, and spheres for vertices. The interval keyword specifies the number of intervals away from the feature to insert the new sheet of hexes. For this command a single sheet of hexes is inserted into the hexahedral mesh.

Figure 4 shows an example of this command where the feature at which refinement is to be performed is a curve. In this case the interval chosen was, 2. This indicated that the elements 2 intervals away from the curve would be refined.

Figure 4. Example of Refinement at a curve

Hexahedral meshes can be refined from a specific node and along a propagated path using the following command

Refine Mesh Start Node <id> Direction Edge <id> End Node <id> [Smooth]

Figure 5 shows a swept mesh and its cross section. The cross section view on the left shows a path that has been propagated through the mesh between the start node and end node. This path is then projected along a chain of edges in the direction given by the direction edge as shown in Figure 5. The start node and end node must be on the same sweep layer. This refinement procedure also requires the volume's meshing scheme to be set to sweep. If the smooth keyword is given the mesh will be smoothed after the refinement step is complete.

Figure 5. Refining a Mesh Along a Path

The following command can be used to refine the elements in one or more hex sheets:

Refine Mesh Sheet [Intersect] { Node <id_1> <id_2> | Edge <id_range> } { Factor <double> | Greater_than <size> } [Smooth] [in volume <id_range> [depth <num_layers]]

The node and edge keywords are used to define the hex sheet(s) to be refined. If the node option is chosen, only one node pair can be entered (see Figure 6). If the edge option is chosen, one or more edges can be entered (see Figure 7).

Figure 6. Refine mesh sheet node 796 782 greater_than 6

Figure 7. Refine mesh sheet edge 1584 1564 1533 1502 1471 greater_than 6

The factor and greater_than keywords are used to specify the refinement criteria for the selected hex sheet(s). If the factor keyword is used, the length of the smallest edge in the hex sheet is determined and any edge in the hex sheet with a length greater than the smallest length multiplied by the factor is refined. If the greater_than keyword is used, any edge in the hex sheet with a length greater than the specified size is refined.

The intersect keyword is optional. It is used to more easily define multiple hex sheets to be refined. If the intersect keyword is entered, the node and edge keywords are used to define a chord rather than a sheet (a chord is the two-dimensional equivalent of the three-dimensional sheet). The chord will be limited to the surface(s) associated with the nodes or edge entered, and all sheets intersecting the chord will be selected for refinement (see Figure 8). When the node keyword is used with the intersect option, the nodes must define an edge on the surface of the mesh.

Figure 8. Refine mesh sheet intersect edge 1499 greater_than 6

The smooth keyword is also optional. When the smooth keyword is entered, the elements that have been refined are smoothed in an attempt to improve element quality. Figure 9 shows the same command as Figure 8 with the addition of the smooth keyword. Smoothing may or may not be beneficial, depending on the situation.

Figure 9. Refine mesh sheet intersect edge 1499 greater_than 6 smooth

Mesh sheet refinement can also be used to refine a mesh in a particular direction. This can help control anisotropy. The following command can be used as a short cut for specifying what sheets should be used in refinement.

Refine Volumes <id_range> using {Plane <options> | Surface <id_range> | Curve <id_range> } [ Depth <num_layers> ] [ Smooth ]

The volumes specified indicate which hexes can be refined. A transition layer will be made out of hexes surrounding the indicated volumes. If the depth option is used, additional layers of hexes around the specified volumes will be included in the refinement region. Behind the using option, if the plane option is employed, all the edges in the volume which are parallel to the plane (to a small tolerance) are used to specify the sheets to refine. If the surface or curve option is employed instead, all the edges in the surfaces or curves will be used.

For example, Figure 10 and 11 shows directional refinement using the plane option. The command used to convert the mesh in Figure 10 to Figure 11 is:

refine vol 2 using plane xplane depth 1

Figure 10. Starting mesh

Figure 11. Directional result of refinement resulting from using the plane option on the refinement command.

Directional refinement can be used iteratively to reduce or create anisotropy of any level. This is done by applying the direction refinement command iteratively. A second iteration of directional refinement can be applied by issuing the same command again. To improve element quality, however, it is often recommended to perform refinement parallel to the plane before subsequent iterations. For example, taking the mesh in Figure 11 as input, the following commands will generate the mesh in Figure 12.

refine mesh sheet edge ( at 4.5 5 5 ordinal 1 ) factor 0

refine vol 2 using plane xplane depth 1

Figure 12. A 2nd iteration of direction refinement is applied.

Since refinement of hex meshes generally occurs by inserting hex sheets, tools have been provided to draw a specified sheet or group of sheets.

This command draws a sheet of hexes that is defined by the edge or node pair.

Draw Sheet {Edge <id> |Node <id_1> <id_2>}[Mesh [List]] [Color <color_name>] [Gradient]

The following command draws the three sheets that intersect to define the given hex. These sheets are drawn green, yellow, and red. To draw a specific sheet, list its color in the command.

Draw Sheet Hex <id> [Green][Yellow][Red][Mesh [List]] [Gradient]

The 'gradient' keyword for both commands draws the sheet in gradient shading according to the distance between opposite hex faces that are parallel to the sheet.

The 'mesh' keyword will draw the hexes in the hex sheet. If the 'list' keyword is also given, the ids of the hexes in the sheet will be listed.

Local refinement of tets, triangles, and edges is available by refining individual entities or by refining to guarantee a user-specified number of tests through the thickness:

Local refinement of tets, triangles, and edges is available. When refining triangles a node is inserted at the enter of the triangle and three new triangles are connected to this node. The original triangle is deleted. The command to refine triangles is:

Refine Local Tri <tri_id_list>

When refining an edge, a node splits the original edge between two triangles and four new triangles are created and connected to the new node. The command to refine an edge is:

Refine Local Edge <edge_id>

When refining a tet edge, the tet edge is split by a node and then all tets attached to the original edge are split into two through a triangle that goes through the new node. All other adjacent nodes and edges are unmodified by the operation. Note that on the interior of the mesh tet edges are not represented explicitly so the command takes two nodes as input to define the edge. The command to refine a tet edge is:

Refine Tet_edge Node <node1_id> <node2_id>

Cubit provides a capability to guarantee a user-specified number of tets through the thickness. This functionality is intended to work on an existing tet mesh using mesh refinement. The user specifies the geometry or mesh defining the thin region and also the number of desired tets through the thickness and the refinement algorithm will run until it meets this criteria. The number of tets through the thickness in this context is interpreted as the number of mesh edges through the thickness and the algorithm will continue to do refinement until there are no mesh edge paths through the thin region that contain fewer mesh edges than the number specified by the user. The command for doing this is:

Refine min_through_thickness <val> source {surface|node|tri|nodeset|sideset|block} <id_range> target {surface|node|tri|nodeset|sideset|block} <id_range> [anisotropic] [single_iteration] [dont_fill_in_gaps]

The various options are described below.

anisotropic: When this option is specified in the command the algorithm will only attempt to refine the edges that go roughly normal to the source and target entities. This will give an anisotropic result. The meshes on the source and target will generally not be affected when this option is used. When this option is not specified the refinement algorithm will be isotropic in nature and will propagate much more. However, it will tend to have better transitioning from the refined region to the non-refined regions.

dont_fill_in_gaps: When this option is specified in the command the algorithm will NOT try to grow the regions that will be refined. When the regions are grown it helps to avoid leaving small pockets of mesh that are not refined (splotchiness). This has effect only on isotropic refinement (when the "anisotropic" option is NOT used).

single_iteration: When this option is specified in the command the algorithm will only run for one iteration even if the min_through_thickness criteria is not met.

A quality command for querying the minimum number of tets through the thickness is found here.

Below is an example using the following commands:

refine min_through_thickness 4 source surf 1 target surf 2 anisotropic

refine min_through_thickness 4 source surf 7 target surf 13 3 14 anisotropic

Surfaces 1 and 2 are the two surfaces on opposite sides of the thin region in the green volume and surfaces 7 13 3 14 are the surfaces on opposite sides of the thin region in the yellow volume.

Figure 13. Before N through the thickness refinement.

Figure 14. After N through the thickness refinement.

The Uniform Mesh Refinement (UMR) tool refines a mesh stored in the Exodus format uniformly, splitting every element in the mesh into a number of sub-elements, and writes the fine mesh to a new Exodus file. The resulting elements have roughly half the edge length of the original mesh. The algorithm uses an efficient streaming pipeline with low memory requirements. On recent CPUs with an SSD (solid state drive), it will write a mesh up to 4 billion elements or nodes in only a few minutes, and millions of elements or nodes in seconds or less.

In the alpha release of UMR, only blocks and sidesets of tetrahedra (4 node) and triangles (3 node) are supported. No projection of new nodes to geometry or smoothing is performed. Each TET element results in 8 new TET elements, each TRI results in 4 new TRI elements. Resulting blocks and sidesets in the output mesh will have the same IDs as the input mesh.

In its current form, UMR is run as an executable available on the LAN. It has the following options as displayed with the '-h' option:

Usage: ./build/extra/extra [OPTIONS] [INPUT] [OUTPUT]

Project home page: https://cee-gitlab.sandia.gov/meshing/extra

---

## Mesh Scaling

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_scaling.htm

**Contents:**
- Mesh Scaling
  - Command Syntax
  - Command Options
    - scale mesh [volume <ids>]
    - [multiplier <value, default=2.0>]
- Tet Mesh Scaling
- Hex Mesh Scaling
  - Hex Scale Mesh Command Options
    - [minimum <value, default=1>]
      - Refinement and Coarsening Levels

Cubit supports the scaling of hexahedra and tetrahedra meshes. Mesh Scaling allows a series of meshes to be built [typically] for solution convergence studies or other purposes. Each mesh has progressively larger or smaller elements. For example, if the input mesh has 10,000 hexahedra, scaling with a multiplier of 2.0 will result in a mesh of about 20,000 hexahedra, with approximately the same element orientation and size gradations as the original, as seen in Figure 1. Additional meshes can be built by scaling the original mesh with multipliers of 4, 6, 8, etc. Scaling by a value less than 1.0 will produce a mesh with fewer elements. Scaling by a negative value is not allowed. Convergence studies can be performed with much less computational cost than if traditional global refinement is used, because the element increase at each step of the series can be smaller.

scale mesh [volume <ids>] [multiplier <value, default=2.0>] [minimum <value, default=1>] [{SWEPT_BLOCKS | legacy | maintain_structure}] [feature_angle <value>] [force_structured in {[volume <ids>] [surface <ids>]}] [thin_gap_intervals <value, default=2>] [fix_all_gaps] [max_aspect_ratio <value> in volume <ids>] [max_feature_length <value, default=30>] [smooth_volume {ON|off}]

Specifying a list of volumes is optional. By default, all volumes will be scaled. For Hex Mesh Scaling, the specified volumes, together with any volumes merged with them, will be scaled. Tet Mesh Scaling only scales the specified volumes, preserving the shared mesh boundary with any non-participating volumes. This approach allows individual assembly components to be scaled, without scaling the entire model.

The target number of output elements is the number of input elements times the multiplier parameter. The default value is 2.0. For example: the mesh in Figure 2a has 3025 hex elements. After scaling by 2.0, the mesh in Figure 2b has 6804 hexes. Note the locations of new nodes are projected to lie on the associated CAD geometry, if any.

Figure 2a. Input mesh of 3025 hex elements.

Figure 2b. Output mesh of 6804 hexes, after scaling with a multiplier of 2.0.

Tetmesh scaling woks by using the original tet mesh as a background sizing mesh, with a size on each node to achieve the desired scale factor. The only command parameter relevant to tet mesh scaling is the multiplier parameter. All others are used for Hex Mesh Scaling.

Hex Mesh Scaling is more flexible than template-based global refinement methods, because it does not require that every element is refined, or refined in the same way. Instead, Hex Mesh Scaling decomposes the entire mesh into larger "blocks" of hexes, and then refines the blocks. In this way, Mesh Scaling supports increasing the element count by small multiplicative factors, e.g. 1.5, that are impossible with template based refinement. However, like template refinement, it can ensure that every location of the mesh is refined. These features can be useful for solution verification.

A traditional template-based refinement replaces each hexahedron with a 2x2x2 structured grid of hexahedra, increasing the element count by a factor of 8X. In contrast, Hex Mesh Scaling refines "blocks" of elements (not to be confused with Exodus element blocks). The block decomposition subdivides the entire mesh into structured (mapped) and swept blocks. A block may contain many elements, but is not allowed to cross geometric boundaries, boundary conditions, and loading constraints. For example, a block cannot have a curve or nodeset in its interior, nor hexes from multiple Exodus blocks. Blocks may be structured or logical sweeps. A structured block is restricted to be a grid of MxNxO hexes, so, its extent is limited by any surface nodes that do not have exactly four edges, etc. Hex Mesh Scaling remeshes the entire model conforming to the block decomposition, using the original mesh as a sizing function, multiplied by the scale factor.

The minimum parameter provides further control over the level of refinement. It is the minimum number of intervals added to each block-curve. Specifying minimum 1, which is the default, will guarantee that at least one interval is added to every element block in all 3 directions, which guarantees every part of the domain is scaled by at least a little bit. This can be "turned off" by specifying minimum 0.

The multiplier determines the target number of output hexes. There is no guarantee it will be achieved exactly. For minimum 0 and small multipliers, there is no guarantee that every block will be refined in all 3 directions. This is because the target number of elements may be reached first. This may lead to unevenly distributed refinement, with jumps in adjacent element sizes.

An uneven distribution may also result if adjacent blocks have significantly different MxNxO intervals; this is common with the legacy option. For example, for a 1x10x12 block adjacent to a 6x10x12 block, Mesh Scaling could output 2x11x13 and 7x11x13 blocks. The M value of the first block has doubled, 2/1, while the M value of the second block has only increased by 7/6. Thus, the user may observe a jump in the lengths of adjacent edges.

To coarsen a mesh, specify a multiplier less than one. For example, a multiplier of 0.9 will attempt to decrease the element count by 10%. Each block side will have its intervals decreased by the minimum value. A block must have at least one interval, so how far the mesh can be coarsened is limited by the distance between mesh irregularities, geometry, boundary condition and loading constraints.

Mesh Scaling is useful for solution verification, as it can easily generate a series of similar meshes of increasing mesh density. For best results, generate each mesh in the series by scaling the original mesh, rather than scaling the previous mesh of the series. It is suggested that each mesh uses a multiplier at least 2X larger, and a minimum at least one more, than the prior mesh. Small multipliers alone are unlikely to produce sufficient changes for solution verification. The minimum is especially useful for ensuring changes in regions that are initially coarse. A good set of (multiplier, minimum) parameters follows:

(2X, 1) (4X, 2) (8X, 3) (16X, 4), (prior *2, prior +1), etc.

A large minimum can cause quality problems and generate too many elements. For example, the minimum in the parameter series (2X, 1) (3X, 2) (4X, 3) (5X, 4) (6X, 5) (7X, 6) (8X, 7) etc. would likely be too aggressive. It would produce many more elements than the specified multiplier, potentially causing poor element quality or even mesh scaling failure. For a slowly increasing set of multipliers, a less aggressive minimum series is recommended, such as

(2X, 1) (3X, 1) (4X, 2) (5X, 2) (6X, 2) (7X, 2) (8X, 3) etc..

There are three major block decomposition variations to choose from. To understand their differences, one must first understand the two types of blocks: "structured" and "swept" blocks. A structured block is a MxNxO structured grid. A swept block is a single-source to single-target sweep of some subset of a single volume. That is, it is composed of a single surface of quad elements, projected some number of layers to form hexes.

The block decomposition options are swept_blocks (default), maintain_structure and legacy. For legacy, only structured blocks are used. For swept_blocks and maintain_structure, the decomposition constructs large swept blocks wherever logical sweeps can be identified, and structured blocks otherwise. The main difference is that swept_blocks remeshes the source surfaces of swept blocks from scratch. In contrast, maintain_structure partition each swept block into structured sub-blocks, and remeshes by selectively refining those sub-blocks. Thus swept_blocks may change the number and relative location of irregular nodes, whereas maintain_structure keeps them the same.

Typically, swept_blocks and maintain_structure provide smoother, more evenly distributed refinements compared to legacy. This is because with swept blocks, there are typically significantly fewer blocks in the decomposition. Having fewer blocks increases the likelihood that each block will receive at least some refinement before the multiplier is reached.

However, legacy and maintain_structure provide element orientations and structure closer to the original mesh than swept_blocks. This is because structured blocks maintain the irregular nodes.

Often maintain_structure provides both element orientations closer to the original mesh and a smoother, more evenly distributed refinement. Its structured blocks preserve orientations and structure. Its swept blocks provide the freedom to distribute changes, and smooth the mesh, across its structured sub-blocks.

In some cases, the user may want to use swept blocks in only some parts of the model. The original mesh may have small regions with carefully constructed meshes. Using swept_blocks can destroy these constructions, replacing them with pave-and-sweep meshes. These constructions can be preserved by specifying force_structured for the surfaces and volumes containing them.

For example, see Figures 3, 4 and 5. In Figure 3 surface 108 was meshed with great care to ensure a structured mesh around the holes, while surface 34 was meshed with paving. Since surface 108 has irregular nodes, it appears to Mesh Scaling as the source surface of a swept block. Figure 4 illustrates the resulting mesh from the command "scale mesh multi 2". Notice the structured meshes around the holes have been replaced with a standard paved mesh. Figure 5 illustrates preserving the structured holes of surface 108 while allowing surface 34 to be repaved. The command was "scale mesh multi 2 force_structured in surface 108". A different mesh would result from the command scale mesh multi 2 force_structured in volume 1 , because this would also preserve the irregular nodes in surface 34, resulting in more blocks and a less smooth mesh.

Figure 3. Input mesh. Surface 108's mesh has desired structure and irregular nodes. Surface 34 contains a paved mesh.

Figure 4. Output mesh from the command "Scale Mesh Multi 2". The mesh on surface 108 is replaced with a paved mesh.

Figure 5. Output mesh from the command "Scale Mesh Multi 2 force_structured in Surface 108". The desired features are maintained, while swept blocks are used in unimportant regions.

For the maintain_structure option, the thin_gap_intervals parameter determines how thin gaps are defined. If two disjoint curves of a surface come close together, the space between them is considered a "thin gap" if the number of intervals across that space is at most thin_gap_intervals. Mesh scaling gives high priority to adding intervals within thin gaps. By default, the position of some nodes within thin gaps are fixed to help reduce skew. The fix_all_gaps option fixes all nodes in thin gaps. Features, e.g. curves and gaps, longer than max_feature_length intervals will be split into multiple features. This results in fixing additional nodes along the feature to help reduce skew.

In general, maintain_structure should result in a smoother scaled mesh than the other algorithms, however, sometimes it can introduce some skew in the scaled elements. If skew is introduced by scaling using maintain_structure, try either increasing the thin_gap_intervals parameters, specifying fix_all_gaps, decreasing the max_feature_length parameter, or all three.

The feature_angle and max_aspect_ratio options affect the formation of swept blocks. These are alpha, experimental commands.

If smooth_volume is on, then the volume mesh is smoothed as a post-process if it has poor quality elements, and smaller minimum quality than the original mesh. By default, smooth_volume is on.

---

## Mesh Smoothing

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/mesh_smoothing.htm

**Contents:**
- Mesh Smoothing
- Global Smoothing
- Focused Smoothing on Groups of Mesh Entities
- Smooth Tolerance
- Boundary Mesh Smoothing

After generating the mesh, it is sometimes necessary to modify that mesh, either by changing the positions of the nodes or by removing the mesh altogether. CUBIT contains a variety of mesh smoothing algorithms for this purpose. Node positions can also be fixed, either by specific node or by geometry entity, to restrict the application of smoothing to non-fixed nodes.

Mesh smoothing in CUBIT operates in a similar fashion to mesh generation, i.e. it is a two-step process whereby a smooth scheme is chosen and set, then a smooth command performs the actual smoothing. Like meshing algorithms, there is a variety of smoothing algorithms available, some of which apply to multiple geometry entity types and some which only apply to one specific type (these algorithms are described below.) To smooth the mesh on a geometry entity, the user must perform the following steps:

{Curve|Surface|Volume} <range> Smooth Scheme <scheme>

where <scheme> is any acceptable smooth scheme described in this section. Also set any scheme-specific information, using the smooth scheme setting commands described below.

Smooth Surface <range> [Global]

Smooth {Body|Volume|Group} <range>

Groups of entities may be smoothed, by smoothing a group or a body.

If a Body is specified, the volumes in that Body are smoothed. If a Group is specified, only the volume meshes within these groups are smoothed - no smoothing of the surface meshes is performed.

When smoothing a set of surfaces, the keyword global can be added to the smooth command such as

Smooth Surface <range> [Global]

If the smoothing algorithm for two neighboring surfaces are both allowed to move boundary nodes, then appending the "global" keyword will often result in a higher quality mesh near the curve(s) shared by those two surfaces.

Meshed entities such as hexes or tris can be smoothed individually or in groups by specifying the entities in a list.

Smooth {Hex|Tet} <range>[Scheme {Equipotential|Laplacian|Random}]

Smooth {Face|Tri} <range>[Scheme {Laplacian|Centroid|Winslow}] [Target Surface <id>]

Smooth Edge <id_range> [Scheme Laplacian] [Target Surface <id>]

The Smooth Edge command allows the user to smooth individual edges owned by a curve. Specifying a target curve allows the user to move the edges on a meshed curve to a different curve. The target curve or surface does not necessarily need to be the owning curve or surface of the nodes. For example, if given two curves (A and B) and curve A was meshed, the target smoothing could be used to move all of the edges of curve A onto curve B. The smooth scheme option for the edge smoothing is currently limited only to the laplacian scheme.

The Smooth Face|Tri command is used to smooth individual faces or triangles. The target option is similar to the curve target option above. Faces or Tris can be smoothed to a surface that is not necessarily the owning surface; in fact, the faces or tris do not even have to be attached to any surface. This makes this option especially helpful for smoothing free meshes. Specifying a smooth scheme allows for relaxation based surface smoothers (i.e. centroid area pull, laplacian, winslow) to be utilized during targeted smoothing. It is not currently enabled for optimization based smoothing schemes.

Smoothing algorithms move nodes in an attempt to improve the quality of the mesh elements. Most of these algorithms are iterative, and the algorithm terminates when some criterion is met. Specifically, for the Laplacian and Equipotential style smoothers, smoothing is terminated either by satisfying a smoothing tolerance or by performing the maximum number of smoothing iterations. For these smoothers, the smooth tolerance may be set by the user:

[Set] Smooth Tolerance <tol>

The value <tol> tells the smoother to stop when node movement is less than tol * local_minimum_edge_length.

The default value for tol is 0.05. The maximum number of iterations may be set by the user. For volumes, the smooth tolerance and iterations may also be set by

(Note: The above command affects all smoother that respect tolerance.)

Volume Smooth Tolerance <tol>

Volume Smooth Iterations <iters>

(Note: The above two commands only affect the volume smoothers.)

Where used in the smooth schemes below, the Free keyword permits the nodes lying on the bounding entities to "float" along those entities; without this keyword, boundary nodes remain fixed.

Nodal positions may be fixed so that no smoothing scheme, either implicit or explicit, will move them, with the following command:

{Curve|Surface|Volume} <range> Node Position {Fixed|Free}

Node <range> Position {Fixed|Free}

The following command does not fix nodal positions, but does fix the connectivity of the mesh, preventing certain volume schemes from changing the bounding mesh:

{Curve|Surface|Volume} Mesh {Fixed|Free}

The additional following scheme is available for research purposes and can be used only after issuing a 'set developer on' command.

---

## Mesh Topology Check

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/topology.htm

**Contents:**
- Mesh Topology Check

The ability to check for non-manifold topology among mesh entities is given with the following command.

Quality Check Topology [[Hex <range>] [Tet <range>] [Face <range>] [Tri <range>]]

If no entity list is given, it will check the entire model. Multiple element types are also allowed. The command checks for non-manifold boundaries (edges) in the element set entered. For quads and tris the command lists and highlights all edges that have more than two tris or faces connected.

Figure 1. Topology check for quads and tris

For hexes and tets it looks for edges with two or more elements connected that do not share common faces.

Figure 2. Topology check for hexes and tets

Additional topology checks fall into three categories:

The model edge check will find edges with adjoining quadrilaterals or triangles whose angles between the surface normals exceed a specified value. The default angle is 40 degrees.

The following commands check for model edges:

Topology check model edge {group|volume|surface|curve} <id_range> [angle <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

Topology check model edge {block|sideset|nodeset} <id_range> [angle <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

Topology check model edge {hex|tet|face|tri|edge} <id_range> [angle <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

The optional angle parameter allows the user to specify a custom angle value against which the check will be performed. The default angle is 40 degrees.

By default, the command will draw the model edges.

By default, very little information is output to the command line. The optional verbose parameter will output a list of the flagged model edges.

By default, the model edges will be written to the group ‘model_edges’. Optionally, the user may specify no grouping, or the user may specify the name or id of an existing group into which the model edges will be written. The contents of the existing group will be replaced by the model edges.

Cubit will verify the interfaces between sections of a model. The existence of coincident nodes, for example, may not necessarily be an error in the model if the nodes are in sliding contact or are constrained by some type of multi-point constraint. The existence of coincident quadrilaterals or triangles may indicate that the model is not correctly joined.

The following commands check for coincident nodes.

Topology check coincident node {group|volume|surface|curve|vertex} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

Topology check coincident node {block|sideset|nodeset} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

Topology check coincident node {hex|tet|face|tri|edge|node} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

The optional tolerance parameter allows the user to specify a custom tolerance value against which the check will be performed. The default tolerance is 1.0 e-6.

The default group name is ‘coincident_nodes.’

All other options behave similarly to those described above under Model Edge Check.

The following commands check for coincident quadrilaterals.

Topology check coincident quad {group|volume|surface} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

Topology check coincident quad {block|sideset|nodeset} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

Topology check coincident quad {hex|tet|face} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

The default group name is ‘coincident_quads.’

All other optional parameters behave similarly to those described above.

The following commands check for coincident triangles.

Topology check coincident tri {group|volume|surface} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

Topology check coincident tri {block|sideset|nodeset} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

Topology check coincident tri {hex|tet|face|tri} <id_range> [tolerance <value>] DRAW|nodraw|highlight] [BRIEF|verbose] [RESULT GROUP[{<name>|{<id>}|nogroup]

The default group name is ‘coincident_tris.’

All other optional parameters behave similarly to those described above.

---

## Mesh Validity

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_validity.htm

**Contents:**
- Mesh Validity

After a mesh is generated, it is checked to ensure that the mesh has valid connectivity. If an invalid mesh is formed, then CUBIT automatically deletes it. This default behavior can be changed with the following command:

Set Keep Invalid Mesh [on|off]

The current behavior can be viewed with the following command:

List Keep Invalid Mesh

The Jacobian quality metric is also computed automatically to check quality after a mesh is generated. If the quality is poor, a warning is printed to the terminal.

---

## Mesh Visualization

**URL:** https://coreform.com/cubit_help/environment_control/graphics_window_control/mesh_slicing.htm

**Contents:**
- Mesh Visualization
- Notes on Mesh Slicing
- Mesh Slicing Command

A volume mesh can be viewed one layer at a time using a visualization tool known as mesh slicing. This tool divides the elements of one or more volumes into axis-aligned layers, and then allows the mesh to be displayed one layer at a time. Mesh slicing is especially useful to view the quality of swept meshes that are axis aligned.

Mesh slicing is only intended to be a rough visualization tool. Because the average mesh edge length is used to determine the thickness of each layer, a layer may be more than one element deep. Unstructured meshes, meshes with large variations in edge length, and non-axis-aligned meshes will be more difficult to visualize with this tool.

Mesh slicing can be started either by entering a keypress in the graphics window, which slices the mesh of the entire model, or by entering the command

Graphics Slice {Body | Volume} <id_range> Axis {X | Y | Z}

which slices only the bodies or volumes indicated, with a plane along the axis specified.

Key presses in the graphics window which control mesh slicing are summarized in the following table.

See Graphics Clipping Plane for instructions on clipping the graphics using the GUI clipping plane.

---

## Metrics for Edge Elements

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/edge_length.htm

**Contents:**
- Metrics for Edge Elements
- Quality Metric Definitions:
- Comments on Algebraic Quality Measures

The metrics used for edge elements in CUBIT are summarized in the following table:

Length: Distance between beginning and ending nodes of an edge

---

## Metrics for Hexahedral Elements

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/hexahedral_metrics.htm

**Contents:**
- Metrics for Hexahedral Elements
- Hexahedral Quality Definitions
  - High Order Elements
- References for Hexahedral Quality Measures

The metrics used for hexahedral elements in CUBIT are summarized in the following table:

With a few exceptions, as noted below, Cubit supports quality metric calculations for linear hexahedral elements only. When calculating quality metrics, that only support linear elements, for a higher order hexahedral element, Cubit will only use the corner nodes of the element.

Aspect Ratio: Maximum edge length ratios at hex center.

Skew: Maximum |cos A| where A is the angle between edges at hex center.

Taper: Maximum ratio of lengths derived from opposite edges.

Stretch: Sqrt(3) * minimum edge length / maximum diagonal length.

Diagonal Ratio: Minimum diagonal length / maximum diagonal length.

Dimension: Pronto-specific characteristic length for stable timestep calculation. Char_length = Volume / 2 grad Volume.

Condition No. Maximum condition number of the Jacobian matrix at 8 corners.

Mass Increase Ratio: This metric stems from the global target time step and the element time step. The density required to fulfill the target time step (via mass scaling) divided by the block density is termed the mass increase ratio. Because the density within each element is constant, a ratio in the element density is equivalent to a ratio in the element mass. This metric calculates the requisite density for each element to attain the prescribed target time step. If that density is greater than the defined density, the metric yields a value greater than one. This desired global time step is set by the user with the command:

[Set] Target Timestep <value>

As stated, this metric computes the element based timestep metric and consequently element blocks must be defined with material properties of Young’s modulus, Poisson’s ratio, and a target timestep must be set.

If this metric is computed in the context of a block ('quality block 1 mass increase ratio') an accompanying printout of the mass increase per block is given.

Node Distance: Minimum distance between any two adjacent corner nodes.

Scaled Jacobian: For linear elements the minimum Jacobian divided by the lengths of the 3 edge vectors.

Shear: 3/Mean Ratio of Jacobian Skew Matrix

Shape: 3/Mean Ratio of weighted Jacobian Matrix

Relative Size: Min(J, 1/J), where J is the determinant of weighted Jacobian matrix

Shear & Size: Product of Shear and Size Metrics

Shape & Size: Product of Shape and Size Metrics

Timestep: The approximate maximum timestep that can be used with this element in explicit transient dynamics analysis. This critical timestep is a function of both element geometry and material properties. To compute this metric on hexes, the hexes must be contained in an element block that has a material associated to it, where the materials poisson's ratio, elastic modulus, and density are defined.

The preceding metrics will measure quality based only on the 8 corner nodes of the hexahedron. The following metrics also take into account the mid nodes.

Distortion: {min(|J|)/actual volume}*parent volume, parent volume = 8 for hex. Cubit also supports Distortion calculations for hex20 elements.

Element Volume: For linear hexes, the jacobian at hex center. For higher-order hexes, the hex is subdivided into sub-tets, the volumes of which are summed.

Jacobian: Minimum pointwise volume of local map at 8 corners at center of hex. Cubit also supports Jacobian calculations for hex27 elements.

---

## Metrics for Quadrilateral Elements

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/quadrilateral_metrics.htm

**Contents:**
- Metrics for Quadrilateral Elements
- Quadrilateral Quality Definitions
- Comments on Algebraic Quality Measures
- References for Quadrilateral Quality Measures
- Details on Robinson Metrics for Quadrilaterals

The metrics used for quadrilateral elements in CUBIT are summarized in the following table:

Aspect Ratio: Maximum edge length ratios at quad center

Skew: Maximum |cos A| where A is the angle between edges at quad center

Taper: Maximum ratio of lengths derived from opposite edges

Warpage: Cosine of Minimum Dihedral Angle formed by Planes Intersecting in Diagonals

Element Area: Jacobian at quad center

Stretch: Sqrt(2) * minimum edge length / maximum diagonal length

Minimum Angle: Smallest included quad angle (degrees).

Maximum Angle: Largest included quad angle (degrees).

Condition No. Maximum condition number of the Jacobian matrix at 4 corners

Jacobian: Minimum pointwise volume of local map at 4 corners & center of quad

Scaled Jacobian: For linear elements the minimum Jacobian divided by the lengths of the 2 edge vectors

Shear: 2/Condition number of Jacobian Skew matrix

Shape: 2/Condition number of weighted Jacobian matrix

Relative Size: Min( J, 1/J ), where J is determinant of weighted Jacobian matrix

Shear and Size: Product of Shear and Relative Size

Shape and Size: Product of Shape and Relative Size

Distortion: {min(|J|)/actual area}*parent area, parent area = 4 for quad

Deviation: Absolute distance from quad centroid to its associated surface

Shape, Relative Size, Shape & Size, and Shear are algebraic quality metrics that apply to quadrilateral elements. Cubit encourages the use of these metrics since they have certain nice properties (see reference 5 below). The metrics are referenced to a square-shaped quadrilateral element, thus deviations from a square are measured in various ways.

Shape measures how far skew and aspect ratio in the element deviates from the reference element.

Relative size measures the size of the element vs. the size of reference element. If the element is twice or one-half the size of the reference element, the relative size is one-half. The reference element for the Relative Size metric is a square whose area is determined by the average area of all the quadrilaterals on the surface mesh under assessment

Shape and size metric measures how both the shape and relative size of the element deviate from that of the reference element.

The SHEAR metric is based on the condition number of the skew matrix. SHEAR is really just an algebraic skew metric but, since the word skew is already used in the list of quad quality metrics, Cubit has chosen to use the word 'shear.'

Shear = 1 if and only if quadrilateral is a rectangle.

The Robinson 'skew' metric equals the ideal (zero) if the quad is a rectangle. It also attains the ideal if the quad is a trapezoid, a kite, or even triangular!

The quadrilateral element quality metrics that are calculated are aspect ratio, skew, taper, element area, and stretch. The calculations are based on metrics described in (Robinson, 87). An illustration of the shape parameters is shown in Figure 1, below. The stretch metric is calculated by dividing the length of the shortest element edge divided by the length of the longest element diagonal.

Figure 1. Illustration of Quadrilateral Shape Parameters (Quality Metrics)

---

## Metrics for Tetrahedral Elements

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/tetrahedral_metrics.htm

**Contents:**
- Metrics for Tetrahedral Elements
- Tetrahedral Quality Definitions
  - High Order Elements
- References for Tetrahedral Quality Measures

The metrics used for tetrahedral elements in CUBIT are summarized in the following table:

With a few exceptions, as noted below, Cubit supports quality metric calculations for linear tetrahedral elements only. When calculating quality metrics, that only support linear elements, for a higher order tetrahedral element, Cubit will only use the corner nodes of the element.

Aspect Ratio Beta: CR / (3.0 * IR) where CR = circumsphere radius, IR = inscribed sphere radius

Aspect Ratio Gamma: Srms**3 / (8.479670*V) where Srms = sqrt(Sum(Si**2)/6), Si = edge length

Condition No.: Condition number of the Jacobian matrix at any corner

Inradius: For all tets but tetra10s, the radius of the smallest, fully contained sphere of the linear tet. For tetra10s, the mid-edge nodes are used to subdivide the tet into 12 linear sub-tets. The inradius is the smallest inradius of the 12 linear sub-tets * 2.3.

Jacobian: Minimum pointwise volume at any corner. Cubit also supports Jacobian calculations for tetra15 and tetra10 elements.

For tetra15 or tetra10 elements, all 15 or 10 nodes are included for the Jacobian calculation. For all other tet types, only the corner nodes are considered.

Node Distance: Minimum distance between any two adjacent corner nodes.

Scaled Jacobian: For linear elements the minimum Jacobian divided by the lengths of 3 edge vectors

Shape: 3/Mean Ratio of weighted Jacobian Matrix

Relative Size: Min(J, 1/J), where J is the determinant of the weighted Jacobian matrix

Shape & Size: Product of Shape and Relative Size Metrics

The preceding metrics will measure quality based only on the 4 corner nodes of the tetrahedron. The following metrics also take into account the mid nodes.

Distortion: {min(|J|)/actual volume}*parent volume, parent volume = 1/6 for tet. Cubit also supports Distortion calculations for tetra10 elements.

For tetra10 elements, the distortion metric can be used in conjunction with the shape metric to determine whether the mid-edge nodes have caused negative Jacobians in the element. The shape metric only considers the linear (parent) element. If a tetra10 has a non-positive shape value then the element has areas of negative Jacobians. However, for elements with a positive shape metric value, if the distortion value is non-positive then the element contains negative Jacobians due to the mid-side node positions.

Element Volume: For linear tets, (1/6) * Jacobian at corner node. For higher order tets, the tet is subdivided into sub-tets, the volumes of which are summed.

Normalized Inradius: Ratio of minimum subtet inner radius to tet outer radius (circumsphere). Subtets are defined by subdividing the tet into 12 smaller tets by using a common point at the centroid of the tet and the 6 mid-edge nodes as shown in Figure 1. The minimum in-radius of any of these 12 tets normalized by its parent outer-radius and a constant is used to determine this metric. The Normalized Inradius metric is also valid for linear elements, except that all mid-edge nodes are defined as the midpoint of their corner nodes.

Figure 1. Subtet subdivision used for determining Normalized Inradius quality metric

Mean Ratio: General description: Mean ratio quality metric measures the deviation of a tetrahedral element from an equilateral tetrahedron through the root-mean-squared edge length. In this context, we employ a volume ratio. For a 4-node tet, the volume is compared to the cube of root-mean-squared length of the six edges. For the 10-node tet, 12 sub-tets are formed and minimum mean ratio of the 12 is returned. Unlike the normalized inradius, the mean ratio is quite sensitive to a single, highly-elongated sub-tet. We note that for an equilateral 10-node tetrahedral element, there are two families of sub-tetrahedra. Sub-tets connected to the corner nodes or parent nodes of the 4-node tet have a mean ratio of 1 by construction. They are equilateral tets. The other family of sub-tets are not equilateral tets. These interior sub-tets connected entirely to mid-edge nodes are scaled such that all sub-tetrahedra have a mean ratio of 1 for an equilateral tet.

Mass Increase Ratio: This metric stems from the global target time step and the element time step. The density required to fulfill the target time step (via mass scaling) divided by the block density is termed the mass increase ratio. Because the density within each element is constant, a ratio in the element density is equivalent to a ratio in the element mass. This metric calculates the requisite density for each element to attain the prescribed target time step. If that density is greater than the defined density, the metric yields a value greater than one. This desired global time step is set by the user with the command:

[Set] Target Timestep <value>

As stated, this metric computes the element based timestep metric and consequently element blocks must be defined with material properties of Young’s modulus, Poisson’s ratio, and a target timestep must be set.

If this metric is computed in the context of a block ('quality block 1 mass increase ratio') an accompanying printout of the mass increase per block is given.

Timestep: The approximate maximum timestep that can be used with this element in explicit transient dynamics analysis. This critical time step is a function of both element geometry and material properties. To compute this metric on tets, the tets must be contained in an element block that has a material associated to it, where the materials poisson's ratio, elastic modulus, and density are defined.

Note that, for tetrahedral elements, there are several definitions of the term "aspect ratio" used in literature and in software packages. Please be aware that the various definitions will not necessarily give the same or even comparable results.

---

## Metrics for Triangular Elements

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/triangular_metrics.htm

**Contents:**
- Metrics for Triangular Elements
- Approximate Triangular Quality Definitions:
- Comments on Algebraic Quality Measures
- References for Triangular Quality Measures

The metrics used for triangular elements in CUBIT are summarized in the following table:

Maximum Angle: Maximum included angle in triangle

Minimum Angle: Minimum included angle in triangle

Aspect Ratio: Ratio of circumcirle to inradius

Aspect Ratio Alpha: Ratio of longest edge length to inradius

Condition No: Condition number of the Jacobian matrix

Deviation: Absolute distance from triangle centroid to associated surface

Scaled Jacobian: Minimum Jacobian divided by the lengths of 2 edge vectors

Relative Size: Min( J, 1/J ), where J is determinant of weighted Jacobian matrix

Shape: 2/Condition number of weighted Jacobian matrix

Shape Size: Product of Shape and Relative Size

Distortion: {min(|J|)/actual area}*parent area, parent area = 1/2 for triangular element

Element Area: (1/2) * Jacobian at corner node

Normalized Inradius: 4.0 * minimum_subtri_inradius / radius of circle containing three corner nodes

Relative Size, Shape, and Shape Size are algebraic metrics, which have well behaved properties. Cubit encourages the use of these metrics over other metrics. These metrics are referenced to an ideal element which, in the case of triangular elements, is an equilateral triangle. Thus deviations from an equilateral triangle are measured in various ways by the algebraic metrics. Relative size measures the size of the element vs. the size of reference element. If the element is twice or one-half the size of the reference element, the relative size is one-half. By default, the size of the reference element is the average size of all the elements that the quality command is currently evaluating.

The shape and size metric measures how both the shape and relative size of the element deviate from that of the reference element.

---

## Metrics for Wedge Elements

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/wedge_metrics.htm

**Contents:**
- Metrics for Wedge Elements
- Wedge Quality Definitions

The metrics used for wedge elements in CUBIT are summarized in the following table:

With a few exceptions, as noted below, Cubit supports quality metric calculations for linear wedge elements only. When calculating quality metrics, that only support linear elements, for a higher order wedge element, Cubit will only use the corner nodes of the element.

Aspect Ratio: Maximum edge length ratios at the wedge center

Element Volume: Calculated by dividing the wedge into 11 tetrahedron and summing the volume of each.

Condition No.: Condition number of the Jacobian matrix at any corner

Jacobian: Minimum pointwise volume at any corner. Cubit also supports Jacobian calculations for Wedge21elements.

Scaled Jacobian: For linear elements the minimum Jacobian divided by the lengths of 3 edge vectors

Shape: 3/Mean Ratio of weighted Jacobian Matrix

Distortion: {min(|J|)/actual volume}*parent volume

---

## Metrics supporting higher-order element types

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_quality_assessment/higher_order_metrics.htm

**Contents:**
- Metrics supporting higher-order element types
- Edges
- Triangles
- Quadrilateral
- Tetrahedron
- Hexahedron

The following tables details the quality metrics that support some higher order element types:

---

## Parallel Meshing

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/parallel.htm

**Contents:**
- Parallel Meshing

Cubit has been designed as a serial application, using a single CPU to generate its meshes. In some cases, where memory or time constraints are critical, parallel meshing may be necessary. Cubit currently provides a few separate applications designed to run in parallel either on a desktop or on massively parallel cluster machines. In these cases, Cubit can be used as a pre-processor to manipulate geometry and set up for meshing, however the actual meshing procedure is performed as a separate process or on another machine. The following two parallel meshing applications are available:

A separate application for parallel refinement is also available:

---

## Pave

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/pave.htm

**Contents:**
- Pave
- Element Shape Improvement
- Controlling Flattening of Elements
- Controlling the Grid Search for Intersection Checking
- Controlling the Paver Sizing Function
- Controlling Paver Cleanup

Summary: Automatically meshes a surface with an unstructured quadrilateral mesh.

Surface <range> Scheme Pave Related Commands:

[Set] Paver Diagonal Scale <factor (Default = 0.9)> [set] Paver Grid Cell <factor (Default = 2.5)>[set] Paver LinearSizing {Off | ON} Surface <range> Sizing Function Type ...

[Set] Paver Smooth Method {DEFAULT | Smooth Scheme | Old}

[Set] Paver Cleanup {ON|Off|Extend}

Paving (Blacker, 91; White, 97) allows the meshing of an arbitrary three-dimensional surface with quadrilateral elements. The paver supports interior holes, arbitrary boundaries, hard lines, and zero-width cracks. It also allows for easy transitions between dissimilar sizes of elements and element size variations based on sizing functions. Figure 1 shows the same surface meshed with mapping (left) and paving (right) schemes using the same discretization of the boundary curves.

Figure 1. Map (left) and Paved (right) Surface Meshes

When meshing a surface geometry with paving, clean-up and smoothing techniques are automatically applied to the paved mesh. These methods improve the regularity and quality of the surface mesh. By default the paver uses its own smoothing methods that are not directly-callable from CUBIT. Using one of CUBIT's callable smoothing methods in place of the default method will sometimes improve mesh quality, depending on the surface geometry and specific mesh characteristics. If the paver produces poor element quality, switching the smoothing scheme may help. This is done by the command:

[set] Paver Smooth Method {DEFAULT | Smooth Scheme | Old}

When the "Smooth Scheme" is selected, the smoothing scheme specified for the surface will be used in place of the paver's smoother. See "Mesh Smoothing" for more information about the available smoothing schemes in CUBIT.

The smoothers flatten elements, such as inserted wedges, that have two edges on the active mesh front. In meshes where this "corner" is a real corner, flattening the element may give an unacceptable mesh. The following command controls how much the diagonal of such an element is able to shrink.

[set] Paver Diagonal Scale <factor (Default = 0.9)>

The range of for the scale factor is 0.5 to 1.0. A scale factor of 1.0 will force the element to be a parallelogram as long as it is on the mesh front. A value of 0.5 will allow the diagonal to be half its calculated length. The element may became triangular in shape with the two sides on the mesh front being collinear.

The paver divides the bounding box of a surface into a number of cells based on the average length of an element. It uses these cells to speed intersection checking of new element edges with the existing mesh. If both very long and very short edges fall in the same area, it is possible that a long edge which spans the search region is excluded from the intersection check when it does intersect the new element. The following command allows the user to adjust the size of the grid cells.

[set] Paver Grid Cell <factor (Default = 2.5)>

The grid cell factor is a multiplier applied to the average element size, which then becomes the grid cell size. The surface's bounding box is divided by this cell size to determine the number of cells in each direction. A larger cell size means each cell contains more nodes and edges. A smaller cell size means each cell has fewer nodes and edges. A larger cell size forces the intersection algorithm to check more potential intersections, which results in long paver times. A smaller cell size gives the intersection algorithm few edges to check (faster execution) but may result in missed intersections where the ratio of long to short element edges is great. Increase this value if the paver is missing intersections of elements.

[set] Paver LinearSizing {Off | ON}

Setting paver linear sizing to "off" will keep the default behavior. The size of the element will be based on the side(s) of the element on the mesh front. For a discussion of sizing functions, including how to automatically set up size transitions, see Adaptive Meshing.

The paver uses a mesh clean-up process to improve mesh quality after the initial paving operation. Clean-up applies local connectivity corrections to increase the number of interior mesh nodes that are connected to four quadrilaterals. Sometimes it fails to improve the mesh. The following command allows the user to control some aspects of the clean-up process.

[Set] Paver Cleanup {ON|Off|Extend}

The default option is to clean-up the mesh. The off option will turn clean-up off and may give an invalid mesh. The extend option enables a non-local topology replacement algorithm. The command without any option will list the current setting.

The extend option attempts to group several defective nodes in a region that may be replaced with a template that has fewer defects. The images below show a mesh before and after using this option.

Figure 2. Paved mesh before using cleanup extend

Figure 3. Paved mesh after using cleanup extend

---

## pCamal

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/pcamal.htm

**Contents:**
- pCamal
- Exporting a Parallel Mesh for pCAMAL

pCamal is an application written and maintained by the Cubit development team. It is designed to work in a distributed computing environment to generate 3D hex elements of a sweep mesh. It first uses the serial Cubit application to generate the 2D quad elements. These elements are written to a file that can then be used by pCamal to generate the most time consuming and memory intensive portion of the mesh: the 3D hex elements. The following describes how to set up the necessary inputs to pCamal using Cubit's sweeping command.

To set up for pCamal, first use the parallel meshing setting:

Set Parallel Meshing {on|OFF}

The following command can be used for exporting a mesh in exodus format for use with pCAMAL

Export Parallel "<filename>" [Block <id_list>] [Overwrite] [Processor <number>]

The options are the same as those for the export genesis command except for the addition of the processor option.

The processor option allows the user to specify the number of processors that will be used to mesh the volume with the pCAMAL option. This same option exists in the pCAMAL application and is more often used there since the number of available processors is known then rather than when the output file is created in Cubit.

If the processor option is given, Cubit attempts to balance the number of sweepable volumes to run on N processors by converting many-to-one sweeps to one-to-one sweeps, subdividing the sweep volume along its sweep direction, or partitioning the source surface of a one-to-one sweep if the number of source quads is much larger than the number of layers.

To determine if you are currently in parallel meshing mode you may list the current status using the List Parallel command.

List Parallel Meshing

Note: pCamal is not currently distributed with the current release of Cubit. Contact the Cubit developers if you are interested in obtaining a copy of the executable for linux operating systems.

---

## Pentagon

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/pentagon.htm

**Contents:**
- Pentagon

Summary: Produces a pentagon-primitive mesh for a surface

Surface <range> Scheme Pentagon

The pentagon scheme is a meshing primitive for 5-sided regions. It is similar to the triprimitive and polyhedron schemes, but is hard-coded for 5 sided surfaces.

The pentagon scheme indicates the region should be meshed as a pentagon. The scheme works best if the shape has 5 well-defined corners; however shapes with more corners can be meshed. The algorithm requires that there be at least 10 intervals (2 per side) specified on the curves representing the perimeter of the surface. In addition, the sum of the intervals on any three connected sides must be at least two greater than the sum of the intervals on the remaining two sides. Figure 1 shows two examples of pentagon meshes.

Figure 1. Examples of Pentagon Scheme Meshes

---

## Periodic Intervals

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/periodic_intervals.htm

**Contents:**
- Periodic Intervals

The number of intervals on a periodic surface, such as a cylinder, in the dimension that is not represented by a curve is usually set implicitly by the surface size.

However, periodic intervals and firmness can be specified explicitly by the following commands:

Surface <range> Periodic Interval <intervals>

Surface <range> Periodic Interval {Default|Soft|Hard}

---

## Pinpoint

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/pinpoint.htm

**Contents:**
- Pinpoint

Summary:Meshes a curve with node spacing specified by the user.

Curve <range> Scheme Pinpoint Location <list of doubles>

The Pinpoint scheme allow the user to specify exactly where on a curve to place nodes. The list of doubles are absolute positions, measured from the start vertex. The user can enter as many as needed, and they do not need to be in numerical order. Below is an example of a curve that has been meshed using the following scheme:

curve 2 scheme pinpoint location 1 4 5 6 6.2 6.4 6.6 9:

---

## Polyhedron

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/polyhedron.htm

**Contents:**
- Polyhedron

Applies to: Surfaces and Volumes.

Summary: Produces an arbitrary-sided block primitive mesh for a surface or volume.

Volume <range> Scheme Polyhedron

Surface <range> Scheme Polyhedron

The polyhedron scheme is a meshing primitive for 2d and 3d n-sided regions. This is similar to the triprimitive , tetprimitive, and pentagon schemes, except rather than 3, 4, or 5 sides, it allows an arbitrary number of sides. The scheme works best on convex regions. Surfaces must have only one loop, and each vertex must be connected to exactly two curves on the surface (e.g., no hardlines). Volumes must have only one shell, each vertex must be connected to exactly three surfaces on the volume, and each surface should be meshed with scheme polyhedron. There are some interval assignment requirements as well, which should be automatically handled by CUBIT.

If the polyhedron scheme is specified for the volume, then the surfaces of the volume are automatically assigned scheme polyhedron as well, unless they were hard-set by the user. Schemes should be specified on all volumes of an assembly prior to meshing any of them. Scheme polyhedron attaches extra data to volumes; if Cubit is behaving strangely, the user may need to explicitly remove that data with a reset volume all, or similar command.

Scheme polyhedron was designed for assemblies of material grains, where each volume is roughly a Voronoi region, and the assembly is a periodic space-filling model (tile). Figure 1 shows two examples of polyhedron meshes.

Figure 1. Examples of Polyhedron Scheme Meshes

---

## QTri

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/conversion/qtri.htm

**Contents:**
- QTri

Summary: Meshes surfaces using a quadrilateral scheme, then converts the quadrilateral elements into triangles.

Surface <range> Scheme Qtri [Base Scheme quad_scheme>]

QTri { Surface <range> | Face <range> }

Set QTri Test {Angle|Diagonal}

QTri is used to mesh surfaces with triangular elements. The surface is, first, meshed with the quadrilateral scheme, and, then, the generated quads are split along a diagonal to produce triangles. The first command listed above sets the meshing scheme on a surface to QTri. The second form sets the scheme and generates the mesh in a single step.

In the first command, the user has the option of specifying the underlying quadrilateral meshing scheme using the base scheme <quad_scheme> option. If no base scheme is specified, CUBIT will automatically select a scheme. For non-periodic surfaces, the base scheme will be set to scheme pave. For periodic surfaces, the base scheme will be set to scheme map.

Generally, the second command, Qtri Surface <range>, is used on surfaces that have already been meshed with quadrilaterals. If, however, this command is used on a surface that has not been meshed, a base scheme will automatically be selected using CUBIT’s auto-scheme capabilities. The user can over-ride this selection by specifying a quadrilateral meshing scheme prior to using the qtri command (using the Surface <range> Scheme <quad_scheme> command). QTri may also be performed on quadrilateral elements on a surface or a subset of quadrilateral elements on a surface. To split existing quadrilaterals, the QTri command can be given a list of faces.

In addition to the default 2 tris per quad, the set qtri split command may alter the QTri scheme so that it will split the quad into 4 triangles per quad. Where the 4 option is used, an additional mesh node is placed at the centroid of each quad.

There are two methods that may be used to calculate the best diagonal to use for splitting the quadrilateral elements: angle or diagonal. The angle measurement uses the largest angle, while the diagonal option uses the shortest diagonal. The largest angle measurement will be more accurate but takes more time.

Also, the QTri scheme is used in the TriMesh command as a backup to the TriAdvance triangle meshing scheme.

Figure 1. Surface meshed with scheme QTri

---

## Quality Groups

**URL:** https://coreform.com/cubit_help/geometry/groups/quality_groups.htm

**Contents:**
- Quality Groups

Groups can also be formed from the hexes or faces obtained from the quality command. Each group formed using quality can be drawn with its associated quality characteristics {i.e. jacobian low .2 high .3} automatically.

Group {<'name'>|id} {Add|Equals|Remove|Xor} Quality { Hex | Tet | Face | Tri | Volume | Surface | Group } <id_range> { quality metric name (default is SHAPE) } [ High <value> ] [ Low <value> ] [ Top <number> ] [ Bottom <number>]

The following example illustrates the use of quality groups:

group 2 add quality volume 1 jacobian

In this case, if the meshed brick from the section Propagated Hex Groups is used, Group 2 will be created and it will contain 1000 hexes with quality characteristics.

The quality metric names can be found in the Quality Assessment section of the documentation.

---

## Radialmesh

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/free/radialmesh.htm

**Contents:**
- Radialmesh

Summary: Creates a free cylindrical mesh with precise node locations based on input radii, angles, and offsets, then creates mesh-based geometry to fit the mesh.

Create Radialmesh \ NumZ <val> [Span <val>] \ Zblock 1 [<offset val>] \ {Interval|Bias|Fraction|First Size} <val> \ [{Interval|Bias|Fraction|Last Size} <val>] \ Zblock 2 [<offset val>] \ {Interval|Bias|Fraction|First Size} <val> \ [{Interval|Bias|Fraction|Last Size} <val>] \ ... NumZ \ NumR <val> {Trisection|Initial Radius<val>} \ Rblock 1 <offset radius val> \ {Interval|Bias|Fraction|First Size} <val> \ [{Interval|Bias|Fraction|Last Size} <val>] \ Rblock 2 <offset radius val> \ {Interval|Bias|Fraction|First Size} <val> \ [{Interval|Bias|Fraction|Last Size} <val>] \ ... NumR \ NumA <val> [Full360] [Span <val>] \ Ablock 1 [<offset angle val>] \ {Interval|Bias|Fraction|First Angle} <val> \ [{Interval|Bias|Fraction|Last Angle} <val>] \ Ablock 2 [<offset angle val>] \ {Interval|Bias|Fraction|First Angle} <val> \ [{Interval|Bias|Fraction|Last Angle} <val>] \ ... NumA

The purpose of the radialmesh command is to create a cylindrical mesh with precise node locations. Unlike all other meshing commands which place nodes using smoothing algorithms to optimize element quality, node locations for the radialmesh command are calculated based on the input radii, angles, and offsets. In addition, the radialmesh command does not mesh existing geometry. Rather, it creates a mesh based on the input parameters, after which a mesh-based geometry is created to fit the free mesh.

The radialmesh command requires input for the 3 coordinate directions (Z, radial, angular). The number of blocks in each direction is specified with the numZ, numR, and numA values in the command. Each block forms a new volume in the final mesh. All bodies in the mesh are merged to form a conformal mesh between blocks.

The Radialmesh command can create meshes which span any angle greater than 0.0 up to 360 degrees. In addition, meshes can model either a tri-section (see Figure 1), or a non-trisection mesh (see Figure 2).

Figure 1. Tri-section Radialmesh

Figure 2. Non-tri-section Radialmesh

The command to generate the mesh in Figure 1 is:

create radialmesh \ numZ 1 zblock 1 1 interval 5 \ numR 3 trisection rblock 1 2 interval 5 \ rblock 2 3 interval 5 \ rblock 3 4 interval 5 \ numA 1 span 90 ablock 1 interval 10

The command to generate the mesh in Figure 2 is:

create radialmesh \ numZ 1 zblock 1 1 interval 5 \ numR 1 initial radius 3 rblock 1 4 interval 5 \ numA 1 span 90 ablock 1 interval 10

A mesh can span an entire 360 degrees by using the “full360” keyword. For example, the mesh in Figure 3 was generated with the following command:

create radialmesh numZ 1 zblock 1 1 interval 5 \ numR 3 trisection rblock 1 1 interval 5 \ rblock 2 2 interval 5 \ rblock 3 3 interval 5 \ numA 5 full360 span ablock 1 interval 5 \ ablock 2 interval 5 \ ablock 3 interval 5 \ ablock 4 interval 5

Figure 4. Radialmesh using full360 option

After the mesh is generated, the radialmesh command fits the mesh with mesh based geometry. The surfaces created to fit the mesh are given special names according to their location on the geometry. To see the names of the surfaces, issue the command label surface name after creating a radialmesh. Also, if you create a tri-section mesh, the edges on the center axis are given names. To see these names issue the command label curve name after creating a trisection Radialmesh.

The user can control the number of intervals and the spacing of these intervals using the optional parameters in each rblock, zblock and ablock. There are 11 combinations that these can be combined as listed below:

Interval Only- Example: "interval 5." The block will be meshed with 5 equally spaced intervals.

First Size Only- Example: “first size 2.5.” The block will be meshed with intervals of approximately 2.5 in length. The total number of intervals is internally calculated and depends on the overall block length.

Fraction Only- Example: “fraction 0.3333.” The block will be meshed with intervals approximately 0.3333*overall block length.

Interval and Bias- Example: “interval 5 bias 1.5.” There will be 5 intervals on the block, which each interval being 1.5 times the previous one. The length of each interval is calculated internally.

Interval and Fraction- Example: “interval 5 fraction 0.25.” There will be 5 intervals on the block, the first being .25 of the length of the block with the remaining decreasing in size.

Interval and First Size- Example: “interval 5 first size 0.2.” There will be 5 intervals on the block, the first being 0.2 in length. The remaining intervals will increase or decrease to fill the blocks length.

First Size and Last Size- Example: “first size 0.2 last size 0.4.” The first interval will be 0.2 in length. The last interval will be 0.4 in length. The total number of intervals is internally calculated to allow for transition between the 2 specified sizes.

First Size and Bias- Example “first size 0.2 bias 0.85.” The first interval will be 0.2 in length and the remaining intervals will scale by a factor of 0.85 from one to the next until the block is filled. The total number of intervals is internally calculated and depends on the overall block length.

Fraction and Bias- Example “fraction 0.25 bias 1.25.” The first interval will be 0.25 of the overall block length and the remaining intervals will scale by a factor of 1.25 from one to the next until the block is filled. The total number of intervals is internally calculated and depends on the overall block length.

Interval and Last Size- Example: “last size 1.5 interval 5.” The last interval will be 1.5 in length. The remaining intervals will scale up or down to fit 5 intervals in the block.

Last Size and Bias- Example: “last size 2.0 bias 1.1.” The last interval will be 2.0 in length. The remaining intervals will scale by 1.1 until the block is filled. The total number of intervals is internally calculated and depends on the overall block length.

Figure 5 shows an example of a bias spaced mesh with the following command:

create radialmesh numZ 2 zblock 1 1 first size 0.2 \ zblock 2 10 first size 0.2 last size 1.0 \ numR 3 trisection rblock 1 1 interval 5 \ rblock 2 2 first size .25 \ rblock 3 5 first size .25 bias 2.0 \ numA 1 span 90 ablock 1 interval 5

Figure 5. Radialmesh created with biased spacing

---

## Refine Mesh Boundary

**URL:** https://coreform.com/cubit_help/appendix/alpha/refine_mesh_boundary.htm

**Contents:**
- Refine Mesh Boundary

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

Boundary effects to be modeled in the analysis code frequently require a refined mesh near a specific surface. CUBIT provides this capability with the Refine Mesh Boundary command. This command is similar to the Refine Mesh Volume Feature command except that it can insert multiple sheets of hexes near the specified surface.

Refine Mesh Boundary Surface <range> Volume <id> {Bias <double>} {First_delta <double> | Thickness <double>} [Layer <num_layers=1>] [SMOOTH|No_smooth]

With this command num_layers of hexes can be inserted at the first interval from the specified surface. A bias factor indicating the change in element size must be specified. You must also indicate a first_delta or thickness which represents the distance to the first inserted layer. The mesh in Figure 5 with bias 1.0 and first_delta of 5. The default smooth option provides the capability to smooth the mesh following the refinement procedure.

Figure 5. Example of Boundary Surface Refinement

---

## Relative Intervals

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/relative_intervals.htm

**Contents:**
- Relative Intervals

If the user needs fine control over mesh density, then for curvy or slanted sides of swept geometries, it is often useful to treat curves as if they had a different length when setting interval sizes. For example, the user may wish to specify that a slanting side curve and a straight side curve have the same "relative" length, despite their true length as shown in the following figure. These are not interval matching constraints; interval matching may change intervals so that the user-specified ratio does not hold exactly.

The relative lengths of curves are set with the following command:

{geom_list} Relative Length <size>

The following command is used to assign intervals proportional to these lengths:

{geom_list} Relative Interval <base_interval>

For a curve with relative length x, setting a relative interval of y produces xy intervals, rounded to the nearest integer.

---

## Remeshing

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/remeshing.htm

**Contents:**
- Remeshing
  - Remeshing a Swept Volume Mesh
  - Remeshing Tetrahedra
  - Inflating a set of Tets
  - Remeshing Triangles

Mesh generation is frequently an iterative process of meshing, deleting the mesh, and remeshing. The remesh command is a convenient tool to bypass the mesh deletion process when used to remesh a volume. You may also use the remesh command to replace a localized set of deformed triangles or tetrahedra after analysis. Thus, remeshing can become part of an optimization loop.

Use the following command to remesh hexahedra:

Remesh Volume <range>

Use the following command to remesh tetrahedra:

Remesh {Volume|Block|Tet} <range> [FIXED|free]

or to remesh a range of tets or tris based upon quality criteria:

Remesh Tet <id_range> | [quality <tet_metric> [less than|greater than] <value> ...] [inflate <value>][size <value>][FIXED|free][preview]

Remesh Tri <id_range> | [quality <tri_metric> [less than|greater than] <value> ...] [inflate <value>][preview]

volume 1 scheme sweep mesh volume 1

volume 1 sweep smooth winslow remesh volume 1

When used for tetrahedra, the Remesh command generates a new tetrahedral mesh after deleting the existing mesh described by the list of tetrahedra, volumes, or blocks. When remeshing a list of tetrahedra, the smallest set of tets possible is replaced, which often means a partial remeshing of volumes, surfaces and/or curves. This set will always include the input list of tetrahedra but may include more.

Each tetrahedron may only be in one volume or block, but the list of tetrahedra may span volumes or blocks. Each block is treated individually if multiple blocks are specified.

The default FIXED option will ensure that any triangle or edge in the tetrahedron list to be remeshed that lie on geometric surfaces or curves will not be affected by the remesh operation. In contrast, the free option allows edges and triangles on curves and surfaces to be removed and remeshed. Use the FIXED option when it is important to maintain the boundary mesh configuration fixed, otherwise the free option will remesh the portions of curves and surfaces in the remesh region.

The Remesh command can be used to selectively remove and remesh a small portion of tetrahedron in the mesh that have been identified as poor quality. This can be an effective tool for improving mesh quality on a deformed mesh following an analysis without the need to regenerate the full mesh.

The quality option will identify those tetrahedra from the full model and apply the remeshing opertaion only to those tetrahedra. Any of the standard quality metrics for tetrahedra may be used as the <tet_metric>. These include: Aspect Ratio Bet, Aspect Ratio Gam, Element Volume, Condition No., Jacobian, Scaled Jacobian, Shape, Relative Size, Shape And Size, Distortion, Allmetrics, Algebraic and Traditional. The metric specification is used in conjunction with a less than or greater than specification and a threshold value. For example, the syntax below would remesh all tetrahedra in the mesh who's scaled jacobian metric was less than 0.2.

The inflate option can be used to expand the set of tets selected by the quality metric criteria. The <value> input following the inflate option is the number of tet layers surrounding the poor quality tets that will be included in the remesh region. Usually a value of 1 is sufficient to allow the tet mesher to generate better quality elements, however 2 or greater will remesh a larger portion of the mesh. A value of 0 is generally not recommended as it usually does not provide enough space for the tet mesher to improve element quality. The inflate option can also be used independently from the remesh command. See the Inflate command described below.

This command also allows for multiple quality criteria. For example, the following command would use both aspect ratio and scaled jacobian as criteria for remeshing. Any number of quality criteria may be included in the command syntax:

The preview option will display the tetrahedra selected by the quality criteria and inflate options without actually performing the remeshing operation.

Sizing functions may be used with tet remeshing. See Mesh Adaptivity and Sizing Functions and Exodus II-based Field Function for more information.

The size parameter may be used to control the size of the tets created in the remesh.

In cases where a set of tets are to be remeshed, it is useful to be able to expand the set to include additional surrounding tets. This is to allow the mesher more freedom to place good quality elements, but also to ensure a valid shape in which the mesher has to work. The Inflate command starts with a given set of tetrahedra and will expand the set based on the number of user defined layers as well as manifold criteria. The result will be added to the curent group, or a new group can be created. The following describes the syntax and arguments to this command:

Inflate {group <id>|tet <ids>} {manifold|layer <value>}[{add|create <"name">}] [draw]

group<id>|tet<range>: input to this command can be with a group name, group id, or a range of tets. The group must contain at least 1 tet. The tets need not be contiguous.

manifold: This option will add tets to the set where the boundary or skin of the tets meet at a single edge or node. This ensures that a complete valid manifold definition of the boundary of the set of tetrahedra can be defined. This is important for the tetrahedral mesh generator which requires a manifold boundary definition. both layer and manifold can be used in the same command.

layer <value>: This option will add the number of layers of tets indicated by value to the set. A layer is defined by all tets connected by at least a node to the skin of the existing set. This option alone does not guarantee a valid manifold definition. Use both the layer and manifold in the same command options to ensure a manifold definition.

add|create<"name">: The add option will add tets in the inflated region to the input group. An input group must be specified for this to be a valid option. The create option will create a new group and add all tets (including the input), to a new group specified by <"name">. If neither add nor create are specified, a new default group named "inflated_tets" will be created. If a group of that name already exists, it will be added to.

draw: The draw option will display both the input set of tets and the inflated tets in the graphics window. The input tets will be displayed in green and the inflated tets will be displayed in red.

Generate a simple tet mesh. For tets with ids 1 to 10, define a 1 layer buffer and ensure it maintains a manifold boundary. The result will be placed in a new group called "inflated_tets" and displayed in the graphics window.

brick x 10 vol 1 scheme tetmesh mesh vol 1 inflate tet 1 to 10 layer 1 draw

Create a group called "bad_tets"containing all tets in volume 1 with quality metric (scaled Jacobian) less than 0.2. Expand that group by one layer and remesh it.

group 'bad_tets' equals qual vol 1 scaled high 0.2 inflate bad_tets layer 1 add remesh tet in bad_tets

Remeshing triangles works in many of the same ways as remeshing tets, generating a new triangle mesh after deleting the existing mesh described by the list of triangles. When remeshing a list of triangles, the smallest set possible is replaced, which often means a partial remeshing of surfaces only. This set will always include the input list of triangles but may include more to ensure the set is non-manifold. Some important differences between remeshing triangles vs tets are:

---

## Removing Intersecting Mesh

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_intersection_removal.htm

**Contents:**
- Removing Intersecting Mesh

In addition to finding mesh intersection , Cubit® can also remove mesh intersection by slightly repositioning the nodes of intersecting elements. Nodes are moved along surface normals just enough so that the intersection is zero or undetectable. The command syntax is:

Remove Mesh Intersection {Block|Body|Volume} <id_list> [with {Block|Body|Volume} <id_list>] [low <value=0.0001>] [high <value>] [detail]

The low and high options set how much cumulative intersection should be detected. A low value of 0.1 would ignore elements that do not intersect more than 10% of their volume. Similarly, a high value of 0.5 would discard elements that intersect more than 50% of their volume. Both low and high can be used simultaneously. The default for the low value is 0.0001

The detail option provides information, printing the ten nodes moved the largest distances, providing users an idea of the greatest changes in the mesh.

Figure 1. "Before and after mesh intersection removal"

**Examples:**

Example 1 (unknown):
```unknown
Largest node movements:
                Node 165 moved a distance 0.003889
                Node 170 moved a distance 0.003886
                Node 1091 moved a distance 0.003861
                Node 163 moved a distance 0.003832
                Node 1100 moved a distance 0.003794
                Node 1090 moved a distance 0.003739
                Node 1101 moved a distance 0.003728
                Node 117 moved a distance 0.003701
                Node 164 moved a distance 0.003672
                Node 121 moved a distance 0.003483
```

---

## Sculpt Adaptive Meshing

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_adapt.htm

**Contents:**
- Sculpt Adaptive Meshing
- Adaptive Refinement Type
- Adaptive Refinement Threshold
- Number of Adaptive Levels
- Info for Adapt Material
- Export Refined Cartesian Grid
- Adapt Cells at Non-manifold Nodes
- Adaptive Parallel Load Balancing
- Write Memory Usage Stats for Adaptivity

Sculpt options for specifying adaptive meshing. Sculpt uses an initial overlay Cartesian grid that serves as the basis for the all-hex mesh. The default mesh size will roughly follow the constant size cells of the overlay grid. The adaptivity option allows the user to automatically split cells of the Cartesian grid based on geometric criteria, resulting in smaller cells in regions with finer details. The adapted grid is then used as the basis for the Sculpt procedure.

Three options are used for controlling the adaptivity in sculpt: adapt_type, adapt_levels and adapt_threshold. The adapt_type option controls the method and geometric criteria used for deciding which cells to split in the grid, while the adapt_levels option controls the the maximum number of times any one cell can be split. Depending upon the adapt_type selected, the adapt_threshold is used as the specific geometric threshold value at which the decision is made to split any given cell.

This option will automatically refine the mesh according to a user-defined criteria. Without this option, a constant cell size will be assumed everywhere in the model. To build the mesh, Sculpt uses an approximation to the exact geometry of the CAD model by interpolating mesh surfaces from volume fraction samples in each cell of the Cartesian grid. In general, the, higher the resolution of the Cartesian grid, the more sampling is done and the more accurate the mesh will represent the initial geometry. The adapt_type selected will control the criteria used for refining the mesh. If the criteria is not satisfied, the refinement will continue until a threshold indicated by the adapt_threshold parameter is satisfied everywhere, or the maximum number of levels (adapt_levels) is reached. The following criteria for refinement are available:

To maintain a conforming mesh, transition elements will be inserted to transition between smaller and larger element sizes. Default for the adapt_type option is off (0) (or that no adaptive refinement will take place).

In all cases the initial Cartesian grid defined by xint, yint and zint or the cell_size value will be used as the basis for refinement and will define the approximate largest element size in the mesh.

This value controls the sensitivity of of the adaptivity. The value used should be based upon the adapt_type:

surface_to_surface (3)

For these options, the adapt_type selected represents an absolute distance between surfaces or facets. Where the distance exceeds adapt_threshold the nearby cell or cells will be identified for refinement. The smaller this number the more sensitive will be the adaptation and greater the resulting number of elements. If not specified, the adapt_threshold will be determined as follows:

The adapt_threshold value in this case represents the maximum difference in volume fraction between a parent cell and the average of its eight child cells. This value should be between 0.0 and 1.0. The smaller the number, the more sensitive will be the adaptation and the greater the number of resulting elements. A default adapt_threshold of 0.01 is used if not specified.

Refinement occurs if volume fraction of material in a cell exceeds the threshold value. A separate threshold can also be set for each adapt_material overriding the the global value for threshold.

Note that the user defined adapt_threshold may not be satisfied everywhere in the mesh if the value defined for adapt_levels is exceeded.

The maximum number of levels of adaptive refinement to be performed. One level of refinement will split each Cartesian grid cell identified for uniform refinement into eight child cells. Two levels of refinement will split each cell again into eight, resulting in sixty-four child cells, three levels into 256, and so on. The maximum number of subdivision per cell is give as:

The minimum edge length for any cell will be given by:

The actual number of refinement levels used will be determined by whether all cells meet the adapt_threshold, or the adapt_levels value is exceeded. The default adapt_levels is 2. Note that setting the adapt_levels more than 4 or 5 can result in long compute times.

Specifies material information to be used with the adapt_type = material option. This option expects up to 5 ordered values representing the following:

This option may be used multiple times in the same input, once per material to be adapted.

Export an exodus mesh containing the refined Cartesian grid. Interface reconstruction, boundary layer insertion and smoothing have not yet been applied to this mesh. It is the base mesh used as input to Sculpt. One file per processor will be exported in the form "vfrac_adapt.e.x.x". The exodus mesh produced will also contain the computed volume fractions for each material present in the model represented as element variables.

This option is primarily used for debugging the refinement option. However the mesh produced with this option can be used as the base mesh when used with the input_mesh option. For example, instead of Cartesian grid options, the input mesh may be specified as input_mesh = vfrac_adapt.e.1.0. Sculpt will use the refined mesh and the volume fraction element variables to build the final mesh.

If refinement results in a non-manifold condition at a node, the surrounding cells will be identified for refinement. In some cases, using this option will result in a closer match to geometry for thin layers or small features. Using this option will normally result in more elements at material interfaces. Note that in all cases non-manifold conditions will be resolved even without this option in a subsequent step, however without this option, the resulting solution may not match geometry as accurately.

The adapt_non_manifold option is off by default. It is currently only implemented for adapt_type that use an STL geometry definition. (adapt_type = 1,2,3)

Do adaptive load balancing during refinement. Uses Zoltan's Recursive Coordinate Bisection (RCB) algorithm to repartition parallel domains following each adaptive level.

Default (OFF), refinement, will use roughly spatially equal volume domains on each processor. This can cause significant imbalance in work between processors, sometimes causing failure, especially where adpativity is localized. When using adapt_load_balance, Sculpt will repartition the parallel domains after each adaptivity level so that each processor maintains approximetly equal numbers of elements to equalize work and memory among processors.

When the adapt_type option is enabled, it allows users to monitor the memory usage and availability during the adaptivity procedures. By setting this option, both minimum and maximum memory usage for the current processor arrangement will be recorded. This information can be particularly useful when building meshes with many levels of refinement or when there are significant variations in the spatial distribution of refinement regions.

**Examples:**

Example 1 (typescript):
```typescript
Adaptive Meshing             -adp     --adapt
  --adapt_type               -A    <arg> Adaptive meshing type                                        
  --adapt_threshold          -AT   <arg> Threshold for adaptive meshing                               
  --adapt_levels             -AL   <arg> Number of levels of adaptive refinement                      
  --adapt_material           -AM   <arg> Info for adapting material                                   
  --adapt_export             -AE         Export exodus mesh of refined grid                           
  --adapt_non_manifold       -ANM        Refine at non-manifold conditions                            
  --adapt_load_balance       -ALB        Adaptive parallel load balancing                             
  --adapt_memory_stats       -AMS        Write memory usage stats for adaptivity                      

Sculpt Command Summary
```

Example 2 (lua):
```lua
Command: adapt_type     Adaptive meshing type

Input file command:   adapt_type <arg>
Command line options: -A <arg>
Argument Type:        integer (0, 1, 2,...7) 
Input arguments: off (0)
                 facet_to_surface (1)
                 surface_to_facet (2)
                 surface_to_surface (3)
                 vfrac_average (4)
                 coarsen (5)
                 vfrac_diff (6)
                 vfrac_difference (6)
                 resample (7)
                 material (8)
                 region (12)
```

Example 3 (yaml):
```yaml
Command: adapt_threshold     Threshold for adaptive meshing

Input file command:   adapt_threshold <arg>
Command line options: -AT <arg>
Argument Type:        floating point value >= 0.0
```

Example 4 (unknown):
```unknown
adapt_threshold = 0.25 * cell_size / adapt_levels^2
```

---

## Sculpt Application

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_app.htm

**Contents:**
- Sculpt Application
- Sculpt System Requirements
- Running Sculpt
- Sculpt Examples
  - Example 1
  - Example 2

This page describes the Sculpt application, a separate companion application to Cubit designed to run in parallel for generating all-hex meshes of complex geometry. Sculpt was developed as a separate application so that it can be run independently from Cubit on high performance computing platforms. It was also designed as a separable software library so it can be easily integrated as an in-situ meshing solution within other codes. As installed with Cubit, Sculpt can be set up and run directly from Cubit, in a batch process from the unix command line or from a user-defined input file. This documentation describes the input file and command line syntax for the Sculpt Application when running in batch mode. See this page for using Cubit to set up input for Sculpt. A brief technical description of Sculpt may also be found here.

Sculpt is currently built for windows, linux and mac operating systems. Current supported OS versions should be the same as those supported by Cubit. It is designed to take advantage of 64 bit multicore and distributed memory computers, using open-mpi as the basis for parallel communications.

Sculpt can be run using one of two excutables:

If appropriate system paths have not been set, you may need to use full paths when referring to mpiexec and psculpt.

The following illustrate simple use cases of the Sculpt application. To use these examples, copy the following stl and diatom files to your working directory

Runs sculpt with 4 processors with geometry input from brick1.stl. Uses a base Cartesian cell size of 0.5. The bounding box and all other parameters will be defaulted. The result should be the 4 exodus files:

These files can be combined into a single file using the SEACAS tool epu

The result of this operation should be a single file:

To view the resulting mesh in Cubit, use the import free mesh command. For example:

Figure 1. Example 1 mesh

In this case we use mpiexec to start 4 processes of psculpt. We explicitly define the number of Cartesian intervals and the dimensions of the grid. Rather than using the -stl option, we use the -d option which allows us to specify the diatom file, bricks.diatom. This file allows us to specify multiple stl files, where each one represents a different material. In this case we use both brick1.stl and brick2.stl, which are called out in bricks.diatom.

We can use similar commands as used in Example 1 to combine and import the free mesh into Cubit for display.

Figure 2. Example 2 mesh

**Examples:**

Example 1 (unknown):
```unknown
mpiexec -np 8 psculpt -stl myfile.stl -cs 0.5
```

Example 2 (unknown):
```unknown
sculpt -j 8 -stl myfile.stl -cs 0.5
```

Example 3 (unknown):
```unknown
sculpt -j 8 -mpi /path/to/mpiexec -stl myfile.stl -cs 0.5
```

Example 4 (unknown):
```unknown
brick1.stl
brick2.stl
bricks.diatom
```

---

## Sculpt Boundary Conditions

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_bcs.htm

**Contents:**
- Sculpt Boundary Conditions
- Void Material ID
- Separate Void Blocks
- Material Name
- Sideset Name
- Nodeset Name
- User Defined Sideset
- User Defined Nodeset
- Generate Sidesets
- Free Surface Sidesets

Sculpt options for specifying the methods for generating nodesets, sidesets and blocks on the mesh. Several automatic methods for generating nodesets and sidesets are provided in Sculpt using the gen_sidesets option. Where multiple blocks are required, Block IDs are normally defined using the material ID in the diatom file. Each STL file can be associated with a different block ID. If the mesh_void option is used, the ID for the block of elements in the void region can be set using the void_mat option.

For other input formats such as volume fraction microstructure data or Cartesian Exodus files, the Block IDs are defined by the individual formats.

When the mesh_void option is used, this value is the material (block) ID assigned to all elements in the void region. If void_mat option is not used, the material ID of elements in the void region will be the maximum material ID in the model + 1. Note that the void_mat may be the same as an existing material in another part of the model.

When the mesh_void option is used, the default case will generate a single block ID for all elements in the void region. Turning this option ON will separate the elements into unique block IDs where the elements are contiguous. For example, elements in a void region completely enclosed and interior to a volume will be assigned a different block ID to those exterior to the volume. The void_mat option can be used to specify the ID of the first void block. Subsequent blocks will be numbered incrementally from the first void mat ID. If void_mat is not defined, the next highest IDs not used by a material will be used for the void block IDs.

Optionally assign a name to a material. Specify a valid material ID followed by a name. This option can be used multiple times to label one or more materials. The material name will be assigned as the block name to be written to the output exodus file. A valid integer representing a material defined in the input should be used. For example, the name will be associated with the material ID identified in the diatom file for a given package. The command will be ignored if a valid matching material is not found.

Note: When using the input_mesh option and input_mesh_material = blocks, block names may be included in the input exodus mesh as part of the exodus block description. If the material_name option is used and exodus blocks names are included in the input file, the specified material name in the sculpt input will be used.

Optionally assign a name to a sideset. Specify a valid sideset ID followed by a name. This option can be used multiple times to label one or more sidesets. For example:

The assigned sideset name will be written to the output exodus file. A valid integer representing a sideset to be generated should be used. The sideset ID should refer to an existing sideset defined using gen_sidesets or sideset options.

Note: When using the input_mesh option and input_mesh_material = blocks, sideset names may be included in the input exodus mesh as part of the exodus sideset description. If the sideset_name option is used and exodus sideset names are included in the input file, the specified sideset name in the sculpt input will be used.

Optionally assign a name to a nodeset. Specify a valid nodeset ID followed by a name. This option can be used multiple times to label one or more nodesets. For example:

The assigned nodeset name be will written to the output exodus file. A valid integer representing a nodeset to be generated should be used. The nodeset ID should refer to an existing sideset defined using gen_sidesets or nodeset options.

Note: When using the input_mesh option and input_mesh_material = blocks, nodeset names may be included in the input exodus mesh as part of the exodus nodeset description. If the nodeset_name option is used and exodus nodeset names are included in the input file, the specified nodeset name in the sculpt input will be used.

Define a sideset (collection of mesh faces) based on a user-defined specification. Requires one integer representing a unique sideset ID and a character string representing a geometry specification. Current supported geometry specifications include: xmin, xmax, ymin, ymax, zmin, zmax. For a mesh defined with an axis-aligned orientation this option will place sidesets at the bounding box boundaries. For example:

Note: See also option gen_sidesets = RVE. The gen_sidesets option will automatically define sidesets at boundaries for Cartesian base meshes.

Define a nodeset (collection of nodes) based on a user-defined specification. Requires one integer representing a unique nodeset ID and a character string representing a geometry specification. Current supported geometry specifications include: xmin, xmax, ymin, ymax, zmin, zmax. For a mesh defined with an axis-aligned orientation this option will place nodesets at the bounding box boundaries. For example:

Generate exodus sidesets using one of the following options:

off (0): No sidesets will be generated

fixed (1): Exactly 3 sidesets will be generated according to the following:

variable (2): A variable number of sidesets will be generated with the following characteristics:

Unlike Fixed sidesets, grouping of sides will be contiguous. A separate sideset will be generated for each set of contiguous sides.

geometric_surfaces (3): Sidesets will be generated according to imported surface ID information. STL files may include an optional surface designation for any or all triangles in the file. Surface information may be written automatically from Cubit based on geometric surface IDs or sideset IDs. See the cubit sculpt parallel sideset option for more details. Alternatively, use the "export stl ..." command with the "sidesets" option to export all sidesets in a Cubit model as surface information. If present, one sideset will be generated for each surface designation in the STL file. Following is an example surface designation in an STL file. It would appear following all triangles.

The id following the surface designation will be used as the sideset ID. Up to 10 triangle IDs, per line may be assigned to the surface. Triangle IDs are assigned based on order they appear in the STL file. Any number of surfaces may be defined. For this option, the assumption is that all triangles included in the STL files will be included in at least one surface designation.

geometric_sidesets (4): Similar to geometric_surfaces, except that only a portion of the triangles may be designated as sideset surfaces. This option is useful when using Cubit to identify specific surfaces as sidesets.

RVE (5): When using the full bounding box, such as representative volume elements (RVE) for microstructures, the nodesets and sidesets with IDs 1 to 6 are reserved for the six faces of the bounding box. They are assigned as follows:

In addition, a nodeset and sideset will be generated on interior surfaces for each unique pair of adjacent material IDs. One final nodeset will also be generated along interior curves at all internal triple junctions (curves where at least 3 surfaces share a common curve).

input_mesh (9): Used with the input_mesh option where an exodus file is used as the base grid. Only sidesets and nodesets defined in the input exodus mesh are transferred to the output mesh.

input_mesh_and_stl (6): Used with the input_mesh option where an exodus file is used as the base grid. Sidesets and nodesets defined in the input exodus mesh are transferred to the output mesh if the surface is not an interior surface. Sidesets defined in the augmented STL input file are transferred to the output mesh for interior surfaces. See also the free_surface_sideset option for prescribing a sideset on interior surfaces cut by the STL definition when using the input_mesh option.

input_mesh_and_free_surfaces (7): Used with the input_mesh option where an exodus file is used as the base grid. Sidesets and nodesets defined in the input exodus mesh are transferred to the output mesh if the surface is not an interior surface. Sidesets defined in the free_surface_sideset option are used to define sidesets for interior surfaces.

rve_variable (8): Nodesets 1-6 and Sidesets 1-6 are defined at the boundaries as described in the gen_sidesets = rve (5) option. With the rve_variable option, additional nodesets and sidesets at material interfaces on the interior of the mesh are defined similar to the gen_sidesets = variable (2) option. Grouping of interior sides in a sidesets will be contiguous, where a separate sideset will be generated for each unique set of contiguous sides. Nodesets will be generated in a similar manner.

Given exodus sidesets are treated as interior surfaces for STL projection.

Used with the input_mesh option when using an exodus mesh as the base grid. This may be useful if the capture option is enabled and some of the STL surfaces are close in proximity to the boundaries of the input exodus mesh. When close in proximity, sculpt will by default not project those boundary nodes to the STL surface but keep them on the domain boundary. If a list of sideset IDs are given here, the sideset faces will be projected to the STL. The sideset IDs should refer to sidesets that are defined in the specified input_mesh exodus file.

If used with an unstructured base grid (input mesh), this option allows the user to define a crack in the input mesh, where the faces of each vertical side (wall) of the crack are each in a different sideset. The faces at the bottom of the crack share a common edge (V-bottom) or face (square-bottom). Sculpt will match or equalize the volume fractions of the bottom cells on either side of the crack. This produces a uniform, higher quality mesh at the crack. The sidesets must be specified in a pairwise order. This option must be used with the --input_mesh (-im) option.

If using the match_sidesets option, this option is used to explicitly define the seam between match_sideset pairs, instead of deriving it. If deriving, the seam is where sideset boundaries share common edges, at the bottom of a crack. But at times the seam can be inadvertently found along the crack wall, if the sideset have been swapped. Explicitly specifing the seam through a nodeset prevents this.

**Examples:**

Example 1 (sass):
```sass
Boundary Conditions          -bc     --boundary_condition
  --void_mat                 -VM   <arg> Void material ID (when mesh_void=true)                       
  --separate_void_blocks     -SVB        Separate void into unique block IDs                          
  --material_name            -mn   <arg> Label Material (Block) with Name                             
  --sideset_name             -sn   <arg> Label Sideset with Name                                      
  --nodeset_name             -nn   <arg> Label Nodeset with Name                                      
  --sideset                  -sid  <arg> User Defined Sideset                                         
  --nodeset                  -nid  <arg> User Defined Nodeset                                         
  --gen_sidesets             -SS   <arg> Generate sidesets                                            
  --free_surface_sideset     -FS   <arg> Free Surface Sideset                                         
  --match_sidesets           -mss  <arg> Sidesets ids of matching pairs                               
  --match_sidesets_nodeset   -msn  <arg> Nodeset defining match_sidesets                              

Sculpt Command Summary
```

Example 2 (sass):
```sass
Command: void_mat     Void material ID (when mesh_void=true)

Input file command:   void_mat <arg>
Command line options: -VM <arg>
Argument Type:        integer > 0
```

Example 3 (yaml):
```yaml
Command: separate_void_blocks     Separate void into unique block IDs

Input file command:   separate_void_blocks
Command line options: -SVB
```

Example 4 (yaml):
```yaml
Command: material_name     Label Material (Block) with Name

Input file command:   material_name <arg>
Command line options: -mn <arg>
Argument Type:        integer and string
```

---

## Sculpt Boundary Layers

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_boundary_layers.htm

**Contents:**
- Sculpt Boundary Layers
- Boundary Layer Begin
- Boundary Layer End
- Boundary Layer Material
- Number of Element Layers in Boundary Layer
- Boundary Layer Thickness
- Boundary Layer Bias

Sculpt options for defining boundary layers in the mesh. Boundary layers are thin hex layers that can be defined at surfaces, extending either inward or outward from a material. The user may specify the number and thickness of the hex layers as well as the material ID of the layers. Layer thicknesses should normally be "thin" with respect to the size of the cells. Layers will not intersect, so should be defined on surfaces where nearby layers will not overlap. Boundary layers are specified based upon a material ID, where hex layers will be placed at surfaces where the material interfaces with other materials, or at free surfaces.

Defines the beginning of a specification block. Must be closed with "end" argument. Currently supports the following specifications:

blayer Defines a boundary layer specification. Layers of hex elements are placed at the interface of a given material. Valid argumnts used within a blayer specification include: material, and begin blayer_block.

blayer_block Defines a set of element layers within a given blayer definition that share a common material ID. Valid arguments used within a blayer_block specification include: material, num_elem_layers, thickness and bias.

Example: The following example shows a boundary layer specification in a sculpt input file. In this example, two boundary layer blocks are defined at the interface of materials 1 and 2. Two material blocks with ID 3 and 4 are generated with 1 and 2 element layers respectively.

Defines the end of a specification block. Must be preceded with "begin" argument. Currently supports arguments blayer and blayer_block.

Defines a material ID in a boundary layer specification. When used within a BLAYER specification, it references one or two existing materials in the input where boundary layers will be generated. If a single material is specified, hex layers will be generated at all interfaces of the designated material with any adjacent material. If two material IDs are specified, layers will be generated only at interfaces where the two materials are adjacent.

In most cases, the material ID(s) in the BLAYER specification refer to material IDs defined in the diatom file for specific geometry inserts such as STL files or diatom primitives. It can also be defined as the void material ID (VOID_MAT) or a material in a volume fraction description such as input_vfrac, input_micro, input_cart_exo or input_spn.

When used within a BLAYER_BLOCK specification, it refers to a new block that will be generated for which all elements in the blayer_block will be assigned. Normally it refers to a unique material ID that is not already referenced in the input. Where the material ID is already used, elements in the blayer block will be added to the existing material.

A material ID must be defined for both a BLAYER and BLAYER_BLOCK. This value does not have a default.

Number of element layers to be defined within a BLAYER_BLOCK specification. num_elem_layers must be defined for all BLAYER_BLOCKs.

Thickness of the first layer defined in a BLAYER_BLOCK. Value is an absolute distance. No default is provided and must be defined for all BLAYER_BLOCKs

Bias factor applied to additional layers of a BLAYER_BLOCK. Used in conjunction with the THICKNESS parameter (thickness of first layer) it defines a multiplier for the thickness for subsequent element layers defined within the same BLAYER_BLOCK. Default BIAS is 1.0 and is optional.

**Examples:**

Example 1 (typescript):
```typescript
Boundary Layers              -bly     --boundary_layer
  --begin                    -beg  <arg> Begin specification blayer or blayer_block                   
  --end                      -zzz  <arg> End specification blayer or blayer_block                     
  --material                 -mat  <arg> Boundary layer material specification                        
  --num_elem_layers          -nel  <arg> Number of element layers in blayer block                     
  --thickness                -th   <arg> Thickness of first element layer in block                    
  --bias                     -bi   <arg> Bias of element thicknesses in blayer block                  

Sculpt Command Summary
```

Example 2 (yaml):
```yaml
Command: begin     Begin specification blayer or blayer_block

Input file command:   begin <arg>
Command line options: -beg <arg>
Argument Type:        blayer, blayer_block
```

Example 3 (julia):
```julia
BEGIN BLAYER
         MATERIAL = 1 2
         BEGIN BLAYER_BLOCK
           MATERIAL = 3
           NUM_ELEM_LAYERS = 1
           THICKNESS = 0.1
         END BLAYER_BLOCK
         BEGIN BLAYER_BLOCK
           MATERIAL = 4
           NUM_ELEM_LAYERS = 2
           THICKNESS = 0.2
           BIAS = 1.3
         END BLAYER_BLOCK
       END BLAYER
```

Example 4 (yaml):
```yaml
Command: end     End specification blayer or blayer_block

Input file command:   end <arg>
Command line options: -zzz <arg>
Argument Type:        blayer, blayer_block
```

---

## Sculpt Command Summary

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_commands.htm

**Contents:**
- Sculpt Command Summary

Following is a listing of the available input commands to either sculpt or psculpt. When used from the unix command line, commands may be issued using the short form argument, designated with a single dash(-), or with the longer form, designated with two dashes (--). When used in an input file, only the long form may be used, omitting the two dashes (--)

**Examples:**

Example 1 (sql):
```sql
Process Control              -pc     --process
  --num_procs                -j    <arg> Number of processors requested                               
  --input_file               -i    <arg> File containing user input data                              
  --debug_processor          -D    <arg> Sleep to attach to processor for debug                       
  --debug_flag               -dbf  <arg> Dump debug info based on flag                                
  --quiet                    -qt         Suppress output                                              
  --print_input              -pi         Print input values and defaults then stop                    
  --version                  -vs         Print version number and exit                                
  --threads_process          -tpp  <arg> Number of threads per process                                
  --iproc                    -ip   <arg> Number of processors in I direction                          
  --jproc                    -jp   <arg> Number of processors in J direction                          
  --kproc                    -kp   <arg> Number of processors in K direction                          
  --build_ghosts             -bg         Write ghost layers to exodus files for debug                 
  --vfrac_method             -vm   <arg> Set method for computing volume fractions                    

Input Data Files             -inp     --input
  --stl_file                 -stl  <arg> Input STL file                                               
  --diatom_file              -d    <arg> Input Diatom description file                                
  --input_vfrac              -ivf  <arg> Input from Volume Fraction file base name                    
  --input_micro              -ims  <arg> Input from Microstructure file                               
  --input_cart_exo           -ice  <arg> Input from Cartesian Exodus file                             
  --input_spn                -isp  <arg> Input from Microstructure spn file                           
  --spn_xyz_order            -spo  <arg> Ordering of cells in spn file                                
  --compress_spn_ids         -csp  <arg> Compress IDs from SPN file                                   
  --input_stitch             -ist  <arg> Input from Stitch file                                       
  --stitch_timestep          -stt  <arg> Timestep in Stitch file to read                              
  --stitch_timestep_id       -stn  <arg> Timestep ID in Stitch file to read                           
  --stitch_field             -stf  <arg> Field in Stitch file to read                                 
  --stitch_info              -sti        List header info for Stitch file                             
  --lattice                  -l    <arg> STL Lattice Template File                                    

Output                       -out     --output
  --exodus_file              -e    <arg> Output Exodus file base name                                 
  --large_exodus             -le   <arg> Output large Exodus file(s)                                  
  --volfrac_file             -vf   <arg> Output Volume Fraction file base name                        
  --quality                  -Q    <arg> Dump quality metrics to file                                 
  --export_comm_maps         -C          Export parallel comm maps to debug exo files                 
  --write_geom               -G          Write geometry associativity file                            
  --write_mbg                -M          Write mesh based geometry file <beta>                  
  --compare_volume           -cv         Report vfrac and mesh volume comparison                      
  --compute_ss_stats         -css        Report sideset statistics                                    

Overlay Grid Specification   -ovr     --overlay
  --nelx                     -x    <arg> Num cells in X in overlay Cartesian grid                     
  --nely                     -y    <arg> Num cells in Y in overlay Cartesian grid                     
  --nelz                     -z    <arg> Num cells in Z in overlay Cartesian grid                     
  --xmin                     -t    <arg> Min X coord of overlay Cartesian grid                        
  --ymin                     -u    <arg> Min Y coord of overlay Cartesian grid                        
  --zmin                     -v    <arg> Min Z coord of overlay Cartesian grid                        
  --xmax                     -q    <arg> Max X coord of overlay Cartesian grid                        
  --ymax                     -r    <arg> Max Y coord of overlay Cartesian grid                        
  --zmax                     -s    <arg> Max Z coord of overlay Cartesian grid                        
  --cell_size                -cs   <arg> Cell size (nelx, nely, nelz ignored)                         
  --align                    -a          Automatically align geometry to grid                         
  --bbox_expand              -be   <arg> Expand tight bbox by percent                                 
  --input_mesh               -im   <arg> Input Base Exodus mesh                                       
  --input_mesh_blocks        -imb  <arg> Block ids of Input Base Exodus mesh                          
  --input_mesh_material      -imm  <arg> Material definition with input mesh                          
  --input_mesh_pamgen        -imp  <arg> Input Base mesh defined by Pamgen                            
  --join_parallel            -jp   <arg> Join parallel files                                          

Mesh Type                    -typ     --type
  --stair                    -str  <arg> Generate Stair-step mesh                                     
  --mesh_void                -V    <arg> Mesh void                                                    
  --trimesh                  -tri        Generate tri mesh of geometry surfaces                       
  --tetmesh                  -tet  <arg> Under Development                                            
  --deg_threshold            -dg   <arg> Convert hexes below threshold to degenerates                 
  --max_deg_iters            -dgi  <arg> Maximum number of degenerate iterations                      
  --htet                     -ht   <arg> Convert hexes below quality threshold to tets                
  --htet_method              -hti  <arg> Method used for splitting hexes to tets                      
  --htet_material            -htm  <arg> Convert hexes in given materials to tets                     
  --htet_transition          -htt  <arg> Transition method between hexes and tets                     
  --htet_pyramid             -htp  <arg> Local transition pyramid                                     
  --htet_tied_contact        -htc  <arg> Local transition tied contact                                
  --htet_no_interface        -htn  <arg> Local transition none                                        
  --periodic                 -per        Generate periodic mesh                                       
  --check_periodic           -cp   <arg> Check for periodic geometry                                  
  --check_periodic_tol       -cpt  <arg> Tolerance for checking periodicity                           
  --periodic_axis            -pax  <arg> Axis periodicity is about                                    
  --periodic_nodesets        -pns  <arg> Nodesets ids of primary/secondary (leading/trailing) nodesets

Boundary Conditions          -bc     --boundary_condition
  --void_mat                 -VM   <arg> Void material ID (when mesh_void=true)                       
  --separate_void_blocks     -SVB        Separate void into unique block IDs                          
  --material_name            -mn   <arg> Label Material (Block) with Name                             
  --sideset_name             -sn   <arg> Label Sideset with Name                                      
  --nodeset_name             -nn   <arg> Label Nodeset with Name                                      
  --sideset                  -sid  <arg> User Defined Sideset                                         
  --nodeset                  -nid  <arg> User Defined Nodeset                                         
  --gen_sidesets             -SS   <arg> Generate sidesets                                            
  --free_surface_sideset     -FS   <arg> Free Surface Sideset                                         
  --match_sidesets           -mss  <arg> Sidesets ids of matching pairs                               
  --match_sidesets_nodeset   -msn  <arg> Nodeset defining match_sidesets                              

Adaptive Meshing             -adp     --adapt
  --adapt_type               -A    <arg> Adaptive meshing type                                        
  --adapt_threshold          -AT   <arg> Threshold for adaptive meshing                               
  --adapt_levels             -AL   <arg> Number of levels of adaptive refinement                      
  --adapt_material           -AM   <arg> Info for adapting material                                   
  --adapt_export             -AE         Export exodus mesh of refined grid                           
  --adapt_non_manifold       -ANM        Refine at non-manifold conditions                            
  --adapt_load_balance       -ALB        Adaptive parallel load balancing                             
  --adapt_memory_stats       -AMS        Write memory usage stats for adaptivity                      

Smoothing                    -smo     --smoothing
  --smooth                   -S    <arg> Smoothing method                                             
  --csmooth                  -CS   <arg> Curve smoothing method                                       
  --laplacian_iters          -LI   <arg> Number of Laplacian smoothing iterations                     
  --max_opt_iters            -OI   <arg> Max. number of parallel Jacobi opt. iters.                   
  --opt_threshold            -OT   <arg> Stopping criteria for Jacobi opt. smoothing                  
  --curve_opt_thresh         -COT  <arg> Min metric at which curves won't be honored                  
  --max_pcol_iters           -CI   <arg> Max. number of parallel coloring smooth iters.               
  --pcol_threshold           -CT   <arg> Stopping criteria for parallel color smooth                  
  --max_gq_iters             -GQI  <arg> Max. number of guaranteed quality smooth iters.              
  --gq_threshold             -GQT  <arg> Guaranteed quality minimum SJ threshold                      
  --geo_smooth_max_deviation -GSM  <arg> Geo Smoothing Maximum Deviation                              

Mesh Improvement             -imp     --improve
  --pillow                   -p    <arg> Set pillow criteria (1=surfaces)                             
  --pillow_surfaces          -ps         Turn on pillowing for all surfaces                           
  --pillow_curves            -pcv        Turn on pillowing for bad quality at curves                  
  --pillow_boundaries        -pb         Turn on pillowing at domain boundaries                       
  --pillow_curve_layers      -pcl  <arg> Number of elements to buffer at curves                       
  --pillow_curve_thresh      -pct  <arg> S.J. threshold to pillow hexes at curves                     
  --pillow_smooth_off        -pso        Turn off smoothing following pillow operations               
  --capture                  -c    <arg> Project to facet geometry <beta>                       
  --capture_angle            -ca   <arg> Angle at which to split surfaces <beta>                
  --capture_side             -sc   <arg> Project to facet geometry with surface ID                    
  --defeature                -df   <arg> Apply automatic defeaturing                                  
  --min_vol_cells            -mvs  <arg> Minimum number of cells in a volume                          
  --defeature_bbox           -dbb        Defeature Filtering at Bounding Box                          
  --defeature_iters          -dfi  <arg> Maximum Number of Defeaturing Iterations                     
  --thicken_material         -thm  <arg> Expand a given material into surrounding cells               
  --thicken_void             -thv  <arg> Insert void material to remove overlap                       
  --micro_expand             -me   <arg> Expand Microstructure grid by N layers                       
  --micro_shave              -ms         Remove isolated cells at micro. boundaries                   
  --remove_bad               -rb   <arg> Remove hexes with Scaled Jacobian < threshold             
  --wear_method              -wm   <arg> Method for removing void at free surface                     
  --crack_min_elem_thickness -cmet <arg> Minimum element thickness in crack                           
  --min_num_layers           -mnl  <arg> Minimum number of layers to keep using wear_method=2         

Mesh Transformation          -tfm     --transform
  --xtranslate               -xtr  <arg> Translate final mesh coordinates in X                        
  --ytranslate               -ytr  <arg> Translate final mesh coordinates in Y                        
  --ztranslate               -ztr  <arg> Translate final mesh coordinates in Z                        
  --xscale                   -xsc  <arg> Scale final mesh coordinates in X                            
  --yscale                   -ysc  <arg> Scale final mesh coordinates in Y                            
  --zscale                   -zsc  <arg> Scale final mesh coordinates in Z                            

Boundary Layers              -bly     --boundary_layer
  --begin                    -beg  <arg> Begin specification blayer or blayer_block                   
  --end                      -zzz  <arg> End specification blayer or blayer_block                     
  --material                 -mat  <arg> Boundary layer material specification                        
  --num_elem_layers          -nel  <arg> Number of element layers in blayer block                     
  --thickness                -th   <arg> Thickness of first element layer in block                    
  --bias                     -bi   <arg> Bias of element thicknesses in blayer block
```

---

## Sculpt

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt.htm

**Contents:**
- Sculpt
- Preparing to Use Sculpt
  - Platforms
  - Sculpt Installation
  - Setting your Working Directory
- Sculpt Command
- Controlling the Execution of Sculpt in Cubit
- Sculpt Help Command
- Sculpt Path Command
- Sculpt Mesh Quality Control

Sculpt is a separate parallel application designed to generate all-hex meshes on complex geometries with little or no user interaction. Sculpt was developed as a separate application so that it can be run independently from Cubit on high performance computing platforms. It was also designed as a separable software library so it can be easily integrated as an in-situ meshing solution within other codes. Cubit provides a front end command line and GUI for the Sculpt application. The command will build the appropriate input files based on the current geometry and can also automatically invoke Sculpt to generate the mesh and bring the mesh back to Cubit.

Sculpt is a stand-alone executable, separate from Cubit. In order for Cubit to start up Sculpt, it must be on your system and accessible to Cubit. The default installation of Cubit should install files in the correct locations for this to occur. Check with Cubit support if it did not come with your installation or you are not able to locate it or any of its supporting applications.

To run Sculpt from Cubit, four executable files are needed:

To view the current path to these executables that Cubit will use, issue the following command from the Cubit command window

See the Sculpt Path Command for more info on setting and customizing these paths.

The following image illustrates the process flow when the sculpt command is used in Cubit.

For the Sculpt meshing process, a set of files, including a facet-based stl file are written to disk. The sculpt application is then started up which in turn invokes mpiexec to start up multiple instances of psculpt in parallel. psculpt then performs the meshing and writes one exodus file per processor. These files can then be combined using epu and then imported back into Cubit for viewing.

When using the Sculpt command in Cubit, several temporary files will be written to the current working directory. Because of this, it is important to set your working directory before using Sculpt to a desired location where you want these files placed.

The Sculpt Command in Cubit invokes the sculpt application. You can designate the target geometry, which can be existing volumes or blocks within the current Cubit run or imported from external files (e.g., STL, diatom, or microstructure files). The command syntax for preparing a model for Sculpt is as follows:

{[volume <ids>] [block <ids>] [stl_file "<filename.stl>"] [diatom_file "<filename.diatom>"] [input_vfrac "<filename.e>"] [input_micro "<filename.tec>"] [input_cart_exo "<filename.e>"] [input_spn "<filename.spn>"]}

[spn_xyz_order "<0,1,..5>"] [input_stitch "<filename.st>"] [stitch_field "<field_name>"] [stitch_timestep {<timestep_value>|first|last}] [stitch_timestep_id <timestep_ID>] [stitch_info]

[processors <value>] [fileroot "<rootfilename>"] [{OVERWRITE|no_overwrite}] [absolute_path] [{EXECUTE|no_execute}] [{COMBINE|no_combine}] [{IMPORT [unique_genesis_ids]|no_import}] [{SHOW|no_show}] [{CLEAN|no_clean}] [{gen_input_file <string>|no_gen_input_file}] [{debug <value>] [quiet] [preview]

[{size <value>|autosize <value>}] [box {align|location <options>|expand <value>}] [{xintervals|nelx} <value> {yintervals|nely} <value> {zintervals|nelz} <value>] [input_mesh "<filename.g>"] [input_mesh_material <value>] [input_mesh_pamgen "<filename.pam>"]

[void <value>] [void_block <value>] [separate_void_blocks] [stair <value>] [htet <value>] [htet_material <value>] [htet_method <value>] [periodic <value>]

[smooth <value>] [csmooth <value>] [num_laplace <value>] [max_opt_iters <value>] [opt_threshold <value>] [curve_opt_thresh <value>] [max_pcol_iters <value>] [pcol_threshold <value>] [max_gq_iters <value>] [gq_threshold <value>] [max_deg_iters <value>] [deg_threshold <value>] [geo_smooth_max_deviation <value>]

[pillow <value>] [pillow_surfaces] [pillow_curves] [pillow_curve_layers <value>] [pillow_curve_thresh <value>] [pillow_boundaries] [pillow_smooth_off] [defeature <value>] [min_vol_cells <value>] [defeature_bbox] [defeature_iters <value>] [capture <value>] [capture_angle <value>] [capture_side <value>] [thicken_material <value>...] [thicken_void <value>] [remove_bad <value>] [wear_method <value>] [crack_min_elem_thickness <value>] [temp_use_sipe_depth <value>] [min_num_layers <value>]

[adapt_type <value>] [adapt_threshold <value>] [adapt_levels <value>] [adapt_material <value>...] [adapt_export] [adapt_non_manifold] [adapt_load_balance]

Boundary Condition Options

[gen_sidesets <value>] [material_name <value>... <string>...] [sideset_name <value>... <string>...] [nodeset_name <value>... <string>...] [sideset_definition <value>... <string>...] [nodeset_definition <value>... <string>...] [free_surface_sideset <value>...] [match_sidesets <value>...] [match_ss_nodeset <value>...]

[exodus <string>] [large_exodus] [xtranslate <value>] [ytranslate <value>] [ztranslate <value>] [xscale <value>] [yscale <value>] [zscale <value>] [volfrac_file <string>] [quality <string>] [write_geom] [write_mbg] [compare_volume] [compute_ss_stats]

volume <ids> | block <ids>

List of volumes or blocks to include in the mesh. One file containing a faceted representation (STL) per volume will be generated and saved in the current working directory to be used as input to Sculpt. Each volume will be treated as a separate material within sculpt and a conforming mesh will be generated where volumes touch. If the Block command is used, one file per block will be used. Each block represents a separate material in Sculpt.

fileroot '<root filename>'

Root of file names for output. When the sculpt command is executed, Cubit will generate multiple files in the working directory used for input to the Sculpt application. The '<root filename>' will be used as the basis for naming these files.

Specify the number of processors that MPI will use to execute the Sculpt application. If not specified, the maximum number of available processors on the local machine will be used up to a maximum of 16.

OVERWRITE | no_overwrite

By default, Cubit will overwrite an existing set of files with the same '<root filename>'. To over-ride, use the no_overwrite option.

By default, Cubit will write the relative path names of files used in the .run and .diatom files. To force absolute path names to be written, use the absolute_path option

By default, Cubit will attempt to run sculpt in parallel on the machine Cubit is currently running on. To generate just the required input to run Sculpt at a later time or on another machine, use this option. A file of the form <root filename>.run will be generated in the current working directory. (for example "model.run"). Executing the .run file from the linux command line should run sculpt in parallel. It can also be used to run sculpt on a cluster where a Cubit executable may not be available.

size <value> | autosize <value>

autosizesizeThe option is the absolute cell size for the Cartesian grid and is the same as the cell_size option in sculpt. The option is a value between 0 and 10. It represents a model independent size where 1 is the small size and 10 is large. This is the same scaling factor used in Cubit's auto sizing but is divided by ten. A size value will be computed from the selected autosize and used as the absolute cell size for the base Cartesian grid.

box location <options>

Note that the xmin, ymin, zmin, xmax, ymax, zmax options can also be used for specifying the bounds of the Cartesian grid from the command line.

If the no_combine option is used, following execution of Sculpt, the resulting exodus meshes will not be combined using the epu seacas tool. Otherwise the default will automatically combine the meshes generated by each processor into a single mesh. Note that epu should be installed on your system and the path to epu defined using the sculpt path command. Epu is a code developed by Sandia National Laboratories and is part of the SEACAS tool suite. It combines multiple Exodus databases produced by a parallel application into a single Exodus database. The epu program should be included with distributions of Cubit beginning with Version 15.0.

no_importIf the option is used, following execution of Sculpt, the result will be not be imported into Cubit as a free mesh. The default IMPORT option will automatically import the mesh that was generated in Sculpt. If the no_combine option has been used, then multiple free meshes will be imported with duplicate nodes and faces at processor domain boundaries. Otherwise a single free mesh, the result of the epu code, will be imported. Note that the resulting mesh will not be associated with the original geometry, however Block (material) definitions will be maintained. In addition, a separate group will be generated for each imported mesh (One per processor). The default will automatically import the mesh following mesh generation in Sculpt.

If the no_show option is used, while the external Sculpt process is running, no ouput from the Sculpt application will be displayed to the command window. Otherwise, the default SHOW is used and output from the Sculpt application will be echoed to the Cubit command window. This option is only effective if the no_execute is not used.

no_cleanCLEANsculptcleanIf the option is used, temporary files generated during the command will be deleted. This includes any exodus mesh files, .stl, .diatom, .log and .run files. The default for this option is , therefore, use the option to keep any temporary files generated as part of the current Sculpt run.

gen_input_file <file name> | no_gen_input_file

An input file with the given file name will be generated when the command is executed. This is a text file containing all sculpt options used in the command. The input file is intended to be used for batch execution of sculpt. To run sculpt from the operating system command line you would use the -i option. For example: sculpt -i myinputfile.i -j 4 where myinputfile.i is the name of the input file specified with the gen_input_file option and -j 4 is the number of processors to use.

debug <value> The debug option is used only as a developer debugging tool. It will set the debug processor and sleep upon execution to allow a debugger to be attached to the process.

The quiet option used as an option in the sculpt command will suppress output from the sculpt application to the Cubit output window.

When used with the sculpt command, the preview option will print the contents of the sculpt input file to the Cubit output window, based on the currently defined options in the sculpt command. It will not execute sculpt.

Help about any of the Sculpt options can be printed to the output window using the following command:

Sculpt [parallel] print_help [<"sculpt_option">]

where <"sculpt_option"> is any valid sculpt application option listed above.

The command for letting Cubit know where the Sculpt and related applications are located is:

Sculpt [Parallel] Path [List|Psculpt|Epu|Mpiexec]

In most cases, the Sculpt tool can be used without adjusting default values. Depending on the characteristics of the geometry to be meshed, the default values may not yield adequate mesh quality. Upon completion, Sculpt reports to the command line, a summary of the mesh that was generated. This includes a summary of the mesh quality. Care should be taken to review this summary to ensure the minimum mesh quality is in a range suitable for analysis.

The element metric used for computing mesh quality in Sculpt is the Scaled Jacobian. This is a value between -1 and 1 that is a relative measure of the angles at the element's nodes. A value of 1 indicates a perfect 90 degree angle between each of its edges. In most cases a value less than zero, or negtive Jacobian element, indicates an unusable mesh. Sculpt's default settings try to achieve a minimum Scaled Jacobian of 0.2, which is normally usable in most analysis. The following discussion provides several options for adjusting the model or Sculpt parameters to help improve mesh quality.

quality hex all scaled jacobian quality hex all draw mesh

The following examples use this simple geometry. Execute these commands prior to performing the example Sculpt command line operations

sphere rad 1 sphere rad 1 vol 2 mov x 2 cylinder rad 1 height 2 vol 3 rota 90 about y vol 3 mov x 1 unite vol all

Figure 1. Geometry created from the above commands and used for the following examples.

This example illustrates use of Sculpt with all default options. So that we can view the result, we will also use the overwrite, combine and import options.

sculpt volume 1 draw block all

The result of this operation is shown in Figure 2. For this example, behind the scenes, Cubit built an input file for Sculpt, ran it on 4 processors, combined the resulting 4 meshes, and subsequently imported the resulting mesh into Cubit. Note that Volume 1 remains "unmeshed" and we have created a free mesh that is not associated with a volume. The result of any Sculpt command is always an unassociated free mesh.

Figure 2. Free mesh generated from sculpt command

This example illustrates the use of the size and box options

delete mesh sculpt volume 1 size 0.1 box location position -1.5 0 -1.5 location position 1 1.5 0 draw block all

In this case we have used the size option to define the base cell size for the grid. We have also used the box option to define a bounding box in which the mesh will be generated. Any geometry falling outside of the bounding box is ignored by Sculpt. Figure 3 shows the mesh generated with this command.

Figure 3. Sculpt "box" option limits the extent of the generated mesh.

In this example we illustrate the use of the void option:

delete mesh sculpt volume 1 size 0.1 box location position -1.5 0 -1.5 location position 1 1.5 0 void 1 draw block all

The result is shown in figure 4. Notice that this example is precisely the same as the last with the exception of the addition of the void option. Mesh is generated in the space surrounding the volume out to the extent of the bounding box. In this case, an additional material block is defined and automatically assigned an ID of 2. The nodes and element faces at the interface between the two blocks are shared between the two materials.

Figure 4. Sculpt "void" operation generates mesh outside the volume.

In this example we illustrate the use of the gen_sidesets option.

Generating sidesets on the free mesh with Cubit: Sideset boundary conditions can be manually created on the resulting free mesh from Sculpt using the standard Sideset <sideset_id> Face <id_range> syntax. The Group Seed command is also useful in grouping faces based on a feature angle to be used in a single sideset.

Generating sidesets in Sculpt: Sculpt also provides several options for defining sidesets as part of the Sculpt run. The following illustrates one option:

delete mesh sculpt volume 1 size 0.1 box location position -1.5 0 -1.5 location position 1 1.5 0 void 1 gen_sidesets 2 list sideset all draw sideset all

Once again we use the same syntax but add the gen_sidesets 2 option to automatically generate a series of sidesets. The list command should reveal that 10 sidesets were defined for this example with IDs 1 to 10. Figure 5 shows the result of the draw command showing all of the sidesets in different colors. Note that for the gen_sidesets 2 option, sidesets are created with the following criteria:

See the gen_sidesets option above for a description of other options for generating sidesets in Sculpt.

Figure 5. Automatic sidesets created using Sculpt

Begin by setting your working directory to a location that is convenient for placing example files

cd "path/to/my/sculpt/examples"

Next we issue the basic sculpt command to mesh the volume

delete mesh sculpt volume 1 processors 8 fileroot "bean" over no_execute no_clean

In this case, we used the no_execute option which does not invoke the Sculpt application. Instead it will write a series of files to the working directory. The fileroot option defines the base file name for the files that will be written; in this case "bean". We also use the processors option to set the number of processors to be used to 8. Finally, since the default clean option will remove temporary files after execution of sculpt, we use the no_clean option to ensure they will persist.

To see the files that Cubit placed in the working directory, bring up a terminal window on your desktop and change directories to the current working directory (ie. cd path/to/my/sculpt/examples). A directory listing should reveal 3 files as shown in Figure 6.

Figure 6. Directory listing of files written from Cubit

The following describes the purpose of each of the resulting files:

Figure 7. Unix command line for running Sculpt generated by Cubit

To run sculpt on the same machine, from the terminal window in your current working directory you would issue the following command:

If Sculpt is to be run on a different machine, copy the files in the working directory to the other machine and issue the same command. Remember to change the path to the mpiexec and psculpt executables to match those on the new machine. For running on cluster machines that have scheduling of resources, check with your system administrator for how to submit a job for running.

After running Sculpt, Figure 8 shows the resulting files that would be written to the current working directory.

Figure 8. 8 Exodus files were generated and placed in working directory

Note that 8 exodus files have been generated, 1 from each processor. These files can be used by themselves or used as-is for use in a simlation, or they can be combined into a single file. The exodus files produced by Sculpt include all appropriate parallel communication information as defined by the Nemesis format. Nemesis is an extension of Sandia's Exodus II format that also includes appropriate parallel communication information.

To combine the resulting exodus files into a single file, we can use the epu tool. Epu should be included in your Cubit distribution, but may require you to set up appropriate paths for it to be recognized. To run epu on this model, use the following command from a unix terminal window:

epu -p 8 bean.diatom_result

The result should be a single file with the name bean.diatom_result.e. The mesh in this file can then be imported into Cubit. Switch back to your Cubit application and from the command line type the following command:

import mesh "bean.diatom_result.e" no_geom

The result should be the same mesh we generated previously that is shown in Figure 2.

delete mesh cylinder rad 0.5 height 3 cylinder rad 0.5 height 3 vol 5 mov x 2

The resulting geometry should look like the image in Figure 9.

Figure 9. Geometry used to demonstrate multiple materials with Sculpt

Use this geometry to generate a mesh using Sculpt.

sculpt volume all size 0.075 draw block all

The resulting mesh should look like the image in Figure 10.

Figure 10. Mesh generated on multiple materials

Notice that one mesh block per volume was created. We should also note that no boolean operations were performed prior to building the mesh with Sculpt. In fact, volumes 4 and 5 were significantly overlapping volume 1. This would be an invalid condition for normal Cubit meshing operations. Figure 11 shows a cut-away image of the mesh using the Clipping Plane tool.

Figure 11. Cut-away of mesh generated on multiple materials

We should also note that imprint/merge operations typically needed, were also not required. While it is usually best to avoid overlaps to avoid ambiguities in the topology, Sculpt is able to generate a mesh giving precedence to the most recently defined materials. Merging is performed strictly by geometric proximity. Volumes closer than about one half the user input size will normally be automatically merged.

Next, we will examine the mesh quality of the free mesh. The following command will display a graphical representation of the Scaled Jacobian metric.

quality hex all scaled jacobian draw mesh

The result is shown in Figure 12. Note the elements (colored red) at the interface between materials are unacceptable for simulation. This is caused by the Sculpt algorithm projecting nodes to a common curve interface shared by the materials.

Figure 12. Mesh quality of multi-material mesh.

In most cases, the poor element quality at material interfaces can be improved by using the pillow option. Adding this option will direct Sculpt to add an additional layer of elements surrounding each surface. To see the result of pillowing, issue the following commands:

delete mesh sculpt volume all size 0.075 over combine import pillow 1 quality hex all scaled jacobian draw mesh

Figure 13. Mesh quality of multi-material mesh using pillow option

The resulting mesh is showed in Figure 13. Note the improved mesh quality at the shared curve interface. A closer look at the mesh, shown in Figure 14. reveals the additional layer of hexes surrounding each surface that allows for improved mesh quality when compared with Figure 11. When generating meshes with multiple materials that must share common interfaces, the pillow option is usually recommended.

Figure 14. Cutaway of mesh reveals the additional layer of hexes surrounding each surface when the pillow option is used.

---

## Sculpt Input Data Files

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_input.htm

**Contents:**
- Sculpt Input Data Files
- STL File
- Diatom File
- Input Volume Fraction File
- Input Microstructure File
- Input Cartesian Exodus File
- Input Microstructure SPN File
- XYZ ordering of cells in SPN File
- Compress IDs in SPN file
- Input Stitch File

Options for specifying input files to Sculpt. Sculpt uses a method for representing geometry based upon volume fractions defined on a Cartesian or unstructured grid. Sculpt will accept facet-based (STL) or analytic (diatom) geometry, but will first convert the input geometry to the required volume fraction description before generating the hexahedral mesh. Various formats for volume fraction data can also be imported directly into Sculpt and used as the basis for hex meshing. The following formats for geometry are currently supported in Sculpt:

File name of a single STL (facet geometry) file to be used as input. Either an stl_file or diatom_file designation should be included to run Sculpt. The stl_file option will support a single STL file. To use multiple STL files, where each file represents a different material, use the diatom_file file option where multiple file names may be specified.

It is recommended that STL files used as input to Sculpt be "water-tight". While in many cases non-watertight geometries will be successful, unexpected or incorrect results may result. It is recommended practice to use Cubit to first import the STL geometry and allow the sculpt parallel command to write a new STL geometry file for use in Sculpt. Cubit's sculpt parallel command will attempt to stitch and repair any triangle facets that are not completely closed. Other commercial tools are available for STL geometry that may be effective in repairing the geometry prior to use in Sculpt.

File name of a diatom file to be used as input to Sculpt. Both stl_file and diatom_file cannot be used simultaneously. A diatom file is a constructive solid geometry description containing primitives for generating a full geometric definition of the model. Diatoms are commonly used as input to Sandia's CTH and Alegra codes. Multiple STL files can also be defined in a Diatom file. The following is a simple example of a diatom file that would read 3 different STL files:

Note that the first two files, blue_part1.stl and blue_part2.stl belong to the same material. As a result, elements generated within the geometry of these files will belong to block 1. Likewise, the elements generated within the geometry of red_part1.stl will belong to block 2.

The Diatom format will also support bitmap files. These are binary files that set each cell either on or off for the specified material. The following is an example diatom specification for a bitmap file. Note that the bitmap specification includes nx, ny, nz dimensions for the size of the input file.

For a full description of the diatom format see the CTH or Alegra documentation.

D. A. Crawford, A. L. Brundage, E. N. Harstad, K. Ruggirello, R. G. Schmitt, S. C. Schumacher and J. S. Simmons, "CTH User’s Manual and Input Instructions, Version 10.3", CTH Development Project, Sandia National Laboratories, Albuquerque, New Mexico 87185, February 14, 2013

Sculpt can optionally take an exodus file containing volume fraction data stored as element variables. Normally the exodus file has initially been written using the --volfrac_file (-vf) option. Since the exodus file will be a Cartesian grid spread across multiple processors, the base filename for the parallel series of exodus files is used as the argument for this command. The input volume fraction file(s) would be used instead of an STL or diatom file. Since computing volume fractions from geometry can be time consuming, precomputing the volume fractions and reading them from a file can be advantageous if multiple meshes are to be generated from the same volume fraction data.

A microstructure file is an ascii text file containing volume fraction data for each cell of a Cartesian grid. The format for this file includes header information followed by data for each cell. The following is an example:

The header information should contain the following:

TITLE: any descriptive character string

VARIABLES: a list of variables separated by spaces or commas. It should include x, y, z as the first three variable names. The remaining names are arbitrary. The number of variable names listed must correspond to the number of data values for each cell of the Cartesian grid.

ZONE: Specify the number of cells in the i, j and k directions (corresponding to x, y, and z respectively)

The body of the file will contain one line per cell of the grid. The first three values correspond to the centroid location of a cell in the grid. The remaining values represent volume fractions for the cell for each variable listed. The sum of the volume fractions for each individual cell should be 1.0

Currently this format assumes that cell sizes are exactly 1.0 x 1.0 x 1.0 and the minimum cell centroid location is always 0.0, 0.0, 0.0. This results in a Cartesian grid with minimum coordinate = (-0.5, -0.5, -0.5) and maximum coordinate = (i-0.5, j-0.5, k-0.5). If a size other than 1x1x1 is required consider using the scale and/or translate options.

Example usage of this command is as follows:

Smoothing: Sculpt will set automatic defaults for smoothing if user options have not been defined. These include:

These options will generally provide a smoother curve and surface representation but may not adhere strictly to the volume fraction geometric definition. To over-ride the defaults, consider using the following options:

Pillowing: For most 3D models it is recommended using pillowing since triple junctions (curves with at least 3 adjacent materials) will typically be defined where malformed hex elements would otherwise be generated. Surface pillowing (option 1) is usually sufficient to remove poor quality elements at triple junctions.

An exodus mesh containing a Cartesian grid of elements can also be used as the source of a sculpt mesh. For this option the following conditions must be met:

Provided these conditions are met, sculpt will treat each block as a separate material and generate a smooth conforming mesh between the materials. This option is useful for converting a stair-step mesh into a smooth conforming mesh. The resulting sculpt mesh will have the same dimensions as the original exodus mesh, but will add layers of hexes at material interfaces.

Example usage of this command is as follows:

Smoothing: Sculpt will set automatic defaults for smoothing if user options have not been defined. These include

These options will generally provide a smoother curve and surface representation but may not adhere strictly to the volume fraction geometric definition. To over-ride the defaults, consider using the following options:

Pillowing: For most 3D models it is recommended using pillowing since triple junctions (curves with at least 3 adjacent materials) will typically be defined where malformed hex elements would otherwise be generated. Surface pillowing (option 1) is usually sufficient to remove poor quality elements at triple junctions.

A .spn file is an optional method for importing volume fraction data into sculpt for meshing. This format is a simple ascii text file containing one integer per cell of a Cartesian grid. Each integer represents a unique material identifier. Any number of materials may be used, however for practical purposes, the number of unique materials should not exceed more than about 50 for reasonable performance.

An example file containing a 3 x 3 x 3 grid with 2 materials may be defined as follows:

Any unique integer may be used to identify a material. All cells with the same ID will be defined as a continuous block with the same exodus block ID in the final mesh. All integers should be separated by a space or newline. The number of integers in the file should exactly correspond to the size of the Cartesian grid. The dimensions of the Cartesian grid must be specified on the command line as part of the input. The following is an example:

The default order of the cells in the input file will be read according to the following schema:

Where nx, ny, nz are the number of cells in each Cartesian direction. This ordering can be changed to nz, ny, nx using the spn_xyz_order option. The initial size of the Cartesian grid will be exactly nx X ny X nz with the minimum coordinate at (0.0, 0.0, 0.0). If a size other than the default is required, consider using the scale and/or translate options.

Smoothing: Sculpt will set automatic defaults for smoothing if user options have not been defined. These include:

These options will generally provide a smoother curve and surface representation but may not adhere strictly to the volume fraction geometric definition. To over-ride the defaults, consider using the following options:

Pillowing: For most 3D models it is recommended using pillowing since triple junctions (curves with at least 3 adjacent materials) will typically be defined where malformed hex elements would otherwise be generated. Surface pillowing (option 1) is usually sufficient to remove poor quality elements at triple junctions.

This option is valid with the 'input_spn' option. The default order of the cells in the spn input file will be read according to the following schema:

If the spn file has the cells in a different order, use this option to specify the order. 0 (xyz) is the default.

This option is valid with the input_spn or input_stitch options. The default will use the integers in the spn or stitch file as the final block IDs in the resulting mesh file. Turning this option ON will compress the IDs so that block IDs will start at 1 and be contiguous through the number of materials. If used, check the Sculpt output for a listing of the correspondance between the block IDs and the IDs used in the SPN file.

Stitch is a new I/O system that has been added to Sandia's SPPARKS (Stochastic Parallel PARticle Kinetic Simulator) tool. It was specially developed for additive manufacturing (AM) simulations. Using Stitch, an output database for microstructure simulations is created incrementally by appending lattice sites much in the same way new material is added to an AM part. See the dump stitch (https://spparks.github.io/doc/dump.html) and set stitch (https://spparks.github.io/doc/set.html) commands in the SPPARKS docs for details.

Used with the input_stitch option to specify a floating point value timestep to extract from the stitch file. Either a stitch_timestep or stitch_timestep_id should be used (not both). If neither is specified, the first timestep in the stitch file will be used. Keywords "first" or "last" may also be used in place of a floating value indicating the first or last timestep in the stitch file.

Used with the input_stitch option to specify an integer ID representing the timestep to extract from the stitch file. Either a stitch_timestep_id or stitch_timestep should be used (not both). The stitch_timestep_id should be an integer, N, representing the Nth timestep encountered in the stitch file. stitch_timestep_id = 1 represents the first timestep in the file. If neither stitch_timestep_id or stitch_timestep is specified, the first timestep encountered in the stitch file will be used.

Used with the input_stitch option to specify the field to extract from the stitch file. If not specified, the first field in the stitch file will be used.

Used with the input_stitch option to list the header information for the given stitch file. If stitch_info is present (no arguments), Sculpt execution will stop after listing stitch information.

Generate a lattice structure from a hex mesh. This command takes the name of an STL format template file which defines the lattice over a unit cube. To generate a valid lattice structure, the facets should be symmetric to the three coordinate planes. The lattice structure will be transformed and copied into each hex of the mesh. The result will be an STL file containing lattice geometry for the mesh.

This option currently requires the name of an exodus mesh on which to define the lattice. Use the --exodus_file (-e) option to specify its path. The current implementation is limited to one block, however if a second block is contained in the Exodus file it will be treated as a solid and stl facets will be generated at the skin of the block.

The name of the output STL file may also be defined by using the --stl_file (-stl) option. If no stl file is specified, the output will use the name of the input exodus file with the extension "_lattice.stl" appended.

In addition to the full lattice geometry, an additional file containing only the lattice from the first layer of hexes will be written. This may be useful in reducing the size of the STL file for visualization purposes only. The name of this file will be the name of the full STL geometry file with the extension ".vis.stl" appended.

The following is an example input file using the lattice option:

Note that this option is currently limited to serial execution (-j 1)

**Examples:**

Example 1 (sql):
```sql
Input Data Files             -inp     --input
  --stl_file                 -stl  <arg> Input STL file                                               
  --diatom_file              -d    <arg> Input Diatom description file                                
  --input_vfrac              -ivf  <arg> Input from Volume Fraction file base name                    
  --input_micro              -ims  <arg> Input from Microstructure file                               
  --input_cart_exo           -ice  <arg> Input from Cartesian Exodus file                             
  --input_spn                -isp  <arg> Input from Microstructure spn file                           
  --spn_xyz_order            -spo  <arg> Ordering of cells in spn file                                
  --compress_spn_ids         -csp  <arg> Compress IDs from SPN file                                   
  --input_stitch             -ist  <arg> Input from Stitch file                                       
  --stitch_timestep          -stt  <arg> Timestep in Stitch file to read                              
  --stitch_timestep_id       -stn  <arg> Timestep ID in Stitch file to read                           
  --stitch_field             -stf  <arg> Field in Stitch file to read                                 
  --stitch_info              -sti        List header info for Stitch file                             
  --lattice                  -l    <arg> STL Lattice Template File                                    

Sculpt Command Summary
```

Example 2 (yaml):
```yaml
Command: stl_file     Input STL file

Input file command:   stl_file <arg>
Command line options: -stl <arg>
Argument Type:        file name with path
```

Example 3 (yaml):
```yaml
Command: diatom_file     Input Diatom description file

Input file command:   diatom_file <arg>
Command line options: -d <arg>
Argument Type:        file name with path
```

Example 4 (unknown):
```unknown
diatoms
      package 'blue_material'
        material 1
        insert stl
          file = 'blue_part1.stl'
        endinsert
        insert stl
          file = 'blue_part2.stl'
        endinsert
      endpackage
      package 'red_material'
        material 2
        insert stl
          file = 'red_part1.stl'
        endinsert
      endpackage
    enddiatom
```

---

## Sculpt Mesh Improvement

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_improvement.htm

**Contents:**
- Sculpt Mesh Improvement
- Pillow
- Pillow All Surfaces
- Pillow Bad Quality at Curves
- Pillow at Domain Boundaries
- Number of Element Layers to Buffer Curves
- Scaled Jacobian Threshold for Curve Pillowing
- Turn OFF Smoothing Following Pillow Operations
- Capture
- Capture Angle

Sculpt options for modifying the mesh to improve mesh quality.

Automatic smoothing provides an effective method for improving element quality. However there may be some cases that cannot be improved with smoothing alone. The options included in this section will apply changes to the underlying hex mesh or to the volume fraction data to increase the opportunity for smoothing to produce a good quality mesh.

For models that have more than one material that share an interface, unless the geometry is precisely aligned with the global axis, it is usually a good idea to turn on pillowing. Pillowing automatically inserts an additional layer of hexes at interface boundaries to improve mesh quality. Without pillowing you may notice inverted or poor quality elements at curve interfaces where 2 or more materials meet.

The pillow option will generate an additional layer of hexes at surfaces as a means to improve element quality near curve interfaces. This is intended to eliminate the problem of 3 or more nodes from a single hex face lying on the same curve. Use one or more of the following options to set up pillowing:

See help on the above options for more information

Pillow option to insert a layer of hexes surrounding each internal surface in the mesh. Where two volumes share a common interface is defined as a surface. All hexes that have at least one of its faces on a surface are defined as the "shrink set" of hexes. A separate shrink set is defined for each unique surface. Hexes in the set are shrunk away from their hex neighbors not in the shrink set. A layer of hexes is then inserted surrounding all hexes in each set. This enforces the condition where no more than one hex edge will lie on any single curve thus allowing more freedom for the smoother to improve element quality.

Surface pillowing is off by default. If both pillow_curves and pillow_surfaces options are used, curve pillowing will be performed before surface pillowing.

See the pillow option for more information on setting additional options for pillowing.

Pillow option to selectively pillow hexes at curves. Only hexes that have faces with 3 or more nodes on a curve will be pillowed. Additional buffer layers of hexes beyond the poor quads at the curves will be included in the pillow region. The number of buffer layers beyond the curve can be controlled with the pillow_curve_layers, where the default will be 3 layers.

Curve pillowing is off by default. If both pillow_curves and pillow_surfaces options are used, curve pillowing will be performed before surface pillowing.

See the pillow option for more information on setting additional options for pillowing.

Pillow option to insert pillow layers at domain boundaries of the initial Cartesian grid definition. One layer of hexes is inserted on each of the six faces of the Cartesian Domain. This option is useful where the void option is used to generate a mesh in the full Cartesian grid and where the adapt option has been used. Without this option, it is likely that hexes with two faces on the same domain boundary will occur if the adaptation extends to the boundary. Turning on the pillow_boundaries option should correct for these cases.

Boundary pillowing is off by default. The pillow_boundaries option may be used in the same input as pillow_surfaces or pillow_curves. The pillow_boundaries option must also be used with the mesh_void option to ensure hexes will exist at the Cartesian domain boundary. See the pillow option for more information on setting additional options for pillowing.

Used for setting the number of buffer hex layers when the pillow_curves option is used. When pillow_curves is used a shrink set is formed from hexes that would otherwise have two or more edges on the same curve. This value will control the extent to which neighboring hexes will be included in the shrink set. The default pillow_curve_layers is 3. Setting this value lower will localize the modifications to the hex mesh, whereas, more layers will extend the region that is affected in correcting the poor quality at curves.

Used for setting the quality threshold for pillowing hexes at curves. When determining hexes to include in the shrink set, the pillow_curves option will look for hexes with more than two nodes of a hex on the same curve. If this condition is satisfied, it will test the mesh quality of quads on the adjacent surfaces that share the common curve. If at least 3 nodes are on a common curve and the Scaled Jacobian of any of the attached quads falls below the, pillow_curve_thresh scaled Jacobian metric, then the associated hexes will be included in the shrink set.

Default for pillow_curve_thresh is 0.3. Increasing this value will tend to increase the total number of hexes added to the mesh, but may result in better mesh quality after smoothing. Lowering this value may reduce the number of additional hexes but could potentially result in more hexes with poor or bad Scaled Jacobian metrics.

Controls the smoothing following pillow operations. To maximize element quality at pillowed hexes, smoothing is always performed after inserting the hex layers. The smoothing step may be omitted if pillow_smooth_off is set. This option can be useful for visualizing the pillow layers that have been inserted, but in most cases will generate poor quality or inverted elements.

This is an experimental option still in development. Nodes at the surfaces of a default sculpt mesh will not necessarily exactly lie on the geometric surfaces prescribed by the input STL geometry. While this characteristic can provide additional flexibility for defeaturing and element quality, there are cases where a more exact surface representation may be desired. The capture option attempts to address this by extracting sharp features and/or projecting nodes to the facet geometry.

Several options are currently being studied as possible solutions. They include the following:

0 = (off) Capture option is off. No attempt is made at capturing sharp features.

1 = (on) STL geometry is used as basis for feature capture. A user defined feature angle is used (capture_angle) to first generate groups of facets from the STL geometry based on capture_angle. Topological curves are defined based on projections to closest surface facets and edges. With default smoothing option, the surface nodes will be projected to the closest STL surfaces as a final step before exporting the exodus mesh. Consider using smooth = to_geometry option.

2 = (exterior_surfaces) Only exterior surfaces are captured. Uses the same procedure as described in capture = 1, except that interior surfaces (those with two adjacent volumes), will be ignored in the capture and projections stage.

3 = (projections_only) For this option, additional topology based on feature angle is not extracted. Only the final projection of surface nodes to the STL facets is done. Note that this option is useful for organic shapes that do not have sharp features, or where sharp features should be ignored.

4 = (feature_angle_smooth) This option uses the procedure outlined in capture = 1, except that the smooth = to_geometry is used by default. Note that capture = 1 used with smooth = to_geometry should be identical to this option.

5 = (topology_smooth) Curve topology is defined similar to capture = 1, except that element face topology is first determined based on closest assigned facet. Curve topology is then extracted based on adjacent element face associativity. Surface node projections are only done for nodes that have unambiguous neighbor associativity. This provides for a tolerant approach to resolving topology that may result in defeaturing. (i.e. where the STL facet topology may be locally more complex than can be resolved by the prescribed resolution). This option also uses the smooth = to_geometry option as default for smoothing. Also note that capture = 5 it is only currently available for serial execution (j=1)

This is an experimental option still in development. Feature angle for capture option.

Similar to the capture option, the capture_side option will project nodes to the initial triangle facets, however projections will be limited only to surface nodes closest to the surface ID specified by the argument. Note that the input STL file can identify and group facets according to a surface ID. However surface IDs are utilized only when using the gen_sidesets option with arguments 3 and 4. When using Cubit, the STL file written when using the sculpt parallel command with sideset options 3 and 4 will include surface identification for surfaces in the STL file. A workflow for using the capture_side option might include the following:

The result should be a mesh where surface nodes closest to the surfaces identified by the unique sideset ID will lie precisely on their closest surface.

Option to automatically detect and remove small features. Primarily used for defeaturing microstructure data, however can be used with any input format. The following options are available:

See also the defeature_iters and defeature_bbox options for additional control of the defeature = filter option. The compare_volume option can also be used to validate that changes made to material volumes are within acceptable limits.

When used with defeature options filter (1) or filter_and_collapse (3), specifies the minimum number of cells below which a volume will be eliminated. The cells of small volumes will be absorbed into the predominant material of the neighboring cells. If not specified and defeature options filter (1) or filter_and_collapse (3) are used, the min_vol_cells value will be set to 5.

The defeature_bbox option is used in conjunction with defeature = filter (1). It is used to modify the defeature filter criteria at cells that are immediately adjacent to the Cartesian grid's domain boundary. It is most effective for microstructure data but can be used with any input format. The defeature = filter (1) option will remove protrusions identified by cells that are surrounded on 4 or 5 sides by another material. For cells that are at the domain boundary, cells will have missing adjacent cells on at least one face. If the defeature_bbox=true option is used, the missing adjacent cells are considered a different material and counted in the 4 or 5 surrounding cells with a different material. In contrast, the defeature_bbox=false option will not count the missing adjacent cells. Using the defeature_bbox=true has the effect of more aggressively modifying cells at the domain boundaries to avoid protrusions. The default for this option is defeature_bbox=false. It will be ignored if defeature = filter (1) is not used.

Used with the defeature option. Controls the maximum number of iterations of defeature filtering that will be performed. Setting this value greater than the default of 10 can be useful for very noisy data where a significant number of iterations will need to be performed to resolve the geometry.

When performing non-manifold resolution, the defeature state of some of the cells may be effected. As a result, the defeaturing and non-manifold resolution procedures are performed in a loop until no further changes can be made. The defeature_iters sets the maximum number of defeature and non-manifold resolution procedures that will be performed. Note that if defeaturing reaches the maximum iteration value without completely resolving all non-manifold conditions, that subsequent sculpt procedures may not succeed. Set this value higher to allow the defeaturing and non-manifold resolution to run to completion. The stair = 1 option can be used to interrogate the model to see where non-manifold conditions may still exist.

Add additional cells at the boundary of a given material. Takes two input values, a material and a volume fraction between 0 and 1. This option is useful for noisy input data that may not form contiguous volumes. Thickening a material may close small gaps making the material continuous. To perform the thicken operation, cells in adjacent materials are removed and reassigned to the indicated material. This option requires both a valid material ID and volume fraction value, where the volume fraction represents the amount of material to be added to each neighboring cell. For example:

thicken material = 1 0.2 thicken_material = 2 0.5

each neighboring cell to material 1 will change approximately 20 percent of its volume to be material 1. Other materials present in the cell will be decreased accordingly to maintain a sum of 1.0 for each cell. Additional material is accumulated in neighboring cells from each adjacent cell it shares with material 1, so that if for example a neighbor cell shares faces with three cells of material 1, it will add 0.6 (0.2 X 3) of material 1 volume fraction to the neighbor. If more than one thicken_material option is used, the thicken operation will be performed in the order they appear in the input. For the above example, material 1 would first be thickened, followed by material 2. If materials 1 and 2 are adjacent, thickening in this case, material 2 would take precedence, potentially removing cells from material 1 at their interface.

Add additional void material when non-void material is detected as touching or immediately adjacent. Takes one input value, a volume fraction normally about 1.0 that indicates the quantity of volume fraction inserted at each node if the input grid where non-void material adjacency is detected. A value of 1.0 indicates void material equal to the volume of one cell will be added at the nodes, reducing the volume fractions of other materials present in adjacent cells. Smaller input values will generate a smaller gap between materials, but can run the risk of materials bleeding into one another.

This option is useful when it is known that non-void materials in the model should not touch, instead should have a gap where they would otherwise touch or overlap. For example:

each node where its adjacent cells have two or more non-void materials present will have additional void material added. In this case, if 8 adjacent cells are assumed, a contribution of 1/8 void volume fraction will be added to each adjacent cell to the node. Other materials present in the cells will be decreased accordingly to maintain a sum of 1.0 for each cell.

This option expands the Cartesian grid by a specified number of layers. It can be used with any of the following input options:

In some cases the interior material interfaces may intersect the domain boundaries at small acute angles. When this occurs it may be difficult or impossible to achieve computable mesh quality at these intersections. To address this problem, one or more layers of hexes may be added to the Cartesian grid. The volume fractions from cells at the boundary are copied to generate additional layers. This has the effect of increasing the angle of intersection for any material interfaces intersecting the domain boundary. Usualy a value of 1 or 2 is sufficient to sufficiently improve quality.

Note that the resulting mesh in the expanded layers serves only to improve mesh quality and will only duplicate existing data at the boundaries. It may not reflect the actual material structure within the expansion layers.

This option potentially modifies the outermost layer of Cartesian cells of a microstructures file. It will identify isolated cells where the assigned material is unique from all of its surrounding cells at the boundary. When this occurs, the cell material is reassigned to the dominant nearby material.

This option is useful if it is noted that a cell structure just barely grazes the exterior planar boundary surface. Poor quality elements can often result with this condition. The micro_shave option will, in effect, remove material from the cell structure, but will result in better quality elements by removing the intersection region with the boundary.

micro_shave can be used with any of the following input options:

Remove hexes below the specified scaled Jacobian metric.

This option defines how the mesh removes void elements that are at the free_surface_sideset. Used with the free_surface_sideset, input_mesh and capture=5 options. Normally with the default wear_method = cell (0) option, elements in the input_mesh outside of the specified free_surface_sideset are removed when the percent of its volume (volume fraction) lying outside of the free_surface_sideset exceeds 50 percent. If the wear_method = sheet (2) option is set, volume fraction of continuous layers of elements (sheets) that lie at the free_surface_sideset can be removed. The entire sheet of elements will be retained or removed based on the total volume fraction of the elements in the sheet.

The wear_method = sheet (2) option is most useful when used with a swept input_mesh where the free_surface_sideset is approximately orthogonal to the sweep direction. It can especially improve mesh quality when using the capture=5 option where small geometric features, such as cracks, are encountered near the free_surface_sideset. See also the crack_min_elem_thickness option, to control how cracks are captured at the free_surface_sideset.

Defines the minimum allowed thickness of the elements resolving the side of a crack. Used with the wear_method = sheet (2) and match_sideset options to potentially improve mesh quality at cracks near the free_surface_sideset. Cracks are normally identified using the match_sideset and match_sidesets_nodset options. The distance from the bottom of the crack to the free_surface_sideset is measured to determine the element thickness. If the thickness is below the specified crack_min_elem_thickness value, the crack walls are merged together at this location. If a crack_min_elem_thickness is not specified, cracks near the free_surface_sideset will only be collapsed when the surrounding volume fraction of the sheet drops below 50 percent.

Defines the minimum number of swept layers of the reference mesh to retain when using sculpt with the wear_method = sheet (2). These layers will be retained even if their volume fraction indicates that they should be discarded.

**Examples:**

Example 1 (sass):
```sass
Mesh Improvement             -imp     --improve
  --pillow                   -p    <arg> Set pillow criteria (1=surfaces)                             
  --pillow_surfaces          -ps         Turn on pillowing for all surfaces                           
  --pillow_curves            -pcv        Turn on pillowing for bad quality at curves                  
  --pillow_boundaries        -pb         Turn on pillowing at domain boundaries                       
  --pillow_curve_layers      -pcl  <arg> Number of elements to buffer at curves                       
  --pillow_curve_thresh      -pct  <arg> S.J. threshold to pillow hexes at curves                     
  --pillow_smooth_off        -pso        Turn off smoothing following pillow operations               
  --capture                  -c    <arg> Project to facet geometry <beta>                       
  --capture_angle            -ca   <arg> Angle at which to split surfaces <beta>                
  --capture_side             -sc   <arg> Project to facet geometry with surface ID                    
  --defeature                -df   <arg> Apply automatic defeaturing                                  
  --min_vol_cells            -mvs  <arg> Minimum number of cells in a volume                          
  --defeature_bbox           -dbb        Defeature Filtering at Bounding Box                          
  --defeature_iters          -dfi  <arg> Maximum Number of Defeaturing Iterations                     
  --thicken_material         -thm  <arg> Expand a given material into surrounding cells               
  --thicken_void             -thv  <arg> Insert void material to remove overlap                       
  --micro_expand             -me   <arg> Expand Microstructure grid by N layers                       
  --micro_shave              -ms         Remove isolated cells at micro. boundaries                   
  --remove_bad               -rb   <arg> Remove hexes with Scaled Jacobian < threshold             
  --wear_method              -wm   <arg> Method for removing void at free surface                     
  --crack_min_elem_thickness -cmet <arg> Minimum element thickness in crack                           
  --min_num_layers           -mnl  <arg> Minimum number of layers to keep using wear_method=2         

Sculpt Command Summary
```

Example 2 (sass):
```sass
Command: pillow     Set pillow criteria (1=surfaces)

Input file command:   pillow <arg>
Command line options: -p <arg>
Argument Type:        integer (0, 1, 2, 3) 
Input arguments: off (0)
                 surfaces (1)
                 curves (2)
                 domain_boundaries (3)
                 surfaces_no_smoothing (100)
                 curves_2_layers (212)
                 curves_3_layers (213)
                 curves_4_layers (214)
                 curves_5_layers (215)
                 curves_2_layers_no_smoothing (202)
                 curves_3_layers_no_smoothing (203)
                 curves_4_layers_no_smoothing (204)
                 curves_5_layers_no_smoothing (205)
```

Example 3 (yaml):
```yaml
Command: pillow_surfaces     Turn on pillowing for all surfaces

Input file command:   pillow_surfaces
Command line options: -ps
```

Example 4 (yaml):
```yaml
Command: pillow_curves     Turn on pillowing for bad quality at curves

Input file command:   pillow_curves
Command line options: -pcv
```

---

## Sculpt Mesh Transformation

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_transformations.htm

**Contents:**
- Sculpt Mesh Transformation
- Translate Mesh Coordinates in X
- Translate Mesh Coordinates in Y
- Translate Mesh Coordinates in Z
- Scale X Mesh Coordinates
- Scale Y Mesh Coordinates
- Scale Z Mesh Coordinates

Sculpt options for applying transformations to the mesh following mesh generation. For cases where the initial geometry description may not be at the desired scale or bounds, the transformation options provide the ability to apply transformations to the node locations following the mesh generation procedure. This can be effective for microstructure models, where the size and location may be defined by the given intervals of the data.

Translate all mesh coordinates written to Exodus file by X delta distance.

Translate all mesh coordinates written to Exodus file by Y delta distance.

Translate all mesh coordinates written to Exodus file by Z delta distance.

Scale all mesh X coordinates written to Exodus file by given factor

Scale all mesh Y coordinates written to Exodus file by given factor

Scale all mesh Z coordinates written to Exodus file by given factor

**Examples:**

Example 1 (csharp):
```csharp
Mesh Transformation          -tfm     --transform
  --xtranslate               -xtr  <arg> Translate final mesh coordinates in X                        
  --ytranslate               -ytr  <arg> Translate final mesh coordinates in Y                        
  --ztranslate               -ztr  <arg> Translate final mesh coordinates in Z                        
  --xscale                   -xsc  <arg> Scale final mesh coordinates in X                            
  --yscale                   -ysc  <arg> Scale final mesh coordinates in Y                            
  --zscale                   -zsc  <arg> Scale final mesh coordinates in Z                            

Sculpt Command Summary
```

Example 2 (yaml):
```yaml
Command: xtranslate     Translate final mesh coordinates in X

Input file command:   xtranslate <arg>
Command line options: -xtr <arg>
Argument Type:        floating point value
```

Example 3 (yaml):
```yaml
Command: ytranslate     Translate final mesh coordinates in Y

Input file command:   ytranslate <arg>
Command line options: -ytr <arg>
Argument Type:        floating point value
```

Example 4 (yaml):
```yaml
Command: ztranslate     Translate final mesh coordinates in Z

Input file command:   ztranslate <arg>
Command line options: -ztr <arg>
Argument Type:        floating point value
```

---

## Sculpt Mesh Type

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_mesh_types.htm

**Contents:**
- Sculpt Mesh Type
- Stair
- Mesh Void
- Trimesh
- Tetmesh
- Degenerate (Edge Collapse) Threshold
- Maxmimum Degenerate Iterations
- HTet
- HTet Method
- HTet Material

Sculpt options for specifying the type of mesh that will be generated. The default mesh type that will be produced from Sculpt is an unstructured all-hex mesh that will attempt to conform as closely as possible to the input geometry. Sculpt will normally generate its mesh on the interior of the input geometry, however with the mesh_void option, it can also generate the mesh on the exterior of the geometry, out to the extent of the user-defined Cartesian overlay grid.

In addition to the default hex mesh, other types of meshes may be produced. This includes the stair-step mesh where the cells of the Cartesian grid inside or intersecting the geometry are used directly as the mesh without projections or smoothing. A triangle mesh may also be generated, which can be used as the basis for a facet-based geometry representation. Other methods include the capabilities to generate a hex-dominant mesh with hexes and tets as well as the ability to include degenerate elements.

The stair option generates a stair-step mesh where the cells of the Cartesian grid are used in the final mesh without projection or smoothing to the material interfaces. Cells selected from the Cartesian grid to be used in the final mesh will have volume fraction greater than 0.5. Several different options for the stair argument are available:

off (0): Stair option is off (default)

full (1): Stair-step mesh is generated, but additional processing is done to ensure material interfaces are manifold. This option may add or subtract cells from the basic mesh (where volume fraction > 0.5) to ensure no non-manifold connections between nodes and edges exist in the final mesh.

interior (2): The exterior boundary will be smooth while internal material interfaces will be stair-step. This option also ensures manifold connections between elements.

fast (3): Generates the final mesh based only on volume fraction criteria. No additional processing is done to ensure manifold connections between edges and nodes.

The mesh_void accepts the following parameters:

off (0): No mesh is generated in the void region

on (1): Mesh is generated in the void region

only (2): Mesh is generated only in the void region and not in the material

If mesh_void option is set to on or only, then the void space surrounding the geometry will be treated as a separate material. Elements will be generated in the void to the extent of the Cartesian grid boundaries. If void_mat option is not used, the material ID of elements in the void region will be the maximum material ID in the model + 1. See also the separate_void_blocks option to separate the void elements into contiguous blocks.

Generate a triangle mesh of the surface geometry. Surface geometry will be defined based on input grid resolution as well as user defined smoothing smoothing parameters. Resulting exodus mesh will contain only TRI elements. All TRI elements will be assigned to the same block in the exodus file.

This option is most often used in conjunction with the --write_geom option used to build a mesh-based geometry in Cubit. Use the following command in Cubit to import a Sculpt trimesh exodus file and s2g file (produced from --write_geom)

See write_geom for more information on s2g files.

Under Development - uses space-filling tets as base grid. Size and extent is defined by bounding box options.

The meshgems (2) option uses a third party tet mesher to place interior tets. Triangle mesh is defined by splitting quads on surface. Both tetmesh options are currently only implemented for serial execution.

Some geometries will not permit a usable mesh with a traditional all-hex mesh. Sculpt includes the option to automatically and selectively collapse element edges to improve low-quality elements. The max_deg_iters and the deg_threshold values are used to control the creation of degenerates. Degenerate elements are treated as standard hex elements, but use repeated nodes in the eight-node connectivity array.

The deg_threshold value indicates scaled Jacobian threshold for edge collapses. Nodes at hexes below this threshold will be candidates for edge collapses, provided doing so will improve the minimum scaled Jacobian at the neighboring hexes. Default is -1.0.

Maximum number of edge collapse iterations to perform to create degenerate hex elements. Default is 0. See also deg_threshold

Automatically generate tets in place of poor quality elements. This option can be used to eliminate poor quality hex elements by replacing each hex that falls below the user defined Scaled Jacobian with 6 or 24 tets. The method used for splitting is controlled by the htet_method option. The default threshold value for htet is -1.0, which turns off the generation of all tets. A value of 1.0 will split all hexes into tets.

If a neighboring element is a hex, and will not be split, one may choose whether to use pyramid transitions or have hanging nodes. The default is to have hanging nodes with a tied contact condition being created. The transition type may be specified with the htet_transition command.

If tet blocks are created, their ids will be the material id plus an offset based on the maximum material id. Likewise, any pyramid blocks created will be offset as well, with their ids coming after hex block ids if there are no tets, or with their ids coming after tet blocks.

Specifies which method is used for splitting hexes into tets:

structured (0): Each hex is subdivided into 24 tets. Additional nodes are The 24 tets are formed by inserting one node at the center of each face and one on the interior.

unstructured (1): Each hex is subdivided into 6 tets. No additional nodes are inserted. Note that the unstructured method does not currently support the htet_transition options pyramid and tied_contact.

Default htet_method is structured (0).

Generate tets in place hexes in a given material. This option can be given multiple times to specify multiple materials. Each hex in a material is replaced with 24 tets. The 24 tets are formed by inserting one node at the center of each face and one on the interior.

If an neighboring element is a hex, and will not be split, one may choose whether to use pyramid transitions or have hanging nodes. The default is to have hanging nodes with a tied contact condition being created. The transition type may be specified with the htet_transition command.

If tet blocks are created, their ids will be the material id plus an offset based on the maximum material id. Likewise, any pyramid blocks created will be offset as well, with their ids coming after hex block ids if there are no tets, or with their ids coming after tet blocks.

When generating tets adjacent to hexes, the transition type between the two elements can be defined. Possible options are:

If pyramid transition is specified, the hex may be split into 1 pyramids and 20 tets, 2 pyramids and 16 tets, 3 pyramids and 12 tets, and so forth. The mesh will remain conformal if pyramid transition is specified.

A tied contact condition can be defined to ensure continuity of the neighboring tets and hexes. To facilitate this, one additional nodeset and sideset will be generated and output to the exodus file if the gen_sidesets = variable (2) option is specified. The sideset and nodeset will be identified with the following IDs:

Sideset 10000 = the set of hex faces that interface a set of 4 tets.

Nodeset 1000 = the set of nodes at the interface between hexes and tets. One node per face in Sideset 10000 will be included.

When generating tets adjacent to hexes, pyramid transitions can be specified for a given material or material interface. To specify a material interface, two material ids are given to specify pyramid transition between the two materials. To specify multiple materials or multiple material interfaces, this command may be used multiple times.

When generating tets adjacent to hexes, tied contact transitions can be specified for a given material or material interface. To specify a material interface, two material ids are given to specify tied contact transition between the two materials. To specify multiple materials or multiple material interfaces, this command may be used multiple times.

When generating tets adjacent to hexes, no transition can be specified for a given material or material interface. To specify a material interface, two material ids are given to specify no transition between the two materials. To specify multiple materials or multiple material interfaces, this command may be used multiple times.

Generates a periodic mesh for either Cartesian or unstructured mesh input. Ensures that resulting mesh nodes and faces are precisely matching on opposite sides of the mesh.

Unstructured mesh input: When used with the --input_mesh option opposite sides of the mesh must be identified using pairs of primary (leading) and secondary (trailing) nodesets using the --periodic_nodesets (-pns) option. Nodes in the nodeset pairs must be separated by a constant translation or rotation. If a rotation is used between primary (leading) and secondary (trailing) nodesets, the --periodic_axis (-pax) option must be used. If not used, then the transformation is assumed to be pure translation. Input geometry is assumed to be periodic with a period equal to that of the input mesh. Results from non-periodic geometry used with the periodic option may be unpredictable. The following is an example of an input file that uses the periodic option on an unstructured input mesh:

Cartesian grid input: This option is often used for computational materials modeling. Sculpt can generate a true periodic mesh in a representative volume element (RVE) where meshes on all opposite faces of the RVE will precisely match. When used with a Cartesian grid, the --periodic_nodesets and --periodic_axis options are ignored. The following is an example sculpt input file that utilizes the --periodic option on a Cartesian grid with geometry defined in a diatom file. It also utilizes the --adapt_type option to automatically refine and the gen_sidesets = RVE option to generate sidesets at the six RVE faces.

Geometry Requirements: In order to generate a valid periodic mesh, the input geometry must also be periodic and the bounding box parameters should span exactly one period of the geometry. To check the periodicity of the geometry and prescribed bounding box, see the check_periodic option.

Note: The resulting mesh at the boundaries of the Cartesian grid (RVE) will not be projected to the planes of the bounding box. The result will be a "ragged" boundary in order to maintain periodicity between nodes on opposite sides of the mesh. Also note that results from the use of the periodic option may be undefined or unstable when used with non-periodic input geometry.

When using the periodic option with a Cartesian base grid, the input geometry must be periodic with respect to the grid bounding box in order to meet the minimum requirements of a valid periodic mesh. The bounding box must span exactly one period in each dimension. If this requirement is not met, a valid mesh may still be generated, however, periodicity will not be guaranteed. The check_periodic option is used to check this requirement. See also check_periodic_tol to set the tolerance for checking periodicity.

The check_periodic option is ignored if the periodic option is OFF or set to false.

Used on conjunction with the check_periodic option. It specifies a tolerance value when checking periodicity. Check periodic option checks the difference between computed volume fractions for cells on the overlay grid that are separated by exactly one period. The periodic tolerance is the allowable volume fraction difference between cells separated by one period. Default value is 1e-6.

For an unstructured base grid, specifies an axis about which the nodes in the primary (leading) nodesets will be rotated about to produce the secondary (trailing) nodesets. Six floating point numbers are specified, the first three define the origin of the axis and the last three define the axis direction. This option must be used with --periodic (-per), --periodic_nodesets (-pns), and --input_mesh (-im) options. If the --periodic (-per) option is used without the --periodic_axis option, the transformation between primary (leading) and secondary (trailing) nodesets is assumed to be pure translation.

For an unstructured base grid, specifies the primary-secondary (leading-trailing) nodeset pairs. Primary (leading) nodesets should be able to be translated or rotated about a specified axis to produce the nodes in the secondary (trailing) nodesets. Nodesets must be specified in pairs, where each primary (leading) nodeset corresponds to a single secondary (trailing) nodeset. Each nodeset pair must maintain an identical translation or rotation. If a rotation is used, the axis and origin of rotation must be specified with the --periodic_axis (-pax) option. This option should be used with --periodic (-per), --periodic_nodesets (-pns), and --input_mesh (-im) options.)

**Examples:**

Example 1 (typescript):
```typescript
Mesh Type                    -typ     --type
  --stair                    -str  <arg> Generate Stair-step mesh                                     
  --mesh_void                -V    <arg> Mesh void                                                    
  --trimesh                  -tri        Generate tri mesh of geometry surfaces                       
  --tetmesh                  -tet  <arg> Under Development                                            
  --deg_threshold            -dg   <arg> Convert hexes below threshold to degenerates                 
  --max_deg_iters            -dgi  <arg> Maximum number of degenerate iterations                      
  --htet                     -ht   <arg> Convert hexes below quality threshold to tets                
  --htet_method              -hti  <arg> Method used for splitting hexes to tets                      
  --htet_material            -htm  <arg> Convert hexes in given materials to tets                     
  --htet_transition          -htt  <arg> Transition method between hexes and tets                     
  --htet_pyramid             -htp  <arg> Local transition pyramid                                     
  --htet_tied_contact        -htc  <arg> Local transition tied contact                                
  --htet_no_interface        -htn  <arg> Local transition none                                        
  --periodic                 -per        Generate periodic mesh                                       
  --check_periodic           -cp   <arg> Check for periodic geometry                                  
  --check_periodic_tol       -cpt  <arg> Tolerance for checking periodicity                           
  --periodic_axis            -pax  <arg> Axis periodicity is about                                    
  --periodic_nodesets        -pns  <arg> Nodesets ids of primary/secondary (leading/trailing) nodesets

Sculpt Command Summary
```

Example 2 (yaml):
```yaml
Command: stair     Generate Stair-step mesh

Input file command:   stair <arg>
Command line options: -str <arg>
Argument Type:        integer (0, 1, 2, 3) 
Input arguments: none (0)
                 off (0)
                 on (1)
                 full (1)
                 interior (2)
                 fast (3)
```

Example 3 (yaml):
```yaml
Command: mesh_void     Mesh void

Input file command:   mesh_void <arg>
Command line options: -V <arg>
Argument Type:        true/false or only 
Input arguments: off (0)
                 false (0)
                 on (1)
                 true (1)
                 only (2)
```

Example 4 (yaml):
```yaml
Command: trimesh     Generate tri mesh of geometry surfaces

Input file command:   trimesh
Command line options: -tri
```

---

## Sculpt Output

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_output.htm

**Contents:**
- Sculpt Output
- Exodus File
- Large Exodus Output
- Volume Fraction File
- Quality
- Export Communication Maps
- Write S2G Geometry File
- Write Mesh Based Geometry
- Report VFrac to Mesh Volume Comparison
- Report Sideset Statistics

Sculpt options for specifying output. The primary format for the hex meshes produced from Sculpt is Exodus II. One exodus file will be produced for each processor based upon the -j or num_procs argument. If required, the exodus files can be joined using the epu utility.

Other options for export include the ability to dump the volume fraction representation of the input geometry as well as the ability to write geometry files for use in Cubit.

The base file name of the resulting exodus mesh. Exodus files will be in the form <exodus_file>.e.<nproc>.<iproc>. For example, if the number of processors used is 3 and the exodus_file argument is "model" the following files would be written:

If no exodus_file argument is used, output files will be in the form <stl_file>_diatom_results.e.<nprocs>.<iproc>. For example, if the number of processors used is 3 and the stl_file (or diatom_file) is "model.stl", the following files would be written:

A full path may be used when specifying the base exodus file name, otherwise files will be placed in the current working directory. If the exodus_file option is not used, exodus files will be placed in the same directory as the input diatom or stl file.

Generate output Exodus file(s) to allow IDs greater than 2^31 (2.14 Billion). This option should be used if the intent is to generate billions of elements in parallel on HPC platforms. This option will approximately double the size of output exodus files, so is normally only used for very large parallel applications.

Optionally generate exodus files containing a hex mesh of the Cartesian grid containing volume fraction data as element variables. This series of parallel exodus files can later be used as direct input to sculpt using the --input_vfrac (-ivf) command. If not specified, no volume fraction data files will be generated.

Specify a filename to write mesh quality metrics. If the file already exists, metrics will be appended. Quality metrics and other details of the run will be written to this file. This option is currently off by default.

Used for debugging and verification. Exodus files of the mesh containing the communication nodes and faces at processor boundaries will be written as nodes and side sets. This provides a way to visually check the validity of the parallel communication maps.

An s2g (Sculpt to Geometry) file, with the pattern <fileroot>.s2g, will be produced when this argument is used where fileroot is the string specified by the --exodus_file or -e option. An s2g file includes geometry associativity for the exodus file that is written. If used with Cubit's "import s2g <fileroot>" a mesh-based geometry will be generated in Cubit with geometric entities prescribed by Sculpt through the s2g file.

When used with the --trimesh option, the s2g file can provide information to Cubit to build a set of mesh-based geometry volumes where only the surfaces are meshed. This is useful for using the tet meshing capabilities in Cubit to mesh the discrete geometry that was generated in Sculpt. For example, a tet mesh may be constructed from microstructures spn data (see import_spn) with the following workflow:

Note that the write_geom and trimesh options are still in development and will currently only work with a single processor (-j 1).

An MBG (Mesh Based Geometry) file will be produced when this argument is used with the pattern <fileroot>.mbg, where fileroot is the string specified by the --exodus_file or -e option. An MBG file includes the surface and topology definition defined by sculpt as a result of the interface reconstruction process. It will correspond to the boundary of the 3D elements that are generated in the exodus file, or the surface elements generated with the --trimesh option.

An MBG file can be be imported into Cubit using the following Cubit command line options:

A report will be generated and printed to the terminal following the mesh summary that compares the input volume fraction of the geometry with that of the final finite element mesh. If a volume fraction format is not used as input, the volume fractions will be computed on the refined base grid and used as comparison. Note that exact geometric volumes of the STL or analytic geometry are not used for comparison, rather the volume fraction approximation of the geometry on the refined Cartesian grid.

The following is a brief description of each column:

A report will be generated and printed to the terminal following the mesh summary that displays the statitics for the surface areas of the sidesets in the final FEA mesh. This is often useful for microstructures use cases where it may be important to know the interface area between materials. This should be used with the gen_sidesets option to be effective.

**Examples:**

Example 1 (typescript):
```typescript
Output                       -out     --output
  --exodus_file              -e    <arg> Output Exodus file base name                                 
  --large_exodus             -le   <arg> Output large Exodus file(s)                                  
  --volfrac_file             -vf   <arg> Output Volume Fraction file base name                        
  --quality                  -Q    <arg> Dump quality metrics to file                                 
  --export_comm_maps         -C          Export parallel comm maps to debug exo files                 
  --write_geom               -G          Write geometry associativity file                            
  --write_mbg                -M          Write mesh based geometry file <beta>                  
  --compare_volume           -cv         Report vfrac and mesh volume comparison                      
  --compute_ss_stats         -css        Report sideset statistics                                    

Sculpt Command Summary
```

Example 2 (yaml):
```yaml
Command: exodus_file     Output Exodus file base name

Input file command:   exodus_file <arg>
Command line options: -e <arg>
Argument Type:        character string
```

Example 3 (unknown):
```unknown
model.e.3.0
    model.e.3.1
    model.e.3.2
```

Example 4 (unknown):
```unknown
model_diatom_results.e.3.0
    model_diatom_results.e.3.1
    model_diatom_results.e.3.2
```

---

## Sculpt Overlay Grid Specification

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_sizing.htm

**Contents:**
- Sculpt Overlay Grid Specification
- Number of Intervals X
- Number of Intervals Y
- Number of Intervals Z
- Xmin Bounding Box Range
- Ymin Bounding Box Range
- Zmin Bounding Box Range
- Xmax Bounding Box Range
- Ymax Bounding Box Range
- Zmax Bounding Box Range

Sculpt options for setting up the overlay grid. Sculpt is an overlay-grid method that requires a base mesh that it will modify to generate the final mesh. The base mesh can be in the form of a Cartesian grid, but can also be any general unstructured hexahedral mesh defined in an exodus file (see the input_mesh option). Pamgen can also be used to generate an unstructured base mesh (see input_mesh_pamgen).

When an overlay Cartesian grid is used as the basis for the all-hex mesh that will be produced, the bounds and size of the cells defining the grid must be specified. The Cartesian grid can be defined in one of two ways:

Other options for setting up the Cartesian base grid include align and expand which are normally used with the second method. The align option will automatically rotate the grid to best match the characteristic direction of the geometry rather than maintaining alignment with the global Cartesian directions. The expand option over-rides the default expansion of the Cartesian grid beyond the bounding box of the geometry and allow the user to specify a specific expansion percentage.

Defines the number of intervals in the x direction of the base Cartesian grid used for defining the volume fraction definition and meshing For best results the intervals specified should result in approximately equilateral cells.

Defines the number of intervals in the y direction of the base Cartesian grid used for defining the volume fraction definition and meshing For best results the intervals specified should result in approximately equilateral cells.

Defines the number of intervals in the z direction of the base Cartesian grid used for defining the volume fraction definition and meshing For best results the intervals specified should result in approximately equilateral cells.

Defines the minimum x coordinate of the bounding box or range of the Cartesian mesh to be used for meshing.

See also ymin, zmin, xmax, ymax, zmax.

Defines the minimum y coordinate of the bounding box or range of the Cartesian mesh to be used for meshing.

See also xmin, zmin, xmax, ymax, zmax.

Defines the minimum z coordinate of the bounding box or range of the Cartesian mesh to be used for meshing.

See also xmin, ymin, xmax, ymax, zmax.

Defines the maximum x coordinate of the bounding box or range of the Cartesian mesh to be used for meshing.

See also xmin, ymin, zmin, ymax, zmax.

Defines the maximum y coordinate of the bounding box or range of the Cartesian mesh to be used for meshing.

See also xmin, ymin, zmin, xmax, zmax.

Defines the maximum z coordinate of the bounding box or range of the Cartesian mesh to be used for meshing.

See also xmin, ymin, zmin, xmax, ymax.

Defines a target edge size for the cells of the base Cartesian grid. Both interval and cell_size can not be specified simultaneously. If cell_size is used without a range specification, a bounding box of the geometry will be computed and used as the default range

The align option will attempt to orient the Cartesian grid with the main dimensions of the geometry. This is done by defining a tight bounding box around the geometry using an optimization procedure where the objective is to minimize the difference in volume between an enclosing box and the geometry. Using the align command will override any bounding box parameters previously entered and will build an "aligned" bounding box around the full geometry. It is currently only implemented for STL geometry and will ignore any other diatom definitions. Note that this option will also write temporary stl and diatom files to the working directory.

Sculpt will measure a tight bounding box of the input model and expand the box by the specified percentage in x, y and z. Input value can be any positive or negative floating point value where 1.0 represents 100 percent expansion. If not specified, the default will add about 2.5 cell widths to the bounding box on each side. This option should be used with the cell_size option. It will be ignored if a specific bounding box has been defined (ie. xmin, ymin, etc...).

Option to import an Exodus file to use as the base mesh for Sculpt. Sculpt's meshing procedure requires a base mesh from which geometry is recovered and captured. The default base mesh is a Cartesian grid that is defined by specifying a bounding box and intervals. The input_mesh option permits a general hexahedral mesh to be used as the base mesh instead of a Cartesian grid. This option currently supports a serial and parallel Exodus files containing HEX8 elements with any number of blocks.

The input_mesh option can also be used in parallel. Sculpt currently requires the mesh to be decomposed prior to running sculpt. The SEACAS decomp tool can be used to pre-process any exodus mesh to break it into multiple meshes ready for use in sculpt. SEACAS is an open source library available on github. For example, when using four processors with sculpt, you would use the following command:

The result would be the four meshes:

Once the base mesh has been decomposed, Sculpt can be run. In this case, the input_mesh option would use the root simple-mesh.g as the argument.

If the -j 4 option is used, sculpt will look for 4 meshes in the current working directory with the appropriate root and extension.

Four different options are supported for describing the geometry when using the input_mesh option:

This option is valid when specifying both input_mesh and spn_file. Using this option, the materials of the cells in the spn file are mapped onto only the elements of the specified blocks in the input_mesh file. The remaining blocks are treated as void. The behavior without this option maps the materials of the cells in the spn file onto elements of all blocks in the input_mesh file.

This option is valid when specifying an 'input_mesh' . Using this option, the material definition in the final mesh may be defined based on the material definitions on the geometry, or based on the block ids of the input mesh. For example, a diatom file defining geometry would have materials defined which are used to define the materials in the final mesh. The default is to use material definitions on the geometry. Possible options are:

Option to use Pamgen to create a base mesh for Sculpt. Pamgen is an open source meshing tool developed at Sandia for generating hexahedral meshes from geometric primitives. In addition to being a stand-alone meshing solution, it is a parallel tool that is integrated as an inline meshing tool for Sandia's shock physics simulation tool, Alegra. Pamgen has also been integrated in Sculpt as a solution for automatically defining a base mesh.

The input_mesh_pamgen option permits a mesh defined my Pamgen input parameters to define the base mesh. A limited set of brick and cylinder primitives are supported by Pamgen. The name of an ascii file containing the pamgen mesh definition is used as the argument for this option. The following is a simple example of a pamgen mesh description. It generates a partial cylinder with a span of 90 degrees and height of 1.0. Other parameters allow for specific interval and sizing specifications as well as block/material identification.

For a full description of Pamgen and input parameters see the following document:

David M. Hensinger, Richard R. Drake, James G. Foucar, Thomas A. Gardiner, "Pamgen, a Library for Parallel Generation of Simple Finite Element Meshes", Sandia Report SAND2008-1933 (2008)

Similar to the input_mesh option, the same geometry input options are available. They include stl_file, diatom_file and input_spn. See the input_mesh option for additional details and limitations.

Import a set of files, one per processor, using the base name defined by the import_mesh option. When not used (default), the assumption of input exodus meshes is to include parallel (nemesis) data where parallel relationships between neighboring processors has already been established. This is normally done by using the SEACAS decomp tool to decompose a single exodus mesh into multiple files.

If the join_parallel option is used, sculpt assumes the parallel relationships are not included and will establish these relationships based on proximity of node locations at processor boundaries. Note that the file naming convention should follow the standard exodus parallel file naming convention. For example, a mesh spread across 4 files would be named:

This option is currently only implemented for axis aligned rectangular processor domains. This option can also be used to just stitch exodus files and dump resulting files without any additional sculpt operations. The following is an example of a sculpt input file that does simple stitching without any additional sculpt operations:

**Examples:**

Example 1 (sql):
```sql
Overlay Grid Specification   -ovr     --overlay
  --nelx                     -x    <arg> Num cells in X in overlay Cartesian grid                     
  --nely                     -y    <arg> Num cells in Y in overlay Cartesian grid                     
  --nelz                     -z    <arg> Num cells in Z in overlay Cartesian grid                     
  --xmin                     -t    <arg> Min X coord of overlay Cartesian grid                        
  --ymin                     -u    <arg> Min Y coord of overlay Cartesian grid                        
  --zmin                     -v    <arg> Min Z coord of overlay Cartesian grid                        
  --xmax                     -q    <arg> Max X coord of overlay Cartesian grid                        
  --ymax                     -r    <arg> Max Y coord of overlay Cartesian grid                        
  --zmax                     -s    <arg> Max Z coord of overlay Cartesian grid                        
  --cell_size                -cs   <arg> Cell size (nelx, nely, nelz ignored)                         
  --align                    -a          Automatically align geometry to grid                         
  --bbox_expand              -be   <arg> Expand tight bbox by percent                                 
  --input_mesh               -im   <arg> Input Base Exodus mesh                                       
  --input_mesh_blocks        -imb  <arg> Block ids of Input Base Exodus mesh                          
  --input_mesh_material      -imm  <arg> Material definition with input mesh                          
  --input_mesh_pamgen        -imp  <arg> Input Base mesh defined by Pamgen                            
  --join_parallel            -jp   <arg> Join parallel files                                          

Sculpt Command Summary
```

Example 2 (yaml):
```yaml
Command: nelx     Num cells in X in overlay Cartesian grid

Input file command:   nelx <arg>
Command line options: -x <arg>
Argument Type:        integer > 0
```

Example 3 (yaml):
```yaml
Command: nely     Num cells in Y in overlay Cartesian grid

Input file command:   nely <arg>
Command line options: -y <arg>
Argument Type:        integer > 0
```

Example 4 (yaml):
```yaml
Command: nelz     Num cells in Z in overlay Cartesian grid

Input file command:   nelz <arg>
Command line options: -z <arg>
Argument Type:        integer > 0
```

---

## Sculpt Process Control

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_process_control.htm

**Contents:**
- Sculpt Process Control
- Number of Processors
- Input File
- Debug Processor
- Debug Flag
- Quiet
- Print Input
- Version
- Threads Per Processor
- Number of processors in I

Options for controlling the execution of Sculpt. Sculpt is a parallel application that uses MPI to distribute and build the hex mesh on multiple processors. The -j or num_procs option is normally used to specify the number of processors to use. Sculpt will write a separate exodus file for each processor, which can be joined into a single file using the epu utility. While any number of processors may be used, you would normally use a -j value less than or equal to the number of cores available on your hardware.

Sculpt options can be specified directly from the command line using the "short" commands, or from an input file where the longer forms of the commands are used. Since an input file can be commented and modified, it is generally the recommended method for running Sculpt.

The number of processors that Sculpt will use to generate the mesh. For a structured, Cartesian base grid, the domain will be automatically divided into roughly equal sized rectangular regions based on this value.

For unstructured input (see --input_mesh), to utilize more than one processor, the base mesh must first be docomposed into the same number of regions specified by num_procs. The decomp tool, part of the Sandia, SEACAS tool suite can be used to break up an exodus mesh into multiple regions suitable for sculpt input.

An independent mesh of a portion of the domain is generated on each processor. Continuity across processor boundaries is maintained with MPI (Message Passing Interface). Each processor will write a separate Exodus II file to disk containing its portion of the domain. The Sandia SEACAS tool, epu can be used to join parallel files into a single file if desired.

If not specified on the command line, the number of processors used will be 1.

For additional control on the arrangement of processor domains on a Cartesian base grid, see arguments iproc, jproc, kproc.

Rather than specifying a complicated series of arguments on the command line, an input file may also be used. An input file is a simple text file containing all arguments and parameters to be used in the current sculpt run. Input files are normally expected to have a ".i" extension. Arguments used in the input file are limited to the Long Names indicated for each command.

User comments can also be made anywhere in the file but must follow a "$" sign. The argument assignments that are intended to be read must be contained within a "begin sculpt" and "end sculpt" block. All arguments may use upper or lower case and can optionally use "=" between the command and its parameter. The following is an example input file:

The following is an example of using an input file with sculpt:

Note that the number of processors (-j) should always be used on the command line and cannot be included in the input file. Relative or absolute paths for files may also be used.

Used for debugging. All processes will sleep until the designated process is attached to a debugger. Note: value of 0 corresponds to first processor, 1 to second, etc.

Used for debugging. Set flag to dump specific info based on the following:

0 (off) Default, No debug output

1 (lost_nodes) Dump processor lost node info

2 (non-manifold) Export Non-manifold resolution state as exodus file after each inner and outer iteration.

3 (defeature) Export Defeature state as exodus file after each inner and outer iteration.

4 (thickening) Export the Thickened st:wqate as exodus file after each material has been thickened.

5 (initial-projections) Turn off initial minimizer projection.

6 (reversal) Use Non-manifold reversal case

7 Combine debug_flag 5 and 6

8 (gq-color) Use guaranteed quality laplacian color smoothing

9 (gq-full) Combine debug_flags 5,6 and 8

10 (hostname) Display the host name for each processor

11 (test_large_global_IDs) starts the global node and element ID numbering at INT_MAX (2^31) for testing large_exodus option.

12 (use_bbox_for_unstructured) Use the xmin, ymin, ... options to limit the domain on an input_mesh

13 (allow_input_mesh_sidesets) Don't restrict use of gen_sidesets = 6, 7 or 9 if using parallel. (This may result in poor elements at proc boundaries). Quiet Command: quiet Suppress output Input file command: quiet Command line options: -qt Command Description: Suppress any output to the command line from Sculpt as it is running. Print Input Command: print_input Print input values and defaults then stop Input file command: print_input Command line options: -pi Command Description: Display all input parameters and defaults used in the current Sculpt run to the output window and then stop. No mesh (or volume fractions) will be generated. Version Command: version Print version number and exit Input file command: version Command line options: -vs Command Description: Prints Sculpt version information and exits. Threads Per Processor Command: threads_process Number of threads per process Input file command: threads_process <arg> Command line options: -tpp <arg> Argument Type: integer > 0 Command Description: This option is currently experimental and under development. Sculpt may use shared memory parallelism to improve performance. When built with the Kokkos library, some algorithms in sculpt will use shared memory parallel threads in addition to MPI distributed memory parallelism (MPI+X). Currently this option is implemented only for surface and volume Laplacian smoothing algorithms. This option may not be available requiring a custom build of sculpt to be used. Check with developers if you would like to use this option. Number of processors in I Command: iproc Number of processors in I direction Input file command: iproc <arg> Command line options: -ip <arg> Argument Type: integer > 0 Command Description: Arguments iproc, jproc and kproc provide user control over the processor decomposition in I, J, and K directions respectively. iproc * jproc * kproc must equal the number of processors specified on the command line using the -j option. In some cases, where it is known that significant refinement will be done in a localized region of the domain, it may be worth manually specifying the number of cell layers, or intervals that each processor will contain. This should provide rough processor load balacing so that regions with an expected large number of elements will have a smaller physical domain, but roughly similar element counts. This may avoid single processor memory limitations on large HPC machines. To specify processor intervals, optionally, the exact interval count in I, J, K directions should be specified. The number of intervals specfied for each direction should be the value of iproc, jproc, and kproc respectively. In addition, the sum of the intervals in each direction should equal the user specified nelx, nely and nelz values respectively. For example, for a 24 processor (-j 24) arrangement with nelx = nely = 28 and nelz = 27, one possible arrangment of processors would be as follows: nelx = 28 nely = 28 nelz = 27 iproc = 2 14 14 jproc = 2 14 14 kproc = 6 7 6 5 4 3 2 For this example the I and J directions are equally subdivided into 2 processors with 14 intervals in both directions. The K direction, however is subdivided into 6 processors, where the intervals are progressively thinner, starting with 7 intervals at the bottom (smallest z) and ending with 2 intervals at the top (largest z). Note that the number of intervals in any direction must always be at least 2 or greater. If processor intervals are omitted, Sculpt will attempt to roughly equally space the intervals in each direction. If at least one direction of intervals is detected in the input, then all directions should be specified. Note that this option is only available when using a Cartesian base grid specification and cannot be used with an unstructured base grid using the input_mesh option. Number of processors in J Command: jproc Number of processors in J direction Input file command: jproc <arg> Command line options: -jp <arg> Argument Type: integer > 0 Command Description: Arguments iproc, jproc and kproc provide user control over the processor decomposition in I, J, and K directions respectively. iproc * jproc * kproc must equal the number of processors specified on the command line using the -j option. In some cases, where it is known that significant refinement will be done in a localized region of the domain, it may be worth manually specifying the number of cell layers, or intervals that each processor will contain. This should provide rough processor load balacing so that regions with an expected large number of elements will have a smaller physical domain, but roughly similar element counts. This may avoid single processor memory limitations on large HPC machines. To specify processor intervals, optionally, the exact interval count in I, J, K directions should be specified. The number of intervals specfied for each direction should be the value of iproc, jproc, and kproc respectively. In addition, the sum of the intervals in each direction should equal the user specified nelx, nely and nelz values respectively. For example, for a 24 processor (-j 24) arrangement with nelx = nely = 28 and nelz = 27, one possible arrangment of processors would be as follows: nelx = 28 nely = 28 nelz = 27 iproc = 2 14 14 jproc = 2 14 14 kproc = 6 7 6 5 4 3 2 For this example the I and J directions are equally subdivided into 2 processors with 14 intervals in both directions. The K direction, however is subdivided into 6 processors, where the intervals are progressively thinner, starting with 7 intervals at the bottom (smallest z) and ending with 2 intervals at the top (largest z). Note that the number of intervals in any direction must always be at least 2 or greater. If processor intervals are omitted, Sculpt will attempt to roughly equally space the intervals in each direction. If at least one direction of intervals is detected in the input, then all directions should be specified. Note that this option is only available when using a Cartesian base grid specification and cannot be used with an unstructured base grid using the input_mesh option. Number of processors in K Command: kproc Number of processors in K direction Input file command: kproc <arg> Command line options: -kp <arg> Argument Type: integer > 0 Command Description: Arguments iproc, jproc and kproc provide user control over the processor decomposition in I, J, and K directions respectively. iproc * jproc * kproc must equal the number of processors specified on the command line using the -j option. In some cases, where it is known that significant refinement will be done in a localized region of the domain, it may be worth manually specifying the number of cell layers, or intervals that each processor will contain. This should provide rough processor load balacing so that regions with an expected large number of elements will have a smaller physical domain, but roughly similar element counts. This may avoid single processor memory limitations on large HPC machines. To specify processor intervals, optionally, the exact interval count in I, J, K directions should be specified. The number of intervals specfied for each direction should be the value of iproc, jproc, and kproc respectively. In addition, the sum of the intervals in each direction should equal the user specified nelx, nely and nelz values respectively. For example, for a 24 processor (-j 24) arrangement with nelx = nely = 28 and nelz = 27, one possible arrangment of processors would be as follows: nelx = 28 nely = 28 nelz = 27 iproc = 2 14 14 jproc = 2 14 14 kproc = 6 7 6 5 4 3 2 For this example the I and J directions are equally subdivided into 2 processors with 14 intervals in both directions. The K direction, however is subdivided into 6 processors, where the intervals are progressively thinner, starting with 7 intervals at the bottom (smallest z) and ending with 2 intervals at the top (largest z). Note that the number of intervals in any direction must always be at least 2 or greater. If processor intervals are omitted, Sculpt will attempt to roughly equally space the intervals in each direction. If at least one direction of intervals is detected in the input, then all directions should be specified. Note that this option is only available when using a Cartesian base grid specification and cannot be used with an unstructured base grid using the input_mesh option. Write the ghost layers for debug Command: build_ghosts Write ghost layers to exodus files for debug Input file command: build_ghosts Command line options: -bg Command Description: If set, this option will dump the ghost hexes at the boundaries of processor domains to the exodus files. This is used only for debugging. Volume Fraction Calculation Method Command: vfrac_method Set method for computing volume fractions Input file command: vfrac_method <arg> Command line options: -vm <arg> Argument Type: integer (1, 2, 3) Input arguments: cth (0) cth (1) r3d (2) winding (3) Command Description: Sets the method used for computing volume fractions from geometry input. Three options are currently available: CTH (1): The default method. It uses the CTH third party library from Sandia Laboratories for approximating intersections using an adaptive ray firing method to determine inside-outside status of multiple locations within a grid cell. This method can be used with STL and all valid primitive types defined by the diatom format. R3D (2): Uses the R3D third party library developed by Los Alamos Laboratories. Machine precision intersection calculations are performed to generate accurate volume fractions from the STL description. This method is valid for STL and diatom input packages specifying STL input files. Non STL format geometry defined in the diatom file will be ignored for this format. Winding (3): Uses the fast winding number from the igl third party library, which should gracefully handle non-watertight stl files. R&D is in progress.

Suppress any output to the command line from Sculpt as it is running.

Display all input parameters and defaults used in the current Sculpt run to the output window and then stop. No mesh (or volume fractions) will be generated.

Prints Sculpt version information and exits.

This option is currently experimental and under development. Sculpt may use shared memory parallelism to improve performance. When built with the Kokkos library, some algorithms in sculpt will use shared memory parallel threads in addition to MPI distributed memory parallelism (MPI+X). Currently this option is implemented only for surface and volume Laplacian smoothing algorithms. This option may not be available requiring a custom build of sculpt to be used. Check with developers if you would like to use this option.

Arguments iproc, jproc and kproc provide user control over the processor decomposition in I, J, and K directions respectively. iproc * jproc * kproc must equal the number of processors specified on the command line using the -j option. In some cases, where it is known that significant refinement will be done in a localized region of the domain, it may be worth manually specifying the number of cell layers, or intervals that each processor will contain. This should provide rough processor load balacing so that regions with an expected large number of elements will have a smaller physical domain, but roughly similar element counts. This may avoid single processor memory limitations on large HPC machines. To specify processor intervals, optionally, the exact interval count in I, J, K directions should be specified. The number of intervals specfied for each direction should be the value of iproc, jproc, and kproc respectively. In addition, the sum of the intervals in each direction should equal the user specified nelx, nely and nelz values respectively. For example, for a 24 processor (-j 24) arrangement with nelx = nely = 28 and nelz = 27, one possible arrangment of processors would be as follows: nelx = 28 nely = 28 nelz = 27 iproc = 2 14 14 jproc = 2 14 14 kproc = 6 7 6 5 4 3 2 For this example the I and J directions are equally subdivided into 2 processors with 14 intervals in both directions. The K direction, however is subdivided into 6 processors, where the intervals are progressively thinner, starting with 7 intervals at the bottom (smallest z) and ending with 2 intervals at the top (largest z). Note that the number of intervals in any direction must always be at least 2 or greater. If processor intervals are omitted, Sculpt will attempt to roughly equally space the intervals in each direction. If at least one direction of intervals is detected in the input, then all directions should be specified. Note that this option is only available when using a Cartesian base grid specification and cannot be used with an unstructured base grid using the input_mesh option.

Arguments iproc, jproc and kproc provide user control over the processor decomposition in I, J, and K directions respectively. iproc * jproc * kproc must equal the number of processors specified on the command line using the -j option. In some cases, where it is known that significant refinement will be done in a localized region of the domain, it may be worth manually specifying the number of cell layers, or intervals that each processor will contain. This should provide rough processor load balacing so that regions with an expected large number of elements will have a smaller physical domain, but roughly similar element counts. This may avoid single processor memory limitations on large HPC machines. To specify processor intervals, optionally, the exact interval count in I, J, K directions should be specified. The number of intervals specfied for each direction should be the value of iproc, jproc, and kproc respectively. In addition, the sum of the intervals in each direction should equal the user specified nelx, nely and nelz values respectively. For example, for a 24 processor (-j 24) arrangement with nelx = nely = 28 and nelz = 27, one possible arrangment of processors would be as follows: nelx = 28 nely = 28 nelz = 27 iproc = 2 14 14 jproc = 2 14 14 kproc = 6 7 6 5 4 3 2 For this example the I and J directions are equally subdivided into 2 processors with 14 intervals in both directions. The K direction, however is subdivided into 6 processors, where the intervals are progressively thinner, starting with 7 intervals at the bottom (smallest z) and ending with 2 intervals at the top (largest z). Note that the number of intervals in any direction must always be at least 2 or greater. If processor intervals are omitted, Sculpt will attempt to roughly equally space the intervals in each direction. If at least one direction of intervals is detected in the input, then all directions should be specified. Note that this option is only available when using a Cartesian base grid specification and cannot be used with an unstructured base grid using the input_mesh option.

Arguments iproc, jproc and kproc provide user control over the processor decomposition in I, J, and K directions respectively. iproc * jproc * kproc must equal the number of processors specified on the command line using the -j option. In some cases, where it is known that significant refinement will be done in a localized region of the domain, it may be worth manually specifying the number of cell layers, or intervals that each processor will contain. This should provide rough processor load balacing so that regions with an expected large number of elements will have a smaller physical domain, but roughly similar element counts. This may avoid single processor memory limitations on large HPC machines. To specify processor intervals, optionally, the exact interval count in I, J, K directions should be specified. The number of intervals specfied for each direction should be the value of iproc, jproc, and kproc respectively. In addition, the sum of the intervals in each direction should equal the user specified nelx, nely and nelz values respectively. For example, for a 24 processor (-j 24) arrangement with nelx = nely = 28 and nelz = 27, one possible arrangment of processors would be as follows: nelx = 28 nely = 28 nelz = 27 iproc = 2 14 14 jproc = 2 14 14 kproc = 6 7 6 5 4 3 2 For this example the I and J directions are equally subdivided into 2 processors with 14 intervals in both directions. The K direction, however is subdivided into 6 processors, where the intervals are progressively thinner, starting with 7 intervals at the bottom (smallest z) and ending with 2 intervals at the top (largest z). Note that the number of intervals in any direction must always be at least 2 or greater. If processor intervals are omitted, Sculpt will attempt to roughly equally space the intervals in each direction. If at least one direction of intervals is detected in the input, then all directions should be specified. Note that this option is only available when using a Cartesian base grid specification and cannot be used with an unstructured base grid using the input_mesh option.

If set, this option will dump the ghost hexes at the boundaries of processor domains to the exodus files. This is used only for debugging.

Sets the method used for computing volume fractions from geometry input. Three options are currently available:

CTH (1): The default method. It uses the CTH third party library from Sandia Laboratories for approximating intersections using an adaptive ray firing method to determine inside-outside status of multiple locations within a grid cell. This method can be used with STL and all valid primitive types defined by the diatom format.

R3D (2): Uses the R3D third party library developed by Los Alamos Laboratories. Machine precision intersection calculations are performed to generate accurate volume fractions from the STL description. This method is valid for STL and diatom input packages specifying STL input files. Non STL format geometry defined in the diatom file will be ignored for this format.

Winding (3): Uses the fast winding number from the igl third party library, which should gracefully handle non-watertight stl files. R&D is in progress.

**Examples:**

Example 1 (lua):
```lua
Process Control              -pc     --process
  --num_procs                -j    <arg> Number of processors requested                               
  --input_file               -i    <arg> File containing user input data                              
  --debug_processor          -D    <arg> Sleep to attach to processor for debug                       
  --debug_flag               -dbf  <arg> Dump debug info based on flag                                
  --quiet                    -qt         Suppress output                                              
  --print_input              -pi         Print input values and defaults then stop                    
  --version                  -vs         Print version number and exit                                
  --threads_process          -tpp  <arg> Number of threads per process                                
  --iproc                    -ip   <arg> Number of processors in I direction                          
  --jproc                    -jp   <arg> Number of processors in J direction                          
  --kproc                    -kp   <arg> Number of processors in K direction                          
  --build_ghosts             -bg         Write ghost layers to exodus files for debug                 
  --vfrac_method             -vm   <arg> Set method for computing volume fractions                    

Sculpt Command Summary
```

Example 2 (yaml):
```yaml
Command: num_procs     Number of processors requested

Input file command:   num_procs <arg>
Command line options: -j <arg>
Argument Type:        integer > 0
```

Example 3 (yaml):
```yaml
Command: input_file     File containing user input data

Input file command:   input_file <arg>
Command line options: -i <arg>
Argument Type:        file name with path
```

Example 4 (julia):
```julia
BEGIN SCULPT
    stl_file = "mygeom.stl"
    cell_size = 0.5
    exodus_file = "mymesh"
    mesh_void = true
  END SCULPT
```

---

## Sculpt Smoothing

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_smoothing.htm

**Contents:**
- Sculpt Smoothing
- Smooth
- Curve Smoothing
- Laplacian Iterations
- Maximum Optimization Iterations
- Optimization Threshold
- Curve Optimization Threshold
- Maximum Parallel Coloring Iterations
- Parallel Coloring Threshold
- Maximum Guaranteed Quality Iterations

Sculpt options for specifying how the mesh will be smoothed following mesh generation.

Sculpt includes a tiered approach to smoothing to improve element quality. It starts by applying smoothing to all nodes in the mesh and progressively restricts the smoothing operations to only those nodes that fall below a user-defined scaled Jacobian threshold. Default numbers of iterations and thresholds for each smoothing phase have been tuned for general use, however it may be worthwhile to adjust these parameters. The three smoothing phases include:

Automatic adjustment of node locations following meshing to improve element quality. Controls the combined Laplacian and optimization smoothing procedures applied to volume and surface nodes (see csmooth for curve smoothing options) Uses the laplacian_iters, max_opt_iters, opt_threshold, max_pcol_iters, pcol_threshold, mqx_gq_iters and gq_threshold arguments to control the sensitivity and aggressiveness of the smoothing operations. In most cases, the default options for these parameters are sufficient, however increasing iterations or threshold values, while potentially causing longer run times, may result in improved mesh quality.

Smoothing will adjust the location of nodes on surfaces, projecting them to an approximated surface representation defined by interface reconstruction from volume fractions. In addition to turning smoothing on and off, the surface projection characteristics can be adjusted using the bbox_fixed and no_surface_projections options.

Boundary Buffer Improvement: Sculpt's smoothing procedures will use an automatic boundary buffer improvement method. It will attempt to improve the quality of hexes where interior surfaces are close to tangent with the bounding box. This can result in nodes that may not lie precisely on the planes of the domain boundary. The fixed_bbox (2) and no_surface_projections (3) options will turn off the automatic boundary buffer improvement.

The csmooth option controls the smoothing method used on curves. In most cases the default should be sufficient, however it may be useful to experiment with different options. The default curve smoothing option is vfrac (5). The following curve smoothing options are available:

Number of Laplacian smoothing iterations performed when Hybrid smoothing option is used. Default value is 2.

Indicates the maximum number of iterations of optimization-based smoothing to perform. May complete sooner if no further improvement can be made. Default is 5

Indicates the value for scaled Jacobian where Optimization smoothing will be performed. Elements with scaled Jacobian less than opt_threshold and their neighbors will be smoothed. Default value is 0.6

Indicates the value for scaled Jacobian where if a node that falls on a curve has neighboring quads less than this value, then the smoothing will no longer honor the curve definition. Instead the optimization smoother will attempt to place the node to optimize the neighboring mesh quality, without regard for its placement on its owning curve.

Normally this value should be set close to zero to avoid too many nodes from floating off of their owning curves, however, if mesh quality is constrained by curve geometry, setting this value higher can help to avoid bad or poor quality elements. Default for this value is 0.1.

Maximum number of spot smoothing (also known as parallel coloring) iterations to perform. May complete sooner if no further improvement can be made. Default is 100. See also pcol_threshold.

Indicates scaled Jacobian threshold for spot smoothing (also known as parallel coloring). A parallel coloring algorithm is used to uniquely identify and isolate nodes to be improved using optimization. Default is 0.2.

Maximum number of guaranteed quality smoothing iterations to perform. Guaranteed quality smoothing performs a constrained Laplacian smoothing algorithm to adjust node locations. If the result of a smoothing operation results in adjacent element quality falling below the specified gq_threshold value, then move distance is cut until minimum threshold is achieved or the metric is improved. To achieve parallel consistency, a parallel coloring methodology is employed. The max_gq_iters defines the maximum number of parallel color iterations employed. Default is 0 (off).

Note that guaranteed quality can be utilized in conjunction with other smoothing methods (Laplacian, Optimization and Parallel Coloring), however to be effective it is normally used independent from other smoothing. For example, to use guaranteed quality the following is suggested:

Indicates scaled Jacobian threshold for guaranteed quality smoothing. Default is 0.2. see also max_gq_iters

Used only in conjunction with the smooth = geo_smooth option. It controls the maximum distance any individual node can deviate from the geometry definition. If a smoothing operation computes a location that will move a node further than the prescribed geo_smooth_max_deviation value from the geometry, the node movement will be artificially limited by this value. If not specificied, no limitations will be placed on node movement due to smoothing operations when the smooth = geo_smooth is used. A value of zero (0) will constrain all nodes at interfaces to lie on the geometry, similar to the smooth = to_geometry option. When using this option, the maximum deviation from the geometry for any individual node will be reported in the MESH SUMMARY in the Sculpt ouput.

**Examples:**

Example 1 (typescript):
```typescript
Smoothing                    -smo     --smoothing
  --smooth                   -S    <arg> Smoothing method                                             
  --csmooth                  -CS   <arg> Curve smoothing method                                       
  --laplacian_iters          -LI   <arg> Number of Laplacian smoothing iterations                     
  --max_opt_iters            -OI   <arg> Max. number of parallel Jacobi opt. iters.                   
  --opt_threshold            -OT   <arg> Stopping criteria for Jacobi opt. smoothing                  
  --curve_opt_thresh         -COT  <arg> Min metric at which curves won't be honored                  
  --max_pcol_iters           -CI   <arg> Max. number of parallel coloring smooth iters.               
  --pcol_threshold           -CT   <arg> Stopping criteria for parallel color smooth                  
  --max_gq_iters             -GQI  <arg> Max. number of guaranteed quality smooth iters.              
  --gq_threshold             -GQT  <arg> Guaranteed quality minimum SJ threshold                      
  --geo_smooth_max_deviation -GSM  <arg> Geo Smoothing Maximum Deviation                              

Sculpt Command Summary
```

Example 2 (yaml):
```yaml
Command: smooth     Smoothing method

Input file command:   smooth <arg>
Command line options: -S <arg>
Argument Type:        integer (0, 1, 2, 3) 
Input arguments: off (0)
                 default (1)
                 on (1)
                 fixed_bbox (2)
                 no_surface_projections (3)
                 to_geometry (4)
                 to_geom (4)
                 geo_smooth (5)
                 geometry_smoothing (5)
                 geo_smoothing (5)
```

Example 3 (lua):
```lua
Command: csmooth     Curve smoothing method

Input file command:   csmooth <arg>
Command line options: -CS <arg>
Argument Type:        integer (0, 1, 2, ...6) 
Input arguments: off (0)
                 circle (1)
                 hermite (2)
                 average_tangent (3)
                 neighbor_surface_normal (4)
                 vfrac (5)
                 linear (6)
```

Example 4 (yaml):
```yaml
Command: laplacian_iters     Number of Laplacian smoothing iterations

Input file command:   laplacian_iters <arg>
Command line options: -LI <arg>
Argument Type:        integer >= 0
```

---

## Sculpt Technical Description

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/parallel/sculpt_tech.htm

**Contents:**
- Sculpt Technical Description
- References

This document provides a brief technical overview of the Sculpt application, a separate companion application to Cubit designed to generate all-hex meshes of complex geometries. Details on command arguments to Sculpt may be found here. Also information for using Cubit to set up input for Sculpt may be found here.

The method for generating an all-hex mesh employed by Sculpt is often referred to in the literature as an overlay-grid or mesh-first method. This differs significantly from the algorithms employed by Sweeping and Mapping, which are classified as geometry-first methods. Mapping and Sweeping start with the geometry, carefully fitting logical groupings of hexes to conform to a recognized topology. In contrast, the Sculpt method begins with a base Cartesian grid encompassing the geometry which is used as the basis for the mesh. Geometric features are carved or sculpted from the Cartesian grid and boundaries smoothed to create the final hex mesh. The obvious benefit of the Sculpt (mesh-first) method over Mapping and Sweeping (geometry-first) methods is there is no need to decompose the geometry into mappable or sweebable components, a process that can often be very time consuming, tedious and sometimes impossible. Input to Sculpt can be any geometry regardless of features and complexity.

The basic Sculpt procedure is illustrated in figure 1. Beginning with a Cartesian grid as the base mesh, shown in figure 1(a), a geometric description is imposed. Nodes from the base grid that are near the boundaries are projected to the geometry, locally distorting the nearby hex cells (figure 1(b)). A pillow layer of hexes is then inserted at the surfaces by duplicating the interface nodes on either side of the boundaries and inserting hexes (figures 1(c) and (d)). While constraining node locations to remain on the interfaces, smoothing procedures can now be employed to improve mesh quality of nearby hexes (figure 1(e)).

Figure 1. The procedure for generating a hex mesh using the Sculpt overlay grid method

Sculpt is limited to capturing geometric features with the available resolution of the selected base mesh. Because of this, care should be taken in selecting an appropriate cell size. In addition, no attempt is made by the Sculpt procedure to capture sharp exterior features. Figure 2 shows an example of a sculpt mesh of a CAD model. Note that exterior corner features are rounded, however the effect of sharp feature capture becomes less pronounced as resolution increases as demonstrated in figures 3(a) and (b).

Figure 2. Hex mesh generated using the Sculpt overlay grid procedure Figure 3. Examples of the same model meshed at two different resolutions showing a cutaway view of the mesh.

Another aspect of model preparation for computational simulation involves geometry cleanup and simplification. In most cases, geometry-first methods, such as Sweeping, require an accurate non-manifold boundary representation before mesh generation can begin. Small, sometimes unseen gaps, overlaps and misalignments can result in sliver elements or mesh failure. Tedious manual geometry simplification and manipulation is often required before meshing can commence. Sculpt, however employs a solution that avoids much of the geometry inaccuracy issues inherent in CAD design models. Using a faceted representation of the solid model, a voxel-based volume fraction representation is generated. Figure 4 illustrates the procedure where a CAD model serving as input (figure 4(a)) is processed by a procedure that will generate volume fraction scalar data for each cell of an overlay Cartesian grid (figure 4(b)). One value per material per cell is computed that represents the volume fraction of material filling the cell. A secondary geometry representation is then extracted using an interface tracking technique from which the final hex mesh is generated (figure 4(c)). While similar to its initial facet-based representation, the new secondary geometry description developed from the volume fraction data results in a simplified model that tends to wash over small features and inaccuracies that are smaller than the resolution of the base cell size.

Figure 4. A representation of the procedure used to generate a hex mesh with Sculpt using Volume Fractions.

While acknowledging some loss in model fidelity in this new volume-fraction based geometric model, the advantage and time-savings to the analyst of being able to ignore troublesome geometry issues is enormous. At the same time it may be important to understand what the additional discrete approximations will make to solution accuracy and employ relevant engineering judgement in the use of this technology.

The following technical papers, written by the author of Sculpt, describe the Sculpt procedure in more depth. These papers were presented at the International Meshing Roundtable and are external links to pdf documents.

Parallel Hex Meshing from Volume Fractions: Describes the basic algorithms and mathematics used in the Sculpt procedure.

Parallel Smoothing for Grid-Based Methods: A brief description of the smoothing procedures used in Sculpt.

Validation of Grid-Based Hex Meshes with Computational Solid Mechanics: Describes a study where computational results from Sculpt meshes are compared with Sweep meshes using the Sierra Solid Mechanics Tool as a comparison.

A Template-Based Approach for Parallel Hexahedral Two-Refinement: Describes the refinement procedures used for generating adapted Sculpt meshes.

---

## Skinning a Mesh

**URL:** https://coreform.com/cubit_help/mesh_generation/skin.htm

**Contents:**
- Skinning a Mesh

Skin {Block|Volume} <range> [Individual] [Nomake]

Skin {Element|Hex|Tet|Wedge|Pyramid|Face|Tri|Block|Volume} <range> [Nomake]

Skin {Element|Hex|Tet|Wedge|Pyramid|Face|Tri|Block|Volume} <range> [Make {Block|Sideset [<id>] |Group [<name>|<id>]}

Skin {Element|Hex|Tet|Wedge|Pyramid|Face|Tri|Block|Volume} <range> {Add|Replace} {Block|Sideset [<id>] |Group [<name>|<id>]}

The Individual keyword tells Cubit to skin Blocks or Volumes, one by one independently of each other, even if they share merged surfaces.

The Nomake keyword tells Cubit to not create any kind of grouping of the mesh faces resulting from the skinning operation.

If the Make option and its arguments are present, then the specified object (block, sideset or group) receives the skin mesh. The command fails if an object with the optional identifier already exists. If the object identifier is omitted, the identifier is set to the next object of that type. The skin mesh is stored in the next available sideset if the Make option is missing.

Another command form has two options, Add and Replace. Each option has a required, associated identifier. If the identifier is missing or invalid, the command fails. The Add option appends the skin mesh to the object. The Replace option removes any existing mesh from the object before adding the skin mesh.

The skin mesh will respect the merged volumes. If two adjacent volumes are merged, the skin mesh will not include the merged surface. If the volumes are not merged, each volume will generate a separate skin surface. If volumes are not merged, they are treated separately. The skin command will also respect any number of interior voids. All surface elements will be oriented forward with respect to the originating volumes.

The primary use for the skin command is to generate surface meshes of quads or tris for sidesets and remeshing.

For Face and Tri elements (2d elements), the skin is a set of edges (1d elements.) The skin for 3d elements is a set of 2d elements.

---

## Smart Laplacian

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/smart_laplacian.htm

**Contents:**
- Smart Laplacian

Applies to: Surface and Volume meshes

Summary: Tries to make equal edge lengths while ensuring no degradation in element shape

{Surface|Volume} <range> Smooth Scheme Smart Laplacian

The Smart Laplacian smoothing approach is a variation on the standard Laplacian algorithm. The algorithm iteratively loops over the mesh and updates nodes based on the location of their neighbors. First, a patch of elements is formed around a given node. The quality of this patch is assessed to determine the quality of the worst shaped element. Then a new candidate node position is calculated as the average of the neighboring nodes. The quality of the patch is assessed again using the candidate node position. If there has been no degradation in the quality of the elements in the patch, the candidate node position is accepted; otherwise, the candidate node position is rejected and the node is returned to its previous position.

The Smart Laplacian smoother is intended to provide a reliable smoother that is nearly as fast as the Length-Weighted Laplacian smoother. Due to the dual goals of this smoother, making equal edge length and improving element shape, it will not always be able to make progress. However, it is often useful as a quick alternative to the more time-consuming optimization methods like Mean Ratio or Condition Number. When this smoother fails to make significant progress, the optimization methods can be tried.

The Smart Laplacian Smoother uses the Mean Ratio quality measure to assess element shape. This smoother is ensuring no degradation in the minimum Mean Ratio. The Mean Ratio smoother is optimizing the same metric, but it is attempting to improve the average Mean Ratio quality.

---

## Source Surface Anisotropic Sizing Function

**URL:** https://coreform.com/cubit_help/mesh_generation/adaptivity_and_sizing_functions/anisotropic_sizing_function.htm

**Contents:**
- Source Surface Anisotropic Sizing Function

The Source Surface Anisotropic Sizing Function, generates a tensor field based upon the geometric shape of the given surfaces, which can be used to generate anisotropic tet elements. This sizing function supports 2 factors for anisotropy. Additionally, if the specified surfaces are cylindrical or conical, 3 factors for anisotropy are supported. If multiple surfaces are given, a sizing tensor at a location in the field is defined by the closest surface.

For anisotropy with 2 factors, one factor is applied in the direction normal to a surface, and the other factor is applied in the orthogonal directions. For anisotropy with 3 factors, one factor is applied in the direction normal to a surface, and one factor is applied in the direction of the axis for The cylindrical surface, and the third factor is applied in the direction orthogonal to the first 2 directions.

The following command is used to generate an anisotropic tensor field:

Volume <range> Sizing Function Source Surface <id> Near <size> [theta <size> | Theta_interval <count> [Theta_axis <axis>]] Growth_factor <factor>

The Near size is the factor applied in the direction normal to the surface The optional Theta size is the factor applied in the direction of the cylindrical surface axis The optional Theta_interval count is the number of elements to create in the direction of the cylindrical surface axis The optional Theta_axis axis provides the axis for a cylindrical surface as an alternative to computing one from the input surface The Growth_factor is the rate of change in the Near size as the location moves away from the surface The factors not specified above will come from the size applied to the volume.

Below are a couple examples of using this anisotropic sizing function.

The following example uses 2 size factors to create an anisotropic tensor field. Figure 1: Anistropy from 2 source surfaces volume 1 size 0.03 volume 1 sizing function source surface 7 8 near 0.003 growth .2 volume 1 scheme tetmesh mesh volume 1 The following example uses 3 size factors to create an anisotropic tensor field. Figure 2: Anistropy from 1 source surface create Cylinder height 0.05 radius 0.1 create Cylinder height 0.05 radius 0.08 subtract volume 2 from volume 1 volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

Figure 1: Anistropy from 2 source surfaces

volume 1 size 0.03 volume 1 sizing function source surface 7 8 near 0.003 growth .2 volume 1 scheme tetmesh mesh volume 1 The following example uses 3 size factors to create an anisotropic tensor field. Figure 2: Anistropy from 1 source surface create Cylinder height 0.05 radius 0.1 create Cylinder height 0.05 radius 0.08 subtract volume 2 from volume 1 volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

volume 1 sizing function source surface 7 8 near 0.003 growth .2 volume 1 scheme tetmesh mesh volume 1 The following example uses 3 size factors to create an anisotropic tensor field. Figure 2: Anistropy from 1 source surface create Cylinder height 0.05 radius 0.1 create Cylinder height 0.05 radius 0.08 subtract volume 2 from volume 1 volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

volume 1 scheme tetmesh mesh volume 1 The following example uses 3 size factors to create an anisotropic tensor field. Figure 2: Anistropy from 1 source surface create Cylinder height 0.05 radius 0.1 create Cylinder height 0.05 radius 0.08 subtract volume 2 from volume 1 volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

The following example uses 3 size factors to create an anisotropic tensor field. Figure 2: Anistropy from 1 source surface create Cylinder height 0.05 radius 0.1 create Cylinder height 0.05 radius 0.08 subtract volume 2 from volume 1 volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

Figure 2: Anistropy from 1 source surface

create Cylinder height 0.05 radius 0.1 create Cylinder height 0.05 radius 0.08 subtract volume 2 from volume 1 volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

create Cylinder height 0.05 radius 0.08 subtract volume 2 from volume 1 volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

subtract volume 2 from volume 1 volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

volume 1 scheme tetmesh volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

volume 1 size 0.01 Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

Volume 1 Sizing Function Source Surface 1 7 Near 0.004 theta 0.025 Growth_factor 0.01 mesh surface all

---

## Sphere

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/sphere.htm

**Contents:**
- Sphere

Applies to: Volumes topologically equivalent to a sphere and having one surface.

Summary: Generates a radially-graded hex mesh on a spherical volume.

Volume <range> Scheme Sphere [Graded_interval <int>] [Az_interval <int>] [Bias <val>] [Fraction <val>] [Max_smooth_iterations <int=2>]

This scheme generates a radially-graded mesh on a spherical volume having a single bounding surface. The mesh is a straightforward generalization of the circle scheme for surfaces. The mesh consists of an inner region and an outer region. The inner region is a mapped mesh of a cube and the outer region contains fronts that trasition from the cube surface to the sphere surface. The following describes the parameters that control the sphere mesh.

The number of intervals in the outer region from the inner mapped mesh to the surface of the sphere is controlled by the graded_interval input parameter. Azimuthal mesh lines in the outer portion of the sphere will have approximately constant radius. If graded_interval is not specified, a default number of intervals will be computed based on the interval size value assigned to the sphere volume.

The number of azimuthal intervals around the equator is controlled by the az_interval input parameter. To maintain symmetry, the az_interval will be rounded to the nearest multiple of 8.

If az_interval is not specified, a default number of intervals will be computed either based on the the the interval value or on the mesh size value assigned to the volume. If the interval value is set (volume 1 interval 40, for example), the interval value will be used to define the number of azimuthal intervals. Otherwise, the mesh size will be used as the approximate size for elements on the inner mapped mesh.

The bias parameter controls the amount of radial grading in the outer region of the mesh from the inner mapped mesh to the sphere surface. A bias = 1 will results in equal size intervals, while a bias < 1 will generate smaller intervals towards the sphere interior and a bias > 1 will generate smaller elements towards the sphere surface. If the bias parameter is not specified, a default bias will be computed so that element size gradually increases from the inner mapped mesh to the sphere surface. The default bias value will also be based on the interval size assigned to the sphere volume as it attempts to maintain approximately isotropic elements throughout the sphere.

The fraction parameter (between 0 and 1) determines what fraction of the sphere is occupied by the inner mapped mesh. The fraction is defined as ratio of the diagonal of the cube containing the mapped mesh to sphere's diameter. The default value for fraction is 0.5. Interval sizes in the inner mapped mesh are normally constrained by the az_intervals. If az_intervals are not specified, element sizes in this region will be based upon the interval size assigned to the sphere volume.

Max_smooth_iterations:

The Max_smooth_iterations parameter determines the number of smoothing iterations following initial definition of the sphere mesh. By default, the number of smoothing interations is set to 0, which will result in a symmetric mesh. Note that smoothing can improve the quality of the mesh, however, it may disturb the bias and fraction. When bias and fraction are critical then smoothing iterations should be set to 0.

SPHERE MESH: fraction 0.3 graded_interval 6 az_interval 40 bias 0.8 max_smooth_iterations 0

BIAS (uniform): fraction 0.3 graded_interval 6 az_interval 40 bias 1.0 max_smooth_iterations 0

FRACTION: fraction 0.7 graded_interval 6 az_interval 40 bias 1.0 max_smooth_iterations 0

INTERVAL: fraction 0.7 graded_interval 9 az_interval 40 bias 1.0 max_smooth_iterations 0

SMOOTHING: fraction 0.7 graded_interval 9 az_interval 40 bias 1.0 max_smooth_iterations 2

AZIMUTHAL (mesh coarseness): fraction 0.7 graded_interval 5 az_interval 32 bias 1.0 max_smooth_iterations 2

BIAS (graded): fraction 0.9 graded_interval 9 az_interval 32 bias 1.5 max_smooth_iterations 0

---

## STransition

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/stransition.htm

**Contents:**
- STransition

Surface <surface_id_range> Scheme STransition [Triangle] [Coarse]

The STransition scheme transitions a mesh from one element density to another across a surface. This scheme is particularly helpful when the Paving scheme produces a poor mesh. The following two figures show a specific case where the STransition scheme may offer an improvement.

The coarse option forces the mesh to transition to a coarser mesh in the first layer.

For triangular surfaces, the STransition scheme with the triangle option will produce similar results when compared to the Triprimitive scheme. However, STransition is capable of handling more varied interval settings. The following triangle fails when using the Triprimitive scheme but succeeds with the STransition scheme.

The figures below show the STransition meshing scheme response to different shapes and interval settings.

The user also has the option of specifying END or SIDE surface vertex types.

Note, that the Centroid Area Pull smoothing algorithm sometimes gives better results than the default Winslow smoothing algorithm for STransition meshes.

---

## Stretch

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/stretch.htm

**Contents:**
- Stretch

Summary: Permits user to specify the exact size of the first and/or last edges on a curve.

Curve <range> Scheme Stretch [First_size <double>] [Last_size <double>] [Start Vertex <id>]

Curve <range> Scheme Stretch [Stretch_factor <double>] [Start Vertex <id>]

Scheme Bias and Dualbias.

This scheme allows the user to specify the exact length of the first and/or last edge on a curve mesh. Intermediate edge lengths will vary smoothly between these input values. Reasonable values for these parameters should be used (for example, the sizes must be less than the total length of the curve). If last_size is input, first_size must be input also. If stretch_factor is input, neither first_size nor last_size can be input. This scheme does not currently work on periodic curves.

---

## Submap

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/submap.htm

**Contents:**
- Submap

Applies to: Surfaces, Volumes

Summary: Produces a structured mesh for surfaces/volumes with more than 4/6 logical sides

{Surface|Volume} <range> Scheme Submap

{Surface|Volume} <range> Submap Smooth <on|off>

Submapping (Whiteley, 96) is a meshing tool based on the surface mapping capability discussed previously, and is suited for mesh generation on surfaces which can be decomposed into mappable subsurfaces. This algorithm uses a decomposition method to break the surface into simple mappable regions. Submapping is not limited by the number of logical sides in the geometry or by the number of edges. The submap tool, however is best suited for surfaces and volumes that are fairly blocky or that contain interior angles that are close to multiples of 90 degrees.

An example of a volume and its surfaces meshed with submapping is shown in Figure 1.

Figure 1. Quadrilateral and Hexahedral meshes generated by submapping

Like the mapping scheme, submapping uses vertex types to determine where to put the corners of the mapped mesh (See Surface Vertex Types). For surface submapping, curves on the surface are traversed and grouped into " logical sides " by a classification of the curves position in a local "i-j" coordinate system.

Volume submapping uses the logical sides for the bounding surfaces and the vertex types to construct a logical "i-j-k" coordinate system, which is used to construct the logical sides of the volume. For surface and volume submapping, the sides are used to formulate the interval constraints for the surface or volume.

Figure 2 shows an example of this logical classification technique, where the edges on the front surface have been classified in the i-j coordinate system; the figure also shows the submapped mesh for that volume.

Figure 2. Scheme Submap Logical Properties

In special cases where quick results are desired, submap cornerpicking can be set to OFF. The corner picking will be accomplished by a faster, but less accurate algorithm which sets the vertex types by the measured interior angle at the given vertex on the surface. In most cases this is not recommended.

Set Submap CornerPicking {ON|off}

In special cases where 4 corners will be selected for a four-sided mapped region, but the region has more than 4 reasonable locations for the 4 corners, one may choose between the submapping or mapping corner picking algorithms to determine the 4 locations for 4 corners. In most cases this is not recommended. The following commands may be used.

Set Cornerpicking_MapAsSubmap {on|OFF}

Set Cornerpicking_SubmapAsMap {on|OFF}

List Cornerpicking_MapAsSubmap

List Cornerpicking_SubmapAsMap

After submapping has subdivided the surface and applied the mapped meshing technique mentioned above, the mesh is smoothed to improve mesh quality. Because the decomposition performed by submapping is mesh based, no geometry is created in the process and the resulting interior mesh can be smoothed. Sometimes smoothing can decrease the quality of the mesh; in this case the following command can turn off the automatic smoothing before meshing:

{Surface|Volume} <range> Submap Smooth <on|off>

Surface submapping also has the ability to mesh periodic surfaces such as cylinders. An example of a periodic surface meshed with submapping is shown in Figure 3. The requirement for meshing these surfaces is that the top and bottom of the cylinder must have matching intervals.

Figure 3. Periodic Surface Meshing with Submapping

For periodic surfaces, there are no curves connecting the top and bottom of the cylinder. Setting intervals in this direction on the surface can be done by setting the periodic interval for that surface (see Interval Assignment). No special commands need to be given to submap a periodic surface, the algorithm will automatically detect the fact that the surface is periodic. Currently, periodic surfaces with interior holes are not supported.

---

## Super Sizing Function

**URL:** https://coreform.com/cubit_help/appendix/alpha/super_sizing.htm

**Contents:**
- Super Sizing Function

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

The Super sizing function computes both the Curvature and the Linear function and takes the smaller value of the two. This is an alpha feature and should be used with caution. The following is an example of Super element sizing.

Figure 1. NURB mesh with super sizing function, 34 by 16 density

---

## Surface Vertex Types

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/surface_vertex_types.htm

**Contents:**
- Surface Vertex Types
- Surface Vertex Commands
- Listing and Drawing Vertex Types
- Triangle Vertex Types
- Adjusting the Automatic Vertex Type Selection Algorithm
- Volume Curve Types

Several meshing algorithms in CUBIT "classify" the vertices of a surface or volume to produce a high quality mesh. This classification is based on the angle between the edges meeting at the vertex, and helps determine where to place the corners of the map, submap or trimesh, or the triangles in the trimap or tripave schemes. For example, a surface mapping algorithm must identify the four vertices of the surface that best represent the surface as a rectangle. Figure 1 illustrates the vertex angle types for mapped and submapped surfaces, and the correspondence between vertex types and the placement of corners in a mapped or submapped mesh.

Figure 1. Angle Types for Mapped and Submapped Surfaces: An End vertex is contained in one element, a Side vertex two, a Corner three, and a Reversal four.

The surface vertex type is computed automatically during meshing, but can also be specified manually. In some cases, choosing vertex types manually results in a better quality mesh or a mesh that is preferable to the user. Vertex types can be specified directly as End, Side, Corner, or Reversal, or can be specified by giving the desired interior angle as 90, 180, 270, or 360, respectively.

Vertex types have a firmness, just as meshing schemes do. Automatically selected vertex types are soft, while user-set vertex types are hard.

Vertex types are set using the following commands:

Surface <surface_id> [Vertex <vertex_id_range> [Loop_index <int>]] Type {End|Side|Corner|Reversal}

Surface <surface_id> [Vertex [<vertex_id_range> [Loop_index <int>]] Angle <value>

Surface <surface_id> [Vertex <vertex_id_range> [Loop_index <int>]] Type {Default|Soft|Hard}

If no vertices are specified, the command is applied to all vertices of each surface.

Note that a vertex may be connected to several surfaces and its classification can be different for each of those surfaces.

The influence of vertex types when mapping or submapping a surface is illustrated in Figure 2. There, the same surface is submapped in two different ways by adjusting the vertex types of ten vertices.

Figure 2. Influence of vertex types on submap meshes; vertices whose types are changed are indicated above, along with the mesh produced; logical submap shape shown below.

The loop_index is an advanced option used only for vertices where the boundary of a single surface passes through the same vertex more than once. This case is not common. If no loop index is specified for such a vertex, the specified vertex type is assigned to all occurrences of the vertex. The loop index for a specific occurrence of a vertex can be determined by listing the surface (list surface <id>) to show the list of curves in each loop bounding the surface, with the start and end vertex listed for each curve. The loop index begins at zero for the first curve in the first loop, and is incremented by one for subsequent curves through the last curve in the last loop. The loop index values corresponding to a specific vertex will be the loop index of each curve whose start vertex is the desired vertex.

Listing a surface lists the types of the vertices. The vertex type settings may also be drawn with the following commands:

Draw Surface <surface_id_range> {Vertex Angle|Vertex Type}

For a surface that will be meshed with scheme trimap or tripave, the user may specify the angle below which triangles are inserted:

Surface <surface_id_range> Angle <angle>

The user may also set whether to add a triangle at a particular vertex:

Surface <surface_id> [Vertex <vertex_id_range> [Loop_index <int>]] Type {Triangle|Nontriangle}

The user may specify the maximum allowable angle at a corner with the following command:

Set {Corner|End} Angle <degrees>

The user may also give greater priority to one automatic selection criteria over the others by changing the following absolute weights. The corner weight considers how large angles are at corners. The turn weight considers how L-shaped the surface is. The interval weight considers how much intervals must change. The large angle weight affects only auto-scheme selection: surfaces with a large angle will be paved instead. Each weight's default is 1 and must be between 0 and 10. The bigger a weight the more that criteria is considered.

Set Corner Weight <value>

Set Turn Weight <value>

Set Interval Weight <value>

Set Large Angle Weight <value>

An illustration of a mesh produced by the submapping algorithm is shown in Figure 2. The meshes produced by submapping on the left and right result from adjusting the vertex types of the eight vertices shown.

When sweeping, a 2.5 dimensional meshing scheme, curves perpendicular to the sweep direction can have a type with respect to the volume. These types are usually automatically selected. The following commands are useful:

Draw Volume <surface_id_range> {Curve Angle|Curve Type}

List Volume <volume_id> Curve Type

Volume <volume_id> [Curve <curve_id_range>] Type {End|Side|Corner|Reversal}

Volume <volume_id> [Curve <curve_id_range>] Type {Default|Soft|Hard}

---

## Sweep

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/sweep.htm

**Contents:**
- Sweep
- Multisweep
- Grouping Sweepable Volumes
- Node Redistribution

Summary: Produces an extruded hexahedral mesh for 2.5D volumes.

Volume <range> Scheme Sweep [Source [Surface] <range>] [Target [Surface] <range>] [Propagate bias] [Sweep smooth {auto | smart affine | linear | residual | winslow} ] [Sweep transform {LEAST SQUARES | Translate}] [Autosmooth target {ON|off} ]

Volume <range> Scheme Sweep Vector <xval yval zval>

Volume <range> autosmooth target [off|ON]

fixed imprints [on|OFF]

smart smooth [ON|off] tolerance <val 0.0 to 1.0=0.2>

Set Multisweep [On|Off]

Multisweep Smoothing {ON|Off}

Multisweep Volume <range> Remove

Volume <range> Redistribute Nodes {ON|off}

[Set] Legacy Sweeper {On|Off}

The sweep algorithm can sweep general 2.5D geometries and can also do pure translation or rotations. A 2.5D geometry is characterized by source and target surfaces which are topologically similar. The hexahedral mesh is swept (extruded) between source and target along a single logical axis. Bounding the swept hexahedra between source and target surfaces, are the linking surfaces. Figures 1 and 2 show examples of source, target and linking surfaces.

Command Options: The user can specify the source and target surfaces. The user can also specify a geometric vector approximating the sweep direction, and let CUBIT determine the source and target surfaces. The user can specify just the source surfaces, and let cubit guess the target, or "scheme auto" can also be used.

Figure 1. Sweep Volume Meshing

Figure 2. Multiple Linking Surface Volume Meshing with Scheme Sweep

In general, the procedure for using the sweep scheme is to first mesh the source surfaces. Any surface meshing scheme may be employed. Figure 1 displays swept meshes involving mapped and paved source surfaces. Linking surfaces must have either mapping or submapping schemes applied. The sweep algorithm can also handle multiple surfaces linking the source surface and the target surfaces. An example of this is shown in Figure 2. Note that for the multiple- linking-surface meshing case, the interval requirement is that the total number of intervals along each multiple edge path from the source surface to the target surface must be the same for each path. Once the appropriate mesh is applied to the source surface and intervals assigned, the mesh command may be issued.

In many cases auto-scheme selection can simplify this process by recognizing sweepable geometries and automatically select source and target surfaces. If the source and target surfaces are not specified, CUBIT attempts to automatically select them. CUBIT also automatically sets curve and vertex types in an attempt to make the mesh of the linking surfaces lead from a source surface to a target surface. These automatic selections may occasionally fail, in which case the user must manually select the source/target surfaces, or some of the curve and vertex types. After making some of these changes, the user should again set the volume scheme to sweep and attempt to mesh. In some cases of 1-1 sweeps, the source and target are swapped. Precedence for which surface to use as the source is {meshed, merged, specified as source}. If the user wants to avoid swaps and enforce that a particular surface is the source, then they can mesh that prior to sweeping.

Occasionally the user must also adjust intervals along curves, in addition to the usual surface interval matching requirements. For a given pair of source/target surfaces, there must be the same number of hexahedral layers between them regardless of the path taken. This constrains the number of edges along curves of linking surfaces. For example, in Figure 1 right, the number of intervals through the holes must be the same as along the outer shell.

Propagate bias Option: The propagate bias option attempts to preserve the source bias by propagating bias mesh schemes from the curves of the source surface to the curves of the target surface. It also propagates bias from one linking curve to all other linking curves.

Sweep transform Option: Swept meshes are created by projecting points between the source and target surfaces using affine transformations and then connecting them to form hexahedra. The method used to calculate the affine transformations is set using the sweep transform option.

Least squares: If the least squares option is selected then affine transformations between the source and target are calculated using a least squares method.

translate: If the translate option is selected then a simple translate affine transformation is calculated based upon the centroid of the source and target.

Sweep smooth Option: Note: This option is available only in Legacy mode. The command 'set legacy sweeper on|off controls the mode. Legacy mode is OFF by default.

To ensure adequate mesh quality, optional smoothing schemes are available to reposition the interior nodes. The sweep tool permits five types of smoothing that are set with the following command prior to meshing a volume whose mesh scheme is sweep:

Linear: If this option is selected, no layer smoothing is performed. The node positions are determined strictly by the affine transformation from the previous layer. Good quality swept meshes can be constructed using “linear” provided the volume geometry and meshed linking surfaces permit the volume mesh to be created by a translation, scaling, and/or rotation of the source mesh. Volumes for which this is nearly true may also produce acceptable quality with “linear”. As one would expect, this option generates swept meshes more quickly than the other sweep smooth options. This option is rarely needed since the next option produces better results with little time penalty.

Smart affine: The “smart affine” option does minimal smoothing of the interior nodes. Affine transformations are used to project the source and target surfaces to the middle surface of the volume. The position of the middle surface nodes is the average of the projected nodes from the source and target surfaces. The error in projecting from source and target is computed, and this error is linearly distributed back to the source and target.

Residual: The “residual” method is often used for meshing volumes that cannot be swept with the “smart linear” method. It tends to produce better quality meshes than the “smart linear” method while running faster than the Winslow-based smoother. The sweeping algorithm uses an affine transformation to calculate the interior nodes’ positions, but the mesh on the linking surface determines the positions of the nodes on the boundary of the layer. For the “residual” method, CUBIT calculates corrective adjustments for interior nodes using the “residuals” from boundary nodes. The “residual” is defined as the distance between the boundary node’s position (as determined by the surface mesh) and the boundary node’s ideal position (as determined by the affine transformation of the previous layer). Cubit computes the residual forward from the source and backward from the target to get best the possible node position.

Winslow: Smooth scheme “winslow” smooths each layer using a weighted, elliptic smoother. The weights are computed from the source mesh; they help maintain any biased spacing that occurs on the source mesh. For example, one might want to use the “winslow” option if the source was a biased mesh that was created using scheme circle. The biasing of the outer elements of the source mesh may be destroyed if one of the other smooth options is used. The interior nodes are initially place using the residual method. AUTO: This is the default for the sweep smooth option. “auto” causes the Sweeper to automatically choose between “smart affine” and “residual.” Auto will choose “off” if the layer needs little or no smoothing or “residual” if it needs smoothing. Scheme “auto” does not guarantee that no negative Jacobians are produced. This option produces acceptable results in most cases. If it fails to produce a quality mesh, then choose one of the other sweep smooth options.

If none of these smooth schemes result in adequate mesh quality, one can consider trying one of the volume smoothing schemes such as condition number or mean ratio.

Autosmooth target Option and Command

During sweeping, a quad mesh is placed on each source surface. Then the collection of nodes & quads from all the source surfaces is projected onto the target surface. The autosmooth target command or sweep command options control the placement of the nodes onto the target surface.

Volume <range> autosmooth target [off|ON]

fixed imprints [on|OFF]

smart smooth [ON|off] tolerance <val 0.0 to 1.0=0.2>

Issuing the command “Volume <id> autosmooth target off”, or using these options in the sweep command, will project the source nodes onto the target without any subsequent smoothing to improve quality. The result is that the relative placement of the nodes on the target will be as close to identical as possible to the relative placement of the node on the sources. This should be used when sweeping models that are very thin, and smoothing of the target could result in significant skew introduced in the thin layers in the sweep. Axisymmetric models might also want to turn OFF the autosmooth target so that the nodes are identically placed on the symmetry plane surfaces.

Issuing the command “Volume <id> autosmooth target on”, or using it as an option in the sweep command, will call a surface smoother after the initial projection of the nodes onto the target in order to improve surface element quality. This smoothing does not consider hex element quality, only quality of the target surface mesh. This command will smooth all nodes on the target surface. Adding the “fixed imprint on” keyword onto the command will cause the target nodes which are projections of source nodes on source curves and vertices to remain fixed during smoothing. Only target nodes, which are projections of source surface nodes will be smoothed. The “smart smooth on” option provides further control to the user. If “smart smooth” is turned on, target surface smoothing will only move nodes which are within “nlayers” of a target surface quad element that has a scaled Jacobian quality measure less than the specified “tolerance” value.

While the basic sweeping algorithm requires a single target surface, the sweeping algorithm can also handle multiple target surfaces. The multisweep algorithm works by recognizing possible mesh and topology conflicts between the source and target surfaces and works to resolve these conflicts through the use of the virtual geometry capabilities in CUBIT. Figure 4 shows some examples of volumes which have been meshed with the multisweep algorithm.

Figure 4. Examples of Multisweep meshes.

Linear: If this option is active and/or target surfaces are omitted from the scheme setting command, CUBIT will determine source and target surfaces (See Automatic Scheme Selection). Sweeping can be further automated using the "sweep groups" command.

Swept meshing relies on the constraint that the source and target meshes are topologically identical or the target surface is unmeshed. This results in there being dependencies between swept volumes connected through non-manifold surfaces; these dependencies must be satisfied before the group of volumes can be meshed successfully. For example, if the model was a series of connected cylinders, the proper way to mesh the model would be to sweep each volume starting at the top (or bottom) and continuing through each successive connected volume.

With larger models and with models that contain volumes that require many source surfaces, the process of determining the correct sweeping ordering becomes tedious. The sweep grouping capability computes these dependencies and puts the volumes into groups, in an order which represents those dependencies. The volumes are meshed in the correct order when the resulting group is meshed.

To compute the sweep dependencies, use the command:

This will create a group named "sweep_groups", which can then be meshed using the command:

In some automated meshing systems, the source and target surfaces are named using a naming pattern. For example, all source surfaces might be given names "xxx.source" and all target surfaces might be named "xxx.target". This allows the automated setting of the sweep direction based on predetermined names rather than ids. The following command is used to set the source and targets based on the naming pattern.

Set {Source|Target} Surface Pattern '<pattern>' [Include Volume Name]

The pattern is checked against all surfaces in the model using a simple case-sensitive substring match. All surfaces which contain that string of letters in their name will be designated as either a source or target surface, depending on which option the user specifies. For example:

br x 10 surface 1 name 'brick.top' surface 2 name 'brick.bottom' set source surface pattern 'top' set target surface pattern 'bottom' volume 1 scheme sweep list volume 1 brief

Volume <range> redistribute nodes {ON|off}

With redistribute set to ON, the boundary nodes of a mappable surface are moved until the spacing between the nodes are equivalent on the two opposing curves. In other words, the parametric values of the nodes lying on the two opposite curves are matched.

Redistribute option ON will assist in avoiding the skewness of the mapped mesh. In the below examples, the linking surfaces are meshed using mapped scheme, and with redistribute option ON, the skewness is significantly avoided (see figures (4) and (5)).

1. Redistribute option ON will affect all mapped surfaces, not just the linking surfaces of a swept volume. Even though the example below shows a swept volume, the command can be used independent of the sweeping command. That is, it can be used while meshing surface models that contain mappable surfaces.

2. If the linking surfaces of a swept mesh contain submappable surfaces, then the affect of redistribute option ON is generally not seen. The current implementation is restricted to mappable surfaces only and doesn’t handle submappable surfaces. In the future, we should be able to easily extend the redistribute option to submappable surfaces.

Figure 1 - Linking surfaces of a many-to-one sweepable solid (shown in green) is mappable

Figure 2 - Highly skewed elements on the linking mapped surface with 'redistribute nodes OFF'

Figure 3 - Quality of mesh with 'Redistribute Nodes OFF'

Figure 4 - High skew on the linking mapped surface can be avoided with 'Redistribute Nodes ON'

Figure 5 - Quality of mesh with 'Redistribute Nodes ON'

---

## TetMesh

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/tetmesh.htm

**Contents:**
- TetMesh
- Discussion
- TetMesh Scheme Options
- Global Tetmesher Options
- Using tets as the basis of an unstructured hexahedral mesh
- Conforming the tetmesh to internal features
- Controling the gradation of the mesh size inside the volume
- Generating a Tetmesh from a Skin of Triangles

Summary: Automatically meshes a volume with an unstructured tetrahedral mesh.

Volume <range> Scheme TetMesh [Proximity Layers {on[<num_layers>]|OFF}] [Geometry Approximation Angle <angle>]

[Set] Tetmesher Add mid_edge_nodes {on|OFF}

[Set] Tetmesher Optimize Surface mid_edge_nodes {on|OFF}

[Set] Tetmesher Anisotropic layers {on|OFF [<layers=2>]}

[Set] Tetmesher Boundary Recovery {on|OFF}

[Set] Tetmesher HPC {ON|off} [Threads <value=4>]

[Set] Tetmesher HPC minimum size [<size>]

[Set] Tetmesher Interior Points {ON|off}

[Set] Tetmesher Optimize { { [Level <level> [Overconstrained Edges {on|OFF}] [Overconstrained Tetrahedra {on|OFF}] [Sliver {on|OFF}] } | Default }

[Set] Trimesher Surface Gradation <value>

[Set] Trimesher Volume Gradation <value>

[Set] Trimesher Geometry Sizing {ON|off}

[Set] Trimesher Split Overconstrained Edges {on|OFF}

Volume <volume_id> Tetmesh Respect {Face|Tri|Edge} <range>

Volume <volume_id> Tetmesh Respect Node <range> [Size <size>]

Volume <volume_id> Tetmesh Respect Clear

Volume <volume_id> Tetmesh Respect File '<filename>'

Volume <volume_id> Tetmesh Respect Location (options)

Tetmesh Tri <range> [Make {Block|Group} [<id>]]

Tetmesh Tri <range> {Add|Replace} {Block|Group} <id>

Volume <id_range> Tetmesh growth_factor <value 1.0 to 10.0 = 1.05>

The TetMesh scheme fills an arbitrary three-dimensional volume with tetrahedral elements. The surfaces are first triangulated with one of the triangle schemes (TriMesh, TriAdvance or TriDelaunay) or a quadrilateral scheme with the quadrilaterals being split into two triangles (QTri). If a meshing scheme has not been applied to the surfaces, the TriMesh scheme will be used.

Included in Cubit is a third party software library for generating tetrahedral meshes called MeshGems. This is a robust and fast tetrahedral mesher developed by the French laboratory INRIA and distributed by Distene. It utilizes an algorithm for automatic mesh generation based upon the Voronoi-Delaunay method. Figure 1 shows a CAD model meshed with the TetMesh scheme, with the TriMesh scheme used to mesh the surfaces.

Figure 1. Tetrahedral mesh generated with the TetMesh scheme using default settings. (a) Initial CAD geometry (b) CAD model with surface mesh generated with TriMesh scheme. (c) and (d) Cut-away views of the interior tetrahedral mesh

The TetMesh scheme is usually very good at generating a mesh with its default settings. In most cases no adjustments to default settings are necessary. Using the size assigned to the volume, either assigned explicitly or defined with an auto size, the TetMesh scheme will attempt to maintain the assigned size, except where features smaller than the specified size exist. In this case, smaller tets will automatically be generated to match the feature size. The tet mesher will then generate a smooth gradation from the small tets used to capture features, to the size specified on the volume. This effect is shown in figure 1 where internal transitions in tetrahedra size can be seen. User defined sizes and intervals can also be assigned to individual surfaces and curves for more specific control of element sizes.

A sizing function can also be used with the TetMesh scheme to control element sizes, however the algorithm used for meshing surfaces will automatically revert to the TriAdvance scheme. This is because the TetMesh scheme provides built-in capabilities for adaptively controlling the element sizes based on geometry. More details can be found in Geometry Adaptive Sizing for TriMesh and TetMesh Schemes

When using the TetMesh and TriMesh schemes, recommended practice is to mesh all surfaces and volumes simultaneously. This provides the greatest flexibility to the algorithms to determine feature sizes and their effect on neighboring surfaces and volumes.

The Tetmesh options described below can be set to adjust the default behavior of the tet mesher. Scheme options are assigned independently to each volume as part of the scheme tetmesh command.

Proximity Layers {on[<num_layers>]|OFF}

In some thin regions of the model, it may be necessary to ensure a minimum number of element layers through the thickness to better capture physical properties. Using the proximity layers setting, the specified minimum num_layers of tetrahedra will be placed in thin regions, even if the tetrahedra sizes drop below the size assigned to the volume. The default setting for proximity layers is OFF where element sizes will not be affected in thin regions.

Figure 2. Demonstrates the effect of using proximity layers on a cut-away section of a volume. Note the layers of smaller tets placed in the thin region.

Geometry Approximation Angle <angle>

For non-planar CAD surfaces, an approximation must always be made to capture the curved features using the linear faces of the tetrahedra. When a geometry approximation angle is specified, the tet mesher will adjust element sizes on curved surfaces so that the linear edges of the tetrahedra will deviate no greater than the specified angle from the geometry. Figure 3 illustrates how the geometry approximation angle is determined. If the red curve represents the geometry and the black segments represent the mesh, the angle θ is the angle between the tangent plane at point A and the plane of a triangle at A. θ represents the maximum deviation from the geometry that the mesh will attempt to capture. As shown in figure 2(b), a smaller geometry approximation angle will normally result in more elements, but it will more closely approximate the actual geometry. The default approximation angle is 15 degrees.

Figure 3. The geometry approximation angle θ is shown as the maximum deviation between the tangent plane at A and the plane of a triangle at A.

Figure 4. Demonstrates the effect of the geometry approximation angle set on the volume. Triangle sizes on the interior of surfaces will be adjusted to better capture curvature.

The user may set options that control the operation of the tet-meshing algorithms. These tetmesher options are global settings and apply to all tetmeshes generated when the scheme is set to TetMesh until the option is changed by the user.

[Set] Tetmesher Add mid_edge_nodes {on|OFF}

If the triangle mesh given to tetmeshing has quadratic (mid-edge) nodes, tetmeshing can automatically create quadratic edge nodes while generating the tets if this option has been turned on. By performing this step during tetmeshing, these nodes can be placed optimally by the Meshgems tetmesher, improving element quality. If triangle or face elements have been set to be 'respected' in the tetmesh, they must also have quadratic edge elements or meshing will fail. The default value for this option is off. If set to off, quadratic edge nodes will be placed after meshing, exactly half way along the linear edge.

[Set] Tetmesher Optimize Surface mid_edge_nodes {on|OFF}

If the triangle mesh given to tetmeshing has quadratic (mid-edge) nodes, tetmeshing can also automatically optimize the locations of these mid edges nodes during the tetmeshing operation to achieve improved quality. create quadratic edge nodes while generating the tets if this option has been turned on. By performing this step during tetmeshing, these nodes can be placed optimally by the Meshgems tetmesher, improving element quality. If triangle or face elements have been set to be 'respected' in the tetmesh, they must also have quadratic edge elements or meshing will fail. The default value for this option is off. If set to off, quadratic edge nodes will be placed after meshing, exactly half way along the linear edge.

[Set] Tetmesher Anisotropic Layers {on|OFF [<layers=2>]}

The Anisotropic Layers setting attempts to place the specified number of layers of tetrahedra through thin regions of the volume while respecting the volume mesh size in the thick direction. The default number of layers is two. This option is currently under development and can sometimes generate high aspect ratio tetrahedra. The number of layers generated can sometimes exceed the number of layers specified..

Figure 5. Anisotropic Volume Meshing

[Set] Tetmesher Boundary Recovery {on|OFF}

The TetMesh scheme includes a specialized module known as Boundary Recovery. Normally if the quality of the surface mesh is good, the boundary recovery module is not used and the resulting tet mesh will conform exactly to the triangles defined on the surfaces without additional processing. In some cases where the surface mesh contains triangles that are of poor quality (ie. highly stretched or sliver shaped triangles) the tet mesher is unable to generate sufficiently good quality elements. When this occurs, the boundary recovery module is automatically invoked. This module does additional processing to temporarily modify boundary triangles so that reasonable quality tets may be inserted. The boundary adjustment is done as an intermediate phase and in most cases the boundary triangulation remains unchanged following meshing. The TetMesh scheme in Cubit will automatically invoke the boundary recovery module if the minimum surface mesh quality drops below a condition number of 0.2. However, if the the boundary recovery option is set to ON, the tet mesher will use the boundary recovery module regardless of surface mesh quality. Turning this setting ON will normally increase the time to generate the mesh, but may result in improved mesh quality. The default setting is OFF.

[Set] Tetmesher HPC {ON|off} [Threads <value=4>]

This option turns on or off MeshGems-Tetra HPC, the multithread or distributed tetrahedral volume mesh generator. The MeshGems-Tetra HPC software is an automatic multithread or distributed tetrahedral mesh generator based on the constrained VORONOI-DELAUNAY method. Using the threads option, one can specify the maximum number of threads MeshGemsTetra HPC will use to generate the mesh. The effective number of threads used will be determined by the number of parallel subdomains used, the default of 4, and the maximum of 8. If HPC is off, the older serial tetmesher MeshGems-Tetra is used. The default setting is ON.

[Set] Tetmesher HPC minimum size [<size>]

Sets the minimum edge length in tetmeshing, when using Distene's MeshGems-Tetra HPC.

[Set] Tetmesher Interior Points {ON|off}

Infrequently, the user desires a model with as few interior points as possible. The Interior Points command allows the user to enable or disable, or turn OFF the insertion of interior points. If interior points are disabled, the tetmesher will attempt to mesh the volume using only the exterior points. This may not be possible and a few points will be inserted to allow tet-meshing to complete. The default setting is ON, meaning that interior points will be inserted according to the specified element size.

[Set] Tetmesher Optimize Level <level>

The Tetmesher Optimize Level command allows the user to control the degree of optimization used to automatically improve element quality following the initial generation of tetrahedra. The optimization level is an integer in the range 0 to 6, which represent how aggressively the algorithm will attempt to improve element quality by automatically adjusting element connectivity and smoothing. The integers 0 to 6 can also be represented as none (0), light (1), medium (2), standard (3), strong (4), heavy (5), and extreme (6). Greater values will result in greater computation time, however may result in improved mesh quality. The default is 3 or standard optimization.

[Set] Tetmesher Optimize Overconstrained Edges {on|OFF}

This option controls the splitting of overconstrained edges. An edge is considered overconstrained when it connects two surface nodes but does not belong to the surface. This condition may not be desirable for some FEA analysis. Splitting edges can useful to guarantee two elements through the thickness. When using MeshGems-Tetra, this option cannot be used by itself; it must be used with the optimize tetrahedra option. If using MeshGems-Tetra HPC, it can be used by itself. The default for optimize overconstrained edges is OFF.

[Set] Tetmesher Optimize Overconstrained Tetrahedra {on|OFF}

In some cases, the default mesh generated with the TetMesh scheme may result in cases where more than one triangle face of a single tetrahedra lies on the same geometric surface. This condition may not be desirable for some FEA analysis. The default for optimize overconstrained tetrahedra is OFF.

[Set] Tetmesher Optimize Sliver {on|OFF}

A sliver tetrahedra is one in which the four nodes of the tet are nearly co-planar. Sliver tets are a common occurrence when using the Delaunay method, but are normally removed by standard optimization. In some cases, sliver tets may still remain even after optimization. To facilitate removal of all sliver-shaped tets, the optimize sliver option may be set to ON. In this event, additional processing will be done on the mesh to attempt to identify and remove all sliver-shaped tets from the mesh. Since this step may take additional time, and in most cases is not needed, the default setting is OFF.

[Set] Tetmesher Optimize Default

The Tetmesher Optimize Default command restores the default optimization values: level = 3 (standard), overconstrained edges = off, overconstrained tetrahedra = off, and sliver = off.

Tet meshing can be used to generate hexahedral meshes using the THex command. Each of the tetrahedron can be converted into 4 hexes, producing a fully conformal hexahedral mesh, albeit of poorer quality. These meshes can often be used in codes that are less sensitive to mesh quality and mesh directionality. The THex command requires that all tets in the model be converted to hexahedra with the same command.

In some cases it is necessary for the finite element mesh to conform to internal features of the model. The tetmesh scheme provides this capability provided the tetmesh respect command has been previously issued to define the features that will be respected.

Volume <volume_id> Tetmesh Respect {Face|Tri|Edge} <range>

Volume <volume_id> Tetmesh Respect Node <range> [Size <size>]

The tetmesh respect command allows the user to specify mesh entities that will be part of a tetrahedral mesh. These faces, triangles, edges, or nodes are inside the volume since all surface mesh features will appear in the final tetrahedral mesh by default. These mesh entities specified to be respected can be generated from other meshing commands on free vertices, curves, or surfaces.

Figure 2. Example of using tetmesh respect to ensure node 9 is captured in the tetmesh.

Figure 2 is an example of using the tetmesh respect command to enforce a node at the center of a cube. Node 9 in this example was generated by first creating a free vertex at the center location and meshing the vertex. (mesh vertex 9). The following commands would then be used to generate the tetmesh that respected node 9.

volume 1 scheme tetmesh tetmesh respect node 9 mesh volume 1

The tetmesh respect command can also be used to enforce multiple mesh entities. To accomplish this, the tetmesh respect command may be issued multiple times. For example, If node 12 and a triangle 2 inside volume 3 was to appear in the volumetric mesh, the following commands could be used:

volume 3 scheme tetmesh volume 3 tetmesh respect node 12 volume 3 tetmesh respect tri 2 mesh volume 1

The tetmesh respect command can also be given a size value with a node. When given a size, the generated tet elements surrounding the node will have sizes matching the given size. This may be useful to provide refinement at given locations within a tet mesh.

Unlike the tetmesh respect command described above, the tetmesh respect file and tetmesh respect location commands do not require underlying geometry.

Volume <volume_id> Tetmesh Respect File '<filename>'

Volume <volume_id> Tetmesh Respect Location (options)

These two commands create mesh data that only the tetmesher knows about. Thus, to respect a point at (1.0, 0.0, -1.0) in your model, enter the command

volume 1 tetmesh respect location 1 0 -1

This is much simpler than creating the vertex, meshing it, and then respecting it.

If the model has many points that must be respected, use the file version of the command. First generate a file with all of the points, edges, and triangles that should be respected. The format of the file is the format used by the facet file. Now, use the following command to respect all of the information in the file for the given volume.

volume 2 tetmesh respect file 'my_points.facet'

Finally, the following command is used to remove the respected data from an entity.

Volume <volume_id> Tetmesh Respect Clear

The tetmesh respect clear command is the only way to remove respected data from a volume without deleting the volume. Unfortunately, it removes all respected data from the volume. Therefore, if the model has a lot of data to be respected, it is best to put it in a file or keep a journal file that can be edited.

Volume <id_range> Tetmesh growth_factor <value 1.0 to 10.0 = 1.05>

The growth_factor option controls how fast the tetrahedra sizes can change when transitioning from small to larger sizes within the volume. For example a value of 1.5 will attempt to limit the ratio between 2 adjacent tetrahedral edges. Valid values for gradation should be greater than or equal to 1.0 and usually less than 2 or 3. The larger the value, the faster the transition is. Likewise, values closer to 1.0 will result in a more uniform mesh. The default setting for growth_factor is 1.05, allowing for a somewhat slow transition between sizes within a volume. The size at the interior of a volume can be controlled using the Volume <range> [Interval] Size <interval_size> command.

Gradation of the triangles on the surfaces can also be controlled independently using the global settings [set] trimesher surface gradation and [set] trimesher volume gradation.

Tetmesh Tri <ids> [growth_factor <value>] [Make {Block|Group} [<id>]]

Tetmesh Tri <ids> [growth_factor <value>] {Add|Replace} {Block <id>|Group <id>}

The Tetmesh Tri command generates a tetrahedral mesh from the list of triangles entered. The triangles must form a closed surface. The command fails if they do not. The list of triangles may be a skin, and thus a command such as tetmesh tri in block 1 would be acceptable, should block 1 be a previously defined skin.

The first command form has optional arguments. If the make option and its arguments are present, then the specified block or group will contain the generated tet elements. The command fails with the make option if the specified block or group already exists. If the block or group id is omitted, the next available block or group id is used.

The second command form has two options, add and replace. Each option requires specifying an existing block or group. If the block or group does not exist, the command fails. The add option appends the tet elements to the block or group. The replace option removes any existing mesh from the block or group before adding the tet elements.

The growth_factor option helps control the transition from small to larger sizes within the mesh. The value specified will be the approximate ratio in the size of adjacent tets going from the boundary into the interior of the mesh. For example, a growth_factor of 1.0 will give near-constant sizing, while a growth_factor of 1.3 allows approximately 30% growth in each layer of adjacent tets.

---

## Tetprimitive

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/tetprimitive.htm

**Contents:**
- Tetprimitive

Summary: Meshes a 4 "sided" object with hexahedral elements using the standard tetrahedron primitive.

Volume <range> Scheme Tetprimitive [Combine Surface <range>] [Combine Surface <range>] [Combine Surface <range>] [Combine Surface <range>]

The tetprimitive scheme is used to create a hexahedral mesh in a volume which fits the shape of a tetrahedral primitive. The Tetprimitive scheme assumes that each of the four surfaces have been meshed with the triprimitive, or similar, meshing scheme. If more than four surfaces form the tetrahedron geometry, the surfaces forming a logical side can be combined using the combine option.

Figure 1. Sphere octant hex meshed with scheme Tetprimitive, surfaces meshed using scheme Triprimitive

---

## THex

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/conversion/thex.htm

**Contents:**
- THex

Summary: Converts a tetrahedral mesh into a hexahedral mesh.

The THex command splits each tetrahedral element in a volume into four hexahedral elements, as shown in Figure 1. This is done by splitting each edge and face at its midpoint, and then forming connections to the center of the tet.

When THexing merged volumes, all of the volumes must be THexed at the same time, in a single command. Otherwise, meshes on shared surfaces will be invalid. An example of the THex algorithm is shown in Figure 2.

Figure 1. Conversion of a tetrahedron to four hexahedra, as performed by the THex algorithm.

Figure 2. A cylinder before and after the THex algorithm is applied.

---

## TQuad

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/conversion/tquad.htm

**Contents:**
- TQuad

Summary: Converts a triangular surface mesh into a quadrilateral mesh.

TQuad Surface <range>

The TQuad command splits each triangular surface element in four quadrilateral elements, as shown in Figure 1. This is done by splitting each edge at its midpoint, and then forming connections to the center of the triangle. The result is the same as using the THex algorithm, but only applies to surfaces. In general it is better to use a mapped or paved mesh to generate quadrilateral surface meshes. However, the TQuad scheme may be useful for converting facet-based triangular meshes to quadrilateral meshes when remeshing is not possible.

Figure 1. A triangle split into 3 quads using the TQuad scheme

---

## Transforming Mesh Coordinates

**URL:** https://coreform.com/cubit_help/finite_element_model/export/transforming_mesh_coords.htm

**Contents:**
- Transforming Mesh Coordinates

A mesh can be scaled and transformed to a new location as it is written to or read from an Exodus file. To transform a mesh during import or export use the following command:

Transform Mesh {Input|Output} [Scale <xyz_factor>] [Scale <x_factor> <y_factor> <z_factor>]] [Scale {X|Y|Z} <factor>] [Translate <dx> [<dy> [<dz>]]] [Translate {X|Y|Z} <distance>] [Rotate <degrees> about {X|Y|Z}] [Reset]

This command may be repeated any number of times using any number of options. Transform commands are cumulative, added to the effect of previous transforms. If more than one transformation is entered in the same command, transformations are applied in the order they appear in the command.

To clear a transformation matrix, use the Reset option:

Transform Mesh {Input|Output} Reset

Mesh input and output transformations are also cleared when you reset the entire model using the Reset command.

Transforming a mesh during output does not change the position of the mesh within CUBIT. It only changes the nodal positions written to the Exodus file. Nodal positions may be changed within CUBIT by transforming the body that contains the mesh. See Geometry Transforms for information on how to apply transformations to a Body.

Transforming a mesh during input does change the position of the mesh with CUBIT. The file being read is not modified.

Transformations applied during mesh input are independent of transformations applied during mesh output.

The following example generates a simple mesh, writes the mesh with its coordinates scaled by a factor of 2, and then re-imports that mesh, restoring the scaling to what it originally was in CUBIT.

brick x 10 volume 1 interval 4 mesh vol 1 transform mesh output scale 2 export mesh 'temp.exo' delete mesh transform mesh input scale .5 import mesh 'temp.exo'

See Geometry Transforms for information on how to apply transformations to a Body.

See Nodeset and Nodeset Repositioning

See Mesh Based Geometry

---

## TriAdvance

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/triadvance.htm

**Contents:**
- TriAdvance

Summary: Automatically meshes surface geometry with triangle elements.

The triangle meshing scheme TriAdvance fills an arbitrary surface with triangle elements. It is an advancing front algorithm which allows holes in the surface and transitions between dissimilar element sizes. It can use a sizing function like the pave scheme if one is defined for the surface. Future development will add hard lines to this scheme's capabilities. You specify this scheme for a surface by giving the command:

To insure that coplanar (two-tris-sharing-three-node condition) or nearly coplanar tris at sharp geometric vertices are not generated using this scheme, a corrective edge-swap is automatically done.

---

## Triangle Mesh Coarsening

**URL:** https://coreform.com/cubit_help/appendix/alpha/triangle_coarsening.htm

**Contents:**
- Triangle Mesh Coarsening

Note: This feature is under development. The command to enable or disable features under development is:

Set Developer Commands {On|OFF}

CUBIT provides the capability for coarsening triangle surface meshes. Triangle coarsening uses a technique known as edge collapsing to coarsen a mesh. With this technique, triangle edges are selectively eliminated from the mesh until the specified criteria have been met. The following commands will coarsen an existing triangle surface mesh:

Coarsen {Node|Edge|Tri} <range> {Factor|Size <double> [Bias <double>]} [Depth <int>|Radius <double>] [Sizing_Function] [no_smooth]

Coarsen {Vertex|Curve|Surface} <range> {Factor|Size<double> [Bias<double>]} [Depth<int>|Radius<double>] [Sizing_Function] [no_smooth]

Important: These commands are currently implemented only for triangle shaped elements.

To use these commands, first select mesh or geometric entities at which you would like to perform coarsening. Coarsening operations will be applied to all mesh entities associated with or within proximity of the entities. The all keyword may be used to uniformly coarsen all triangles in the model.

Following is a description of each of the coarsen options:

Defines the approximate size relative to the existing edge lengths for which the coarsening will be applied. For example, a factor of 2 will attempt to make every edge length within the specified region approximately twice the size. A factor of 3 will make everything three times the size. Valid input values for factor must be greater than 1. Figure 1 shows an example where a coarsening factor of 2 was applied

Figure 1. Example of coarsening all triangles with a factor of 2.

The Size and Bias options are useful when a specific element size is desired at a known location. This might be used for locally coarsening around a vertex or curve. The Bias argument can be used with the Size option to define the rate at which the element sizes will change to meet the existing element sizes on the model. Valid input values for Bias are greater than 1.0 and represent the maximum change in element size from one element to the next. Since coarsening is a discrete operation, the Size and Bias options can only approximate the desired input values. This may cause apparent discontinuities in the element sizes. Using the default smooth option can lessen this effect. It should also be noted that the Size option is exclusive of the Factor option. Either Factor or Size can be specified, but not both.

The Depth option permits the user to specify how many elements away from the specified entity will also be coarsened. Default Depth is 1.

Figure 2. Coarsening performed at a node with factor = 3 and depth = 3

Instead of specifying the number of elements to describe how far to propagate the coarsening, a real Radius may be entered.

Coarsening may also be controlled by a sizing function. CUBIT uses sizing functions to control the local density of a mesh. Various options for setting up a sizing function are provided, including importing scalar field data from an exodus file. In order to use this option, a sizing function must first be specified on the surface on which the coarsening will be applied. See Adaptive Meshing for a description of how to define a sizing function.

The default mode for coarsening operations is to perform smoothing after coarsening the elements. This will generally provide better quality elements. In some cases it may be necessary to retain the original node locations after coarsening. The no_smooth option provides this capability.

---

## TriDelaunay

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/tridelaunay.htm

**Contents:**
- TriDelaunay

Summary: Automatically meshes parametric surface geometry with triangle elements.

Surface <range> Scheme TriDelaunay

The scheme TriDelaunay is a parametric meshing algorithm. It can be run in two modes. The default mode (asp) combines the Delaunay [Watson,81] criterion for connecting nodes into triangles with an advancing-front approach for inserting nodes into the mesh. This method maximizes the number of regular triangles in the mesh but does not guarantee the minimum angle quality of the triangles. A guaranteed quality (gq) mode can be used for planar surfaces (only). This mode refines the initial Delaunay configuration by placing points at the centroids of the worst triangles until the mesh has an acceptable density. To switch between the two modes, use the following setting command.

[Set] Tridelaunay point placement {gq | guaranteed quality | asp}

---

## TriMap

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/trimap.htm

**Contents:**
- TriMap

Summary: Places triangle elements at some vertices, and map meshes the remaining surface.

Surface <range> Scheme Trimap

Surface <range> Vertex <range> Type {Triangle|Notriangle}

Some surfaces contain bounding curves which meet at a very acute angle. Meshing these surfaces with an all-quadrilateral mesh will result in a very skewed quad to resolve that angle. In some cases, this is a worse result than simply placing a triangular element to resolve that angle. This scheme resolves this situation by placing a triangular element in these tight corners, and filling the remainder of the surface with a mapped mesh.

The algorithm can automatically compute whether a triangular element is necessary, along with where to place that element. To override the choice of where triangular elements are used, the following command can be issued:

Surface <range> Vertex <range> Type {Triangle|Notriangle}

---

## TriMesh

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/trimesh.htm

**Contents:**
- TriMesh
- TriMesh Scheme Options
- Global Trimesher Gradation Options

Summary: Automatically meshes surface geometry with triangle elements using the third part meshgems tool.

Surface <range> Scheme TriMesh [Geometry Approximation Angle <angle>] [Meshgems] [Minimum Size <value>]

[Set] Trimesher Minimum Size <value>

[Set] Trimesher Surface Gradation <value>

[Set] Trimesher Volume Gradation <value>

[Set] Trimesher Geometry Sizing {ON|off}

[Set] Trimesher Clean Discrete {on|OFF}

[Set] Trimesher Discrete Composites {on|OFF}

[Set] Trimesher Split Overconstrained Edges {on|OFF}

[Set] Trimesher Ridge Angle {<value=100>}

[Set] Trimesher Anisotropic layers {on|OFF [<layers=2>]}

[Set] Trimesher Surface Proximity {on|OFF [<ratio=1>]}

[Set] Trimesher Coarse {on|OFF} [Ratio <ratio=100>] [Angle <angle=5>]

The TriMesh scheme fills a surface of arbitrary shape with triangle elements. The TriMesh scheme serves as the default method for meshing the surfaces of volumes for the TetMesh scheme.

Included in Cubit is a third party software library for generating triangle meshes called MeshGems. This is a robust and fast triangle mesher developed and distributed by Distene. Figure 1 shows a CAD model where surfaces have been meshed with the TriMesh scheme. The triangle mesh was then used as input to the TetMesh scheme.

Figure 1. Triangle meshes generated with the TriMesh scheme using default settings on the surfaces of a CAD model.

The TriMesh scheme is usually very good at generating a mesh with its default settings. In most cases no adjustments to default settings are necessry. Using the size assigned to the surface, either assigned explicitly or defined with an auto size, the TriMesh scheme will attempt to maintain the assigned size, except where features smaller than the specified size exist. In this case, smaller triangles will automatically be generated to match the feature size. The triangle mesher will then generate a smooth gradation from the small triangles used to capture features, to the size specified on the surface. This effect is shown in figure 1 where the transitions in triangle sizes can be seen. If no size is specified on the surface, it will use the size that was set on its parent volume. User defined sizes and intervals can also be assigned to individual curves for more specific control of element sizes.

Although rare, if meshing fails when using the TriMesh scheme, Cubit will automatically attempt to mesh the surface with the TriDelaunay scheme. Subsequent mesh failures will also attempt meshing with the TriAdvance and QTri schemes.

A sizing function can also be used with the TriMesh scheme to control element sizes, however the algorithm used for meshing will automatically revert to the TriAdvance scheme. This is because the MeshGems algorithm provides built-in capabilities for adaptively controlling the element sizes based on geometry. More details can be found in Geometry Adaptive Sizing for TriMesh and TetMesh Schemes

When using the TriMesh and TetMesh schemes, recommended practice is to mesh all surfaces and volumes simultaneously. This provides the greatest flexibility to the algorithms to determine feature sizes and their effect on neighboring surfaces and volumes.

The TriMesh options described below can be set to adjust the default behavior of the tri mesher. Scheme options are assigned independently to each surface as part of the scheme TriMesh command. Note that the options described here will apply only if the TriMesh scheme is used. TriDelaunay and TriAdvance schemes will not utilize these options when meshing.

Geometry Approximation Angle <angle>

For non-planar CAD surfaces and non-linear curves, an approximation must always be made to capture the curved features using the linear edges of the triangle. When a geometry approximation angle is specified, the triangle mesher will adjust triangle sizes on curved boundaries so that the linear edges of the triangle will deviate from the geometry by no greater than the specified angle. Figure 2 illustrates how the geometry approximation angle is determined. If the red curve representes the geometry and the black segments represent the mesh, the angle &theta; is the angle between the tangent plane at point A and the plane of a triangle at A. &theta; represents the maximum deviation from the geometry that the mesh will attempt to capture. As shown in figure 2(b), a smaller geometry approximation angle will normally result in more elements, but it will more closely approximate the actual geometry. The default approximation angle is 15 degrees.

Figure 2. The geometry approximation angle &theta; is shown as the maximum deviation between the tangent plane at A and the plane of a triangle at A.

Note that the geometry approximation angle is also effective in controlling the element size on the interior of surfaces as illustrated in figure 3. This is most useful when used in conjunction with the TetMesh Scheme where smaller tets will be placed in regions of higher curvature.

Figure 3. Demonstrates the effect of the geometry approximation angle to better capture surface curvature on the interior of surfaces.

By specifying a minimum size, the tri mesher will attempt to prevent creating elements smaller than this specified size. It should be noted that there may still be a small number of elements with a size slighly less that this value; it is not an exact setting.

The MeshGems option will use only the MeshGems triangle mesher on the specified surfaces. It will not revert upon failure to the TriDelaunay or TriAdvance schemes.

The user may set options that control the gradation of the tri-meshing algorithms. These trimesher options are global settings and apply to all trimeshes generated when the scheme is set to TriMesh until the option is changed by the user.

The minimum size setting controls the smallest edge length generated during triangle meshing.

[Set] Trimesher Minimum Size <value>

The global gradation options control how fast the triangle sizes can change when transitioning from small to larger sizes. For example a value of 1.5 will attempt to limit the change in element size of adjacent triangles to no greater than a factor of 1.5. Valid values for gradation should be greater than 1.0 and usually less than 2 or 3. The larger the value, the faster the transition resulting in fewer total elements. Likewise, values closer to 1.0 can result in significantly more elements, especially when small features are present. The default setting for gradation is 1.3. Gradation can be controlled for both surfaces and volumes.

[Set] Trimesher Surface Gradation <value>

Surface gradation will control the growth of triangles where element size has been determined by bounding curves. For example, Figure 4 shows a small feature where element sizes have been determined locally by the length of the small curves. A gradation is applied so that triangle sizes increase away from the small feature. A surface gradation of 1.3 is shown on the left, while a surface gradation of 1.1 is shown on the right.

Figure 4. Demonstrates the effect of changing the default gradation, where (a) is the default gradtion of 1.3, compared with (b) using a gradation of 1.1. Note that both images use the same interval size setting for the surface.

[Set] Trimesher Volume Gradation <value>

Volume gradation will control the growth of triangles where element size has been determined by the proximity of other nearby surfaces. For example, Figure 5a and 5b shows a brick with a small void where the surface meshes are generated with the TriMesh scheme. The surface gradation has been adjusted to a large number so its effect is negligible. The small element size determined for the void is propagated to the exterior surfaces. The resulting gradation of the nearby triangles on the surface is determined by the trimesh volume gradation setting.

Note that the trimesh volume gradation command is different than the growth factor control setting. The trimesh volume gradation controls the gradation of triangles on the surface due to nearby features where small tets will exist, whereas the volume <range> tetmesh growth_factor command controls the gradation of the interior tet elements.

Figure 5a. An example of a cut-away mesh with a volume gradation, where the small size on the interior void propagates to the exterior surfaces

Figure 5a. An example of a cut-away mesh with a volume gradation, where the small size on the interior void propagates to the exterior surfaces

[Set] Trimesher Geometry Sizing {ON|off}

The global Geometry Sizing setting can be toggled on or off. If set to on, the element size will be influenced by the geometry approximation angle. If set to off, geometry approximation angle will not be involved in the computation of element size. See geometry approximtion angle for more information.

[Set] Trimesher Discrete Composites {on|OFF}

The option Discrete Composites forces trimeshing to convert the composite into a discrete (faceted) representation, from which the trimesher generates a mesh. The default behavior is to use the underlying geometry, if the composite has it, to generate a mesh. Using the underlying geometry is typically a more robust and reliable approach, not dependent on good faceting. However, it should be noted that composites with mesh curves will be triangle meshed with the discrete method, as this is not supported with the default method at this time but shortly will be.

[Set] Trimesher Clean Discrete {on|OFF}

The option Clean Discrete performs a step to 'clean' the faceting given to the trimesher for discrete surfaces (mesh-based geometry and composites), previous to triangle meshing. The 'cleaning' is actually a meshing of the facets which typically generate a better, more optimal set of facets representing the surface. This 'clean' step uses geometry approximation, with angle of 8 degrees to generate the new facets. The option is OFF by default.

[Set] Trimesher Ridge Angle {<value=100>}

The ridge_angle setting is only used when meshing discrete surfaces (composites or facet/mesh-based geometry surfaces). It is the threshold for deteremining when to preserve lines (ridges) defined in the discrete surface. Lines in the discrete surface having a dihedral angle larger than ridge_angle will be preserved in the generated triangle mesh. In Figure 7, the composite surface has a dihedral angle of 17° at its ridge. In the first image ridge_angle is set to less than 17° so the ridge is preserved. In the second image ridge_angle is set to greater than 17° so the ridge is not preserved.

Figure 6. Ridge Angle Setting

[Set] Trimesher Split Overconstrained Edges {on|OFF}

The global Split Overconstrained Edges, if set to on, splits edges owned by the surface, but with both nodes on curves. This feature can help when two elements through the thickness of the mesh is desired. Figure 7 shows the effect of this option.

Figure 7. Split overconstrained edges

[Set] Trimesher Anisotropic Layers {on|OFF [<layers=2>]}

The Anisotropic Layers setting attempts to place the specified number of layers triangle through thin regions of the surface while respecting the surface mesh size in the thick direction. The default number of layers is two. This option is currently under development and can sometimes generate ill-formed triangles. The number of layers generated can sometimes exceed the number of layers specified..

Figure 8. Anisotropic Surface Meshing

[Set] Trimesher Surface Proximity {on|OFF [<ratio=2>]}

The Surface Proximity setting will add refinment to thin regions of surfaces. The ratio option can be used to multiply a scale factor to a size computed from proximity. By default, Surface Proximity is not enabled and if enabled, the default ratio is 1.0.

Figure 9. Surface Proximity disabled on the left, and enabled on the right

[Set] Trimesher Coarse {on|OFF} [Ratio <ratio=100>] [Angle <angle=5>]

The Coarse setting produces a fast, sparse triangle mesh that is coarse over flat regions of a surface and refined over curved regions. It is intended for DAGMC particle-transport workflows, where a lightweight watertight surface mesh is preferred over a uniformly sized one. When the toggle is on, the next surface-mesh operation drives the MeshGems mesher along its anisotropic path instead of the regular sizing pipeline.

The Ratio option sets the anisotropic ratio — the length-to-width ratio allowed for the anisotropic elements. The ratio must be greater than zero and is typically large; the default is 100. The Angle option sets the geometric approximation angle, in degrees, that controls how closely the mesh follows curvature; it must be greater than zero and defaults to 5. By default the Coarse setting is off.

Figure 10. Coarse trimesh for DAGMC: large triangles over flat regions and finer triangles over curved regions.

---

## TriPave

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/tripave.htm

**Contents:**
- TriPave

Summary: Places triangle elements at some vertices, and paves the remaining surface.

Surface <range> Scheme Tripave

Surface <range> Vertex <range> Type {triangle|notriangle}

Similar to the trimap algorithm, but uses paving instead of mapping to fill the remainder of the surface with quadrilaterals.

The algorithm can automatically compute whether a triangular element is necessary, along with where to place that element. To override the choice of where triangular elements are used, the following command can be issued:

Surface <range> Vertex <range> Type {triangle|notriangle}

---

## TriPrimitive

**URL:** https://coreform.com/cubit_help/mesh_generation/meshing_schemes/traditional/triprimitive.htm

**Contents:**
- TriPrimitive

Summary: Produces a triangle-primitive mesh for a surface with three logical sides

Surface <range> Scheme Triprimitive [SMOOTH | nosmoothing]

By default, the triprimitive algorithm will smooth the mesh with an iterative smoothing scheme. This smoothing can be disabled by using the "nosmoothing" option with this command. The quality of the mesh will often be significantly degraded by disabling smoothing, but in certain cases the unsmoothed mesh may be preferred.

Figure 1. Surfaces meshed with scheme Triprimitive

---

## Untangle

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/untangle.htm

**Contents:**
- Untangle

Applies to: Triangular or Quadrilateral Surface Meshes Tetrahedral or Hexahedral Volume Meshes. Does not apply to Mixed Element Meshes.

Summary: Removes as many negative Jacobians from the mesh as possible by minimizing a certain objective function.

Surface <surface_id_range> Smooth Scheme Untangle [beta <double=0.02>] [cpu <double=10>]

Volume <volume_id_range> Smooth Scheme Untangle [beta <double=0.02>] [cpu <double=10>]

The Untangle 'smoother' is designed to eliminate negative Jacobians from a given mesh by moving nodes to appropriate locations. If a mesh node is not involved in causing a negative Jacobian it will not be moved. If a mesh has no negative Jacobians, the Untangler will not move any of the nodes. This smoother is not magic: if an untangled mesh does not exist for the given mesh topology, the untangler will not untangle the mesh. Instead, it will do the best it can and exit gracefully. An untangled mesh produced by this smoother will often have poor shape quality; in that case it is recommended that untangling be followed by condition number smoothing. The untangle smoother is automatically called by the condition number smoother.

There is no "fixed/free" option with this command; boundary nodes are always held fixed. As a result, users should be aware that the volume untangler cannot succeed if the volume contains a surface mesh which contains a negative Jacobian. In that case, one must first remove the surface mesh negative Jacobians by invoking the surface Untangler and then invoke the volume Untangler.

The command above only sets the smoothing scheme; to actually smooth the mesh one must subsequently issue the command "smooth surface <surface_id_range>" or "smooth volume <volume_id_range>".

Stopping Criteria: Untangling will proceed until the objective function has been minimized or the optional user input "cpu" has been satisfied. The latter stopping criterion tells the code how many minutes to spend trying to untangle the mesh. The default value is 10 minutes. Optimization may also be halted by using "control-C" on your keyboard.

Beta Parameter: An optional user input parameter "beta" plays a role in determining the optimal mesh. Optimization proceeds until the minimum scaled Jacobian of the mesh is (roughly) greater than beta. To remove negative Jacobians one would need beta=0 (however, as a safety margin, we choose beta=0.02 as the default). To further improve the scaled Jacobian of the mesh, input a larger value of "beta". If a mesh with all scaled Jacobians greater than "beta" does not exist, optimization will continue until the cpu time stopping criterion has been met. Therefore, it is best not to use "beta" values too large (say, greater than 0.2) without also decreasing the cpu time limit.

To view a detailed report of the smoothing in progress issue the command "set debug 91 on" prior to smoothing the surfaces or volumes. You will get a synopsis of whether or not untangling is needed and whether the stopping criteria are satisfied. In addition the following printout information is given for each iteration of the conjugate gradient numerical optimization:

Iteration=n, Evals=m, Fcn=value1, dfmax=value2, time=value3 min_jsc=value4

n is the iteration count, m is the number of objective function evaluations performed per iteration, value1 is the value of the objective function (this usually decreases monotonically), value2 is the norm of the gradient (does not always decrease monotonically), and value3 is the cumulative cpu time (in seconds) spent up to the current iteration. The minimum possible value of the objective function is zero; this value is attained only when the minimum scaled Jacobian of the mesh exceeds "beta". The minimum scaled jacobian is also reported.

---

## Using Mesh Intersections to Partition Surfaces

**URL:** https://coreform.com/cubit_help/geometry/virtual_geometry/partitioned_geometry/mesh_based_imprinting.htm

**Contents:**
- Using Mesh Intersections to Partition Surfaces

To assist in various mesh editing tasks such as joining, a mesh-based imprinting capability is provided. The command

Imprint Mesh {Body | Volume} <id_list>

determines imprint locations using the mesh on the surfaces of the specified bodies or volumes. Regions of coincidence between the surfaces is determined by searching for coincident nodes in the mesh of the surfaces. Virtual geometry is then used to partition the surfaces and curves at the boundary of these regions of coincident mesh.

The imprint mesh functionality differs from a normal geometric imprint in the following ways:

The following is a trivial example of this capability. The following commands create two meshed blocks:

brick width 10 brick width 6 body 2 move x 8 volume 1 2 size 1 mesh volume 1 2

Figure 1 shows the results of these commands.

Figure 1. Two adjacent meshed volumes. The coincident meshes will form the basis of the imprint operation.

The mesh of the blocks can be joined by first doing a mesh-based imprint and then merging:

imprint mesh body 1 2 merge body 1 2

Figure 2. shows the results of the imprint operation. A meshed surface is created at the interface between the two meshed volumes. The nodes on the new surface are shared by the neighboring hexahedra of both volumes.

Figure 2. The imprinted surface. Adjacent volume meshes joined at the interface surface.

---

## Vertex Sizing and Automatic Curve Biasing

**URL:** https://coreform.com/cubit_help/mesh_generation/interval_assignment/vertex_sizing_curve_biasing.htm

**Contents:**
- Vertex Sizing and Automatic Curve Biasing

Sizes can now be specified on vertices to control biasing along curves. If a curve has a bias scheme the vertex sizes will be honored, even if it is inherited from parent geometry.

Set a size on a vertex with the following command:

vertex <id> size <size>

Bias can be turned on with:

curve <id> scheme bias

For tri/tet meshing, curve biasing is on by default to generate higher quality tri/tet meshes. Not only is the difference noticeable when setting sizes on vertices, but it is also noticeable when setting various sizes on connected curves, surfaces, or volumes. To turn curve biasing off issue the following command:

curve<id> scheme equal

In the following examples, the surfaces have been given sizes. In the first graphic auto bias is not enabled. In the second graphic auto bias is enabled.

When auto bias is enabled sizes on vertices are respected. If a size hasn't been directly set on a vertex the size is inherited from the parent(s). If there are multiple parents the inherited size is averaged. In the examples shown above the sizes of the vertices attached to both surfaces was an average of the two surface sizes. That affected the biasing while curve meshing.

---

## Winslow

**URL:** https://coreform.com/cubit_help/mesh_generation/mesh_modification/mesh_smoothing/winslow.htm

**Contents:**
- Winslow

Applies to: Surface meshes

Summary: Elliptic smoothing technique for structured and unstructured surface meshes

Surface <range> Smooth Scheme Winslow [Free]

Winslow elliptic smoothing (Knupp, 98) is based on solving Laplaces equation with the independent and dependent variables interchanged. The method is widely used in conjunction with the mapping and submapping methods to give smooth meshes with positive Jacobians, even on non-convex two-dimensional regions. The method has been extended in CUBIT to work on unstructured meshes.

The free option allows the nodes on the boundary (curves) to be moved during the smooth operation.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_mesh_error_feedback.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ get_entity_id()
- ◆ get_entity_type()
- ◆ get_error_code()
- ◆ get_error_text()
- ◆ set_entity_id()
- ◆ set_entity_type()
- ◆ set_error_code()

Class to implement mesh command feedback processing. More...

Class to implement mesh command feedback processing.

---
