T | lo | med | hi 
--- | --- | --- | ---
pixel sample | 4x4 | - | 7x7


PBR       realistic light with multip dif bounces. (use rayytrace) and phis light www.sidefx.com/tutorials/mantra-pbr-sampling-render-settings-path-tracer-houdini-16-1/
```css
[mantra] rendering >  shadeing:  ENABLE ABSORBTIONA AND NESTED DIELECTRICS ~!!!! turn on !
GI - diffuse limits
```
MICRO POLIGON  (divide to micro polis in buckets) (same as pbr but mp)
```css
 - rendering DICEING: shader quality 1 >>5
 ```

RAY TRACRING: reflection & refraction. (cleaner resoult because not diceing) its going pixel by pixelon image.
```css
[mantra] rendering > sampling  > pixel sample: mnoznik 
-prev 4x4 
-high 7x7
-production 10x10 (jak duzo ruchu albo fur)

<Min/Max ray samples>
-normal 1/9
-production 2/9

Noise Levels 
-normal: 0.1
-production: 0.08

[light] light: sample quality on lights more than 1 (on direct samples) now direct light is clean. 

[mantra] rendering > sampling  > Stochastic samp: (Stochastic is AA breaking reg iun sampling) for Volume (1-4)

Indirect illumination:
[mantra] rendering > limits:  2 3 2 0 1
[mantra] rendering > sampling, Qualities. diffiuse, reflection  quality (1-4)

Reflect/Refract/Diffuse lim 4/4/1

Color Space Gamma 2.2

Color Limit 4

Sample Lock
-normal ON
-production OFF
```

PHOTON MAP generaiotn (Final gather)
```css
for final gather
```
