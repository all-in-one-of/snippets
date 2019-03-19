
### Inputs:
`v@P` // fetch point position from first imput  
`v@opinput1_P` // fetch attribute from second input  
`point(1, @P, ptnum)` // normal from 1st input (counting from 0)  
`point(1, 'P', @ptnum)` ?????????    
`opname(".")` // $OS ??  
`opinput(".", 0)` //   
$HIP/``opinput(".", -1)``.``$F-1``.bgeo.sc // in from 1 geo   
`opinputpath(".", 0)`  // path of the node connected to the first input.  
`opinputpath("../",0)` // path of geo (level up)  
op:``opinputpath("../", 1)`` // Second context geometry  
`geoself()`  

`point(1, 'Cd', pt);` Why 'Cd' not '@Cd': The @ syntax is specific to wrangles, if you look in vops you see they don't use that prefix. Internally attributes are just plain names, the @ is a shorthand so wrangles know when you're referring to attributes vs referring to local variables. As such, the point() function, which is much older than wrangles are, doesn't use @'s. @Matt  


`npoints()` - fn similar to @ptnum should use whenever you want number of points from the other inputs of wrangle node (second, third an so on).  

`ch("Multi")`  
`chramp()`  

Rampkeys:  
```glsl 
int rampkeys = chramp("ramp");

for( int i=i; i<=rampkeys; i++){
    float pos = ch(sprintf("ramp%gpos", i));
    float val = ch(sprintf("ramp%gvalue", i));
}
```
