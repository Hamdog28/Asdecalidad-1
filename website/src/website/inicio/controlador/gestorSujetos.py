import sys
from controlador.DAOBDmuestral import DAOBDmuestral
  
sys.path.append("..")

from modelo.sujeto import sujeto 

class gestorSujetos:
    '''
    Clase gestorSujetos
    Encargada de la gestion de los sujetos (carga y organizacion de las imagenes de los sujetos)
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.lista_sujetos=[]
        self.BDmustral=DAOBDmuestral()
        
    def cargar(self):
        '''
        Utiliza DAOBDmuestral para cargar las imagenes de cada sujeto.
        '''
        self.BDmustral.leerCarpetas()
        for i in self.BDmustral.nombres_carpetas:
            s=sujeto(i)
            s.imagenes=self.BDmustral.leerImagenes(i)
            self.lista_sujetos.append(s)
            