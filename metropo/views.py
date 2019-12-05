from django.shortcuts import render
from django.utils import timezone
from .models import Juego
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'metropogames/index.html' )


def welcome(request):
    if request.user.is_authenticated:
        return render(request, "registration/welcome.html")
    return redirect(request, '/login')

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/login')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/formulario.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/loginvista.html", {'form': form})

def logout(request):
    # Redireccionamos a la portada
    do_logout(request)
    return redirect('/')

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
