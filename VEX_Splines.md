

### Delete last point    
`@ptnum == @numpt-1` - group the last point on curve  
`@ptnum == npoints(0)-1` - group the last point on curve (using fn)  
`@ptnum%(@numpt-1)==0`  - first&last = 0 rest @ptnum   

0-`npoints(opinputpath(“.”,0))-2`- selects all points but the last.  
0 `npoints(0)-1` - select first and last point   

`neighbourcount(0, @ptnum) == 2` - Groupexpreesion SOP  

###  Gradient along curve:
```cpp
float ValueAlongSpline = @ptnum/(@numpt-1.0);
```
###  Gradient along curve (ramp):
```cpp
float gradient = @ptnum/(@numpt-1.0); //numpt is int .0 < will convert it   
@Cd.y = chramp('colorRamp', gradient);  
```
### Spring on Curve

```
float rad=chf("radius");
vector dir=set(0,0,1)*rad;
matrix3 myMatrix=set(v@T,v@B,normalize(cross(v@T,v@B)));
3@myMatrix=myMatrix;
float rot=radians(chf("rotate"));
float sum=0;
for (int i=0; i<=@ptnum;i++)
    {
    float tempt=float(i)/(@numpt-1);
    sum+=(chramp("rampRot",tempt)-0.5)*2/@numpt;
    }

sum*=360*chf("scaleRamp");
f@integralRamp=sum;


rot+=radians(sum);

rotate(myMatrix,rot,v@T);
dir=myMatrix*dir;
@P= @P+dir;
```


## Geometry From Spline 

### Polywire shape with ramp for combined curves 
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

### PolyWire pscale SOP
prim wrangle between resample and polywire  
```
i[]@primPts = primpoints(0, @primnum);

foreach (int i; int currentPoint; @primPts){
    float ramp_index = fit(i, 0, len(@primPts)-1, 0,1);
    f@widthPrim = chramp("shape", ramp_index)/20;
    setpointattrib(0, "width", currentPoint, @widthPrim, "set"); 
    }
```

### Carve Curve
```cpp
float max = chf("max"); // like carve u parm
float min = chf("min"); // like carve v parm
vector uv;     
int primnum = @primnum;
float d = xyzdist(0, @P, primnum, uv);
@P = primuv(0, "P", primnum, set(fit01(uv.x,min,max), 0.0, 0.0));
```

```cpp
float animDur       = f@perimeter * 400.0;

float n             = fit( noise( v@P * 22.0 ), 0.2, 0.8, 0.0, 1.0 );
float offset        = fit01( lerp( n, rand( @primnum ), 0.35 ), 0.0, 15.0 );
float animPer       = fit( @Time - offset, 0.0, animDur, 0.0, 1.0 );

int primPts[]       = primpoints( 0, @primnum );
foreach( int pt; primPts )
{
    float u         = point( 0, "curveu", pt );
    if( u > animPer ){
        removepoint( 0, pt );
    }
}

if( animPer > 0.0 ){
    vector pos      = primuv( 0, "P", @primnum, set( animPer, 0.0, 0.0 ) );
    int newPt       = addpoint( 0, pos );
    addvertex( 0, @primnum, newPt );
}
```

// Scale 10 times first and last points

```cpp
if ((@ptnum == 0) || (@ptnum == (@numpt-1))) f@pscale = 10; 
else f@pscale = 1;
// Scale 10 times first and last points, short form    
f@pscale = (@ptnum == 0) || @ptnum ==(@numpt-1) ? 10 : 1;
```

 convert | arg; 
--- | --- 
"poly" |  Closed polygon. Can use 0 or more points. 
"polyline"  |  Open polygon. Can use 0 or more points.      
"tet" | Tetrahedron primitive. Requires exactly 4 points. You cannot add vertices to this primitive.
"sphere", "circle", "tube", "metaball", "metasquad" |   Require exactly 1 point. You cannot add vertices to these primitives.
"AlembicRef", "PackedDisk" | Packed Alembic or packed disk primitive. Require exactly 1 point. You cannot add vertices to these primitives. 

### Measure
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



