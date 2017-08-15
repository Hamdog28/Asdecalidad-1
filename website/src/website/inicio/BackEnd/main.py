
from controlador.gestorSujetos import gestorSujeto
from modelo.sujeto import sujeto
gs=gestorSujeto()

gs.cargar()

for i in gs.lista_sujetos: 
    print(i.nombre)

