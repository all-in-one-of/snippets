

# Constraints
Stack constraints and applay them to point groups:  
Edit it in "velumConstrainsProperties" inside vellum solver   

`Distance` - Keep Length Along Edges by Stifnes and Damping // basic    
`Bend` (Rotation) - Keep angle Across Trix // basic   
`Cloth` = `Distance` + `Bend`  

`Hair` = `StretchShear` + `BendTwist` - Use polylines as input (its like distance bend and twist)    
`String`  = `Distance` + `Angle` - cheaper than hairs    

`Pressure` (Volume) - compresable (air) (enforce volume depending of stiffness)    
`Tetrahedral` (Volume) - uncompresable materials (most liquids) fwm (slower than pressure)          
`Struts` - stretch body (internal struts that conect opose sides)  stiffness (good for stftb. that does not stiff tu much)    

`Pin to Target` - pin to pos (Soft pin with stiffness - like magnes)    
`Attach to Geo` - look for closeest point and stick to geometry (target to geo to stic / up value of clostest point ) use in anim   
`Stich` - (connect cloths) or stich points in 2 groups that are far away and keep it apart    

`Glue`  -  Source and target geo and search distance to connect pts. (check nr constrains per point)   breaking treshold 
`Weld Points` - Tide fracture when pts are in same @P     Breaking level at stress level   


# [Vellum Solver]
- Geo - You can merge all geo and apply constraints by groups  
- Constrains 
- Colliion
You can write initial attribs to points of geometry like velocity  
You can enter solver and manage forces inside 
Not updating some animatied values of attribs ffrom constrains in solver  instead of it dive velum solver and place `VelumConstraintProperties` check constr in each frame! You can also set POP forces  
Add friction porint: `f@friction`  

# [Vellum Solver drape]
To create drape from patches.  
`welding frame` - where it start to fuse  (maby work on frame 1 ?)   
`forces` - increse velocity damping and air drag if cloth move to much  


### [Configure Cloth]
 For Drape   
`Mass` -   
`Thicknes` - on drape see resoult in postprocess spheres could by to big  depend on `scale`     
`Drag` -    
`Strech`   
- `Stiffnes` - default infinite (never be strachy) 
- `Damping Ratio` - lit more energy from sim  if too lively  (dont change) too much destory  
- `compression stiffnes` -(how much one point can shrink to other )  (decresse more smooth look ! dont enforce wrincles ) with low res help to remove jagginess lower param  
- `plsticity` - not use rather  

`Bend`
- `Stiffnes` - is soft if you want rigit make higher  / decrese to make softer  and bend more  (0.0001 to super soft)
- `plsticity` - will update rest pos.   
  - `treshold` - low so will enter new config eay and quick     
  - `rate` and  `hardening` higher - make hardne over time of banding    
 
 
### [Configure baloon]
= cloth Constraint + Pressure Constraint     
`VelumConstraintProperties` in solver   
- anim stretch on pressre   
- change volume by - rest length scale    

### [Configure soft body]
= cloth + struts     

### [Configure grain]
Increase substeps !!! 5 +   
`@isgrain = 1` -   
`mass` -   
`pscale` -   
`v` -   


## Drape

`Weld Points` - create constraint, glue drapes by points.  (breaking treshold)  
`planar patch from curve` - from curves   
`planar patch` - only simple shapes   
`planar pleat` - make patterns   

#### Mirroring cloth: 

`*_L*`  
`*_R*`  
 
`Name_RB` -   Right Back  
`Name_RF` -   Right Front  
`Name_LB` -   Left Back  
`Name_LF` -   Left Front  

## [Detangle]
run in forloop with fedback.   
- rest position as previous position   
- pscale  

## [Post Process]
Spply Welds - Weld geometry that have cuts  and in therory should stick toghether   
Vissualise - !   


## Tips of adjusting params (in solver):
- geometry > `mass`   
- geometry > `thickness`   
- stretch > `stiffness` - low is stretch high is stiff   
- stretch > `compression stiffness` (if compress how likley it stay compress)  more is more likley stay   
- bend > `stiffness` how much bend (how much resistent to unroll or bend)   
