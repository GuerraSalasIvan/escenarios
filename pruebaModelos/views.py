from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mostar_proyectos(request):
    proyectos = Proyecto.objects.select_related("tareas_proyecto").select_related("creador").prefetch_related("usuario").all()
    
    return render(request, 'proyecto/mostar.html',{"mostrar_proyectos":proyectos})

def mostar_tareas_ordenado (request):
    tareas = Tarea.objects.select_related("creador").prefetch_related("usuario").order_by("-fechaCreacion").all()
    
    return render(request, 'tarea/mostrar_tarea.html',{'mostrar_tarea':tareas})

def mostar_tareas_asociadas (request, id_proyecto):
    tareas = Proyecto.objects.select_related("tareas_proyecto").select_related("creador").prefetch_related("usuario").get(id=id_proyecto)
    
    return render(request, 'proyecto/mostrar_uno.html',{"mostrar_proyectos":tareas})
    