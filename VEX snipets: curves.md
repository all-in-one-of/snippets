# Curve/Spline

Gradient along curve:
```cpp
float ValueAlongSpline = @ptnum/(@numpt-1.0);
```
Curve on Ramp:
```cpp
float gradient = @ptnum/(@numpt-1.0); 
@Cd.y = chramp('colorRamp', gradient);  
```
measure:
```cpp
vector2 uv4 = set(f@curveu, 0);
uv4 = primuvconvert("op:../curve1", uv4, 0, chi("mode"));
f@curveu = uv4.x;
```

 convert | arg; | value
--- | --- | ---
real > unit |          0  |  0.11..   
real > unitlen |       1  |  0.9..
real > len |          2 |  15..
unit > real  |         3  |  9
unit > unitlen  |      4  | 0-1
unit > len    |        5  | dl! // 33 
unitlen > real  |      6  |  9
unitlen > unit  |       7  | 0-1
unitlen > len  |       8  | dl! // 33
len > real   |        9  |  0.06
len > unit    |        10  |  0.07
len > unitlen |      11  |  0.033


**Shape Polywire with ramp for combined curves**
```
// Create Primitive Wrangle before polywire, use @width as Wire Radius
// Get array of points in each curve (primitive)
i[]@primPts = primpoints(0, @primnum);

// For each point in current curve
foreach (int i; int currentPoint; @primPts){
    float ramp_index = fit(i, 0, len(@primPts)-1, 0,1);
    f@widthPrim = chramp("shape", ramp_index)/20;
    setpointattrib(0, "width", currentPoint, @widthPrim, "set"); 
    }
 ```

**Fade noise on curves with ramp**
```
// Requires uvtexture SOP in "Pts and Columns" mode before this wrangle

// Define UI controls
float remap_uv = chramp('remap_uv', @uv.x);
float power = chf('Noise_Power');
float freq = chf('Noise_Frequency');

// Create noise
vector noiseXYZ = noise(@P*freq);
// Modify noise values
vector displace = fit(noiseXYZ, 0,1, -1, 1)*power*remap_uv;
// Apply modified noise to a points position
@P += displace;
// Visualize fade ramp on curve
@Cd = remap_uv;
```
