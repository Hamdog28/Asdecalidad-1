from django.http import HttpResponse

from django.template import loader

def index(request):
    template= loader.get_template("test/index.html")
    context={}
    return HttpResponse(template.reander(context,request))