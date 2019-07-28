### Shader structure 
```
// Inputs
float4x4 object_to_world: WORLD;
float4x4 object_to_clip: WORLDVIEWPROJECTION;
float3 light_pos: LIGHT_POS;
float3 light_color: LIGHT_COLOR;

float3x3 object_to_world3x3 = (float3x3)object_to_world;

// Structures
struct vs_in {
   float4 pos_object: POSITION;
   float3 normal_object: NORMAL;
};

struct ps_in {
   float4 pos_clip: POSITION;
   float3 normal_world: TEXCOORD0;
   float3 light_world: TEXCOORD1;
};

// Vertex Shaders
ps_in vs_main(vs_in input) {
   ps_in output;
   output.pos_clip = mul(input.pos_object, object_to_clip);
   output.normal_world =
      mul(input.normal_object, object_to_world3x3);
   float4 pos_world = mul(input.pos_object, object_to_world);
   output.light_world = light_pos - pos_world.xyz;
   return output;
}

// Pixel Shaders
float4 ps_main(ps_in input) : COLOR {
   float3 result = light_world;
   float3 normal_world = normalize(input.normal_world);
   float3 light_world = normalize(input.light_world);
   result *= saturate(dot(normal_world, light_world));
   return float4(result, 1.f);
}

// Techniques
technique main {
   pass p0 {
      VertexShader = compile vs_3_0 vs_main();
      PixelShader = compile ps_3_0 ps_main();
   }
}
```
http://shaderjvo.blogspot.com/2011/08/introduction-to-hlsl-part-3.html  


### Var

`float4 color;`   
`uniform float4 position : SV_POSITION;`    
`const float4 lightDirection = {0,0,1};`  



discard; Do not output the result of the current pixel.

## Loop  
`[Attribute] do { Statement Block; } while( Conditional );` 
- Execute a series of statements continuously until the conditional expression fails. For statement.  Iteratively executes a series of statements, based on the evaluation of the conditional expression.    

`[Attribute] while ( Conditional ) { Statement Block; }` 
- while  
## Conditioning
`[Attribute] if ( Conditional ) { Statement Block; }`  




## Switch
`[Attribute] switch( Selector ) { case 0 : { StatementBlock; } break; case 1 : { StatementBlock; } break; case n : { StatementBlock; } break; default : { StatementBlock; } break;`

https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-intrinsic-functions
intrinsic functions list: https://docs.microsoft.com/en-us/windows/desktop/direct3dhlsl/dx-graphics-hlsl-intrinsic-functions HLSL-Spherical-Harmonics
