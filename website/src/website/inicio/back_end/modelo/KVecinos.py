import numpy as np
from .Clasificacion import Clasificacion

class KVecinos(Clasificacion):
    
    def __init__(self):
        Clasificacion.__init__(self)
    
    def clasificar(self,img,autoespacio,proyecciones):
        return 1,0
    
    