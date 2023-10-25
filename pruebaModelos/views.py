from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mostar_proyectos(request):
    proyectos = Proyecto.objects.select_related("tareas_proyecto").select_related("creador").prefetch_related("usuario").all()
    
    return render(request, 'proyecto/mostar.html',{"mostrar_proyectos":proyectos})