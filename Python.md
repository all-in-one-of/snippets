  


translate = (1.0, 4.0, 2.0)
print translate[0]

### Data types
```python
str = "3" + str(3) 
float = 3.
int = 3
bool = True 
bool = False 
```
#### Cast
`str()` - to string  
`int()` - if used on float it will  round down  
`float()`  

#### Strings
```python 
print 230
print 'Hello World' # python 2.x 
print "Hello World" # python 2.x both Valid!  
print("String Text") # python 3.x  
print("String Text" + string_var + "Another Text")  #with var  
print("FirstLine \nSecondLine")  # Virtual Enter

print "ChAnGe StRiNg To LoW CaSe".lower()  # lower( ), belong to strings, only attached to strings, 
print(phrase.upper()) #

phrase = "String text with more signs"  # VAR called phrase
print(phrase + "Another Text")

print(phrase[3] + " - 3 letter of string")   # search array for
print(phrase.index("have"))    # search array for in
print(phrase.replace("have", "dont have"))  # replace
```

#### List, Key&Value
```python
colors = ['red','green','blue'] //list  
print colors[1] //call list item   

geo = {"ROP": "Mantra", "COP": "Color", "SOP": "Platonic"}  # key and value   
geo["ROP"]  
```

#### import operator
```python
weightDict={"plane": 150, "car": 2, "house": 400, "banana":0.2}
sortedDict = sorted(weightDict.items(), key=operator.itemgetter(1),reverse=True)
```
### Math
`divisiontyp1 = 7/2` = 3   
`divisiontyp2 = 7/2.` = 3.5    
`divisiontyp2 = float(7)/2` = 3.5  

### Function
```python 
def say_hi(name, age):  
    print("Hello" + name + " ,you are" + age) #(code inside fn must be indentet)  

say_hi("Mike", "35") # ads not in function anymore
say_hi("Mi2ke", "325") # ads not in function anymore
```

```python 
def examplereturn(name):
   return name.upper()

print examplereturn("houdini") # will print HOUDINI with all big captions
```

### Import Library

```python 
from math import *
```
