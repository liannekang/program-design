from random import random

CANVAS = 1000
size(CANVAS, CANVAS)

def draw(x, y, width, height, rotationCenter):
    rotate(10, rotationCenter)
    oval(x, y, width, height)


def pattern(x, y, size, rotationCenter):
    if (size < CANVAS / 4):
        return
    
    stroke(random(), random(), random()) 
    rotationNum = 0
    while rotationNum < 36:
        draw(x, y, size, size, rotationCenter)
        rotationNum += 1
        
    print(x)
    print(y)
    print(size)
    print(rotationCenter)
    print("---------------")

    # right
    pattern(x, y+size/4, size/2,(x+size/2, CANVAS/2))
    
    # bottom
    pattern(x, y-size/4, size/2, (CANVAS/2, y))
    
    # left
    pattern(0, y+size/4, size/2,(x-size/2, CANVAS/2))
    
    # top
    pattern(x, 2*y + size/4, size/2,(CANVAS/2, CANVAS - CANVAS/4))

    # center
    pattern(x, y+size/4, size/2,(CANVAS/2, 2*y))


fill(0, 0, 0)
rect(0, 0, width(), height())

# fill(None, None, 0)
pattern(CANVAS/2, CANVAS/2 - CANVAS/4, CANVAS/2, (CANVAS/2, CANVAS/2))
    