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
        
        imagen = np.matrix(img.vector).T        
        imagen = imagen - np.mean(self.muestra.matriz, axis=1)
        imagen_proyectada = autocaras.T * imagen
        
        distancia = np.power(np.sum(np.power( proyecciones - imagen_proyectada, 2)),0.5)
        
        v=np.min(distancia)
        for i in self.muestra.sujetos:
            imagen = np.matrix(img.vector).T
            i.generar_submatriz()
            imagen = imagen - np.mean(np.matrix(i.submatriz), axis=1)
            imagen_proyectada = autocaras.T * imagen
            distancia = proyecciones - imagen_proyectada
            distancia_normalizada = np.linalg.norm(distancia)
            valores_distancias.append(np.min(distancia_normalizada))
            sujetos.append(i)
        
        
        valor = min(valores_distancias)
        indice = valores_distancias.index(valor)
        valores_distancias = np.array(valores_distancias)
        valores_distancias = np.min(valores_distancias/ np.sum(valores_distancias))
        
        
        """
        789136.936619
        467760.314293
        549642.457243
        436704.237006
        435769.09093
        
        """

        return v,sujetos[indice].nombre,valores_distancias
       
