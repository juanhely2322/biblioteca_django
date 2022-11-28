from django import forms
from .models import Libro,persona

class LibroForm(forms.ModelForm):
    class Meta:
        
        model =Libro
        fields = ["titulo","descripcion","cantidad","imagen","genero_libro"]


class personaForm(forms.ModelForm):
    class Meta:
        model=persona
        fields=["nombre","apellido", "cedula","telefono","email","direccion","edad"]