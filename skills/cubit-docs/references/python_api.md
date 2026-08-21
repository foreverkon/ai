# Coreform-Cubit-Docs-Skill_Docs - Python Api

**Pages:** 24

---

## Coreform Cubit Python API: Method-Based API

**URL:** https://coreform.com/cubit_help/python/cubit_python_api_method_based.htm

**Contents:**
- Coreform Cubit Python API: Method-Based API
- Common Methods
- Get Methods
- Query State Methods
- Get ID Methods
- Bounding Box Methods
- Mesh Query Methods
- Geometry Creation Methods

Geometry Creation Methods

Pass a command string into Coreform Cubit. Passing a command into Coreform Cubit using this method will result in an immediate execution of the command. The command is passed directly to Coreform Cubit without any validation or other checking.

input_string – Pointer to a string containing a complete Coreform Cubit command

Parse a list of integers into a Cubit style id list. Return string will not include carriage returns or line break.

entity_ids – tuple of integers return A string representing the id list without line breaks

a Cubit stype string of ids

Use cubit.init() to initialize Coreform Cubit in a stand-alone python session.

Cubit may be imported into python without starting up the GUI. The path to a licensed version of Coreform Cubit must be specifed and Cubit must be initialized prior accessing the other methods in this API.

The arguments to the init() method are the command line arguments for Coreform Cubit with the addition that the first argument is the program name “cubit”.

The following python script shows an example of initializing and using Coreform Cubit. The key parts are ensuring that the Coreform Cubit libraries are in the path, importing the Coreform Cubit libraries, and calling cubit.init().

argv – List of command line start-up directives. A blank list such as [‘’] will suffice. If command parameters are specified, the first item in the list is ignored.

Parse a Cubit style entity list into a list of integers Users are allowed to input many variations of entities and IDs for any given command. This routine parses the input and returns a regular list of valid IDs for the specified entity type. For example:

type – The specific entity type represented by the list of entities

entity_list_string – The string that contains the entity list

A list of valid ids for the given type within the specified parameters.

Get the arc length of a specified curve

curve_id – ID of the curve

Arc length of the curve

Get the block name for a given block id.

block_id – Id of block in question

Block name associated with this block or “” if none

Get the center point of the arc

curve_id – ID of the curve

x, y, z center point of the curve

Get the length of a specified curve

curve_id – ID of the curve

Get the radius of a specified arc

curve_id – ID of the curve

Get the distance from a point on a curve to the curve’s start point

x – value of the point to measure

y – value of the point to measure

z – value of the point to measure

curve_id – ID of the curve

Distance from the xyz to the curve start

Get the center point of a specified entity.

entity_type – Specifies a string representing the geometry type of the entity

entity_id – Specifies the id of the entity

The x, y, z, coordinates of the center point

Given 2 surfaces, get the common curve id

surface_1_id – The id of one of the surfaces

surface_2_id – The id of the other surface

The id of the curve common to the two surfaces

Given 2 curves, get the common vertex id

curve_1_id – The id of one of the curves

curve_2_id – The id of the other curves

The id of the vertex common to the two curves, 0 if there is none

Get all entities of a specified type (including geometry, mesh, etc…).

entity_type – Specifies the type of the entity

A tuple of ids of the specified geometry type

Get the list of nearby entities of type curve, surface or volume given a list of the same entity type. For example, given one or more volumes, find all the volumes that are closer than a specified distance.

gtype – "curve", "surface" or "volume"

ent_ids – Find entities close to the entities in this list.

compare_ents – Entities of same type to check against. If empty, will check against all of them.

distance – Maximum distance betwen entities. Optional. Use -1 to compute default tolerance.

A list of entities of type gtype that are nearby to ent_ids from the compare_ents list.

Get the color of a specified entity.

entity_type – Specifies the type of the entity

entity_id – Specifies the id of the entity

The color of the entity (r, g, b, a). Note that (0,0,0,0) denotes the default color.

tuple[float], length 4

Get the name of a specified entity Names returned are of two types: 1) user defined names which are actually stored in Coreform Cubit when the name is defined, and 2) ‘default’ names supplied by Coreform Cubit at run-time which are not stored in Cubit. The second variety of name cannot be used to query Coreform Cubit.

entity_type – Specifies the type of the entity

entity_id – Specifies the id of the entity

no_default – True to return an empty string if no name is set

The name of the entity

Get the number of errors in the current Coreform Cubit session.

The number of errors in the Coreform Cubit session.

Get the current merge tolerance value

The value of the current merge tolerance

Get the interval count for a specified entity.

geom_type – Specifies the geometry type of the entity

entity_id – Specifies the id of the entity

The entity’s interval count

Get the mesh scheme for the specified entity.

geom_type – Specifies the geometry type of the entity

entity_id – Specifies the id of the entity

The entity’s meshing scheme

Get the mesh size for a specified entity.

geom_type – Specifies the geometry type of the entity

entity_id – Specifies the id of the entity

The entity’s mesh size

Get the area of a surface

surface_id – ID of the surface

Get the surface centroid for a specified surface

surface_id – ID of the surface

tuple[float], length 3

Get the surface normal for a specified surface

surface_id – ID of the surface

surface normal at the center

tuple[float], length 3

Get the surface normal for a specified surface at a location

surface_id – ID of the surface :param coord: array of x,y,z location on surface

surface normal at coord

tuple[float], length 3

Get the total volume for a list of volume ids

volume_list – List of volume ids

The total volume of all volumes indicated in the id list

Get the Coreform Cubit version.

A string containing the current version of Coreform Cubit.

Get the area of a volume

volume_id – ID of the volume

Get the volume of a volume

volume_id – ID of the volume

Get the list of volumes that are within a given distance of a specified volume.

volume_id – id of the volume to check

compare_volumes – list of volume ids to check against. If the list is empty, all volumes in the model are checked

distance – maximum distance between volumes. Use -1 to compute a default tolerance

list of volume ids from compare_volumes that are nearby to volume_id

Get the sense of a surface with respect to a specified volume.

surface_id – ID of the surface

volume_id – ID of the volume

the sense of the surface with respect to the volume: “Forward”, “Reversed”, or “Both”. Returns an empty string if the surface or volume does not exist

Get the parametric (u, v) location of a given point on a surface.

surface_id – ID of the surface

position – x, y, z location on the surface

u, v parametric location on the surface

Get the x, y, z position on a surface for a given parametric (u, v) location.

surface_id – ID of the surface

u – u parametric coordinate

v – v parametric coordinate

x, y, z location on the surface

Determines whether a specified entity is merged.

geom_type – Specifies the geometry type of the entity

entity_id – Specifies the id of the entity

Determines whether a specified entity is meshed.

geom_type – Specifies the geometry type of the entity

entity_id – Specifies the id of the entity

Query whether a specified surface or curve is periodic.

geom_type – Specifies the geometry type of the entity

entity_id – Specifies the id of the entity

True is entity is periodic, otherwise false

Determine if given point is inside, outside, on or unknown the given entity. note that this is typically used for volumes or sheet bodies

geom_type – string defining geometry type (volume or body)

id – ID of the geometric entity

xyz_point – triplet defining the point x,y,z coordinates

tuple[float], length 3

-1 failure, 0 outside, 1, inside, 2 on

Check if surface is meshable with current scheme.

A boolean indicating whether surface is meshable with current scheme.

Query if the given surface is planar.

surface_id – Specifies the id of the surface

Check if volume is meshable with current scheme.

A boolean indicating whether volume is meshable with current scheme

Query whether a specified volume is a sheet body

volume_id – Id of the volume

True if volume is a sheet body, otherwise false

Returns distance between two geometry entities and their closest points.

entity_type1 – type of first entity

entity_id1 – id of first entity

entity_type2 – type of second entity

entity_id2 – id of second entity

str, one of “vertex”, “curve”, “surface”, “volume”, “node”, “edge”, “tri”, “face”, “tet”, “hex”, “wedge”, “pyramid”

The distance between two entities

Fire a ray at a list of target entities and return the hit locations and the ids of the entities that were hit.

origin – x, y, z coordinate of the ray start point

direction – x, y, z vector defining the ray orientation

target_type – type of entity to test for intersections

target_ids – one or more entity ids for the targets

max_hits – (optional) number of intersection hits to find. If 0, all intersections are found

ray_radius – (optional) a tolerance on the ray for intersection calculations

target_type is a str, one of “vertex”, “curve”, “surface”, “volume”, or “body”

A pair containing the list of hit locations and the list of ids of the hit entities of the specified target_type. No ids are returned for intersections that are not of the specified type.

tuple[list[float], list[int]]

Check whether an entity of the given type and id exists.

entity_type – type of the entity being queried

entity_id – id of the entity being queried

entity_type is a str, one of “body”, “volume”, “surface”, “curve”, “vertex”, “group”, “node”, “edge”, “tri”, “quad”, “face”, “tet”, “hex”, “wedge”, “pyramid”, “block”, “nodeset”, or “sideset”

whether the entity exists

Check whether a GUI graphics window is enabled.

whether a graphics window is enabled

Get id for a named entity This routine returns an integer id for the entity whose name is passed in.

name – Name of the entity to examine return Integer representing the entity

The id associated with the given name.

Get the id of the last created entity of the given type.

entity_type – Type of the entity being queried

str, one of “body”, “volume”, “surface”, “curve”, “vertex”, “group”, “node”, “edge”, “tri”, “quad”, “face”, “tet”, “hex”, “wedge”, or “pyramid”

The id of last created entity

Get a next available block id

Next available block id

Get the next available group id from Coreform Cubit

Get a next available nodeset id

Next available nodeset id

Get a next available sideset id

Next available sideset id

Get the bounding box for a specified entity.

geom_type – Specifies the geometry type of the entity

entity_id – Specifies the id of the entity

A tuple of coordinates describing the entity’s bounding box. Ten (10) values will be:

[9] = box diagonal length

tuple[float], length 10

Get the bounding box for a list of entities.

geom_type – Specifies the geometry type of the entity

entity_list – List of ids associated with geom_type

An array of coordinates for the entity’s bounding box.

[9] = box diagonal length

tuple[float], length 10

Get the tight bounding box for a list of entities.

geom_type – Specifies the geometry type of the entity

entity_list – List of ids associated with geom_type

A tuple of center point coordinates and axis definitions.

[3] = normalized u component 0

[4] = normalized u component 1

[5] = normalized u component 2

[6] = normalized v component 0

[7] = normalized v component 1

[8] = normalized v component 2

[9] = normalized w component 0

[10] = normalized w component 1

[11] = normalized w component 2

tuple[float], length 15

Get the node closest to the given coordinates

id of closest node, 0 if none found

Get the list of node ids contained within a mesh entity.

entity_type – The mesh element type

entity_id – The mesh element id

Get the list of node ids contained within a mesh entity, including interior nodes.

entity_type – The mesh element type

entity_id – The mesh element id

Tuple of all node ids associated with the element, including interior (high-order) nodes

Return the type of a given element

element_id – The element id (i.e. the global element export id)

Get the geometric owner of this mesh element.

entity_type – The mesh element type

entity_id – The mesh element id

Get the nodal coordinates for a given node id.

node_id – The node id

A tuple containing the x, y, and z coordinates

tuple[float], length 3

Get the list of hex elements forming a hex column through the given quad/face. Note that quad elements normally only exist on surfaces, so the starting face and the column start will exist on a surface. Free mesh must be skinned to have a starting quad.

quad_id – id of the quad/face element to start the column from

the list of hex element ids forming the column

Create a NURBS curve from a set of control points, weights, and a knot vector.

degree – the degree of the NURBS curve

ctrl_pts – a list of x, y, z coordinates representing the control points, of the form [x0, y0, z0, x1, y1, z1, ... , xn, yn, zn]. The minimum size of this list must be degree + 1

weights – a list of weights for each control point. The size of this list should equal the number of control points

knot_vec – the knot vector for the curve. Its size should be (num_ctrl_pts + degree - 1) or (num_ctrl_pts + degree + 1)

the id of the newly created curve, or -1 if curve creation was unsuccessful

**Examples:**

Example 1 (unknown):
```unknown
cubit.init()
```

Example 2 (unknown):
```unknown
cubit.init()
```

---

## Coreform Cubit Python API: Object-Based API

**URL:** https://coreform.com/cubit_help/python/cubit_python_api_object_based.htm

**Contents:**
- Coreform Cubit Python API: Object-Based API
- Object Creation Methods
- Entity
- GeomEntity
- Body
- Volume
- Surface
- Curve
- Vertex
- Dir

Object Creation Methods

The object-based API provides a more “pythonic” interface. This interface is maintained and tested. There are object modification methods that are not documented here. Those methods are deprecated and are not under current development.

The leaf objects correspond to entities in Coreform Cubit. They are derived from GeomEntity and Entity. All methods defined in the base classes are available in the leaf classes.

Cubit entities should be created using the cmd method. There are operators to convert from an id to an object and back. For example,

Objects can be useful to track and store ids and state.

Cubit objects are created from an id and return an object of the given type.

Creates a body object from an ID

id_in (int) – The ID of the body

Creates a volume object from an ID

id_in (int) – The ID of the volume

Creates a surface object from an ID

id_in (int) – The ID of the surface

Creates a curve object from an ID

id_in (int) – The ID of the curve

Creates a vertex object from an ID

id_in (int) – The ID of the vertex

The base class of all the geometry and mesh types.

Get the bounding box of the Entity.

The bounding box as a vector (or list) where the indices correspond to the values as follows:

tuple[float] length 6

Get the center point of the Entity. Note that this is an approximate centroid.

The center point as a list of length 3 where the indices correspond to the values as follows:

tuple[float], length 3

Get the id of the Entity.

Get the visibility state of the Entity.

The current visiblity state of the Entity (1 if visible, 0 if not)

Get the tranparency state of the Entity.

The current transparency state of the Entity (1 if transparent, 0 if not)

The base class for specifically the Geometry types (Body, Surface, etc.)

Return the current mesh state of the GeomEntity.

Whether the GeomEntity is meshed or not

Smooths the mesh on the GeomEntity.

Removes the mesh on the GeomEntity.

Return the first name of the GeomEntity.

The first name of the GeomEntity

Return the all the names of the GeomEntity.

A tuple strings containing all the names of the GeomEntity

Get the dimensions of the GeomEntity.

The dimension of the GeomEntity

Get the bodies in the GeomEntity.

A tuple of bodies contained within the GeomEntity

Get the volumes in the GeomEntity.

A tuple of volumes contained within the GeomEntity

Get the surfaces in the GeomEntity.

A tuple of surfaces contained within the GeomEntity

Get the curves in the GeomEntity.

A tuple of curves contained within the GeomEntity

Get the vertices in the GeomEntity.

A tuple of vertices contained within the GeomEntity

The Body class contains a Cubit body and provides methods to query the body.

Defines a body object that mostly parallels Cubit’s Body class

Get the mass properties of the Body, specifically the center of gravity.

A tuple of numerical data corresponding to the center of gravity of the body with indices as follows:

Get whether a point is in, on, or outside the Body.

Whether a point is unknown (-1), outside (0), in (1), or on (2) the Body

Get the volume of the Body.

The volume of the Body

Get whether the Body is a sheet body or not.

Whether the Body is a sheet body or not

The Volume class contains a Cubit volume and provides methods to query the volume.

Defines a volume object that mostly parallels Cubit’s RefVolume class

Get the volume of the Volume.

The volume of the Volume

Get the color of the Volume.

The color value associated with the volume’s current color. Note (0.,0.,0.,0.) denotes the default color with no assigned color value.

Get the principal axes of the Volume.

A vector (or list) of the principal axes of the volume with the indices of the vector corresponding to the values as follows:

tuple[float], length 9

Get the principal moments of the Volume.

A vector (or list) of the principal moments of the volume with the indices of the vector corresponding to the values as follows:

tuple[float], length 3

Get the centroid of the Volume.

A tuple of the coordinates of the centroid of the volume with the indices of the tuple corresponding to the values as follows:

tuple[float], length 3

The Surface class contains a Cubit surface and provides methods to query the surface.

Defines a surface object that mostly parallels Cubit’s RefFace class

Get the color of the surface.

The color value associated with the volume’s current color. Note (0.,0.,0.,0.) denotes the default color with no assigne color value.

tuple[float], length 4 (r, g, b, a).

Get the ordered loops of the Surface where the first loop is the outer most loop.

A tuple of tuples of Curves in loops

0, 0 - loop 1 curve 1

0, 1 - loop 1 curve 2

1, 0 - loop 2 curve 1

Get the normal at a particular point on the Surface.

location – A list or tuple containing three values that are the coordinates of a point

A tuple of floats representing values of normal vector as follows

Get the nearest point on the Surface to point specified.

location – A tuple containing three values that are the coordinates of a point

A vector (or list) of doubles representing values of nearest point as follows

Get the nearest point on the Surface to point specified along the specified vector.

location – A list or tuple containing three values that are the coordinates of a point

A tuple of doubles representing values of nearest point as follows

Get whether a point is on or off of the Surface.

point_in (tuple[float] length 3, in) – A vector containing three values that are the coordinates of a point

A python boolean representing whether the point is off (0) or on (1) the Surface

Get the principal curvatures of the Surface.

point (tuple[float], in) – A vector containing three values that are the coordinates of a point

A list of two floats representing the curvatures

tuple[float], length 2

Get the Cartesian coordinates from the uv coordinates on the Surface.

u (float, in) – The u parameter

The Cartesian coordinates of the supplied uv coordinates as a vector.

tuple[float], length 3

Get the uv coordinates from the supplied Cartesian coordinates on the Surface.

location (list[float] in) – A vector containing the Cartesian coordinates

tuple[float] length 2

Get range of u for the Surface.

tuple[float], length 2

0 - The lowest value in the u direction

1 - The highest value in the u direction

Get range of v for the Surface.

tuple[float], length 2

0 - The lowest value in the v direction

1 - The highest value in the v direction

Get area of the Surface.

The area of the Surface

Get whether the Surface is planar or not.

Whether the Surface is planar or not

Get whether the Surface is cylindrical or not.

Whether the Surface is cylindrical or not

Get the dihedral angle between this surface and another surface at a fraction along the shared curve between them.

other (Surface) – The other surface object used to form the dihedral angle

fraction (float) – The fraction along the shared curve at which to calculate the dihedral angle (0.0 – 1.0)

the dihedral angle between the surfaces, in radians

The Curve class contains a Cubit curve and provides methods to query the curve.

Defines a curve object that mostly parallels Cubit’s RefEdge class

Get the color of the Curve.

The color value associated with the volume’s current color. Note (0.,0.,0.,0.) denotes the default color with no assigne color value.

Get the tangent to the Curve at a particular point.

point (tuple[float], length 3 , in) – A vector containing 3 doubles representing coordinates of a location on the Curve

The tangent to the Curve at the location specified

tuple[float], length 3

Get the curvature of the Curve at a particular point.

point (tuple[float], length 3, in) – A vector containing 3 doubles representing coordinates of a location on the Curve

The curvature of the Curve at the location specified

tuple[float], length 3

Get the curvature of the Curve at a particular point.

point (tuple[float], length 3, in) – A vector containing 3 doubles representing coordinates of a location on the Curve

The closest point to the Curve from the location specified

Get the curvature of the Curve at a particular point.

point (tuple[float], length 3, in) – A vector containing 3 doubles representing coordinates of a location on the Curve

The closest point to the Curve from the location specified

Get the length of the Curve.

The length of the Curve

Get the center point of the Curve.

A vector containing the coordinates of the Curve’s center according to the following:

tuple[float], length 3

Get the position of the point a specified fraction along the Curve.

fraction_along_curve (float, in) – A decimal value between 0 and 1 to determine a particular position along the Curve

A vector containing the coordinates of the position a specified fraction along the Curve:

Get the lowest value of the Curve in uv space.

The beginning value of the parameter

Get the highest value of the Curve in uv space.

The ending value of the parameter

Get the u value of a particular position on the Curve.

position (tuple[float], length 3, in) – A vector containing the coordinates of the input position

The u value of the position along the Curve

Get the position of a particular u value for the Curve.

u_value (float, in) – The u value of the position along the Curve

A vector containing the coordinates of the output position

Get the u value for a point a specified arc length away from a specified root parameter on the Curve.

root_param (float, in) – The beginning parameter from which the arc length is added to

arc_length (float, in) – The length away from the root parameter of the output parameter

The u value of the Curve the arc length away from the root parameter

Get the fraction along the Curve a specified arc length is away from a given Vertex.

root_vertex (Vertex, in) – The Vertex to start from (vertex object)

length (float, in) – The length along the Curve away from the root Vertex

The fraction of the Curve that is the specified length away from the specified Vertex

Get the position on a Curve that is a specified arc length away from the specified root parameter.

root_param (float, in) – The root parameter from which the arc length is added to

arc_length (float, in) – The arc length along the Curve away from the root parameter

A vector that contains the coordinates of a position a specified arc length away from the root parameter

Get the length between two specified parameters on a Curve.

parameter1 (float, in) – The beginning parameter

parameter2 (float, in) – The ending parameter

The length between the two specified paramters along the Curve

Get whether the Curve is periodic or not.

Whether the Curve is periodic or not

Get the dihedral angle between this curve and another curve relate to the given surface.

other (Curve) – The other curve object that forms a dihedral angle with this one.

common_surface (Surface) – Surface object that contains both curves.

the dihedral angle between the curves, in radians

The Vertex class contains a Cubit vertex and provides methods to query the vertex.

Defines a vertex object that mostly parallels Cubit’s RefVertex class

Get the color of the Vertex.

The color value associated with the vertex’s current color

tuple[float], length 4

Get the Cartesian coordinates of the Vertex.

A vector containing the coordinates of the Vertex with indices corresponding to the coordinates as follows:

The Dir class stores and manipulates a vector used as a direction.

Defines a direction object

Get the x location of the point

float See also: y(), z()

Get the y location of the point

float See also: x(), z()

Get the z location of the point

float See also: y(), x()

Set the x location of the point

x_in (float) – the new x value

Set the y location of the point

y_in (float) – the new y value

Set the z location of the point

z_in (float) – the new z value

Get an array of the vector

Normalize ‘this’ vector :return: void :rtype: void

Set the xyz values of the vector

Returns the cross product of this X vec2

Returns the dot product

get the distance between two points

Returns the interior angle of two vectors. The return the angle is in radians.

Finds 2 (arbitrary) vectors that are orthogonal to this one

---

## Python Cubit Enhancement Scripts

**URL:** https://coreform.com/cubit_help/appendix/python/python_cubit_enhancement_scripts.htm

**Contents:**
- Python Cubit Enhancement Scripts

The Python-Cubit enhancement code base is intended to be used as an extension to already existing Cubit functionality. It provides the user with a number of functionalities that are either currently outside the realm of the python functions which cubit supplies internally (such as vector math), or that are comprised of commonly used combinations of already existing python functionalities.

Python Cubit Enhancement Scripts

---

## Python Interface

**URL:** https://coreform.com/cubit_help/appendix/python/cubit_python_interface.htm

**Contents:**
- Python Interface
- Functions
- Classes

The following Python functions and objects provide capability to query and modify Cubit models.

CubitInterface - Cubit model query and modify functions.

Entity - The base class of all the geometry and mesh types. GeomEntity - The base class for specifically the Geometry types (Body, Surface, etc.). Body - Defines a body object that mostly parallels Cubit's Body class. Volume - Defines a volume object that mostly parallels Cubit's RefVolume class Surface - Defines a surface object that mostly parallels Cubit's RefFace class. Curve - Defines a curve object that mostly parallels Cubit's RefEdge class. Vertex - Defines a vertex object that mostly parallels Cubit's RefVertex class. CFD BC Interface -Defines the interface to CFD Boundary Condition entities Direction Interface -Defines the interface to a Direction object Location Interface -Defines the interface to a Location object CubitFailureException - An exception class to alert the caller when the underlying Cubit function fails. InvalidEntityException - An exception class to alert the caller that an invalid entity was attempted to be used. InvalidInputException - An exception class to alert the caller of a function that invalid inputs were entered. MeshError - Mesh error interface AssemblyItem - AssemblyItem interface

---

## The Coreform Cubit Python API

**URL:** https://coreform.com/cubit_help/python/cubit_python_api.htm

**Contents:**
- The Coreform Cubit Python API

Coreform Cubit's Application Programming Interface (API) for Python provides methods that allow Coreform Cubit to be scripted to automatically to create meshes and geometry for complex models. It can be used to generate models for parametric studies where either geometric or mesh parameters are changed. It also provides archival capabilities to recreate models without having to store large datasets.

The Coreform Cubit Python API presents some of the most commonly used commands. The graphical user interface for Coreform Cubit is implemented using the C++ version of these commands. These commands are maintained, used, tested, and being developed.

The API is designed to be a read only interface. All modification to Coreform Cubit should be completed by executing Cubit commands. This is done with the cmd method.

There are a number of functions in the API that are not presented here, but they can be found in the Appendix. Many of the skipped commands can be implemented using the commands presented here. For example, there is an API function to get the hexahedral elements in a volume. Most users should prefer the command parse_cubit_list. For example,

In addition to the method based API there are also Cubit objects. Only the query methods are documented here. The object modification methods are not supported.

The API is documented in the following sections.

Object Creation Methods

**Examples:**

Example 1 (unknown):
```unknown
parse_cubit_list
```

---

## use iface ...

**URL:** https://coreform.com/cubit_help/appendix/python/namespacecubit.htm

**Contents:**
- Classes
- Functions
- Variables
- Function Documentation
- ◆ add_entities_to_group()
- ◆ add_entity_to_group()
- ◆ add_filename_to_recent_file_list()
- ◆ add_filter_type()
- ◆ app_util()
- ◆ are_adjacent_curves()

Add a list of entities to a specified group.

.. code-block:: python

Add a specific entity to a given group.

.. code-block:: python

Add a filename to Cubit's recent-file list in the GUI File menu.

Registers the specified file path so it appears under "Recent Files" in Cubit's GUI.

Add an entity type to the graphics pick filter.

Allows picking entities of the specified type in addition to any existing filters.

Return Cubit's AppUtil interface for global services.

Provides access to application-level utilities–logging, configuration, file I/O, and more–required by higher-level modules like CubitML.

Python usage example:

.. code-block:: python

Typically used together with cgm_iface() to bootstrap ML workflows.

return type of : std:: shared_ptr< AppUtil >

Return whether two or more curves share at least one manifold vertex.

Given a list of curve IDs, this function returns whether the curves are adjacent. Two curves are considered adjacent if they share at least one manifold vertex: a vertex that is connected to exactly two curves.

If the shared vertex is connected to more than two curves, the curves are not considered adjacent .

Return whether two or more surfaces share at least one manifold curve.

Given a list of surface IDs, this function returns whether the surfaces are adjacent. Two surfaces are considered adjacent if they share at least one manifold curve (a curve that is part of exactly two surfaces).

Check if automatic mesh sizing is outdated and needs recomputation.

Returns true if the model has changed since the last auto size calculation, indicating that automatic sizes (which can be expensive to compute) should be recalculated before generating a mesh.

if cubit.auto_size_needs_to_be_calculated() : cubit.cmd ("volume 1 size auto factor 3")

Find the best edge to collapse to remove an interior node in a triangular mesh.

For a given interior mesh node (no geometry association), this function identifies the best adjacent edge whose collapse would remove the node. If no suitable edge is found, returns 0.

if best_edge > 0: print(f"Collapse interior node 50 along edge {best_edge}") else:

Retrieve a body by its ID.

Retrieves the body object corresponding to the provided ID.

Create a brick of specified width, depth, and height.

Creates a brick geometry with the given dimensions. If only width is provided (depth and height default to -1), a cube of side length width is generated.

Estimate the time step based on element sizes and material properties.

Calculates a time step estimate for specified mesh elements of a given type. Supported "tet", "hex", "volume", "block", "group". Elements must belong to a single block with an assigned material defining at least elastic_modulus, poisson_ratio, and density.

Estimate the stable time step using user-specified material properties.

Calculates a time step estimate for mesh elements of the given type, using provided density, Young's modulus, and Poisson's ratio rather than block-assigned materials.

Return the raw CGMApp kernel instance used by Cubit.

Grants direct access to lower-level CGM application calls (version, kernel settings, etc.).

return type of : CGMApp

Return the CGM-based geometry interface for Cubit.

Yields a CubitGeometryInterface implemented on the CGM kernel, enabling CAD topology queries and edits needed for ML feature extraction.

Python usage example:

.. code-block:: python

Use this interface for all geometry operations in the ML pipeline.

return type of : CubitGeometryInterface

Clear all geometry in a named drawing set (e.g., mesh preview).

Removes any preview graphics associated with the specified set name, leaving the set empty for fresh drawing operations.

Clear all entity highlights.

Removes highlights and selections from every entity in the graphics window.

Clear the list of currently picked entities.

Empties the internal pick list without altering the pick filter or highlights.

Clear preview graphics without affecting other display settings.

Removes only the temporary preview without altering the main geometry or mesh visibility.

Execute a raw Cubit command string immediately (modifies model state).

This is one of the two primary ways (silent_cmd) to change the CAD model within Cubit. Sends the exact command text to Cubit for execution with no pre-validation. See Cubit's command syntax in the online documentation for a full description.

Query whether any child entities of a specified geometry entity are virtual.

.. code-block:: python

Check if a convection BC is on a shell top or bottom.

type of entity_id: int

Check if a convection BC is on a solid.

type of entity_id: int

Create a duplicate of the specified body.

Returns a new Body object that is an exact copy of the input body, including geometry and mesh data.

Create an arc curve using end vertices and an intermediate point.

Constructs a circular arc passing through the specified start and end vertices and the given intermediate point.

Create a curve between two vertices.

Constructs a straight-line curve connecting the two specified vertices.

Create a new, empty group and return its ID.

.. code-block:: python

Create a spline curve through a sequence of 3D points on a surface.

Constructs a smooth spline curve passing through the provided points, projected onto the specified surface. Projection is mandatory: the surface_id must refer to an existing surface entity. At least two points are required; otherwise, a CubitFailureException is thrown. A non-existent surface_id produces an InvalidEntityException . Other errors during projection or spline creation will result in a CubitFailureException or runtime error.

Create a sheet body from boundary curves.

Constructs a sheet body bounded by the specified closed curves. The returned Body contains exactly one surface and one volume. To access the underlying Surface , retrieve it from the body's surface list.

Create a vertex at specified coordinates.

Creates a 0-dimensional geometric entity (vertex) at the given (x, y, z) location. If no coordinates are specified, the vertex is placed at the origin (0,0,0).

Get the number of entities in the current selection list.

Returns how many entities have been picked and are available for navigation.

Retrieve a curve object by its ID.

Retrieves the curve object corresponding to the provided ID.

Create a cylinder or truncated cone of specified dimensions.

Creates a cylindrical or conical body based on provided bottom and top radii. A zero top radius yields a cone; a top radius equal to the x and y radii yields a straight cylinder.

Remove all groups from the current Cubit session.

.. code-block:: python

Delete a specific group by ID.

.. code-block:: python

Shut down Cubit and close the active journal file.

Flushes any pending commands, closes the journal, and releases Cubit resources. After calling destroy() , no further Cubit calls should be made.

Check if developer commands are enabled.

Returns true if Cubit is running in developer mode, allowing access to internal or experimental commands.

if cubit.developer_commands_are_enabled() : print("Developer commands are enabled.")

Compute ML predictions for a list of operations with multiple entities.

This is a batch variant of get_ML_predictions() that accepts lists of entity IDs per operation, enabling more flexible inputs. Features are computed and predictions are generated via a scikit-learn ensemble of decision trees.

type of ml_op_names: std::vector< std::string,std::allocator< std::string > >

Check whether an entity of the specified type and ID exists.

This function returns true if an entity of the given type and ID exists in the model; otherwise it returns false .

Supported entity types include: "vertex", "curve", "surface", "volume", "body", etc.

Find curves whose exterior angle between adjacent surfaces is less than a given threshold.

This function implements the Cubit "draw curve with exterior_angle < test_angle" test. For each curve in curve_list, it computes the exterior angle (the angle on the outside of the volume) between the two faces sharing that curve and returns those curves whose exterior angle is below test_angle.

Return the exterior angle at a single curve with respect to a volume.

Computes the exterior angle (in degrees) on the outside of the specified volume between the two faces sharing the given curve.

Return the interior angle at a vertex on a specified surface.

Computes the angle in degrees between the two edges meeting at vert_id on surf_id, measured inside the surface. For a planar cube face, each corner vertex has an interior angle of 90 degrees.

Check if the Exodus sizing function file currently exists.

Returns true if an Exodus II file has been imported as a sizing function and still resides on disk; returns false otherwise.

Identify cone surface(s) starting from a candidate surface.

Given a surface ID, this function determines if the surface is part of a cone. If the surface is a cone with an adjacent surface also part of the same cone, both surface IDs are returned. Otherwise, only the input surface ID is returned.

Identify overlapping curves in a specified list of curves.

The result is a vector of vectors. Each vector contains the IDs of curves that overlap with one another. Only overlaps between curves of different volumes or touching surfaces are reported.

for overlap in my_overlaps: print("Curves:", tuple(int(cid) for cid in overlap))

Force immediate rendering of pending graphics operations.

Ensures that any queued draw calls (for example, draw location or mesh preview) are displayed before subsequent commands execute. Requires an active graphics window.

Gathers surfaces connected across shared edges, forming a surface enclosure.

Starting from a list of seed surfaces, recursively finds and returns all surfaces that are connected to them across shared edges. The resulting set typically forms a closed or connected surface group (enclosure).

If all_surf_ids is provided, the search is limited to those surfaces. If empty, all model surfaces are considered.

This function is useful for finding surface enclosures, identifying connected outer boundaries, or selecting surface groups in models with voids or non-manifold geometry.

Get associated 2D sheet volumes from a reduced 3D thin volume.

Returns the IDs of sheet bodies created from a 3D thin volume using reduce thin commands. These sheet volumes preserve thickness and loft attributes for shell FEA purposes.

Get the original 3D thin volume associated with a 2D sheet volume.

Used to retrieve the parent 3D geometry from a 2D sheet volume generated by a reduce thin operation. Supports traceability in shell FEA workflows.

Get the combine method for an acceleration BC.

Valid options include "Overwrite", "Average", "SmallestCombine", or "LargestCombine". type of entity_id: int

Retrieve the ACIS kernel version string.

Returns the ACIS geometric modeling kernel version used by Cubit.

Retrieve the ACIS kernel version as an integer.

Returns the ACIS version encoded as an integer (e.g., 202107 for version 2021.07).

Get a list of surfaces adjacent to a specified surface (including the surface itself).

For a given surface, this returns all surfaces that either own the specified entity or share a boundary with it. The returned list includes the queried surface as well.

Get a list of adjacent volumes to a specified entity.

For a specified entity, find all volumes that own the entity and volumes that touch the volume that owns this entity.

Get all available time steps from an Exodus file.

Opens an Exodus II file and returns a vector of all stored time values (time steps). These time values are used when importing deformed meshes (via the Time <time> or Step <step> options) to select which deformation state to import. The last time in the list corresponds to the default import time.

for t in times: print(" Time:", t)

Get all variable names of a given type from an Exodus file.

Opens an Exodus II file and returns a vector of all variable names of the requested type. These variable names are used when importing nodal or element variable data into Cubit via the nodal_var and element_var import options.

Valid variable types:

for var_name in nodal_vars: print(" ", var_name)

Get the list of geometric owners for a set of mesh entities and their child entities.

Returns the geometric owners of the specified mesh entities and any child entities (e.g., edges or nodes of a quad).

Title Supported mesh entity types

Retrieve all IDs of entities of a specified geometry type whose names start with a given prefix.

.. code-block:: python

Get the numeric value of a specified Aprepro variable.

Aprepro is a lightweight macro language in Cubit used for variable substitution and simple scripting.

Get the string value of an Aprepro variable.

Aprepro is a lightweight macro language in Cubit used for variable substitution and simple scripting.

Retrieve the current Aprepro variable names.

Aprepro is a lightweight macro language in Cubit used for variable substitution and simple scripting.

Get the center point and radius of a specified arc curve.

If the curve is a circular or elliptical arc (e.g., an end circle of a cylinder), returns its center (X,Y,Z) and constant radius. For any other curve type, returns {0,0,0,0} and emits a warning.

Get the parametric (arc) length of a specified curve.

Returns the length measured along the curve's parameterization. For most curves in Cubit, this matches the physical 3D length, but for certain spline or NURBS representations, arc length may be computed by integrating the parametric form.

Get classification category metadata.

return type of : string

Get classification level metadata.

return type of : string

Get the description of an assembly node.

type of assembly_id: int

Get the file format from which the assembly node was imported.

type of assembly_id: int

Get the instance number of an assembly node.

Distinguishes nodes with the same name. type of assembly_id: int

Get the hierarchy level of an assembly node.

Level 0 is the root. type of assembly_id: int

Get the material description for a part.

type of assembly_id: int

Get the material specification for a part.

type of assembly_id: int

Get metadata for a specified volume.

Returns metadata associated with a volume's part, such as part number, description, material info, or file reference. type of volume_id: int

Get the name of an assembly node.

type of assembly_id: int

Get the full path of an assembly node, identifying its hierarchy.

type of assembly_id: int

Get the type of an assembly node ("part" or "assembly").

type of assembly_id: int

Get the units of measurement used in the assembly node.

type of assembly_id: int

Get weapons category metadata.

return type of : string

Predict the automatic mesh size for a set of entities.

Calculates the mesh size (target edge length) that would be applied if the command 'size auto factor n' were issued on the given entities. This does not modify the model or set any sizes-it only returns the value.

Get active boundary condition (BC) IDs of a specified type.

Returns a list of active BC IDs matching the given type enum.

type of bc_type_enum: int

Get the name of a specific boundary condition (BC).

Retrieves the name associated with a given BC ID and type.

type of bc_type_enum: int

Get the temperature value for a specified BC area.

type of bc_type_enum: int

Return collections of surfaces that form blend chains in the specified volumes.

A blend chain is a group of contiguous surfaces that together form a smooth transition feature, such as a fillet or round. Blend chains are filtered by their computed radius.

If radius_threshold is provided, only blend chains with radius less than this value are returned.

for surfaces, radius in blend_collections: print("Blend chain surfaces:", tuple(surfaces), "Radius:", radius)

Returns the blend chains for a given surface.

Given a surface ID, this function returns all blend chains associated with that surface. If the surface is part of one or more blend chains, each chain will be returned as a list of surface IDs.

for chain in blend_chains: print("Blend chain:", tuple(chain))

Find blend (fillet) surfaces within specified volumes.

Iterates over all faces of volumes in target_volume_ids and returns those for which is_blend_surface returns true.

Get the number of attributes assigned to a block.

Each block can store up to 20 attributes, which represent physical properties like material parameters.

Get the name of a specific attribute for a block.

Returns the name associated with the attribute at the specified index for a given block. Attribute names are typically assigned to describe the purpose or meaning of each attribute, such as "thickness" or "thermal_conductivity".

Get the value of a specific attribute for a block.

Returns the floating-point value of the attribute at the specified index for a given block. Attributes are user-defined values assigned to represent physical or material properties in a block, such as shell thickness or temperature.

Get the current number of element blocks in the model.

In Cubit, an element block groups related mesh elements of the same type into a single entity. Blocks can be defined by geometric entities (volumes, surfaces, curves) or by directly specifying mesh entities. Once defined, all elements owned by those entities become part of the block.

Get the list of curve IDs contained in a block.

This function returns the IDs of all curves that are part of the specified block.

for curve_id in curve_ids: print(f" Curve ID: {curve_id}")

Get the list of edge IDs contained in a block.

This function returns the IDs of all edges that are part of the specified block.

for edge_id in edge_ids: print(f" Edge ID: {edge_id}")

Get the number of attributes defined for elements in the specified block.

This returns the number of attribute values associated with each element in a block. Attributes can represent properties like shell thickness, material coefficients, etc.

Get the list of attribute names associated with block elements.

Returns the names of all attributes associated with the elements of a given block. These names describe the meaning of each attribute (e.g., "thickness", "material_id").

for name in names: print(name)

Get the element type associated with a block.

Returns the finite element type (e.g., HEX8, HEX20, TET10) used in the specified block.

Get the list of face IDs contained in a block.

This function returns the IDs of all face elements that are part of the specified block.

for face_id in face_ids: print(f" Face ID: {face_id}")

Get the list of hexahedron (hex) IDs contained in a block.

This function returns the IDs of all hexahedron (hex) elements that are part of the specified block.

for hex_id in hex_ids: print(f" Hex ID: {hex_id}")

Get the element block ID associated with a geometric entity.

Returns the ID of the element block that is associated with the specified curve, surface, or volume. A geometric entity may be assigned to only one block. If no block is assigned, this function returns 0.

Get a list of all active block IDs.

Returns a vector of all currently active element block IDs in the model. A geometric entity may be assigned to only one block.

for block_id in block_ids: print(" Block ID:", block_id)

Get list of block IDs from a mesh geometry file.

Opens a mesh geometry file (Exodus II format) and returns a vector of all element block IDs defined in the file. This allows users to inspect available blocks before importing the mesh, and to selectively import blocks by ID.

for block_id in block_ids: print(" Block ID:", block_id)

Get the ID of the material assigned to the specified block.

Returns the material ID associated with the block. This ID corresponds to a defined material (as created with material commands). A value of 0 indicates that no material is currently assigned.

Get the list of node IDs contained in a block.

This function returns the IDs of all nodes that are part of the specified block.

for node_id in node_ids: print(f" Node ID: {node_id}")

Get the list of pyramid IDs contained in a block.

This function returns the IDs of all pyramid elements that are part of the specified block.

for pyr_id in pyramid_ids: print(f" Pyramid ID: {pyr_id}")

Get the list of surface IDs contained in a block.

This function returns the IDs of all surfaces that are part of the specified block.

for surf_id in surface_ids: print(f" Surface ID: {surf_id}")

Get the list of tetrahedron (tet) IDs contained in a block.

This function returns the IDs of all tetrahedron (tet) elements that are part of the specified block.

for tet_id in tet_ids: print(f" Tet ID: {tet_id}")

Get the list of triangle (tri) IDs contained in a block.

This function returns the IDs of all triangle elements that are part of the specified block.

for tri_id in tri_ids: print(f" Tri ID: {tri_id}")

Get the list of vertex IDs contained in a block.

This function returns the IDs of all vertices that are part of the specified block.

for vertex_id in vertex_ids: print(f" Vertex ID: {vertex_id}")

Get the list of volume IDs contained in a block.

This function returns the IDs of all volumes that are part of the specified block.

for vol_id in volume_ids: print(f" Volume ID: {vol_id}")

Get the list of wedge IDs contained in a block.

This function returns the IDs of all wedge elements that are part of the specified block.

for wedge_id in wedge_ids: print(f" Wedge ID: {wedge_id}")

Get all block IDs and their associated material IDs.

Returns a list of all existing block IDs and the corresponding material ID assigned to each. This function helps identify which blocks are assigned materials. Blocks without an assigned material will have a material ID of 0 in the returned pair.

for pair in block_mats: print("Block", pair[0], "has material", pair[1])

Computes the default depth used to blunt a tangency at a vertex.

Used with the blunt tangency command to eliminate small angles caused by fillets. This function estimates the default depth parameter based on the specified angle and whether material is added or removed.

Get the current number of bodies in the model.

.. code-block:: python

Get the normalized axis vector of a bolt volume.

Returns the primary axis direction of the specified bolt geometry, normalized to unit length. If the volume is invalid or the axis cannot be determined, the returned vector will be [0, 0, 0].

Identify clamped members associated with a bolt.

Returns the ordered list of volume IDs that represent the bolt's clamped components:

If nearby_vols is empty, Cubit will automatically determine nearby volumes (less efficient).

for group in clamped: print(group)

Get local coordinate system for a bolt or bolt hole.

Returns the coordinate system as three 3D points defining the origin, the Z-direction point, and a point in the XZ plane. This is useful for aligning or analyzing bolt and hole geometry in local space.

For hole-based queries, only one surface from the hole is needed; it must uniquely identify the hole.

Get the shank diameters of specified bolt volumes.

Returns the estimated shank diameter for each volume in the input list. Volumes that are invalid or for which the diameter cannot be determined will return a value of 0.

type of vol_ids: std::vector< int,std::allocator< int > >

Identify upper and lower pilot hole surfaces from clamped members.

Analyzes the provided volumes or blocks to extract the top and bottom surfaces of pilot holes (e.g., for bolts) based on radius and proximity criteria. The output can be passed directly to reduce bolt commands.

Identify concentric pilot holes across clamped members.

Analyzes a list of clamped volumes or blocks to identify sets of concentric holes that qualify as bolt pilot holes, based on a maximum radius and proximity criteria. Returns detailed information including hole surfaces, radii, axes, and associated volumes.

for hole in pilot_holes: print("Bearing volume:", hole.bearingVolume, "radius:", hole.bearingRadius)

Get the equivalent Shigley frustum radius at the bolt interface.

Calculates the radius of a Shigley-style frustum representing the stress cone between upper and lower volumes surrounding a bolt. This is typically used to evaluate stress distribution. A standard angle of 30 degrees is common.

Optionally accounts for a washer in the bolt-washer clamp mechanism by specifying its entity ID (set to 0 if no washer is used).

Get the washer volume ID associated with a given bolt.

Returns the volume ID of the washer corresponding to the specified bolt ID. If no washer is associated with the bolt, the function returns 0.

Identify bolts clamping the given volumes or blocks.

Performs ML-based classification on provided candidate volumes to identify which are bolts, then checks which of those bolts clamp the specified clamped members.

Retrieve default boolean-valued sculpt parameter.

Matches the input variable name substring to known sculpt parameters and returns its default.

Title Available boolean parameters

type of variable: string

Get the algorithm type used by the specified boundary layer.

Returns the name of the algorithm (e.g., "Structured", "Unstructured"). type of boundary_layer_id: int

Get the continuity setting of a boundary layer.

Indicates whether the boundary layer is continuous across adjacent entities. type of boundary_layer_id: int

Get a list of all defined boundary layer IDs.

return type of : std::vector< int,std:: allocator< int > >

Get all boundary layers associated with a specified base entity.

Retrieves boundary layer IDs that use the given base entity. type of base_type: string

Get all boundary layers associated with a base-parent pair.

Returns boundary layers defined using both the base and parent entities. type of base_type: string

Get the axis-aligned bounding box for a specified entity.

.. code-block:: python

Title: Array contents

Retrieve the Cubit build number.

Returns the build identifier for the current Cubit binary.

Return the surfaces in the cavity adjacent to the specified surface.

The function returns a list of surface IDs that belong to the same cavity as the given surface. The input surface_id must already be part of a cavity. The result includes surface_id itself.

Get the 3D center or coordinates of a specified entity.

Returns the centroid for geometry entities (body, volume, surface), midpoint for curves, coordinates for vertices, or center for mesh entities (node, edge, face, tri, quad, hex, tet, wedge, pyramid, sphere).

Get the CFD boundary condition subtype.

type of entity_id: int

Return collections of surfaces that form chamfer chains in the specified volumes.

A chamfer chain is a group of contiguous planar surfaces that together form a chamfer feature. Chamfer chains are filtered by their computed thickness (distance between chamfer edges).

If thickness_threshold is provided, only chamfer chains with thickness less than this value are returned.

for surfaces, thickness in chamfer_collections: print("Chamfer chain surfaces:", tuple(surfaces), "Thickness:", thickness)

Returns the chamfer chains for a given surface.

Given a surface ID, this function returns all chamfer chains associated with that surface. If the surface is part of one or more chamfer chains, each chain will be returned as a list of surface IDs.

for chain in chamfer_chains: print("Chamfer chain:", tuple(chain))

Get the list of chamfer surfaces for a list of volumes.

type of target_volume_ids: std::vector< int,std::allocator< int > >

Compute the minimum separation distance between loops on a surface.

For a surface with two or more boundary loops, returns the smallest distance between any two loops. If the surface has fewer than two loops, returns 0.

Find faces with multiple loops closer than a given threshold.

Iterates over all faces of volumes in target_volume_ids. A face is included if it has two or more boundary loops and the minimum distance between any two loops is <= mesh_size.

This differs from get_narrow_regions and get_surfs_with_narrow_regions by only checking loop-to-loop proximity on faces with multiple loops, rather than edge splits or oriented edge-pair tests.

Find faces with multiple loops closer than a threshold and return their minimum loop separations.

Iterates over all faces of volumes in target_volume_ids. A face is included if it has (genus + 1) loops (where genus = num_loops - 1) and the minimum distance between any two loops is <= mesh_size. Returns a list of [surface_id, min_distance] pairs for each qualifying face.

This function differs from get_close_loops by filtering faces by genus and also returning the minimum loop-to-loop distance for each face.

for sid, dist in results: print("Surface", sid, "has min loop distance", dist) # expect: Surface 9 has min loop distance 1.0

Find pairs of vertices and curves within a specified tolerance across given volumes.

Unlike get_coincident_vertices, which identifies vertices that coincide with other vertices, this function finds vertices that lie within high_tolerance of a curve. Iterates over all vertices and curves of volumes in target_volume_ids and returns pairs whose shortest distance is <= high_tolerance.

for i in range(0, len(pairs), 2): print("Vertex", pairs[i], "is close to Curve", pairs[i+1])

Find faces on closed surfaces whose two boundary edges remain within a distance threshold.

A surface is "closed in U" (or "closed in V") if traversing its U (or V) parameter from minimum to maximum returns to the same point (no open edge). For each face of volumes in target_ids, the following criteria are applied:

This function differs from get_narrow_regions and get_surfs_with_narrow_regions by only considering closed two-loop faces and sampling along their boundary loops, rather than testing all faces or arbitrary edge pairs.

Find the mesh node closest to a given point.

This function searches the current mesh and returns the ID of the node whose coordinates are nearest to the specified (x, y, z) point. If the mesh contains no nodes, it returns 0.

Find vertex pairs within a specified tolerance across given volumes.

Iterates over all vertices of volumes in target_volume_ids and identifies pairs whose distance is <= high_tolerance. Returns a flat list of vertex ID pairs: [v1_a, v1_b, v2_a, v2_b, . . .].

for i in range(0, len(pairs), 2): print("Coincident pair:", pairs[i], "and", pairs[i+1])

Retrieve a specific command from Cubit's history buffer.

.. code-block:: python

for i in range(count): print(cubit.get_command_from_history(i))

Get the number of commands in Cubit's history buffer.

.. code-block:: python

Return a curve shared by two surfaces.

Finds the curve that bounds both input surfaces. Assumes both surface IDs are valid and that only topologically adjacent surfaces can share a curve. Returns -1 if no shared curve exists.

Return a vertex shared by two curves.

Finds the vertex that bounds both input curves. Assumes both curves exist and that only adjacent curves share a vertex. Returns 0 if no shared vertex exists.

Identify full conical surfaces in given volumes.

Detects conical surfaces within the specified volumes that are represented by a single, unsplit surface. Cones that are split into mirrored surface pairs are intentionally not identified by this function. Use get_surface_cone_collections() if detection of both full and split (mirrored) cones is required.

type of target_volume_ids: std::vector< int,std::allocator< int > >

Find surfaces connected to a given set of surfaces.

Given a list of surface IDs, this function groups them into "patches" of connected surfaces (connection means sharing a common curve). Merged surfaces are always excluded.

Title Behavior based on the number of patches found:

Get the list of node IDs comprising a mesh element.

This function returns the connectivity of the specified mesh element by listing the IDs of its corner nodes. The ordering of nodes follows the Exodus convention; see the Exodus documentation for the element type-specific node ordering.

Get the dependent entity of a specified constraint.

type of constraint_id: int

Get the reference point of a specified constraint.

type of constraint_id: int

Get the type of a specified constraint.

type of constraint_id: int

Get the exterior state of a contact pair.

type of entity_id: int

Get the friction value for a contact pair.

type of entity_id: int

Get the general contact state.

type of entity_id: int

Get the tied state of a contact pair.

type of entity_id: int

Get the lower bound tolerance for a contact pair.

type of entity_id: int

Get the upper bound tolerance for a contact pair.

type of entity_id: int

Returns collections of continuous curves in the given volumes.

Continuous curves are defined as curves connected at 2-valent vertices, where the tangents at the common vertex form an angle of 180 degrees +/- the specified angle tolerance.

for curve_ids, total_length in collections: print("Curve IDs:", curve_ids, "Length:", total_length)

Return the list of adjacent continuous curves.

Two curves are considered continuous if the angle between them at a shared vertex is 180 degrees +/- angle_tol.

The returned list includes the input curve_id and any connected continuous curves.

If require_two_valent is true, continuity does not extend across vertices connected to more than two curves.

Returns collections of continuous surfaces in the given volumes.

Continuous surfaces are defined as surfaces connected at 2-valent curves, where the surface normals at the common curve form an angle of 180 degrees +/- the specified angle tolerance.

for surface_ids, total_area in collections: print("Surface IDs:", surface_ids, "Area:", total_area)

Return the list of adjacent continuous surfaces.

Two surfaces are considered continuous if the exterior angle between them at a shared curve is 180 degrees +/- angle_tol.

The returned list includes the input surface_id and any connected continuous surfaces.

Get convection coefficient from a convection BC.

type of entity_id: int

Returns a list of coordinate system IDs.

Retrieves the IDs of all coordinate systems currently defined in the model.

In Python, the returned list is a tuple of IDs.

Get the current block behavior setting for geometry copy.

When a geometric entity is copied, this setting controls how blocks are propagated:

Get the current nodeset behavior setting for geometry copy.

When a geometric entity is copied, this setting controls how nodesets are propagated:

Get the current sideset behavior setting for geometry copy.

When a geometric entity is copied, this setting controls how sidesets are propagated:

Retrieve the current Cubit "digits" setting.

Returns the number of digits after the decimal point that Cubit uses when printing numeric output. This corresponds to the value set by the Cubit command set digits N .

Retrieve the current Cubit message handler.

Returns the handler instance currently receiving Cubit messages.

Retrieve IDs of all current geometry entities of a specified type.

Returns the IDs of every geometry entity matching the given type. Supported types are "body", "volume", "surface", "curve", and "vertex".

Notes To include mesh entities (e.g. "node", "element"), use get_entities() .

Get the filename of the current journal file.

Returns the path to the active journal file. With journaling on by default, this shows which file Cubit is writing to upon startup.

Get the "coarse size" parameter for a biased curve, if set.

Returns the user-specified "coarse" interval size for the curve's bias scheme. If no coarse size is set, returns 0.

Get the "fine size" parameter for a biased curve, if set.

Returns the user-specified "fine" interval size for the curve's bias scheme. If no fine size is set, returns 0.

Retrieve the fraction of curve length used as the first interval size.

Returns the first interval length expressed as a fraction of total curve length. (e.g., if fraction = 0.25, the first interval = 0.25 * curve_length).

Query the length of the first interval on a biased curve.

Returns the absolute length of the first (smallest) mesh interval on the curve. This corresponds to the "first_delta" if that form was used, or the automatically computed value.

type of curve_id: int

Retrieve the ratio of first-to-last interval at the start of a biased curve.

Returns the ratio of the length of the first interval to the last interval at the curve's start vertex. Useful for understanding how aggressively the mesh is biased at the beginning.

Retrieve the ratio of first-to-last interval at the end of a biased curve.

Returns the ratio of the length of the first interval to the last interval at the curve's end vertex. Useful for understanding how aggressively the mesh is biased near the end.

Determine if the bias is measured from the curve's start vertex.

By default, any "bias" scheme is applied from the start vertex. If you call "curve <id> reverse bias", this flips the progression so it is measured from the end. This function sets the output boolean to true if the bias progression begins at the start vertex, or false if it was reversed.

Check if the "bias from start" flag has been explicitly set on a curve.

Returns true if the bias-from-start setting (or "reverse bias") has been defined for this curve. If the curve is unmeshed but you have never called "reverse bias", this may still report true (default).

Get the primary geometric progression factor used for biasing a curve.

Retrieves the ratio between successive edge lengths at the start of the curve. This "factor" defines the geometric progression for a biased mesh from the first vertex.

type of curve_id: int

Get the secondary geometric progression factor for a dual-bias curve.

Retrieves the same "factor" used from the end vertices toward the middle when using dualbias. For a dualbias, there is only one factor value (applied symmetrically from both ends).

type of curve_id: int

Retrieve the ratio of last-to-first interval at the start of a biased curve.

Returns the inverse of the first/last ratio at the curve's start vertex (i.e., last interval length / first interval length).

Retrieve the ratio of last-to-first interval at the end of a biased curve.

Returns the inverse of the first/last ratio at the curve's end vertex (i.e., last interval length / first interval length)

Retrieve the vertex ID designated as the start of bias on a curve.

Returns the ID of the vertex used as the bias "start" point when using curve-based vertex sizes. If no custom start vertex is defined, returns -1.

if start_vertex >= 0: print("Start vertex for bias:", start_vertex) # Should print 1

Retrieve the bias scheme type applied to a curve.

Returns a string describing the bias scheme for the specified curve. Possible values include "Bias", "Dualbias", "Multi_bias", or "None".

type of curve_id: int

Retrieve the center point of a specified curve.

Title Center computation

Get the current number of curves in the model.

.. code-block:: python

Get the current number of curves in the specified volumes.

.. code-block:: python

Get the list of edge element IDs on a curve.

This function returns the IDs of all edge elements that are on the specified curve.

for edge_id in edge_ids: print(f" Edge ID: {edge_id}")

Get the 3D length of a specified curve.

This returns the physical length of the curve in model units. For closed curves (e.g., circles), it equals the circumference; for lines, the straight-line distance.

Retrieve the curvature mesh scheme adaptation value for a curve.

Returns the double parameter that controls how node spacing adapts to local curvature. A value of zero produces nearly equal intervals; positive values concentrate nodes in high-curvature regions.

Retrieve the pinpoint mesh scheme locations for a curve.

Returns a list of absolute positions along the curve (measured from the start vertex) where nodes have been placed by the pinpoint scheme.

Get the list of node IDs owned by a curve.

This function returns the IDs of nodes owned by the specified curve. Nodes on the bounding vertices of the curve are excluded.

for node_id in curve_nodes: print(f" Node ID: {node_id}")

Compute the radius of a specified curve.

Get the curve type for a specified curve.

Returns a descriptive string indicating the curve's geometry.

Title Available curve types

Retrieve the default value of a named sculpt parameter.

Matches the given substring against known double-valued sculpt parameters and returns its default.

Title Available parameters

type of variable: string

Compute Cubit's heuristic default automatic mesh size for the current model.

Returns the target edge length determined by Cubit's auto-sizing heuristics (model dimensions, curve lengths, etc.). This is equivalent to running:

.. code-block:: python

Retrieve the current default element type for meshing.

.. code-block:: python

Get the name of the default modeler engine.

The default engine is the geometry kernel used for creating new geometry. ACIS is the default but can be changed to facet.

Get the combine method for a displacement BC.

Valid options include "Overwrite", "Average", "SmallestCombine", or "LargestCombine". type of entity_id: int

Get the Euclidean distance between two vertices.

.. code-block:: python

Get the minimum distance between two geometry entities.

Computes the shortest straight-line distance between any point on the first entity and any point on the second entity. Supported entity types are "vertex", "curve", "surface", and "volume".

Get the distance along a curve from its start to the closest point on the curve.

If the given xyz is not exactly on the curve, the closest point on the curve is used.

Retrieve the count of edges between surface elements in the current model.

For a volume mesh, only edges on the surface-between surface elements-are counted.

Get the Global Element ID for a specific edge element.

Cubit assigns a Global Element ID to each mesh element when it is placed into a block. This function returns the Global Element ID corresponding to the given local edge ID within its type-specific ID space.

Get edges on triangles at a knife-edge curve that are candidates for swapping.

Given a curve that defines a knife-edge between two triangle-meshed surfaces, this function returns the IDs of mesh edges on the triangles at the curve that are good candidates for edge swapping.

Swapping these edges can improve the local dihedral angles between adjacent triangles, resulting in larger available volumes for successful tet meshing.

This function is commonly used as a postprocessing step after tri or tet meshing to identify edges that may be swapped to improve mesh quality. The Cubit command: Swap Edge <ids> can then be used to perform the actual swapping.

if edge_ids: swap_cmd = "Swap Edge" for edge_id in edge_ids: swap_cmd += f" {edge_id}"

Python-friendly version of get_quality_stats without reference parameters.

Computes quality statistics and returns all results–including failing element IDs–in a single vector.

Get the block ID containing a given global element.

In Cubit, elements receive a Global Element ID when placed into a block. This function returns the ID of the block that contains the specified global element. Returns 0 if the element is not assigned to any block. You can also use the interactive command list element <global_id> to see the block.

Estimate the total element count for a set of volumes given size settings.

Calculates an approximate "element budget" (total number of elements) for the specified volumes, based on the current mesh size factor and element type. For hexahedral meshes, the target edge length (esize) is related to the model volume (Vmodel) and the hex count (Nhex) by:

Solving for Nhex gives:

For tetrahedral meshes, the element count is roughly seven times that of a hex mesh with the same edge length (i.e., Ntet ~ 7 * Nhex)

Retrieve the count of exportable elements in the current model.

Exportable elements are those that have been assigned to a block. If no blocks are defined, all elements (nodes, edges, quad, hex, tet, tri, wedge, sphere, etc.) are considered exportable.

Check whether a global mesh element ID exists in the model.

In Cubit, elements receive a Global Element ID when they are placed into a block. This function returns true if the specified global element ID has been established (i.e., the element was assigned to a block); otherwise it returns false .

Get the specific mesh element type for a global element ID.

CUBIT supports a variety of element types, each with different node counts and accuracy orders. This function returns one of the specific type strings defined in CUBIT; for example, "HEX20", "TETRA4", "TRISHELL7", etc. Supported element types are detailed in the CUBIT documentation or the Exodus manual.

print("Element 1 type:", elem_type) // should print HEX20

Map a Global Element ID back to its local mesh entity ID.

Cubit assigns each element a Global Element ID when it is placed into a block. This function returns the corresponding local mesh entity ID within that element's type-specific ID space (hex, tet, tri, etc.). Together with get_element_type, it lets you determine both the element's type and its local ID.

Retrieve IDs of all current entities of a specified type (geometry and mesh).

Returns the IDs of every entity matching the given type, including both geometry entities (body, volume, surface, curve, vertex) and mesh entities (node, element).

Notes To restrict the results to geometry entities only, use get_current_ids() .

Get the color of a specified entity.

Returns the RGBA color as four doubles in [0, 1] for the given entity.

Get the color index of a specified entity.

Cubit uses predefined color indices to represent common colors.

Title Available color indices

Get the modeler engine type for a specified entity.

Returns the engines associated with this entity. Valid return strings are: acis, facet, virtual.

Get the name of a specified entity.

Returns either a user-defined name (stored in Cubit) or a default name generated at run-time. If no_default is true and the entity has only a default name, an empty string is returned.

Get all names associated with a specified entity.

Retrieves every name attribute set on the entity. By default, returns all names, but if first_name_only is true, only the first name is returned. Setting no_default to true excludes default names.

Get the sense of an entity in a sideset.

This function returns the sense of the specified entity (face, quad, or tri) within the specified sideset. The sense indicates the orientation of the entity relative to the sideset.

Retrieve the total number of errors in the current Cubit session.

Use this to check whether any errors have occurred since Cubit was started (or since the last manual reset).

Errors can be cleared by issuing the Cubit command reset error .

Get the number of elements in a Exodus entity.

.. code-block:: python

Get the description of an Exodus entity.

Returns the description string associated with a block, sideset, or nodeset entity. If no description is assigned or the entity does not exist, an empty string is returned.

Get the name of an Exodus entity.

Retrieves the user-defined name of an Exodus entity of the given type and ID.

Get the Exodus type of an entity.

Returns the Exodus type string associated with the mesh group of a block, sideset, or nodeset. If the entity does not exist, an empty string is returned.

Get the Global Element ID for a mesh entity.

In Cubit, each mesh element type (hex, tet, quad, tri, etc.) has a local ID unique only among its type. When elements are placed into a block, they receive a Global Element ID that is unique across all blocks and element types. Global Element IDs are exported to Exodus files for downstream applications to map back to the original Cubit elements.

Notes In an interactive session you can also use list <type> <local_id> (e.g. list hex 100 ) to display the Global Element ID.

Retrieve the Exodus sizing function file name.

Returns the path or file name of the Exodus II file from which the sizing function was imported. If no file has been imported, returns an empty string.

Retrieve the Exodus-based sizing function variable name.

Returns the name of the field variable currently used as the sizing function. This is the Exodus variable (node- or element-based) driving adaptive meshing.

Get the number of Exodus variables in a nodeset, sideset, or block.

Get the names of Exodus variables in a nodeset, sideset, or block.

Retrieve the Exodus mesh library version.

Returns the version string of the Exodus library used for mesh I/O.

Get the list of node IDs for a mesh element, including interior nodes.

This function returns the IDs of all nodes associated with the specified mesh element, including both corner (boundary) and interior nodes. The ordering follows the Exodus convention; see the Exodus documentation for element-specific node ordering.

Get the direction vector of a force BC.

type of entity_id: int

Get the force magnitude of a force BC.

type of entity_id: int

Get the moment vector of a force BC.

type of entity_id: int

Identify gaps between surfaces in a list of volumes.

This is a Python-friendly version of get_volume_gaps .

For each pair of volumes that have surface gaps, a VolumeGap object is returned. Each VolumeGap contains:

Caching can be used to avoid redundant distance calculations when this function is called together with get_overlapping_surfaces_in_volumes . Both functions require the same underlying distance computations between surfaces in the specified volumes. If caching is enabled, the results of these distance calculations will be saved and reused when the second function is called. If you are calling only this function by itself, caching provides no performance benefit.

for gap in gaps: print(f"Volumes: ({gap.volume1}, {gap.volume2})") for surf_pair, dist, area in zip(gap.surfPairs, gap.gaps, gap.overlapAreas): print(f" Surfaces: ({surf_pair[0]}, {surf_pair[1]}), " f {dist:.6f}, Overlap area: {area}")

Get geometric owners for a set of mesh entities.

Returns the geometric owners of the specified mesh entities (e.g. "surface 3", "curve 5").

Title Supported mesh entity types

Get the number of mesh nodes on a geometric entity.

This function returns the count of mesh nodes associated with the specified geometric entity (surface, curve, etc.).

Get the geometric owner of a mesh element.

This function returns the geometric entity that owns the specified mesh element. For example, it may return "surface 3", "volume 1", etc., indicating where the element lives.

Return the analytic geometry type for a list of surfaces or curves.

This function behaves similar to get_surface_type and get_curve_type but accepts multiple IDs. Note also the difference in return types

Alias for get_exodus_id: get the Global Element ID for a local mesh entity.

This function is equivalent to get_exodus_id and returns the Global Element ID assigned to the specified local mesh entity within its type-specific ID space.

Retrieve the VTK (Visualization Toolkit) version used by Cubit.

Returns the version string of the VTK graphics library integrated into Cubit.

Return direct child body IDs for a specified group, if any.

.. code-block:: python

Return direct child curve IDs for a specified group, if any.

.. code-block:: python

Return direct child edge IDs for a specified group, if any.

.. code-block:: python

Retrieve direct child group IDs for a specified parent group, if any.

.. code-block:: python

Return direct child hexahedral element IDs for a specified group, if any.

Hexahedral elements are generated on volumes using the default map scheme and meshed via: mesh volume all

Return direct child node IDs for a specified group, if any.

.. code-block:: python

Return direct child pyramid element IDs for a specified group, if any.

.. code-block:: python

Return direct child quad IDs for a specified group, if any.

.. code-block:: python

Return direct child sphere element IDs for a specified group, if any.

Sphere elements are generated by inserting nodes or vertices into a block using: Block <id> {node|vertex} <id_range>

Once created, spheres can be located and grouped for querying.

Return direct child surface IDs for a specified group, if any.

.. code-block:: python

Return direct child tetrahedron IDs for a specified group, if any.

.. code-block:: python

Return direct child triangle IDs for a specified group, if any.

.. code-block:: python

Return direct child vertex IDs for a specified group, if any.

.. code-block:: python

Return direct child volume IDs for a specified group, if any.

.. code-block:: python

Return direct child wedge element IDs for a specified group, if any.

.. code-block:: python

Get the heatflux value on a specified area.

type of bc_area_enum: int

Retrieve the count of hexahedral elements in the current model.

.. code-block:: python

Get the Global Element ID for a specific hexahedral element.

This function returns the Global Element ID assigned to the given local hex ID when the element was placed into a block.

Retrieve the IDs of all hexahedral elements forming a hex sheet through two nodes.

A hex sheet is a layer of contiguous hexes. The two node IDs define an edge perpendicular to that layer.

Return the surfaces in the hole adjacent to the specified surface.

The function returns a list of surface IDs that belong to the same hole as the given surface. The input surface_id must already be part of a hole. The result includes surface_id itself.

Compute the hydraulic radius of a specified surface.

Compute the hydraulic radius of a specified volume.

Retrieve the integer ID of an entity by its name.

.. code-block:: python

Convert a list of integers into a compact Cubit-style ID range string.

Collapses consecutive IDs into "start to end" ranges and separates entries with commas. Unlike string_from_id_list() , this variant does not insert any newline characters.

Get the idless signature of a geometric or mesh entity.

This function returns the idless signature of the specified entity. The idless signature is a position-based and ordinal-based reference to the entity, independent of its current ID.

Idless signatures are used to create version-independent journal files . Because entity IDs can change between different Cubit versions or after model operations (e.g., webcuts), using the idless signature ensures that journal files will still refer to the correct entity by position and ordinal rather than ID.

Example format of an idless signature: "volume at 3.42 5.66 6.32 ordinal 2" or "curve at (1 1 0 ordinal 2)"

Common usage scenario:

Notes: For full context, see the Cubit command: journal idless {on | off | reverse} .

Get the idless signatures of a range of geometric or mesh entities.

This function returns the idless signatures of the specified entities as a single string. The idless signature is a position-based and ordinal-based reference to each entity, independent of its current ID.

Idless signatures are used to create version-independent journal files . Since entity IDs can change between different Cubit versions or after model operations (e.g., webcuts), using idless signatures ensures that journal files remain valid by referring to entities by position and ordinal instead of ID.

The return string will contain one idless signature per entity, space-separated. Title Example:

type of entity_type: string

Notes: For full context, see the Cubit command: journal idless {on | off | reverse} .

Retrieve default integer-valued sculpt parameter.

Matches the input variable name substring to known sculpt parameters and returns its default value.

Title Available integer parameters

type of variable: string

Retrieve a Cubit interface by name.

Returns a pointer to the requested CubitBaseInterface instance, or nullptr if no matching interface is registered.

if iface is not None:

cubit.release_interface(iface)

Gets the current label display type for a given entity type.

Queries the label display type currently associated with the specified entity type.

Valid entity_type values:

Returned value corresponds to SVUtil::LabelType : 0=CUBIT_LABEL_NONE, 1=CUBIT_LABEL_ID, 2=CUBIT_LABEL_ELEMENT_ID, 3=CUBIT_LABEL_NAME, 4=CUBIT_LABEL_INTERVAL, 5=CUBIT_LABEL_SIZE, 6=CUBIT_LABEL_MERGE, 7=CUBIT_LABEL_IS_MERGED, 8=CUBIT_LABEL_FIRMNESS, 9=CUBIT_LABEL_SCHEME, 10=CUBIT_LABEL_NAME_ID, 11=CUBIT_LABEL_NAME_ONLY, 12=CUBIT_LABEL_SPHERE_ID

Get the ID of the last created entity of the given type.

This function returns the ID of the most recently created entity of the specified type.

Supported entity types include: "vertex", "curve", "surface", "volume", "body", etc.

Get all free (unattached) entities of a given geometry type.

.. code-block:: python

Get the name of a material or CFD media by ID.

type of material_id: int

Get list of all material names.

return type of : std::vector< std::string,std::allocator< std:: string > >

Get the value of a material property.

type of material_property_enum: int

Get list of all CFD media names.

return type of : std::vector< std::string,std::allocator< std:: string > >

Get the media classification of a material.

type of entity_id: int

Get merge mode ("on", "off", or "auto") for a given entity.

By disabling merge on an entity, adjacent geometry remains separate-preserving material boundaries, distinct mesh regions, and contact interfaces.

Return the current merge tolerance value.

The merge tolerance is an absolute distance value used to determine geometric correspondence when merging entities. Vertices, curves, and surfaces are compared using spatial checks within this tolerance. Entities closer than the merge tolerance are considered equivalent and may be merged, even if their parameterizations differ.

The default merge tolerance in Cubit is 5.0e-4. The lower limit is 1.0e-6. There is no defined upper limit.

Get the list of mergeable curves from a list of volumes or bodies.

Given a list of volume IDs, this function returns a list of lists of potentially mergeable curves. Each inner list contains the curve IDs of one set of curves that can be merged. Each set may contain more than two curves.

Curves are considered mergeable if they are within the current merge tolerance. If not explicitly set, the default merge tolerance is 1e-6.

In Python, the lists will be returned as Python tuples.

for group in mergeable_curves: print(group)

Get the list of mergeable surfaces from a list of volumes or bodies.

Given a list of volume IDs, this function returns a list of lists of potentially mergeable surfaces. Each inner list contains the surface IDs of one set of surfaces that can be merged. Each set may contain more than two surfaces.

Surfaces are considered mergeable if they are within the current merge tolerance. If not explicitly set, the default merge tolerance is 1e-6.

In Python, the lists will be returned as Python tuples.

for group in mergeable_surfaces: print(group)

Get the list of mergeable vertices from a list of volumes or bodies.

Given a list of volume IDs, this function returns a list of lists of potentially mergeable vertices. Each inner list contains the vertex IDs of one set of vertices that can be merged. Each set may contain more than two vertices.

Vertices are considered mergeable if they are within the current merge tolerance. If not explicitly set, the default merge tolerance is 1e-6.

In Python, the lists will be returned as Python tuples.

for group in mergeable_vertices: print(group)

Compute the length of a specified mesh edge.

Returns the geometric length, in model units, of the mesh edge with the given ID.

Get the mesh element type applied to a geometric entity.

Returns the type of elements used to mesh the specified geometry. Possible return values: "hex", "tet", "pyramid", "wedge", "face" (quad), "tri", "edge", or "node". Returns an empty string if the entity has not been meshed.

Retrieve recommended solutions and context cues for a mesh error.

Given a mesh error code, returns a triplet of strings: 1) Solution text describing how to correct the error. 2) Help context cue for detailed guidance. 3) Command-panel cue suggesting the UI panel or command to use.

Get the geometry approximation angle for TriMesh/TetMesh on a given entity.

Returns the maximum deviation angle (in degrees) used to approximate curved CAD surfaces when meshing. A smaller angle yields more finely triangulated surfaces. The value may be explicitly set on a curve, surface, or volume, or computed from adjacent geometry if not user-set.

Retrieve parent group IDs for a specific mesh element.

Returns IDs of all groups containing the given mesh element (excluding pick group).

Retrieve the interval firmness for a specified geometry entity.

Interval firmness determines whether a curve's interval count or size can be modified by other commands. Title Possible return values:

Get the mesh interval count for a specified entity.

Title Retrieves the number of mesh intervals (curve subdivisions) defined on a geometry entity.

Retrieve the meshing scheme applied to a geometric entity.

Returns the name of the scheme currently set on the specified entity. This can be called at any time after a scheme has been assigned (e.g., via cubit.cmd("vol 1 scheme sweep") ) to confirm which scheme is in use.

Retrieve the meshing scheme firmness for a specified surface or volume.

Scheme firmness controls whether a user-assigned scheme can be overridden by automatic selection. Valid firmness values are "Default" (automatic selection allowed), "Soft" (automatic selection preferred), and "Hard" (scheme locked and not changed by automatic selection). Only "surface" and "volume" entities support scheme firmness.

Retrieve the effective target edge length for meshing an entity.

Returns the mesh size (in model units) used when generating 2D or 3D elements.

Retrieve the mesh size setting type for a specified entity.

Unlike get_mesh_interval_firmness() , which returns the firmness of an interval count (number of edges), this function returns the status of a target edge length ("mesh size") setting. The returned value may reflect direct user input, automatic calculation from connected geometry, or lack of any setting.

Title Possible return values are:

Sum mesh volumes or surface areas for CAD entities or mesh elements.

Retrieve the MeshGems library version.

Returns the version string of the MeshGems library used by Cubit.

Get the top classification label for a single volume or surface.

This function performs the full classification workflow, equivalent to calling get_ML_operation_features() followed by get_ML_predictions() . It uses the appropriate model ("volume_no_op" for volumes or "classify_surface" for surfaces) and returns the category with the highest predicted probability.

type of geom_type: string

Retrieve all available classification categories for a geometry type.

This function queries the ML system for every label used to classify volumes or surfaces. It can also accept the specific ML model type, such as "volume_no_op" or "surface_classification".

type of geom_type: string

Retrieve the list of supported classification ML model names.

Queries the ML subsystem for all available classification models used for labeling or categorization.

return type of : std::vector< std::string,std::allocator< std:: string > >

Classify multiple volumes or surfaces in a single batch operation.

Perform classification on a collection of entities at once to improve efficiency over repeated individual calls.

type of geom_type: string

Compute the weighted distance between two feature vectors.

Applies operation-specific importance weights derived from an ensemble of decision trees to each feature, then calculates the Euclidean distance between the weighted vectors. The distance indicates the geometric or topological similarity between the two entities, where a distance of zero signifies an exact match.

type of op_name: string

Retrieve feature importance scores for a given ML operation.

Queries the trained model to obtain the relative importance of each feature used in the specified operation.

type of op_name: string

for i in range(len(feature_names)): print(f"{feature_names[i]}\t{importances[i]}")

Compute ML feature vectors for operations permitting multiple entities.

This is a batch variant of get_ML_operation_features() that accepts lists of IDs per operation, enabling feature extraction across multiple entities at once.

type of ml_op_names: std::vector< std::string,std::allocator< std::string > >

Capture entities for survival tracking before a CAD operation.

This function sets a baseline for CAD operation models that measure mesh quality before and after the operation. It is used with get_ML_surviving_entities() to identify entities that replace or correspond to the originals after the operation.

type of op_name: string

Retrieve the unique numeric ID for a given ML model or operation name.

Looks up the internal mapping from a model or operation name to its assigned ID.

type of model_name: string

Retrieve the name of an ML model based on its ID.

This function returns the name of the ML model corresponding to the provided model ID. The model name is used to identify a specific machine learning model that can be used for various operations such as classification or prediction.

type of model_ID: int

Generate the command, display label, and preview text for an ML operation.

Constructs three strings for the specified operation and entities:

type of op_name: string

Retrieve the list of feature names for a specified ML operation.

This function returns a vector of strings naming each feature in the operation's input vector.

type of ml_op_name: string

for i in range(len(feature_names)): print(f"{i}\t{feature_names[i]}\t{feature_types[i]}\t{features[0][i]}")

Retrieve the expected feature-vector length for a given ML operation.

For the specified operation (as described by get_ML_operation_features() ), this function returns the number of features that the model expects as input.

type of ml_op_name: string

Get the data-type descriptor for each feature of a specified ML operation.

This function returns a list of strings indicating the type of data expected for each feature in the operation's input vector. The types can be:

type of ml_op_name: string

Compute ML feature vectors for a list of Cubit operations.

This function computes machine learning feature vectors for a list of Cubit operations based on specified parameters, including entity IDs and target mesh size. It returns the computed feature vectors for each operation.

Supported operations: ### Outdated ###

13 | R | 3 | remove_cone | surface | none |

15 | R | 3 | remove_blend | surface | none | 16 | R | 3 | remove_cavity | surface | none |

19 | C | 1 | classify_surface | surface | none |

type of ml_op_names: std::vector< std::string,std::allocator< std::string > >

Retrieve the expected label vector length for a given ML operation.

Returns the number of entries in the output label vector for the specified operation or model.

type of ml_op_name: string

Compute ML predictions for a list of operations on single-entity pairs.

This function loads the ML training data (if not already loaded), computes features for each specified operation and its associated entities, and then runs predictions using a scikit-learn ensemble of decision trees.

type of ml_op_names: std::vector< std::string,std::allocator< std::string > >

Retrieve the list of supported regression ML model names.

Queries the ML subsystem for all available regression models used for prediction or analysis.

return type of : std::vector< std::string,std::allocator< std:: string > >

Identify which entities survive after a CAD operation.

Uses the snapshot from get_ML_initialize_surviving_entities() to find entities that remain or correspond to the initial set after the operation is completed.

type of op_name: string

for id in result[1]: print("Surviving entity ID:", id)

Get the moment magnitude of a force BC.

type of entity_id: int

Finds the N largest node-to-element distances between two meshes.

For each node on the entities in ids1 , computes its distance to nearby elements on ids2 .

for i in range(0, len(distances), 3): print("Distance:", distances[i], "Node ID:", int(distances[i+1]), "Element ID:", int(distances[i+2]))

Find faces containing narrow regions within specified volumes.

Collects all unique faces of volumes in target_ids. For each face:

This function differs from get_closed_narrow_surfaces by applying to all faces (not just closed two-loop faces), and from get_surfs_with_narrow_regions by using split-point and loop-to-loop proximity tests rather than purely edge-pair orientation checks.

Find surfaces with narrow regions in specified volumes.

For each face of volumes in target_volume_ids, checks if any two non-adjacent edges form a narrow region (distance <= mesh_size and orientation difference > 15deg). Returns all face IDs that meet this criterion.

for sid in narrow_surfaces: print("Narrow surface ID:", sid)

Identify nearby entities of type curve, surface, or volume for a given list of the same type.

Returns a list of entities of type gtype that are within the specified distance of the entities in ent_ids . If compare_ents is empty, all entities of type gtype in the model will be used for comparison.

If distance is set to -1, a default tolerance will be computed internally.

for id in nearby_ents: print(id)

Identify nearby volumes in the model for a list of target volumes.

For each volume in volume_id , returns a list of volumes from compare_volumes (or all volumes in the model if compare_volumes is empty) that are within the specified distance.

The distances vector specifies the maximum distance to use for each corresponding volume in volume_id . If a value is set to -1, a default tolerance will be computed for that volume.

The result is a vector of vectors: one list of nearby volumes per input volume in volume_id .

for i, near_list in enumerate(nearby_volumes): print(f"Volume {volume_ids[i]} nearby volumes:", " ".join(str(v) for v in near_list))

Get the next available block ID.

.. code-block:: python

Get the next available boundary layer ID.

This ID can be used to define a new boundary layer entity. return type of : int

Get the next command from the history buffer.

Advances an internal history pointer and returns the next command.

Return the next available group ID from Cubit.

.. code-block:: python

Get the next available nodeset ID.

.. code-block:: python

Get the next available sideset ID.

.. code-block:: python

Get the coordinates of a mesh node.

This function returns the (x, y, z) coordinates of the specified node ID. In C++, the coordinates are returned as a std::array<double,3>. In Python, the coordinates are returned as a tuple of three floats.

Query whether node constraint is enabled (move mid-nodes to geometry).

Node constraints control how higher-order mid-nodes snap to curved geometry:

Query the current quality metric for smart node constraint.

When node constraint is in "smart" mode for tets or tris, this returns either "distortion" or "normalized inradius", indicating which metric controls snapping.

Query the current quality threshold for smart node constraint.

When node constraint is in "smart" mode, mid-nodes are only projected if element quality remains above this threshold.

Query the numeric value of the node constraint setting.

Returns 0 for off, 1 for on, or 2 for smart. This corresponds to the "set Node Constraint" options.

Retrieve the count of nodes in the current model.

.. code-block:: python

Get the IDs of all edge elements adjacent to a node.

Edge elements are created on meshed curves and throughout meshed surfaces, but not within the interior volume mesh. Nodes not on any meshed curve or surface will have no adjacent edges.

Check whether a node exists in the model.

This function returns true if the specified node ID exists in the current model; otherwise it returns false .

Get the IDs of all quadrilateral elements (faces) adjacent to a node.

In Cubit, "faces" are represented as quad elements on surfaces. Nodes in the interior of volumes will have no adjacent faces returned.

Get the global node ID assigned in the Exodus file for a mesh node.

In Cubit, each node has a local ID unique within the session. Upon exporting the mesh to an Exodus file, nodes are renumbered into a global ID space from 1 to N. This function returns the Exodus global node ID for the given local node ID, or 0 if the mesh has not been exported.

Query whether a mesh node is fixed (constrained against smoothing).

A fixed node will not be moved by mesh smoothing or optimization operations.

Get the IDs of all triangular elements adjacent to a node.

In Cubit, triangular "faces" are represented as tris on surfaces. Nodes in the interior of volumes will have no adjacent tris returned.

Get the current number of nodesets in the model.

In Cubit, a nodeset groups mesh nodes for applying boundary conditions or loads. Nodesets can be defined by assigning vertices, curves, surfaces, volumes, or individual nodes to a given ID.

Get the list of curve IDs associated with a nodeset.

This function returns the IDs of all curves that are associated with the specified nodeset.

for curve_id in curve_ids: print(f" Curve ID: {curve_id}")

Get a list of all active nodeset IDs.

Returns a vector of all currently active nodeset IDs in the model.

for nodeset_id in nodeset_ids: print(" Nodeset ID:", nodeset_id)

return type of : std::vector< int,std:: allocator< int > >

Get list of nodeset IDs associated with a boundary condition.

Returns nodesets to which the BC is applied.

type of bc_type_enum: int

Get the number of nodes in a nodeset.

type of nodeset_id: int

Get the list of node IDs explicitly assigned to a nodeset.

This function returns the IDs of nodes that were specifically assigned to the nodeset.

If the nodeset was created on geometry (e.g. a surface or volume), this function will not return the nodes on that geometry unless they were explicitly assigned. To include nodes on geometry, use 'get_nodeset_nodes_inclusive' instead.

for node_id in node_ids: print(f" Node ID: {node_id}")

Get the list of node IDs associated with a nodeset (inclusive).

This function returns the IDs of all nodes associated with the specified nodeset. It includes:

Use this function when the nodeset was created using geometry and you want all associated nodes . For only explicitly assigned nodes, see 'get_nodeset_nodes'.

for node_id in node_ids: print(f" Node ID: {node_id}")

Get the list of surface IDs associated with a nodeset.

This function returns the IDs of all surfaces that are associated with the specified nodeset.

for surf_id in surface_ids: print(f" Surface ID: {surf_id}")

Get the list of vertex IDs associated with a nodeset.

This function returns the IDs of all vertices that are associated with the specified nodeset.

for vertex_id in vertex_ids: print(f" Vertex ID: {vertex_id}")

Get the list of volume IDs associated with a nodeset.

This function returns the IDs of all volumes that are associated with the specified nodeset.

for vol_id in volume_ids: print(f" Volume ID: {vol_id}")

Get the number of shells in a volume.

A "shell" is a closed set of faces bounding a region within the volume. For a simple solid with no internal cavities, this returns 1. If the volume contains voids or nested regions, each closed boundary counts as a separate shell.

Retrieve IDs of overconstrained tetrahedra within specified volumes.

Overconstrained tetrahedra are those that have two triangular faces on the same surface and all four corner nodes lying on surfaces, curves, or vertices. Such tets cannot be smoothed and are typically removed to improve mesh quality.

type of volumes: std::vector< int,std::allocator< int > >

ids_str = cubit.string_from_id_list(over_tets)

Get the current maximum angle tolerance used for calculating surface overlaps.

Returns the maximum angle (in degrees) allowed between normals of adjacent surfaces when determining overlaps. This setting controls how much angular deviation is tolerated before surfaces are considered non-overlapping.

Get the current maximum gap tolerance used for calculating surface overlaps.

Returns the maximum allowable gap between adjacent surfaces when determining overlaps. This setting controls how large a gap is tolerated before surfaces are considered non-overlapping.

Get the current minimum gap tolerance used for calculating surface overlaps.

Returns the minimum allowable gap between adjacent surfaces when determining overlaps. This setting can be used to ignore negligible gaps that should be treated as overlapping.

Identify surfaces in the model that overlap a single target surface.

Returns a list of surfaces that overlap the specified surface_id . If compare_volumes is empty, all volumes in the model will be used for comparison.

Caching can be used to avoid redundant distance calculations when this function is called together with get_overlapping_surfaces_in_volumes . Both functions require the same underlying distance computations between surfaces in the specified volumes. If caching is enabled, the results of these distance calculations will be saved and reused when the second function is called. If you are calling only this function by itself, caching provides no performance benefit.

for s_id in overlapping_surfaces: print(s_id)

Identify overlapping surfaces between different volumes in a set of bodies.

Overlaps are only reported between surfaces from different volumes . The result is a vector of vectors. The first surface ID in each vector overlaps with all subsequent surfaces in that vector.

for surfaces in overlaps: print("Surfaces:", tuple(int(sid) for sid in surfaces))

type of body_ids: std::vector< int,std::allocator< int > >

Identify overlapping volumes in a list of volumes.

For each pair of overlapping volumes, two volume IDs are returned in the output list. The first volume ID overlaps with the second, the third overlaps with the fourth, and so on. The list should always contain an even number of volume IDs (modulus 2 = 0).

for i in range(0, len(overlapping_volumes), 2): print(f"Volumes: ({overlapping_volumes[i]}, {overlapping_volumes[i+1]})")

Identify volumes in the model that overlap a single target volume.

Returns a list of volumes that overlap the specified volume_id . If compare_volumes is empty, all volumes in the model will be used for comparison.

for v_id in overlapping_volumes: print(v_id)

Get the owning body for a specified entity.

Returns the ID of the body that contains (owns) the given entity.

Get the owning volume for a specified entity.

Returns the ID of the volume that contains (owns) the given entity.

Get the owning volume for an entity by its name.

.. code-block:: python

Get the instance number of the parent of an assembly node.

type of assembly_id: int

Get the path of an assembly node's parent.

type of assembly_id: int

Retrieve the list of entity types currently allowed for picking.

Returns all types in the active pick filter. Only entities of these types can be selected in the graphics window.

for t in filters: print("Pick filter:", t)

Get the current pick mode for entity selection.

Returns the pick type that the graphics system is using for selection. This corresponds to the GUI icons and can be one of: "vertex", "curve", "surface", "volume", "node", "edge", "face", etc.

for id in ids: print(f"Selected {mode}: {id}")

Get the function expression associated with a pressure BC.

type of entity_id: int

Get the magnitude value of a pressure BC.

type of entity_id: int

Get the previous command from the history buffer.

Moves the internal history pointer backwards and returns that command.

Return the surfaces in the protrusion connected to the specified surface.

The function returns a list of surface IDs that belong to the same protrusion feature as the given surface. The input surface_id must be part of a protrusion. The result includes surface_id itself.

type of surface_id: int

Retrieve the count of pyramid elements in the current model.

.. code-block:: python

Get the Global Element ID for a specific pyramid element.

This function returns the Global Element ID assigned to the given local pyramid ID when the element is placed into a block.

Retrieve the Python interpreter version used by Cubit.

Returns the version string of the embedded Python interpreter in Cubit.

Retrieve the count of quadrilateral elements in the current model.

For a hexahedral volume mesh, this returns the number of quad faces on the surface.

Get the Global Element ID for a specific quadrilateral element.

Cubit assigns a Global Element ID to each element when it is placed into a block. This function returns the Global Element ID corresponding to the given local quad ID within its type-specific ID space.

Python-friendly version of get_quality_stats operating on geometry entities.

Computes quality statistics over all mesh elements attached to the specified geometry entities (curves, surfaces, or volumes) up to a given adjacency level, using the specified metric and threshold criteria. Results are packed into a single std::vector<double> as follows:

Unlike get_elem_quality_stats() , which operates on a flat list of mesh-element IDs, this function first gathers all mesh elements of mesh_type attached to the given geometry_type entities (expanding connectivity up to expand_levels) and then calls get_elem_quality_stats() internally.

Retrieve a specific quality metric value for a single mesh element.

Returns the requested quality metric for the given mesh entity.

Retrieve quality metric values for multiple mesh elements.

Returns a vector of metric values for the specified list of element IDs. This differs from get_quality_value() , which only returns a single element's metric.

for eid, val in zip(mesh_ids, skew_vals): print(f"Element {eid} skew: {val}")

Computes default core dimensions for a bolt volume in reduce bolt core operation.

Used with reduce volume <id> bolt core to estimate the default values for c1, c2, and c3, which define the extent of the core geometry surrounding the bolt.

Get the relatives (parents or children) of a specified entity.

Use this to fetch either ancestor (parent) or descendant (child) entities of one type for a given source entity. For example, to list all curves bounding surface 12, call with source_geometry_type="surface", source_id=12, target_geom_type="curve".

Get the current graphics rendering mode.

Returns an integer code for the active rendering style:

Retrieve the explicitly requested interval firmness for a specified entity.

Unlike get_mesh_interval_firmness() , which returns the effective firmness after considering influences from connected topology, this function returns only the firmness setting directly assigned by the user on the entity itself (no inheritance or propagation).

Title Possible return values are:

Retrieve the mesh interval count explicitly set on a geometry entity.

Returns the number of subdivisions assigned directly to the specified geometry entity.

Retrieve the mesh size explicitly set on a geometry entity.

Returns the target edge length that was directly assigned to the entity, not inherited from parent entities. If no explicit size was set, returns -1.

Retrieve the mesh size setting type explicitly requested on a specified entity.

Unlike get_mesh_size_type() , which may return "CALCULATED" if the size was inherited or computed, this function returns only the status of a mesh size setting directly applied by the user on this entity.

Title Possible return values are:

Retrieve the Cubit revision date.

Returns the date of the last code revision applied to the Cubit engine.

Get the current rubberband selection shape.

Returns an integer code for the active selection shape in the graphics window:

Get the selected entity ID by index.

Use together with get_selected_ids() and get_selected_type() to inspect selections.

for i in range(len(ids)): id = cubit.get_selected_id(i)

Retrieve all currently selected entity IDs in pick order.

Returns a vector of IDs for entities selected via the graphics interface or programmatic pick commands. The order reflects the sequence in which entities were picked.

for i, id in enumerate(ids): t = cubit.get_selected_type(i)

Get the selected entity type by index.

Use together with get_selected_ids() and get_selected_id() to inspect selections.

if ids: id = cubit.get_selected_id(0)

Retrieve the SGM (Solid Geometry Manager) version.

Returns the version string of the SGM engine integrated with Cubit.

Identify vertices at sharp curve angles in a set of volumes.

This function computes the interior angles at curve intersections (sharp corners) on the surfaces of each of the specified volumes. Vertices are identified where the interior angle exceeds the specified upper_bound or falls below the lower_bound threshold.

for vid, angle in zip(vertex_ids, angles): print(f"Vertex {int(vid)} angle {angle:.1f}")

Get the total area of a sideset.

If the sideset contains triangle or quadrilateral elements, this function returns the sum of the areas of those elements. Otherwise, it finds the geometric faces associated with the sideset and returns the sum of the areas of the corresponding geometric surfaces.

Identify sideset-based contact interfaces and return compact integer interaction records.

This scans sidesets associated with the specified volumes or blocks, groups sidesets that represent a common contact interface (1-to-1, one-to-many, many-to-one, or many-to-many), and returns each interface as a compact integer record. Records may also represent "intent" where only one side has a named sideset but the opposite entity is known.

Each returned interaction record is encoded as:

[ status, A_id, B_id, bolt_id, n_A_to_B, A_to_B_ss..., n_B_to_A, B_to_A_ss... ]

Related helpers once you have sideset IDs:

.. code-block:: python

for rec in pairs: status, a_id, b_id, bolt_id = rec[0], rec[1], rec[2], rec[3]

for sid in ab_ids: name = cubit.get_exodus_entity_name ("sideset", sid)

for sid in ba_ids: name = cubit.get_exodus_entity_name ("sideset", sid)

Get the current number of sidesets in the model.

In Cubit, a sideset groups element faces (or edges) for applying boundary conditions. Sidesets can be defined by assigning surfaces, curves, faces, or mesh entities to a given ID.

Get the list of curve IDs associated with a sideset.

This function returns the IDs of all curves that are associated with the specified sideset.

for curve_id in curve_ids: print(f" Curve ID: {curve_id}")

Get the list of edge IDs contained in a sideset.

A sideset can contain edge elements. This function returns the IDs of those edge elements, if they exist. An empty list will be returned if there are no edges in the sideset.

for edge_id in edge_ids: print(f" Edge ID: {edge_id}")

Get the element type of a sideset.

type of sideset_id: int

Get a list of all active sideset IDs.

Returns a vector of all currently active sideset IDs in the model.

for sideset_id in sideset_ids: print(" Sideset ID:", sideset_id)

Get list of sideset IDs associated with a boundary condition.

Returns sidesets to which the BC is applied.

type of bc_type_enum: int

Get the list of quadrilateral (quad) element IDs contained in a sideset.

A sideset can contain quadrilateral elements (faces). This function returns the IDs of those quad elements, if they exist. An empty list will be returned if there are no quads in the sideset.

for quad_id in quad_ids: print(f" Quad ID: {quad_id}")

Get the list of surface IDs contained in a sideset.

A sideset can contain surfaces. This function returns the IDs of those surfaces, if they exist. An empty list will be returned if there are no surfaces in the sideset.

for surf_id in surface_ids: print(f" Surface ID: {surf_id}")

Get the list of triangle (tri) element IDs contained in a sideset.

A sideset can contain triangle (tri) elements. This function returns the IDs of those tri elements, if they exist. An empty list will be returned if there are no tris in the sideset.

for tri_id in tri_ids: print(f" Tri ID: {tri_id}")

Find curves with lengths similar to a given curve.

This function compares the length of the curve in curve_ids against all other curves in the model. Curves whose lengths differ by no more than tol (interpreted as a fraction if use_percent_tol is true, or as an absolute length if false) are considered similar. If on_similar_vols is true, only curves on volumes with the same geometry as the volume owning curve_ids are compared.

Find surfaces with similar area and curve count to given surfaces.

This function compares each surface in surface_ids against all other surfaces in the model. Surfaces whose areas differ by no more than tol (interpreted as a fraction if use_percent_tol is true, or as an absolute area if false) and that have the same number of bounding curves are considered similar. If on_similar_vols is true, only surfaces on volumes with the same geometry as the volumes owning surface_ids are compared.

Find volumes with similar size and face count to given volumes.

This function compares each volume in volume_ids against all other volumes in the model. Volumes whose volumes differ by no more than tol (interpreted as a fraction if use_percent_tol is true, or as an absolute volume if false) and that have the same number of faces are considered similar.

Retrieve the meshing sizing function type for a surface or volume.

Returns the sizing function type assigned to the specified entity. Possible return values: "constant", "curvature", "interval", "inverse", "linear", "super", "test", "exodus", or "none".

Find surfaces that are either small in area or contain narrow regions.

For each face of volumes in target_ids, measures its area and checks if area <= small_area. Also checks for narrow regions by evaluating pairs of non-adjacent edges: if their distance <= small_curve_size and orientation difference > 15deg, the face is narrow. Returns all face IDs meeting either criterion.

for sid in results: print("Surface ID:", sid)

Find curves with edge length below a threshold within given volumes.

For each curve on faces of volumes in target_volume_ids, measures its edge length. Curves with length <= mesh_size are returned.

for cid in small_curves: print("Small curve ID:", cid)

Find blend surfaces with radius of curvature <= max_radius.

Iterates over all faces of volumes in target_volume_ids and returns those blend surfaces whose radius of curvature is <= max_radius. If max_radius = 0, all blend surfaces are returned.

Find surfaces with area below a given threshold.

Gathers all unique faces from the specified volumes, measures each face's area, and returns those with area <= area_threshold.

for sid in small_surfaces: print("Small surface ID:", sid)

Python-callable version: identify small hydraulic-radius surfaces.

Computes hydraulic radius = 4*(area/perimeter) for each face in target_volume_ids. Returns IDs of faces with hydraulic radius <= mesh_size.

for sid in small_surfaces: print("Small surface ID:", sid)

Find volumes whose size is below a threshold based on mesh size.

Volumes with actual volume < 10 * mesh_size^3 are considered "small".

Return IDs of the smallest curves in the specified volumes.

Measures the length of each curve on faces of volumes in target_volume_ids and returns the number_to_return curves with the shortest lengths.

for cid in smallest_curves: print("Curve ID:", cid)

Retrieve the smoothing scheme for a specified geometry entity.

This returns the name of the smoothing scheme applied to the given entity ("curve", "surface", or "volume") and ID. If none is set, returns an empty string.

Provide remedy for bad geometry via ACIS healing (deprecated).

Bad geometry often results from imperfect CAD translations. This function invokes ACIS's built-in healing operation.

type of geom_type: string

Provide possible blend removal solutions for a given surface (and its blend chain if applicable).

Given a surface ID, this function returns possible solutions for removing or adjusting blends on that surface. If the surface is part of a blend chain, the solutions will include operations for the entire blend chain as well.

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

Suggests operations for a volume classified as a bolt using known subcomponent IDs.

This function provides modification options for a bolt volume using known insert and threaded subcomponent volumes. It is more efficient than get_solutions_for_classified_volume when those IDs are already available.

Set insert_id or threaded_vol_id to 0 if the corresponding volume is not present or not known. To classify bolt volumes in the model, use get_ML_classification() .

for i in range(3): print("Option:", solutions[0][i])

Suggests repair or modification options for a set of concentric fastener pilot holes.

Given a bearing hole surface ID and a list of concentric threaded hole surface IDs, this function identifies potential repair or optimization operations.

for i in range(3): print("Option:", solutions[0][i])

Provide possible cavity removal or adjustment solutions for a given surface (and its cavity if applicable).

Given a surface ID, this function returns possible solutions for removing or adjusting cavity geometry on that surface. If the surface is part of a cavity, the solutions will include operations for the entire cavity as well.

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

Provide possible chamfer removal solutions for a given surface (and its chamfer chain if applicable).

Given a surface ID, this function returns possible solutions for removing or adjusting chamfers on that surface. If the surface is part of a chamfer chain, the solutions will include operations for the entire chamfer chain as well.

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

Suggests remedies or modifications for a classified surface.

.. code-block:: python

for disp, cmd, prev, shrt in zip(solutions[0], solutions[1], solutions[2], solutions[3]): print("Option:", disp)

Suggests geometry fixes or feature operations for a volume based on its classification.

Given a classification type and a volume ID, this function generates recommended modifications.

To obtain classifications from Cubit's ML system, use get_ML_classification() .

for i in range(3): print("Option:", solutions[0][i])

Retrieve recommended remedies for a close-loop surface to resolve narrow regions.

.. code-block:: python

for disp, cmd, prev, shrt in zip(solutions[0], solutions[1], solutions[2], solutions[3]): print("Option:", disp)

Suggests remedies for a surface classified as a cone.

Returns recommended operations for a conical surface, including human-readable descriptions, Cubit command strings to apply them, preview commands for visualization, and shorthand strings for serialization or machine learning workflows.

for disp, cmd, prev, shrt in zip(solutions[0], solutions[1], solutions[2], solutions[3]): print("Option:", disp)

Propose two operations for a connected set of surfaces.

Given a list of surface IDs that are mutually connected, this function returns exactly two candidate operations: (1) Removal of the connected region. (2) Composite of the surfaces into a single face.

Each solution is represented as a 4-element string list: [0] Display string for the operation. [1] Cubit command to execute it. [2] Cubit preview command. [3] ML shorthand string (includes operation + IDs).

The ML shorthand encodes the operation and surface IDs; its feature type is derived from the specified common_surface_type .

for disp, cmd, prev, shrt in zip(*solutions): print("Option:", disp)

type of surf_ids: std::vector< int,std::allocator< int > >

type of common_surface_type: string

return type of : std::vector< std::vector< std::string,std::allocator< std::string > >,std::allocator< std::vector< std::string,std::allocator< std:: string > > > >

Provide possible decomposition solutions for volumes based on exterior angle criteria.

Given a list of volumes and an exterior angle threshold, this function suggests possible decompositions. Optionally, imprinting and merging can be performed to support the decomposition process.

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

Suggests remedies for imprint/merge when two overlapping surfaces are on different volumes.

Given two overlapping surface IDs from different volumes, this function provides suggested operations to resolve the overlap.

To detect overlapping surfaces beforehand, use get_overlapping_surfaces_at_surface (for a single surface) or get_overlapping_surfaces_in_volumes (for sets of volumes).

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

Suggests remedies when a vertex lies nearly on a curve from a different volume.

Given a vertex and a nearby curve from different volumes, this function identifies operations to resolve the near-coincidence without introducing geometry issues.

To detect such vertex-curve pairs, use get_close_vertex_curve_pairs.

for i in range(3): print("Option:", solutions[0][i])

Suggests remedies when a vertex lies nearly on a surface from a different volume.

Given a vertex and a nearby surface from different volumes, this function identifies potential fixes such as tweaks or volume adjustments.

To identify near-coincident vertex-surface pairs, use get_close_vertex_surface_pairs.

for i in range(3): print("Option:", solutions[0][i])

Provide remedies for two nearly coincident vertices on different volumes to resolve gaps or misalignments.

Vertices must belong to different volumes.

for disp, cmd, prev, shrt in zip(solutions[0][:3], solutions[1][:3], solutions[2][:3], solutions[3][:3]): print("Option:", disp)

Suggests remedies for two overlapping surfaces on different volumes.

Given two overlapping surface IDs from different volumes that share the same spatial region, this function provides imprint and merge options for resolving the overlap.

To identify overlapping surfaces beforehand, use get_overlapping_surfaces_at_surface or get_overlapping_surfaces_in_volumes.

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

Provide remedies for two overlapping volumes based on gap and angular tolerances.

If two volume IDs represent overlapping solids and the overlap exceeds a given gap or angle tolerance, this function suggests operations to resolve the interference.

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

Provide possible protrusion removal or adjustment solutions for a given surface (and its protrusion if applicable).

Given a surface ID, this function returns possible solutions for removing or adjusting protrusion geometry on that surface. If the surface is part of a protrusion, the solutions will include operations for the entire protrusion group as well.

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

type of surface_id: int

Retrieve recommended remedies for a sharp angle at a vertex.

.. code-block:: python

for disp, cmd, prev, shrt in zip(solutions[0], solutions[1], solutions[2], solutions[3]): print("Option:", disp)

Propose surface-tweak, imprint, and merge operations to bridge two sheet-volume sets.

Unlike get_solutions_for_sheet_volumes (single group), this function connects two distinct sheet-body sets by first merging within each set (if needed) and then suggesting tweaks, imprint, and merge steps between them. Sheets remain separate bodies to retain unique material assignments.

Propose surface-extension and imprint/merge operations to connect sheet bodies.

Analyze sheet-body volumes and suggest surface-tweak commands that extend surfaces to fill gaps between them, then propose imprint and merge operations. The sheets remain separate bodies to accommodate unique material assignments.

for disp, cmd, prev, shrt in zip(*solutions): print("Option:", disp)

Recommend remedial operations on a curve already flagged as small.

Operates on a curve marked small by small_curve_size and mesh_size, and suggests surface removals, surface-replacement tweaks, curve collapses to vertices, or topology rebuild operations.

for disp, cmd, prev, shrt in zip(*solutions)[:3]: print("Option:", disp)

Recommend remedial operations on a surface already flagged as small.

Operates on a surface marked small by small_curve_size and mesh_size, and suggests composite merges, topology rebuilds, surface removals, or surface-replacement tweaks.

for disp, cmd, prev, shrt in zip(*solutions)[:3]: print("Option:", disp)

Recommend operations to eliminate narrow regions on a surface identified as narrow.

Analyzes a surface with narrow regions and suggests operations.

type of surface_id: int

Generate candidate operations to reduce a thin volume into a sheet body.

Suggest copying or midsurfacing operations (with optional weights/types) to reduce a volume to a shell.

for disp, cmd, prev, shrt in zip(*solutions[:3]): print("Option:", disp)

Recommend remediation operations for volumes with features below a size threshold.

Analyze a given volume to find curves smaller than a user-specified threshold and suggest operations to eliminate those features before meshing.

for disp, cmd, prev, shrt in zip(*solutions): print("Option:", disp)

Retrieve the list of sweep source surfaces for a specified volume.

When a volume uses the Sweep scheme, source surfaces are the starting faces from which the hexahedral mesh is extruded. This function returns all surface IDs designated as sources. If no explicit source was set, returns an empty list.

Retrieve the count of sphere elements in the current model.

Sphere elements are nodes whose element type has been set to "sphere".

Get the Global Element ID for a specific node (SPHERE element).

Cubit assigns a Global Element ID to each mesh entity when it is placed into a block. Nodes are represented as SPHERE elements in the mesh. This function returns the Global Element ID corresponding to the given local sphere (node) ID within its type-specific ID space.

Retrieve default string-valued sculpt parameter.

Matches the input variable name substring to known sculpt parameters and returns its default.

Title Available string parameters

type of variable: string

Get the lower-dimensional entities of a higher-dimensional mesh element.

This function returns the IDs of all sub-entities of the specified dimension for a given mesh element. For example, to get all faces (dimension 2) of a hexahedron, or all edges (dimension 1) of a triangle.

Notes Faces and edges are only created on surfaces and curves, respectively. Interior faces or edges within volumes are not generated. In the example below, only three faces appear because they lie on the exterior surfaces of volume 1.

Get a list of vertex IDs and their corner-type codes for a surface submap.

Vertex types classify each corner based on how many mesh elements meet there:

type of surface_id: int

Get the area of a specified surface.

.. code-block:: python

Return collections of surfaces that form cavities in the specified volumes.

A cavity is a collection of contiguous surfaces, bounded by curves where the exterior angle is greater than or equal to (180 - angle_tolerance). Cavities are filtered by their total surface area.

If combine_cavities is true, small adjacent cavities are merged after initial cavity detection.

If area_threshold < 0.0, all cavities are returned. If angle_tolerance < 0.0, a default of 0.01 degrees is used.

for surfaces, area in cavity_collections: print("Cavity surfaces:", tuple(surfaces), "Area:", area)

Get the approximate centroid of a specified surface based on graphics faceting.

The centroid is computed from the faceted representation of the surface, so it is an approximation.

Identify collections of surfaces that comprise cones in specified volumes.

Cones may be represented by a single surface or by two adjacent surfaces symmetrically split. Results can be filtered by a maximum cone radius.

for surfaces, radius in cone_collections: print("Radius:", radius, "Surfaces:", [int(sid) for sid in surfaces])

type of volume_list: std::vector< int,std::allocator< int > >

Get the current number of surfaces in the model.

.. code-block:: python

Retrieve the count of elements on a specified surface.

Returns the total number of quadrilateral and triangular elements present on the given surface, regardless of block assignments.

Return collections of surfaces that form holes in the specified volumes.

A hole is a collection of contiguous surfaces that form a cylindrical or approximately cylindrical feature. Holes are filtered by their computed radius.

If radius_threshold is provided, only holes with radius less than or equal to this value are returned.

for surfaces, radius in hole_collections: print("Hole surfaces:", tuple(surfaces), "Radius:", radius)

Get the curve IDs for each loop on a surface.

This function returns the boundary curves for each closed loop on the specified surface. Each loop is represented as an ordered list of curve (RefEdge) IDs that form a closed boundary. Surfaces with holes or internal boundaries will have multiple loops.

If the surface ID is invalid, an error is printed and an empty list is returned.

for i, loop in enumerate(loops): print(" loop %d curves: %s" % (i, " ".join(str(c) for c in loop)))

Get the ordered list of node IDs on the loops of a surface.

This function returns the ordered list of node IDs for each loop on the specified surface. The first loop in the list is the external loop. Each loop is returned as a separate list of node IDs.

Loops are ordered as follows:

for i, loop in enumerate(loop_nodes): print(f" Loop {i+1} has {len(loop)} node(s):", " ".join(str(node_id) for node_id in loop))

Get the list of node IDs owned by a surface.

This function returns the IDs of nodes owned by the specified surface. Nodes on the bounding curves and vertices of the surface are excluded.

for node_id in surface_nodes: print(f" Node ID: {node_id}")

Get the unit normal vector at the center of a specified surface.

.. code-block:: python

Get the unit normal vector at a specified point on a surface.

.. code-block:: python

Get the number of loops on a surface.

This function returns the number of loops on the specified surface. A loop is a closed boundary on the surface. Surfaces with holes or internal boundaries will have multiple loops.

Get the principal curvatures of a surface at its midpoint.

Principal curvatures quantify how a surface bends in two orthogonal directions at a point. At the surface midpoint, this function returns two scalar values: k1 and k2. For a planar surface, both values are 0. For a sphere of radius R, both values equal 1/R.

Return collections of surfaces that form protrusions in the specified volumes.

A protrusion is a collection of contiguous surfaces, bounded by curves where the exterior angle is greater than or equal to (180 + angle_tolerance). Protrusions are filtered by their total surface area.

If combine_protrusions is true, small adjacent protrusions are merged after initial detection.

If area_threshold < 0.0, all protrusions are returned. If angle_tolerance < 0.0, a default of 0.01 degrees is used.

for surfaces, area in protrusion_collections: print("Protrusion surfaces:", tuple(surfaces), "Area:", area)

type of volume_list: std::vector< int,std::allocator< int > >

Get the list of quadrilateral (quad) element IDs on a surface.

This function returns the IDs of all quadrilateral (quad) elements on the specified surface.

for quad_id in quad_ids: print(f" Quad ID: {quad_id}")

Get the orientation ("sense") of a specified surface.

.. code-block:: python

Get the list of triangle (tri) element IDs on a surface.

This function returns the IDs of all triangle (tri) elements on the specified surface.

for tri_id in tri_ids: print(f" Tri ID: {tri_id}")

Get the surface type for a specified surface.

Title Available surface types

Find surfaces with narrow regions based on edge-pair orientation and proximity.

For each face of volumes in target_ids, iterates over every pair of non-adjacent edges. For each pair:

This function differs from get_closed_narrow_surfaces by checking all faces (not only closed two-loop faces), and from get_narrow_regions by requiring an oriented edge-pair test rather than loop-split or loop-proximity tests.

Find surfaces with tangential intersection angles outside specified bounds.

Iterates over all faces of volumes in target_volume_ids. For each face, computes any tangential intersection angles between adjacent faces. A surface is included if any angle is < lower_bound or > upper_bound.

type of target_volume_ids: std::vector< int,std::allocator< int > >

Retrieve the list of sweep target surfaces for a specified volume.

When a volume uses the Sweep scheme, target surfaces are the ending faces to which the hexahedral mesh is extruded. This function returns all surface IDs designated as targets. If no explicit target was set, returns an empty list.

Return the current target time step threshold used in the density multiplier metric.

This threshold influences adaptive time stepping by multiplying element-based estimates.

Retrieve the count of tetrahedral elements in the current model.

.. code-block:: python

Get the Global Element ID for a specific tetrahedral element.

This function returns the Global Element ID assigned to the given local tet ID when the element was placed into a block.

Get the growth factor for tet meshing on a volume.

The growth factor controls how quickly tetrahedral sizes can change when transitioning from small to larger elements within the volume. Valid values range from 1.0 (uniform sizing) to 10.0 (rapid growth).

Get the global flag indicating insertion of mid-edge (quadratic) nodes during tet meshing.

Returns true if the tet mesher is configured to create mid-edge nodes while generating tets (improves quadratic element quality); false if midnodes are inserted post-meshing.

Get the global flag indicating minimization of interior points in tet meshing.

Returns true if the tet mesher will attempt to reduce the number of interior nodes inserted; false if interior point insertion is unrestricted. Disabling interior point insertion may produce a mesh with fewer nodes but can fail in complex geometries.

Get the global flag indicating minimization of sliver tetrahedra.

Returns true if the tet mesher will apply additional processing to identify and remove sliver-shaped tetrahedra (minimize slivers); false if sliver removal is not explicitly requested.

Get the global number of anisotropic tet layers setting.

Returns how many anisotropic layers the tet mesher will attempt to place in thin regions. If this global setting is zero, anisotropic layering is disabled.

Get the global tet meshing optimization level.

Returns the integer optimization level in use for the tet mesher, ranging from 0 (none) to 6 (extreme). Higher levels yield better element quality at the expense of runtime.

Get the global flag indicating optimization of mid-edge nodes during tet meshing.

Returns true if the tet mesher is configured to optimize (adjust) mid-edge node positions during meshing to improve element quality; false if no midnode optimization is performed.

Get the global flag indicating optimization of overconstrained edges.

Returns true if the tet mesher will split edges that connect two surface nodes but do not lie on the surface ("overconstrained edges"); false if not.

Get the global flag indicating optimization of overconstrained tetrahedra.

Returns true if the tet mesher will optimize any tetrahedra that have more than one triangular face on the same geometric surface (removes "overconstrained" tets); false if not.

Get the global parallel-tetmesher flag (HPC) setting.

Returns true if the MeshGems-Tetra HPC (parallel) tet mesher is enabled globally; false if using the older serial tet mesher. This setting applies to all subsequent tet meshes until changed.

Get the proximity-layer flag for tet meshing on a volume.

Returns whether proximity layers are enabled for the specified volume. When enabled, the tet mesher will insert a minimum number of tetrahedral layers in thin regions to capture physical features.

Get the number of proximity layers for tet meshing on a volume.

Returns the integer number of tetrahedral layers configured for thin regions. Only valid if proximity is enabled; otherwise, returns zero.

Get the global flag indicating relaxation of surface mesh constraints in tet meshing.

Returns true if the tet mesher is configured to relax surface mesh conformity constraints, allowing insertion of tetrahedra that may deviate slightly from the exact surface mesh; false otherwise.

Get the tight bounding box for a list of entities.

Computes an oriented (tight) bounding box for the specified entities. The box is aligned with the principal axes of the geometry, not the global axes. This provides a minimal-volume bounding box that follows the geometry's orientation.

Get the combined bounding box for a list of entities.

.. code-block:: python

Get the total volume for a list of volumes.

.. code-block:: python

Retrieve the count of triangular elements in the current model.

For a tetrahedral volume mesh, returns the number of surface triangles.

Get the Global Element ID for a specific triangular element.

Cubit assigns a Global Element ID to each element when it is placed into a block. This function returns the Global Element ID corresponding to the given local tri ID within its type-specific ID space.

Retrieve the global geometry sizing flag for the TriMesh scheme.

If ON, TriMesh will incorporate the geometry approximation angle when computing element sizes. If OFF, geometry approximation is ignored.

Retrieve the global number of anisotropic triangle layers for the TriMesh scheme.

When ON, TriMesh will attempt to place specified layers of triangles in thin surface regions. Returns the number of layers; zero if anisotropic layers are disabled.

Retrieve the global ridge angle for the TriMesh scheme.

The ridge angle determines which angles in a discrete surface are preserved as ridges when meshing. Triangles on discrete surfaces with dihedral angles above this threshold remain as ridges.

Retrieve the global flag for splitting overconstrained edges in the TriMesh scheme.

If ON, TriMesh will split edges owned by a surface but whose nodes lie on curves, ensuring two elements through thickness in those regions.

Retrieve the global surface mesh gradation for the TriMesh scheme.

The surface gradation controls how quickly triangle sizes change on surfaces when using MeshGems. A value > 1.0 limits the size ratio of adjacent triangles; larger values yield faster growth.

Retrieve the global surface proximity ratio for the TriMesh scheme.

The proximity ratio is used when surface proximity is ON to scale the feature-based size in thin regions.

Retrieve the target minimum triangle size set on a specific geometry entity for the TriMesh scheme.

Returns the local "minimum size" constraint for the given entity (curve, surface, or volume) when using TriMesh. If no minimum was set on that entity, returns 0.

Retrieve the global tiny edge length for the TriMesh scheme.

The tiny edge length setting defines the minimum edge length below which elements are considered "tiny". TriMesh may use this value during cleanup or facet generation.

Retrieve the global surface proximity flag for the TriMesh scheme.

When enabled, surface proximity adds refinement in thin regions of surfaces based on a proximity ratio.

Retrieve the global volume mesh gradation for the TriMesh scheme.

The volume gradation controls how triangle sizes on adjacent surfaces respond to nearby features. This affects how small surface triangles propagate to neighboring regions.

Query whether undo is currently enabled.

.. code-block:: python

Identify unmerged curves between sheet (shell) volumes for use in shell construction workflows.

This function is normally used in the construction of shell representations from thin volumes. It identifies unmerged curve IDs on the specified shell_vols that are within the corresponding thickness distance of faces on other shell volumes in the list. These curves typically represent locations where the sheet bodies would need to be extended or trimmed to fully match the geometry of the original thin volumes.

Only sheet (shell) volumes are processed; solid volumes are ignored.

The thickness list specifies a proximity distance (normally the thickness of the original thin volumes) to use for detecting nearby curves. The list must match the length of shell_vols.

for c_id in unmerged_curves: print(c_id)

Get the valence (number of incident edges) for a specific vertex.

The valence of a vertex is the number of curves (edges) that meet at that vertex.

Get a list of valid element types for the specified block.

Returns the list of supported element types (e.g., "hex8", "hex20", "tet10") that can be assigned to the given block, based on its associated geometry or mesh configuration.

for t in valid_types: print(t)

Get the velocity's combine type.

Returns how multiple velocity boundary conditions are combined. Possible values include "Overwrite", "Average", "SmallestCombine", or "LargestCombine".

type of entity_id: int

Retrieve the current Cubit version string.

Returns the version identifier of the active Cubit engine, typically in "major.minor.patch" format.

Get the 3D coordinates of a vertex.

Returns the exact 3D coordinates for a vertex.

Get the current number of vertices in the model.

.. code-block:: python

Get the node ID owned by a vertex.

This function returns the ID of the node associated with the specified vertex. If the vertex does not have an associated node, the function returns -1.

Retrieve the vertex type for a given vertex on a surface.

Vertex types classify each corner based on how many mesh elements meet there:

Get the camera's current "at" (target) point.

Returns the xyz coordinates of the point that the camera is looking at. Requires an active graphics window; if graphics are disabled, this call may fail.

Get the camera's distance between its position and focus point.

Returns the straight-line distance from the camera "from" point to its "at" point. Requires an active graphics window; if graphics are disabled, this call may fail.

Get the camera's current 'from' (position) point.

Returns the xyz coordinates of the camera's location in space. Requires an active graphics window; if graphics are disabled, this call may fail.

Get the camera's 'up' direction vector.

Returns the normalized xyz vector that defines the upward orientation of the camera. Requires an active graphics window; if graphics are disabled, this call may fail.

Get the total surface area of a specified volume.

This returns the sum of all face areas bounding the volume.

Get the current number of volumes in the model.

.. code-block:: python

Retrieve the count of 3D elements in a specified volume.

Returns the total number of hexahedra, tetrahedra, pyramids, and wedges within the given volume (regardless of block assignments).

Suggests remedies for a gap between two surfaces on different volumes.

Given two surface IDs from different volumes that are close but separated by a gap, this function provides options to close or reconcile the gap.

To identify surface gaps, use get_gaps_between_volumes or get_volume_gaps.

for i in range(len(solutions[0])): print("Option:", solutions[0][i])

Get the list of hexahedron (hex) IDs contained in a volume.

This function returns the IDs of all hexahedron (hex) elements that are part of the specified volume.

for hex_id in hex_ids: print(f" Hex ID: {hex_id}")

Get the list of node IDs owned by a volume.

This function returns the IDs of nodes owned by the specified volume. Nodes on bounding surfaces, curves, and vertices are excluded. Only interior (volume-owned) nodes are returned.

for node_id in volume_nodes: print(f" Node ID: {node_id}")

Get the list of pyramid IDs contained in a volume.

This function returns the IDs of all pyramid elements that are part of the specified volume.

for pyr_id in pyramid_ids: print(f" Pyramid ID: {pyr_id}")

Get the list of tetrahedron (tet) IDs contained in a volume.

This function returns the IDs of all tetrahedron (tet) elements that are part of the specified volume.

for tet_id in tet_ids: print(f" Tet ID: {tet_id}")

Get the enclosed volume of a specified volume.

.. code-block:: python

Get the list of wedge IDs contained in a volume.

This function returns the IDs of all wedge elements that are part of the specified volume.

for wedge_id in wedge_ids: print(f" Wedge ID: {wedge_id}")

Retrieve the count of wedge-shaped elements in the current model.

.. code-block:: python

Get the Global Element ID for a specific wedge element.

This function returns the Global Element ID assigned to the given local wedge ID when the element is placed into a block.

Get the 'with-respect-to' entity of an item in a sideset.

This function returns the "with-respect-to" (WRT) entity associated with the specified entity (face, quad, or tri) in the specified sideset. The WRT entity provides context for how the sideset references or is oriented with respect to the entity.

Retrieve names and IDs of all defined groups (excluding the pick group).

Returns a vector of (name, ID) pairs for each active group in the current session.

for name, gid in groups: print(f"Group '{name}' has ID {gid}")

Check whether a geometric entity has a valid size.

Title This function returns whether the specified geometric entity currently has a valid size.

Check if a heatflux BC is on a shell area.

type of bc_area_enum: int

Highlight the given entity in the graphics window without selecting it.

Adds a visual highlight (for example, an orange colored overlay) to the specified entity. Unlike selection, highlighting does not add the entity to the pick list or change its selection state. Selecting an entity (for example, via "select volume 5") also produces a highlight, but calling this function only affects appearance.

Initialize the Cubit engine with optional startup arguments.

Must be called before any other Cubit API functions. Passing a single empty string in the argument list will launch Cubit with default settings.

type of argv: std::vector< std::string,std::allocator< std::string > >

Determine whether the ACIS geometry engine is available.

Notes ACIS is the default engine in standard Cubit distributions and should always be available.

Check if metadata is attached to a volume.

Used to validate part association or identify unassociated geometry. type of volume_id: int

Determine if a face's underlying surface is a blend (fillet).

Checks whether the surface with ID surface_id represents a blend created by a fillet operation.

Check if a boundary layer ID is currently available.

Useful for verifying uniqueness before assignment. type of boundary_layer_id: int

Determine whether the CATIA geometry engine is available.

Notes CATIA is not included in standard Cubit distributions. Only special builds with CATIA support will return true.

Return whether the specified surface is part of a cavity.

A cavity surface is a surface that bounds a closed void within the model geometry.

If the surface is part of a cavity (such as the inner walls of a subtracted volume), this function returns true; otherwise, false.

Determine if a face's underlying surface is a chamfer.

Checks whether the surface with ID surface_id represents a chamfer by comparing its maximum thickness to thickness_threshold.

Get the current clipping plane manipulation status :rtype: boolean.

Get the current clipping plane status :rtype: boolean.

Check if a surface has multiple loops closer than a given threshold.

Returns true if the face has two or more boundary loops and any two edges from different loops lie within mesh_size of each other. Otherwise returns false.

Check whether Cubit echoes commands to the console.

Returns true if each command is printed as it is executed.

Query whether Cubit is journaling commands.

Returns true if command journaling is currently enabled. Journaling is on by default, but may be turned off explicitly using a command or API call.

if not cubit.is_command_journaled() : print("Journaling is disabled.")

Determine whether a surface is a cone.

Returns whether the specified surface is a conical surface.

Notes This test returns true only for a single, complete cone that includes the apex (hard point). It is not intended to identify cone surfaces after a periodic split.

type of surface_id: int

Return whether the surface has any adjacent continuous surfaces.

Two surfaces are considered continuous if the exterior angle between them at a shared curve is 180 degrees +/- angle_tol.

Determine if a given face's underlying surface is a circular cylinder.

Checks whether the surface associated with the specified face ID is a true cylindrical surface.

Check whether a file is an HDF5 file.

.. code-block:: python

type of filename: string

Check if geometry graphics are visible in the graphics window.

Geometry display can be toggled on or off to show or hide CAD entities. This is useful when you want to view only the mesh without underlying geometry.

Return whether the specified surface is part of a hole.

A hole surface is one that bounds a small feature, such as a drilled or machined hole, whose maximum radius does not exceed the given threshold.

If radius_threshold < 0, the default is used: 3 x mesh_size.

Check if any loop on a surface has an odd number of mesh intervals.

The pave meshing scheme requires each loop on a surface to have an even number of intervals so that quads can be generated. Use this function to detect if a surface contains any loop with an odd interval count, which would prevent pave meshing.

if has_odd: print("Surface 5 contains an odd loop; cannot apply pave mesh.") else:

Check if a specified geometry entity has been merged into another.

This function returns true if the given entity-identified by its geometry type ("curve", "surface", or "volume") and integer ID-has been merged into a different entity; otherwise, it returns false.

After performing merge operations (for example, merge vol all), shared or redundant entities may no longer exist as standalone objects. Use is_merged() to verify whether a particular entity was absorbed by another during such operations.

if (cubit.is_merged ("surface", 6)) { std::cout << "Surface 6 has been merged." << std::endl; } else { std::cout << "Surface 6 is not merged." << std::endl; }

Check if a specific mesh element belongs to any group.

.. code-block:: python

if cubit.is_mesh_element_in_group ("tet", 445): print("Tet 445 is in a group") else:

Check if mesh graphics are visible in the graphics window.

Mesh display can be toggled on or off to show or hide mesh elements. Hiding mesh can improve performance when displaying the geometry.

Determine whether a specified geometry entity has been meshed.

Returns true if the given entity (curve, surface, or volume) already has a valid mesh; otherwise false.

if cubit.is_meshed ("surface", 137): print("Surface 137 is meshed.") else:

Check if the model has been modified since import or last save.

Returns true if any CAD operation has altered the current model state (e.g., remove surface 10 after an import), false if the model is still in its original, unmodified state.

Check if a body contains multiple volumes.

Cubit bodies typically consist of a single volume; multi-volume bodies are rare and usually arise from importing ACIS models. To split a multi-volume body into separate volumes, use: cubit.cmd ('split body <id>')

if multi: print("Body 10 has multiple volumes. Splitting...")

Determine if any two non-adjacent edges on the surface form a narrow region.

Iterates over all pairs of edges without a shared vertex. For each pair, if their shortest distance <= mesh_size and their local edge directions (relative to surface normals) differ by more than 15deg, the surface is marked narrow.

Check if occlusion is enabled.

Returns true if occlusion is currently active.

Check if a boundary condition is applied to a thin shell.

Valid for temperature, convection, and heatflux BCs.

type of bc_type_enum: int

Determine whether the OpenCASCADE geometry engine is available.

Notes OpenCASCADE is not included in standard Cubit distributions. Only special builds with OpenCASCADE support will return true.

Check if an ID is present in a list of IDs.

This function checks whether the specified target ID is present in the given list of IDs. Returns true if the target ID is found in the list; otherwise returns false .

Query whether an undo operation is currently being performed.

Use this to detect if Cubit is in the middle of executing an undo command.

Query whether a specified surface or curve is periodic.

.. code-block:: python

Check if perspective projection is enabled.

Returns true if the graphics window is using perspective projection; false if orthographic.

Check if journal playback is currently paused.

Returns true if journal playback is currently paused, either manually via pause_playback() or due to an error when playback-paused-on-error is enabled.

if cubit.is_playback_paused() : print("Playback is currently paused.")

Query whether playback is paused on error.

Returns the current setting that controls whether Cubit pauses journal playback when an error occurs.

if cubit.is_playback_paused_on_error() : print("Playback paused on error.")

Determine if a point is inside, outside, on, or unknown relative to a given entity.

Commonly used for volumes or sheet bodies to test point containment.

Return whether the specified surface is part of a protrusion.

A protrusion surface is a surface that bounds a region of material extending outward from the main geometry.

If the surface is part of a protrusion (such as a boss or raised feature), this function returns true; otherwise, false.

type of surface_id: int

Check if the scale annotation is visible in the graphics window.

The scale annotation displays X, Y, and Z axes (with unit markings) at the bounding box of the current objects. It helps judge physical dimensions.

Check if partial selection is enabled.

return type of : boolean

Determine if a volume is a sheet body (zero thickness).

.. code-block:: python

Check if a special build type is available.

Determines if the specified build_type corresponds to a special Cubit build or engine support compiled into this Cubit build. The comparison is case-insensitive and "acis", "catia", "goodyear", "granite", "machine_learning" ("ml"), "opencascade", and "sgm".

Check if a surface is meshable under the current meshing scheme.

Returns whether the specified surface can be meshed using the active mesh settings. Surfaces have a default scheme if none was explicitly set.

Query whether a specified surface is planar.

Some workflows require distinguishing planar faces from curved ones. Both is_surface_planer (archaic spelling) and is_surface_planar are provided for compatibility; they behave identically.

Check if a specific entity type is currently excluded from picking.

Returns true if the given type is in the pick filter list (i.e., will not be picked).

Check if the model requires an undo checkpoint save.

Returns true if any CAD operation has modified the model since the last call to set_undo_saved() .

Query whether a specified geometry entity is virtual.

.. code-block:: python

Query visibility for a specific geometry entity.

.. code-block:: python

if not cubit.is_visible ("volume", 4): print("Volume 4 is now hidden.")

if cubit.is_visible ("volume", 4): print("Volume 4 is now visible.")

Check if a volume is meshable under the current meshing scheme.

Returns whether the specified volume can be meshed using the active mesh settings. Volumes have a default scheme if none was explicitly set.

Check if the "-workingdir" option was provided at Cubit startup.

Determines whether the user specified a working directory on the Cubit command line using -workingdir <path>.

Enable or disable journaling of Cubit commands.

Controls whether commands issued via cubit.cmd or API calls are recorded in the active journal file. Journaling is enabled by default when Cubit starts.

Load machine learning training data into memory.

This function loads and caches the specified machine learning models for immediate use in predictions or feature extraction. If a model is required by another ML function and not yet loaded, it will be loaded automatically. Calling this function explicitly ensures the model is loaded immediately.

type of model_type: string, optional

if success: print("Regression models loaded.") else:

Returns the shortest distance between two geometry entities and their closest points.

Computes the closest points between two entities and returns the distance along with the coordinates of these points.

Force retraining of the ML classification model for a specific geometry type.

This function initiates a new training run for the specified classification operation. Currently, it is supported only for "volume_no_op" and "surface_no_op" models.

type of geom_type: string

if success: print("Training for surface model started successfully.") else:

Translates an Entity by a specified vector.

Moves the given entity by the offset defined in vector . Use preview to display the translation without applying it.

Query the number of undoable commands in the stack.

.. code-block:: python

Parse a Cubit-style entity selection expression into a list of IDs.

Converts a free-form Cubit entity expression?supporting ranges, name patterns, and topological queries?into a flat list of integer IDs for the given type.

Title Supported syntax examples

Parse a Cubit location specification into concrete 3D coordinates.

Accepts any Cubit-style location expression and returns the resulting point(s) as x-y-z triples. See documentation for supported location options.

Pause journal playback immediately.

Halts any ongoing playback of journal commands. Typically used within a journal file to pause execution for debugging or inspection. Playback can be resumed by calling resume_playback() .

Display Cubit's supported startup options.

Prints every command-line flag that the Cubit executable accepts when launched from a terminal, along with its syntax and description.

Example output (first few of many):

.. code-block:: python

Print all selected entities and their types.

Outputs each selection in order (index, type, and ID) to the console.

Print details of the current selected entity.

Shows the type and ID of the entity at the internal selection pointer.

Print a message through Cubit's messaging system.

Send an informational message to the Cubit message handler for display or logging.

Display context-sensitive help while typing commands.

Called when the user presses one of the help keys ('?', '&', or '!') at the prompt. It prints relevant syntax or usage hints based on the current input line.

Print summary statistics for all surfaces in the model.

Title Reported metrics

Print summary statistics for all volumes in the model.

Title Reported metrics

Create a prism of the specified dimensions.

Creates an extruded prism from a regular polygon base defined by major and minor radii. The prism height and number of sides specify its shape and extrusion.

Map points in a unit square (u-v coordinates on a quad face) and project them onto a surface.

For each (u, v) in pts (with values in [0, 1], representing local coordinates on the quad face), this function uses node00_id (u=0, v=0) and node10_id (u=1, v=0) to locate the corresponding point on the quad (quad_id), then projects that 3D point onto the specified surface (surface_id). Returns the 3D coordinates of each projected point.

for p in positions: print(p) # Each p is a list [x, y, z]

Create a pyramid of specified dimensions.

Creates an extruded pyramid from a regular polygon base defined by major and minor radii. The apex or top plateau size can be specified.

Reflects an Entity about a specified axis (e.g., plane normal).

Reflects the given entity across the plane perpendicular to axis . The original entity can be previewed without modification using preview .

Release a previously retrieved Cubit interface.

Decrements the reference count (or performs cleanup) for the given interface instance. After calling this, the pointer should not be used.

if iface is not None:

success = cubit.release_interface(iface) if not success: print("Failed to release interface")

Remove a specific entity from a given group.

.. code-block:: python

Remove an entity type from the graphics pick filter.

Disallows picking of the specified entity type; other filters remain unchanged.

Replace the current progress-bar callback handler and return the old one.

Unregisters the existing handler and replaces it with the given one. Returns the previous handler without deleting it.

Clears all geometry and mesh data currently loaded in the session, returning Cubit to its initial state.

Reset the camera view and clear auxiliary graphics windows.

Restores the default view, closes dialogs, and clears overlays.

Resume a paused journal playback.

Continues journal playback after it has been paused, either manually via pause_playback() or automatically due to an error when playback-paused-on-error is enabled.

Scales an Entity uniformly by a specified factor.

Scales the given entity by factor in all directions. Use preview to display the scaled geometry without applying it.

Set the behavior for block propagation during geometry copy.

Set the behavior for nodeset propagation during geometry copy.

Set the behavior for sideset propagation during geometry copy.

Enable or disable interruptible operations in Cubit.

When set to true, any interruptible Cubit process will be stopped at the next interrupt check.

Redirect Cubit output to a custom message handler.

Replace the default Cubit message handler so that all subsequent messages are routed to the provided handler instance, which must implement print_message() and/or print_error().

class MyHandler(cubit.CubitMessageHandler ): def print_message(self, message):

def print_error(self, message): print("[Error]", message, file=sys.stderr)

Sets scalar variables on specified mesh elements for Exodus export.

Assigns the element variable named variable_name to the elements in element_ids , using the corresponding values in variables . If variables contains a single entry, that value is applied to all elements; otherwise, its length must match element_ids . When exporting the mesh to an Exodus file, these element variables will be included for downstream analysis.

Set the name of a specified entity.

Equivalent to the command:

For example, to name vertex 22 "point_load":

.. code-block:: python

if success: print("Rename succeeded")

Set a custom exit callback for Cubit.

Provide an ExternalExitHandler-derived instance to handle Cubit's exit events.

class MyExitHandler(cubit.ExternalExitHandler ): def handle_exit_event(self, code):

Set multiple pick filter types for graphics selections.

Configures the graphics system to allow picking any entity whose type is in the provided list. Overrides any previously set pick filters.

Sets label display type for a given entity type.

Controls how labels are displayed for the specified entity type in the graphics window.

Valid entity_type values:

Label flag values ( SVUtil::LabelType ): 0=CUBIT_LABEL_NONE, 1=CUBIT_LABEL_ID, 2=CUBIT_LABEL_ELEMENT_ID, 3=CUBIT_LABEL_NAME, 4=CUBIT_LABEL_INTERVAL, 5=CUBIT_LABEL_SIZE, 6=CUBIT_LABEL_MERGE, 7=CUBIT_LABEL_IS_MERGED, 8=CUBIT_LABEL_FIRMNESS, 9=CUBIT_LABEL_SCHEME, 10=CUBIT_LABEL_NAME_ID, 11=CUBIT_LABEL_NAME_ONLY, 12=CUBIT_LABEL_SPHERE_ID

Reset Cubit's internal maximum group ID to a specified value.

Cubit tracks a monotonically increasing next group ID. GUI power tools may create and delete groups behind the scenes, incrementing Cubit's group ID counter and causing downstream journal files to reference unexpected IDs. This function restores control by resetting Cubit's max group ID, but only when the specified maximum_group_id matches Cubit's current highest ID?otherwise no change occurs.

type of maximum_group_id: int

Set the root directory for user-provided ML training data (classification only).

Specifies the location of user training files for classification operations. The directory must contain subfolders matching the ML operation names (e.g., "ml/volume_no_op").

Reset the model's modified status to "unmodified".

Clears the internal flag so that is_modified() returns false until the next CAD operation.

Sets scalar variables on specified mesh nodes.

Assigns the nodal variable named variable_name to the nodes in node_ids , using the corresponding values in variables . If variables contains a single value, that value is applied to all nodes; otherwise, its length must match node_ids . When exporting to Exodus, these nodal values will be included for analysis.

Set the maximum angle tolerance for calculating surface overlaps.

Updates the threshold that defines how much angular difference between surface normals can exist before surfaces are considered non-overlapping. Smaller values enforce stricter overlap detection by requiring surfaces to be nearly coplanar.

Set the maximum gap tolerance for calculating surface overlaps.

Updates the threshold that defines how large a gap between two surfaces can be before they are considered non-overlapping. Smaller values make the overlap test more stringent, while larger values allow greater discrepancies.

Set the minimum gap tolerance for calculating surface overlaps.

Updates the threshold that defines how small a gap between two surfaces can be before they are considered overlapping. Smaller values enforce stricter overlap detection by ignoring only very tiny gaps.

Set the current pick mode for entity selection.

Specifies which entity type the graphics system will select on the next pick. This determines the output of get_selected_ids() and pick dialogs.

Configure whether playback pauses on error.

Controls whether Cubit pauses journal playback automatically when an error occurs, allowing inspection before continuing.

Register a progress-bar callback handler with Cubit.

Sets the given handler as the active progress-bar callback. If a handler is already registered, it is released (but not returned).

class MyProgressHandler(cubit.CubitProgressHandler ): def start(self, title, info_string, hasCancel): print {info_string}") def end(self): print("Progress complete.") def percent(self, pcnt): print {pcnt * 100:.1f}%", end="\r") def check_interrupt(self): return False

type of progress: :py:class: CubitProgressHandler

Set the current graphics rendering mode (equivalent to "Graphics Mode <option>").

This is the programmatic equivalent of the Cubit command:

where mode can be one of HiddenLine , TrueHiddenLine , SmoothShade , Transparent , WireFrame , or GeomFacet . Instead of a string, this function accepts an integer code:

Clear the undo-needed flag for the model.

Marks the current model state as saved for undo purposes. After calling, is_undo_save_needed() returns false until the next modifying operation.

Execute a Cubit command without echoing or verbose output.

Behaves like cmd() , but suppresses prompt echo and messages–ideal for scripting.

Snaps given XYZ locations to nearest points on specified entity.

Points are first snapped to the closest location on the specified entity. Within the provided tolerance, points are then snapped preferentially to vertices, followed by curves.

Create all or part of a sphere.

Creates a spherical geometry of given radius. Optional planar cuts (along the yz, xz, or xy planes) and an inner radius for hollow spheres can be specified.

Advance to the next entity in the current selection list.

Moves the internal selection pointer forward, updating which entity is considered the "current" selection for print_currently_selected_entity() .

Move back to the previous entity in the current selection list.

Moves the internal selection pointer backward, so that the "current" selection reverts to the one before the last step.

Stop journal playback entirely.

Immediately terminates the execution of a journal file. This is typically used within a journal to abort playback due to errors or conditional logic. To restart, use resume_playback() or manually reissue commands.

Convert a list of integers into a compact Cubit-style ID string.

Collapses consecutive IDs into "start to end" ranges, separates entries with commas, and inserts line breaks at 80 characters for readability.

Performs a boolean subtract operation: removes tool bodies from target bodies.

Subtracts each body in tool_in from the corresponding body in from_in . The subtraction can imprint shared geometry if imprint_in is true, and the original bodies can be preserved if keep_old_in is true.

Retrieve a surface object by its ID.

Retrieves the surface object corresponding to the provided ID.

Sweep one or more curves along a path to create sheet bodies.

Constructs sheet bodies by sweeping the specified cross-section curves along the given path curves. Optional draft angle, draft type, and rigidity control taper and rounding behavior. This creates surface bodies (no solid volume); each returned Body contains exactly one Surface . Use the body's surfaces() method to access it and obtain area.

Check if a temperature BC is on a shell area.

type of bc_type_enum: int

Check if a temperature BC is applied to a solid region.

Valid for temperature and convection BCs.

type of bc_type_enum: int

Create a torus of specified dimensions.

Creates a toroidal geometry defined by the distance from center to the center of the swept circle (major radius) and the radius of the swept circle (minor radius).

2D equivalent of tweak_surface_offset: offsets specified curves on a sheet body.

Offsets each curve in curves by the corresponding value in distances on a 2D sheet body. The original sheet can be retained via keep_old , and a preview generated via preview .

Removes specified curves and extends adjacent surfaces on a sheet body.

2D equivalent of tweak_surface_remove. Removes each curve (edge) in curves from a 2D sheet body. Adjacent surfaces are extended to fill the gap created by removal. The original sheet can be retained via keep_old , and a preview can be generated without modification when preview is true.

Offsets specified surfaces by given distances.

Offsets each surface in surfaces by the corresponding value in distances , modifying the geometry and returning the resulting bodies (one per set of inputs).

Removes specified surfaces from a body, optionally extending adjacent surfaces.

Removes each surface in surfaces from its body. If extend_ajoining is true, adjacent surfaces are extended to close the gap. The original body can be retained via keep_old , and a preview can be generated without modification when preview is true.

2D sheet vertex chamfer: creates chamfers at specified vertices by offsetting adjacent curves.

Performs a chamfer operation at each vertex in verts on a 2D sheet body. Adjacent curves are trimmed and extended to form a flat face at distance radius from the vertex. The original sheet can be retained via keep_old , and a preview generated via preview .

Performs a boolean unite operation: merges specified bodies into one.

Unites the bodies in body_in into a single body. Surfaces in contact remain connected. The original bodies can be retained via keep_old_in .

Unload machine learning training data from memory.

This function clears cached ML models and releases associated resources for the specified type.

type of model_type: string, optional

Unselect an entity that is currently selected.

Removes the highlight and pick status of the specified entity.

Retrieve a vertex object by its ID.

Retrieves the vertex object corresponding to the provided ID.

Retrieve a volume by its ID.

Retrieves the volume object corresponding to the provided ID.

Determine whether a specified volume contains any tetrahedral elements.

.. code-block:: python

Report whether the last executed command was undoable.

Returns true if the most recent Cubit command supports undo; false otherwise.

Append a custom entry to Cubit's journal and recording streams.

Forces the given text to be recorded as if it were a Cubit command. This marks the model as modified and, if journaling and recording are enabled, writes the entry to the active journal and recording files.

**Examples:**

Example 1 (elixir):
```elixir
@n type of group_id:  int
```

Example 2 (elixir):
```elixir
@n type of group_id:  int
```

Example 3 (julia):
```julia
.. code-block:: python
```

Example 4 (elixir):
```elixir
@n type of filename:  string
```

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_cubit_failure_exception.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ what()

An exception class to alert the caller when the underlying Cubit function fails. More...

An exception class to alert the caller when the underlying Cubit function fails.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_loc.htm

**Contents:**
- Properties
- Detailed Description
- Property Documentation
- ◆ xVal
- ◆ yVal
- ◆ zVal

Defines a location object. More...

Defines a location object.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_body.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ get_mass_props()
- ◆ is_sheet_body()
- ◆ point_containment()
- ◆ volume()

Defines a body object that mostly parallels Cubit's Body class. More...

Defines a body object that mostly parallels Cubit's Body class.

Get the center of gravity of the Body .

Computes and returns the mass properties of this Body , specifically the center of gravity coordinates.

Get whether the Body is a sheet body or not.

Determines if this Body represents a sheet (2D) geometry rather than a volume (3D).

Determine point containment relative to the Body .

Checks whether a given point is inside, on, or outside this Body

Get the volume of the Body .

Notes This function is only available on Body objects.

**Examples:**

Example 1 (julia):
```julia
.. code-block:: python
```

Example 2 (cpp):
```cpp
@n return type of : std:: array< double,3 >
```

Example 3 (julia):
```julia
.. code-block:: python
```

Example 4 (elixir):
```elixir
@n return type of :  boolean
```

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_invalid_entity_exception.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ what()

An exception class to alert the caller that an invalid entity was attempted to be used. More...

An exception class to alert the caller that an invalid entity was attempted to be used.

Likely the user is attempting to use an Entity who's underlying CubitEntity has been deleted.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_c_f_d___b_c___entity.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ get_id()
- ◆ get_name()
- ◆ get_type()
- ◆ set_id()
- ◆ set_name()
- ◆ set_type()

Class to implement cfd bc data retrieval. More...

Class to implement cfd bc data retrieval.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_assembly_item.htm

**Contents:**
- Public Member Functions
- Properties
- Detailed Description
- Member Function Documentation
- ◆ get_id()
- ◆ get_instance()
- ◆ get_level()
- ◆ get_name()
- ◆ get_path()
- ◆ get_type()

Class to implement assembly tree interface. More...

Class to implement assembly tree interface.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_entity.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ bounding_box()
- ◆ center_point()
- ◆ id()

The base class of all the geometry and mesh types. More...

The base class of all the geometry and mesh types.

.. code-block:: python

Returns the axis-aligned bounding box of the Entity .

Computes the minimum and maximum coordinates of the Entityxs geometry in X, Y, and Z directions.

Returns the geometric center point of the Entity .

Computes the centroid of the Entityxs geometry based on its current position.

Retrieves the unique identifier of the Entity .

Returns the integer ID assigned to the Entity upon creation.

**Examples:**

Example 1 (julia):
```julia
.. code-block:: python
```

Example 2 (cpp):
```cpp
@n return type of : std:: array< double,6 >
```

Example 3 (julia):
```julia
.. code-block:: python
```

Example 4 (cpp):
```cpp
@n return type of : std:: array< double,3 >
```

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_cubit_message_handler.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ print_error()
- ◆ print_message()

CubitMessageHandler provides a way to override how messages are displayed to the user. More...

CubitMessageHandler provides a way to override how messages are displayed to the user.

You can derive from CubitMessageHandler to implement your own way of redirecting messages from Cubit to a different destination.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_surface.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ area()
- ◆ closest_point_along_vector()
- ◆ closest_point_trimmed()
- ◆ color()
- ◆ get_param_range_U()
- ◆ get_param_range_V()
- ◆ is_cylindrical()

Defines a surface object that mostly parallels Cubit's RefFace class. More...

Defines a surface object that mostly parallels Cubit's RefFace class.

Get area of the Surface .

.. code-block:: python

Get the nearest point on the Surface to point specified along the specified vector.

.. code-block:: python

Get the nearest point on the Surface to point specified.

.. code-block:: python

Get the color of the surface.

.. code-block:: python

Get range of u for the Surface .

.. code-block:: python

Get range of v for the Surface .

.. code-block:: python

Get whether the Surface is cylindrical or not.

.. code-block:: python

Get whether the Surface is planar or not.

.. code-block:: python

Get the normal at a particular point on the Surface .

.. code-block:: python

Get the ordered loops of the Surface .

.. code-block:: python

0, 0 - loop 1 curve 1

0, 1 - loop 1 curve 2

1, 0 - loop 2 curve 1

Get whether a point is on or off of the Surface .

.. code-block:: python

Get the Cartesian coordinates from the uv coordinates on the Surface .

.. code-block:: python

Get the principal curvatures of the Surface .

.. code-block:: python

Set the color of the surface.

.. code-block:: python

Get the uv coordinates from the supplied Cartesian coordinates on the Surface .

.. code-block:: python

**Examples:**

Example 1 (elixir):
```elixir
@n return type of :  float
```

Example 2 (cpp):
```cpp
@n type of location:  std::array< double,3 >, in
```

Example 3 (cpp):
```cpp
@n type of location:  std::array< double,3 >, in
```

Example 4 (cpp):
```cpp
@n return type of : std:: array< double,4 >
```

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_invalid_input_exception.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ what()

An exception class to alert the caller of a function that invalid inputs were entered. More...

An exception class to alert the caller of a function that invalid inputs were entered.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_curve.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ arc_center_radius()
- ◆ closest_point()
- ◆ closest_point_along_vector()
- ◆ closest_point_trimmed()
- ◆ color()
- ◆ curvature()
- ◆ curve_center()

Defines a curve object that mostly parallels Cubit's RefEdge class. More...

Defines a curve object that mostly parallels Cubit's RefEdge class.

Get the center and radius of an arc curve, otherwise returns 0 for non-arc.

.. code-block:: python

Get the curvature of the Curve at a particular point.

.. code-block:: python

Get the nearest point on the Curve to point specified along the specified vector.

.. code-block:: python

Get the closest location on the Curve from a particular point.

.. code-block:: python

Get the color of the Curve .

.. code-block:: python

Get the curvature of the Curve at a particular point.

.. code-block:: python

Get the center point of the Curve .

.. code-block:: python

Get the highest value of the Curve in uv space.

.. code-block:: python

Get the fraction along the Curve a specified arc length is away from a given Vertex .

.. code-block:: python

Get whether the Curve is periodic or not.

.. code-block:: python

Get the length of the Curve .

.. code-block:: python

Get the length between two specified parameters on a Curve .

.. code-block:: python

Get the position on a Curve that is a specified arc length away from the specified root parameter.

.. code-block:: python

Get the position of the point a specified fraction along the Curve .

.. code-block:: python

Get the position of a particular u value for the Curve .

.. code-block:: python

Set the color of the Curve .

.. code-block:: python

Retrieve the full set of spline parameters for this curve.

This method wraps the underlying geometry engine's spline-parameter routine (e.g., ACIS), extracting control point positions, weights, and knot data into a uniform flat vector. It throws InvalidEntityException for invalid entities and reports failure on non-spline curves.

for p in pts: print(f" {p}") print(f"Weights({m_w}): {weights}") print {knots}") print {reversed_flag}")

Get the lowest value of the Curve in uv space.

.. code-block:: python

Get the tangent to the Curve at a particular point.

.. code-block:: python

Get the u value for a point a specified arc length away from a specified root parameter on the Curve .

.. code-block:: python

Get the u value of a particular position on the Curve .

.. code-block:: python

**Examples:**

Example 1 (cpp):
```cpp
@n return type of : std:: array< double,4 >
```

Example 2 (cpp):
```cpp
@n type of point:  std::array< double,3 >, in
```

Example 3 (cpp):
```cpp
@n type of location:  std::array< double,3 >, in
```

Example 4 (cpp):
```cpp
@n type of point:  std::array< double,3 >, in
```

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_geom_entity.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ bodies()
- ◆ curves()
- ◆ dimension()
- ◆ entity_name()
- ◆ entity_names()
- ◆ is_meshed()
- ◆ is_transparent()

The base class for specifically the Geometry types (Body , Surface , etc.) More...

The base class for specifically the Geometry types (Body , Surface , etc.)

Retrieve bodies contained within the geometry entity.

Returns a list of Body objects associated with this GeomEntity , such as sheet bodies from a surface or volumes from a body.

Retrieve curves (edges) associated with the geometry entity.

Returns a list of Curve objects that bound this GeomEntity , such as the edges of a brick or boundary curves of surfaces.

Get the topological dimension of the geometry entity.

Returns the dimension (0 for Vertex , 1 for Curve , 2 for Surface , 3 for Volume/Body) of this GeomEntity .

for c in curves: print("Curve dimension:", c.dimension()) # Expected output: 1

Retrieve the primary name of the geometry entity.

Returns the first name assigned to this GeomEntity , useful for identification and labeling.

Retrieve all names assigned to the geometry entity.

Returns a list of every name that has been assigned to this GeomEntity , allowing enumeration of aliases or prior identifiers.

for n in names: print("Name:", n)

Returns the current mesh state of the GeomEntity .

Indicates whether the GeomEntity has mesh elements defined.

Get the transparency state of the geometry entity.

Returns whether this GeomEntity is currently rendered as transparent ( 1 ) or opaque ( 0 ).

Get the visibility state of the geometry entity.

Returns whether this GeomEntity is currently visible in the viewport (1) or hidden (0).

Generates mesh on a GeomEntity and verifies meshing status.

Discretizes the geometry of the given GeomEntity (e.g., surface, volume) into mesh elements. Use is_meshed to verify if meshing has been performed on the entity.

Get the count of names assigned to the geometry entity.

Returns the number of names currently assigned to this GeomEntity for tracking aliases or identifiers.

Remove a specific name from the geometry entity.

Deletes one of the names previously assigned to this GeomEntity , preserving any other names.

for n in names: print("Remaining name:", n)

Remove all non-default names from the geometry entity.

Deletes every custom name assigned to this GeomEntity , preserving its inherent default name.

Remove any mesh associated with the geometry entity.

Deletes the mesh on a GeomEntity

Assign a name to the geometry entity.

Sets the primary name of this GeomEntity for identification and labeling.

Set the transparency state of the geometry entity.

Toggles whether this GeomEntity is rendered with transparency. Passing 1 makes it transparent; 0 makes it opaque. The default state upon creation is transparent.

Set and verify the visibility state of the geometry entity.

Toggles whether this GeomEntity is rendered in the viewport. Passing true makes it visible; false hides it. Use is_visible() to query the current state.

Smooths the mesh on a GeomEntity to improve element quality.

Applies mesh smoothing to the existing mesh on the GeomEntity . Requires that the entity has already been meshed ( is_meshed() returns true). Smoothing method is based on the scheme currently set on the geomEntity (ie. Laplacian, Mean Ratio, etc.)

Retrieve surfaces associated with the geometry entity.

Returns a list of Surface objects that bound this GeomEntity , such as the faces of a brick.

Retrieve vertices (points) associated with the geometry entity.

Returns a list of Vertex objects that bound this GeomEntity , such as the corners of a brick.

Retrieve volumes associated with the geometry entity.

Returns a list of Volume objects associated with this GeomEntity , such as the volume created by a brick.

**Examples:**

Example 1 (julia):
```julia
.. code-block:: python
```

Example 2 (cpp):
```cpp
@n return type of : std::vector< CubitInterface::Body,std::allocator< CubitInterface:: Body > >
```

Example 3 (julia):
```julia
.. code-block:: python
```

Example 4 (cpp):
```cpp
@n return type of : std::vector< CubitInterface::Curve,std::allocator< CubitInterface:: Curve > >
```

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_dir.htm

**Contents:**
- Public Member Functions
- Properties
- Detailed Description
- Member Function Documentation
- ◆ angle()
- ◆ cross()
- ◆ dir_print()
- ◆ distance()
- ◆ dot()
- ◆ get_xyz()

Defines a direction object. More...

Defines a direction object.

Returns the interior of two vectors return the angle is in radians.

Returns the cross product of this X vec2 :rtype: :py:class: Dir

get the distance between two points

Returns the dot product.

Get an array of the vector.

Normalize 'this' vector :rtype: void.

Finds 2 (arbitrary) vectors that are orthogonal to this one.

Set the xyz values of the vector.

Set the x location of the point.

Set the y location of the point.

Set the z location of the point.

Get the x location of the point.

Get the y location of the point.

Get the z location of the point.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_mesh_import.htm

**Contents:**
- Public Member Functions
- Member Function Documentation
- ◆ add_elements()
- ◆ add_elements_to_block()
- ◆ add_elements_to_sideset()
- ◆ add_nodes()
- ◆ add_nodes_to_nodeset()
- ◆ create_block()
- ◆ create_nodeset()
- ◆ create_sideset()

Add elements of a single type.

The start ID of the first element is returned; this returned ID can be used in other functions.

.. code-block:: python

add a group of elements to a block.

.. code-block:: python

Add a group of sides to a sideset.

Sides are specified by element IDs and a side index.

.. code-block:: python

Add nodes with a given dimension.

The start ID of the first node is returned; this returned ID can be used in other functions.

.. code-block:: python

Add a group of nodes to a nodeset.

.. code-block:: python

Create a block with a preferred ID.

The assigned ID is returned.

Create a nodeset with a preferred ID.

The assigned ID is returned.

Create a sideset with a preferred ID.

The assigned ID is returned.

Print a message into the cubit message system.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_volume.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ centroid()
- ◆ color()
- ◆ principal_axes()
- ◆ principal_moments()
- ◆ set_color()
- ◆ volume()

Defines a volume object that mostly parallels Cubit's RefVolume class. More...

Defines a volume object that mostly parallels Cubit's RefVolume class.

Get the centroid of the Volume .

.. code-block:: python

Get the RGBA color of this Volume entity.

Retrieves the current display color of the volume as RGBA channels.

Example create a sphere with radius 1, apply a yellow color (via command or API), and retrieve its color.

Retrieve the principal axes of this Volume entity.

Returns the three principal directions (axes) of the volume, corresponding to its principal moments of inertia, as a flattened 3x3 matrix.

Example create a unit sphere and get its principal axes (unit vectors along X, Y, Z).

Get the principal moments of the Volume .

.. code-block:: python

Set the RGBA color of this Volume entity.

Applies a display color using red, green, blue, and alpha (opacity) channels.

Example create a sphere with radius 1, apply yellow color (full and semi-transparent) via command and API, and force graphics updates.

Compute the three-dimensional volume of this Volume entity.

Calculates the geometric volume enclosed by this Volume object.

Example create a sphere with radius 1 via command-line, obtain its Volume object, and measure its volume.

**Examples:**

Example 1 (cpp):
```cpp
@n return type of : std:: array< double,3 >
```

Example 2 (julia):
```julia
.. code-block:: python
```

Example 3 (cpp):
```cpp
@n return type of : std:: array< double,4 >
```

Example 4 (julia):
```julia
.. code-block:: python
```

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_vertex.htm

**Contents:**
- Public Member Functions
- Detailed Description
- Member Function Documentation
- ◆ color()
- ◆ coordinates()
- ◆ set_color()

Defines a vertex object that mostly parallels Cubit's RefVertex class. More...

Defines a vertex object that mostly parallels Cubit's RefVertex class.

Get the color of the Vertex .

.. code-block:: python

Get the Cartesian coordinates of the Vertex .

.. code-block:: python

Set the color of the Vertex .

.. code-block:: python

**Examples:**

Example 1 (cpp):
```cpp
@n return type of : std:: array< double,4 >
```

Example 2 (cpp):
```cpp
@n return type of : std:: array< double,3 >
```

Example 3 (cpp):
```cpp
@n type of value:  std::array< double,4 >, in
```

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_bolt_hole_info.htm

**Contents:**
- Properties
- Detailed Description
- Property Documentation
- ◆ bearingAxis
- ◆ bearingHoleSurfaces
- ◆ bearingRadius
- ◆ bearingVolume
- ◆ boundingBox
- ◆ id
- ◆ threadAxes

Struct for BoltHoleInfo data used in CubitInterface. More...

Struct for BoltHoleInfo data used in CubitInterface.

---

## 

**URL:** https://coreform.com/cubit_help/appendix/python/classcubit_1_1_volume_gap.htm

**Contents:**
- Properties
- Detailed Description
- Property Documentation
- ◆ gaps
- ◆ overlapAreas
- ◆ surfPairs
- ◆ volume1
- ◆ volume2

Struct for VolumeGap data used in CubitInterface. More...

Struct for VolumeGap data used in CubitInterface.

---
