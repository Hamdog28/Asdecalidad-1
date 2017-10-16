import cv2
import os 
from ..modelo.Imagen import Imagen
from .Configuracion import Configuracion

class DaoDBMuestral:
    
    def __init__(self):
        '''
        Constructor
        '''
        None
        
    def leer_carpetas(self):
        """
        leer_carpetas
        @details lee las nombres de las carpetas dentro del directorio seleccionado
        
        @rtype: []
        @return: nombres_carpetas listado con los nombres de las carpetas 
        """
        nombres_carpetas = []
        for filename in os.listdir(Configuracion.RUTA):
            nombres_carpetas.append(filename) 
        return nombres_carpetas

    def leer_imagenes(self,sujeto):
        """
        leer_imagenes
        @details lee todas las imagenes del directorio senalado
        
        @type 1: String
        @param 1: sujeto
        
        @rtype: []
        @return: lista de imagenes 
        """
        lista_img = []
        nombres_archivos = os.listdir(Configuracion.RUTA+"/"+sujeto)        
        for nombre_archivo in nombres_archivos:
            img = cv2.imread(Configuracion.RUTA+"/"+sujeto+"/"+nombre_archivo)
            i = Imagen(img)
            i.vectorizar()
            lista_img.append(i)
        return lista_img

  

