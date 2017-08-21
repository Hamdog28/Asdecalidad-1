import numpy as np
import cv2
import os 

class imagen:
    '''
    Clase encargada de representar las imagenes de los sujetos.
    '''
    def __init__(self,img):
        '''
        Constructor
        :param img: Imagen que va a guardar.
        '''
        self.img=img
        self.vector=[]
        self.directorio= "./BaseDatosMuestral/ejemplos" #Se debe agregar el directorio coorespondiente
        
        
    def vectorizar(self):
        '''
        Transforma la imagen a un vector mediante el uso de OpenCV.
        '''
        
        for i in cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY):#Duda de si interfiere
            
            self.vector=np.concatenate((self.vector,i),axis=0)
        

    def leerImagenes(self,nombre_archivo):
        '''
        Lee una imagen con un nombre de archivo dado en el directorio local.
        Invoca al metodo que vectoriza la imagen.
        :param nombre_archivo:
        '''
           
        self.img = cv2.imread(self.directorio+"/"+nombre_archivo)
        
        self.vectorizar()
    
            
    def imgAgris(self):
        '''
        Retorna la imagen en escala de grises. 
        '''
        return cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
    
    def cambiarTamanoPorcentualImagen(self, porcentajeX, porcentajeY):
        '''
        Le cambia el tamano a la imagen a un porcentaje del original (1.0=100%)
        :param porcentajeX: Porcentaje en X 
        :param porcentajeY: Porjentaje en Y
        '''
        self.img=cv2.resize(self.img, (0,0), fx = porcentajeX, fy = porcentajeY)

    def cambiarDimensionesImagen(self, tamanoX, tamanoY):
        '''
        Le cambia el tamano a la imagen a un tamano determinado
        :param tamanoX: Pixeles en X
        :param tamanoY: Pixeles en Y
        '''
        
        self.img=cv2.resize(self.img, (tamanoX, tamanoY))
