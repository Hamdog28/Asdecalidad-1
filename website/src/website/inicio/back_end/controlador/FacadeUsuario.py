from .Facade import Facade

class FacadeUsuario(Facade):
    
    def __init__(self):    
        Facade.__init__(self)
    
    def identificacion_sujeto(self):
        Facade.identificacion_sujeto(self)
        return None

