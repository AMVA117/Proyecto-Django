from pages.models import Page

# Función de procesador de contexto (Context Processor)
def get_pages(request):
    # Consulta a la base de datos: trae únicamente las páginas marcadas como visibles (visible=True) y las ordena de forma ascendente por su campo 'order'
    pages = Page.objects.filter(visible=True).order_by('order')
    
    # Retorna un diccionario con los datos que estarán disponibles de forma global en todas las plantillas HTML del proyecto
    return {
        'pages': pages
    }