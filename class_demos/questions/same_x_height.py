fonts = installedFonts()
fill(1,0,0,.5)
for f in fonts:
    if "Slab" in f:
        font(f)
        s = 30
        fontSize(s)
        while fontXHeight() < 500:
            s += 1
            fontSize(s)
        text("x", (100,100))