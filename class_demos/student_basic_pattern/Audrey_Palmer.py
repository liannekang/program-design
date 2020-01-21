from random import random 

size (1000,1000)
module = 100
padding = 40

width=range(0,width(),100)
height=range(0,height(),100)

blendMode("multiply")
cmykFill(1, 0, 0, 0)
oval(200, 200, 300, 300)
cmykFill(0, 1, 0, 0)
rect(390, 390, 300, 300)

blendMode("multiply")
cmykFill(1, .25, 0, 0)
rect(100, 100, 200, 100)
cmykFill(0, 1, 0, 0)
oval(490, 290, 300, 300)

def pattern():
    for x in width:
        for y in height:
            stroke(random(),0,0,1)
            strokeWidth(10)
            fill(random(),random(),random(),1)
            
            image=module-padding
            d=padding/2
            rect(x+d,y+d,image,image)

           
pattern()
