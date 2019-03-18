data types  
``` Use This Intrinsic Type    To Define This Shader Variable
Buffer    Buffer, which contains one or more scalars
Scalar    One-component scalar
Vector, Matrix    Multiple-component vector or matrix
Sampler, Shader, Texture    Sampler, shader, or texture object
Struct, User Defined    Custom structure or typedef
```





http://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm



### Math
```hlsl
sin(Emitter.Age)*56
abs(Particles.NormalizedAge * 2.0f -1.0f)
cross(Particles.RandomVector, float3(0,8,0)) * 
    (float3(0.0f, 0.0f, Emitter.ZOffset) *0.2f) + 
    (-1.0f * normalize(Emitter.InitialPosition - Particles.Position)*20) 
normalize(((( rand(float3(1.0,1.0,1.0) ))) * 2 ) -1 )
Particles.Position + float3(0, 0, ( sin(Engine.Time) * 0.3f ))
Emitter.InitialPosition + Particles.RandomVector *rand(145.0f)
(1.0f - abs(Particles.NormalizedAge * 2.0f -1.0f)) * 2.0f
1-Particles.RandomVector * (length(Particles.Position - Emitter.InitialPosition)*0.25)
```
### Fn
```hlsl
rand(1.5f) + 2.2f
rand(11.1f) + 2.5f
length(Particles.Position - Emitter.InitialPosition)

```
### If
```hlsl
Particles.NormalizedAge < 0.333 ? float4(1,0.1,0.1,1) : Particles.NormalizedAge < 0.575 ? float4(0.1,1,0.1,1) : float4(0.1,0.1,1,1)
Particles.Position.z > Emitter.InitialPosition.z - Emitter.ZOffset ? Particles.Position : float3(Particles.Position.x, Particles.Position.y, Emitter.InitialPosition.z -Emitter.ZOffset)

```

