from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('listar_productos')), 
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/<int:producto_id>/', views.ver_detalle, name='ver_detalle'),
]