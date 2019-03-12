# EMITER MODULES:
Emiter Spawn
``` 
- Particle ID  -   CPU ? - more persistent
- Execution Index - GPU ?
- ArrayIndex != ExecIndex (you can verify this by writing out Particles.MyExecIndex)

options:
- interpolated spawning 
- require ID
```
Emiter Update
```cpp
 - Age:  Emiter Looped Age - tyle żyją ile loop
- Generate location Event  // ADD TO LEADER
```
Particle Spawn
```
-
```
Particle Update
```
- Generate Houdini Event (jak zwykly event tylko z fn.)

```
Event Handler
```cpp
Event Handler Properties // ADD TO FOLLOWER 
Recive Enebt Locaation // ADD TO FOLLOWER```
Render
```

# NAME SPACES  
(readable/writable  R/W)  
`User `  /* ALL OUT DATA */ // set per component or through blueprints / R:  EVERYWHERE / W: NOT writable within Niagara.  
`System` shared by everything within the system  /   R:  EVERYWHERE /  W:   only within SYSTEM SCRIPT and persisted frame to frame.  
`Emitter` shared by everything within that emitter instance  /  R:  in EMITER & PARTICLE SCRIPTS  /   W:  only in EMITER SCRIPT and persisted frame to frame.   
`Particles` per-particle values  /   R:  only by PARTICLE SCRIPTS  /   W:  only by PARTICLE SCRIPT and persisted frame to frame.  
`Engine` defined within the runtime for Niagara itself R:  EVERYWHERE / W: NOT writable.  
`Module` defined within a module are R/W: within that module and in the owning context (System/Emitter/Particle) can be written to if you know the unique module name in that context. In other words, if you add a AddVelocity module, you can address its parameters from the owning particle update script by replacing "Module" with "AddVelocity".  
`NPC` Niagara Parameter Collection / usually followed by another sub-namespace that defines the name of the NPC from which you are pulling the value from.  
Arbitrary namespaces:  
`Physics/Temp/Transient/Etc.` are “temporary”, meaning they only have meaning for the script type that you are on. The values are scoped to that update, spawn or event and are not persisted in any way.  
`Particles.MyCompanyName.VariableName` Anything you create will follow that same paradigm. However, you can create sub-namespaces within the supported ones. So. is a perfectly valid namespace to organize all your custom variables into.  
`Output` Output namespace to signify that these are useful values for binding into other modules. convention: Output.Module.VariableName . is just a convention.    

# EXECUTION INDEX / POINT ID :
For this module we just need to get the particles execution index, make a Niagara ID and assign the execution index to the ID index, and then set Particles.RibbonID in the Map with our new ID

Now we can return to the Niagara Emitter stack and add our new module (I named it SetRibbonIDByExecOrder) to the Particle Spawn section. With this, every ribbon in the grid should have a unique ID.
https://unrealingens.wordpress.com/2018/06/11/exploring-niagara-pre-release-part-3//

# HOUDINNI ARRAY INTERFACE: 
`@id`  per particle  
`@time` of pop-up  
`@type` group   
*[emiter update]* spawn form array playback   
*[particle spawn]* hanldle spawn particles / by type   
### H EVENTS:   
*[particle update]* generate location event  // FOR LEADER  writing to struct pos and we can listen it    
*[Event handler]* is listening for event. //FOR FOLLOWER  

### POINT ANIM:

`@id` same for one particle   
`@life` Life set for first point    
`@time` arrival time // just normalize time before ezport!  check length from a to b and set time    
*[emiter update]* spawn form array playback    
*[particle spawn]* hanldle spawn particles  
*[particle update]* update pos from Harray  
