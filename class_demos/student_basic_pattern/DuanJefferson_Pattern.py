from random import random

size(1000,1000)
d = 200 #for diameter#

def seigaiha(x, y):
    #this first section allows for a main color and one randomly occurring accent color. fill and stroke can be switched out for different effect.#
    cValue = random()
    if cValue >=.3:
        fill(64/255, 64/255, 64/255, 1)
        stroke(0)
    else: #random accent#
        fill(242/255, 217/255, 53/255, 1)
        stroke(0)
    
    strokeWidth(4+(d/100))
    oval(x, y, d, d)
    for i in [1,2,3]:
        oval(x+(i*d/8), y+(i*d/8), d-(i*d/4), d-(i*d/4))

# seigaiha(0-d/2, 0-d/2)
w = range(0, width()+d, d)
h = range(height()+d, 0, -int(d/4))

for n,r in enumerate(h): #rows first#
    for c in w: #columns second#
        if n%2 == 0:
            seigaiha(c, r-d)
        else:
            seigaiha(c-d/2, r-d)