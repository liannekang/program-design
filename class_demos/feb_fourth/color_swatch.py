
color = (1,1,1,1)

def swatch(color):
    r, g, b, a = color
    lighter = (r*.2, g, b, a)
    darker = (r*.8, g, b, a)
    return lighter, darker

lighter, darker = swatch(color)

fill(*lighter)
fill(*color)
rect(0,0,width()/3,height())


rect(width()/3,0,width()/3,height())

fill(*darker)
rect(width()/3*2, 0,width()/3,height())
    