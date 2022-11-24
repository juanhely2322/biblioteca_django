from django.db import models
import os

class Libro(models.Model):

    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField (verbose_name="Imagen", null=True) 
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    cantidad=models.PositiveIntegerField( default=0,verbose_name="Cantidad",null=False)
    disponible=models.PositiveIntegerField(verbose_name="Cantidad disponible",null=True)
    def __str__(self):
        return "Libro: "+self.titulo
    
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(Libro,self).delete(*args,**kwargs)