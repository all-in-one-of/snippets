## Functions
```cpp

float randValue(float seed; int pointNum) {
 float val = rand(seed * pointNum);
 return val;
}
float seed = 1.12345;
@Cd.y = randValue(seed, @ptnum);
```
```cpp
int test(int a, b; string c) {
    if (a > b) {
        printf(c);
    }
}


```
## Conditioning
```glsl
if(b < a) {
    s@out = "true";
}
else {
    s@out = "false";
}
```
```glsl
if(b < a)
    s@out = "true";
else
    s@out = "false";
```

(condition) ? true : false // conditional (ternary)  
simple condition can be written in the same line
```cpp
@Cd = (@ptnum <= 0 || @ptnum >= (@numpt-1)) ? 1 : 0;  
v@P.x *= v@P.x > 0 ? 0.5 : 1.5;
int condition = (@P.x > 0) ? 1 : 3;
```
or in any other line, since VEX is not indented language, 
but this works only for one operation, else-if block will 
end with the first semicolon
```cpp
if (v@P.y < 0) v@Cd = {1,0,0}; 
else if (v@P.x < 0)  v@Cd = {0,1,0}; 
```
 use of logical operators AND: &&, OR: ||
```cpp
if (v@P.y < 0 && v@P.x > 0) v@P -= v@N * .3;    
if (v@Cd == {0,0,1} || v@Cd == {1,0,0}) v@P += v@N * .4;   
```
## For Loop
VEX uses C-like syntax for for-loops
```cpp
int valA = 2;
for (int i=0; i<11; i++) {
    valA *= 2;
}
i@valA = valA;
```
```cpp
for(int i = 0; i < npoints(0); i++) { }; // for na wszystkich punktach:
for (int i=0; i<@numpt; i++) { }; // for na wszystkich punktach:
```
## ForEach Loop (arrys)
```cpp
int vertices[] = pointvertices(0, 10);
foreach (int num; vertices) {
 @P %= num/10;
 @Cd = @P;
}
```
```cpp
int nbs[] = nearpoints(0, v@P, .5);
vector P_avg = {0};
foreach(int nb_ptnum; nbs) {
    P_avg += point(0, "P", nb_ptnum);
}
P_avg /= len(nbs);
v@P = P_avg;
```
"break" keyword - can stop the loop at any point
```cpp
int valB = 5;
for (int i=0; i<13; i++) {
    valB *= 5;
    if (valB > 10000000) break;
}
i@valB = valB;
```
"continue" keyword to jump to the next loop iteration. in this example we average point position with positions of neighbours 
// which are above it in world space (their Y coordinate is larger)
```cpp
int pts[] = neighbours(0, @ptnum);
vector P_avg_upper = {0};
int count = 0;

foreach(int nb_ptnum; pts) {
    vector pos = point(0, "P", nb_ptnum);
    if (pos.y <= v@P.y) continue;
    P_avg_upper += pos;
    count++;
}

P_avg_upper /= count;
v@P = P_avg_upper;
```

## Arrays
```cpp
int MyArray[] = {}; // declare var
i[]@MyArray = {-1,0,1}; // declare attrib
i@MyArray[1] = @primnum; // Set primnum in array[1]


removevalue(i[]@MyArray, ValueToRemove); 
i[]@connected_pts = neighbours(0, @ptnum);
```
This code, even thou it also runs in detail mode, 
iterates over the geometry points, reads their positions 
(with use of “point” function) and puts each value into 
a detail array called “myarray”. This is a vector array
```cpp
v[]@myarray;
for(int i=0; i<@numpt; i++)
{
vector item = point(0, 'P', i);
insert(@myarray, 0, item);
}
```
This code expects an existing detail array called “pt” 
(listing input point numbers). It is imported as a local 
point array and iterated over in foreach loop.
If any array element modulo of 2  is equal to zero, 
point with the same number is colored.
```cpp
int importarray[] = detail(0, 'pt');
foreach(int i; importarray)
{
if(i%2 == 0)
{
setpointattrib(0, 'Cd', i, {1,0,0});
}
}
```
