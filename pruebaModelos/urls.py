from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    
    path('proyectos',views.mostar_proyectos, name='mostar_proyectos'),
    
    path('tareas/ordenado',views.mostar_tareas_ordenado, name='mostar_tareas_ordenado'),
    
    path('tarea_asociada/<int:id_proyecto>',views.mostar_tareas_asociadas, name='mostar_tareas_asociadas'),
    
]
