


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
