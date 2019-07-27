- Particle IDs  -   CPU ? - more persistent  
- Execution Index - GPU ?  
- ArrayIndex != ExecIndex (you can verify this by writing out Particles.MyExecIndex)  


# EMITER MODULES:
Emiter Spawn
``` 
- local space
- deterministic
- interpolated spawning 
- require persistent ID
```
Emiter Update
```cpp
loop options
spawn: burst / rate / per unit 
```
Particle Spawn
```
Age:  Emiter Looped Age - tyle żyją ile loop
```
Particle Update
```
- Generate Houdini Event (jak zwykly event tylko z fn.)
- Generate location Event  // ADD TO LEADER
```
Event Handler
```cpp
Event Handler Properties // ADD TO FOLLOWER 
Recive Eneble Locaation // ADD TO FOLLOWER
Render
```

# NAME SPACES  
(readable/writable  R/W)  


---

NAME SPACE  | R | W | define | share within 
--- | --- | --- | --- | --- 
System | Everyehere | System | persisted frame 2 frame | system
Emitter | Emiter & Particle | Emitter | persisted frame 2 frame | emitter inst
Particles | Particle | Particle |  persisted frame 2 frame |  per-particle values
Engine |  Everyehere  | NOT | runtime for Niagara itself | 
Module | Module | Modules | within a module |
User |  Everyehere  | NOT | in component or through blueprints | **[ALL OUT DATA]**


  
`NPC` - Niagara Parameter Collection / usually followed by another sub-namespace that defines the name of the NPC from which you are pulling the value from.   

Arbitrary namespaces:  
`Physics/Temp/Transient/Etc.` - “temporary”, they only have meaning for the script type that you are on. The values are scoped to that update, spawn or event and are not persisted in any way.  
`Particles.MyCompanyName.VariableName` - Anything you create will follow that same paradigm. However, you can create sub-namespaces within the supported ones. So. is a perfectly valid namespace to organize all your custom variables into.  
`Output` - Output namespace to signify that these are useful values for binding into other modules. convention: Output.Module.VariableName . is just a convention.    

# MAP ATTRIBUTES

Particles.Lifetime

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
*[particle update]* generate location event  // LEADER  writing to struct pos and we can listen it    
*[Event handler]* is listening for event. // FOLLOWER  

### POINT ANIM:

`@id` same for one particle   
`@life` Life set for first point    
`@time` arrival time // just normalize time before ezport!  check length from a to b and set time    
*[emiter update]* spawn form array playback    
*[particle spawn]* hanldle spawn particles  
*[particle update]* update pos from Harray  
