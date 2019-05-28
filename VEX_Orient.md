Try to use one transform at a time:

If pivot exists, use it as the **[local transformation]** of the copy/instance.  
If the **[transform]** attribute exists: Use it as a 3×3/4×4 matrix to transform the copy/instance.  
//If the transform attribute does not exist:  
If the **[orient]** attribute exists: Use it to orient the copy/instance.  
//If the orient attributes does not exist:  
Orient the copy/instance using **[N]** as the +Z axis and up as +Y axis.  
If N does not exist, use **[v]** (velocity) if it exists.  
If the **[rot]** attribute exists, apply it after the above.  
If **[pscale]** exists, use it to scale the to scale the copy/instance (multiplied by scale if it exists).  
If **[scale]** exists, use it to scale the copy/instance (multiplied by pscale if it exists).  
If **[trans]** exists, use it and P to move the copy/instance.  

`v@pivot` - Local pivot point for the copy  
`3@` or `4@transform` - Transformmatrix overriding everything except translations from [P], [pivot], and [trans]  
`p@orient` float4 (quaternion) - Orientation of the copy  
`v@N` - Normal (+Z axis of the copy, if no orient)  
`v@up` - Up vector of the copy use with @N to orient inst (+Y axis of the copy, if no orient)  
`v@v` - Velocity of the copy (motion blur, and used as +Z axis of the copy if no orient or N)  
`p@rot` - float4 (quaternion) // Additional Q rotation (applied after the orientation attributes above)  
`f@pscale` - Uniform scale   
`v@scale` - float3 - Non-uniform scale `scale(3@transform, vector(@pscale));` //if transf 1  
`v@trans` - Translation of the copy, in addition to P  
`v@P` - Translation of the copy - Instance Position  
  
#### Roatate Normal by matrix:
rotate normals along tangent. Add polyframe with tangent before
```
matrix rot = ident();
float angle = radians(ch("angle"));
rotate(rot, angle, @tangent);
@N= @N*rot;
```

#### Rotate Object about axies:
```cpp
matrix3 m = ident(); //create a def "identity" matrix, meaning no rotation
vector axis = chv("axies"); // to this matrixa around given axies 
float angle = radians(ch('amount')); // rot to radians 
rotate(m, angle, axis); // multi each point by new matrix  (pivot @ orig to rot this in place)
@P *= m; // apply rotation
```

#### Rotate Individual Points quaternion:
The maketransform() function used here instead of ident()  means our starting matrix is already pointing the way we want it to be before we start rotating. We define an axis and angle, exactly as before, and spin that matrix around. The last step is just converting the matrix to a quaternion and naming it @orient,  which the Copy SOP knows to read.
```
// run@points, IN: points
v@up = chv("up_vector");
// create a 3x3 orientation matrix using N and up as
matrix3 m = maketransform(@N, v@up);
vector axis = @N;
float angle = radians(ch("angle"));
rotate(m, angle, axis);
p@orient = quaternion(m);// make the orient quaternion
// OUT TO COPY TO POINTS SOP
```

#### Rotate Packed Geometry:
```cpp
// run over poinwrangle with packed geo input:
matrix3 x = primintrinsic(0, "transform", @primnum); // matrix3 x = ident();
vector axis = normalize(chv("axis"));
float angle = radians(chf("angle"));
rotate(x, angle, axis);
setprimintrinsic(0, "transform", @primnum, x, "set");
```

#### Move an object to the origin and return back:
Create wrangle to move object to the origin
```
// Get center of the oject bounding box (centroid)
vector min = {0, 0, 0};
vector max = {0, 0, 0};
getpointbbox(0, min, max);
vector centroid = (max + min)/2.0;

// Build and apply transformation matrix
vector translate = centroid;
vector rotate = {0,0,0};
vector scale = {1,1,1};
matrix xform = invert(maketransform(0, 0, translate, rotate, scale));
@P *= xform;

// Store transformation matrix in attribute
4@xform_matrix = xform;
```
Create the second wrangle to return it to the original position
```
@P *= invert(4@xform_matrix);
```

#### Orient piece of geometry by 4 points: {@vux}
- src_pt - source point 1
- dst_pt - destination point 1
- src_opt - source point 2
- dst_opt - destination point 2
```
int src_pt = 10 ;
int dst_pt = 2 ;
int src_opt = 11 ;
int dst_opt = 3 ;
vector4 q = dihedral( point(geoself(), “P”, src_pt)-point(geoself(), “P”, src_opt), point(geoself(), “P”, dst_pt)-point(geoself(), “P”, dst_opt) );
@P = qrotate(q, @P)+point(geoself(), “P”, dst_pt)-qrotate(q, point(geoself(), “P”, src_pt));
```
