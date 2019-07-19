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
