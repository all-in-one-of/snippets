`ident()` - empty matrix in centroid with no transforms  

### Arrays

`resize()` - Sets the length of the array. If the array is enlarged, intermediate values will be 0 or "".    
`len()` - -length of an array.    
`pop(i[]@MyArray, IndexToRemove)` - -last item from the array (decreasing the size of the array by 1) and returns it.    
`find(i[]@MyArray, ValueToFind)`    
`push(@MyArray, ValueToAdd)` - Adds an item to the end of an array (increasing the size of the array by 1).    
`getcomp()` - Gets the value of an array component, the same as array[num].   
`setcomp()` - Sets the value of an array component, the same as array[num] = value.    
`array()` - Efficiently creates an array from its arguments.   
`serialize()` - Flattens an array of vectors or matrices into an array of floats.    
`unserialize()` - Reverses the effect of serialize: assembles a flat array of floats into an array of vectors or matrices.    
`neighbours()` - An array-based replacement for the neighbourcount/neighbour combo. Returns an array of the point numbers of the neighbors of a given point.    

In addition, the following functions work with arrays:  
`min()`
`avg()`
`spline()`
`import()`
`addattribute()`
`metaimport()`

### Bounds

`getbbox(min, max)`  
`getbbox_center()` relative bbox  
`centroid("../in",D_X)` relative bbox  
`@Cd = relbbox(0, @P);` Color from bbox  

```cpp
vector min, max;
getbbox(min, max);
vector center = (min+max)/2;
```

### Measurement

`distance(@P, center );`  
`minpos(1,@P);`  
`nearpoint(1,@P);`  

### Conversion


`atof()`  
`atoi()`  

`degrees ()`  
`eulertoquaternion()`  
`qconvert()`  
`radians()`  

`hsctorgb()`  
`rgbtohsv()`  
`rgbtoxyz()`  
`zyztorgb()`  

`serialize ()`  
`unserialize()`  

