from django.db import models

# Create your models here.

class Project(models.Model):
    title= models.CharField(max_length=200, verbose_name="titulo")
    descriptions =models.TextField(verbose_name="descripcion")
    image = models.ImageField(upload_to="project",verbose_name="imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion") 

    class Meta:
        verbose_name='proyecto'
        verbose_name_plural = 'proyectos'
        ordering =["-created"]

    def __str__(self):
        return  self.title