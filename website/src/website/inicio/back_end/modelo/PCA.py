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
        agregar_muestra
        @details permite agregar la muestra que sera entrenada
        
        @type 1: Muestra
        @param 1: muestra
        
        @rtype: None
        @return: None 
        """
        self.muestra=muestra
        return None
    
    def entrenamiento(self,cantidad_autovectores):
        """
        Entrenamiento
        @details utiliza la mustra y la cantidad de autovectores para generar el entrenamiento
        
        @type 1: int
        @param 1: cantidad_autovectores
        
        @rtype: Boolean
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
        
        @rtype: Int,String
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        clasificacion=DistanciaCentroide(self.muestra)
        valor,sujeto,por=clasificacion.clasificar(img,self.proyeccion.autocaras,self.proyeccion.proyecciones)
        return valor,sujeto,por


    
    