from .Control import Control

class Facade:
    
    def __init__(self):
        self.contol=Control()
    
    def entrenamiento(self,cantidad_autovectores):
        self.contol.entrenamiento(cantidad_autovectores)
        return None

    def identificacion_sujeto(self):
        self.contol.identificacion_sujeto()
        return None

    def cargar_imagenes(self,direccion):
        self.contol.cargar_imagenes(direccion)
        return None   

    def pruebas(self):
        self.contol.pruebas()
        return None
    
    def agregar_nuevo_sujeto(self):
        self.contol.agregar_nuevo_sujeto()
        return None