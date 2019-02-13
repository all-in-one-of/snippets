

# Python:
object in class hou
```python
hou.node('/path')
```
Read node parameter:
```python
param = hou.ch("param")
```
Assign objecto to var: n
```python
n = hou.node('/path')
n.name // return name of object.
```

Access local variables:
```python
xBoundSize=lvar('SIZEX')
```

### Groups:
Create group:
```python
myGrp=geo.createPrimGroup('name')
```
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
Delete group, leaving contents intact:
```python
group.destroy()
```
### Attributes:
Set attribute:
```python
points[index].setAttribValue("Cd",(1.0,1.0,1.0))
```
Get attribute:
```python
 redVal=point.attribValue("Cd")[0]
 ```
### Delete primitives
```python
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
t = n.children() // tablica dzieci noda
t[0]
t[1]
....
```

```python
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
