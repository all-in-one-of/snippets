

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
