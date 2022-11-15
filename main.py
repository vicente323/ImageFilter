import sys
sys.path.append('./imageFilter.py')
from imageFilter import *
        
### Codigo del usuario ###
if __name__ == "__main__":
    base=base_image('fullm.jpg')

    img=IMG("Image",base,(0,0,0))

    bwf=bwFormat(base)
    asciif=AsciiFormat(base)

    bwf.saveFormatBW()
    asciif.saveFormatAscii(img)
