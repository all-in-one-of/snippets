```If you find yourself editing a lot of python code, you might like the joy of Sublime or vi(m) to edit your files. Place your python code in $HOME/houdiniXX.X/scripts/python, for example as "test.py", then inside Houdini, drop a python node and do as follows:
import test
reload(test)
from test import *```
Group related:
Create group:
```myGrp=geo.createPrimGroup('name')```
Add Point to group:
```point=geo.createPoint()
myGrp=geo.createPointGroup('name')
myGrp.add(point)```
Iterate group:```
groups = geo.primGroups()
for group in groups:
    print group.name```
Delete group, leaving contents intact:```
group.destroy()```
Attributes```
Set attribute
points[index].setAttribValue("Cd",(1.0,1.0,1.0))```
Get attribute:```
 redVal=point.attribValue("Cd")[0]```
Delete primitives```
deleteList=[]
for i in boundingGrp.prims():
    deleteList.append(i)
geo.deletePrims(deleteList)```
Access local variables:```
xBoundSize=lvar('SIZEX')```
Read node parameter:
```
bitmask = hou.ch("bitmask")```
More or less Houdini unrelated:```
sort a dict, if needed into list of tuples```
import operator```
weightDict={"plane": 150, "car": 2, "house": 400, "banana":0.2}
sortedDict = sorted(weightDict.items(), key=operator.itemgetter(1),reverse=True)```