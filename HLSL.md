### Intrinsic Data types    
`Buffer` -   Buffer, which contains one or more scalars  
`Scalar`  -  One-component scalar  
`Vector`, `Matrix`  -  Multiple-component vector or matrix  
`Sampler`, `Shader`, `Texture `  - Sampler, shader, or texture object  
`Struct`, `User Defined`  - Custom structure or typedef  

### Variables
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






### Vertex Shader Semantics:
`BINORMAL[n]`	float4 - Binormal	  
`BLENDINDICES[n]`	uint - Blend indices	    
`BLENDWEIGHT[n]`	float - Blend weights	    
`COLOR[n]`	float4 - Diffuse and specular color	/ Diffuse or specular color  
`NORMAL[n]` float4 -	Normal vector	  
`POSITION[n]`	float4 - Vertex position in object space  
`POSITIONT` 	float4 -	Transformed vertex position     
`PSIZE[n]`		float - Point size   
`TANGENT[n]`		float4 - Tangent    
`TEXCOORD[n]`		float4 - Texture coordinates 

##### Output: 
`POSITION[n]`	float4 - Vertex position in homogenous space. Compute position in screen-space by dividing (x,y,z) by w   
`FOG`	float - Vertex fog	   
`PSIZE`float -	Point size  
`TESSFACTOR[n]` float -	Tessellation factor  
`TEXCOORD[n]`	float4 - Texture coordinates   

### Pixel Shader Semantics:
`COLOR[n]`	float4 - Diffuse or specular color    
`TEXCOORD[n]` float4	- Texture coordinates	   
`SV_IsFrontFace` float - 	Floating-point scalar that indicates a back-facing primitive. A negative value faces backwards   
`SV_Position`	float2 - The pixel location (x,y) in screen space  

##### Output:    
`SV_Depth`, `COLOR[n]`	float4 - Output color	     
`SV_Target`, `DEPTH[n]`	float - Output depth	    

### DirectX10 Semantics:  
`SV_POSITION`, which is interpreted by the rasterizer stage can be specified as an input to a vertex shader as well as an output Pixel shaders can only write to parameters with the SV_Depth and SV_Target system-value semantics    
`SV_VertexID`, `SV_InstanceID`, `SV_IsFrontFace` can only be input into the first active shader   
`SV_Target[n]`, where 0 <= n <= 7	The output value that will be stored in a render target. available to all shaders    
`SV_Depth`  

http://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm   - SDF & HLSL

### Key Words

`return [value];`    
`continue;`   - Stop loop (do, for, while) / update the loop conditions / begin executing from the top of the loop   
`discard;`  - Do not output the result of the current pixel     
`break;`  - Exit the surrounding loop (do, for, while).  


```
float Scale;
float4 main(in float2 uv: TEXCOORD0): SV_TARGET
{
 float x = sin(uv.x*Scale);
 return float4(0.4,x,0.5,1.0);   
}
```
https://www.bouncepatch.com/hlsl.html  - hlsl tuts
https://www.ronja-tutorials.com/2018/03/20/hlsl-basics.html  - hlsl tuts  
http://www.catalinzima.com/xna/tutorials/crash-course-in-hlsl/  - hlsl ala wiki
http://rbwhitaker.wikidot.com/hlsl-tutorials - hlsl xna

http://www.alanzucconi.com/2016/07/01/volumetric-rendering/ - volume implementation hlsl 
