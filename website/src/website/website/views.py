from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from controlador.gestorMuestra import gestorMuestra

def index(request):
    gs=gestorMuestra()
    gs.cargar()
    return HttpResponseRedirect("/inicio")