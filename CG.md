OBJ TO FBX: Rotate 90

# EXPORT H>UE4 resolutions
4k = 16 777 216 pix  
Vertex anim   
2k - 200 frames -        - 20k poly  
4k - 150 frames - 4 sek - 111,8k poly  
4k - 300 frames - 8 sek - 55,9k poly  
4k - 360 frames - 10-15 sek - 46,6k poly  
4k - 500 frames - 16,6-20,8 sek - 33,5k poly  
Flip books  
4k tex = 256 frames x 256 pix  
4k tex =  64 frames x 512 pix  

# MODELING
- Low with map > Hi > Ray Trace to conform 
- Low > High > retopo with base lo
- Scan > Reducer > // Geometry is bloby on corner trix, could be fliped and is 30-100% less efficient in polycount hard to uv

# BAKE:
### Painter 
- Bake by name // https://support.allegorithmic.com/documentation/spdoc/matching-by-name-127074308.html  
### Designer
- low obj/fbx  high: obj
- `vert color` `material Color` `File id`   (`mesh id` `polygroups`-(Primitive Groups)) 
### Xn
- only fbx support cage files
### Zbrush
- ... `polygroups`-(Primitive Groups)
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

Youtube:
Progressive scan (no interlacing)  
High Profile  
2 consecutive B frames  
Closed GOP. GOP of half the frame rate.  
CABAC  
Variable bitrate. No bitrate limit required, though we offer recommended bit rates below for reference  
Chroma subsampling: 4:2:0  

Recommended video bitrates for HDR uploads  
2160p (4k)	44-56 Mbps (24-30k)	66-85 Mbps (60k)  
Type	Audio Bitrate  

Stereo	384 kbps  
5.1	512 kbps  

# PROJECT  
File_001.hip  
/source  
/material  
/geometry - cache for middle
/bake  
/backup  

# H  
Attributes:  
VERTEX @N  
POINT: v@rest v@Cd i@id @P  
PRIM: s@name = nazwa label   // PRIMS  
@shop_materialpath  ??????  
