4k piz = 16 777 216 points  
vertex anim: 33 550 points; 500frames (~16sek) = 4k tex   

# Source:  
  
### 3dScan   
Flaws: Cannot move high / not quads / bridged geo with other probrms than unfoald / duplicated geo / other typ of data / inverted few faces / swaped trix connection.   
- Retopo Geometry is bloby on corner trix, could be fliped and is 30-100% less efficient in polycount hard to uv and select. 
- Make mid res with reduced details and errors. Dynamesh it. 
- (back and forh for frip edges)

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
`*.sim` - more expensive H cache (eg in output node in dop)  

`*.ztl` - Tool>SaveAs. selected 3D object (including all its subtools, subdivisions, settings, 3D layers, etc.).  
`*.zpr` - Project `Ctrl+S` will save multiple ZTools at once.  
`*.hda` - Houdini Digital Asse. Old ones: .otl
### transforms:
OBJ TO FBX: Rotate 90

### Images   
`*.tiff` (adobe reach format) - save image fom photoshop  
`*.tga` - only for UE  16/24/32 bits per pixel (24?)  

`*.sbs` - Substance Designer Document  
`*.sbsar` - Substance Archive  

### Compression
LDR - 8F  bits per channel
HDR low precission 16F   
HDR high precision 32F  

### Compression game:

DXT1 works on RGB data. DXT3 & DXT5 also provide an alpha channel (only 4 bits), however DXT5 is considered the better of the two. Technically DXT1 supports 1 bit of alpha,
BPTC is a 3:1 compression format, RGB, 8BPP
DXT1 is a 6:1 compression format, RGB, 4BPP
DXT5 is a 4:1 compression format, RGBA, 8BPP
RGTC1 is a 2:1 compression format, 1 channel only, 4BPP

DXT1 compresses color information into 4 bits per pixel, and has a maximum color resolution of 16 bits (as old VGA adapters.) DXT1 can also compress the special color "Black, transparent," so it can be used for certain kinds of pre-multiplied alpha. This is about as much as you can compress a texture and still retain some semblance of useful color information.
DXT5 uses DXT1 for the color part, but adds another 4 bits per pixel of alpha. This gives you better transparency. Also, with a bit of shader magic, you can use the "alpha" bits for something other than alpha, to get a bit higher quality than raw DXT1. Normal maps are a great example.

DXT compression (also known as S3TC) has been around for a long time (15 years at least!) For more modern graphics APIs, there are more compression formats, that improve on DXT in certain ways, such as using 24-bit or even more for the base color resolution (useful for HDR rendering) and encoding things like "edges" within compressed blocks of pixels.
But, those formats generally use slightly more storage to achieve higher quality, rather than trying to squeeze colors down to less than 4 bits per pixel.


Unreal | Compression | ---  | --- 
--- | ---  | ---  | --- 
Default  | DXT1/5 BC1/3 (DX11)| ---  | ---  | --- 
NormalMap | DXT5 BC5 | ---  | --- 
--- | BC7 | ---  | --- 
Grayscale | --- | (R8 RGB8 sRGB) | --- 
Displacement | --- |(8/16bit)  | --- 
Vector Displacement  | --- | (RGBA8) | (Standard 8bits RGBA format.)
Mask | --- | ---  | Linear Color
Alpha | BC4 (DX11)| ---  | Linear Color
HDR | RGB | ---  | Linear Color
HDR Compressed | RGB BC6H (DX11) | ---  | Linear Color

# P4
`Accept Source` GEt clean file from repo, discarding your changes.  
`Accept Target` Accepts the file local, overwriting repo.  

# video
H.264 -  
ffmpg -  
https://github.com/Aeoll/FFmpegify  

### Youtube: 
Progressive scan (no interlacing) / High Profile / 2 consecutive B frames /  Closed GOP. GOP of half the frame rate. / CABAC  /  Variable bitrate. No bitrate limit required, though we offer recommended bit rates below for reference /  Chroma subsampling: 4:2:0 \ Recommended video bitrates for HDR uploads:
- 2160p (4k)	44-56 Mbps (24-30k)	66-85 Mbps (60k)  

Type	Audio Bitrate  
- Stereo	384 kbps  
- 5.1	512 kbps  

### res:

4K (4K UHD) (2160p) 3840 x 2160   
4K (DCI) movie ind. 4096 × 2160 
full HD 1080p image is only a 1920x1080 



HDTV format (16:9) 1.7778
WideScreen format (1.85:1)  
CinemaScope (2.35:1.00) 
