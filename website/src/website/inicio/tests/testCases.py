import unittest
#import controlador.DAOBDmuestral.DAOBDmuestral
from controlador.DAOBDmuestral import DAOBDmuestral
from controlador.gestorMuestra import gestorMuestra
from controlador.gestorSujetos import gestorSujetos
import numpy as np

class testCases(unittest.TestCase):
    '''
    Clase destinada a la ejecucion de pruebas unittest
    '''
    
    def testCargarDesdeBD(self):
        gestor=gestorSujetos()
        gestor.cargar()
        
        #Revisa si se cargaron sujetos
        self.assertTrue(gestor.lista_sujetos, "Fallo en la carga, los sujetos no fueron cargados")
        
        #Revisa por cada sujeto si se cargaron sus fotos
        indice=0
        standardSize=(112,92,3)
        for sujeto in gestor.lista_sujetos:
            indice+=1
            print("Sujeto ",indice)
            if self.assertTrue(sujeto.imagenes, "Un sujeto no tiene imagenes."):
                break
            
            #Revisa si las imagenes cumplen con standardSize
            for imagen in sujeto.imagenes:
                self.assertEqual(imagen.img.shape, standardSize, "El tamano de la imagen no es valido")
            
        print(indice," sujetos analizados.")
        
    def testGenerarMatrizImagenes(self):
        gestor=gestorMuestra()
        gestor.cargar()
        
        #Revisa si se creó la matriz de imagenes.
        self.assertTrue(gestor.muestra.matriz, "No hay matriz de imagenes")
        
        
        
        
    def test3(self):
        print("")
        
    def test4(self):
        print("")
        
unittest.main()