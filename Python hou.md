Where to use:
- Python Shell - Live code
- Python Source Editor - you can save  code and function / hou.session.myDefinedFunction()
- Digital Asset -
- Shelf Tool - scrpit section to write code Executed after shelf click

### hou:
- `hou.` is houdini python class. We can drop it in **expressions**:  
- see what params is passing `kwargs` (pthos dict to see what is avalable)


# Python:
`node = hou.pwd()` -    
`node = hou.node('.')` - getting a reference to the current node.
`hou.node('/path')` - object in class hou  
`param = hou.ch("param")` - Read node parameter  
`bitmask = hou.ch("bitmask")` - Read node parameter   
`xBoundSize=lvar('SIZEX')` - Read local variables    
`geo = node.geometry()` - grabs the geometry data that is being fed into this node by calling its geometry() method.  

Assign objecto to var: foo
```python
foo = hou.node('/path')
foo.name #return name of object.

```


### evalParm(path) 
reference to this Python SOP via the node variable, we can use evalParm(path)to access each parameter  
```python
seed = node.evalParm('seed')
threshold = node.evalParm('threshold')
```

### Groups:

`myGrp=geo.createPrimGroup('name')` - Create group   
`group.destroy()` - Delete group, leaving contents intact  

Add Point to group:
```python
point=geo.createPoint()
myGrp=geo.createPointGroup('name')
myGrp.add(point)
```
Iterate group:
```python
groups = geo.primGroups()
for group in groups:
    print group.name
```

### Attributes:

`points[index].setAttribValue("Cd",(1.0,1.0,1.0))` - Set attribute
`redVal=point.attribValue("Cd")[0]` - Get attribute:

###  Delete primitives
```
deleteList=[]
for i in boundingGrp.prims():
    deleteList.append(i)
geo.deletePrims(deleteList)
```

### Import operator
```python
weightDict={"plane": 150, "car": 2, "house": 400, "banana":0.2}
sortedDict = sorted(weightDict.items(), key=operator.itemgetter(1),reverse=True)
```
### Arrays
```python
t = n.children() # tablica dzieci noda
t[0]
t[1]
....
```

```python
for c in n.children():
     print.name()
```

### Function:
Create function (define)
```python
def childrenOfNode(node):
	result = []
	for c in node.children():
		result.appnd(c)
		result += childrenOfNode(c)
	return result 
```
Call defined fn by calling var: n with (node):
```python
childrenOfNode(n) 
childrenOfNode(hou.node('/obj/adress'))
```

### UI

`hou.ui.displayMessage("hello")` #display popup 
`print p.selectPosition()` - print location of click in the node editor  network 

create new node with box on the position under mouse 
```python
p = hou.ui.paneTabOfType (hou.paneTabType.NetworkEditor)
position = p.selectPosition() #position clicked
new_node = p.pwd().createNode("box") #posWorkDir
new_node.setPosition(position) 
```


### swap $HIP to $JOB
NickD
```python
def hipToJob():
    for node in hou.node("/").allSubChildren():
        if node.type().name()=="redshift::TextureSampler":
            fileJob = node.parm("tex0").rawValue().replace("$HIP","$JOB")
            node.parm("tex0").set(fileJob)
```


### Johny

```python
node = hou.pwd()
geo = node.geometry()

for shali in geo.points():
    print shali.number()
    node = hou.node('/obj/target%s' %int(shali.number()+1))
    pos = node.evalParmTuple('t')
    rot =node.evalParmTuple('r')
    shali.setPosition(pos)
    shali.setAttribValue("rot", rot)
```


 
### Expressions:
`frame()/4` - $F/4    
`time()` - $T  
`lvar("nameoflocalVAr")`  
`lvar("PT")` - $PT  

### External editor

If you find yourself editing a lot of python code, you might like the joy of Sublime or vi(m) to edit your files. Place your python code in $HOME/houdiniXX.X/scripts/python, for example as "test.py", then inside Houdini, drop a python node and do as follows:
```python 
import test
reload(test)
from test import *
```
