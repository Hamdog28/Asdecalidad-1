from .Control import Control

class Facade:
    
    def __init__(self):
        """
        Constructor
        """
        self.contol = Control()
        return None
    
    def entrenamiento(self,cantidad_autovectores):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Int
        @param 1: cantidad_autovectores
        
        @rtype: boolean
        @return: True si se ejecuto correctamente la funcion False si no 
        """
        funciona = self.contol.entrenamiento(cantidad_autovectores,0)
        return funciona 

    def identificacion_sujeto(self):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,Boolean
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        valor,sujeto=self.contol.identificacion_sujeto()
        return valor,sujeto

    def cargar_imagenes(self,direccion):
        """
        cargar_imagenes
        @details Solicita la funcion de cargar imagen
        
        @type 1: string
        @param 1: direccion
        
        @rtype: Boolean
        @return: True si se ejecuto correctamente la funcion False si no 
        """
        funciona = self.contol.cargar_imagenes(direccion)
        return funciona   

    def pruebas(self):
        """
        pruebas
        @details facilita la realisacion y confirmacion de pruebas
        
        @rtype: None
        @return: None 
        """
        self.contol.pruebas()
        return None
    
    def agregar_nuevo_sujeto(self):
        """
        agregar_nuevo_sujeto
        @details permite agregar una nueva funcion a la base de datos y entrenarla
        
        @rtype: None
        @return: None 
        """
        self.contol.agregar_nuevo_sujeto()
        return None