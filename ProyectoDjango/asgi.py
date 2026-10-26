"""
ASGI config for ProyectoDjango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Configura la variable de entorno predeterminada para que Django sepa 
# cuál es el archivo de configuración del proyecto ('ProyectoDjango.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoDjango.settings')

# Crea y expone el objeto ASGI ejecutable a nivel de módulo, 
# necesario para que los servidores web asíncronos gestionen las peticiones del proyecto
application = get_asgi_application()