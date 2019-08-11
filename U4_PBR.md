### Mat 
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
Neutral Gray | 128 | .5
Middle Gray |  46 | .18




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


Grays



- Dielectric F0 Reflectance Value = ( (1 - IOR) / (1 + IOR) )² 
- Gamma Correction-to-Linear RGB Linear RGB Value = ( Gamma Correction Value ^ (1 / 2.2))  
- Linear RGB-to-Gamma Correction Gamma Correction Value = (Linear RGB Value ^ 2.2)  


(Dielectric F0 Reflectance Value / 0.08) = UE4 Specular Reflectivity Value 






https://seblagarde.wordpress.com/2011/08/17/feeding-a-physical-based-lighting-mode/

Note: The roughness here is coupled with the BRDF used by the Unreal engine 4, it may not be compatible with other engine or offline renderer.
