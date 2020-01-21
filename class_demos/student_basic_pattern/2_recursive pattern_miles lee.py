
# size(1000,1000)


# module = 250
# padding = 50

w = 1000
h = 1000
module = 100
padding = 20

size(w, h)

width = range(0, width(), module)
height = range(0, height(), module)


def recursion(xcenter, ycenter, radius):
    fill(.7, 0.1, random(), random())

    if radius <10:
        return
    else:
        #green
        fill(random(), 0.7, random(), 1)
        #red
        #fill(0.7, random(), random(), 1)
        #blue
        #fill(random(), random(), 0.7, 1)
        
        rect(xcenter, ycenter, radius, radius)
        recursion(xcenter, ycenter+radius, radius/2)
        recursion(xcenter+radius, ycenter, radius/2)
        recursion(xcenter-radius, ycenter, radius/2)
        recursion(xcenter, ycenter-radius, radius/2)


def pattern():
        for xcenter in enumerate(width):
            for ycenter in height:
                recursion(500, 500-padding, 200)
                
pattern()

# for p in range(6):
#     if p==0:
#         pattern()
#     else:
#        newPage()
#        pattern()
saveImage("~/Documents/WASHU/WASHU 2019-2020/PROGRAMMING DESIGN/pattern_recursiong.png")