### Data types  

Use This Intrinsic Type    To Define Shader Variable: 
`Buffer`    Buffer, which contains one or more scalars  
`Scalar`    One-component scalar  
`Vector`, `Matrix`    Multiple-component vector or matrix  
`Sampler`, `Shader`, `Texture `   Sampler, shader, or texture object  
`Struct`, `User Defined`    Custom structure or typedef  


`bool` true or false  
`int` 32-bi integer  - int Foo[3]; / int Foo[3] = {1,2,3};  
`half` 16bit integer  
`float` 32bit float  - float Foo = 3.1f;  
`double` 64bit double  
`float3` vectorTest  
`float` vectorTest[3]  
`vector` vectorTest  
`float2` vectorTest    
`bool3` vectorTest    
`float3x3`: a 3×3 matrix, type float  
`float2x2`: a 2×2 matrix, type float  


### Var

`float4 color;`   
`uniform float4 position : SV_POSITION;`    
`const float4 lightDirection = {0,0,1};`  


### Vertex Shader Semantics:

Input	Description	Type  
`BINORMAL[n]`	Binormal	float4  
`BLENDINDICES[n]`	Blend indices	uint    
`BLENDWEIGHT[n]`	Blend weights	float    
`COLOR[n]`	Diffuse and specular color	float4  / Diffuse or specular color	float4  
`NORMAL[n]`	Normal vector	float4  
`POSITION[n]`	Vertex position in object space.	float4  / Position of a vertex in homogenous space. Compute position in screen-space by dividing (x,y,z) by w. Every vertex shader must write out a parameter with this semantic.	float4  
`POSITIONT`	Transformed vertex position.	float4  
`PSIZE[n]`	Point size	float   
`TANGENT[n]`	Tangent	float4  
`TEXCOORD[n]`	Texture coordinates	float4  
`Output`	Description	Type  
`FOG`	Vertex fog	float  
`TESSFACTOR[n]`	Tessellation factor	float  
`TEXCOORD[n]`	Texture coordinates	float4  

### Pixel Shader Semantics:
`COLOR[n]`	Diffuse or specular color.	float4  
`TEXCOORD[n]`	Texture coordinates	float4  
`SV_IsFrontFace`	Floating-point scalar that indicates a back-facing primitive. A negative value faces backwards, while a positive value faces the camera. float  
`SV_Position`	The pixel location (x,y) in screen space. float2  
`Output`	Description	Type   
`COLOR[n]`	Output color	float4  
`DEPTH[n]`	Output depth	float  

All system-values begin with an SV_ prefix,  
 `SV_POSITION`, which is interpreted by the rasterizer stage can be specified as an input to a vertex shader as well as an output. 
 Pixel shaders can only write to parameters with the SV_Depth and SV_Target system-value semantics.  
 `SV_VertexID`, `SV_InstanceID`, `SV_IsFrontFace` can only be input into the first active shader   
 `SV_Target[n]`, where 0 <= n <= 7	The output value that will be stored in a render target. The index indicates which of the 8 possibly bound render targets to write to. The value is available to all shaders.  
`SV_Depth`  



http://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm   
### Key Words

`return [value];`  
`continue;`   
- Stop executing the current loop (do, for, while)  
- update the loop conditions  
- begin executing from the top of the loop  

`discard;`  
- Do not output the result of the current pixel   

`break;`  
- Exit the surrounding loop (do, for, while).

http://iquilezles.org/www/index.htm   
https://www.bouncepatch.com/hlsl.html  
https://www.ronja-tutorials.com/2018/03/20/hlsl-basics.html  
http://www.catalinzima.com/xna/tutorials/crash-course-in-hlsl/  
http://rbwhitaker.wikidot.com/hlsl-tutorials
