
POPs: Vex based solver


# Properties
```md
- OBJECT 
- PRE-SOLVE ??
- SOURCE 
```

#### OBJECT Input  
- popobject  

#### PRE-SOLVE Input    
- pop vop  

#### SOURCE Input    
- fireworks  
- popattract (to point or geometry)  
- popdrag  
- popvop // sam mozesz zrobic force, np ( vel +=  noise)  
  
- popcurveforce // podpinasz krzywa i leci  
- popcolision (stick/ bounce)  
- popgroup  
- popforce // jakies noizy CHUJOWE NIE UZYWAC   

## POP FLUIDS:  
popfluid PBD fluid make intersection in pops (node from white water) (h17 core of new water solver in future maby with vellum). 
```
Constrain Iteration -  20 
Constrain Stiffness - 100 (stay toghether )
Viscosity - higher value to sticky durfaces 
Tensile Strengh - keep distance between particles 0.01 - larger make
```
The difference between traditional SPH and PBD fluid is, SPH uses a kernel to “smooth out” essential attributes around every particle, whose neighbors are within the smoothing radius, so it tends to get unstable when nearby density is inconsistent and requires lots of substeps to solve the problem, very costly. PBD fluid (which contains parts of the XSPH) tries to solve this problem by bringing the pressure solving stage(where the density problem happens) into the PBD framework, which uses constraints to solve problems (constraints avoids). Basically, a new type of constraint which is based on the positions of each particle, rather than a smoothing kernel, is introduced to help to get a more consistent density with iterations(by updating positions directly within each iteration, not accumulating pressure throughout all the substeps and then apply forces).
[dont use, old popinteract ,  particlefluid solver   old and slow - SPH fluid ased on particles = unstable when dens is inconsiostant req substep  - slow and unstable !!!!!!!!!!!!!!]

## SOURCE
(source obj) debricesource // for RBD ingeret vel
(source obj) fluidfource // volume source from point
