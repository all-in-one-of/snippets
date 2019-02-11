Transform Q:

If pivot exists, use it as the **[local transformation]** of the copy/instance.--

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
3@ or 4@transform  // Transformation matrix overriding everything except translations from P, pivot, and trans.
p@orient // float4 (quaternion) //Orientation of the copy
v@N // Normal (+Z axis of the copy, if no orient)
v@v // Velocity of the copy (motion blur, and used as +Z axis of the copy if no orient or N)
p@rot // float4 (quaternion) // Additional rotation (applied after the orientation attributes above)
f@pscale  // Uniform scale
v@scale // float3 // Non-uniform scale


v@P //  Translation of the copy
v@trans // Translation of the copy, in addition to P

v@up // Up vector of the copy (+Y axis of the copy, if no orient)
```

 if it's 1, you can use the scale() vex function(edited)like: scale(3@transform, vector(@pscale));
