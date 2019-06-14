
# VELLUM
Vellum XPBD is expansion of grain PBD - pos base dynamic. Ppoints + constraints   
Visualise evetyrhing by postprocess   
Paintem mozemy zmieniac lokalnie restlen np.  
v@v = ; - take speed directly. !
```
- geometry 
- constrain 
- collision
```
# [Vellum Solver] 
Constraint iteration + substeps   
Colision iterations are lower cause are cost expensive   
Smoothing error iters   

#### Forces 
Drag - if stuff in simulation have to much energy you can increse drag !!!!   
#### Advancde
Second order is more precisem, but canhav issues on colllsion, (bounce) if that turn on max accel   

[Vellum Object]
[Vellum Source]
Create frame can import obj everth fr. 


# CONSTRAINTS  

#### Hard pins:   
Is storet as geo point attrib  - not solving constr, update pos directly.   

mass = 0 hard const., ale masy nie animujemy    
To break hard constraint:  
`i@stopped = 0;`   // set to 0 to break constraint - like in pops  
`i@pintoanimation = 0;`  // if set to anim.  
 
#### Sofft pins:  
constr peimitives (pin stitch glue)  
