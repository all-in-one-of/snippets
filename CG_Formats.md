
### VAT

4k pix = 16 777 216 points  
vertex anim: 33 550 points; 500frames (~16sek) = 4k tex   


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

### Substance 
`*.sbs` - Substance packsge edited within Substance Designer. 
`*.sbsar` - compiled/portable version that you can use in other software like Substance Painter.

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


BC - Block Compressions:

--- | Data | Pal | Palette 
--- | ---  | ---  | ---  
BC1 | RGB + A(1bit)| 4  |   
BC2 | RGB + A(4bit)| 4  | 
BC3 | RGBA | 4 + 8A | BC1 for the RGB part and BC4 for A col+Hmap
BC4 | R | 8 | height maps
BC5 | RG | 8  | 2xBC4
BC6 | RGBA(Float) | 8-16 | can natively store HDR
BC7 | RGB / RGBA | 4-16 | xtremely well on the gradient D3D11-more complex 


http://www.reedbeta.com/blog/understanding-bcn-texture-compression-formats  
https://www.fsdeveloper.com/wiki/index.php?title=DXT_compression_explained  

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
