import numpy as np

class Proyeccion:
    
    def __init__(self):
        self.autocaras = []
        self.proyecciones = []
        
    def proyectar(self,muestra,cantidad_autovectores):
        cantidad_valores = int(muestra.matriz.shape[1] * cantidad_autovectores / 100)
        orden = np.argsort(muestra.autovalores)[::-1]
        autovectores = muestra.autovectores[orden]
        autovectores = autovectores[0: cantidad_valores]
        self.autocaras = muestra.matriz * autovectores.T
        self.autocaras = self.autocaras / np.linalg.norm(self.autocaras, axis=0)
        self.proyecciones=self.autocaras.T * muestra.matriz[:,0]
        for i in range(1,muestra.matriz.shape[1]):
            self.proyecciones = np.concatenate((self.proyecciones,self.autocaras.T * muestra.matriz[:,i]),axis=1)
        
        


    