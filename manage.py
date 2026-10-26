#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Configura la variable de entorno predeterminada para que Django sepa 
    # qué archivo de configuraciones utilizar al ejecutar comandos por consola ('ProyectoDjango.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoDjango.settings')
    
    try:
        # Intenta importar la función principal para ejecutar comandos de administración desde la línea de comandos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si falla la importación, lanza un error explicativo indicando que Django podría no estar instalado 
        # o que se olvidó activar el entorno virtual (virtualenv)
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    # Ejecuta el comando de administración utilizando los argumentos pasados en la terminal (sys.argv), 
    # por ejemplo: python manage.py runserver, python manage.py migrate, etc.
    execute_from_command_line(sys.argv)


# Comprueba si el script se está ejecutando directamente desde la terminal para invocar la función principal
if __name__ == '__main__':
    main()