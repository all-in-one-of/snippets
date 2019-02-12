// curve >> resample
// curveu (resample sop ?)- unit curve parametter for point
refine 

Curve/Spline
```cpp
float ValueAlongSpline = @ptnum/(@numpt-1.0); // Gradient along curve 
```

```cpp
float gradient = @ptnum/(@numpt-1.0); 
@Cd.y = chramp('colorRamp', gradient);  //Curve on Ramp:
```

```cpp
vector2 uv4 = set(f@curveu, 0);
uv4 = primuvconvert("op:../curve1", uv4, 0, chi("mode"));
f@curveu = uv4.x;

//PRIMUV_REAL_TO_UNIT         0 // 0.11..   
//PRIMUV_REAL_TO_UNITLEN      1 // 0.9..
//PRIMUV_REAL_TO_LEN          2 // 15..
//PRIMUV_UNIT_TO_REAL         3 // 9
//PRIMUV_UNIT_TO_UNITLEN      4 0-1
//PRIMUV_UNIT_TO_LEN          5 dlugosc w unitach // 33 
//PRIMUV_UNITLEN_TO_REAL      6 // 9
//PRIMUV_UNITLEN_TO_UNIT      7 0-1
//PRIMUV_UNITLEN_TO_LEN       8 dlugosc w unitach // 33
//PRIMUV_LEN_TO_REAL          9 // 0.06
//PRIMUV_LEN_TO_UNIT          10 // 0.07
//PRIMUV_LEN_TO_UNITLEN       11 // 0.033
```
