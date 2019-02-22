
Particle-Based Fluids are implemented in OpenCL and therefore also calculated on the graphics card. The Particle-Based Fluids Node can also be used outside the Ocean and Water tools for simpler fluids and can be combined with Vellum. Solver is hybrid and transfer a lot of data from particle to background grid but mostly working on volumes.

# Properties
```md
- OBJECT 
- PARTICLE VELOCITY
- VOLUME VELOCITY
- SOURCE 
```

#### *Input OBJECT*
- `Flip Object`

#### *Input PARTICLE VELOCITY* 
- `Pop Solver`   
- `Pop Curve force` (Illume Jeff I ) // input curve 
- `Sop Solver` // acces any sop (cmi) 

#### *Input PARTICLE VELOCITY*  

#### *Input VOLUME VELOCITY*  
- `gas field vop` // taki volume from sim  (Illume Jeff II )
#### *Input SOURCE*  
- `gas temp update`    
- `heatvoluem`  // can spread temperatue   // lave cool rate 
- `pop color` 
- `source volume` (initialize source flip) with SOP link to: `fluid source SOP`
 
# FLIP Solver   
### [Substeps]:
- timestep = (divide 1 frame to few)  
- substep = (add steps in 1 framie) Fluid dont need it exxeption are: fast moving fluid that collides with other objects and Surface tension. 


### [Particle Motion]:
- `Collision detection` Move Outside Collision is the fastest collision handling method and provides the smoothest splashes, however it is not as accurate with fast-moving collision geometry. It is also the only collision method that works with Volume Source based collisions. the Particle method only works when a collision is represented by an actual DOP object.  
- `default velocity scale` for Volume Source is 1.5, which will cause larger splashes by default, but for moving containers this should be set to 1.
#### Separation:  
#### Droplets:  
#### Vorticity: 
- preservation rate (how much vorticity should rename of end of second) (decay value) retain sworling motion.  


### [Volume Motion]:  
- smoothing 
#### Volume Limits:  
- **waterline** (semi open boundaries)(above opne, belowe close) it should be on water level.   
- **use boundary layer** - (adv waterline) (velocity volume - at volume boundaries) (surface volume control geo in boundary padding) if both not connected it will use warterline options. (Houdini 16 Masterclass)  
#### Collisions:  
- stick on collision [viscosity free solutions!: ]( simualte sth like (free slip condition) but inbverse)   
#### Viscosity: (lava)     
- **slip on colision** 0 to take velo from collision (Can't slip) Sticky / 1 to completly slide fluid on collider Slipy (can slip (tangentialy)) (fluid velo = no impact of collider tangential velocity). [Its oposie to: stick to colision]. (Houdini 16 Masterclass)
Measured in: (centi)Poise.

Substance | CentiPoise
--- | --- 
Water | 1
Honey | 3000 
Mustard | 50 000 
Peanut Butter | 150 000 
Sanitary Silicon | 5M - 10M

#### Density:   
- By default, the fluid has uniform density as set on the Physical tab of the FLIP Object. 
#### Air:  
- Enforce Air Incompressibility on the FLIP Solver. This feature prevents air pockets from collapsing
#### Divergence:  
- Positive values cause particles to spread out, and negative values cause them to clump together.
#### Surface Tension:   
- Createing the surfacepressure field. fight against gravity trying to put particles in to drop (bostly in places where curvature of shape is bigest). Crown Splash, Suction, Avoidance (Houdini 16 Masterclass). *In small scale it can be unstable !!*   


### [NarrowBand]:   

### [Distribution]:    
- for net renders


# NODES:
## Flip Object
- **Particle Separation** // overal scale   
- **grid scale** // higher for sharper // fat crona >> thinner splash  
- bounds
### [Initial Data]
Input type: *Surface sop, particle field, Narrow Band*  
### [Physical]
Physical behaviour : `Bounce`,`Friction`,`Temperature`,`Density`,`Viscosity` (if viscosity by attribute in solver is checked and there is point attribute at sop viscosity will be multiplayed)



# Collisions  
`static object` with volume collision.   
- Enabling Collision Separation on the FLIP Object and setting this value to the Particle Separation or smaller will create a higher-resolution collision field 
- Accurate velocities for moving collision objects are extremely important.
- {Deforming Object} shelf tool to set up deforming geometry as a FLIP collision object.

- SOP `Collision Source` SOP -  interpolate deforming geometry, calculate point velocities, and create VDB. Usually used in conjunction with a Static Object DOP.


# Sourcing
- SOP `fluid source` SOP  (for source volume  DOP) // attach this sop to geometry (change  [Initial Data] input to *Surface sop*)
in container settings: Source FLIP
in velocity volumes: you can add initial velo and noise (Add Velocity)
- SOP `pointes from volume` SOP (for source volume  DOP) // source from points (change[Initial Data] input to *particle field*)
- SOP `Oceane Source` (for flip object  DOP) (particles(points)+volume for: sop path and surface volume) //  (change [Initial Data] input to *narrow band*)
- SOP `FLIP Source` (for Volume Source DOP)- converts its input geometry into a volume that can be used to control simulations. For instance, the generated volume can be used to inject liquid into a FLIP simulation or act as a sink in a smoke simulation. 

# Setups  
**Crown Splash**
```
Flip tank with bounadary layer 

Flip solver: Velocity transfer Splashy >> Swirly  
// not as noisy and turb. (Houdini 16 Masterclass) and keep vorticity better
Enable surface tenssion 48 // high value less motion for 
FLIP object: - particle separation 0.03
grid scale // fat /thin 1.5
in self they reduce gravity 
substeps up!!
```
**Droplet**
```
surface tenssion 48000
```
**floating RDB:**   DOP>flipsolver>Volume Motion>solver change Feedback Scale from 0 to 1.   https://vimeo.com/116176349#at=158
```
merge: rigidbody solver + flip solver 
check density of object (mass)  
Substeps -  Max Substeps change from 2 to 1.  
check Particle Separation changed to 0.1  
```
```
bullet solver with rdb object is working as well
```
**Pyro > Fluid**  
https://vimeo.com/157944287 
```
Sim Pyro > Import > Points from volume 
Flip Object > change sop path to points 
// cration frame spec sim frame check
link resolution of flip with point separation 
```

## ###

You can stop the particles in a flip sim with i@stopped  
http://www.sidefx.com/docs/houdini/nodes/dop/flipsolver.html  
