
### OpInputs:
`opname(".")` // $OS ??  
`opinput(".", 0)` //   

`opfullpath(".")` - The full path of the current node being evaluated
`opfullpath("..")` - The full path of the current node’s parent
`opinputpath(".", 0)`  // path of the node connected to the first input.  
`opinputpath("../",0)` // path of geo (level up)    
`geoself()`  Returns a handle to the current geometry.   


```$HIP/geo/$HIPNAME.$OS.$F.bgeo.sc```   
```$HIP/render/${HIPNAME}_$(CHANNEL).png```  
```$HIP/${HIPNAME}/`detail(0,"AtribToGrabName", 0)`.fbx```   
```$HIP/${HIPNAME}/cache_`opname("..")`/$OS.obj``` - path with name of containter object  
```$HIP/`details("../", "filename")`.fbx``` - from detail attrib  
```$HIP/`opinput(".", -1)`.`$F-1`.bgeo.sc``` - used in Adress, read $OS from node refered in spare param    

```MyImage'$F+12'.pic```   
```Pics${W}x${H}/$F.pic.  ```   


### LOOP
Iterations:
```
detail(-1,"iteration", 0)
detail("../repeat_begin1_metadata1/","iteration", 0)
```
`npoints()` - fn similar to @ptnum should use whenever you want number of points from the other inputs of wrangle node (second, third an so on).  



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



## H Script file names
`$OS` - Operator String. Contains the current OP’s name.   
`$CH` - Current channel name.   
`$F` - The current frame, (as set with the Playbar controls).  
`$SF`- Sim,ulation frame (must be checked in dop object?).  
`$HFS` - The directory where Houdini is installed.    
`$HH` - $HFS/houdini.   
`$HIP` - The directory containing the current scene file.   
`$HIPFILE` - The full path of the current scene file, including the file extension.   
`$HIPNAME` - The name of the current scene file without the extension. 
`$PDG_DIR`   
`$PDG_SHARED_ROOT`  
`$HOME` - Your home directory.  
`$JOB` - The project directory.  
`$NFRAMES` (the number of frames in the animation) = `$FEND - $FSTART + 1`.  
`$ACTIVETAKE` - Contains the name of the current take.   
