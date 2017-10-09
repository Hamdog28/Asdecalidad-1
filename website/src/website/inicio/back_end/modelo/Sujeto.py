

class Sujeto:
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.imagenes = []
        self.submatriz = []
       
    def agregar_imagen(self,imagen):
        self.imagenes.append(imagen)
        return None
    
    def generar_submatriz(self):
        self.submatriz = []
        for i in self.imagenes[0].vector:
            self.submatriz.append([])
        
        for i in range(len(self.imagenes)):
            for j in range(len(self.imagenes[i].vector)):
                self.submatriz[j].append(self.imagenes[i].vector[j])
    
    