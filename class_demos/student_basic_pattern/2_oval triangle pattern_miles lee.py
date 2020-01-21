
# size(1000,1000)


# module = 250
# padding = 50

w = 2000
h = 2000
module = 250
padding = -70

size(w, h)

width = range(0, width(), module)
height = range(0, height(), module)


def draw(x, y, width, height):
    fill(random(), random(), 0.7, 0.9)
    oval(x, y, 500, 500)
    
    # polygon((x, y), (x, y+500), (x+500, y+500))
    # fill(0.7, random(), random(), 0.3)
    # polygon((x, y), (x, y+500), (x-500, y+500))
    # fill(random(), random(), 0.7, 0.6)
    # polygon((x, y), (x, y-500), (x+500, y-500))


def pattern():
    #enumerating through width list
    for x in width:
        for y in height:
            image = module - padding
            diff = padding/2
            draw(x+diff, y+diff, image, image)
                  
pattern()

# for p in range(6):
#     if p==0:
#         pattern()
#     else:
#        newPage()
#        pattern()

#saveImage("~/Documents/WASHU/WASHU 2019-2020/PROGRAMMING DESIGN/pattern_pattern_scale2.png")