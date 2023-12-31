from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    
    path('principal', views.principal, name='principal'),
    
    path('proyectos',views.mostar_proyectos, name='mostar_proyectos'),
    
    path('tareas/ordenado',views.mostar_tareas_ordenado, name='mostar_tareas_ordenado'),
    
    path('usuario_asociado_tarea/<int:id_tarea>',views.usuario_asociado_tarea, name='usuario_asociado_tarea'),
    
    path('tarea_contenga_observacion/<str:texto>',views.tarea_contenga_observacion, name='tarea_contenga_observacion'),
    
    path('proyecto_entre_fechas/<int:fechaMax>/<int:fechaMin>',views.proyecto_entre_fechas, name='proyecto_entre_fechas'),
    
    path('ultimo_usuario_comentado_tarea/<int:id_proyecto>',views.ultimo_usuario_comentado_tarea, name='ultimo_usuario_comentado_tarea'),
    
    path('comentario_tarea_año/<int:id_tarea>/<str:texto>/<int:anyo>',views.comentario_tarea_año, name='comentario_tarea_año'),
    
    path('lista_etiquetas',views.lista_etiquetas, name='lista_etiquetas'),
]
