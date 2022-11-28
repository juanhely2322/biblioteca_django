from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, genero, persona
from django.db import connection
from django.core.files.storage import FileSystemStorage
from django.db.utils import IntegrityError
import os
from .forms import LibroForm, personaForm


def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def libros(request):
    libros = Libro.objects.all()

    return render(request, 'libros/index.html', {'libros': libros})


def crear(request):
    gene = genero.objects.all()
    if request.method == "GET":
        return render(request, 'libros/crear.html', {'formulario': LibroForm, "genero": gene})
    else:

        try:
            form = LibroForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.is_valid())
                lib = Libro()

                try:
                    # image=request.FILES["imagen"]
                    # im=FileSystemStorage()
                    # imageName=im.save(image.name,image)
                    #lib.imagen= str(im.url(imageName))
                    lib.titulo = form.cleaned_data["titulo"]
                    lib.cantidad = form.cleaned_data["cantidad"]
                    lib.disponible = form.cleaned_data["cantidad"]
                    lib.genero_libro = form.cleaned_data["genero_libro"]
                    lib.imagen = request.FILES["imagen"]
                except:
                    lib.imagen = "media/imagen_libro/default.png"

                lib.descripcion = form.cleaned_data["descripcion"]
                print("este es el valor;  " +
                      str(form.cleaned_data["genero_libro"]))

                print("imagen guardada en: "+str(lib.imagen))

                lib.save()
                return render(request, 'libros/crear.html', {'formulario': LibroForm, "error": "Se ha guardado con exito", "genero": gene})

        except ValueError:

            return render(request, 'libros/crear.html', {'formulario': LibroForm, "error": "ha ocurrido un error", "genero": gene})


def editar(request):
    return render(request, 'libros/editar.html')


def delete(request, id_libro):
    print(id_libro)
    #libro=get_object_or_404(Libro, pk=id_libro)
    try:
        libro = Libro.objects.get(pk=id_libro)
        image = libro.imagen
        libro.delete()
        if image != "media/imagen_libro/default.png":
            os.remove(image)
        return redirect("libros")

    except:

        return render(request, 'libros/index.html', {'libros': libros, "error": "ha ocurrido un error"})


# prestamo de libros

def prestamo(request, id_libro):

    print(id_libro)

    if request.method == "GET":
        return render(request, 'libros/prestamo.html')
    else:
        if request.method == "POST":
            lib = Libro.objects.get(pk=id_libro)
            person = persona()
            person.nombre = request.POST["nombre"]
            person.apellido = request.POST["apellido"]
            person.cedula = request.POST["cedula"]
            person.telefono = request.POST["telefono"]
            person.direccion = request.POST["direccion"]
            person.email = request.POST["email"]
            person.edad = request.POST["edad"]
            person.save()
            lib.prestamo.add(person)
            return redirect("libros")
            print(person.id)

       # return render(request, 'libros/prestamo.html', {"error": "algo ha ocurrido"})

def historial(request):
    cursor=connection.cursor()
    cursor.execute("""SELECT  * from libreria.libros_persona  inner join libros_libro_prestamo
on libros_libro_prestamo.persona_id=libreria.libros_persona.id
inner join libros_libro  on  libros_libro.id= libros_libro_prestamo.libro_id;""")
    r=cursor.fetchone()
    print(r)
    return render(request,"libros/history.html",{"historys":r})