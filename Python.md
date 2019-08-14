  


translate = (1.0, 4.0, 2.0)
print translate[0]

### Variable types
```python 
string_var = "stringi"  
bool_var = True  
float_var = 3.1415  
```
### Import Lib

```python 
from math import *
```

#### Strings
```python 
print 230  
print "Hello World" 
print("String Text")
print("String Text" + string_var + "Another Text")  #with var
print("FirstLine \nSecondLine")  # Virtual Enter

phrase = "String text with more signs"  # VAR called phrase
print(phrase + "Another Text")
print(phrase.upper()) #
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

### Function
```python 
def say_hi(name, age):  
    print("Hello" + name + " ,you are" + age) #(code inside fn must be indentet)  

say_hi("Mike", "35") # ads not in function anymore
say_hi("Mi2ke", "325") # ads not in function anymore
```

```python 
def example(name):
   print name + "Our String" + colors[4]

def examplereturn(name):
   return name.upper()

print examplereturn("houdini") # will print HOUDINI with all big captions
```
