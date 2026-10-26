from django.contrib import admin
from .models import Page

# Configuración extra para personalizar el panel de administración del modelo Page
class PageAdmin(admin.ModelAdmin):
    # Campos de solo lectura (el usuario no puede modificarlos en el admin, útil para fechas automáticas)
    readonly_fields = ('created_at', 'updated_at')
    # Campos en los que se podrá buscar mediante una barra de búsqueda en el admin
    search_fields = ('title', 'content')
    # Filtros laterales para filtrar registros rápidamente (en este caso por visibilidad)
    list_filter = ('visible',)
    # Columnas que se mostrarán en la tabla principal del listado de páginas en el admin
    list_display = ('title', 'visible', 'created_at')
    # Orden por defecto de los registros (el signo menos '-' indica orden descendente, del más reciente al más antiguo)
    ordering = ('-created_at',)

# Register your models here.
# Registra el modelo Page aplicando la configuración personalizada de PageAdmin en el panel de control
admin.site.register(Page, PageAdmin)


# Register your models here.
# Personalización de los textos globales de la interfaz del panel de administración de Django
title = "Proyecto con Django"
subtitle = "Panel de Gestion"

# Texto que aparece en la parte superior de todas las páginas del admin (barra de navegación superior)
admin.site.site_header = title
# Texto que aparece en la pestaña del navegador web
admin.site.site_title = title
# Título principal que se ve en la página de bienvenida (índice) del panel de administración
admin.site.index_title = subtitle