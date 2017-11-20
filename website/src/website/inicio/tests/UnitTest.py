import unittest
#import controlador.DAOBDmuestral.DAOBDmuestral
from back_end.modelo.Imagen import Imagen
from back_end.modelo.Muestra import Muestra
from back_end.controlador.GestorMuestra import GestorMuestra
from back_end.controlador.GestorPCA import GestorPCA
from back_end.controlador.Configuracion import Configuracion
from stub_muestra import stub_muestra
import numpy as np

class UnitTest(unittest.TestCase):
    
    def test_1(self):
        print("Test1: Cargar imagen")
        img = Imagen(None)
        self.assertTrue(img.leer_imagen(Configuracion.RUTA_2+"otros/1.pgm"), "Error al leer la imagen")
        
    def test_2(self):
        print("Test2: Cargar BD con un 50% para mustras")
        gestor=GestorMuestra()
        gestor.cargar(50)
        print("Tamaño de muestra")
        print(np.shape(gestor.muestra))
        self.assertTrue(gestor.muestra.sujetos, "Fallo en la carga, los sujetos no fueron cargados")
        
        
    def test_3(self):
        print("Test3: Generar matriz covarianza")
        muestra=Muestra()
        sm=stub_muestra()
        muestra.matriz=sm.matriz
        muestra.generar_matriz_covarianza()
        self.assertTrue(muestra.generar_matriz_covarianza(),"Erro en calcular la matriz de covarianza")
        

    def test_4(self):
        print("Test4: generar autovectores y autovalores")
        muestra = Muestra()
        sm=stub_muestra()
        muestra.matriz_covarianza=sm.matriz_covarianza
        muestra.calcular_autovalores_autovectores()
        self.assertTrue(muestra.calcular_autovalores_autovectores(),"Erro en calcular los autovalores y autovectores")
                

if __name__ == '__main__':
    unittest.main()

