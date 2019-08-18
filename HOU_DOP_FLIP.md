
# FLIP
Fluid Implicit Particle - Based on Navier–Stokes equations, implemented in OpenCL (can combine with vellum) hybrid solver. All fluid data is stored in the particles (with pscale) and only particles need to persist frame to frame, However, the pressure projection step is done on a volume. 
www.sidefx.com/docs/houdini/nodes/dop/flipsolver.html   
http://www.danenglesson.com/images/portfolio/FLIP/rapport.pdf  

Size sensitive, use units as meters. 
Time sensitive !! I don't know how and why  



```md
- OBJECT 
- PARTICLE VELOCITY
- VOLUME VELOCITY
- SOURCE 
```

#### *Input OBJECT*
- `Flip Object` - mandatory

#### *Input PARTICLE VELOCITY* 
- `PopVop` / `popwrangle` - @viscosity= 
- `popforce` (can be merged)
- `Pop Curve force` (Illume Jeff I ) // input curve  

- `Pop Solver`   
- `Sop Solver` // acces any sop (cmi) 
#### *Input VOLUME VELOCITY*  
- `gas field vop` // taki volume from sim  (Illume Jeff II )
- `source volume` -  fluid source as velocity field 
  

#### *Input SOURCE*  
If nothing here will use source from op1 Flip Object  
- `Volume Source` (initialize source flip) (with SOP link to: `Flip Source` SOP)

- `heatvoluem`  // can spread temperatue   // lave cool rate 
- `gas temp update` 
- `pop color` 
---
# [FLIP Solver]   
### [Substeps]:
Time Scale !  
- timestep = (divide 1 frame to few)  
- substep = (add steps in 1 framie) Fluid dont need it exxeption are: fast moving fluid that collides with other objects and Surface tension. 


### [Particle Motion]:
`Collision detection` Move Outside Collision is the fastest collision handling method and provides the smoothest splashes, however it is not as accurate with fast-moving collision geometry. It is also the only collision method that works with Volume Source based collisions. the Particle method only works when a collision is represented by an actual DOP object.  
`Default velocity scale` for Volume Source is 1.5, which will cause larger splashes by default, but for moving containers this should be set to 1.
#### Reseed:
You’ll get an uneven distribution due to numerical error, especially with Reseed Particles turned off.  
#### Separation:  
#### Droplets:  
Tend to clamp toghether when partic drop below certain density turn dto droplets more like . After blend back to fluid: Merge/kill
#### Vorticity: 
Chaos and for for white water. 
- preservation rate (how much vorticity should rename of end of second) (decay value) retain sworling motion.  


### [Volume Motion]:  
- Velocity transfer `Splashy` >> `Swirly`  is not as noisy and turb. (Houdini 16 Masterclass) and keep vorticity better
- Smoothing 
#### Volume Limits:  
- **waterline** (semi open boundaries)(above opne, belowe close) it should be on water level.   
- **use boundary layer** - (adv waterline) (velocity volume - at volume boundaries) (surface volume control geo in boundary padding) if both not connected it will use warterline options. (Houdini 16 Masterclass)  
#### Collisions:  
- Stick on collision [viscosity free solutions!: ]( simualte sth like (free slip condition) but inbverse)   
#### Viscosity:    
Adhesive force which resist motion (lava).  Measured in: (centi)Poise.

Substance | CentiPoise
--- | --- 
Water | 1
Honey | 3000 
Mustard | 50 000 
Peanut Butter | 150 000 
Sanitary Silicon | 5M - 10M

- **Slip on colision** 0 to take velo from collision (Can't slip) Sticky / 1 to completly slide fluid on collider Slipy (can slip (tangentialy)) (fluid velo = no impact of collider tangential velocity). [Its oposie to: stick to colision]. (Houdini 16 Masterclass)


#### Density:   
By default, the fluid has uniform density as set on the Physical tab of the FLIP Object. 
#### Air:  
Enforce Air Incompressibility on the FLIP Solver. This feature prevents air pockets from collapsing
#### Divergence:  
Divergence is measure of imbalance. `Scale` component is using pressure field  
Incompresive fluid - have not "scale factor" still have : swirl , shear and translate factors

Value | .
--- | --- 
`-` | cause them to clump together.
`0` | for Incompresive fluid
`+` | cause particles to spread out

#### Surface Tension:   
- Propoerty of warte molecules that are attracted to eachother (cohesion). it is on surface, where molecules have space to stronger their bonds forming a tension that is absent in rest  Measured in: Pa*s.

Createing the surfacepressure field. Fight against gravity trying to put particles in to drop (bostly in places where curvature of shape is bigest). Crown Splash, Suction, Avoidance (Houdini 16 Masterclass). *In small scale it can be unstable*   
- Bigger value, liquid tend to min. surface area. Bluring shape. Create oposeing forces on large changind curvature. 
### [NarrowBand]:   
- work only with reseed  
### [Distribution]:    
- for net renders

---
# [Flip Object]
- **particle separation** Point separation (seed density) Increasing will lower the resolution 
- **particle radious scale**  - actual radious of every particle  
- **grid scale** // higher for sharper // fat crona >> thinner splash   
- Bounds
### [Initial Data]
Input type: *Surface sop, particle field, Narrow Band*  
### [Physical]
Physical behaviour : `Bounce`,`Friction`,`Temperature`,`Density`,`Viscosity` (if viscosity by attribute in solver is checked and there is point attribute at sop viscosity will be multiplayed)




---
# [FLIP Wrangler]
`i@stopped`   - You can stop the particles in a flip sim with 
`v@v` => vel
 
## Velocity
youcan cereate `velocity field` > `source volume`

# Sourcing
#### [Volume Source] - to last solver op  
Initialize as
- `Source FLIP` - default
- `Sink FLIP` - sink point  (size depend speed of sink)
---
# SOP Sourcing

#### [FLIP Source] (for Volume Source DOP)- converts its input geometry into a volume that can be used to control simulations. For instance, the generated volume can be used to inject liquid into a FLIP simulation or act as a sink in a smoke simulation.   
[volume operations] set behaviour (add/overide velo)      
[velocity volumes] source attributes - we can sample it from N or sth. 
[container settings] - velocity

#### [Flip Tank]

- `Points From Volume` (for source volume  DOP) // source from points (change[Initial Data] input to *particle field*)
-- `Oceane Source` (for flip object  DOP) (particles(points)+volume for: sop path and surface volume) //  (change [Initial Data] input to *narrow band*) Fluid Tank ?   

- `Limit Refinment iteration` - can remove glitches, use only in small scale (good for visc droplets ect...)    (particle fluid surface)  
---
# Populate cointiners 
Can work with flips 
`Pump from ` - create volume velocity (like)
---
# Collision 
 Deforming Object shelf tool to set up deforming geometry as a FLIP collision object.!! (docs note)  
 
 If using Volume Source based collisions, you must use the Move Outside Collision method for particle collisions, because the Particle method only works when a collision is represented by an actual DOP object.   
 Move Outside Collision is the fastest collision handling method and provides the smoothest splashes, however it is not as accurate with fast-moving collision geometry. It is also the only collision method that works with Volume Source based collisions.  
  
`static object` with collision mode to: volume sample {DeformingGeo shelf}   
- Enabling Collision Separation on the FLIP Object and setting this value to the Particle Separation or smaller will create a higher-resolution collision field 
- Accurate velocities for moving collision objects are extremely important.
- {Deforming Object} shelf tool to set up deforming geometry as a FLIP collision object.
- SOP `Collision Source` -  interpolate deforming geometry, calculate point velocities, and create VDB. Usually used in conjunction with a Static Object DOP.


 # Dop import
 -`Particle Fluid Surface` - limit refinment if unstable. / Change surfacing > surface output > from surfacepolygons to SUrface VDB !!
For emitting large numbers of particles, the Volume Source DOP can be much faster than the Particle Fluid Emitter DOP.

---
# Setups  
**Crown Splash**
```
Flip tank with bounadary layer 
Velocity transfer Splashy >> Swirly  
Surface tenssion 48 // high value less motion for 
Grid scale // fat /thin 1.5
In self they reduce gravity 
Substeps up!!
```
**Droplet**

- if small flip is unstable if smaller increase substeps minim 5 -6 
- Surface tenssion 48000
- grid scale tez wpływa 
- reduce gravity for slow moving slow scale 

**Suction**
- op2 antigravity (opose gravity around object)
- op3 suctionforce. strength + gradient on distance sometimes you need to keyframe it  
- collision source on geometry (velocity, volume out) + interior exterior distance for gradient

**floating RDB:**   DOP>flipsolver>Volume Motion>solver change Feedback Scale from 0 to 1.   https://vimeo.com/116176349#at=158
```
Merge: rigidbody solver + flip solver 
Check density of object (mass)    
Bullet solver with rdb object is working as well
```
**Pyro > Fluid**  
https://vimeo.com/157944287  
```
Sim Pyro > Import > Points from volume 
Flip Object > change sop path to points 
Cration frame spec sim frame check
```

**Pyro > Fluid**
https://vimeo.com/296410457  

**Fluid Follow Curve**  
https://forums.odforce.net/topic/31596-fluid-follow-curve/   

**Mix Colors**
https://youtu.be/DWxcfZMsZW8  
