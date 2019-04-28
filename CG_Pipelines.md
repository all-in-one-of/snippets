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

prim: `s@shop_materialpath` - to split mesh in partes / or do it by primitive Groups   
prim: `s@name` - label   
prin: `i@class` -  
vert: `v@N`    
point: `v@rest`, `v@Cd`, `i@id`, `@P`   

(Houdini 1 U = 1m) (Zbrush ?) - scale *100  

# Source:  
  
### 3dScan   
- Supper highPoly make unable to move/scale geo.   
- Reduce from mid res with reduced details, get rid of bridges, unfolds, duplicate/inverted faces, Dynamesh it.   
- AutoReduce is not shape aware and less efficient(30%), hard to uv (fliped edges connections) and select edges.        
- Bake into mid res >> transfer geo    

### Procedural   
- Imported blueprints have different formats.
- Build geo from curves and points.  
- Make Mid -  using crease! 
- Conform with ray to match Hi.  

### Sculpt  
- Quick mid with creases to subd with smooth    
- Use Dynamesh on already smooth geo    (scale!)  
- Retopo by hand  

# Export:
- consistant texel   
- separate parts with alphas to second texture  
- orient uv - usefull for brushing in substance + directional mask   
- mirroring ?  
- rebake and rotate ?  

### ZBrush
Export Zplugins
- obj (All subtools): >PrintHub // polygroups > (H: Prim Groups)  
- fbx: >FBX // Export poligroups as material > (H: `s@shop_materialpath`)   // subtools names should corespond in Substance (but didnt try) 
- (reordering subtools in ZBrush will also reorder them when exporting the FBX)     

### Substance Designer  
- part by materials in one mesh. (Id's)  
- **bake by name:**    
`low`: fbx from H - to get Substance groups files need to be in separate 'geometry' nodes `a_low`, `b_low`  
`high`: obj  from Z  (for evey subtool with name Name_high) - obj, one sub tool for substance: uncheck `Grp` before export `a_high_doesnotmatter`, `a_high_whatisafter`, `b_high_suffix`    
     


### Painter
(Painter Match by mesh names (mesh ID))  
(mesh id polygroups-(Primitive Groups))   
(dont bake displacements)

### Xn
Default Normal OpenGl (+Y)   (G-invert in unreal) ( Designer use `innvert` )   
Cage - only fbx      
16bits - Heightmap export plugins > image exporters > tiff > 16bits per chan  

### Unreal
Default Normal DirectX (-Y)  
RGB - linear   
sRGB - 2.2 Gamma  (1/2.2=0.4545)   

# PDG
name index frame state id   
`@wedgeindex` - wedge individual index   
`@pdg_name` - PDG var   
`@pdg_output` - PDG var with sop path  
`@pdg_input` - see ropgeometry TOP  
`@pdg_input.1` - to access 1item in partitions  
`@pdg_input.2` - to access 2item in partitions  
Hda processor // create inputs ?   


# REF
- References   
   - Read it with human scale and relations (bigest to smallest details), read paterns.     
   - Dna   
   - Age   
- Sculpt  
   - Siluette  
   - Dont forget aboud mid freq.    
   - Make contrast comp with details placement.   

- Try to sculpt across the form (not with the flow).    
- work in HSV, Keep Valor in check.   

