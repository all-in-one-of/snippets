
flipbook: file > export > ffmpegmp4 

### res:

4K (4K UHD) (2160p) 3840 x 2160   
4K (DCI) movie ind. 4096 × 2160 
full HD 1080p image is only a 1920x1080 



HDTV format (16:9) 1.7778
WideScreen format (1.85:1)  
CinemaScope (2.35:1.00) 


### Mesh  
`*.obj` - no vertex color and 2-uvs standarised, no attribs
`*.fbx` - 
`*.gltf`-    Create unwanted catalog in UE4, no Vert Color?  
`*.bgeo.sc` - cache  
`*.sim` - more expensive H cache (eg in output node in dop)  

`*.ztl` - Tool>SaveAs. selected 3D object (including all its subtools, subdivisions, settings, 3D layers, etc.).  
`*.zpr` - Project `Ctrl+S` will save multiple ZTools at once.  
`*.hda` - Houdini Digital Asse. Old ones: .otl
### transforms:
OBJ TO FBX: Rotate 90

### Substance 
`*.sbs` - Substance packsge edited within Substance Designer. 
`*.sbsar` - compiled/portable version that you can use in other software like Substance Painter.

### Images   

`linear space` - RGB   
`gamma space` - sRGB - 2.2 Gamma  (1/2.2=0.4545)     

`*.tiff` (adobe Tagged Image File Format) - save image fom photoshop, can constain additional metadata i.e. GeoTiff   
`*.tga` - only for UE  16/24/32 bits per pixel (24?)   
`*.exr` - OpenEXR is Light & Magic  high dynamic range raster file format, 
`*.sbs` - Substance Designer Document  
`*.sbsar` - Substance Archive  

### Compression
`LDR` - 8F  bits per channel    
`HDR` - 16F low precission     
`HDR` - 32F high precision   

### Unreal Compression:

Unreal | Compression | ---  | --- 
--- | ---  | ---  | --- 
Default  | DXT1/5 BC1/3 (DX11)| ---  | ---  | --- 
NormalMap | DXT5 BC5 | ---  | --- 
--- | BC7 | ---  | --- 
Grayscale | R8 | (R8 RGB8 sRGB) | --- 
Displacement | R8 |(8/16bit)  | --- 
Vector Displacement  | BGRA8| (RGBA8) | (Standard 8bits RGBA format.)
Mask | DXT1 | ---  | Linear Color
Alpha | BC4 (DX11)| ---  | Linear Color
HDR | RGB | RGBA Float | Linear Color
HDR Compressed | RGB BC6H (DX11) | ---  | Linear Color


#### Block Compressions: ####

--- | Data | Pal | Palette 
--- | ---  | ---  | ---  
BC1 | RGB + A(1bit)| 4  |   
BC2 | RGB + A(4bit)| 4  | 
BC3 | RGBA | 4 + 8A | BC1 for the RGB part and BC4 for A col+Hmap
BC4 | R | 8 | height maps
BC5 | RG | 8  | 2xBC4
BC6 | RGBA(Float) | 8-16 | can natively store HDR D3D11-more complex 
BC7 | RGB / RGBA | 4-16 | xtremely well on the gradient D3D11-more complex 

#### DirectX Compression: ####

--- | --- | --- 
--- | ---   | ---    
DXT1 | RGB + A(1bit)| 4BPP bits per pixel, and has a maximum color resolution of 16 bits (as old VGA adapters.)  6:1 
DXT3 | RGBA | Better use 5 alpha channel (only 4 bits)
DXT5 | RGBA | 8BPP  4:1 uses DXT1 for the color part, but adds another 4 bits per pixel of alpha. This gives you better transparency. 

# P4
`Accept Source` GEt clean file from repo, discarding your changes.  
`Accept Target` Accepts the file local, overwriting repo.  

# video
H.264 -  
ffmpg -  
https://github.com/Aeoll/FFmpegify  

Progressive scan (no interlacing) / High Profile / 2 consecutive B frames /  Closed GOP. GOP of half the frame rate. / CABAC  /  Variable bitrate. No bitrate limit required, though we offer recommended bit rates below for reference /  Chroma subsampling: 4:2:0 \ Recommended video bitrates for HDR uploads:
- 2160p (4k)	44-56 Mbps (24-30k)	66-85 Mbps (60k)  

Type	Audio Bitrate  
- Stereo	384 kbps  
- 5.1	512 kbps  

