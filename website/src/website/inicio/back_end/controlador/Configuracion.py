import os

class Configuracion:
    DIRECCION = os.path.split(os.path.abspath(__file__))[0]
    RUTA = DIRECCION+"../../archivos/Datos"
    RUTA_2 = DIRECCION+"../../archivos/"
    PORCENTAJE_PRUEBA = 60
    CANTIDAD_AUTOVECTORES = 80
    IMG_Y = 112
    IMG_X = 92
