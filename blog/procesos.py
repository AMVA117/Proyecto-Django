from blog.models import Article, Category

# 1. Definición del procesador de contexto (Context Processor)
# Un context_processor en Django es una función que inyecta variables globales 
# disponibles automáticamente en todas las plantillas HTML del proyecto.
def get_categories(request):
    
    # 2. Filtrado optimizado de categorías en uso:
    # - Article.objects.filter(public=True): Filtra solo los artículos que están publicados.
    # - .values_list('categories', flat=True): Extrae únicamente los IDs de las categorías asociadas a esos artículos (flat=True devuelve una lista plana en lugar de tuplas).
    # - .distinct(): Elimina los IDs duplicados para que cada categoría aparezca una sola vez.
    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True).distinct()
    
    # 3. Consulta de categorías filtradas y optimizadas:
    # - Category.objects.filter(id__in=categories_in_use): Busca solo aquellas categorías cuyos IDs estén presentes en la lista obtenida antes.
    # - .values_list('id', 'name'): Devuelve únicamente una lista de tuplas con el ID y el nombre de cada categoría para optimizar memoria.
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')

    # 4. Retorno del diccionario de contexto:
    # Las llaves de este diccionario se convierten en variables accesibles directamente en cualquier plantilla HTML 
    # (siempre que este archivo esté registrado en settings.py bajo TEMPLATES -> OPTIONS -> context_processors).
    return {
        'categories': categories,
        'ids': categories_in_use
    }