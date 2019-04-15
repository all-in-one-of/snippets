# Project

`$HIP/source/` - sources (read only)   
`$HIP/${HIPNAME}/$OS.fbx` - Export file   
`$HIP/${HIPNAME}/material/..`  - Substance&Material   
`$HIP/${HIPNAME}/material/bake_$OS/${HIPNAME}_$OS_$(CHANNEL).png` - Texture bake      
`$HIP/${HIPNAME}/export/vat_$OS/$OS.` - Export Vertex Anim      
`$HIP/${HIPNAME}/export/$OS_lo.obj ` - Export Low to bake  
`$HIP/${HIPNAME}/zbrush/$OS_hi.obj` - Export High to bake  
`$HIP/${HIPNAME}/export/$OS.csv`   
`$HIP/${HIPNAME}/cache_geo/$OS.obj` - cache static  
`$HIP/${HIPNAME}/cache_sim/$OS.$F.bgeo.sc` - cache sim  
```$HIP/${HIPNAME}/cache_pdg/$HIPNAME.$OS.`@wedgeindex`.$F.bgeo.sc``` - PDG local  
```F:/SIM/${HIPNAME}/$HIPNAME.$OS.`@wedgeindex`.$F.bgeo.sc``` - PDG for cache disc   



# Source:  
  
### 3dScan   
Flaws: Cannot move high / not quads / bridged geo with other probrms than unfoald / duplicated geo / other typ of data / inverted few faces / swaped trix connection.   
- Retopo Geometry is bloby on corner trix, could be fliped and is 30-100% less efficient in polycount hard to uv and select. 
- Make mid res with reduced details and errors. Dynamesh it. 
- (back and forh for frip edges)
- bake broken parts into 

### Houdini low with uv's.   
Generate from Imported or Procediural data.  / Curve toolset (loft with uv's ??)
- Make Mid -  using crease! 
- Conform with ray to match Hi.  
- scale *100
 
### Zbrush High  
- Use Dynamesh  
- Retopo by hand  
reordering subtools in ZBrush will also reorder them when exporting the FBX,

## Scale   
real world scale if possible  (Houdini 1 U = 1m) (Zbrush ?)

### Designer
- part by materials in one mesh. (Id's)


# BAKE:

### ZBrush
Export Zplugins
- obj (All subtools): >PrintHub // polygroups > (H: Prim Groups)  
- fbx: >FBX // Export poligroups as material > (H: `s@shop_materialpath`)   // subtools names should corespond in Substance (but didnt try) 

### Houdini
prim: `s@shop_materialpath` - to split mesh in partes / or do it by primitive Groups  
prim: `s@name` - label  
vert: `@N`    
point: `v@rest`, `v@Cd`, `i@id`, `@P`    


### PAINTER/DESIGNER  
**bake by name:**    
low: fbx from H    
- to get Substance groups files need to be in separate 'geometry' nodes named (Name_low)  
high: obj  from Z  (for evey subtool with name Name_high)  
- obj, one sub tool for substance: uncheck `Grp` before export  

```
a_high_doesnotmatter  
a_high_whatisafter   
b_high_suffix 
a_low  
b_low 
``` 
(Painter Match by mesh names (mesh ID)) 
(mesh id polygroups-(Primitive Groups))  

### Xn
only fbx support cage files 
Heightmap export plugins > image exporters > tiff > 16bits per chan
(DirectX vs OpenGl normal)    
(baked object have other orientation)   



## Collision  
## LOD's  

# PDG
name index frame state id   
`@wedgeindex` - wedge individual index   
`@pdg_name` - PDG var   
`@pdg_output` - PDG var with sop path  
`@pdg_input` - see ropgeometry TOP  
`@pdg_input.1` - to access 1item in partitions  
`@pdg_input.2` - to access 2item in partitions  
Hda processor // create inputs ?   
