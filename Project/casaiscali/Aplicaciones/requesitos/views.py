from django.shortcuts import render, redirect

# Create your views here.
def servicios(request):
    return render(request, "infogen/servicios.html")

def eventos(request):
    return render(request, "infogen/eventos.html")

def zpsico(request):
    return render(request, "infogen/zpsicologica.html")

def zgrafica(request):
    return render(request, "infogen/zdgrafico.html")