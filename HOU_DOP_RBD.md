- spheres collision over convex !!!!!!
- objects is grey plug
- data is green plug

RigidBodySolver vs RBD vs staticSolver  

- This solver is a union of two different rigid body engines, the RBD engine and the Bullet engine. The RBD engine uses volumes and is useful for complicated, deforming, stacked, geometry. The Bullet engine offers simpler collision shapes and is suitable for fast, large-scale simulations.
- RBD Solver is unable to enforce glue constraints between RBD Objects and Static Objects. You can work around this limitation by using constrained RBD Objects (perhaps with some RBD Pin Constraint DOPs) instead of a Static Object.
```
substeps: 
- to wiev subframes: - in global anim options  (global subs?) And Time is float turn off
- solver substeps (expensive when stacking obj)
- constrain substeps
```

# Solvers:   

```
- OBJECT
- PRE-SOLVE
- POST-SOLVE
```
apply pop forces in RBD in dop: plug pop forces into middle input  
### Static solver  

### Rigid solver 
use rigidbodysolver not bullet solver
#### rdb   

#### bullet
bullet likes pieces between 0.1 and 100 if you need smaller pieces, scale up and boost gravity proportionally  

### Multi Solver  
- multisolver is for pops (and rigid body)  






## Physical parms
`rotational stifness` // how much object will spin (how much object inherites rotation when hit by another object), 0 - means no rotation  
`bounce` // how much energy conservation there is when two objects collide, this is multiplication between the two objects (e.g. sphere and the ground)  
`friction` // how difficult is to move object from rest. 0 - no resistance at all  
`dynamic friction` // multiplier for objects that are already moving  


# RDB Objects:  

### static object 
moze byc jako kolizyjna ruchoma geometria w dopach (Simulating a Splashdown in Houdini - Escape Studios Free Tutorial)  
if its plane turn off volume based collision
**Vdb collision source:**
- mode: collision intersect to volume source 
- proxy volume: vdb path

### rdb object  
Also use for collision in flips  flips  (FLIP Fluids https://vimeo.com/116176349)
- increes density 


### rdb packed object  
- rotation for packed RDB :  dop angular momentum ? ??? or use POP torque !

# Constrains:

```cpp
- Unpack
- Adjectconnectedpieces 
- Primwrangle:
s@constraint_name="YoName";
s@constraint_type="position";

```
# Collision

COLLISION:
```cpp
- Volume collisions support
- Sphere collision for bullet ! Super fast  // on object use 'compound' collision  /// + BAKE ODE in SOP 
- Convex decompositon // can be slower than spheres
```

#  magia jakaś: 

STATES:  Key for states: Na spakowanegj geo przed solverem: //active = solve //  deforming: Anim > Pack  // animated: Pack > Anim  
```cpp

i@active=0;  
i@deforming=0; 
i@animated=0;  ```
` set i@active=0 after packed primitives in SOP's
in dopnet create multiple solver
connect sop solver
in sop solver make group (box) selection of the geometry
animate the selection
attrib wrangle on the group to change i@active to 1`
```
Key frame active  // node
Physical params  // Set Attributes in DOPs
Apply Data  // apply attributes in DOPs
```

