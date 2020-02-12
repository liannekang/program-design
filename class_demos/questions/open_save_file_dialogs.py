# See https://github.com/robotools/vanilla/blob/master/Lib/vanilla/dialogs.py
from vanilla.dialogs import getFile, putFile

# Get a gif or png image
filePath = getFile(messageText="Get a file", fileTypes=['gif', 'png'])
print("filePath:")
print(filePath)

# Draw image on canvas (dumb I know)
image(filePath[0], (0, 0))

# Save the file, only allow it to be a PDF or Gif, if no file extension is
# given, defaults to PDF as it's first in the fileTypes list
savePath = putFile(messageText="Select a spot to save a file", fileTypes=['pdf', 'gif'])
print("savePath:")
print(savePath)

saveImage(savePath)
