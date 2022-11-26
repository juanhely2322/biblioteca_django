from django.db import models
import os

class genero(models.Model):
       
    #libro=models.ForeignKey(Libro,verbose_name="Libro genero",on_delete=models.CASCADE)
    genero=models.CharField(default="Sin genero",verbose_name="Genero",max_length=20,null=False)
    
    def __str__(self):
            return self.genero


class Libro(models.Model):
    
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField (upload_to="media",verbose_name="Imagen", null=False) 
    descripcion = models.TextField(verbose_name="Descripción", null=False)
    cantidad=models.PositiveIntegerField( default=0,verbose_name="Cantidad",null=False)
    disponible=models.PositiveIntegerField(verbose_name="Cantidad disponible",null=True)
    genero_libro=models.ForeignKey(genero,blank=True,verbose_name="Libro genero",on_delete=models.CASCADE, related_name="libro_genero")
    
    def __str__(self):
        return "Libro: "+self.titulo
    


           