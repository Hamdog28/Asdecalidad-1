from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
import sys 
from django.shortcuts import render
import os 
from back_end.modelo.Imagen import Imagen
from back_end.controlador.Control import Control

ctl = Control()
ctl.entrenamiento(100)

def index(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))

def nuevo_usuario(request):
    template = loader.get_template('nuevo_usuario.html')
    context={}
    return HttpResponse(template.render(context,request))

def upload_files(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse('<script>function mensaje() {alert("Imagen ingresada con exito"); }mensaje();window.location.replace("http://127.0.0.1:8000/inicio");</script> ')
        
    return HttpResponse('<script>function mensaje() {alert("Imagen ingresada incorrectaente"); }mensaje();window.location.replace("http://127.0.0.1:8000/inicio");</script> ')


def upload_file(request):
    if request.method == 'POST':
        try:
            Nombre = request.POST['nombre']
            handle_uploaded_file(request.FILES['file1'], str(request.FILES['file1']))
            handle_uploaded_file(request.FILES['file2'], str(request.FILES['file2']))
            handle_uploaded_file(request.FILES['file3'], str(request.FILES['file3']))
            handle_uploaded_file(request.FILES['file4'], str(request.FILES['file4']))
            handle_uploaded_file(request.FILES['file5'], str(request.FILES['file5']))
            handle_uploaded_file(request.FILES['file6'], str(request.FILES['file6']))
            handle_uploaded_file(request.FILES['file7'], str(request.FILES['file7']))
            handle_uploaded_file(request.FILES['file8'], str(request.FILES['file8']))
            handle_uploaded_file(request.FILES['file9'], str(request.FILES['file9']))
            handle_uploaded_file(request.FILES['file10'], str(request.FILES['file10']))
            return HttpResponse('<script>function mensaje() {alert("Imagen ingresada con exito"); }mensaje();window.location.replace("http://127.0.0.1:8000/inicio");</script> ')
        except:
            valor,sujeto=handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
            return HttpResponse('<script>function mensaje() {alert("Sujeto '+sujeto+'"); }mensaje();window.location.replace("http://127.0.0.1:8000/inicio");</script> ')
       
        
    return HttpResponse('<script>function mensaje() {alert("Imagen ingresada incorrectaente"); }mensaje();window.location.replace("http://127.0.0.1:8000/inicio");</script> ')

 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    img=Imagen([])
    
    img.leer_imagen('upload/'+filename)
    
    valor,sujeto=ctl.identificacion_sujeto(img)
    return valor,sujeto