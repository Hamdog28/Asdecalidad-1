import numpy as np
from .Clasificacion import Clasificacion

class DistanciaCentroide:

    def __init__(self,muestra):
        Clasificacion.__init__(self)
        self.muestra = muestra
        
    def clasificar(self,img,autocaras,proyecciones):
        """
        clasificar
        @details permite clasficar la imagen por el metodo de la distancia de los centroides
        
        @type 1: Imagen
        @param 1: img

        @type 2: np.matriz()
        @param 2: autocaras

        @type 3: np.matriz()
        @param 3: proyecciones
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
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
        """
        789136.936619
        467760.314293
        549642.457243
        436704.237006
        435769.09093
        
        """
        if valor< 400000:
            return valor,sujetos[indice].nombre
        else:
            return valor,"no identificado"
        
