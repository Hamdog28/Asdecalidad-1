from .Facade import Facade

class FacadeAdministadror(Facade):
    
    def __init__(self):
        Facade.__init__()
    
    def entrenamiento(self,cantidad_autovectores):
        Facade.entrenamiento(self, cantidad_autovectores,0)
        return None

    def identificacion_sujeto(self):
        Facade.identificacion_sujeto(self)
        return None

    def cargar_imagenes(self,direccion):
        Facade.cargar_imagenes(self, direccion)
        return None   

    def pruebas(self):
        Facade.pruebas(self)
        return None
    
    def agregar_nuevo_sujeto(self):
        return None