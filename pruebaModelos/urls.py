from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('proyectos',views.mostar_proyectos, name='mostar_proyectos'),
]
