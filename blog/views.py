from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required
# Create your views here.

# ---------------------------------------------------------
# 1. VISTA DE LISTADO DE ARTÍCULOS (Con Paginación)
# ---------------------------------------------------------
# El decorador @login_required protege la vista: solo permite el acceso a usuarios autenticados.
# Si no ha iniciado sesión, lo redirige automáticamente a la URL nombrada como 'login'.
@login_required(login_url='login')
def list(request):
    # Trae todos los artículos de la base de datos ordenados según el modelo
    articles = Article.objects.all()
    
    # Crea un objeto Paginator dividiendo la lista de artículos en bloques de 2 por página
    paginator = Paginator(articles, 2)  
    
    # Obtiene el número de página actual desde los parámetros GET de la URL (ej. ?page=2)
    page = request.GET.get('page')
    
    # Obtiene los artículos correspondientes a esa página (gestiona errores si la página no existe o no es un número)
    page_articles = paginator.get_page(page)

    # Renderiza la plantilla HTML enviando un diccionario de contexto con el título y los artículos paginados
    return render(request, 'articles/list.html', {
        'title' : 'Articulos',
        'articles' : page_articles
    })

# ---------------------------------------------------------
# 2. VISTA DE ARTÍCULOS FILTRADOS POR CATEGORÍA
# ---------------------------------------------------------
@login_required(login_url='login')
def category(request, category_id):
    # get_object_or_404 busca la categoría por su ID. Si no existe, lanza un error HTTP 404 (Página no encontrada) automáticamente.
    category = get_object_or_404(Category, id=category_id)
    
    # Filtra los artículos de la base de datos que estén asociados a esa categoría específica
    articles = Article.objects.filter(categories=category_id)

    # Renderiza la plantilla de categorías pasando el objeto categoría y su lista de artículos asociados
    return render(request, 'categories/category.html', {
        'category' : category,
        'articles' : articles
    })

# ---------------------------------------------------------
# 3. VISTA DE DETALLE DE UN ARTÍCULO INDIVIDUAL
# ---------------------------------------------------------
@login_required(login_url='login')
def article(request, article_id):
    # Busca el artículo específico por su ID. Si el ID no existe en la base de datos, muestra un error 404.
    article = get_object_or_404(Article, id=article_id)

    # Renderiza la plantilla de detalle pasando el objeto artículo único
    return render(request, 'articles/detail.html', {
        'article' : article
    })