from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_vehiculo, name= 'inicio_vehiculo'),
    path('listar-vehiculos', views.listar_vehiculos, name='listar-vehiculos'),
    path('form-registro', views.registrar_vehiculo),
    path('crear-vehiculo', views.crear_vehiculo),
    path('editar-vehiculo/<str:patente>/', views.editar_vehiculo, name='editar-vehiculo'),
    path('editar-vehiculo/', views.editar_vehiculo, name='editar-vhcl'),
    path('eliminar-vehiculo/<str:patente>/', views.eliminar_vehiculo, name='eliminar-vehiculo'),
    path('buscar-vehiculo', views.buscar_vehiculo, name='buscar-vehiculo'),
    path('buscar-vehiculo-dato', views.buscar_vehiculo_dato, name='buscar-vehiculo-dato'),
    path('buscar-vehiculo-fecha', views.buscar_vehiculo_fecha, name='buscar-vehiculo-fecha')


]