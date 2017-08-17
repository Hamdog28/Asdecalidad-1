
from .controlador.gestorSujetos import gestorSujetos
from .modelo.sujeto import sujeto
gs=gestorSujetos()

gs.cargar()

for i in gs.lista_sujetos: 
    print(i.nombre)

