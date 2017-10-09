import numpy as np
from .Clasificacion import Clasificacion

class DistanciaCentroide:

    def __init__(self,muestra):
        Clasificacion.__init__(self)
        self.muestra=muestra
        
    def clasificar(self,img,autocaras,proyecciones):
        for i in self.muestra.sujetos:
            imagen = np.matrix(img.vector).T
            i.generar_submatriz()
            imagen = imagen - np.mean(np.matrix(i.submatriz), axis=1)
            imagen_proyectada = autocaras.T * imagen
            distancia = proyecciones - imagen_proyectada

            distancia_normalizada = np.linalg.norm(distancia)

            similitud = np.mean(distancia_normalizada)
            sujeto = i
            print(sujeto.nombre, similitud)
        return 1,0
        