

# Python:
object in class hou
```
hou.node('/path')
```
Read node parameter:
```
param = hou.ch("param")
```
Assign objecto to var: n
```
n = hou.node('/path')
n.name // return name of object.
```

Access local variables:
```
xBoundSize=lvar('SIZEX')
```

### Groups:
Create group:
```
myGrp=geo.createPrimGroup('name')
```
Add Point to group:
```
point=geo.createPoint()
myGrp=geo.createPointGroup('name')
myGrp.add(point)
```
Iterate group:
```
groups = geo.primGroups()
for group in groups:
    print group.name
```
Delete group, leaving contents intact:
```
group.destroy()
```
### Attributes:
Set attribute:
```
points[index].setAttribValue("Cd",(1.0,1.0,1.0))
```
Get attribute:
```
 redVal=point.attribValue("Cd")[0]
 ```
### Delete primitives
```
deleteList=[]
for i in boundingGrp.prims():
    deleteList.append(i)
geo.deletePrims(deleteList)
```

### Import operator
```
weightDict={"plane": 150, "car": 2, "house": 400, "banana":0.2}
sortedDict = sorted(weightDict.items(), key=operator.itemgetter(1),reverse=True)
```
### Arrays
```
t = n.children() // tablica dzieci noda
t[0]
t[1]
....
```

```
for c in n.children():
     print.name()
```

### Function:
```python
def childrenOfNode(node):
	reylt = []
	for c in node.children():
		result.appnd(c)
		result += childrenOfNode(c)
	return result 
```
