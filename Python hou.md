Where to use:
- Python Shell - Live code
- Python Source Editor - you can save  code and function / hou.session.myDefinedFunction()
- Digital Asset -
- Shelf Tool - scrpit section to write code Executed after shelf click



# Python:
`node = hou.pwd()` -    
`param = hou.ch("param")` - Read node parameter  
`bitmask = hou.ch("bitmask")` - Read node parameter   
`xBoundSize=lvar('SIZEX')` - Read local variables    

Assign objecto to var: foo
```python
foo = hou.node('/path')
foo.name #return name of object.

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
`redVal=point.attribValue("Cd")[0]` - Get attribute   

###  Delete primitives
```
deleteList=[]
for i in boundingGrp.prims():
    deleteList.append(i)
geo.deletePrims(deleteList)
```

### Arrays
```python
t = n.children() # tablica dzieci noda
t[0]
t[1]
....
```
### For Loop
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
# Class


### hou
- `hou.` is houdini python class. We can drop it in **expressions**:  
- see what params is passing `kwargs` (pthos dict to see what is avalable)


### hou.node
node in trees
```python
ball = hou.node('/obj/ball')

ball = setSelected(True) # select ball node
ball = isSelected() # give you a bool 
ball = type().name() # geo
ballTx = ball.parm("tx") # get val of parameter
ball.evalParm("tx") # give you val of parameter  in particular moment 
ball.setParms({"tx":3, "tx":2, "tx":1})

# get all parameters names in ball obj
for parm in ball.parms():
     print parm.name() 

# print all inputs of node 
mynode = hou.node('/obj/ball')
for input in mynode.inputs():
     print input

# print all outputs of node 
mynode = hou.node('/obj/ball')
for output in mynode.outputs():
     print output

# change which node input node
hou.node('/obj/nodetochange').setInput(0, hou.node('/obj.newnode'))

box = hou.node('/obj/ball').createNode("box","NewBoxName") # create node conected to parrent
box = ball.createNode("box","NewBoxName")
box.destroy 
```

`node = hou.node('.')` - getting a reference to the current node  
`hou.node('/path')` - object in class hou  
`geo = node.geometry()` - grabs the geometry data that is being fed into this node by calling its geometry() method    

Reference to this Python SOP via the node variable, we can use **evalParm(path)** to access each parameter  
```python
seed = node.evalParm('seed')
threshold = node.evalParm('threshold')
```
#### swap $HIP to $JOB
NickD
```python
def hipToJob():
    for node in hou.node("/").allSubChildren():
        if node.type().name()=="redshift::TextureSampler":
            fileJob = node.parm("tex0").rawValue().replace("$HIP","$JOB")
            node.parm("tex0").set(fileJob)
``` 
### hou.parm 
behaviour of all parameters 
```python
ty = hou.parmTuple('/obj/ball/t')[1] 
ty.name() # 'ty'
ty.path() # 'obj/ball/ty'
ty.eval() # 1.11111
ty.evalAtFrame(10) # 1.44324

t = ty.tuple() # list of all params 
len(t) # how many params have list

for parm in t: 
		print parm.name() # tx, ty, tz

ry.hou.paramTuple('/obj/ball/r')[1]
ry.deleteAllKeyFrames()
ry.set(25) # will set rotationy in 25
ry.setRxpression("2*frame()") # now will rotate in time 
ry.expression() # will give you: '2*frame()'

rx = hou.parmTuple('/obj/ball/r')[0]
keys = rx.keyframes() 

# print keys
for key in keys:
	print key  

# will print expression animation we set earlier 
for key in ry.keyframes():
	print key 

ry.asCode() # will print code 
```

### hou.Obj.Node

```python
```
### hou.Geometry

```python
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

### Import

```python 
import test
reload(test)
from test import *
```

# Expressions:

`frame()/4` - $F/4    
`time()` - $T  
`lvar("nameoflocalVAr")`  
`lvar("PT")` - $PT  

10/frame() * sin(frame()/10.0)
(1+ch("../ty"))/2

