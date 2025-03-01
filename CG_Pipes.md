# Project setup

**Project&Export:**  
`File.hip`  
`$HIP/source/` - sources (read only)   

**Exports:**  
`$HIP/${HIPNAME}/export/$OS.fbx` - Export file  
`$HIP/${HIPNAME}/export/$OS_lo.obj ` - Export Low to bake  
`$HIP/${HIPNAME}/zbrush/$OS_hi.obj` - Export High to bake   
`$HIP/${HIPNAME}/export/$OS.csv`   

`$HIP/${HIPNAME}/export/vat_$OS/$OS.bgeo.sc` - Export Vertex Anim     

**FileCache:**   
```$HIP/${HIPNAME}/cache_geo/$OS.obj``` - cache static  
```$HIP/${HIPNAME}/cache_`opname("..")`/$OS.obj``` - cache static   
```$HIP/${HIPNAME}/cache_sim/$OS.$F.bgeo.sc``` - cache sim  
```$HIP/${HIPNAME}/cache_`opname("..")`/$OS.$F.bgeo.sc``` - cache sim   
 
 
 `$HIP/${HIPNAME}/zbrush/..`  - Zbrush   
 
**Materials:**  
`$HIP/${HIPNAME}/material/..`  - Substance&Material    
`$HIP/${HIPNAME}/bake_$OS/${HIPNAME}_$OS_$(CHANNEL).png` - Texture bake      

**PDG:**  
```$HIP/${HIPNAME}/cache_pdg/$HIPNAME.$OS.`@wedgeindex`.$F.bgeo.sc``` - PDG local  
```F:/SIM/${HIPNAME}/$HIPNAME.$OS.`@wedgeindex`.$F.bgeo.sc``` - PDG for cache disc   

# Data Pipes

### Houdini   
(Houdini 1 U = 1m) (Zbrush ?) - scale *100  obj rotation ?    
`s@shop_materialpath` (prim) - to split mesh in partes / or do it by primitive Groups: Attr copy to `name`  
`s@name` (prim) - label    
`i@class` (prim) -    
`v@N` (vert) -   
`@P`, `v@rest`, `v@Cd`, `i@id`, `@Alpha` (point) -  
### Collisions 

- `UCX_*` - from houdini need to be in separated containers  named UCX_nameOfGeoContainer. - object level  (make container !!! and ROPnet > fbx)

### VAT    
Cloth, Liquid, Rigid, PointCloud
`4096` pix = `16 777 216` points   
`4096` pix - 33 550 points - 500frames (~16sek)     

Unreal:   
- [x] precise uvs on mesh   
- [x] world space nm on material   

### PivotPainter  
Houdini:  
#### object 
`s@name`(pts), `v@N`(pts)   
- pos: `uv2.x`, `uv2.y`, `uv1.x`    
- axies: `Cd.r`, `Cd.g`, `Cd.b`  
- Random: `uv1.y`  
- Mask: `Alpha`   

#### hierarchical 
`s@name`(pts), `v@N`(pts),  `[LeafGroup]` (prim), `[BranchGroup]` (prim) - on geometry     
- Leaf: `uv2.x`, `uv2.y`, `uv1.x`  
- Branch pivot: `Cd.r`, `Cd.g`, `Cd.b`  
- Branch angle: `Alpha`, `uv1.y`,  

Unreal:  
- [ ] create lightmap uv's
- [ ] connvert scene      
- rotating in unreal required updated normals. ( by vertShader: custom uvs 4,5)   

### Flow Maps
- Constant bias to make vector 2 ways (nm is ok and have biass) 
- import map as vector displacement  2 channels  

# Data transfer

### ZBrush
- obj: polygroups > (Houdini: Prim Groups)  Zplugins > PrintHub (AllSubtools)  
- fbx: poligroups > (Houdini: `s@shop_materialpath`) > FBX plugin | subtools names matching in Substance // didnt check       
- (reordering subtools in ZBrush will also reorder them when exporting the FBX)        

### Unreal

- landscape: dont use smooth brush it can make weight < 1  


# Bake

lo:
- consistant texel    
- orient uv - for brushing, directional mask   
- separate parts with alphas  
- mirroring ? rebake and rotate ?  

### Substance Designer  
- part by materials in one mesh. (mesh ID)       
- parts from Houdini: `s@shop_materialpath` (prim)    
- **bake by name:**    
`low`: fbx from H - to get Designer groups files need to be in separate 'geometry' nodes `a_low`, `b_low`  
`high`: obj  from Z  (for evey subtool with name Name_high) - obj, one sub tool for substance: uncheck `Grp` before export `a_high_doesnotmatter`, `a_high_whatisafter`, `b_high_suffix`    

### Painter
- `mesh id polygroups`= Houdini `Primitive Groups`     

### Xn (OpenGl +Y)     
- 16bits - Heightmap export plugins > image exporters > tiff > 16bits per chan    
- Cage - only fbx      
- separate scan by material (for xn: rename atrib  `s@shop_materialpath`(prim) > `name`)   

### Unreal (DirectX -Y) 


Megascans  (OpenGl +Y)  

# PDG
name index frame state id   
`@wedgeindex` - wedge individual index   
`@pdg_name` - PDG var   
`@pdg_output` - PDG var with sop path  
`@pdg_input` - see ropgeometry TOP  
`@pdg_input.1` - to access 1item in partitions  
`@pdg_input.2` - to access 2item in partitions  
Hda processor // create inputs ?   


