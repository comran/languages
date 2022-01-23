from PIL import Image
import sys
import os

im = Image.open(sys.argv[1])

width, height = im.size
aspect = width / height
width = 1000
height = int(width / aspect)
im = im.resize((width, height))
filename, extension = os.path.splitext(os.path.basename(sys.argv[1]))
im.save("../" + filename + extension)
