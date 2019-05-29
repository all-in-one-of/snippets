### Circle
detail  
```int a = ch("angle");
float r = ch("radian");
// ad point in given coords 
for(a=0; a<360; a++){
addpoint(geoself(),set(cos(radians(a))*r, sin(radians(a))*r,0));
}
```
### Logarytmic spiral
detail  
- r = e^(a*theta)
```
#include <math.h>

float e = M_E;
float a = ch("a");
float theta = radians(ch("Theta"));

float r, x, y;
int line = addprim(0,"polyline");

float iterations = ch("Iterations");
for(int i= 0; i < iterations; i++){

r = pow(e,a*(theta * i));

x = r * cos(theta * i);
y = r * sin(theta * i);

int point = addpoint(0,set(x,y,0));
addvertex(0,line,point);
}
```

### Rhodonea Curve (sin @ polar)
detail
- k = n/d
- x = cos(k(theta))*cos(theta)
- y = cos(k(theta))*sin(theta)
```
float theta = radians(ch("Theta"));
float n = ch("n");
float d = ch("d");
float k = n/d;

float x,y;
int iterations = chi("Iterations");
int line = addprim(0,"polyline");

for(int i = 0; i < iterations; i++){

x = cos(k*theta * i) * cos(theta * i);
y = cos(k*theta * i) * sin(theta * i);

int point = addpoint(0,set(x,y,0));
addvertex(0,line,point);

}
```

### Polar Limacon
detail  
- r = a + b * cos(theta)
```
float a = ch("A");
float b = ch("B");
float theta = radians(ch("Theta"));

int iterations = chi("Iterations");
int line = addprim(0,"polyline");

float r;
for(int i = 0; i < iterations; i++){

float r = a + b * cos(theta * i);
float x = r * cos(theta * i);
float y = r * sin(theta * i);

int point = addpoint(0,set(x,y,0));
addvertex(0,line,point);
}
```
### Lissajous Curve
detail
- Freq_1
- Freq_2
- Freq_3
- Max Itteration
```
vector pos = set(0,0,0);

float f1 = chf("Freq_1");
float f2 = chf("Freq_2");
float f3 = chf("Freq_3");
float maxiter = chf("Max_Iterations");

int newprim = addprim(0, "polyline");

for(float angle = 0; angle < maxiter; angle += 0.01){
    float x = cos(angle * f1);
    float y = sin(angle * f2);
    float z = cos(angle * f3);
    pos = set(x,y,z);
    int newpt = addpoint(0, pos);
    addvertex(0, newprim, newpt);
}
```

### Superformula 2d

```
int   numsteps = chi("num_points");
float a = chf("a");
float b = chf("b");
float m = chf("m");
float n1 = chf("n1");
float n2 = chf("n2");
float n3 = chf("n3");

float   rad = radians(chf("degrees"));
float   step = (rad/numsteps);
float   theta = 0.0f;

for(int i=0; i<numsteps; i++) {
    // superformula
    float c = pow(abs(cos((m*theta)/4) / a), n2);
    float s = pow(abs(sin((m*theta)/4) / b), n3);
    float r = pow((c + s), (1/n1)*-1);
        
    // soh cah toa - convert polar coords to x,z plane
    float zaxis = sin(theta) * r;
    float xaxis = cos(theta) * r;    
    vector pos = set(xaxis, 0, zaxis);
    
    // create the point
    addpoint(geoself(), pos);
    
    // increse theta by the step size before next loop iter
    theta += step;
}
```
```
int   numsteps = chi("num_points");
float a = chf("a");
float b = chf("b");
float y = chf("y");
float z = chf("z");
float n1 = chf("n1");
float n2 = chf("n2");
float n3 = chf("n3");

float   rad = radians(chf("degrees"));
float   step = (rad/numsteps);
float   theta = 0.0f;

for(int i=0; i<numsteps; i++) {
    // superformula
    float c = pow(abs(cos((y*theta)/4) / a), n2);
    float s = pow(abs(sin((z*theta)/4) / b), n3);
    float r = pow((c + s), (1/n1)*-1);
        
    // soh cah toa - convert polar coords to x,z plane
    float zaxis = sin(theta) * r;
    float xaxis = cos(theta) * r;    
    vector pos = set(xaxis, 0, zaxis);
    
    // create the point
    addpoint(geoself(), pos);
    
    // increse theta by the step size before next loop iter
    theta += step;
}
```
### Superformula 3D

```
addpointattrib(geoself(), "long", 0, "");
addpointattrib(geoself(), "lat", 0, "");
// parms
int   numsteps_long = chi("num_points_long");
int   numsteps_lat = chi("num_points_lat");
float a1 = chf("a1");
float b1 = chf("b1");
float m1 = chf("m1");
float n1 = chf("n1");
float n2 = chf("n2");
float n3 = chf("n3");
float a2 = chf("a2");
float b2 = chf("b2");
float m2 = chf("m2");
float n4 = chf("n4");
float n5 = chf("n5");
float n6 = chf("n6");
float   step_long = ((2*$PI)/numsteps_long);
float   step_lat  = ($PI/numsteps_lat);
float   long    = -1*($PI);
float   lat     = -1*($PI/2);
for(int j=0; j<numsteps_lat; j++) {
for(int i=0; i<numsteps_long; i++) {
// superformula a
    float c1 = pow(abs(cos((m1*long)/4) / a1), n2);
    float s1 = pow(abs(sin((m1*long)/4) / b1), n3);
    float r1 = pow((c1 + s1), (1/n1)*-1);
// superformula b
    float c2 = pow(abs(cos((m2*lat)/4) / a2), n5);
    float s2 = pow(abs(sin((m2*lat)/4) / b2), n6);
    float r2 = pow((c2 + s2), (1/n4)*-1);
// 3D point plotting
    float xaxis = (r1 * cos(long)) * (r2 * cos(lat));
    float yaxis = (r1 * sin(long)) * (r2 * cos(lat));
    float zaxis = (r2 * sin(lat));
    vector pos = set(xaxis, yaxis, zaxis);
// create the point
    int pt = addpoint(geoself(), pos);
    setpointattrib(geoself(), "long", pt, i, "set");
    setpointattrib(geoself(), "lat", pt, j, "set");
// increse theta by the step size before next loop iter
    long += step_long;
}
    lat += step_lat;
}
```
### Hypotrochoid
detail
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
