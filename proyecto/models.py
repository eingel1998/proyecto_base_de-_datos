from django.db import models

# Create your models here.
class Persona (models.Model):
    id_persona = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre_persona = models.CharField(max_length=30)
    cedula_persona = models.PositiveIntegerField()
    telefono_persona = models.CharField(max_length=10)

class Estudiante (models.Model):
    codigo_universitario = models.CharField(max_length=30)
    correo_institucional = models.CharField(max_length=30)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Conductor (models.Model):
    horario = models.CharField(max_length=30)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Ruta (models.Model):
    numero_ruta = models.CharField(max_length=30)
    estado_ruta = models.CharField(max_length=30)
    recorrido_ruta = models.TextField()
    Conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

class lista (models.Model):
    plaza_dis = models.CharField(max_length=30)
    horario_salida = models.CharField(max_length=30)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)