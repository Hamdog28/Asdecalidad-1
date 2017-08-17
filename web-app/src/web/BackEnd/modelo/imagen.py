import numpy as np
import cv2

class imagen:
    def __init__(self,img):
        self.img=img
        self.vector=[]
        
        
    def vectorizar(self):
        
        for i in cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY):#Duda de si interfiere
            
            self.vector=np.concatenate((self.vector,i),axis=0)
        

    def leerImagenes(self,nombre_archivo):
           
        self.img = cv2.imread(self.directorio+"/"+nombre_archivo)
        
        self.vectorizar()
    
            
    def imgAgris(self):
        return cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)