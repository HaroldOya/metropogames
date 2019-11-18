from django.shortcuts import render
from django.utils import timezone
from .models import Juego
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request, 'metropogames/index.html' )


def formulario(request):
    return render(request, 'metropogames/formulario.html' )

def loginvista(request):
    return render(request, 'metropogames/loginvista.html' )

def galeria(request):
    return render(request, 'metropogames/galeria.html' )


def nuevojuego(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            juego = form.save(commit=False)
            juego.save()
            return redirect('metropogames/galeria.html')
    else:
        form = PostForm()
    return render(request, 'metropogames/nuevojuego.html', {'form': form})
