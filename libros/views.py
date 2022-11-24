from django.shortcuts import render, redirect,get_object_or_404
from .models import Libro
from django.db import IntegrityError
from django.core.files.storage import FileSystemStorage
from .forms import LibroForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
   
    return render(request, 'libros/index.html', {'libros':libros})

def crear (request):
    if request.method == "GET":
        return render(request, 'libros/crear.html', {'formulario': LibroForm })
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
                lib.imagen=im.url(imageName)
                lib.descripcion=form.cleaned_data["descripcion"]
                lib.save()
                return render(request, 'libros/crear.html', {'formulario': LibroForm ,"error":"se ha guardado con exito"}) 
           
        except ValueError:
            
            return render(request, 'libros/crear.html', {'formulario': LibroForm ,"error":"ha ocurrido un error"})

    

def editar (request):
    return render(request, 'libros/editar.html')


def delete (request, id_libro):
    print(id_libro)
    libro=get_object_or_404(Libro, pk=id_libro)
    try:
            libro.delete()
            return redirect("libros")
    
    except ValueError:
        
        return render(request, 'libros/index.html', {'libros':libros,"error":"ha ocurrido un error"})      
   
   





