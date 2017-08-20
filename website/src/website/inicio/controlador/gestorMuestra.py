

from .DAOBDmuestral import DAOBDmuestral
  

from modelo.sujeto import sujeto 
from modelo.muestra import muestra

class gestorMuestra:
    def __init__(self):
        
        self.BDmustral=DAOBDmuestral()
        self.muestra=muestra()
        
    def cargar(self):
        
        self.BDmustral.leerCarpetas()
        lista_sujetos=[]
        for i in self.BDmustral.nombres_carpetas:
            s=sujeto(i)
            s.imagenes=self.BDmustral.leerImagenes(i)
            lista_sujetos.append(s)
        
        self.muestra.sujetos=lista_sujetos
        self.muestra.sujetos[0].imagenes
        self.muestra.generarMatriz()
        
            