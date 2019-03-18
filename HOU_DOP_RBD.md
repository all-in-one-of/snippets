# Solvers:   

```
- OBJECT
- PRE-SOLVE
- POST-SOLVE
```

### Static solver  

### Rigid solver 
#### rdb   

#### bullet
bullet likes pieces between 0.1 and 100 if you need smaller pieces, scale up and boost gravity proportionally  

### Multi Solver  
- multisolver is for pops (and rigid body)  

# RDB Objects:  

### static object 
moze byc jako kolizyjna ruchoma geometria w dopach (Simulating a Splashdown in Houdini - Escape Studios Free Tutorial)  
if its plane turn off volume based collision
**Vdb collision source:**
- mode: collision intersect to volume source 
- proxy volume: vdb path

### rdb object  
Also use for collision in flips  flips  (FLIP Fluids https://vimeo.com/116176349)
- increes density 

### rdb packed object  



