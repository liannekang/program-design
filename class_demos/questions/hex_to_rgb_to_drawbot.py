def isRGB(rgb):
    # Checks that the rgb value is a valid color
    
    # Check that the right number of values are given
    if len(rgb) != 3:
        print("Wrong number of values")
        return False
    
    # Check that the values are in the right range
    for v in rgb:
        if v < 0 or v > 255:
            print(f"Value out of range: {v}")
            return False
    return True

def hex_to_rgb(value):
    # Drop the leading '#' if present
    value = value.lstrip('#')
    lv = len(value)
    
    # Color hex values are either ff00cc or fc0, so check length
    if lv not in [3, 6]:
        print("Value isn't in range")
        return
    
    # Convert (grabbed from https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    # RGB should be a tuple in the format of:
    # (0, 255, 154)
    # Numbers range from 0 to 255
    
    if isRGB(rgb):
        # Convert to hex
        return '#%02x%02x%02x' % rgb
    
def color_to_drawbot(color, opacity=1):
    # Take a rgb or hex value, and a value (optional)
    # for opacity, return the color for DrawBot
    
    if opacity > 1 or opacity < 0:
        print("Opacity must be between 0 and 1")
        return
        
    if isinstance(color, str):
        color = hex_to_rgb(color)

    if isRGB(color):
        r, g, b = color
        return (r/255, g/255, b/255, opacity)
        
print(hex_to_rgb("#ffefcc"))
print(rgb_to_hex((255, 239, 204)))
print(color_to_drawbot("#ffefcc"))
print(color_to_drawbot((255, 239, 204)))