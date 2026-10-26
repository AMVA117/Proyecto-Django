from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 1. Creación del Formulario de Registro personalizado
# Hereda de 'UserCreationForm', un formulario prediseñado de Django que ya incluye 
# de forma automática la lógica segura de validación y almacenamiento cifrado de contraseñas.
class RegisterForm(UserCreationForm):

    # 2. Clase interna Meta: Configura los metadatos del formulario para enlazarlo con la base de datos
    class Meta:
        # Define que este formulario trabajará directamente con el modelo de Usuario por defecto de Django
        model = User
        
        # Especifica los campos de la tabla User que aparecerán en el formulario web 
        # para que el usuario los llene al momento de registrarse.
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']