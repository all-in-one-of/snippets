
Inputs:
```cpp
@P // fetch point position from first imput
v@opinmut1_P // fetch attribute from second input

f@foo // fetch first input foo
f@opinput1_foo // fetch second input foo

v@opinput1_N - normal from 1st input (counting from 0)
point(1, @N, ptnum) - normal from 1st input (counting from 0)

opinput(".", 0) //
opinputpath(".", 0)  // path of the node connected to the first input.
opinputpath("../",0) // path of geo (level up)
op:`opinputpath("../", 1)` // Second context geometry
geoself()

opname(".")  // operatorstring $OS  @OpInput1  
```

GROUP AS ATTRIBUTE
```cpp
i@group_mygroup=1; // in groups
group_name //In other than GroupSOP, specify a named group (created with the GroupSOP)
(*, ?, and [ ])  /* You can use pattern matching in the group name. 
For example, arm* includes all point/primitive groups whose names start with arm. 
^ can be used in the pattern by enclosing the pattern in { }. For example */ 
{arm* ^arm3*}  /* includes all groups whose names start with arm, but not arm3. */

@gorup_myGroup // READ FROM GROUP !!!!
@Cd.x = (@group_myGroup==1) ? 1:0;  // 1 albo 0 w zaleznoci czy nalezy do myGroup czy nie 

//2
int in_group = (@group_myGroup==1) ? 1:0;
@Cd = set(in_group, 0 , 0);

//3
@Cd = {0,0,0};
@Cd.x = (@group_myGroup == 1) ? 1:0;

//4 
if (@group_mygroup ==1)  {
@Cd = {1,1,0};
}
else {
    @Cd = {0,0,1};
}


```


ATTRIBUTE AS GROUP
```cpp
Group:
Attributes as groups, or groups with @ syntax

Base group / expression:
0-5000:2 ^ 40-200
!50-200
@P.y>0 /*  group of all points whose Y component is greater than 0*/ $BBY>.9999 
@id=5-10
@id="5 8 10 15" // You can also use the attribute syntax 
//space separated list of integer values, need to enclose the list in quotes.
@myattr="foo bar" /* quotation marks if it contains spaces,  */  
(* and ?) /*  wildcards value when using  */ 
=, ==, and !=  /* on string attr*/

@objname=myObject  // what about using Blast SOP and put this in Group field:
@objname=my* // or you can even use patterns
$OBJ+1 // numer obiektu + 1 bo numeracja od zera

if (f@burned>0)
if ($F%10==0, $FF,0) // evert 10th frame create obj and floating frame 
if (@Cd.r < 0.1) {  i@group_mygroup=1;  }
if ( rand(@ptnum) > ch('threshold') ) {   removepoint(0,@ptnum);  }

fit01(rand($OBj),-1,1)* 10 // - rand negative -10 do 10
point("../" + opinput(".", 0), $PT, "neighbour", 0) <= 3
rand($OBJ)
strcmp($OBJNAME,“myObject”)  // Compares two strings.
chramp(ramp_path, position, component_index)
`ch("../A/sx")/2` 

// `What’s more is, you can execute script in those fields by putting it in back-ticks.`
```
delete last point
```cpp
@ptnum == `npoints(0)-1` //group the last point on curve
@ptnum == @numpt-1 // group the last point on curve
@ptnum%(@numpt-1)==0  //1st AND last point at the same time

0-`npoints(opinputpath(“.”,0))-2` // selects all points but the last. //
0 `npoints(0)-1` // select first and last point
/*to delete last point
- Delete By Pattern: $N
- Delete By Expression: $PT==$NPT-1
- Delete By Range: change Start to: $N*/
```
