import numpy as np
from .Clasificacion import Clasificacion

class DistanciaCentroide:

    def __init__(self,muestra):
        Clasificacion.__init__(self)
        self.muestra=muestra
        
    def clasificar(self,img,autoespacio,proyecciones):
        for i in self.muestra.sujetos:
            imagen = np.matrix(img.vector).T
            i.generar_submatriz()
            imagen = imagen - np.mean(np.matrix(i.submatriz), axis=1)
            imagen_proyectada = autoespacio.T * imagen
            distancia = proyecciones - imagen_proyectada
            distancia = np.power(distancia,2)
            distancia = np.sqrt(distancia)
            distancia_normalizada = np.linalg.norm(distancia, axis=0)
            Lista_similitudes = np.abs((distancia_normalizada / np.max(distancia_normalizada))-1 )
            similitud = np.mean(Lista_similitudes)
            indice = i
            print(indice.nombre, similitud)
        return 1,0
        