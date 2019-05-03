

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

### OpInputs:
`opname(".")` // $OS ??  
`opinput(".", 0)` //   

`opfullpath(".")` - The full path of the current node being evaluated
`opfullpath("..")` - The full path of the current node’s parent
`opinputpath(".", 0)`  // path of the node connected to the first input.  
`opinputpath("../",0)` // path of geo (level up)    
`geoself()`  Returns a handle to the current geometry.   
```$HIP/`opinput(".", -1)`.`$F-1`.bgeo.sc``` - used in Adress, read $OS from node refered in spare param  


### channels:
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

 you can interact with ramp keys just like a multiparm block. The ramp parameter itself has the value of how many keys there are:

```
c int rampkeys = chramp(“ramp”);
for( int i=i; i<=rampkeys; i++){ float pos = ch(sprintf("ramp%gpos", i)); 
float val = ch(sprintf("ramp%gvalue", i)); // Do stuff }
```
@flight404 (I normally don’t condone 1-based loop indices but the keys do start at 1 and not 0. I supposed you could switch to doing `i+1` in the `sprintf` calls though if you wanted)  
