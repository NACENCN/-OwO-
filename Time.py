import time

minutes = int(input("Enter the number of minutes to focus: "))
seconds = minutes * 60

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up!")


# -- coding utf-8 --

Clean keyFrames, zero Attrs, clean displays, clean unused skin,
Set camera in front,


import maya.cmds as cmds
import sys

all_curve = cmds.listRelatives(MotionSystem, ad=1, type=nurbsCurve)
geos = cmds.listRelatives(Geometry, ad=1, f=1, typ=mesh)

all_ctrl = []

for i in all_curve
    tempt = i[-5]
    if tempt[-1] is not S
        all_ctrl.append(tempt)
cmds.cutKey(all_ctrl, time=(1, 400), clear=True)
for i in all_ctrl
    try
        cmds.setAttr(i + .tx, 0)
        cmds.setAttr(i + .ty, 0)
        cmds.setAttr(i + .tz, 0)
        cmds.setAttr(i + .rx, 0)
        cmds.setAttr(i + .rx, 0)
        cmds.setAttr(i + .ry, 0)
        cmds.setAttr(i + .rz, 0)
        cmds.select(i, r=1)
    except
        pass

cmds.currentTime(1, update=1)
cmds.select(cl=1)

display = cmds.ls(ap=1, type=displayLayer)
display.remove(defaultLayer)
if len(display)  0
    cmds.delete(display)

cmds.undoInfo(state=0)

skined_geo = []
print(geos)
for i in geos
    if i[-5] == Shape
        temp_geo = i.split()
        skined_geo.append(temp_geo[-2])
print(skined_geo)
cmds.cutKey(skined_geo, time=(1, 400), clear=True)
for i in skined_geo
    cmds.skinCluster(i, e=1, rui=1)

cmds.undoInfo(state=1)

all_joint = cmds.ls(ap=1, type=joint)
head = none
for i in all_joint
    if Head in i
        head = i

head_trans = cmds.xform(head, q=1, ws=1, t=1)
came_height = head_trans[1]

cmds.setAttr(persp.tx, 0)
cmds.setAttr(persp.ty, came_height  0.7)
cmds.setAttr(persp.tz, came_height  2)
cmds.setAttr(persp.rx, 0)
cmds.setAttr(persp.ry, 0)
cmds.setAttr(persp.ry, 0)

cmds.file(save=1)
sys.stdout.write( File cleaned and Saved)
