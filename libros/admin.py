from django.contrib import admin
from .models import Libro,genero,persona
# Register your models here.
admin.site.register(Libro)
admin.site.register(genero)
admin.site.register(persona)