from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página principal (raíz del sitio web, ej. misitio.com/), 
    # asociada a la función index de views.py y nombrada 'index'.
    path('', views.index, name='index'),
    
    # Ruta alternativa para la página de inicio (ej. misitio.com/inicio/), 
    # que apunta a la misma vista index pero con el nombre 'inicio'.
    path('inicio/', views.index, name='inicio'),
    
    # Ruta para la página de registro de usuarios (ej. misitio.com/registro/), 
    # vinculada a la función register_page y nombrada 'register'.
    path('registro/', views.register_page, name='register'),
    
    # Ruta para la página de inicio de sesión (ej. misitio.com/login/), 
    # vinculada a la función login_page y nombrada 'login'.
    path('login/', views.login_page, name='login'),
    
    # Ruta para cerrar la sesión del usuario (ej. misitio.com/logout/), 
    # vinculada a la función logout_user y nombrada 'logout'.
    path('logout/', views.logout_user, name='logout'),
]