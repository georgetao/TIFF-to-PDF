import sys
from PIL import Image
import numpy as np

############### COMMAND TO RUN IS 
############### python tiffToPdf.py [inputFile.tiff] [number of pages]

docName = sys.argv[1]
numPages = int(sys.argv[2])

outputFile = docName[:-5] + ".pdf"

im = Image.open(docName)


# Finding dimensions of each page
imArray = np.array(im)
l = imArray.shape[0]/numPages
w = imArray.shape[1]


# New variable that shows each individual page
im2 = im.crop((0, 0, w, l))
im2.save(outputFile)

for i in range(1, numPages):
    im2 = im.crop((0, l * (i), w, l * (i + 1)))
    im2.save(outputFile, append = True)
    
