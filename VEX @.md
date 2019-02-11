Wrangle
[attrib wrangle]: //CVEX-contects  more generic and the trend seems to be steering away from sop/pop specific nodes. wrapper around the more generic "attribvop" sop.   Attrib Wrangle/VOP and other CVEX nodes like Geo Wrangle DOP, POP Wrangle DOP, Volume Wrangle...) and their VOP equivalents node set to run over Detail (only once) addprim() addpoint() addvertex() removeprim() removepoint() (There is no removevertex() functiononly Attribwrangle you can add geometry (points, prims etC), which you can't in a point wrangle.  Also the functions to access geometry are differen

[pointwrangle]:  //wraps around a vopsop which provides a bit more data to vex in order to qualify it as "vop" contex (still some functions  unique to Point Wrangle)
```cpp
f@ // float
u@ // vector2 (2 floats)
v@ // vector (3 floats) 
p@ // vector4 (4 floats)
i@ // int
2@ // matrix2 (2×2 floats) 
4@myMatrix4x4 = matrix( ident() );
s@myString = "abc";
```


ATTRIBUTES: 
Time:
```cpp
f@Time // Current time, in seconds//Float time ($T)
f@TimeInc   // Time increment per frame in seconds
f@Frame  //  Current frame//Float frame ($FF)
f@SimTime // Float simulation time ($ST), only present in DOP contexts.
f@SimFrame // Float simulation frame ($SF), only present in DOP contexts.
f@TimeInc // Float time step (1/$FPS)
```
General
```cpp
i@ptnum //Point Number
i@numpt //Total number of points
i@primnum //Primitive Number
i@numprim //Total number of primitives
i@vtxnum //Vertex number
i@numvtx   // Total number of vertices
```
Geometry
```cpp
v@P   // Point/Primitive Position
v@N   // Point/Primitive/Vertex Normal - to initialize normals @N = @N
v@v   // Velocity (e.g. for motion blur / in particle systems)
f@pscale  //   Uniform scale. Used in copy-SOP or particle systems
v@scale   // Non-Uniform scale. For use see pscale
v@up    //Up-Vector. Used together with @N to orient point/particle/instance
p@orient    //Quaternion defining the rotation of a point/particle/instance
p@rot //Quaternion defining additional rotation
v@trans    //Translation of instance
3@transform   // Transformation matrix (used e.g. in Copy-SOP)
v@pivot    //Local pivot point for instance
f@lod  //  Detail/Primitive Level of detail
v@rest   // Rest position
v@force    //Force (e.g. acting on particle)
f@age //Particle Age
f@life //Max. Particle Life
v@Cd // color 
v@Cd[2]  //  [index] after the attribute name will get the blue channel 
of the diffuse color (Cd) attribute. can also use .x, .y, and .z  [0], [1], and [2]
```
Volumes
```cpp
f@density  //  Density of voxel
i@ix, @iy, @iz   // Voxel indices along each axis. Ranging from 0 to resolution-1
v@center   //  Center of current Volume
v@orig   // Bottom left corner of current Volume
v@size  //  Size of current Volume
v@dPdx  //  Change in position to get from one voxel to the next in x direction
v@dPdy  //  Change in position to get from one voxel to the next in y direction
v@dPdz  //  Change in position to get from one voxel to the next in z direction
v@BB // relative position inside bounding box. Ranging from {0,0,0} to {1,1,1}
```
Shading
```cpp
v@Cd  //  Diffuse Color
f@Alpha //   Alpha transparency
v@uv // Point/Vertex UV coordinates
v@Cs // Specular Color
v@Cr // Reflective Color
v@Ct // Transmissive Color
v@Ce // Emissive Color
f@rough // Roughness
f@fresnel // Fresnel coefficient
f@shadow // Shadow intensity
f@sbias // Shadow bias```
COPY TO POINT SOP```cpp
v@P //   Instance Position
f@pscale  //  Uniform scale
v@scale  //  Non-Uniform scale
v@N //   Normal (+Z axis of the copy, if no orient)
v@up  //  Up-Vector. Used with @N to orient inst(+Y axis of the copy, if no orient)
v@orient  //  Quaternion defining the rotation of a point/particle/instance
v@rot // Quaternion defining additional rotation (applied after @orient)
v@v  //  Velocity (motion blur, also used as +Z axis of the cop
```