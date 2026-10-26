from django.apps import AppConfig

# 1. Clase de configuración de la aplicación 'blog'
class BlogConfig(AppConfig):
    # 2. Define el tipo de campo automático por defecto para las claves primarias (IDs) en los modelos de esta app (genera enteros grandes autoincrementales de 64 bits)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 3. Indica el nombre de la aplicación dentro del proyecto (debe coincidir con la carpeta)
    name = 'blog'
    
    # 4. Define el nombre legible o amigable para los seres humanos que aparecerá en el panel de administración de Django (en lugar de ver solo "Blog", se verá "Gestion del Blog")
    verbose_name = 'Gestion del Blog'