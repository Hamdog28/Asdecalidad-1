from .DaoBDMuestral import DaoDBMuestral
from ..modelo.Muestra import Muestra
from ..modelo.Sujeto import Sujeto
from warnings import catch_warnings

class GestorMuestra:
    
    def __init__(self):
        self.BDmuestral = DaoDBMuestral()
        self.muestra = Muestra()
    
    def cargar(self):
        """
        cargar
        @details agrega todos los sujetos
        
        @rtype: Boolean
        @return: True si se ejecuto correctamente la funcion False si no 
        """
        try:
            nombres_carpetas = self.BDmuestral.leer_carpetas()
            lista_sujetos = []
            for i in nombres_carpetas:
                s=Sujeto(i)
                s.imagenes = self.BDmuestral.leer_imagenes(i)
                lista_sujetos.append(s)
            self.muestra.sujetos=lista_sujetos
            return True
        except:
            return False

    def cargar_imagenes(self,direccion):
        """
        cargar_imagenes
        @details permite cargar las imagenes de un directorio
        
        @rtype: Boolean
        @return: True si se ejecuto correctamente la funcion False si no  
        """
        return False   
    
    def agregar_nuevo_sujeto(self):
        """
        agregar_nuevo_sujeto
        @details gestiona el agregar un nuevo sujeto
        
        @rtype: Boolean
        @return: True si se ejecuto correctamente la funcion False si no 
        """
        return False