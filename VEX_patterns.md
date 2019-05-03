

### Arithmetic 
`=`, `==` (same as), `!=`, `>`,` <`, `>=`, `<=` , `+=`, `++` - add one , `%` - modulus  

### Conditionals:
`!` - Logic negation, `==` - equal, `!=` - is not equal, `||`- Logic OR, `&&` - Logic AND
### Patterns:
Pattern may be a numeric pattern, attribute pattern, or group name pattern.
`?` -  Match any character  
`*` - Match any substring  
`^` - Exclude from match  
`[list]` - Match any of the characters specified in the list.  
`!*` - ????????????  
`a*`,`^aardvark` - Match any string beginning with a except for aardvark.    
`[abc]*z` - Match any string beginning with a, b or c and ending with z.    
`g*`,`^geo*` - Match any string beginning with g, but not any string beginning with geo.    
`^pattern` - Remove matching, `0-100:2 ^10-20` every other number 1 to 100 except the 10 to 20.  
`!pattern` - Every except the ones matching the pattern. `!1-10` means every except the numbers 1 to 10.   

### Points/primitives numbered:
`n` - number n.   
`n-m` - from n to m (inclusive).   
`n-m:step` - from n to m (inclusive) skipping every step. Eg; `1-100:2` every other number from 1 to 100.    
`n-m:keep,step` - from n to m (inclusive). Use the first keep numbers and then skip every step after that.    

### Delete node
`$N` - Delete By Patte  
`$PT==$NPT-1` - Delete By Expression    
`$N*` - Delete By Range: change Start to  
