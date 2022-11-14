
from PIL import Image, ImageDraw
import clipboard
from abc import ABC, abstractmethod
from copy import deepcopy, copy

ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# We set an array of charactes as our material for recreate the image, we ordered from the smallest to the bigest 

class imagenGenerica(ABC):
    @abstractmethod
    def clonar(self):
        pass

class base_image(imagenGenerica):
    def __init__(self,src) -> None:
        self.src=src
        self.ascii= []
        self.image= Image.open(f'./IMG/{src}')
        self.image= self.image.resize((250, 250))
        self.size = self.image.size
    def clonar(self):
        return copy(self)

    def pxToRgb(self,pixel):
        (r,g,b)=pixel
        brightness=r+g+b 
        char=0
        print(f"Brillo:{brightness}")
        print(f"Pixel:{pixel} len: {len(ascii_characters_by_surface)}")
        # 255 * 3 due to we can set in 255 the 3 RGB values individualy R - G - B
            
        try:
            char=len(ascii_characters_by_surface)/(255*3) 
        except:
            print("final de la imagen")
        index=int(brightness*char)-1
        return ascii_characters_by_surface[index]

    def parseToAscii(self):
        for y in range(0,self.size[1]):
            line=''
            for x in range(0, self.size[0]):
                px=self.image.getpixel((x,y))
                line += self.pxToRgb(px)
            self.ascii.append(line)

class IMG(imagenGenerica):
    def __init__(self,name,*args):
        self.name=name
        self.RGB=args
        self.img=Image.new('RGB', (250*6, 250*10), color = args)
    
    def save_into_new(self,base_image:base_image):
        print(f"{len(base_image.ascii)}: len")
        for x in range(0,len(base_image.ascii)):
            d = ImageDraw.Draw(self.img)
            d.text((10,10*x), base_image.ascii[x], fill=(255,255,0))
        self.img.save('newIMG.png')

    def clonar(self):
        return copy(self)

base=base_image('ahegao.jpg')
New_base=base.clonar()
base.parseToAscii()
img=IMG("Image",(0,0,255))
new_img=img.clonar()
img.save_into_new(New_base)

new_img.save_into_new(New_base)