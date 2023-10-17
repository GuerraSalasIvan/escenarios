from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuarios(models.Model):
    nombre = models.TextField()
    correo_electronico = models.TextField(unique = True)
    contraseña = models.TextField()
    fechaRegistro = models.DateTimeField(default=timezone.now)
    

class Tarea(models.Model):
    
    ESTADOS = ('PE','Pendiente'),
    ('PR','Progreso'),
    ('CO','Completada'),
    
    nombre = models.TextField()
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estadio = models.CharField(
        max_length=2,
        choices=ESTADOS,
        default='PE')
    
    completada = models.BooleanField()
    fechaCreacion = models.DateTimeField(default=timezone.now)
    horaVencimineto = models.DateField()
    
    creador = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    usuario = models.ManyToManyField(Usuarios, through="AsignacionTarea", related_name="usuario_asignado")
    
    

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.FloatField()
    fechaInicio = models.DateTimeField()
    fechaFin = models. DateTimeField()
    
    creador = models.ForeignKey(Usuarios , on_delete=models.CASCADE)
    tareas_proyecto = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ManyToManyField(Usuarios, through="Proyectos_asignados",related_name="usuarioAsignado")
    

    
    
class AsignacionTarea(models.Model):
    oberservaciones = models.CharField(max_length=100)
    fechaAsignacion = models.DateTimeField()
    autor = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE)
    
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    tarea = models.ManyToManyField(Tarea, through="Etiquetas_asociadas", related_name="etiqueta_asociada")    
    
class Comentario(models.Model):
    contenido = models.CharField(max_length=100)
    fechaComentario = models.DateTimeField()
    
    autor = models.OneToOneField(Usuarios, on_delete=models.CASCADE)
    rel_tarea = models.OneToOneField(Tarea, on_delete=models.CASCADE)
    
    
class Proyectos_asignados(models.Model):
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)


class Etiquetas_asociadas(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)