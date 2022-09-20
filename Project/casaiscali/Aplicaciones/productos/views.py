from django.shortcuts import render, redirect
from .models import Producto


# Create your views here.

#Aqui se van a listar los producto registrados
def productos(request):
    pListados = Producto.objects.all()
    return render(request, "productos/productos.html", {"products" : pListados})

