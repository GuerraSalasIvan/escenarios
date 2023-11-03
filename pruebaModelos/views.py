from django.shortcuts import render
from .models import *
from django.views.defaults import page_not_found
from django.db.models import Q, Prefetch

# Create your views here.

def index(request):
    return render(request, 'index.html')

def principal(request):
    return render(request, 'principal.html')

def mostar_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related("usuario").all()
    
    return render(request, 'proyecto/mostar.html',{"mostrar_proyectos":proyectos})


def mostar_tareas_ordenado (request):
    tareas = Tarea.objects.select_related("creador").select_related("tareas_proyecto").prefetch_related("usuario").order_by("-fechaCreacion").all()
    
    return render(request, 'tarea/mostrar_tarea.html',{'mostrar_tarea':tareas})


def usuario_asociado_tarea (request, id_tarea):
    usuarios = Usuarios.objects.filter(asignaciontarea__tarea=id_tarea).order_by("asignaciontarea__tarea").all()
    
    return render (request, 'usuario/mostrar_usuarios.html',{'usuario_asociado_tarea':usuarios})


def tarea_contenga_observacion(request, texto):
    tareas = Tarea.objects.select_related("creador").select_related("tareas_proyecto").prefetch_related("usuario").filter(asignaciontarea__oberservaciones__contains=texto).all()
    
    return render(request, 'tarea/mostrar_tarea.html',{'mostrar_tarea':tareas})


def proyecto_entre_fechas(request, fechaMax, fechaMin):
    tareas = Tarea.objects.select_related("creador").select_related("tareas_proyecto").prefetch_related("usuario").filter(fechaCreacion__year__gte=fechaMin).filter(fechaCreacion__year__lte=fechaMax).filter(estadio='CO').all()
    
    return render(request, 'tarea/mostrar_tarea.html',{'mostrar_tarea':tareas})
    

def ultimo_usuario_comentado_tarea(request, id_proyecto):
    comentario = Comentario.objects.select_related("autor").select_related("rel_tarea").filter(rel_tarea__tareas_proyecto=id_proyecto).order_by("-fechaComentario")[:1].get()
    
    return render(request, 'comentario/mostrar_comentario.html', {'comentario':comentario})

    
def comentario_tarea_año(request, id_tarea, texto, anyo):
    comentario = Comentario.objects.select_related("autor").select_related("rel_tarea").filter(rel_tarea=id_tarea).filter(contenido__startswith=texto).filter(fechaComentario__year=anyo).all()
    
    return render(request, 'comentario/mostrar.html', {'comentario':comentario})

def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.distinct().all()
    
    return render(request, 'etiqueta/mostrar.html', {'etiqueta':etiquetas})

# ERRORES

def mi_error_404(request, exception=None):
    return render (request, 'errores/404.html',None, None, 404)

def mi_error_403 (request, exception=None):
    return render (request, 'errores/403.html',None, None, 403)

def mi_error_400 (request, exception=None):
    return render (request, 'errores/400.html',None, None, 400)

def mi_error_500(request, exception=None):
    return render (request, 'errores/500.html',None, None, 500)