
www.editor.thebookofshaders.com
www.thebookofshaders.com
Vertex shader pixel shader compute shader


### Data types  

`float` -  
`vec2` -   
`vec3` -   
`vec4` -   
`mat2` -   
`mat3` -   
`mat4` -   
`sampler2D` -  
`samplerCube` - 

Attributes (data pulled from buffers)
Uniforms (values that stay the same for all vertices of a single draw call)
Textures (data from pixels/texels)

### Key Words

`gl_FragColor` - Shader Language has a single main function that returns a color assigned to the reserved global variable 

`vec4 gl_FragCoord`  

**Macros** are part of a pre-compilation step. With them it is possible to `#define` global variables and do some basic conditional operation (with `#ifdef` and `#endif`). All the macro comands begin with a hashtag (#).  
```glsl
#ifdef GL_ES
precision mediump float;
#endif
```
Pre-compilation happens right before compiling and copies all the calls to `#defines` and check `#ifdef` (is defined) and `#ifndef` (is not defined) conditionals.


#### - 

```
vec4 red(){
    return vec4(1.0,0.0,0.0,1.0);
}
```

```
vec4 color = vec4(vec3(1.0,0.0,1.0),1.0);
```
 sin(), cos(), tan(), asin(), acos(), atan(), pow(), exp(), log(), sqrt(), abs(), sign(), floor(), ceil(), fract(), mod(), min(), max() and clamp().
 
```glsl
 #ifdef GL_ES
precision mediump float;
#endif

uniform float u_time;

void main() {
	gl_FragColor = vec4(abs(sin(u_time)),0.0,0.0,1.0);
}
```
#### fn
```
int newFunction(in vec4 aVec4,      // read-only
                out vec3 aVec3,     // write-only
                inout int aInt);    // read-write
		
	```
