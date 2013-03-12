from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template 
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from demo.models import *
from demo.forms import *

def home(request):
    return HttpResponse("Hola mundo")
    
def post(request,id):
    return HttpResponse("post %s" % id)
    

def template(request):
    menu = clase.objects.all()
    galeria = Elemento.objects.filter(mostrar = True)
    template = "galeria.html"
    data = {'galeria' : galeria, "menu" : menu}
    return render_to_response(template, context_instance=RequestContext(request,data))
    

def acerca(request):
    template = "index.html"
    return render_to_response(template, context_instance=RequestContext(request)) 

from django.contrib.auth.decorators import login_required

def agregar(request):
    template = "agregar.html"
    
    if request.method == 'POST':
        form = ElementoForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ElementoForm()
    data = {'form': form}
    return render_to_response(template, context_instance=RequestContext(request,data))
