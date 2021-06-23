#!/usr/bin/env python3
import PIL
import os 
from PIL import Image

dict = "/supplier-data/images/"
''' THIS PROGRAM WAS MEDE FOR THE LAST WEEK OF TE GOOGLE COURSE, CONVERTS THE .TIFF IMGS IN .JPG FORMAT EN RESIZE THEM'''
for filename in os.listdir(dict):
    if filename.endswith(".tiff"):
         path = dict + filename
         print(path)
         im = Image.open(path)
         im = im.resize((600,400))
         im_RGB = im.convert('RGB')         
         im_RGB.save(path.repalce('.tiff','.jpeg'))