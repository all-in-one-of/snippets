# Wrangler:

**[attrib wrangle]:** //CVEX-contects  more generic and the trend seems to be steering away from sop/pop specific nodes. wrapper around the more generic "attribvop" sop.   Attrib Wrangle/VOP and other CVEX nodes like Geo Wrangle DOP, POP Wrangle DOP, Volume Wrangle...) and their VOP equivalents node set to run over Detail (only once) addprim() addpoint() addvertex() removeprim() removepoint() (There is no removevertex() functiononly Attribwrangle you can add geometry (points, prims etC), which you can't in a point wrangle.  Also the functions to access geometry are differen

**[pointwrangle]:**  //wraps around a vopsop which provides a bit more data to vex in order to qualify it as "vop" contex (still some functions  unique to Point Wrangle)

`f@` // float  
`u@` // vector2 (2 floats)  
`v@` // vector (3 floats)   
`p@` // vector4 (4 floats)  
`i@` // int  
`2@` // matrix2 (2×2 floats)   
`4@myMatrix4x4 = matrix( ident() );`  
`s@myString = "abc";`  


# Read Attribs
`v@P` // fetch point position from first imput  
`v@opinput1_P` // fetch attribute from second input  

`point(1, "Cd", @ptnum)`; // normal from 1st input (counting from 0)  
`point(1, 'Cd', pt);` Why 'Cd' not '@Cd': The @ syntax is specific to wrangles, if you look in vops you see they don't use that prefix. Internally attributes are just plain names, the @ is a shorthand so wrangles know when you're referring to attributes vs referring to local variables. As such, the point() function, which is much older than wrangles are, doesn't use @'s. @Matt  


# Vex reserved:

`break`, `bsdf`, `char`, `color`, `const`, `continue`, `do`, `else`, `export`, `false`, `float`, `for`, `forpoints`, `foreach`, `gather`, `hpoint`, `if`, `illuminance`, `import`, `int`, `integer`, `matrix`, `matrix2`, `matrix3`, `normal`, `point`, `return`, `string`, `struct`, `true`, `typedef`, `union`, `vector`, `vector2`, `vector4`, `void`, `while`  

# ATTRIBUTES: 
Material:

`s@shop_materialpath` - Path to a material. You can add this attribute to points using the Material surface node. When you instance an object onto a point with this attribute, the instanced object uses the given material. Not supported in the viewport.  

`s@material_override` A serialized Python dictionary mapping parameter names to values. You can add this attribute to points using the "override" controls on the Material surface node. When you instance an object onto a point with this attribute, the instanced object applies the given overrides to its material.  

#### Time
`f@Time` - Current time, in seconds // Float time `$T`  
`f@TimeInc` - Time increment per frame in seconds  
`f@Frame` -  Current frame//Float frame `$FF`  
`f@SimTime` - Float simulation time `$ST`, only present in DOP contexts.  
`f@SimFrame` -Float simulation frame `$SF`, only present in DOP contexts.  
`f@TimeInc` - Float time step `1/$FPS`    
`$F` - The current frame, (as set with the Playbar controls)  

#### General
`i@ptnum` - Point Number  
`i@numpt` - Total number of points  
`i@primnum` - Primitive Number  
`i@numprim` - Total number of primitives  
`i@vtxnum` - Vertex number  
`i@numvtx` - Total number of vertices  

#### Geometry  
`v@P` - Point/Primitive Position  
`v@N` - Point/Primitive/Vertex Normal - to initialize normals @N = @N  
`v@v` - Velocity (e.g. for motion blur / in particle systems)  
`f@pscale` - Uniform scale. Used in copy-SOP or particle systems  
`v@scale` - Non-Uniform scale. For use see pscale  
`v@up` - Up-Vector. Used together with @N to orient point/particle/instance    
`p@orient` - Quaternion defining the rotation of a point/particle/instance  
`p@rot` - Quaternion defining additional rotation  
`v@trans` - Translation of instance  
`3@transform` - Transformation matrix (used e.g. in Copy-SOP)  
`v@pivot` - Local pivot point for instance  
`f@lod` - Detail/Primitive Level of detail  
`v@rest` - Rest position  
`v@force` - Force (e.g. acting on particle)  
`f@age` - Particle Age  
`f@life` - Max. Particle Life  
`v@Cd` - color   
`v@Cd[2]` - [index] after the attribute name will get the blue channel   
of the diffuse color (Cd) attribute. can also use .x, .y, and .z  [0], [1], and [2]  

#### Volumes
`f@density` - Density of voxel  
`i@ix, @iy, @iz` - Voxel indices along each axis. Ranging from 0 to resolution-1  
`v@center` - Center of current Volume  
`v@orig` - Bottom left corner of current Volume  
`v@size` - Size of current Volume  
`v@dPdx` - Change in position to get from one voxel to the next in x direction  
`v@dPdy` - Change in position to get from one voxel to the next in y direction  
`v@dPdz` - Change in position to get from one voxel to the next in z direction  
`v@BB` - relative position inside bounding box. Ranging from {0,0,0} to {1,1,1}  

#### Shadin
`v@Cd` - Diffuse Color  
`f@Alpha` - Alpha transparency  
`v@uv` - Point/Vertex UV coordinates  
`v@Cs` - Specular Color  
`v@Cr` - Reflective Color  
`v@Ct` - Transmissive Color  
`v@Ce` - Emissive Color  
`f@rough` - Roughness  
`f@fresnel` - Fresnel coefficient  
`f@shadow` - Shadow intensity  
`f@sbias` - Shadow bias  

#### H Script file names
`$OS` - Operator String. Contains the current OP’s name `opname(".")`
`$CH` - Current channel name.   

`$HFS` - The directory where Houdini is installed.    
`$HH` - $HFS/houdini.   
`$HIP` - The directory containing the current scene file.   
`$HIPFILE` - The full path of the current scene file, including the file extension.   
`$HIPNAME` - The name of the current scene file without the extension. 
`$PDG_DIR`   
`$PDG_SHARED_ROOT`  
`$HOME` - Your home directory.  
`$JOB` - The project directory.  
`$NFRAMES` (the number of frames in the animation) = `$FEND - $FSTART + 1`.  
`$ACTIVETAKE` - Contains the name of the current take.   

`intrinsic` - being an extremely important and basic characteristic of a person or thing.  

# VEX
Accumulate
```
f@accusum = 0;

for(int i=0; i<@numpt; i++){
    @accusum = @accusum + point(0, 'mattemp', i);
    @testloopcount += 1;
    }
    
for(int j=0; j<@numpt; j++){
    setpointattrib(0, 'accu', j, @accusum);
    }
```

Collect in detail attrib:
```
vector p[];
p[0] = v@P;
setdetailattrib(0, "pArray", p, "append");
```








