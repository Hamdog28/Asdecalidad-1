from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
import sys 
from django.shortcuts import render
import os 
from modelo.imagen import imagen

def index(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))


def upload_file(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse('<script>function mensaje() {alert("Imagen ingresada con exito"); }mensaje();window.location.replace("http://127.0.0.1:8000/inicio");</script> ')
        
    return HttpResponse('<script>function mensaje() {alert("Imagen ingresada incorrectaente"); }mensaje();window.location.replace("http://127.0.0.1:8000/inicio");</script> ')

 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    img=imagen()
    img.leerImagenes(filename,'upload/')
          