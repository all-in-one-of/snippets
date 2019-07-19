Shader Language has a single main function that returns a color at the end. This is similar to C.

The final pixel color is assigned to the reserved global variable gl_FragColor.  

Macros are part of a pre-compilation step. With them it is possible to #define global variables and do some basic conditional operation (with #ifdef and #endif). All the macro comands begin with a hashtag (#). Pre-compilation happens right before compiling and copies all the calls to #defines and check #ifdef (is defined) and #ifndef (is not defined) conditionals. In our "hello world!" example above, we only insert the line 2 if GL_ES is defined, which mostly happens when the code is compiled on mobile devices and browsers.

```
vec4 red(){
    return vec4(1.0,0.0,0.0,1.0);
}
```
```
```vec4 color = vec4(vec3(1.0,0.0,1.0),1.0);
```
