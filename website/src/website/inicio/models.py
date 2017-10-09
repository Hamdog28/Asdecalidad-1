from django.db import models
'''
import numpy as np
import cv2
from unittest.util import _MAX_LENGTH
# Create your models here.


class imagen(models.Model):
    def __init__(self,img):
        self.img=img
        self.vector=[]
        
        
    def vectorizar(self):
        
        for i in cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY):#Duda de si interfiere
            
            self.vector=np.concatenate((self.vector,i),axis=0)
        
class sujeto(models.Model):
    nombre=models.CharField(max_length=250)
    imagenes= models.
    matriz=models.
    def __init__(self,nombre):
        self.nombre=nombre
        self.imagenes=[]
        self.matriz=[]
            
    def agregarImagene(self,imagen):
        self.imagenes.append(imagen)
    
'''