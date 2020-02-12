def myround(number, multiple=5):
    """
    x is the number to round
    base is the multiple to round to, default 5
    """
    return multiple * round(number/multiple)
x = 100
y = 100
size(2000,1000)

Variable([
    # create a variable called 'w'
    # and the related ui is a Slider.
    dict(name="x", ui="Slider",
                args=dict(
                # some vanilla specific
                # setting for a slider
                value=width()/2,
                minValue=0,
                maxValue=width())),
    dict(name="y", ui="Slider"),
    dict(name="w", ui="Slider"),
    # create a variable called 'h'
    # and the related ui is a Slider.
    dict(name="h", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=100,
                minValue=50,
                maxValue=300)),
    ], globals())

w = myround(w,10)
print(w)
oval(x,y,w,h)