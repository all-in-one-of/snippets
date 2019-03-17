

# BAKE:

### ZBrush
Export Zplugins
- Obj (All subtools): >PrintHub // polygroups > (H: Prim Groups)  
- Fbx: >FBX // Export poligroups as material > (H: `s@shop_materialpath`)  
subtools > names 
1) After save as zBrush renames 1 subb tool 
2) `_` came as `-` so but watch cause zBrush rename it `Alt`+`Shift`+`_`

### Houdini
prim: `s@shop_materialpath` - to split mesh in paiter  
prim: `s@name` - label  
vert: `@N`    
point: `v@rest`, `v@Cd`, `i@id`, `@P`    

low: fbx

### PAINTER/DESIGNER  
low fbx, high: obj   
   
**bake by name:**    
name attribute of mesh  to name of .obj    
name high(mesh/parts) and low (parts) 
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

(DirectX vs OpenGl normal)    
(relation high to low baking)  
(baked object have other orientation)   


## Source:  
  
### 3dScan   
Flaws: Cannot move high / not quads / bridged geo with other probrms than unfoald / duplicated geo / other typ of data / inverted few faces / swaped trix connection.   
- Retopo Geometry is bloby on corner trix, could be fliped and is 30-100% less efficient in polycount hard to uv  
  
### Houdini low with uv's.   
Generate from Imported or Procediural data.  
- Make Mid -  creesed copy to get high  
- Conform with ray to match Hi.  
 
### Zbrush High  
- Use Dynamesh  
- Retopo by hand  
reordering subtools in ZBrush will also reorder them when exporting the FBX,

## Scale   
real world scale if possible  (Houdini 1 U = 1m) (Zbrush ?)

## Collision  

## LOD's  


# PDG
name index frame state id   
$PDG_DIR >> is lookin to working dir in processor  
`@wedgeindex` // wedge individual index  
`@pdg_name` // PDG var  
`@pdg_output` // PDG var with sop path 
`@pdg_intput` // finals ?
Hda processor // create inputs ?   


# FORMATS:   
### Mesh  
`*.obj` - no vertex color and 2-uvs standarised, no attribs
`*.fbx` -  
`*.gltf`-   
`*.bgeo.sc` - cache  

`*.ztl` - Tool>SaveAs. selected 3D object (including all its subtools, subdivisions, settings, 3D layers, etc.).  
`*.zpr` - Project `Ctrl+S` will save multiple ZTools at once.  

### transforms:
OBJ TO FBX: Rotate 90

### Images   
`*.tiff` (adobe reach format) - save image fom photoshop  
`*.tga` - only for UE  16/24/32 bits per pixel (24?)  

`*.sbs` - Substance Designer Document  
`*.sbsar` - Substance Archive  

LDR - 8F  bits per channel
HDR low precission 16F   
HDR high precision 32F  

### video
H.264 -  
ffmpg -  

### Youtube: 
Progressive scan (no interlacing) / High Profile / 2 consecutive B frames /  Closed GOP. GOP of half the frame rate. / CABAC  /  Variable bitrate. No bitrate limit required, though we offer recommended bit rates below for reference /  Chroma subsampling: 4:2:0 \ Recommended video bitrates for HDR uploads:
- 2160p (4k)	44-56 Mbps (24-30k)	66-85 Mbps (60k)  

Type	Audio Bitrate  
- Stereo	384 kbps  
- 5.1	512 kbps  
