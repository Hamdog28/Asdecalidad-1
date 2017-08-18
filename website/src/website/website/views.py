from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from controlador.gestorSujetos import gestorSujetos

def index(request):
    gs=gestorSujetos()
    gs.cargar()
    return HttpResponseRedirect("/inicio")