from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Perrito
from .forms import RegistroForm
from django.contrib import messages

def lista_perritos(request):
    perritos = Perrito.objects.all()
    return render(request, 'lista_perritos.html', {'perritos': perritos})

def pag_principal(request):
    perritos = Perrito.objects.all()  # Obtener todos los perritos
    return render(request, 'pag_principal.html', {'perritos': perritos})

def catalogo_perritos(request):
    return render(request, 'catalogo_perritos.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pag_principal')  # Redirige a la página principal después del login.
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')
