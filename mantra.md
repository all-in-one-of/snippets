


### PBR      

```css
realistic light with multip dif bounces. (use rayytrace) and phis light 
www.sidefx.com/tutorials/mantra-pbr-sampling-render-settings-path-tracer-houdini-16-1/
[mantra] rendering >  shadeing:  ENABLE ABSORBTIONA AND NESTED DIELECTRICS ~!!!! turn on !
GI - diffuse limits
```

### MICRO POLIGON  

```css
-(divide to micro polis in buckets) (same as pbr but mp)
- rendering DICEING: shader quality 1 >> 5
 ```

### RAY TRACRING: 
```css
reflection & refraction. (cleaner resoult because not diceing) its going pixel by pixelon image.
```

## Render Settings:
setting | lo | med | hi | production 
--- | --- | --- | --- | ---
pixel sample | 4x4 | - | 7x7 | 10x10 (fur or huge motion)
Min/Max ray samples | - | 1/9 | - | 2/9
Noise Levels | - | 0.1 | - | 0.08
Sample Lock | - | ON | - | OFF
Stochastic sample (AA volume quality) | 1 | - | - | 4

**[light]** light: sample quality on lights more than 1 (on direct samples) now direct light is clean. 

### Indirect illumination:
[mantra] rendering > limits:  2 3 2 0 1
[mantra] rendering > sampling, Qualities. diffiuse, reflection  quality (1-4)
Reflect/Refract/Diffuse lim 4/4/1  
Color Space Gamma 2.2
Color Limit 4

### PHOTON MAP 
generaiotn (Final gather) for final gather
