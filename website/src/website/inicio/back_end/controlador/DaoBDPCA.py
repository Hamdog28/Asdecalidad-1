import numpy as np
from .Configuracion import Configuracion

class DaoDBPCA:
    
    def __init__(self):
        None
    
    def cargar(self):
        """
        cargar
        @details carga los detalles guardados
        
        @rtype: None
        @return: None 
        """
        return None

    def guardar(self,datos):
        """
        guardar
        @details guarda la informacion del entrenamiento
        
        @rtype: None
        @return: None 
        """
        np.savetxt(Configuracion.RUTA_2+'/autocaras.csv', datos.autocaras, delimiter=",")
        np.savetxt(Configuracion.RUTA_2+'/proyecciones.csv', datos.proyecciones, delimiter=",")

        return None
