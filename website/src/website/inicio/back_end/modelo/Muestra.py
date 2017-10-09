import numpy as np

class Muestra:
    
    def __init__(self):
        self.sujetos = []
        self.matriz = []
        self.promedio = []
        self.matriz_covarianza = []
        self.autovalores = []
        self.autovectores = []
    
    def generar_matriz(self):
        self.matriz = []
        for i in self.sujetos[0].imagenes[0].vector:
            self.matriz.append([])
        for sujeto in self.sujetos:
            for i in range(len(sujeto.imagenes)):
                for j in range(len(sujeto.imagenes[i].vector)):
                    self.matriz[j].append(sujeto.imagenes[i].vector[j])
        self.matriz=np.matrix(self.matriz)
        return None

    def generar_matriz_covarianza(self):
        self.promedio = np.mean(self.matriz,axis=1,dtype="float64")
        self.matriz=self.matriz-self.promedio
        self.matriz_covarianza = np.cov(self.matriz.T)
       
        """
        print(self.matriz.shape)
        self.promedio = np.mean(self.matriz,axis=1,dtype="float64")
        #print(self.promedio)
        matriz_d=np.matrix(self.matriz)-self.promedio 
        print(matriz_d.shape)
        self.matriz_covarianza = matriz_d.T * matriz_d
        self.matriz_covarianza /= self.matriz.shape[1] - 1 
        """    
        return None
  
    def calcular_autovalores_autovectores(self):
        self.autovalores, self.autovectores = np.linalg.eig(self.matriz_covarianza)
        return None   


    
    