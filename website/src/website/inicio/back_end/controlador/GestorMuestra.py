from .DaoBDMuestral import DaoDBMuestral
from ..modelo.Muestra import Muestra
from ..modelo.Sujeto import Sujeto

class GestorMuestra:
    
    def __init__(self):
        self.BDmuestral=DaoDBMuestral()
        self.muestra=Muestra()
    
    def cargar(self):
        self.BDmuestral.leer_carpetas()
        lista_sujetos=[]
        for i in self.BDmuestral.nombres_carpetas:
            s=Sujeto(i)
            s.imagenes=self.BDmuestral.leer_imagenes(i)
            lista_sujetos.append(s)
        self.muestra.sujetos=lista_sujetos
        return None

    def cargar_imagenes(self,direccion):
        return None   
    
    def agregar_nuevo_sujeto(self):
        return None