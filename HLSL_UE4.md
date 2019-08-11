# Unreal custom node: 


```
float3 foo = InputName;
returen foo; 
```

#### Exp fn. 
INPUT: `Input_1`  
INPUT: `exp`  
```hlsl
float ip1 = Input_1;
float S = float3(pow(ip1,exp));
return S;
```

#### Lerp
```hlsl
float3 ip1 = input_1;
float3 ip2 = input_2;
float3 ret = float3(lerp(ip1,ip2,ips));
return ret;
```


#### Blur (UE docs)
IN: Tex, Uv, r, dist  
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
https://forums.unrealengine.com/development-discussion/rendering/1409859-custom-hlsl-tips
https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-intrinsic-functions  fn list   
https://api.unrealengine.com/INT/API/Runtime/Engine/FViewUniformShaderParameters/index.html   

# NIAGARA



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

```hlsl
rand(1.5f) + 2.2f
rand(11.1f) + 2.5f
length(Particles.Position - Emitter.InitialPosition)
saturate (use as clamp 0-1 cause is fast!!)  

```
###  Conditioning  
```hlsl
Particles.NormalizedAge < 0.333 ? float4(1,0.1,0.1,1) : Particles.NormalizedAge < 0.575 ? float4(0.1,1,0.1,1) : float4(0.1,0.1,1,1)
```
```hlsl
Particles.Position.z > Emitter.InitialPosition.z - Emitter.ZOffset ? Particles.Position : float3(Particles.Position.x, Particles.Position.y, Emitter.InitialPosition.z -Emitter.ZOffset)
```
