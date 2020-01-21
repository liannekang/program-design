from random import random

w = 1000
h = 1000
module = 20
padding = 5

size(w,h)

width = range(0,width(), module)
height = range(0,height(), module)

def draw(x,y, width, height):
    stroke(1, 1, 1, 1)
    strokeWidth(1)
    fill(.5, .5, random(), 1)
    oval(x, y, width, height)


def pattern():
   for i, x in enumerate(width):
       for y in height:
           image = module - padding
           draw(x, y, image, image)
      
def overlaypattern():
   for i, x in enumerate(width):
       for y in height:
           yy = y
           xx = x
           if i % 2 == 0:
               yy = y + module/2
               xx = x + module/2
           image = module - padding
           draw(xx, yy, image, image)                               
                
def overlaypatterntwo():
   for i, x in enumerate(width):
       for y in height:
           yy = y
           xx = x
           if i % 2 == 0:
               yy = y + module/2
               xx = x + module/2
           image = module - padding
           draw(xx, yy, image * 2, image * 2)                               
                
                
                
def background():
    fill(1, 1, 1, 1)
    rect(1,1,w,h)
    

    
background()
overlaypatterntwo()
pattern()
overlaypattern()





