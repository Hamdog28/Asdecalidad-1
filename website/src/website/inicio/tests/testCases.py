import unittest
#import controlador.DAOBDmuestral.DAOBDmuestral
from modelo.imagen import imagen
from controlador.gestorMuestra import gestorMuestra
from controlador.gestorSujetos import gestorSujetos
import numpy as np

class testCases(unittest.TestCase):
    '''
    Clase destinada a la ejecucion de pruebas unittest
    '''
    def testCargarDesdeBD(self):
        print("Test1")
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
        print("Test2")
        gestor=gestorMuestra()
        gestor.cargar()
        
        #Revisa si se creo la matriz de imagenes.
        self.assertTrue(gestor.muestra.matriz, "No hay matriz de imagenes")
        
        
        
        
    def testCambiarTamano(self):
        print("Test3")
        gestor=gestorSujetos()
        
        gestor.cargar()
        for sujeto in gestor.lista_sujetos:
            for imagen in sujeto.imagenes:
                imagenPrueba=imagen
                tamanoPrueba=(200,100,3)
                imagenPrueba.cambiarDimensionesImagen(tamanoPrueba[1], tamanoPrueba[0])
                self.assertEqual(imagenPrueba.img.shape, tamanoPrueba, "El tamano de la imagen (Especifico) no fue cambiado correctamente")
                tamanoPrueba=(100,50,3)
                imagenPrueba.cambiarTamanoPorcentualImagen(0.5, 0.5)
                self.assertEqual(imagenPrueba.img.shape, tamanoPrueba, "El tamano de la imagen (Porcentual) no fue cambiado correctamente")
                
        print("")

    def testMatrizCovarianza(self):
        print("Test4")
        gestor=gestorMuestra()
        gestor.cargar()#Tambien genera la muestra 
        gestor.muestra.generarMatrizCovarianza2() #20 segundos aprox
        
        self.assertTrue(gestor.muestra.matrizCovarianza.any(), "No se creo matriz de covarianza")

        self.assertEqual(len(gestor.muestra.matrizCovarianza), 10304, "El tamano de la matriz no es el adecuado")
       
        
unittest.main()