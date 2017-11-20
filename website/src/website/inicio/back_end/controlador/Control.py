from .GestorPCA import GestorPCA
from .GestorMuestra import GestorMuestra
from symbol import except_clause

class Control:
    
    def __init__(self):
        '''
        Constructor
        '''
        self.gestor_pca = GestorPCA()
        self.gestor_muestra = GestorMuestra()
        
    def entrenamiento(self,cantidad_autovectores,porcentaje_prueba):
        """
        entrenamiento
        @details Se encarga de solicitar la funcion de entrenamiento 
        
        @type 1: int
        @param 1: cantidad_autovectores
        
        @rtype: Boolean
        @return: True si se ejecuto correctamente
        """
        self.gestor_muestra.cargar(porcentaje_prueba)
        self.gestor_pca.entrenamiento(self.gestor_muestra.muestra,cantidad_autovectores)
        sujeto=[]
        aciertos=0
        for i in self.gestor_muestra.muestra.sujetos:
            sujeto.append([i.nombre,0,0,0,0,0,0])
        cant_muestras = 0
        for i in self.gestor_muestra.muestra.sujetos:
            
            for j in i.imagenes_prueba:
                cant_muestras+=1
                x,y,z=self.gestor_pca.identificacion_sujeto(j)
                if i.nombre == y:
                    
                    sujeto[int(i.nombre[1:])-1][3]+=1
                    aciertos+=1
                else:
                    sujeto[int(i.nombre[1:])-1][1]+=1
                    sujeto[int(y[1:])-1][2]+=1

        for i in sujeto:
            
            try:
                i[4]=i[3]/(i[3]+i[1])
            except:
                i[4]=None
                
            try:
                i[5]=i[3]/(i[3]+i[2])
            except:
                i[5]=None
                
            try:
                i[6]=(2*i[5]*i[4])/(i[4]+i[5])
            except:
                i[6]=None
            
        return sujeto

    def identificacion_sujeto(self,img):
        """
        identificacion_sujeto
        @details Solicita la funcion de identificar sujeto
        
        @type 1: Imagen
        @param 1: img
        
        @rtype: Int,String
        @return: valor dato=seleccionado como el mas optimo, sujeto=nombre del sujeto 
        """
        valor,sujeto , por= self.gestor_pca.identificacion_sujeto(img)
        return valor,sujeto,por

    def cargar_imagenes(self,direccion):
        """
        cargar_imagenes
        @details Solicita la funcion de cargar imagenes
        
        @type 1: String
        @param 1: direccion
        
        @rtype: None
        @return: None 
        """
        self.gestor_muestra.cargar_imagenes(direccion)
        return None   

    def pruebas(self):
        """
        pruebas
        @details Solicita la funcion de realizar pruebas
        
        @rtype: None
        @return: None 
        """
        self.gestor_pca.pruebas()
        return None
    
    def agregar_nuevo_sujeto(self):
        self.gestor_muestra.agregar_nuevo_sujeto()
        return None
    