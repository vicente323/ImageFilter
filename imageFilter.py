
from PIL import Image, ImageDraw,ImageEnhance
from abc import ABC, abstractmethod
from copy import deepcopy, copy

ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# We set an array of charactes as our material for recreate the image, we ordered from the smallest to the bigest 

# 1.- Interface (Componente)  Interface para los wrappers
class filter(ABC):
    @abstractmethod
    def saveFormat(self) -> str:
        pass
class imagenGenerica(ABC):
    @abstractmethod
    def clonar(self):
        pass
# 2.- Componentes Concretos Estos son a los que se les puede poner el filter
class base_image(filter):
    #Clase singleton
    _INSTANCIA = None
    def __init__(self,src) -> None:
        if base_image._INSTANCIA == None:
            self.usuario = src
            base_image._INSTANCIA = self
            print(f'-I- {src}')
        else:
            print('-E- Ya tienes una imagen abierta')

        self.src=src
        self.ascii= []
        self.image= Image.open(f'./IMG/{src}')
        self.size = self.image.size

    def saveFormat(self) -> str:
        return self.image

class IMG(imagenGenerica):
    def __init__(self,name,base_image:base_image,*args):
        self.name=name
        self.RGB=args
        self.img=Image.new('RGB', (base_image.size[0]*6, base_image.size[1]*10), color = args)
    
    def save_into_new(self):


        self.img.save('newIMG.png')

    def clonar(self):
        return copy

# 3.- Clase Decoradora Encargado de definir la estructura del wrapper
class Decorator(filter): 

    def __init__(self, filter) -> None:
        self._format = filter

    @property
    def format(self):
        return self._format
    



# 4.- Decoradores Concreto  donde ponemos nuestras funcionalidades
class AsciiFormat(Decorator):

    def pxToRgb(self,pixel):

        '''Method called by toAscii Method'''
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
    


    def toAscii(self,imageToSave:IMG):
        '''format method'''
        for y in range(0,self.format.size[1]):
            line=''
            for x in range(0, self.format.size[0]):
                px=self.format.image.getpixel((x,y))
                line += self.pxToRgb(px)
            self.format.ascii.append(line)
        
        for x in range(0,len(self.format.ascii)):
            d = ImageDraw.Draw(imageToSave.img)
            d.text((10,10*x), self.format.ascii[x], fill=(255,255,0))
        return imageToSave.save_into_new()
    
    def saveFormatAscii(self,imageToSave:IMG):

        return self.toAscii(imageToSave)
    
    def saveFormat(self) -> str:
        return super().saveFormat()
class bwFormat(Decorator):
    def toBw(self):
        img = self.format.image
        self.img=img.convert("L")
        self.img.save('Bw.png')

    def saveFormatBW(self):
        self.toBw()
    def saveFormat(self) -> str:
        return super().saveFormat()
