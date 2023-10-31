import math
from PIL import Image
import os

#fullimage = Image.open('hiraganachart.jpg')

#numchops = 3 # this number squared is the number of sections created

def imagechop(imagepath, numchops: int):
    
    numchops = int(math.sqrt(int(numchops)))
    fullimage = Image.open(imagepath)
    chopw = fullimage.width/numchops
    choph = fullimage.height/numchops

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    for i in range(numchops): # for each row
        for j in range(numchops): # for each column
            
            top = i*choph
            left = j*chopw 

            chop = fullimage.crop((left, top, left+chopw-1, top+choph-1))
            chop.save(desktop+"/chop_{}_{}.jpg".format(i, j))



