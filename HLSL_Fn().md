# Data types  
Use This Intrinsic Type    To Define This Shader Variable   
`Buffer`    Buffer, which contains one or more scalars  
`Scalar`    One-component scalar  
`Vector`, `Matrix`    Multiple-component vector or matrix  
`Sampler`, `Shader`, `Texture `   Sampler, shader, or texture object  
`Struct`, `User Defined`    Custom structure or typedef  
 
bool true or false  
int 32-bit integer  
half 16bit integer  
float 32bit float  
double 64bit double  
float3 vectorTest  
float vectorTest[3]  
vector vectorTest  
float2 vectorTest    
bool3 vectorTest    
float3x3: a 3×3 matrix, type float  
float2x2: a 2×2 matrix, type float  



http://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm



`break;` Exit the surrounding loop (do, for, while).

### Math
```hlsl
sin(Emitter.Age)*56
float3(Particles.UV,0)*400
abs(Particles.NormalizedAge * 2.0f -1.0f) 
normalize(((( rand(float3(1.0,1.0,1.0) ))) * 2 ) -1 )
Particles.Position + float3(0, 0, ( sin(Engine.Time) * 0.3f ))
Emitter.InitialPosition + Particles.RandomVector *rand(145.0f)
(1.0f - abs(Particles.NormalizedAge * 2.0f -1.0f)) * 2.0f
1-Particles.RandomVector * (length(Particles.Position - Emitter.InitialPosition)*0.25)

cross(Particles.RandomVector, float3(0,8,0)) * 
    (float3(0.0f, 0.0f, Emitter.ZOffset) *0.2f) + 
    (-1.0f * normalize(Emitter.InitialPosition - Particles.Position)*20)
```

### Fn
intrinsic functions list: 
https://docs.microsoft.com/en-us/windows/desktop/direct3dhlsl/dx-graphics-hlsl-intrinsic-functions
```hlsl
rand(1.5f) + 2.2f
rand(11.1f) + 2.5f
length(Particles.Position - Emitter.InitialPosition)

```


