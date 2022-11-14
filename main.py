
from PIL import Image, ImageDraw
import clipboard
from abc import ABC, abstractmethod
ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# We set an array of charactes as our material for recreate the image, we ordered from the smallest to the bigest 
# (r,g,b)= pixel

# pixel_brightness = r + g + b

# rgbPixels=(255,255,255)


# max_brightness=255*3

# brightness_weight = len(ascii_characters_by_surface) / max_brightness
# index = int(pixel_brightness * brightness_weight) - 1

# print(brightness_weight)


class imagenGenerica(ABC):
    @abstractmethod
    def clonar(self):
        pass


def pxToRgb(pixel):
    (r,g,b)=pixel
    brightness=r+g+b 
    char=0
    print(f"Brillo:{brightness}")
    print(f"Pixel:{pixel} len: {len(ascii_characters_by_surface)}")
    # 255 * 3 due to we can set in 255 the 3 RGB values individualy R - G - B

    try:
        char=len(ascii_characters_by_surface)/(255*3) 
    except:
        print("final")
    index=int(brightness*char)-1
    return ascii_characters_by_surface[index]

def save_as_text(ascii_art):  
    with open("image.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
        file.close()

def cpyToClipboadr(txt):
    strToSave=''
    for y in range(0,len(txt)-1):
        strToSave+=txt[y]+'\n'

    clipboard.copy(strToSave)   


def createNewImage():
    
    img = Image.new('RGB', (250*6, 250*10), color = (0, 0, 0))
    return(img)

    

#ascii_characters_by_surface = "'`^.,:;Il!i~+_-?][FB1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
asciiIMG=[]
image=Image.open('ahegao.jpg')

image = image.resize((250, 250))
(width,height)=image.size

print(f"{width}:{height}")
img=createNewImage()

for y in range(0,height):
    line=''
    for x in range(0, width):
        px=image.getpixel((x,y))
        line += pxToRgb(px)
    asciiIMG.append(line)

save_as_text(asciiIMG)
cpyToClipboadr(asciiIMG)


d = ImageDraw.Draw(img)
d.text((10,10), asciiIMG[0], fill=(255,255,0))

for x in range(0,len(asciiIMG)):
    d = ImageDraw.Draw(img)
    d.text((10,10*x), asciiIMG[x], fill=(255,255,0))
    
img.save('newIMG.png')
print(asciiIMG[0])
