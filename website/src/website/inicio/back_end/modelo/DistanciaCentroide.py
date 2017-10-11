import numpy as np
from .Clasificacion import Clasificacion

class DistanciaCentroide:

    def __init__(self,muestra):
        Clasificacion.__init__(self)
        self.muestra = muestra
        
    def clasificar(self,img,autocaras,proyecciones):
        valores_distancias = []
        sujetos = []
        for i in self.muestra.sujetos:
            imagen = np.matrix(img.vector).T
            i.generar_submatriz()
            imagen = imagen - np.mean(np.matrix(i.submatriz), axis=1)
            imagen_proyectada = autocaras.T * imagen
            distancia = proyecciones - imagen_proyectada
            distancia_normalizada = np.linalg.norm(distancia)
            valores_distancias.append(np.mean(distancia_normalizada))
            sujetos.append(i)
        
        valor = min(valores_distancias)
        indice = valores_distancias.index(valor)
        return valor,sujetos[indice].nombre
        