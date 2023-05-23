from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registrar-usuario', views.registrar_usuario, name = 'registrar-usuario'),
    path('ingresar-usuario', views.ingresar_usuario, name = 'ingresar-usuario'),
    path('actualizar_usuario/<str:username>/', views.actualizar_usuario, name = 'actualizar_usuario'),
    path('editar_usuario', views.actualizar_usuario, name = 'editar_usuario'),
    path('eliminar_usuario/<str:username>/', views.eliminar_usuario, name = 'eliminar_usuario'),
    path('listar-usuarios', views.listar_usuarios, name = 'listar-usuarios'),
    
]