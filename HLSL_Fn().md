

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


