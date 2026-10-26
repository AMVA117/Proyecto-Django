"""
WSGI config for ProyectoDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Configura la variable de entorno predeterminada para que Django sepa 
# cuál es el archivo de configuración del proyecto ('ProyectoDjango.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoDjango.settings')

# Crea y expone el objeto WSGI ejecutable a nivel de módulo, 
# que es la interfaz estándar utilizada por los servidores web síncronos tradicionales (como Gunicorn o uWSGI) para comunicarse con Django
application = get_wsgi_application()