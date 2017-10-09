import os

class Configuracion:
    DIRECCION = os.path.split(os.path.abspath(__file__))[0]
    RUTA = DIRECCION+"../../archivos/Datos"
    IMG_Y = 112
    IMG_X = 92
