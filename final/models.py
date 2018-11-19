from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.
class Profesor(models.Model):
    nombre  =   models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre  =   models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    Profesor = models.ForeignKey(Profesor, blank=True, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Grado(models.Model):
    nombre  =   models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    Materia = models.ManyToManyField(Materia, through='Pensum')

    def __str__(self):
        return self.nombre

class Pensum (models.Model):
    Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class PensumInLine(admin.TabularInline):
    model = Pensum
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (PensumInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (PensumInLine,)
