### GROUP AS ATTRIBUTE

`i@group_mygroup=1;` - in groups   
`group_name` - In other than GroupSOP, specify a named group (created with the GroupSOP)  

expression:  
`{arm* ^arm3*}`  - in the pattern. includes all groups whose names start with arm, but not arm3.   
`@Cd.x = (@group_myGroup==1) ? 1:0;` - 1 albo 0 w zaleznoci czy nalezy do myGroup czy nie @gorup_myGroup - read    

```
int in_group = (@group_myGroup==1) ? 1:0;
@Cd = set(in_group, 0 , 0);
```
```
@Cd = {0,0,0};
@Cd.x = (@group_myGroup == 1) ? 1:0;
```
```
if (@group_mygroup ==1)  {
@Cd = {1,1,0};
}
else {
    @Cd = {0,0,1};
}
```
### ATTRIBUTE AS GROUP
Attributes as groups, or groups with @ syntax

expression:  
`0-5000:2 ^ 40-200`  
`!50-200`   
`@P.y>0` - group of all points whose Y component is greater than `0*/ $BBY>.9999`     
`@id=5-10`  
`@id="5 8 10 15"` - You can also use the attribute syntax //space separated list of integer values, need to enclose the list in quotes. 
`@myattr="foo bar"` - quotation marks if it contains spaces   
`=`, `==`, and `!=`  - on string attr  
`(* and ?)` -  wildcards value when using   



`@objname=myObject` - what about using Blast SOP and put this in Group field:   
`@objname=my*` - or you can even use patterns   
`$OBJ+1` - numer obiektu + 1 bo numeracja od zera   

`if (f@burned>0)`  
`if ($F%10==0, $FF,0)` - evert 10th frame create obj and floating frame   
`if (@Cd.r < 0.1) {  i@group_mygroup=1;  }`   
`if ( rand(@ptnum) > ch('threshold') ) {   removepoint(0,@ptnum);  }`     

`fit01(rand($OBj),-1,1)* 10` - rand negative -10 do 10  
`point("../" + opinput(".", 0), $PT, "neighbour", 0) <= 3`    
`rand($OBJ)`   
`strcmp($OBJNAME,“myObject”)` - Compares two strings.  
`chramp(ramp_path, position, component_index)`   
`ch("../A/sx")/2`   

What’s more is, you can execute script in those fields by putting it in back-ticks - `
