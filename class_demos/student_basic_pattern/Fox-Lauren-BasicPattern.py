from random import random

w = 1500
h = 1500
module = 150
padding = 20

size(w,h)



width = range(0,width(), module)
height = range(0, height(), module)

def draw(x,y,width,height):
    fill(1,1,1,0)
    stroke(random(), 0.5, random(), random())
    strokeWidth(60)
    oval(x,y,width,height)
    

def pattern():
    for i, x in enumerate(width):
        for y in height:
            image = module - padding
            d = padding/2
            draw(x+d,y+d,image,image)

pattern()

# for p in range(10):
#     if p != 1:
#         newPage()
        
# saveImage("~/Desktop/pattern.gif")