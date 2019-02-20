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



```cpp

v@pivot // Local pivot point for the copy
3@ or 4@transform  // Transformmatrix overriding everything except translations from [P], [pivot], and [trans]
p@orient // float4 (quaternion) //Orientation of the copy
v@N // Normal (+Z axis of the copy, if no orient)
v@up // Up vector of the copy use with @N to orient inst (+Y axis of the copy, if no orient)
v@v // Velocity of the copy (motion blur, and used as +Z axis of the copy if no orient or N)
p@rot // float4 (quaternion) // Additional Q rotation (applied after the orientation attributes above)
f@pscale  // Uniform scale 
v@scale // float3 // Non-uniform scale
v@trans // Translation of the copy, in addition to P
v@P //  Translation of the copy  //   Instance Position

```

 if it's 1, you can use the scale() vex function(edited)like: scale(3@transform, vector(@pscale));
 


**rotate packed geo:**
```cpp
// run over poinwrangle with packed geo input:
matrix3 x = primintrinsic(0, "transform", @primnum); // matrix3 x = ident();
vector axis = normalize(chv("axis"));
float angle = radians(chf("angle"));
rotate(x, angle, axis);
setprimintrinsic(0, "transform", @primnum, x, "set");
```

**roatate matrix:**
```cpp
int numbers[] = array(1,2,3,4);
vector myVectorArray[] = v[]@myVectorArray; 
// load array attributes into local var

matrix3 m = ident(); //create a def "identity" matrix, meaning no rotation
vector axis = chv("axies"); // to this matrixa around given axies 
float angle = radians(ch('amount')); // rot to radians 
rotate(m, angle, axis); // multi each point by new matrix 
(pivot need to be @ orig to rot this in place)
@P *= m; // apply rotation
```

**rotate matrix to quaternions:**
The maketransform() function used here instead of ident()  means our starting matrix is already pointing the way we want it to be before we start rotating. We define an axis and angle, exactly as before, and spin that matrix around. The last step is just converting the matrix to a quaternion and naming it @orient,  which the Copy SOP knows to read.
```cpp
v@up = chv("up_vec");
matrix3 m = maketransform(@N, v@up); //3x3 otrien amtrix using N and up as ther principal axies 
vector axis = @N;
float angle = radians(ch("angle")); // now rot thji matrix round N axix at over time
rotate(m, angle, axis); //make the orient quaternion from this matrix
p@orient = quaternion(m);
```

