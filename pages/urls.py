from django.urls import path 
from . import views

urlpatterns = [
    # Ruta dinámica que captura un parámetro de texto (string) llamado 'slug' directamente desde la URL 
    # (por ejemplo, /mi-pagina-estatica/), lo pasa como argumento a la función 'pages' de 'views.py', 
    # y nombra la ruta como 'page' para poder referenciarla fácilmente en las plantillas.
    path('<str:slug>/', views.pages, name="page"),
]