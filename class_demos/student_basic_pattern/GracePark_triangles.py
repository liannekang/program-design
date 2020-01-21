from random import random

w = 900
h = 1000
size (w, h)

origPoint = 45
firstPoint = origPoint
padding = 10
firstHeight = (firstPoint*2)-padding
height = firstHeight
idkImGuessing = 0
rightPoint = firstPoint*2
leftPoint = 0

#xConstant = ((origPoint/2)+firstHeight)-(padding*2)
xConstant = (origPoint*3)-(padding*2)

def pointDown():
    newPath()
    moveTo((firstPoint, idkImGuessing)) #bottom 
    lineTo((leftPoint, height)) #left 
    lineTo((rightPoint, height)) #right 
    closePath()
    fill(random(), random(), random(), 1)
    drawPath()

def pointUp():
    newPath()
    moveTo(((rightPoint+padding), height)) #top 
    lineTo(((firstPoint+padding), idkImGuessing)) #left 
    lineTo(((firstPoint+xConstant)-padding, idkImGuessing)) #right
    closePath()
    fill(random(), random(), random(), 1)
    drawPath()

length = int(w/(xConstant-padding))
rows = int(h/height)

for y in range(rows):
    for x in range(length):
        pointDown()
        pointUp()
        firstPoint += xConstant
        leftPoint += xConstant
        rightPoint += xConstant
    idkImGuessing += (firstHeight+padding)
    height += (firstHeight+padding)
    leftPoint = 0
    firstPoint = origPoint
    rightPoint = firstPoint*2
    if y%2 == 0:
        leftPoint -= (origPoint+padding)
        firstPoint += leftPoint
        rightPoint += leftPoint