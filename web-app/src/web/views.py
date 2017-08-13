from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .BackEnd.controlador.gestorSujetos import gestorSujeto

"""
def home(request):
    html = "<html><body>Hola mundo</body></html>" 
    return HttpResponse(html)
 """

def home(request):
    if request.method == 'POST':
        gs=gestorSujeto()
        
        gs.cargar()
        lista=[]
        for i in gs.lista_sujetos: 
            lista.append(i.nombre)
        print(lista)
        return render(request,"home.html",{"retorno":"Carga completa","datos":lista})
    return render(request,"home.html",{})

  
"""
def home(request):
    template = loader.get_template("home.html")
    
    return HttpResponse(template.render({},request))
    
 """