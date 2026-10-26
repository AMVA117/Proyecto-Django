"""
URL configuration for ProyectoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ProyectoDjango import settings


urlpatterns = [
    # Ruta para acceder al panel de administración predeterminado de Django (ej. /admin/)
    path('admin/', admin.site.urls), #panel de administración por defecto
    
    # Incluye y enlaza todas las rutas definidas en el archivo urls.py de la aplicación 'mainapp' a la raíz del sitio
    path('',include('mainapp.urls')), #incluimos las urls de la app mainapp
    
    # Incluye las rutas de la app 'pages' bajo el prefijo 'pagina/' (ej. /pagina/mi-slug/)
    path('pagina/',include('pages.urls')), #incluimos las urls de la app pages
    
    # Incluye y enlaza las rutas de la aplicación 'blog' a la raíz del sitio
    path('',include('blog.urls')),
]

# Condicional de desarrollo: si DEBUG está activo, permite servir archivos multimedia (imágenes subidas) localmente
if settings.DEBUG:
    from django.conf.urls.static import static
    # Agrega a urlpatterns la ruta necesaria para servir archivos estáticos/multimedia desde MEDIA_ROOT usando MEDIA_URL
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)