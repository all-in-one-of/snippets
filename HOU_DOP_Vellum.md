# VELLUM
```
- geometry 
- constrain 
- collision
```
# [Vellum Solver] 


i@layer = layer shock on solver 

# [Vellum Solver drape]

welding frame - where it start to fuse  (maby work on frame 1 ?)  
forces - increse velocity damping and air drag if cloth move to much 

# Constraints
Most of behaviour    
Paintem mozemy zmieniac lokalnie restlen np.  
# [Vellum Cloth setup]
disiatance & bend constran  
`Mass` -   
`Thicknes` - on drape see resoult in postprocess spheres could by to big  depend on `scale`     
`Drag` -    
`Strech`   
- `Stiffnes` - default infinite (never be strachy) 
- `Damping Ratio` - lit more energy from sim  if too lively  (dont change) too much destory  
- `compression stiffnes` -(how much one point can shrink to other )  with low res help to remove jagginess zig zag  more detail higher ! oO    
- `plsticity` - will update rest pos.   
 - `treshold` - low so will enter new config eay and quick   
 - ... make softer over time of banding  
`Bend`
- `Stiffnes` - is soft if you want rigit make higher  / decrese to make softer  and bend more  

# Workflows  

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




