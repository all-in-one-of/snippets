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



# OPTIMISATION

## UE4

The only way to group meshes into one draw call is by using instanced meshes. Meshes using the same material/instance will still take one draw call each. However, they are drawn in an order that is grouped by material/instance, to reduce the number of render state changes, kinda like this:

3 meshes using the same material:
set shader, draw mesh #1, draw mesh #2, draw mesh #3

3 meshes using a different material each:
set shader #1, draw mesh #1, set shader #2, draw mesh #2, set shader #3, draw mesh #3




From Eric Ketchum https://answers.unrealengine.com/questions/127435/using-instanced-meshes-doesnt-reduce-draw-calls.html:

Instanced meshes will reduce the draw call overhead on the CPU but will not reduce the GPU cost. In fact the GPU time can increase when using instancing. Allow me to get a little technical for a moment:

This process has to do with the limitations of the CPU vs. GPU and how the API (OpenGL or DirectX) tries to maximize this limitation through batching. Instancing being a special case of batching. With a scene rendered with many small or simple objects each with only a few triangles, the performance is entirely CPU-bound by the API; the GPU has no ability to increase it. More precisely, "the processing time on the CPU for the draw call is greater than the amount of time the GPU takes to actually draw the mesh, so the GPU is starved." [Moeller, Real Time Rendering, 708]. So Batching attempts to allow the CPU to combine a number of objects into a single API call. In the case of Instancing it is the one mesh and the number of times you are drawing with a separate data structure for holding information about each separate mesh.

From a Rendering Engineerer:

"On meshes and material IDs, let me present a hypothetical situation to try to explain the situation more clearly. Let's say you have a mesh that has three materials: wood, chrome, and leather. Now let's say you place 100 of these meshes in your level. Ignoring other passes (shadow, depth only), this will result in 300 draw calls: one per-ID, per-instance. You can see this by looking at the section counts in the primitive stats window.

First thing to keep in mind: some draw calls are more expensive than others. The renderer sorts by material. So in this hypothetical scene we will draw the 100 wood elements first, the 100 chrome elements next, and the 100 leather elements last. Once we draw a wood element, the cost of drawing another wood element is not so high because we are rendering using the same shader and with mostly the same textures. But once we switch materials to draw the chrome we incur a high cost. That's why the renderer sorts by material.

Compare that situation to another scene where you have the same mesh instanced 100 times but each mesh has its own unique material. The scene is still 300 draw calls but the renderer incurs the material switch cost for every draw call. Instancing a mesh provides performance benefits even if the total number of draw calls does not reflect that"

To really see the performance boost in using Instances bring up the Stat UNIT and watch the DRAW versus GPU (CPU vGPU) and notice when you instance a mesh the CPU time remains fairly consistent depending on the additional information you are wanting to pass to each instance, while the GPU will increase. All of these numbers are still dependent on the size of your mesh and the type of material setup and the ultimate limitations of your CPU and GPU.

https://software.intel.com/en-us/gpa/graphics-frame-analyzer\  
Enable in U4: ToggleDrawEvents  
https://developer.nvidia.com/gameworksdownload  
