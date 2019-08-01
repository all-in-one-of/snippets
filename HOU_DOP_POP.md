
# POP  
POPs: Vex based solver.  green inputs have wired into them POP microsolvers.
Multisolver is for POP and rigids.
***Velocitty*** -  go this far every second in units. (by default distance is divide per 24 frames).   
Apply it by forces or inheret v@v - create from motion by trail sop!   


```md
- OBJECT 
- PRE-SOLVE
- SOURCE 
```

#### *Input OBJECT*
- `popobject` - mandatory pop object

#### *Input PRE-SOLVE*  
- `pop vop`  

#### *Input SOURCE*  
- `pop source` - !!! mandatory (birth/birth from attribute) constant activation - for sec., impuls for frame.
- `fireworks`
- `popattract` - (to point or geometry)  
- `popdrag`  
- `popvop` - sam mozesz zrobic force, np ( vel +=  noise)  
- `popcurveforce` - podpinasz krzywa i leci  
- `popcolision` - (stick/ bounce)  
- `popgroup` -  
- `popforce` - jakies noizy Old thing   
- `popwind` - stop accumulating v on given speed  
- `popkill` - `if (@age>1) dead = 1;`  

# [POP Solver] 
### [Collision]:
### [Sleeping]:

# [POP Object] 
Bucket for particles 
Physical parameters: `Bounce`, `Friction`, `Temperature`
# [POP Source]  
source types: set to all points for points in.  
impulse count (per frame) / constant birth (for time) / life  
attribtes > velocity > inherent (default!) from param: v@v  
attribtes > velocity > for the first frame 
Emission Attribute - ATTRIBUTE TO EMIT PARTICLES (float 0-1)
# Sourcing 
(source obj) `debricesource` // for RBD ingeret vel   
(source obj) `fluidfource` // volume source from point   

# [POP Fluids]
`popfluid` PBD fluid make intersection - maintain Particle Separation (node from white water) Can make cohesion and basic surface tension (https://vimeo.com/295491505 Lewis Orton).   

- `Constrrain iteration` 20+  (50?)
- `Constrain stifnes` // up do sich particles. 
- `Viscosity` // up even to 1
- `Tensile Str.` // up to 0.01 even more to not break so easly.

# [POP Grains]
Are just proper collisions for pops   
`POP Grains` - set next after source   
- particle sep should be same as grain source  
- for test you can lower constrain itters  
Friction:  
- static treshold  
- scale kinetics (accelerate friction and stop to scatter on collision)  
Clumping: make stick particle toghether  
Break constraint treshold:  

#### Source ####
`Grain Source` [SOP] - export points with pscale  >> 
`POP Source` (DOP) emit from all points (if you are using constrains from geometry)
#### POP Solver ####
- itterations 10 
- max speed - can change speed scale to decrees forces  
https://vimeo.com/132847114  
# [POP Wrangler]
@dead = 1; // kill (pop solver > update > reap particles)


# Setups  

#### Condensation - Shelf tool 
 
***Adhesion parameter*** is creating force with collision geo. (meniscus {wklęsły i wypuły :]}) 
- `Strength Multiplier` parameter on the Geometry Wrangle (adhesion_force).    
- `Friction` parameter on the POP Object Control how slowly the liquid flows over the object make the liquid drip off the object quicker
- pop fluids parameters to set fluid.
--
- Limit Refinment iteration  at  (particle fluid surface)  
Source:  
- `add emision scale` - max value zmniejsz zeby zmniejszyc ilesc klatek w ktorych jest emisja ()  
- `fade` - how long emiting from one spot. (less, smaller ) (Wywill kernel - for not conecting so much) (ew. distance treshold) 
- `scatter` - po lewej wiekszy daje ci strumien, po prawej wiecje ptk daj droplety 
 (https://www.youtube.com/watch?v=yQoWgVuLXo8)    

#### White Water

(h17 core of new water solver in future maby with vellum).  
```
Constrain Iteration -  20 
Constrain Stiffness - 100 (stay toghether )
Viscosity - higher value to sticky durfaces 
Tensile Strengh - keep distance between particles 0.01 - larger make
```
https://vimeo.com/323269227 (Entagma)


