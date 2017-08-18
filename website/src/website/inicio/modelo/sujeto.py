
import numpy as np
from .imagen import imagen


class sujeto:
    def __init__(self,nombre):
        self.nombre=nombre
        self.imagenes=[]
        self.matriz=[]
            
    def agregarImagene(self,imagen):
        self.imagenes.append(imagen)
        
    def generarMatriz(self):
        
        for i in self.imagenes[0].vector:
            self.matriz.append([])
        
        for i in range(len(self.imagenes)):
            for j in range(len(self.imagenes[i].vector)):
                self.matriz[j].append(self.imagenes[i].vector[j])
                 
        return self.matriz
 