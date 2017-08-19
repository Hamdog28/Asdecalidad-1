import numpy as np
import numpy.linalg as linalg
import cv2
import os 

class muestra:
    '''
    Encargada de representar y realizar calculos sobre las muestras 
    '''
    
    def __init__(self):
        
        self.sujetos=[]
        self.matriz=[]
        self.matrizCovarianza=[]
        self.autovalores=[]
        self.autovectores=[]
    
    def generarMatriz(self):
        '''
        Genera matriz de imagenes vectorizadas de cada sujeto
        '''
        
        for i in self.sujetos[0].imagenes[0].vector:
            self.matriz.append([])
        
        for sujeto in self.sujetos:
            for i in range(len(sujeto.imagenes)):
                for j in range(len(sujeto.imagenes[i].vector)):
                    self.matriz[j].append(sujeto.imagenes[i].vector[j])
                 
        
    def generarMatrizCovarianza2(self):
        self.matrizCovarianza=np.cov(self.matriz)
        
    def generarMatrizCovarianza(self):
        '''
        Generacion de la matriz de covarianza para la definicion de informacion
        relevante para los calculos
        '''
        m=np.array(self.matriz)
        promedios=[]
        for i in range(len(m)):
            promedios.append(np.mean(m[i]))
            self.matrizCovarianza.append([])
          
        resultado=0
        for i in range(1,len(m)+1):
            
            self.matrizCovarianza[i-1].append((1/(len(m)))*np.sum((promedios[i-1]-m[i-1])**2))
            for j in range(i,len(m)):

                resultado=(1/(len(m)))*np.sum((promedios[i-1]-m[i-1])*(promedios[j]-m[j]))
                self.matrizCovarianza[i-1].append(resultado)
                self.matrizCovarianza[j].append(resultado)
                
        
        
        #np.mean()
  
        
    def calcularAutovalores(self):
        '''
        Calcula los autovalores utilizando la matriz de covarianza.
        '''
        self.autovalores = linalg.eig(np.matrix(self.matrizCovarianza))
        
    
    def calcularAutovectores(self):
        print("hola mundo")