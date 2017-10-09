from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader




def home(request):
    lista=[]
    if request.method == 'POST':

        #for i in gs.lista_sujetos: 
        #   lista.append(i.nombre)
        
        return render(request,"home.html",{"retorno":"Carga completa","datos":lista,"class":"btimgok","text":"Sistema entrenado"})
    return render(request,"home.html",{"class":"btimgko","text":"Entrenar sistema"})

