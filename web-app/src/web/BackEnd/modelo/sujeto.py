import numpy as np
from .imagen import imagen

class sujeto:
    def __init__(self,nombre):
        self.nombre=nombre
        self.imagenes=[]

            
    def agregarImagene(self,imagen):
        self.imagenes.append(imagen)
        

 
        