from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^nuevo',views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^principal',views.principal, name='principal'),
    url(r'^identificar',views.identificar, name='identificar'),
    url(r'^entrenamiento',views.entrenamiento, name='entrenamiento'),
    url(r'^pruebas',views.pruebas, name='pruebas'),
    url(r'^resultado',views.resultado, name='resultado'),
    url(r'^usuario',views.upload_file, name='upload_file'),
    url(r'^imagen',views.upload_files, name='upload_files'),
    url(r'^carga_imagen',views.uploaded_db, name='uploaded_db'),
    url(r'^$',views.index, name='index'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)