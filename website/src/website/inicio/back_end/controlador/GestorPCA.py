from .DaoBDPCA import DaoDBPCA
from ..modelo.Muestra import Muestra
from ..modelo.PCA import PCA
from ..modelo.Imagen import Imagen
class GestorPCA:
    
    def __init__(self):
        self.dao_db_pca = DaoDBPCA()
        self.pca = PCA()
    
    def entrenamiento(self,muestra,cantidad_autovectores):
        self.pca.agregar_muestra(muestra)
        self.pca.entrenamiento(cantidad_autovectores)
        return None

    def identificacion_sujeto(self,img):

        i,j=self.pca.identificacion_sujetos(img)
        return i,j 

    def pruebas(self):
        return None
    
    def agregar_nuevo_sujeto(self):
        return None