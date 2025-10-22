from django.urls import path
from . import views

app_name = 'app_proveedor'

urlpatterns = [
    path('', views.listar_proveedores, name='listar_proveedores'),
    path('proveedor/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('crear/', views.crear_proveedor, name='crear_proveedor'),
    path('editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),
]