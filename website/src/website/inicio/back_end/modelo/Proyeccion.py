import numpy as np

class Proyeccion:
    
    def __init__(self):
        self.autoespacio = []
        self.proyecciones = []
        
    def proyectar(self,muestra,cantidad_autovectores):
        cantidad_valores = int(muestra.matriz.shape[1] * cantidad_autovectores / 100)
        orden = np.argsort(muestra.autovalores)[::-1]
        autovectores = muestra.autovectores[orden]
        autovectores = autovectores[0: cantidad_valores]
        self.autoespacio = muestra.matriz * autovectores.T
        self.autoespacio = self.autoespacio / np.linalg.norm(self.autoespacio, axis=0)
        self.proyecciones = self.autoespacio.T * muestra.matriz


    