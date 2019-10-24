from django.shortcuts import render
from django.utils import timezone
from .models import Juego

# Create your views here.

def index(request):
    return render(request, 'metropogames/index.html' )


def formulario(request):
    return render(request, 'metropogames/formulario.html' )

def loginvista(request):
    return render(request, 'metropogames/loginvista.html' )

def galeria(request):
    return render(request, 'metropogames/galeria.html' )



