from django.urls import path
from . import views

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('libros/eliminar/<int:id_libro>', views.delete, name='delete'),
    path("libros/prestamo/<int:id_libro>",views.prestamo,name="prestamo"),
    path('libros/historial', views.historial, name='history')
]