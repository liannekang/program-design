im = ImageObject()

with im:
    size(200, 200)
    # draw something
    fill(1, 0, 0)
    rect(0, 0, width(), height())
    fill(1)
    fontSize(30)
    skew(30)
    text("Hello World", (10, 10))
im.colorInvert()
image(im, (10, 50))

