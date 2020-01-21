from random import random

w = 900
h = 900
size (w, h)
checkBoard = 100

a = int(w/checkBoard)
opacVar = 10

def pattern(): 
    for x in range(a):
        ran1 = random()
        ran2 = random()
        ran3 = random()
        for y in range(a):
            if (x%2 == 0 and y%2 != 0) or (x%2 != 0 and y%2 == 0):
                fill(ran1, ran2, ran3, y/opacVar)
            else:
                fill (0)
            rect(x*checkBoard, y*checkBoard,checkBoard, checkBoard)

pattern()

# for p in range(10):
    # if p != 0:
        # newPage()
#saveImage("~/Desktop/why.gif")