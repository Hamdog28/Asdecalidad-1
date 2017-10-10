from .GestorPCA import GestorPCA
from .GestorMuestra import GestorMuestra

class Control:
    
    def __init__(self):
        self.gestor_pca = GestorPCA()
        self.gestor_muestra = GestorMuestra()
        
    def entrenamiento(self,cantidad_autovectores):
        self.gestor_muestra.cargar()
        self.gestor_pca.entrenamiento(self.gestor_muestra.muestra,cantidad_autovectores)
        return None

    def identificacion_sujeto(self,img):
        valor,sujeto = self.gestor_pca.identificacion_sujeto(img)
        return valor,sujeto

    def cargar_imagenes(self,direccion):
        self.gestor_muestra.cargar_imagenes(direccion)
        return None   

    def pruebas(self):
        self.gestor_pca.pruebas()
        return None
    
    def agregar_nuevo_sujeto(self):
        self.gestor_muestra.agregar_nuevo_sujeto()
        return None
    