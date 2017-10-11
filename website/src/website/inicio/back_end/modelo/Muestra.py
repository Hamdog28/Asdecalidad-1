import numpy as np

class Muestra:
    
    def __init__(self):
        self.sujetos = []
        self.matriz = []
        self.cara_promedio = []
        self.matriz_covarianza = []
        self.autovalores = []
        self.autovectores = []
    
    def generar_matriz(self):
        """
        generar_matriz
        @details permite generara la matriz de mustra
        
        @rtype: None
        @return: None 
        """
        self.matriz = []
        for i in self.sujetos[0].imagenes[0].vector:
            self.matriz.append([])
        for sujeto in self.sujetos:
            for i in range(len(sujeto.imagenes)):
                for j in range(len(sujeto.imagenes[i].vector)):
                    self.matriz[j].append(sujeto.imagenes[i].vector[j])
        self.matriz = np.matrix(self.matriz)
        return None

    def generar_matriz_covarianza(self):
        """
        generar_matriz_covarianza
        @details permite generar la matrix de covarianza utilisando el metodo de la traspuesta
        
        @rtype: None
        @return: None 
        """
        self.cara_promedio = np.mean(self.matriz,axis=1,dtype="float64")
        self.matriz = np.matrix(self.matriz) - self.cara_promedio 
        self.matriz_covarianza = self.matriz.T * self.matriz
        self.matriz_covarianza = self.matriz_covarianza / self.matriz.shape[1] - 1 
        return None
  
    def calcular_autovalores_autovectores(self):
        """
        calcular_autovalores_autovectores
        @details Calcula los autovalores y autovectores de la matrix de covarianza
        
        @rtype: None
        @return: None 
        """
        self.autovalores, self.autovectores = np.linalg.eig(self.matriz_covarianza)
        return None   


    
    