# Project setup

**Project&Export:**  
`File.hip`  
`$HIP/source/` - sources (read only)   
`$HIP/${HIPNAME}/$OS.fbx` - Export file  

**Materials:**  
`$HIP/${HIPNAME}/material/..`  - Substance&Material   
`$HIP/${HIPNAME}/bake_$OS/${HIPNAME}_$OS_$(CHANNEL).png` - Texture bake    
`$HIP/${HIPNAME}/zbrush/$OS_hi.obj` - Export High to bake 
`$HIP/${HIPNAME}/export/$OS_lo.obj ` - Export Low to bake  

**Anim&data:**  
`$HIP/${HIPNAME}/export/vat_$OS/$OS.bgeo.sc` - Export Vertex Anim     
`$HIP/${HIPNAME}/export/$OS.csv`   

**Cache:**   
```$HIP/${HIPNAME}/cache_geo/$OS.obj``` - cache static  
```$HIP/${HIPNAME}/cache_`opname("..")`/$OS.obj``` - cache static  
```$HIP/${HIPNAME}/cache_sim/$OS.$F.bgeo.sc``` - cache sim  

**PDG:**  
```$HIP/${HIPNAME}/cache_pdg/$HIPNAME.$OS.`@wedgeindex`.$F.bgeo.sc``` - PDG local  
```F:/SIM/${HIPNAME}/$HIPNAME.$OS.`@wedgeindex`.$F.bgeo.sc``` - PDG for cache disc   

# Data Pipes

### Houdini   
(Houdini 1 U = 1m) (Zbrush ?) - scale *100  obj rotation ?    

`s@shop_materialpath` (prim) - to split mesh in partes / or do it by primitive Groups    
`s@name` (prim) - label    
`i@class` (prim) -    
`v@N` (vert) -   
`v@rest`, `v@Cd`, `i@id`, `@P` (point) -  


### VAT    
`4096` pix = `16 777 216` points   
`4096` pix - 33 550 points - 500frames (~16sek)     
`8192`    

Unreal:   
- [x] precise uvs on mesh   
- [x] world space nm on material   

### PivotPainter  
Houdini:  
- `s@name`(pts), `v@N`(pts) -  required  
- normals must b ubdated by: customUv (4,5)  
Unreal:  
- [ ] connvert scene      

# Data transfer

### ZBrush
- obj: polygroups > (Houdini: Prim Groups)  Zplugins > PrintHub (AllSubtools)  
- fbx: poligroups > (Houdini: `s@shop_materialpath`) > FBX plugin | subtools names matching in Substance // didnt check       
- (reordering subtools in ZBrush will also reorder them when exporting the FBX)        

### Unreal
 
- `UCX_*` - from houdini need to be in separated containers  named UCX_nameOfGeoContainer. If you have more parts need to separate to convex shapes and create empty containers with next _nameOfGeoContainer_x ... according to the count of colision parts    
- landscape: dont use smooth brush it can make weight < 1  


# Bake

lo:
- consistant texel    
- orient uv - for brushing, directional mask   
- separate parts with alphas  
- mirroring ? rebake and rotate ?  

### Substance Designer  
- part by materials in one mesh. (mesh ID)      
- **bake by name:**    
`low`: fbx from H - to get Substance groups files need to be in separate 'geometry' nodes `a_low`, `b_low`  
`high`: obj  from Z  (for evey subtool with name Name_high) - obj, one sub tool for substance: uncheck `Grp` before export `a_high_doesnotmatter`, `a_high_whatisafter`, `b_high_suffix`    

### Painter
- `mesh id polygroups`= Houdini `Primitive Groups`     

### Xn (OpenGl +Y)     
- 16bits - Heightmap export plugins > image exporters > tiff > 16bits per chan    
- Cage - only fbx      
- separate scan by material (for xn: rename atrib  `s@shop_materialpath`(prim) > `name`)   

### Unreal (DirectX -Y) 




# PDG
name index frame state id   
`@wedgeindex` - wedge individual index   
`@pdg_name` - PDG var   
`@pdg_output` - PDG var with sop path  
`@pdg_input` - see ropgeometry TOP  
`@pdg_input.1` - to access 1item in partitions  
`@pdg_input.2` - to access 2item in partitions  
Hda processor // create inputs ?   


