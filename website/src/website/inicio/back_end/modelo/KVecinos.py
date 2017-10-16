import numpy as np
from .Clasificacion import Clasificacion

class KVecinos(Clasificacion):
    
    def __init__(self):
        Clasificacion.__init__(self)
    
    def clasificar(self,img,autoespacio,proyecciones):
        """
        clasificar
        @details permite el identificar la imagen por el metodo de KVecions mas cercanos
        
        @type 1: Imagen
        @param 1: img

        @type 2: np.matriz()
        @param 2: autocaras

        @type 3: np.matriz()
        @param 3: proyecciones
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        return 1,0
    
    