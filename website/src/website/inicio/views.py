from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
import sys 
from django.shortcuts import render
import os 
from back_end.modelo.Imagen import Imagen
from back_end.controlador.Control import Control
from django.template.context_processors import request
from django.core.files.storage import FileSystemStorage
from back_end.controlador.Configuracion import Configuracion
from django.core.files.base import ContentFile
from django.db import models
ctl = Control()


def index(request):
    template = loader.get_template('Login.html')
    context={}
    return HttpResponse(template.render(context,request))

def principal(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))

def identificar(request):
    template = loader.get_template('identificar.html')
    context={}
    return HttpResponse(template.render(context,request))

def pruebas(request):
    template = loader.get_template('Pruebas.html')
    context={}
    return HttpResponse(template.render(context,request))

def entrenamiento(request):
    template = loader.get_template('Entrenamiento.html')
    
    if request.method == 'POST':
        template = loader.get_template('Resultado.html')
        C_autovectores =int( request.POST['cantidad_autovectores'])
        P_muetra = int( request.POST['porcentaje_muestra'])
        prueba=ctl.entrenamiento(C_autovectores,P_muetra)
        context={"prueba":prueba}
        return HttpResponse(template.render(context,request))
    
    context={"ruta":"/inicio/entrenamiento","boton":"Entrenamiento","prueba":[]}
    return HttpResponse(template.render(context,request))



def nuevo_usuario(request):
    template = loader.get_template('nuevo_usuario.html')
    context={}
    return HttpResponse(template.render(context,request))

def resultado(request):
    template = loader.get_template('resultado.html')
    context={}
    return HttpResponse(template.render(context,request))

def upload_files(request):
    template = loader.get_template('Imagen.html')
    if request.method == 'POST':
        
        valor,sujeto, por=handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        
        context={"Sujeto":sujeto}
        return HttpResponse(template.render(context,request))
        
        
    context={"Sujeto":"Imagen incorrecta"}
    return HttpResponse(template.render(context,request))


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

def uploaded_db(request):
    template = loader.get_template('carga_imagenes.html')
    context={}
    if request.method == 'POST':
        handle_uploaded_folder(request)
        return HttpResponse(template.render(context,request))
        
    return HttpResponse(template.render(context,request))




        
def handle_uploaded_folder(file):
    directory=Configuracion.RUTA_2+"Datos_2/"

    i=1
    j=1
    for afile in file.FILES.getlist('file'):
        if not os.path.exists(directory):
            os.makedirs(directory+"s"+str(i))
        fs = FileSystemStorage(location=directory+"s"+str(i))
        
        filename = fs.save(str(afile), afile)
        uploaded_file_url = fs.url(filename)
        
        j=j+1
        if j%10==0:
            i=i+1
 

            
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    """
        fs = FileSystemStorage()
    
    print(filename)
    filename = fs.save(filename, file)
    uploaded_file_url = fs.url(filename)
    """
    img=Imagen([])
    
    img.leer_imagen('upload/'+filename)
    
    valor,sujeto=ctl.identificacion_sujeto(img)
    return valor,sujeto