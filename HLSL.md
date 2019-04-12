### Data types  

Use This Intrinsic Type    To Define Shader Variable   
`Buffer`    Buffer, which contains one or more scalars  
`Scalar`    One-component scalar  
`Vector`, `Matrix`    Multiple-component vector or matrix  
`Sampler`, `Shader`, `Texture `   Sampler, shader, or texture object  
`Struct`, `User Defined`    Custom structure or typedef  

http://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm   
`bool` true or false  
`int` 32-bi integer  
`half` 16bit integer  
`float` 32bit float  
`double` 64bit double  
`float3` vectorTest  
`float` vectorTest[3]  
`vector` vectorTest  
`float2` vectorTest    
`bool3` vectorTest    
`float3x3`: a 3×3 matrix, type float  
`float2x2`: a 2×2 matrix, type float  

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




### UE4 example  
```hlsl 

float3 blur = Texture2DSample(Tex, TexSampler, UV);

for (int i = 0; i < r; i++)
{

  blur += Texture2DSample(Tex, TexSampler, UV + float2(i * dist, 0));
  blur += Texture2DSample(Tex, TexSampler, UV - float2(i * dist, 0));

}

for (int j = 0; j < r; j++)
{ 

  blur += Texture2DSample(Tex, TexSampler, UV + float2(0, j * dist));
  blur += Texture2DSample(Tex, TexSampler, UV - float2(0, j * dist));

}

blur /= 2*(2*r)+1;
return blur;

```
