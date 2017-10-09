
from controlador.DAOBDmuestral import DAOBDmuestral
from modelo.sujeto import sujeto 
from modelo.muestra import muestra

class gestorMuestra:
    '''
    Encargada de la gestion de las muestras.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
        self.BDmuestral=DAOBDmuestral()
        self.muestra=muestra()
        
    def cargar(self):
        '''
        Carga las muestras
        '''
        
        self.BDmuestral.leerCarpetas()
        lista_sujetos=[]
        for i in self.BDmuestral.nombres_carpetas:
            s=sujeto(i)
            s.imagenes=self.BDmuestral.leerImagenes(i)
            lista_sujetos.append(s)
        
        self.muestra.sujetos=lista_sujetos
        self.muestra.sujetos[0].imagenes
        self.muestra.generarMatriz()
