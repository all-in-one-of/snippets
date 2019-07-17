# Point Clouds

Point Clouds architecture in VEX is based on data structure called kd-trees. They are created in memory from Houdini geometry and kept in cache for a period of VEX execution. Handle is like a reference of this structure inside a single VEX instance . If you create two point clouds, they will probably have handles 0 and 1 pc functions require that handle to find the point cloud to both read and write in to the separate memory. It's basically an integer which lets you tell to other pc* functions which point cloud you're interested in (among many possibly created)

`pcopen()` - the points are ordered from closest to farthest. also, if you simply restrict your pcopen() to a single point, it will be the one that's closest to your search point.  

`int handle = pcopen("test.pc", "P", P, "N", N, 1e6, 100, "ndot", 0.8);` // This will only return points where dot(N, Npoint) > 0.8 Returns a handle to a point cloud file.  
`pcfilter()` Filters points found by pcopen using a simple reconstruction filter.  
`int pts[] = pcfind(1,'P',@P,ch('d'),25);` Returns a list of closest points from a file.  
`pcfind_radius` Returns a list of closest points from a file taking into account their radii.  
`pcfarthest()` Returns the distance to the farthest point found in the search performed by pcopen.  
 
`pcclose(handle)` Na koniec zamykamy uchwyt, aby uzyskać dostęp do bazy danych punktu 


#### Avg Position from 1Op 
```
int mypc = pcopen(1, 'P', @P, ch('d'), chi('amnt'));
@P = pcfilter(mypc, 'P');
```
 
```cpp
int pc_ptnum, pc_points;
float pc_attr, accum;
vector pc_pos;

pc_points = 40;
pc_attr = 0;
accum = 0;

int handle = pcopen(@OpInput1, "P", @P, 1000, pc_points);

while(pciterate(handle)) { //untill there are points

    pcimport(handle, "point.number", pc_ptnum);

    if (pc_ptnum == @ptnum)
        continue; 
    
    pcimport(handle, "Alpha", pc_attr);

    accum += pc_attr;
}
pcclose(handle);
f@Alpha = accum / pc_points;
```
Performing a proximity query  

```cpp
int handle = pcopen(texturename, "P", P, maxdistance, maxpoints);
while (pcunshaded(handle, "irradiance"))
{
    pcimport(handle, "P", cloudP);
    pcimport(handle, "N", cloudN);
    ir = computeIrraciance(cloudP, cloudN);
    pcexport(handle, "irradiance", ir);
}
pcfilter(handle, radius, "irradiance", ir);
```


### GEOMETRY PROXIMITY  
`neighbour()` point number of the next point connected to a given point   
`neighboucount()` number of edges from point // i@count = neighbourcount(0,@ptnum);  
`neighbours()`  array of the point numbers of the neighbours of a point.   
`nearpoint()` - closest point in a geometry  
`nearpoints()` - all the closest point in a geometry.  
`minpos()` - closest position on the surface of a geometry  
`surfacedist()` - distance of a point to a group of points along the surface of a geometry  
`xyzdist()` - distance of a point to a geometry.   


```cpp
int []
neighbours(int opinput, int ptnum)
{
    int     i, n;
    int     result[];
    n = neighbourcount(input, ptnum);
    resize(result, n);
    for (i = 0; i < n; i++)
        result[i] = neighbour(input, ptnum, i);
}
```

```cpp
int nearpt = nearpoints(0, @P, 1e34, 2)[1:][0]; // find a nearest point which is not self
int neighbourcount(0, @ptnum); // count of neighbours `neighbourcount` / `neighbours` Connected Points:
i[]@connected_pts = neighbours(0, @ptnum); // get matrix with all neighbours
```

```cpp
int [] nearpoints(<geometry>geometry, vector pt, float maxdist, int maxpts) 
```

 ****if a point is inside, or below a surface based on normals.****
 ```
f@radius = 100000;
i@maxPoints = 10;
i@handle = pcopen(@OpInput2, “P”, @P, @radius,@maxPoints);
@N = pcfilter(@handle,“N”);
v@groundP = pcfilter(@handle,“P”);
v@up = normalize(@P - @groundP);
@Cd = dot(@up,@N);
```

