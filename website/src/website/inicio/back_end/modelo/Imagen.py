import numpy as np
import cv2
from ..controlador.Configuracion import Configuracion

class Imagen:
    
    def __init__(self,img):
        self.img = img
        self.vector = []

    def vectorizar(self):
        """
        vectorizar
        @details vectoriza la imagen
        
        @rtype: None
        @return: None 
        """
        img = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        self.vector = img.T.flatten().T
        return None

    def leer_imagen(self,directorio):
        """
        leer_image
        @details permite leer una imagen dado un directorio
        
        @type 1: String
        @param 1: directorio
        
        @rtype: None
        @return: None 
        """
        self.img = cv2.imread(directorio)
        self.cambiar_dimenciones_imagen(Configuracion.IMG_X, Configuracion.IMG_Y)
        self.vectorizar()
        return None

    def img_a_gris(self):
        """
        img_a_gris
        @details permite convetir la imagen a tonalidades de gris
        
        @rtype: None
        @return: None 
        """
        self.img=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        return None   

    def cambiar_tamano_porcentual_imagen(self,porcentajeX,porcentajeY):
        """
        cambiar_tamano_porcentual_imagen
        @details permite cambiar el tamano de la imagen dado un porcentaje
        
        @type 1: Int
        @param 1: porcentajeX

        @type 2: Int
        @param 2: porcentajeY
        
        @rtype: None
        @return: None 
        """
        self.img = cv2.resize(self.img, (0,0), fx = porcentajeX, fy = porcentajeY)
        return None

    def cambiar_dimenciones_imagen(self,tamanoX, tamanoY):
        """
        cambiar_dimenciones_imagen
        @details permite cambiar el tamano de la imagen
        
        @type 1: Int
        @param 1: tamanoX

        @type 1: Int
        @param 1: tamanoY
                
        @rtype: None
        @return: None 
        """
        self.img = cv2.resize(self.img, (tamanoX, tamanoY))
        return None    
    