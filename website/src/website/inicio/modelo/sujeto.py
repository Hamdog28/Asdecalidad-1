import numpy as np
from modelo.imagen import imagen


class sujeto:
    '''
    Clase encargada de representar a los sujetos a quienes pertenecen las imagenes.
    '''
    def __init__(self,nombre):
        '''
        Constructor
        :param nombre: Nombre del sujeto.
        '''
        self.nombre=nombre
        self.imagenes=[]
        self.matriz=[]
            
    def agregarImagene(self,imagen):
        '''
        Agrega una imagen a la lista de imagenes del sujeto.
        :param imagen: Imagen a agregar.
        '''
        self.imagenes.append(imagen)
