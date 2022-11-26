from django.shortcuts import render, redirect,get_object_or_404
from .models import Libro,genero
from django.db import IntegrityError
from django.core.files.storage import FileSystemStorage
from django.db.utils import IntegrityError

from .forms import LibroForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
   
    return render(request, 'libros/index.html', {'libros':libros})

def crear (request):
    gene=genero.objects.all()
    if request.method == "GET":
        return render(request, 'libros/crear.html', {'formulario': LibroForm,"genero":gene })
    else: 
        
        try:
            form=LibroForm(request.POST,request.FILES)
            if form.is_valid():
                print(form.is_valid())
                image=request.FILES["imagen"]
                im=FileSystemStorage()
                imageName=im.save(image.name,image)
                lib=Libro()
        
                lib.titulo=form.cleaned_data["titulo"]
                lib.cantidad=form.cleaned_data["cantidad"]
                lib.disponible=form.cleaned_data["cantidad"]
                lib.genero_libro=form.cleaned_data["genero_libro"]
                print("este es el valor;  "+str(form.cleaned_data["genero_libro"]))
                lib.imagen=im.url(imageName)
                lib.descripcion=form.cleaned_data["descripcion"]
                lib.save()
                return render(request, 'libros/crear.html', {'formulario': LibroForm ,"error":"Se ha guardado con exito","genero":gene}) 
           
        except ValueError:
            
            return render(request, 'libros/crear.html', {'formulario': LibroForm ,"error":"ha ocurrido un error","genero":gene})

    

def editar (request):
    return render(request, 'libros/editar.html')


def delete (request, id_libro):
    print(id_libro)
    #libro=get_object_or_404(Libro, pk=id_libro)
    try:
            libro=Libro.objects.get(pk=id_libro)
            libro.delete()
            return redirect("libros")

    except IntegrityError :
        
        return render(request, 'libros/index.html', {'libros':libros,"error":"ha ocurrido un error"})      
   
   
#prestamo de libros

def prestamo(request):
    return render(request, 'libros/index.html',)




