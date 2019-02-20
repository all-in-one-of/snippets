





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

## [detial]  Arraty from points.

```cpp
int npt = npoints(0); 
vector all_pos[];
resize(all_pos, npt);

for(int i = 0; i < npt; i++) {
    all_pos[i] = point(0, "P", i);
} 
```
