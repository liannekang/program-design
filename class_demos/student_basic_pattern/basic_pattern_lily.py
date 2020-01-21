from random import random

w = 1000
h = 1000
module = 15
padding = 3

size(w, h)

width = range(0, width(), module)
height = range(0, height(), module)

def draw(x, y, width, height):
        fill(random(),.7,random(),1)
        oval(x, y, width, height)

def pattern():
    for i, x in enumerate(width):
        for y in height:
            fill(random(),.44,.9,.7)
            if i % 2 == 0:
                y = y+(module/2)
            image = module - padding
            d = padding/4
            oval(x+d, y+d, image, image)
            
            if i % 1 == 0:
                y = y+(module/2)
                fill(.44, random(),.66,.7)
            image = module - padding
            d = padding/10
            rect(x+d, y+d, image, image)
    
    for b, y in enumerate(height):
        for x in width:
            fill(random(),.44,.66,.7)
            if i % 2 == 0:
                y = y+(module/2)
            image = module - padding
            d = padding/3
            oval(x+d, y+d, image, image)


            
            
pattern()

