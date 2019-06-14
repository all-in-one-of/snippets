
# [Vellum Solver]

# [Vellum Solver drape]
To create drape from patches.  
`welding frame` - where it start to fuse  (maby work on frame 1 ?)   
`forces` - increse velocity damping and air drag if cloth move to much  

# Constraints
`Distance Along Edges` - Keep Stifnes and Damping `Distance` (like spring)     
`Bend Across Trix` - Keep angle  `Rotation` (rotation spring)    
`Cloth` - Bend, Length
`Hair` - Bend, Length, Twist   
`String` - Bend, Length  
`Pin to Target` - Help    
`Attach to Geo` - Help   
`Stich` - Help (no łaczenie clohow)   
`Pressure` - filled with compresable (Air) `Volume` - Constraint  
`Tetrahedral Volume` - filled with uncompresable fluid (water) fwm   
`Weld Points` -    
`Glue`  -    
`Struts` - internal struts that conect opose sides, so sstretch body    stiff default 10 not stiff as much  100 stiffer 


# [Configure Cloth]
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
 
 
# [Configure baloon]
= cloth + pressure   
# [Configure soft body]
= cloth + struts    
# [Configure grain]



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

# [Detangle]
run in forloop with fedback.   
- rest position as previous position   
- pscale  

# [Post Process]
Spply Welds - Weld geometry that have cuts  and in therory should stick toghether   
Vissualise - !  
