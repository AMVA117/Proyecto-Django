from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# Vista de la página principal (index)
def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

# otra ruta (Vista de la página "Sobre Nosotros")
def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre Nosotros'
    })

# Vista para el registro de nuevos usuarios
def register_page(request):
    # Si el usuario ya inició sesión, se le impide ver el registro y se redirige al inicio
    if request.user.is_authenticated:
        return redirect('inicio')  # Redirige a la página de inicio si el usuario ya está autenticado
    
    # Instancia un formulario de registro vacío
    register_form = RegisterForm()
    
    # Si el usuario envía el formulario mediante POST
    if request.method == 'POST':
        # Rellena el formulario con los datos enviados por el usuario
        register_form = RegisterForm(request.POST)
        # Valida que los datos cumplan con las reglas del formulario
        if register_form.is_valid():
            # Guarda el nuevo usuario en la base de datos (con contraseña cifrada automáticamente)
            register_form.save()
            # Muestra un mensaje de éxito temporal al usuario
            messages.success(request, 'Se ha registrado correctamente')
            # Redirige al inicio tras un registro exitoso
            return redirect('inicio')  # Asegúrate de que coincida con el name de tu urls.py
            
    # Renderiza la plantilla de registro enviando el formulario y el título en el contexto
    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })

# Vista para el inicio de sesión (Login)
def login_page(request):
    # Si ya está autenticado, lo redirige al inicio
    if request.user.is_authenticated:
        return redirect('inicio')  # Redirige a la página de inicio si el usuario ya está autenticado
    else:
        # Si envía credenciales por método POST
        if request.method == 'POST':
            # Captura el usuario y la contraseña enviados
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Verifica si las credenciales son correctas en la base de datos
            user = authenticate(request, username=username, password=password)
            # Si el usuario existe y las credenciales son válidas
            if user is not None:
                # Inicia sesión formalmente creando la sesión HTTP
                login(request, user)
                # Redirige al inicio
                return redirect('inicio')  # Redirige a la página de inicio después del inicio de sesión
            else:
                # Si las credenciales fallan, muestra un mensaje de error
                messages.error(request, 'No ha podido iniciar sesión!!!')
                
        # Renderiza la plantilla de login si es una petición GET o si falló el inicio de sesión
        return render(request, 'users/login.html', {
            'title': 'Identificate'
        })

# Vista para el cierre de sesión (Logout)
def logout_user(request):
    # Cierra la sesión activa del usuario
    logout(request)
    # Redirige a la pantalla de login después de salir
    return redirect('login')  # Redirige a la página de login después del cierre de sesión