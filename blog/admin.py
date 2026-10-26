from django.contrib import admin
from .models import Category, Article

# 1. Configuración del Administrador para el modelo 'Category'
class CategoryAdmin(admin.ModelAdmin):
    # Campos de solo lectura: Evita que el usuario modifique la fecha de creación en el panel de administración
    readonly_fields = ('created_at',)
    
    # Columnas que se mostrarán en la tabla de la vista de listado en el admin
    list_display = ('name', 'created_at')
    
    # Campos habilitados para la barra de búsqueda del panel
    search_fields = ('name', 'created_at')

# 2. Configuración del Administrador para el modelo 'Article'
class ArticleAdmin(admin.ModelAdmin):
    # Campos que el usuario no podrá editar directamente desde el formulario del admin por seguridad/control
    readonly_fields = ('user', 'created_at', 'updated_at')
    
    # Campos por los que se podrá buscar. 
    # NOTA: 'user__username' y 'categories__name' usan doble guion bajo (__) para realizar "Lookups" a través de relaciones (ForeignKey y ManyToMany)
    search_fields = ('title', 'content', 'user__username', 'categories__name')  
    
    # Columnas visibles en la tabla de listado de artículos
    list_display = ('title', 'user', 'public', 'created_at')
    
    # Filtros laterales (sidebar) para ordenar y filtrar rápidamente los registros en el admin
    list_filter = ('public', 'user__username', 'categories__name')            

    # 3. Método personalizado para guardar el modelo de forma automática
    def save_model(self, request, obj, form, change):
        # Si el artículo es nuevo y no tiene un usuario asignado...
        if not obj.user_id:
            # Asigna automáticamente el ID del usuario que está haciendo la petición (el administrador logueado)
            obj.user_id = request.user.id
        # Guarda el objeto en la base de datos
        obj.save()

# 4. Registro de los modelos en el panel de administración de Django
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)