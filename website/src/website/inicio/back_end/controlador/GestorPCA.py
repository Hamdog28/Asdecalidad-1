from .DaoBDPCA import DaoDBPCA
from ..modelo.Muestra import Muestra
from ..modelo.PCA import PCA
from ..modelo.Imagen import Imagen
class GestorPCA:
    
    def __init__(self):
        self.dao_db_pca = DaoDBPCA()
        self.pca = PCA()
    
    def entrenamiento(self,muestra,cantidad_autovectores):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        self.pca.agregar_muestra(muestra)
        self.pca.entrenamiento(cantidad_autovectores)
        return None

    def identificacion_sujeto(self,img):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        valor,sujeto = self.pca.identificacion_sujetos(img)
        return valor,sujeto 

    def pruebas(self):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,String
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        return None
    
    def agregar_nuevo_sujeto(self):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        return None