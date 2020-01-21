from random import random

w = 4000
h = 5000
module = 55
padding = 50
size(w,h)

fill(0, 0, 0)
rect(0, 0, width(), height())

width = range(0, width(), module)
height = range(0, height(), module)

def draw(x, y, width, height):
    fill(0,0,0)
    stroke(1,1,1)
    strokeWidth(x/400)
    oval(sqrt(x)*90, sqrt(y)*90, 400, 400)
    rotate(30,center=(w/2,h/2))

def pattern():
    for i, x in enumerate(width):
        for y in height:
            if i % 2 == 0:
                y = y+(module/2)
            image = module - padding
            d = padding/2
            draw(x+d, y+d, image, image)

pattern()