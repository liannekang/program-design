

def swatch(color):
    r, g, b, a = color
    lighter = (r*.2, g, b, a)
    darker = (r*.8, g, b, a)
    return lighter, darker

for p in range(5):
    if p != 0:
        newPage()
    
    if p == 0:
        color = (.3,.5,0,1)
    else:
        color = (1/p,.5,0,1)


    lighter, darker = swatch(color)

    fill(*lighter)
    fill(*color)
    rect(0,0,width()/3,height())


    rect(width()/3,0,width()/3,height())

    fill(*darker)
    rect(width()/3*2, 0,width()/3,height())
    