OBJ TO FBX: Rotate 90

# EXPORT H>UE4 resolutions
**Pix to Verts**  
4k = 16 777 216 pix  
**Vertex anim**   
2k - 200 frames -        - 20k poly  
4k - 150 frames - 4 sek - 111,8k poly  
4k - 300 frames - 8 sek - 55,9k poly  
4k - 360 frames - 10-15 sek - 46,6k poly  
4k - 500 frames - 16,6-20,8 sek - 33,5k poly  
**Flip books**  
4k tex = 256 frames x 256 pix  
4k tex =  64 frames x 512 pix  

# Source:  
  
### scan geo   
(cannot move high) (not quads) (bridged geo with other probrms than unfoald) ) (duplicated geo) (other typ of data) (inverted few faces) (swaped trix connection)
- Retopo Geometry is bloby on corner trix, could be fliped and is 30-100% less efficient in polycount hard to uv
  
### H low with uv's.   
(Generate from Imported or Procediural data.)  
- Make Mid -  creesed copy to get high  
- Conform with ray to match Hi.  
 
### Clean Zbrush High  
- Use Dynamesh  
- Retopo by hand  

# BAKE:

### ZBrush
Export All subtools to obj: Zpluginds>PrintHub>ExportAll // polygroups > (H: Prim Groups)
Export Fbx: Zplugins>FBX // Export poligroups as material > (H: shop_materialpath)

### Houdini
prim: `s@shop_materialpath` - to split mesh in paiter
prim: `s@name` = nazwa label
vert: `@N`  
point: v@rest v@Cd i@id @P  

### PAINTER/DESIGNER
low fbx, high: obj
(mesh id polygroups-(Primitive Groups))  
**bake by name:**  
name attribute of mesh  to name of .obj  
>> name high and low parts  
(Painter Match by mesh names (mesh ID))  
```a_high_doesnotmatter  
a_high_whatisafter   
b_high_suffix 
a_low  
b_low 
``` 

### Xn
only fbx support cage files


# FORMATS:   
### Mesh  
`*.obj` - no vertex color and 2-uvs standarised  
`*.fbx` -  
`*.gltf`-   
`*.bgeo.sc` - cache  

`*.ztl` - Tool>SaveAs. selected 3D object (including all its subtools, subdivisions, settings, 3D layers, etc.).  
`*.zpr` - Project `Ctrl+S` will save multiple ZTools at once.  
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
Progressive scan (no interlacing) / High Profile / 2 consecutive B frames /  Closed GOP. GOP of half the frame rate. / CABAC  /  Variable bitrate. No bitrate limit required, though we offer recommended bit rates below for reference /  Chroma subsampling: 4:2:0  
Recommended video bitrates for HDR uploads:
- 2160p (4k)	44-56 Mbps (24-30k)	66-85 Mbps (60k)  
Type	Audio Bitrate  
- Stereo	384 kbps  
- 5.1	512 kbps  

# PDG
name index frame state id   
$PDG_DIR >> is lookin to working dir in processor  
`@wedgeindex` // wedge individual index  
`@pdg_name` // PDG var  
`@pdg_output` // PDG var with sop path 
`@pdg_intput` // finals ?
Hda processor // create inputs ?   
