from blog.models import Article, Category

def get_categories(request):
    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True).distinct()
    # Trae únicamente las categorías marcadas como visibles y las ordena por su campo 'order'
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')

    
    return {
        'categories': categories,
        'ids': categories_in_use
    }