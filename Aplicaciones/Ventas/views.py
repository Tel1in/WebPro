from django.shortcuts import render , redirect
from .models import Clientes
from django.contrib import messages

# Create your views here.

def home(request):
    cliente = Clientes.objects.all()
    messages.success(request, '¡ Clientes Listados !')
    return render(request,"gestionClientes.html", {"cliente" : cliente})

def registrarCliente(request):
    id = request.POST['txtId']
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTel']
    edad = request.POST['txtEdad']

    cliente = Clientes.objects.create(id=id, nombre=nombre , telefono=telefono , edad=edad)
    messages.success(request, '¡ Clientes Registrado !')
    return redirect('/')

def actualizarCliente(request , id):
    cliente = Clientes.objects.get(id=id)
   
    return render(request,"modificarCliente.html",{"cliente": cliente})
    
def editarCliente(request):
    id = request.POST['txtId']
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTel']
    edad = request.POST['txtEdad']
    cliente = Clientes.objects.get(id=id)
    cliente.nombre = nombre
    cliente.telefono = telefono
    cliente.edad = edad
    cliente.save()
    messages.success(request, '¡ Cliente Actualizado !')
    return redirect('/')


def eliminarCliente(request , id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    messages.success(request, '¡ Cliente Eliminado !')
    return redirect('/')