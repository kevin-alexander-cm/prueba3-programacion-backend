from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_computacion, name = 'inicio_computacion'),
    path('registrar_computacion', views.registrar_computacion, name = 'registrar_computacion'),
    path('crear_computacion', views.crear_computacion, name = 'crear_computacion'),
    path('listar_computacion', views.listar_computacion, name = 'listar_computacion'),
    path('editar_computacion', views.editar_computacion, name = 'editar_computacion'),
    path('editar_computacion/<str:nro_insumo>', views.editar_computacion, name = 'editar_computacion'),
    path('eliminar_computacion/<str:nro_insumo>', views.eliminar_computacion, name = 'eliminar_computacion'),

]