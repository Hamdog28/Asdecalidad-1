import numpy as np
import cv2
from ..controlador.Configuracion import Configuracion

class Imagen:
    
    def __init__(self,img):
        self.img = img
        self.vector = []

    def vectorizar(self):
        for i in cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY):         
            self.vector=np.concatenate((self.vector,i),axis=0)
        return None

    def leer_imagen(self,directorio):
        self.img = cv2.imread(directorio)
        self.cambiar_dimenciones_imagen(Configuracion.IMG_X, Configuracion.IMG_Y)
        self.vectorizar()
        return None

    def img_a_gris(self):
        return cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        return None   

    def cambiar_tamano_porcentual_imagen(self,porcentajeX,porcentajeY):
        self.img=cv2.resize(self.img, (0,0), fx = porcentajeX, fy = porcentajeY)
        return None

    def cambiar_dimenciones_imagen(self,tamanoX, tamanoY):
        self.img=cv2.resize(self.img, (tamanoX, tamanoY))
        return None    
    