from pages.models import Page

def get_pages(request):
    pages = Page.objects.all()
    return {
        'pages': pages
    }