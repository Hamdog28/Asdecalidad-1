import unittest
#import controlador.DAOBDmuestral.DAOBDmuestral
#from back_end.controlador.DaoDBMuestral import DaoDBMuestral

from back_end.modelo.Imagen import Imagen
from back_end.modelo.Muestra import Muestra
from back_end.modelo.Proyeccion import Proyeccion
from back_end.modelo.Clasificacion import Clasificacion
from back_end.modelo.DistanciaCentroide import DistanciaCentroide
from back_end.controlador.GestorMuestra import GestorMuestra
from back_end.controlador.GestorPCA import GestorPCA
from back_end.controlador.Configuracion import Configuracion

from back_end.controlador.DaoBDPCA import DaoDBPCA


import numpy as np




class IntegrationTest(unittest.TestCase):
    gestor_muestra = GestorMuestra()
    muestra = Muestra()
    proyeccion = Proyeccion()
    clasificacion = Clasificacion()
    dao_db_pca = DaoDBPCA()

    
    def test_1(self):
        print("Test1: pueba de gestor de carga y muestra")
        IntegrationTest.gestor_muestra.cargar(0)
        IntegrationTest.muestra=IntegrationTest.gestor_muestra.muestra
        IntegrationTest.muestra.generar_matriz()
        IntegrationTest.muestra.generar_matriz_covarianza()
        
    def test_2(self):
        print("Test2: muestra y proyeccion")
        IntegrationTest.muestra.calcular_autovalores_autovectores() 
        IntegrationTest.proyeccion.proyectar(IntegrationTest.muestra,10)
        
        
        
    def test_3(self):
        print("Test3: proyeccion y clasificacion")
        img = Imagen(None)
        img.leer_imagen(Configuracion.RUTA_2+"otros/1.pgm")
        IntegrationTest.clasificacion=DistanciaCentroide(IntegrationTest.muestra)
        IntegrationTest.clasificacion.clasificar(img,self.proyeccion.autocaras,self.proyeccion.proyecciones)

    def test_4(self):
        print("Test4: proyeccion y dao db pca")
        IntegrationTest.dao_db_pca.guardar(IntegrationTest.proyeccion)
                

if __name__ == '__main__':
    unittest.main()