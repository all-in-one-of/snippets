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
- Lo obj/fbx  Hi: obj
- vert color / material Color /  mesh id / polygroups  / File id ??  
### Xn
- only fbx support cage files
# FORMATS:   
### Mesh  
`obj` - no vertex color  
`fbx` -  
`gltf`-   
`bgeo.sc` - cache  
  
### Images   
`tiff` (adobe reach format) - save image fom photoshop  
`tga` - only for UE  

bits per channel 8 << (16/32 high ress)(edited)  
LDR - 8F  
HDR low precission 16F   
HDR high precision 32F  

### video
H.264 -  
ffmpg -  

# OPTIMISATION

https://software.intel.com/en-us/gpa/graphics-frame-analyzer\  
Enable in U4: ToggleDrawEvents  
https://developer.nvidia.com/gameworksdownload  
