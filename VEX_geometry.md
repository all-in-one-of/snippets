### Hypotrochoid
- x = (R-r) * cos(alpha) + d * cos(R-r/r*alpha)
- y = (R-r) * sin(alpha) - d * sin(R-r/r*alpha)
- R is radius of outer circle
- r is radius of rolling circle
- d is displace amount (scalar multiply) applied to center of rolling circle
to create trace point
```
#include <math.h>

float theta = ch("Theta") * PI * 2;
@theta2 = ch("Theta") * PI * 2;
float R = ch("R");
float r = ch("r");
float d = ch("d");

//Outer Circle
int R_circle = addprim(0,"polyline");

for(int i = 0; i < 400; i++){
    float x, y;
    x = R * cos(radians(1) * i);
    y = R * sin(radians(1) * i);

    int point = addpoint(0,set(x,y,0));
    addvertex(0,R_circle,point);
}

//Rolling Circle
int r_circle = addprim(0,"polyline");

for(int i = 0; i < 400; i++){
    float x, y;
    x = r * cos(radians(1) * i) + (R - r) * cos(theta);
    y = r * sin(radians(1) * i) + (R - r) * sin(theta);

    int point = addpoint(0,set(x,y,0));
    addvertex(0,r_circle,point);
}
  
//Center of rolling circle
    float centerx, centery;
        
    centerx = (R - r) * cos(theta);
    centery = (R - r) * sin(theta);
    
    vector center = set(centerx,centery);
    
    int centerpoint = addpoint(0,center);

//Solve right triangle of center of rolling circle and origin
    
//Find hypotenuse
    @hypotenuse = length(center);
    
    vector origin = (0,0,0);
    int originpoint = addpoint(0,v@origin);
    
    int hypotenuseprim = addprim(0,"polyline");
    addvertex(0,hypotenuseprim,originpoint);
    addvertex(0,hypotenuseprim,centerpoint);
    
 //Find adjacent
    @adjacent = center.x;
    
    int adjpoint = addpoint(0,set(@adjacent,0,0));
    
    int adjacentprim = addprim(0,"polyline");
    addvertex(0,adjacentprim,adjpoint);
    addvertex(0,adjacentprim,originpoint);
    
 //Find opposite with pythagorean theoream
    
    float c = pow(@hypotenuse,2);
    float a = pow(@adjacent,2);   
    @opposite = sqrt(c - a);
    
    int oppositeprim = addprim(0,"polyline");
    addvertex(0,oppositeprim,adjpoint);
    addvertex(0,oppositeprim,centerpoint);
    
 // Find all trig functions
    
    float tan = @opposite / @adjacent;
    float sin = @opposite / @hypotenuse;
    float cos = @adjacent / @hypotenuse;
 
    // Find all inverse trig functions
    @arctan = atan(tan);
    @arcsin = asin(sin);
    @arccos = acos(cos);
    
//Solve

float rate = ch("Rate");
int hypotrochoidline = addprim(0,"polyline");
float hx = (R - r) * cos(theta) + d * cos((R-r/r)*theta*rate);
float hy = (R - r) * sin(theta) - d * sin((R-r/r)*theta*rate);
int hypotrochoidpoint = addpoint(0,set(hx,hy,0));
addvertex(0,hypotrochoidline,hypotrochoidpoint);
addvertex(0,hypotrochoidline,centerpoint);

//Make the trail
int hypotrochoidtrail = addprim(0,"polyline");

float resolution = ch("Resolution");
float iterations = ch("Iterations");
for(int i = 0; i < iterations; i++){

float x = (R - r) * cos(theta-(resolution*i)) + d * cos((R-r/r)*(theta-(resolution*i))*rate);
float y = (R - r) * sin(theta-(resolution*i)) - d * sin((R-r/r)*(theta-(resolution*i))*rate);

int point = addpoint(0,set(x,y,0));
}
```
