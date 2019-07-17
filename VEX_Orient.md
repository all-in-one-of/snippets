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
`p@orient` (quaternion) - Orientation of the copy  float4 
`v@N` - Normal (+Z axis of the copy, if no orient)  
`v@up` - Up vector of the copy use with @N to orient inst (+Y axis of the copy, if no orient)  
`v@v` - Velocity of the copy (motion blur, and used as +Z axis of the copy if no orient or N)  
`p@rot` - (quaternion) - Additional Q rotation (applied after the orientation attributes above)  
`f@pscale` - Uniform scale   
`v@scale` - Non-uniform scale `scale(3@transform, vector(@pscale));` (keep transform:1)    
`v@trans` - Translation of the copy, in addition to P  
`v@P` - Translation of the copy - Instance Position   
 
 
 
matrix3 m = ident(); //create a def "identity" matrix, meaning no rotation  
 
 
#### Roatate Normal Along Tangent:
 Add polyframe with `tangent`. Run on points  
```
matrix rot = ident();
float angle = radians(ch("angle"));
rotate(rot, angle, @tangent);
@N= @N*rot;
```

#### Rotate Object about axies:
Point wrangle, input: geometry   
```cpp
matrix3 m = ident(); 
vector axis = chv("axies"); 
float angle = radians(ch('amount')*360); // rot 0-1 *360 > to radians 
rotate(m, angle, axis); 
@P *= m;  
```

#### Rotate Individual Points quaternion:
The maketransform() function used here instead of ident()  means our starting matrix is already pointing the way we want it to be before we start rotating. We define an axis and angle, exactly as before, and spin that matrix around. The last step is just converting the matrix to a quaternion and naming it @orient,  which the Copy SOP knows to read.  
// run@points,   
IN: points / OUT copy to points sop
```
v@up = chv("up_vector"); // create a 3x3 orientation matrix using N and up as  
matrix3 m = maketransform(@N, v@up);   
vector axis = @N;  
float angle = radians(ch("angle")); // or instead of angle: rand(@ptnum)*360  
rotate(m, angle, axis);  
p@orient = quaternion(m); // make the orient quaternion  
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
vector4 q = dihedral( point(geoself(), “P”, src_pt)-point(geoself(), “P”, src_opt), 
                     point(geoself(), “P”, dst_pt)-point(geoself(), “P”, dst_opt) );
@P = qrotate(q, @P)+point(geoself(), “P”, dst_pt)-qrotate(q, point(geoself(), “P”, src_pt));
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
https://www.toadstorm.com/blog/?p=493    
http://www.tokeru.com/cgwiki/?title=Copy,_Stamps,_Rotation,_Hscript,_Vex,_a_ramble  
http://yoong-cut-and.blogspot.com/2014/12/orienting-objects-to-curve-basic-of.html  
