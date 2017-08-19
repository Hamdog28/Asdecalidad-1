import numpy as np
import cv2
from cv2 import WINDOW_NORMAL
import itertools
import os



from ..modelo.imagen import imagen

class DAOBDmuestral:


    def __init__(self):
        self.nombres_carpetas=[]
        self.ROOT_PATH = os.path.split(os.path.abspath(__file__))[0]
        self.archivos=[]
        self.directorio= self.ROOT_PATH+"/BaseDatosMuestral/input"
        
    def leerCarpetas(self):
       for filename in os.listdir(self.directorio):
           self.nombres_carpetas.append(filename) 

    def leerImagenes(self,sujeto):
        lista_img=[]
        nombres_archivos=os.listdir(self.directorio+"/"+sujeto)
        
        for nombre_archivo in nombres_archivos:
            
            img = cv2.imread(self.directorio+"/"+sujeto+"/"+nombre_archivo)
            

            i=imagen(img)
            i.vectorizar()
            lista_img.append(i)
        return lista_img

               
    def leerImagenestogris(self):
       for nombre_archivo in self.nombres_archivos:
           img = cv2.imread("files/"+nombre_archivo)
           gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
           a=[]
           for i in gray:
               a=np.concatenate((a,i),axis=0)
               self.archivos.append(np.array(a)[:,None])
    

