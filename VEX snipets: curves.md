# Curve/Spline
curve >> resample // refine
Gradient along curve:
```cpp
float ValueAlongSpline = @ptnum/(@numpt-1.0);
```
//Curve on Ramp:
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
unit > len    |        5  | dlugosc w unitach // 33 
unitlen > real  |      6  |  9
unitlen > unit  |       7  | 0-1
unitlen > len  |       8  | dlugosc w unitach // 33
len > real   |        9  |  0.06
len > unit    |        10  |  0.07
len > unitlen |      11  |  0.033
