### Mat 
Albedo 

Mat | Albedo | |  
-- | -- | -- | 
Charcoal | 0.02  
Fresh asphalt | 0.02   
Worn asphalt | 0.08 
Bare soil | 0.13  
Green grass | 0.21  
Desert sand | 0.36  
Fresh concrete | 0.51  
Ocean Ice | 0.56  
Fresh snow | 0.81  
Metallic  | (179, 179, 179) - (255, 255, 255) | 0.7 - 1

Spec / Refraction

DIELECTRIC F0 REFLECTANCE VALUE FORMULA​
​( (1 - IOR) / (1 + IOR) )² = Dielectric F0 Reflectance Value
(Dielectric F0 Reflectance Value / 0.08) = UE4 Specular Reflectivity Value 


Mat | specular | IRO  Refraction |  
-- | -- | -- | 
Air | | 1
Ice | 0.224 | 1.31
Water  |  0.255 | 1.33
Milk | 0.277 |
Skin | 0.35 |  
Glass | 0.5 | 1.52
Plastic | 0.5 | 
Quartz | 0.57 |
Diamond | | 2.42
Dielectrics COMON | | 1.5

Gray | Col | % | 
-- | -- | -- | 
Neutral Gray | 128 | .5
Middle Gray |  46 | .18



Gamma Correction-to-Linear RGB
( Gamma Correction Value ^ (1 / 2.2) ) = Linear RGB Value
Linear RGB-to-Gamma Correction
(Linear RGB Value ^ 2.2) = Gamma Correction Value
