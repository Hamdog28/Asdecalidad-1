import numpy as np
from .Muestra import Muestra
from .Clasificacion import Clasificacion
from .KVecinos import KVecinos
from .DistanciaCentroide import DistanciaCentroide
from .Proyeccion import Proyeccion
class PCA:
    
    def __init__(self):
        self.proyeccion = Proyeccion()
        self.clasificacion = Clasificacion()
        self.muestra = None

    def agregar_muestra(self,muestra):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        self.muestra=muestra
        return None
    
    def entrenamiento(self,cantidad_autovectores):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        try:
            self.muestra.generar_matriz()
            self.muestra.generar_matriz_covarianza()
            self.muestra.calcular_autovalores_autovectores()        
            self.proyeccion.proyectar(self.muestra,cantidad_autovectores)
            return True
        except:
            return False
                 

    def identificacion_sujetos(self,img):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        clasificacion=DistanciaCentroide(self.muestra)
        valor,sujeto=clasificacion.clasificar(img,self.proyeccion.autocaras,self.proyeccion.proyecciones)
        return valor,sujeto

    
    