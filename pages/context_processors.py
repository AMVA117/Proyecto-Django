from pages.models import Page

def get_pages(request):
    # Trae únicamente las páginas marcadas como visibles y las ordena por su campo 'order'
    pages = Page.objects.filter(visible=True).order_by('order')
    
    return {
        'pages': pages
    }