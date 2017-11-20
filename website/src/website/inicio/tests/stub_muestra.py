import numpy as np

class stub_muestra:
    
    def __init__(self):
        self.matriz = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
        self.matriz_covarianza = np.cov(self.matriz) 