from .DaoBDMuestral import DaoDBMuestral
from ..modelo.Muestra import Muestra
from ..modelo.Sujeto import Sujeto
from warnings import catch_warnings
import random 

class GestorMuestra:
    
    def __init__(self):
        self.BDmuestral = DaoDBMuestral()
        self.muestra = Muestra()
    
    def cargar(self,porcentaje_prueba):
        """
        cargar
        @details agrega todos los sujetos
        
        @rtype: Boolean
        @return: True si se ejecuto correctamente la funcion False si no 
        """
        try:
            nombres_carpetas = self.BDmuestral.leer_carpetas()
            nombres_carpetas = self.ordenar(nombres_carpetas)
            
            lista_sujetos = []
            for i in nombres_carpetas:
                s=Sujeto(i)
                s.imagenes = self.BDmuestral.leer_imagenes(i)
                
                numero_sujetos=int(len(s.imagenes)*porcentaje_prueba/100)
                for j in range(numero_sujetos):
                    quitar=random.randrange(0,len(s.imagenes)-1)
                    img=s.imagenes.pop(quitar)
                    s.imagenes_prueba.append(img)
                lista_sujetos.append(s)
            self.muestra.sujetos=lista_sujetos
            return True
        except:
            return False

    def ordenar(self,Lista):
        for i in range(len(Lista)):
            minimo = i
            for k in range(i+1, len(Lista)):
                if int(Lista[k][1:]) < int(Lista[minimo][1:]):
                    minimo = k

            temp = Lista[minimo]
            Lista[minimo] = Lista[i]
            Lista[i] = temp
        return Lista

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