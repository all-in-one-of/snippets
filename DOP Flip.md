# FLIP SOLVER:
Particle-Based Fluids are implemented in OpenCL and therefore also calculated on the graphics card. The Particle-Based Fluids Node can also be used outside the Ocean and Water tools for simpler fluids and can be combined with Vellum

## Properties
```md
- OBJECT 
- PARTICLE VELOCITY
- VOLUME VELOCITY
- SOURCE 
```

**[PARTICLE MOTION]**  
`separation` / `droplet` / `vorticity`   

**[VOLUME MOTION]**  
`Surface Tension` - createing the surfacepressure field. fight against gravity trying to put particles in drop. Crown Splash, Suction, Avoidance  
`Density`  
`Divergence` - However, you may want to adjust the particle spacing. Doing this with forces is difficult because the volume projection will undo your forces.  
`Viscosity` - lepkość (lava) (    - slip colision to 1 completly slide fluid on collider  (stick to colision) // jest tesz w collision stick on collision (free sleep condition  in viscosity opposite: control no sleep colliision)) (0 plynne - 7000 guma) 
`Air Incompressibility - Enforce ! By default, the air volume is not simulated and is treated entirely as a void.   


## Solver 
-timestep = podziel czas na czesci   
- substep - dodaj stepy w framie  

## Collisions

## Setups


RDB floating on FLIP:   DOP>flipsolver>Volume Motion>solver change Feedback Scale from 0 to 1.   https://vimeo.com/116176349#at=158
```
merge: rigidbody solver + flip solver 
check density of object (mass)  
Substeps -  Max Substeps change from 2 to 1.  
check Particle Separation changed to 0.1  
```

## ###

You can stop the particles in a flip sim with i@stopped
http://www.sidefx.com/docs/houdini/nodes/dop/flipsolver.html
