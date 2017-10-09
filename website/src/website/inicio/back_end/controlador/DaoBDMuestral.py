import cv2
import os 
from ..modelo.Imagen import Imagen
from .Configuracion import Configuracion

class DaoDBMuestral:
    
    def __init__(self):
        self.nombres_carpetas = []
        
    def leer_carpetas(self):
        for filename in os.listdir(Configuracion.RUTA):
            self.nombres_carpetas.append(filename) 
        return None

    def leer_imagenes(self,sujeto):
        lista_img=[]
        nombres_archivos=os.listdir(Configuracion.RUTA+"/"+sujeto)        
        for nombre_archivo in nombres_archivos:
            img = cv2.imread(Configuracion.RUTA+"/"+sujeto+"/"+nombre_archivo)
            i=Imagen(img)
            i.vectorizar()
            lista_img.append(i)
        return lista_img

  

