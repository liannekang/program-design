from random import random

w = 1000
h = 1000
module = 100
padding = 0

size(w,h)

width = range(0, width(), module)
height = range (0, height(), module)

def draw(x, y, width, height):
    fill(random(),.6,random(),.7)
    oval(x, y, 100*random(), height) 
    fill(random(),.6,random(),.7)
    oval(x, y, width, 100*random())
    
def pattern():
    for x in width:
        for y in height:  
            if x == 1:
                y = y+(module/2)          
            image = module - padding
            d = padding/2
            draw(x+d, y+d, image, image)
            
pattern()






