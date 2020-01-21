from random import random

w = 2000
h = 2000
module = 100
padding = 50

size(w,h)

width = range(0,width(),module)
height = range(0,height(),module)

def draw(x,y,width,height):
    fill(random(),random(),random(),random())
    oval(x,y,width,height)

def pattern():
    for x in width:
        for y in height:
            image = module + padding*3
            draw(x,y,image,image)
            
pattern()