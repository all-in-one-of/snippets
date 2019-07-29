# NOISE TYPES:
`Perlin` - perlin moze miec artefakty   
`Simplex` - faster  
  
`Spare convolution` - chyba do chmur ???  
`Sinus` -  
  
`Worley` -  Computes 1D, 3D, and 4D Worley noise, which is synonymous with "cell noise".   
`Voronoi` -  Voronoi noise, which is similar to Worley noise but has additional control over jittering.  
`Cell` - Computes 2D, anti-aliased cellular noise suitable for shading.  
`Alligator` -  
  
`Hebyshev`  - kwadratowy H16.5   
`Manhattan` - kwadratowy H16.5  

### Anti Alias noise  - [0.5 - .5]  
Faster than unified. Compute band-limited noise. Ideal for shading

### Unified noise [0-1]  
Presents a unified interface and uniform output range for all the noise types available in VEX

### Curl noise
divergence-free 3D (vector) noise - function for perlin or simplex divergence is a vector operator that produces a scalar field

### Turbulence noise 
Compute turbulence with roughness and attenuation

`Original Perlin` - similar to Perlin noise, but marginally less efficient in computation and with different characteristics. The bounds on the noise are roughly (-1, 1) when turbulence is 0.    
`Perlin` - sums octaves of a noise with range about (0, 1), resulting in a non-zero centered result. Thus the zero centered perlin better matches the ranges of the other noise fields.    
`Simplex` - close to Perlin noise, except with the samples on a simplex mesh rather than a grid. This results in less grid artifacts. It also uses a higher order bspline to provide better derivatives    
`Alligator` - similar to Worley It is currently not possible to simulate Alligator noise using the Worley functions, but it is possible to get a very similar 'look'. The bounds on the noise are roughly (0, 0.5) when turbulence is 0.    
`Sparse Convolution` - similar to Worley The noise returned is based on the weights of all of the closest points, with each point’s contribution based on a meta-ball like rolloff curve. That is, if the sample point is close to the sphere, its contribution will be greater. The bounds on the noise are roughly (-1.7, 1.7) when turbulence is 0    


---

COST | NOISE | - | VEX
--- | --- | --- | --- 
1.0 | Perlin Noise | (see Periodic  Noise operator) | (string value "pnoise")
1.1 | Original Perlin Noise | (see Turbulent Noise operator) | (string value "onoise")
1.8 | Worley Noise | - | -
1.8 | Periodic Worley Noise | (see Periodic Worley Noise operator) | -
1.9 | Voronoi Noise | (see Voronoi   Noise operator) | -
2.1 | Sparse Convolution Noise | (see Turbulent Noise operator) | (string value "snoise")
2.3 | Alligator Noise | (see Turbulent Noise operator) | (string value "anoise")
x | Simplex noise | - | (string value "xnoise")
x |Zero Centered Perlin | - | (string value "correctnoise")

           
           
# RANDOM:
`v@v = rand(@Time+@ptnum);` // random between 0-1  
`v@v = sample_hemisphere({0,0,1},@bias,u);` -   
`v@v = sample_direction_cone()` -     
`v@v = sample_sphere_cone()` -   

#### Random Color 
```cpp
float pscale = rand(@ptnum);
vector direction = rand(@ptnum); //will create rand float for x, y and z direction
float r = random(@ptnum+1);
float g = random(@ptnum+2);
float b = random(@ptnum+3);
@Cd = set(r,g,b);
```

#### Divergence free noise  
(divergence free vector field) based on the cross product of the derivatives of two simplex noise functions.  
```cpp
vector frequency = chv("Frequency");
vector offset = chv("Offset");
vector dir = curlnoise((@P * frequency) + offset);  // perlin
vector dir = curlxnoise((@P * frequency) + offset); // simplex 

```
#### Offset Position
```
vector offset =  xnoise(v@P + set(p,p,p)) - {.5,.5,.5};
v@P += offset;
```


#### Fade noise on curves with ramp 
```
// Requires uvtexture SOP in "Pts and Columns" mode before this wrangle

// Define UI controls
float remap_uv = chramp('remap_uv', @uv.x);
float power = chf('Noise_Power');
float freq = chf('Noise_Frequency');

// Create noise
vector noiseXYZ = noise(@P*freq);
// Modify noise values
vector displace = fit(noiseXYZ, 0,1, -1, 1)*power*remap_uv;
// Apply modified noise to a points position
@P += displace;
// Visualize fade ramp on curve
@Cd = remap_uv;
```

#### Delete Points based on noise  
```

// Visualise nose as Black and White values
// Delete black and white points separatly

// Default non zero values for 10X10 grid:
// Noise_size = 1
// Noise_threshold = 0.5

// Make geometry white
@Cd = {1, 1, 1};

// Setup noise
float noseValues = noise(@P*(1/chf('Noise_Size')) + chf('Noise_Offset'));

// Paint-delete points with noise
if(noseValues > chf('Noise_Threshold')){
    @Cd = 0;
    if(rand(@ptnum) < ch('delete_black')){
        if(chi('del') == 0){
            @Cd = {1,0,0};
            }
        else{
            removepoint(0,@ptnum);
            }
        }
    }

if(noseValues < chf('Noise_Threshold')){
    if ( rand(@ptnum) < ch('delete_white') ) {       
        if(chi('del') == 0){
            @Cd = {1,0,0};
            }
        else{
            removepoint(0,@ptnum);
            }
        }
    }
```



https://www.nekopori.com/blog/houdini-noisesample  
