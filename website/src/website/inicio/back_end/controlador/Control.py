from .GestorPCA import GestorPCA
from .GestorMuestra import GestorMuestra

class Control:
    
    def __init__(self):
        '''
        Constructor
        '''
        self.gestor_pca = GestorPCA()
        self.gestor_muestra = GestorMuestra()
        
    def entrenamiento(self,cantidad_autovectores,porcentaje_prueba):
        """
        entrenamiento
        @details Se encarga de solicitar la funcion de entrenamiento 
        
        @type 1: int
        @param 1: cantidad_autovectores
        
        @rtype: Boolean
        @return: True si se ejecuto correctamente
        """
        self.gestor_muestra.cargar(porcentaje_prueba)
        self.gestor_pca.entrenamiento(self.gestor_muestra.muestra,cantidad_autovectores)
        sujeto=[]
        for i in self.gestor_muestra.muestra.sujetos:
            for j in i.imagenes_prueba:
                x,y,z=self.gestor_pca.identificacion_sujeto(j)
                sujeto.append([y,z])
        return sujeto

    def identificacion_sujeto(self,img):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,String
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        valor,sujeto , por= self.gestor_pca.identificacion_sujeto(img)
        return valor,sujeto

    def cargar_imagenes(self,direccion):
        """
        cargar_imagenes
        @details Solicita la funcion de cargar imagenes
        
        @type 1: String
        @param 1: direccion
        
        @rtype: None
        @return: None 
        """
        self.gestor_muestra.cargar_imagenes(direccion)
        return None   

    def pruebas(self):
        """
        pruebas
        @details Solicita la funcion de realizar pruebas
        
        @rtype: None
        @return: None 
        """
        self.gestor_pca.pruebas()
        return None
    
    def agregar_nuevo_sujeto(self):
        self.gestor_muestra.agregar_nuevo_sujeto()
        return None
    