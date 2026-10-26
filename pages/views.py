from django.shortcuts import render, get_object_or_404
from .models import Page
from django.contrib.auth.decorators import login_required

# Decorador de seguridad: obliga a que el usuario haya iniciado sesión obligatoriamente para ver esta vista. 
# Si no está autenticado, lo redirige automáticamente a la ruta nombrada 'login'.
@login_required(login_url='login')
def pages(request, slug):
    # Buscar la página en la base de datos por su slug
    # get_object_or_404 intenta obtener el objeto Page que coincida con el slug recibido por la URL.
    # Si el registro no existe, Django interrumpe la ejecución y muestra automáticamente una página de error 404 (No Encontrado).
    page = get_object_or_404(Page, slug=slug)
    
    # Renderiza la plantilla HTML de detalle de la página enviando el objeto 'page' y su título en el diccionario de contexto
    return render(request, 'pages/page.html', {
        'page': page,
        'title': page.title
    })