from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


"""
def home(request):
    html = "<html><body>Hola mundo</body></html>" 
    return HttpResponse(html)
 """

def home(request):
    if request.method == 'POST':
        print("hola mundo")
        return render(request,"home.html",{})
    return render(request,"home.html",{})

  
"""
def home(request):
    template = loader.get_template("home.html")
    
    return HttpResponse(template.render({},request))
    
 """