### Data types  

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

float4 color;  
uniform float4 position : SV_POSITION;   
const float4 lightDirection = {0,0,1};  



Use This Intrinsic Type    To Define Shader Variable   
`Buffer`    Buffer, which contains one or more scalars  
`Scalar`    One-component scalar  
`Vector`, `Matrix`    Multiple-component vector or matrix  
`Sampler`, `Shader`, `Texture `   Sampler, shader, or texture object  
`Struct`, `User Defined`    Custom structure or typedef  

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
