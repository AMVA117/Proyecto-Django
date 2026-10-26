from django.urls import path
from . import views

# 1. Lista de URLs (Enrutamiento de la aplicación)
# El objeto urlpatterns mapea las rutas web (URLs) con las funciones correspondientes (vistas) definidas en views.py.
urlpatterns = [
    # 2. Ruta para el listado general de artículos:
    # - Patrón: 'articulos/' (ej. misitio.com/articulos/)
    # - Vista: views.list (la función que procesa la petición)
    # - Nombre (name): 'list_articles' (etiqueta única para referenciar esta ruta desde las plantillas HTML con {% url 'list_articles' %})
    path('articulos/', views.list, name='list_articles'),

    # 3. Ruta para filtrar artículos por categoría:
    # - Patrón: 'categoria/<int:category_id>/' (ej. misitio.com/categoria/5/)
    # - <int:category_id>: Convierte el segmento de la URL en un número entero (int) y lo pasa como parámetro (category_id) a la función de la vista.
    # - name='category': Etiqueta para generar la URL de forma dinámica en los enlaces del HTML.
    path('categoria/<int:category_id>/', views.category, name='category'),

    # 4. Ruta para ver el detalle de un artículo específico:
    # - Patrón: 'articulo/<int:article_id>/' (ej. misitio.com/articulo/12/)
    # - <int:article_id>: Captura el ID numérico del artículo desde la URL y se lo inyecta como argumento a la vista `views.article`.
    # - name='article': Nombre clave utilizado en los enlaces de las tarjetas de los artículos (ej. {% url 'article' article.id %}).
    path('articulo/<int:article_id>/', views.article, name='article'),
]