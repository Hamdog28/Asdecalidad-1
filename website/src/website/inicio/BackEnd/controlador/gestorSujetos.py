import sys
from .DAOBDmuestral import DAOBDmuestral
  
sys.path.append("..")

from .modelo.sujeto import sujeto 

class gestorSujeto:
    def __init__(self):
        self.lista_sujetos=[]
        self.BDmustral=DAOBDmuestral()
        
    def cargar(self):
        self.BDmustral.leerCarpetas()
        for i in self.BDmustral.nombres_carpetas:
            s=sujeto(i)
            s.imagenes=self.BDmustral.leerImagenes(i)
            self.lista_sujetos.append(s)
            
        
    
