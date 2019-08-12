# Materials
Albedo 

Mat | Albedo int U4 | Lagarde tut (linear space) other workfolw?|  
-- | -- | -- | 
Charcoal / Fresh asphalt | 0.02 | 0.04
Worn asphalt | 0.08 | 0.12
Bare soil | 0.13  | 0.17
Green grass | 0.21 |  0.25
Desert sand | 0.36  | 0.40
Fresh concrete | 0.51 |   0.55
Ocean Ice | 0.56 | 0.5–0.7
Fresh snow | 0.81 |  0.80–0.90
Metallic  |  0.7 - 1 |
-- | -- | -- | 
Neutral Gray | .5 | (128, 128, 128)
Middle Gray |  .18 | (46, 46, 46)




Spec / Refraction

Mat | specular U4 | Index of Refraction (IOR) |  
-- | -- | -- | 
COMON | 0.5 | 1.5
Air | | 1
Ice | 0.224 | 1.31
Water  |  0.255 | 1.33
Milk | 0.277 | 1.350
Skin | 0.35 |  
Glass | 0.5 | 1.52
Plastic | 0.5 | 1.460
Quartz | 0.57 | 1.544 - 1.644
Diamond | | 2.42


- Dielectric F0 Reflectance Value = ( (1 - IOR) / (1 + IOR) )² 
- Gamma Correction-to-Linear RGB Linear RGB Value = ( Gamma Correction Value ^ (1 / 2.2))  
- Linear RGB-to-Gamma Correction Gamma Correction Value = (Linear RGB Value ^ 2.2)  


(Dielectric F0 Reflectance Value / 0.08) = UE4 Specular Reflectivity Value 



https://seblagarde.wordpress.com/2011/08/17/feeding-a-physical-based-lighting-mode/

Note: The roughness here is coupled with the BRDF used by the Unreal engine 4, it may not be compatible with other engine or offline renderer.


# PostProcess  

 

# Photorealism transfer guide

#### Photo references

Automatic Exposure Bracketing examples:  
13EV's of scene light for interiors (7 shots with 2EV)  
26EVs for Outdoors - Sun visible sometimes even on -20EV  

#### Shoot
- Shoot RAW - 16 bit if possible. HDR: (if not PBR will be affected)   
- Orient set to recognize front direction  
- Shoot in central point of scene: Cannot change EV during shot.    

`Color checker` - white ballans. from differences between shoot and CG create transform matrix to neutralize colour cast (shoot fulll exposure)   
`Gray card` - to set base EV (correctly expoing for 18% grey calibration card (fill frame) which is oriented twoward main light (without shadow))  
`Gray ball` -  lighting intensity and direction 18% grey (like lambert shading)   
`Chroma ball` -  help to correct Lightprobe rotation and light locations- shoot front and side   
`Lightprobe` shot for HDRI shoot with 8mm lens 3 shoots 0 120 240  

`RAW` > `TIFF` (PTGUI software) > merge to  `EXR` panorama  > color correction 

#### Unreal Light
- For unreal HDRI mask out light sources to get ambient light   
- Gray Ball 18% Sepecular 0.7 Roughtnss 0.85 - paint on physical grayball    
- Position ball in exact location, find front orientation   
- Turn off PP    
- Set lights in proper location  
- Set lights intensity: Go to HDR view and match chroma ball with reference image by seting   

#### Color
people have Trichromatic Vision - RGB

- `Spectral Locus` - ploting all visible colors can show how much sRGB is limited. rec2020 (much vider color space)    
- `Linear Color` - (for render) humans persute color in not linear We apply gamm acorection to look like we see   
- Linear to sRGB (for sRGB dvices) - Mid grey 18% after gamma look like 50%     
- Enviroment make diference how we see image  (monitor clalib and viewing conditions)

#### HDR
HDR Affect diffuse and specular
Render in linear > Apply gamma > apply s-curve corections.
ACES - Academy color space  to prserce dynamic rangfe and color values  
