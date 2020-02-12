"""
How to pull information out of fonts

This is going to get a bit technical!

A font file has a bit of meta-data about the font inside of it.
Some of this data is stored in a table called the OS/2 table (long story).
To get to that data, we need to read the font file and parse that data.

Luckily, we don't actually have to do much coding to do this, as Drawbot has
installed inside of it a very useful code package called fontTools. It can read
data from a font.

First step, load the fontTools font object with an import
"""

from fontTools.ttLib import TTFont

"""
The TTFont lets us open up a font into fontTools from a path, so we need to get
the path of the font we want to look at. Let's just pull a random font from our
system to open and look at. We'll be a bit tricky in pulling a random font, by
using the random package, so we'll need to import the 'choice' method:
"""

from random import choice

"""
'choice' will take a list and randomly pick one thing from the list.
'installedFonts()' gives a list of all the installed fonts, so all we have
to do is:
"""

f = choice(installedFonts())

"""
Now that we have a font, we need to get the path to the font.
Drawbot comes to the rescue here, with its 'fontFilePath()' method.
This method returns the path to the font that is set in drawbot, so
first we need to set Drawbot to use our randomly chosen font, then we can
set a variable, path, to be the path of the font.
"""

font(f)
path = fontFilePath()
print("Our font path:")
print(path)

"""
So far so good.

Now we need to get the fontTools version of the font file so that we can
lookup the data inside of it. To do so, we do this:
"""

fontToolsFont = TTFont(path)

# With 'fontToolsFont' we can get the OS/2 table for our info:
info = fontToolsFont["OS/2"]

"""
Now we can get info about our random font.

How heavy is this font? Each font file has a value for its weight, ranging
from 0 to 1000. A weight of 400 should be the Regular, a weight of 700 should
be Bold. (CSS folks, this is what is setting the font when you set the
font-weight parameter). That value in the OS/2 table is called 'usWeightClass':
"""

weight = info.usWeightClass
print("Our font’s weight value:")
print(weight)

"""
Is the font condensed? Wide? Regular? There is a value for this too:
'usWidthClass'. This value ranges from 1 to 9, with 5 being a normal width.
"""

width = info.usWidthClass
print("Our font’s width value:")
print(width)

"""
The specification for the OS/2 table defines descriptors for each value.
You can make a dictionary to look up what each value means, like so:
"""

widths = {
    1: "Ultra-condensed",
    2: "Extra-condensed",
    3: "Condensed",
    4: "Semi-condensed",
    5: "Medium (normal)",
    6: "Semi-expanded",
    7: "Expanded",
    8: "Extra-expanded",
    9: "Ultra-expanded"
}

print("Our font’s width value name:")
print(widths[width])

"""
The weight value should be accurate to the font, and usually the width value
too. Because humans are setting these values, sometimes they aren't right
(sometimes for reasons, sometimes it's just an error —looking at you DAFont
font files). Just know that.

If you want to find out the foundry that made a font, there is a bit of data
for that too. Foundries usually have a registered foundry code (a list of this
is here: https://docs.microsoft.com/en-us/typography/vendors/). Yes, Agyei
Archer (who is going to skype into our class has foundry code !666, cheeky
devil).
"""

# To get a fonts's foundry code, you look up the 'achVendID'
foundryCode = info.achVendID
print("Our font’s vender code:")
print(foundryCode)

"""
The last bit of data that can be useful is this strange thing called Panose.
Panose was a system of classifying fonts so that if a laser printer didn't
have a font you wanted installed, it could substitute something that was close.
I know this sounds insane, but back in yea olden days, sending fonts over a
network to a printer was slow, and printers had very little memory. Too many
fonts and a document wouldn't print, so printers had a set of fonts installed
in them that they could use when a document called for that font, or to match
a missing font.

This is still part of the font specification, and some software still uses
them, so foundries often (but not always) set these values. We'll look at the
two that were asked about: if something is Serif or Sans, and what the contrast
of the font is.
"""

# First we need to get the panose values, that's easy:
panose = info.panose

"""
if we print panose, we'll see that it's something we haven't see yet in
class, an object
"""

print("Our font’s panose values:")
print(panose)

"""
We know it's an object, because it starts and ends in angle brackets < >
This just means that we need to get specific values out, like what we do
above. We are interested in 'bSerifStyle' and 'bContrast', the values for
serif and contrast.
"""

serif = panose.bSerifStyle
contrast = panose.bContrast

print("Our font’s panose serif value:")
print(serif)
print("Our font’s contrast serif value:")
print(contrast)

"""
We'll just get back a number for each value, which isn't helpful unless you
know what those numbers correspond to. I've pulled this out of the Panose
Specification for you, as that document is the definition of cray
(https://monotype.github.io/panose/).
"""

# Serif style
panose_serif = {
    0: "Any",
    1: "No Fit",
    2: "Cove",
    3: "Obtuse Cove",
    4: "Square Cove",
    5: "Obtuse Square Cove",
    6: "Square",
    7: "Thin",
    8: "Oval",
    9: "Exaggerated",
    10: "Triangle",
    11: "Normal Sans",
    12: "Obtuse Sans",
    13: "Perpendicular Sans",
    14: "Flared",
    15: "Rounded"
}

# Contrast
panose_contrast = {
    0: "Any",
    1: "No Fit",
    2: "None",
    3: "Very Low",
    4: "Low",
    5: "Medium Low",
    6: "Medium",
    7: "Medium High",
    8: "High",
    9: "Very High"
}

# With that, you can then look up what the values mean:
print("Our font’s serif and contrast from panose:")
print(panose_serif[serif])
print(panose_contrast[contrast])

"""
If you get back a value of 0 (Any), that means the foundry
was lazy and didn't really set a value, so Panose can't be
of much help.

This is a bunch of things, but hopefully it is somewhat clear.
if you get an error when running this script, it means that
the random font that was chosen is a TTC font (True Type Collection),
just run the script again.

If you want to dig more into the OS/2 table, the specification is here:
https://docs.microsoft.com/en-us/typography/opentype/spec/os2
And the bit of fontTools that deals with it is here:
https://github.com/fonttools/fonttools/blob/master/Lib/fontTools/ttLib/tables/O_S_2f_2.py
Unfortunately, fontTools doesn't have very good documentation, so reading
the code is the best way to figure out what to do.
"""
