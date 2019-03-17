
POPs: Vex based solver


# Properties
```md
- OBJECT 
- PRE-SOLVE
- SOURCE 
```

#### OBJECT Input  
- `popobject`   - base pop object

#### PRE-SOLVE Input    
- pop vop  

#### SOURCE Input    
- `pop source` !!! mandatory
(birth/birth from attribute)
- fireworks  
- popattract (to point or geometry)  
- popdrag  
- popvop // sam mozesz zrobic force, np ( vel +=  noise)  
  
- popcurveforce // podpinasz krzywa i leci  
- popcolision (stick/ bounce)  
- popgroup  
- popforce // jakies noizy Old thing   

## POP SOLVER:  
(behavior on collisions)


## SOURCE  
(source obj) `debricesource` // for RBD ingeret vel  
(source obj) `fluidfource` // volume source from point  

## POP Fluids:  
`popfluid` PBD fluid make intersection - maintain Particle Separation (node from white water) Can make cohesion and basic surface tension (https://vimeo.com/295491505 Lewis Orton).   
- `Constrrain iteration` 20+  (50?)
- `Constrain stifnes` // up do sich particles. 
- `Viscosity` // up even to 1
- `Tensile Str.` // up to 0.01 even more to not break so easly.

**Condensation** - Shelf tool 
- `Friction` parameter on the POP Object Control how slowly the liquid flows over the object make the liquid drip off the object quicker
- `Strength Multiplier` parameter on the Geometry Wrangle (adhesion_force).    

**Setup**  
(h17 core of new water solver in future maby with vellum).  
```
Constrain Iteration -  20 
Constrain Stiffness - 100 (stay toghether )
Viscosity - higher value to sticky durfaces 
Tensile Strengh - keep distance between particles 0.01 - larger make
```
https://vimeo.com/323269227 (Entagma)

## POP Grains:

