import unittest
#import controlador.DAOBDmuestral.DAOBDmuestral
from back_end.modelo.Imagen import Imagen
from back_end.controlador.GestorMuestra import GestorMuestra
from back_end.controlador.GestorPCA import GestorPCA
from back_end.controlador.Configuracion import Configuracion
import numpy as np

class testCases(unittest.TestCase):
    '''
    Clase destinada a la ejecucion de pruebas unittest
    '''
    def testCargarDesdeBD(self):
        print("Test1")
        gestor=GestorMuestra()
        gestor.cargar()
        #Revisa si se cargaron sujetos
        self.assertTrue(gestor.muestra.sujetos, "Fallo en la carga, los sujetos no fueron cargados")
        
        #Revisa por cada sujeto si se cargaron sus fotos
        indice=0
        standardSize=(112,92,3)
        sujeto = gestor.muestra.sujetos[0]
        indice+=1
        print("Sujeto ",indice)
        self.assertTrue(sujeto.imagenes, "Un sujeto no tiene imagenes.")
            
            
            #Revisa si las imagenes cumplen con standardSize
        for imagen in sujeto.imagenes:
            self.assertEqual(imagen.img.shape, standardSize, "El tamano de la imagen no es valido")
            
        print(indice," sujetos analizados.")
        
    def testGenerarMatrizImagenes(self):
        print("Test2")
        gestor=GestorMuestra()
        gestor.cargar()
        
        #Revisa si se creo la matriz de imagenes.
        self.assertTrue(gestor.muestra.matriz==[], "No hay matriz de imagenes")
        
        
        
        
    def testCambiarTamano(self):
        print("Test3")
        gestor=GestorMuestra()
        
        gestor.cargar()   
        imagenPrueba=gestor.muestra.sujetos[0].imagenes[0]
        tamanoPrueba=(200,100,3)
        imagenPrueba.cambiar_dimenciones_imagen(tamanoPrueba[1], tamanoPrueba[0])
        self.assertEqual(imagenPrueba.img.shape, tamanoPrueba, "El tamano de la imagen (Especifico) no fue cambiado correctamente")
        tamanoPrueba=(100,50,3)
        imagenPrueba.cambiar_tamano_porcentual_imagen(0.5, 0.5)
        self.assertEqual(imagenPrueba.img.shape, tamanoPrueba, "El tamano de la imagen (Porcentual) no fue cambiado correctamente")
                
        print("")

    def testMatrizCovarianza(self):
        print("Test4")
        gestor=GestorMuestra()
        gestor.cargar()#Tambien genera la muestra 
        gestor.muestra.generar_matriz()
        gestor.muestra.generar_matriz_covarianza() #20 segundos aprox
        self.assertEqual(len(gestor.muestra.matriz_covarianza) , 410, "El tamano de la matriz no es el adecuado")
       
        
    def testEntrenamiento(self):
        print("Test5")
        gestor=GestorMuestra()
        gestor_pca=GestorPCA()
        gestor.cargar()#Tambien genera la muestra 
        gestor.muestra.generar_matriz()
        gestor.muestra.generar_matriz_covarianza() #20 segundos aprox
        gestor.muestra.calcular_autovalores_autovectores()
        self.assertEqual(len(gestor.muestra.matriz_covarianza) , 410, "El tamano de la matriz no es el adecuado")
        gestor_pca.pca.agregar_muestra(gestor.muestra)
        valor=gestor_pca.pca.entrenamiento(80)
        gestor_pca.dao_db_pca.guardar(gestor_pca.pca.proyeccion)
        self.assertTrue(valor, "Error entrenamiento")

    def testIdentificacion(self):
        print("Test6")
        gestor=GestorMuestra()
        gestor_pca=GestorPCA()
        gestor.cargar()#Tambien genera la muestra 
        gestor.muestra.generar_matriz()
        gestor.muestra.generar_matriz_covarianza() #20 segundos aprox
        gestor.muestra.calcular_autovalores_autovectores()
        self.assertEqual(len(gestor.muestra.matriz_covarianza) , 410, "El tamano de la matriz no es el adecuado")
        gestor_pca.pca.agregar_muestra(gestor.muestra)
        valor=gestor_pca.pca.entrenamiento(80)
        gestor_pca.dao_db_pca.guardar(gestor_pca.pca.proyeccion)
        self.assertTrue(valor, "Error entrenamiento")
        img=Imagen([])
        img.leer_imagen(Configuracion.RUTA_2+"/otros/1.pgm")
        valor,sujeto =  gestor_pca.pca.identificacion_sujetos(img)
        print("El sujeto identificado es "+sujeto)
        
    def testPruebas(self):
        print("Test7")
        gestor_pca=GestorPCA()
        gestor_pca.pruebas()
       
    def testCargarImagenesDeDireccion(self):
        print("Test5")
        gestor=gestorMuestra()
        gestor.cargar()
        
<<<<<<< HEAD
if __name__ == '__main__':
    unittest.main()
=======
        #Revisa si se creo la matriz de imagenes.
        self.assertTrue(gestor.muestra.matriz, "No hay matriz de imagenes")
    
    
unittest.main()
>>>>>>> d9d7ea7f426aac9a19790aa79f2f33e26ced0e0a
