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
        self.muestra = muestra
        return None
    
    def entrenamiento(self,cantidad_autovectores):
        self.muestra.generar_matriz()
        self.muestra.generar_matriz_covarianza()
        self.muestra.calcular_autovalores_autovectores()        
        self.proyeccion.proyectar(self.muestra,cantidad_autovectores)
        return None

    def identificacion_sujetos(self,img):
        clasificacion=DistanciaCentroide(self.muestra)
        valor,sujeto=clasificacion.clasificar(img,self.proyeccion.autocaras,self.proyeccion.proyecciones)
        return valor,sujeto

    
    