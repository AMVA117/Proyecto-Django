from django.shortcuts import render, get_object_or_404
from .models import Page

def pages(request, slug):
    # Buscar la página en la base de datos por su slug
    page = get_object_or_404(Page, slug=slug)
    
    return render(request, 'pages/page.html', {
        'page': page,
        'title': page.title
    })