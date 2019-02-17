
Particle-Based Fluids are implemented in OpenCL and therefore also calculated on the graphics card. The Particle-Based Fluids Node can also be used outside the Ocean and Water tools for simpler fluids and can be combined with Vellum

## Properties
```md
- OBJECT 
- PARTICLE VELOCITY
- VOLUME VELOCITY
- SOURCE 
```
## OBJECT
### Flip Object
Standard object
-  **Particle Separation** // overal scale 
- **grid scale** // higher for sharper // fat crona >> thinner splash

## FLIP Solver 

**Particle Motion:**  
`separation` / `droplet` / `vorticity`   

**Volume Motion:**  
volume limits:
- **waterline** (semi open boundaries)(above opne, belowe close) it should be on water level. 
- **use boundary layer** - (adv waterline) (velocity volume - at volume boundaries) (surface volume control geo in boundary padding) if both not connected it will use warterline options. (Houdini 16 Masterclass)

collisions:
- stick on collision [viscosity free solutions!: ]( simualte sth like (free slip condition) but inbverse) 

`Surface Tension` - createing the surfacepressure field. fight against gravity trying to put particles in to drop (bostly in places where curvature of shape is bigest). Crown Splash, Suction, Avoidance (Houdini 16 Masterclass). *In small scale it can be unstable !!*   

`Viscosity` - (lava)   
- **slip on colision** 0 to take velo from collision (Can't slip) Sticky / 1 to completly slide fluid on collider Slipy (can slip (tangentialy)) (fluid velo = no impact of collider tangential velocity). [Its oposie to: stick to colision]. (Houdini 16 Masterclass)


`Density`  
`Divergence` - However, you may want to adjust the particle spacing. Doing this with forces is difficult because the volume projection will undo your forces.  
`Air Incompressibility - Enforce ! By default, the air volume is not simulated and is treated entirely as a void.   

(0 plynne - 7000 guma)  
-timestep = podziel czas na czesci   
- substep - dodaj stepy w framie  

## Collisions

## Setups
**Crown Splash**
```
Flip tank with bounadary layer 

Flip solver: Velocity transfer Splashy >> Swirly  // not as noisy and turb. (Houdini 16 Masterclass)
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

## ###

You can stop the particles in a flip sim with i@stopped
http://www.sidefx.com/docs/houdini/nodes/dop/flipsolver.html
