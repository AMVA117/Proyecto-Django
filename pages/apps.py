from django.apps import AppConfig

# Clase de configuración para la aplicación 'pages'
class PagesConfig(AppConfig):
    # Define el tipo de campo automático por defecto para las claves primarias (IDs) de los modelos en esta app (un entero grande de 64 bits)
    default_auto_field = 'django.db.models.BigAutoField'
    # Indica el nombre técnico de la aplicación dentro del proyecto de Django
    name = 'pages'
    # Nombre descriptivo y legible que aparecerá en el panel de administración de Django para identificar a esta app
    verbose_name = 'Gestión de Páginas'