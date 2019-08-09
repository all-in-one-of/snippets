Eye 20 f-stops / best cams 16 / dlsr - up to 13  

#### Photo references
- ISO 
- EV 
- shutter speed 
- f-number

Lenns info
The Nodal Point of the lens (or more correctly, the entrance pupil) can be considered as the point at which the rays entering the lens converge. It can also be considered as the centre of perspective of the lens or the apparent pupil. 
 
 
  
HDR: (if not PBR will be affected)    
AEB examples:  
13EV's of scene light for interiors (7 shots with 2EV)  
26EVs for Outdoors - Sun visible sometimes even on -20EV  

#### Shoot
Shoot RAW - 14 bit compression, (16 bit if possible)  
Orient set to recognize front direction  

Shoot in central point of scene: Cannot change EV during shot.    
`Color checker` - white ballans. from differences between shoot and CG create transform matrix to neutralize colour cast (shoot fulll exposure)   
`Gray card` - to set base EV (correctly expoing for 18% grey calibration card (fill frame) which is oriented twoward main light (without shadow))  
`Gray ball` -  lighting intensity and direction 18% grey (like lambert shading)   
`Chroma ball` -  help to correct Lightprobe rotation and light locations- shoot front and side   
`Lightprobe` shot for HDRI shoot with 8mm lens 3 shoots 0 120 240  

`RAW` > `TIFF` (PTGUI software) > merge to  `EXR` panorama  > color correction 

#### Unreal Light
For unreal HDRI mask out light sources to get ambient light   
Gray Ball 18% Sepecular 0.7 Roughtnss 0.85 - paint on physical grayball    
Position ball in exact location, find front orientation   
Turn off PP    
Set lights in proper location  
Set lights intensity: Go to HDR view and match chroma ball with reference image by seting   
 
 
# Color
#### Trichromatic Vision - RGB
Radio Wave > Mivcrowave > Infrared > R (780nm) > G > B (380nm) > Ultraviolet > X-rays >Gamma    
Spectral Locus - ploting all visible colors can show how much sRGB is limited. rec2020 (much vider color space)    
Linear Color - (for render) humans persute color in not linear We apply gamm acorection to look like we see   
Linear to sRGB (for sRGB dvices) -   
Mid grey 18% after gamma look like 50%     
Enviroment make diference how we see image  (monitor clalib and viewing conditions)
#### HDR
HDR Affect diffuse and specular
Render in linear > Apply gamma > apply s-curve corections.
ACES - Academy color space  to prserce dynamic rangfe and color values  


BlackBody: 

### measurement  
Azimuth - Horizontal angle of the sun’s position.
Zenith - Vertical angle of the sun’s altitude.
Unmotivated Light - Support light that doesn't have a physical representation.
`Key light`, `fill light`, `rim light`, 
`Direct`, `Indirect`, `Ambient`, `Difuse light `  

#### Camera 
Shutter Speed = (1 / Time) = Fraction of a Second
EV100 = ( log2(Aperture² / (Shutter Speed) * 100 / ISO) )



