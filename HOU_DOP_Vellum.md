# VELLUM
Vellum is expansion of grain PBD - pos base dynamic. Ppoints + constraints   
Visualise evetyrhing by postprocess   
Paintem mozemy zmieniac lokalnie restlen np.  

```
- geometry 
- constrain 
- collision
```
# [Vellum Solver] 
COnstraint iteration + suubstep  

# [Vellum Solver drape]

welding frame - where it start to fuse  (maby work on frame 1 ?)  
forces - increse velocity damping and air drag if cloth move to much 

# Constraints
`Distance Along Edges` - Keep Stifnes and Damping `Distance` (like spring)     
`Bend Across Trix` - Keep angle  `Rotation` (rotation spring)    
`Cloth` -   
`Hair` - Bend, Length,Twist   
`String`- Bend, - Length  
`Pin to Target` - Help    
`Attach to Geo` - Help   
`Stich` - Help (no łaczenie clohow)   
`Pressure` - filled with compresable (Air) `Volume` - Constraint  
`Tetrahedral Volume` - filled with uncompresable fluid (water) fwm   
`Weld Points` -    
`Glue`  -    
`Struts` - internal struts that conect opose sides, so sstretch body    

# [baloon]
= cloth + pressure   
# [soft body]
= cloth + struts    
# [grain]


# [Vellum Cloth setup]
**disiatance** & **bend** constrants    
`Mass` -   
`Thicknes` - on drape see resoult in postprocess spheres could by to big  depend on `scale`     
`Drag` -    
`Strech`   
- `Stiffnes` - default infinite (never be strachy) 
- `Damping Ratio` - lit more energy from sim  if too lively  (dont change) too much destory  
- `compression stiffnes` -(how much one point can shrink to other )  (decresse more smooth look ! dont enforce wrincles ) with low res help to remove jagginess lower param  
- `plsticity` - not use rather  

`Bend`
- `Stiffnes` - is soft if you want rigit make higher  / decrese to make softer  and bend more  
- `plsticity` - will update rest pos.   
  - `treshold` - low so will enter new config eay and quick     
  - `rate` and  `hardening` higher - make hardne over time of banding    
 
# Workflows  
## VEX

i@layer = layer shock on solver  

## Cloth 
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




