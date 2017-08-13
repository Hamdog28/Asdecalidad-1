from .imagen import imagen

class sujeto:
    def __init__(self,nombre):
        self.nombre=nombre
        self.imagenes=[]
        self.matriz=[]
            
    def agregarImagene(self,imagen):
        self.imagenes.append(imagen)
        