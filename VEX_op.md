

### LOOP
Iterations:
```
detail(-1,"iteration", 0)
detail("../repeat_begin1_metadata1/","iteration", 0)
```
Get name of node from spare input: -1
```
$HIP/cache/Clouds.`opinput(".", -1)`.`$F-1`.bgeo.sc
```

`npoints()` - fn similar to @ptnum should use whenever you want number of points from the other inputs of wrangle node (second, third an so on).  

### Inputs:

`opname(".")` // $OS ??  
`opinput(".", 0)` //   

`opinputpath(".", 0)`  // path of the node connected to the first input.  
`opinputpath("../",0)` // path of geo (level up)   
`geoself()`  Returns a handle to the current geometry.  
used in Adress, read $OS from node refered in spare param:
```
$HIP/`opinput(".", -1)`.`$F-1`.bgeo.sc
```


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
