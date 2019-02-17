# FLIP SOLVER:

```md
- OBJECT 
- PARTICLE VELOCITY
- VOLUME VELOCITY
- SOURCE 
```

**[PARTICLE MOTION]**  
`separation` / `droplet` / `vorticity`   

**[VOLUME MOTION]**  
`Surface Tension` - createing the surfacepressure field. fight against gravity trying to put particles in drop. `Crown Splash`,`Suction`,`Avoidance`  
`Density`  
`Divergence` - However, you may want to adjust the particle spacing. Doing this with forces is difficult because the volume projection will undo your forces.  
`Viscosity` - lepkość (lava) (    - slip colision to 1 completly slide fluid on collider  (stick to colision) // jest tesz w collision stick on collision (free sleep condition  in viscosity opposite: control no sleep colliision))  
`Air Incompressibility - Enforce ! By default, the air volume is not simulated and is treated entirely as a void.   







http://www.sidefx.com/docs/houdini/nodes/dop/flipsolver.html
