
Particle-Based Fluids are implemented in OpenCL and therefore also calculated on the graphics card. The Particle-Based Fluids Node can also be used outside the Ocean and Water tools for simpler fluids and can be combined with Vellum. Solver is hybrid and transfer a lot of data from particle to background grid but mostly working on volumes.

# Properties
```md
- OBJECT 
- PARTICLE VELOCITY
- VOLUME VELOCITY
- SOURCE 
```

#### OBJECT Input
- `Flip Object`

#### PARTICLE VELOCITY Input  
- `Pop Solver`   
- `Pop Curve force` (Illume Jeff I ) // input curve 

#### PARTICLE VELOCITY Input  

#### VOLUME VELOCITY Input  
- gas field vop // taki volume from sim  (Illume Jeff II )
#### SOURCE Input  
- `gas temp update`    
- `heatvoluem`  // can spread temperatue   // lave cool rate 
- `pop color` 
- `source volume` ( initialize source flip) with SOP link to: `fluid source SOP`
 
# Flip Object  
### Standard object  
- **Particle Separation** // overal scale   
- **grid scale** // higher for sharper // fat crona >> thinner splash  
Here we can adjust physical beh.: `Bounce`,`Friction`,`Temperature`,`Density`,`Viscosity`  
# FLIP Solver   
### [Substeps]:
- timestep = podziel czas na czesci   
- substep = dodaj stepy w framie  

### [Particle Motion]:

#### Separation:  
#### Droplets:  
#### Vorticity: 
- preservation rate (how much vorticity should rename of end of second) (decay value) retain sworling motion.  

### [Volume Motion]:  

#### Volume Limits:  
- **waterline** (semi open boundaries)(above opne, belowe close) it should be on water level.   
- **use boundary layer** - (adv waterline) (velocity volume - at volume boundaries) (surface volume control geo in boundary padding) if both not connected it will use warterline options. (Houdini 16 Masterclass)  

#### Collisions:  
- stick on collision [viscosity free solutions!: ]( simualte sth like (free slip condition) but inbverse) //??(0 plynne - 7000 guma)  
  
#### Viscosity: - (lava)     
- **slip on colision** 0 to take velo from collision (Can't slip) Sticky / 1 to completly slide fluid on collider Slipy (can slip (tangentialy)) (fluid velo = no impact of collider tangential velocity). [Its oposie to: stick to colision]. (Houdini 16 Masterclass)

#### Density:   
By default, the fluid has uniform density as set on the Physical tab of the FLIP Object. 
#### Air:  

#### Divergence:  
Positive values cause particles to spread out, and negative values cause them to clump together.
#### Surface Tension:   
createing the surfacepressure field. fight against gravity trying to put particles in to drop (bostly in places where curvature of shape is bigest). Crown Splash, Suction, Avoidance (Houdini 16 Masterclass). *In small scale it can be unstable !!*   


### [NarrowBand]:   

### [Distribution]:    
for net renders

## Collisions  
- IN SOPS: **collision source** 
input this with vdb 
- IN DOPS Dop static object with volume collision. 

# Sourceing

-  IN SOPS: **fluid source SOP**  to the geometry  // 
in container settings: Source FLIP
in velocity volumes: you can add initial velo and noise (Add Velocity)


## Setups  
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
**RDB floating on FLIP:**   DOP>flipsolver>Volume Motion>solver change Feedback Scale from 0 to 1.   https://vimeo.com/116176349#at=158
```
merge: rigidbody solver + flip solver 
check density of object (mass)  
Substeps -  Max Substeps change from 2 to 1.  
check Particle Separation changed to 0.1  
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
