from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCliente/', views.registrarCliente),
    path('actualizarCliente/<id>',views.actualizarCliente),
    path('editarCliente/',views.editarCliente),
    path('eliminarCliente/<id>',views.eliminarCliente)
]