# Unreal custom node: 

 
#### Exp fn. 
INPUT: `Input_1`  
INPUT: `ex`  
```hlsl
float ip1 = Input_1;
float S = float3(pow(ip1,ex));
return S;
```

#### Lerp
```hlsl
float3 ip1 = input_1;
float3 ip2 = input_2;
float3 ret = float3(lerp(ip1,ip2,ips));
return ret;
```
