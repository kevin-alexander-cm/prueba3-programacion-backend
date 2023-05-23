from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_oficina, name ='inicio_oficina'),
    path('registrar_oficina', views.registrar_oficina, name ='registrar_oficina'),
    path('crear_oficina', views.crear_oficina, name ='crear_oficina'),
    path('listar_oficina', views.listar_oficina, name ='listar_oficina'),
    path('editar_oficina/<int:nro_article>/', views.editar_oficina, name ='editar_oficina'),
    path('editar_oficina/', views.editar_oficina, name ='ofi'),
    path('eliminar_oficina/<int:nro_article>/', views.eliminar_oficina, name ='eliminar_oficina'),
    path('buscar_oficina/', views.buscar_oficina, name ='buscar_oficina'),
    path('buscar_oficina_dato/', views.buscar_oficina_dato, name ='buscar-oficina-dato')
]