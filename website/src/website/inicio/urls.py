from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^imagen',views.upload_file, name='upload_file'),
=======
    url(r'^nuevo',views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^imagen',views.upload_file, name='upload_file'),
    url(r'^usuario',views.upload_files, name='upload_files'),
    url(r'^carga_imagen',views.uploaded_db, name='uploaded_db'),
>>>>>>> Olman
    url(r'^$',views.index, name='index'),
    
]