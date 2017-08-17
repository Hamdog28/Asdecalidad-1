from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^imagen',views.upload_file, name='upload_file'),
    url(r'^$',views.index, name='index'),
    
]