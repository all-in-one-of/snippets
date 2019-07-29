

# EMITER MODULES:
Emitter Spawn
- local space
- deterministic
- interpolated spawning 
- require persistent ID  // - Particle IDs  -   CPU ? - more persistent  

Emitter Update  
- spawn loop options
- spawn: `Burst` / `Rate` / `Per Unit` 

Particle Spawn  
- `Age`:  Emiter Looped Age - tyle żyją ile loop

Particle Update  
- `Generate Houdini Event` (jak zwykly event tylko z fn.)
- `Generate Location Event`  // ADD TO LEADER

Event Handler  
- `Event Handler Properties` // ADD TO FOLLOWER 
- `Recive Locaation Event` // ADD TO FOLLOWER

Render

# NAME SPACES  

NameSpace | R | W | Define | Share within 
--- | --- | --- | --- | --- 
`System` | Everyehere | System | persisted frame 2 frame | system
`Emitter` | Emiter, Particle | Emitter | persisted frame 2 frame | emitter inst
`Particles` | Particle | Particle |  persisted frame 2 frame |  per-particle values
`Engine` |  Everyehere  | - | runtime for Niagara itself | 
`Module` | Module | Modules | within a module |
`User` |  Everyehere  | - | in component or through blueprints | **[ALL OUT DATA]**
`NPC` |  Everyehere | - | in parameter collection | 

`Physics/Temp/Transient/Etc.` - “temporary”, they only have meaning for the script type that you are on. The values are scoped to that update, spawn or event and are not persisted in any way.  
`Particles.MyCompanyName.VariableName` - Anything you create will follow that same paradigm. However, you can create sub-namespaces within the supported ones. So. is a perfectly valid namespace to organize all your custom variables into.  
`Output` - Output namespace to signify that these are useful values for binding into other modules. convention: Output.Module.VariableName . is just a convention.    

# MAP ATTRIBUTES

#### Time:
`Emitter.Age`
`Engine.DeltaTime`
`Engine.InverseDeltaTime`
`Engine.Owner.TimeSinceRendered`
`Engine.RealTime`
`Emitter.System.Age`
`Emitter.System.TickCount`
`Emitter.Time`        
`Particles.Age`
`Particles.Lifetime`
`Particles.NormalizedAge`
`Module.DeltaTime`
`Module.LifeTime`
`Module.LoopParticlesLifetime`

#### Translation
`Particles.Owner.Position`
`Particles.Owner.Rotation`
`Particles.Owner.Scale`
`Particles.Position`
`Particles.Scale`
`Particles.SpriteAlignment`
`Particles.SpriteFaceing`
`Particles.SpriteRotation`
`Particles.SpriteSize`
`Particles.RibbonFaceing`
`Particles.RibbonLinkOrder`
`Particles.RibbonTwist`
`Particles.RibbonWidth`
`Particles.SpriteUVScale`
`Particles.SpriteSubimageIndex`

#### ID ?
`Engine.ExecutionCount`
`Engine.Owner.ExecutionState`
`Particles.ID`
`Particles.RibbonID`
`Particles.UniqueID`

#### v
`Engine.Owner.Velocity`
`Particles.Velocity`

# EXECUTION INDEX / POINT ID :
- Execution Index - GPU ?   - ArrayIndex != ExecIndex (you can verify this by writing out Particles.MyExecIndex)  
make a Niagara ID and assign the execution index to the ID index, and then set Particles.RibbonID in the Map with our new ID

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
*[Event handler]* is listening for event. 2  events! // FOLLOWER  

### POINT ANIM:

`@id` same for one particle   
`@life` Life set for first point    
`@time` arrival time // just normalize time before ezport!  check length from a to b and set time    
*[emiter update]* spawn form array playback    
*[particle spawn]* hanldle spawn particles  
*[particle update]* update pos from Harray  
