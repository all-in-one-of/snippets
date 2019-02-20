

### Gradient on Curve
```
@gradient = @ptnum/(@numpt-1.0);
@ramponcurve = chramp('ColorRamp', gradient);  // map it to ramp
```

### Carve Curve
```cpp
//by @mr5iveThou5and:
float max = chf("max"); // like carve u parm
float min = chf("min"); // like carve v parm
vector uv;     
int primnum = @primnum;
float d = xyzdist(0, @P, primnum, uv);
@P = primuv(0, "P", primnum, set(fit01(uv.x,min,max), 0.0, 0.0));
```
### Delete last point
```cpp
@ptnum == `npoints(0)-1` //group the last point on curve
@ptnum == @numpt-1 // group the last point on curve
@ptnum%(@numpt-1)==0  //1st AND last point at the same time

0-`npoints(opinputpath(“.”,0))-2` // selects all points but the last. //
0 `npoints(0)-1` // select first and last point
/*to delete last point
- Delete By Pattern: $N
- Delete By Expression: $PT==$NPT-1
- Delete By Range: change Start to: $N*/
```

### Remove overlaped prims

```
int prim_points[] = primpoints( geoself(), @primnum );
vector pos_accum = 0;

for ( int i = 0; i < len(prim_points); i++ )
{
    pos_accum += attrib( 0, "point", "P", prim_points[i] );
}

pos_accum /= len(prim_points);

int xyz_prim;
vector xyz_uv;

float xyz_dist = xyzdist( 0, pos_accum, xyz_prim, xyz_uv);

if ( xyz_prim > @primnum && xyz_dist < 0.001 )
    removeprim(geoself(), @primnum, 1);
else if ( xyz_prim < @primnum && xyz_dist < 0.001 )
    removeprim(geoself(), xyz_prim, 1);
```
