import cv2
import os
import numpy as np
import random 
from .Configuracion import Configuracion
from .DaoBDPCA import DaoDBPCA
from ..modelo.Muestra import Muestra
from ..modelo.PCA import PCA
from ..modelo.Imagen import Imagen
from .DaoBDMuestral import DaoDBMuestral
from ..modelo.Sujeto import Sujeto
from .DaoBDMuestral import DaoDBMuestral
class GestorPCA:
    
    def __init__(self):
        self.dao_db_pca = DaoDBPCA()
        self.pca = PCA()
    
    def entrenamiento(self,muestra,cantidad_autovectores):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        self.pca.agregar_muestra(muestra)
        self.pca.entrenamiento(cantidad_autovectores)
        self.dao_db_pca.guardar(self.pca.proyeccion)
        return None

    def identificacion_sujeto(self,img):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        valor,sujeto = self.pca.identificacion_sujetos(img)
        return valor,sujeto 

    def pruebas(self):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,String
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        muestra = Muestra()
        pca = PCA()
        BDmuestral = DaoDBMuestral()

        nombres_carpetas = BDmuestral.leer_carpetas()
        lista_sujetos = []
        lista_sujetos_prueba = []
        for i in nombres_carpetas:
            s=Sujeto(i)
            s_p=Sujeto(i)
            s.imagenes = BDmuestral.leer_imagenes(i)
            sujetos=len(s.imagenes)
            numero_sujetos=int(sujetos*Configuracion.PORCENTAJE_PRUEBA/100)
            imagen_prueba = []
            for j in range(numero_sujetos):
                quitar=random.randrange(0,len(s.imagenes)-1)
                img=s.imagenes.pop(quitar)
                imagen_prueba.append(img)
            s_p.imagenes = imagen_prueba
            lista_sujetos_prueba.append(s_p)
            lista_sujetos.append(s)
        muestra.sujetos=lista_sujetos
        pca.agregar_muestra(muestra)
        pca.entrenamiento(Configuracion.CANTIDAD_AUTOVECTORES)
        fp_fn = []
        indice = 0
        for x in lista_sujetos_prueba:
            fp_fn.append([0,0])
            for y in x.imagenes:
                valor,sujeto = pca.identificacion_sujetos(y)
                if sujeto==x.nombre:
                    fp_fn[indice][0]= fp_fn[indice][0]+1
                else:
                    fp_fn[indice][1]= fp_fn[indice][1]+1
            indice=indice+1
        m_fp_fn = np.matrix(fp_fn)
        np.savetxt(Configuracion.RUTA_2+'/fp_fn.csv', m_fp_fn, delimiter=",")
                    
            
        
        return None
    
    def agregar_nuevo_sujeto(self):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        return None