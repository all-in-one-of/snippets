
### Inputs:
```cpp
@P // fetch point position from first imput
v@opinmut1_P // fetch attribute from second input

f@foo // fetch first input foo
f@opinput1_foo // fetch second input foo

v@opinput1_N // normal from 1st input (counting from 0)
point(1, @N, ptnum) // normal from 1st input (counting from 0)

opinput(".", 0) //
opinputpath(".", 0)  // path of the node connected to the first input.
opinputpath("../",0) // path of geo (level up)
op:`opinputpath("../", 1)` // Second context geometry
geoself()

opname(".")  // operatorstring $OS  @OpInput1  
```

`point(1, 'Cd', pt);` Why its 'Cd' and not '@Cd' is less easy to explain. The @ syntax is specific to wrangles, if you look in vops you see they don't use that prefix. Internally attributes are just plain names, the @ is a shorthand so wrangles know when you're referring to attributes vs referring to local variables. As such, the point() function, which is much older than wrangles are, doesn't use @'s.
```
@P = point(1, 'P', @ptnum);
@P = @opinput1_P;
```
`npoints()` - fn similar to @ptnum should use whenever you want number of points from the other inputs of wrangle node (second, third an so on).



`ch("Multi")`
`chramp()`

```glsl
int rampkeys = chramp("ramp");

for( int i=i; i<=rampkeys; i++){
    float pos = ch(sprintf("ramp%gpos", i));
    float val = ch(sprintf("ramp%gvalue", i));
}
```
