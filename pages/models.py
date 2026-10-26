from django.db import models
from ckeditor.fields import RichTextField

# Definición del modelo 'Page' para gestionar páginas estáticas en la base de datos a través del ORM de Django
class Page(models.Model):
    # Campo de texto corto para el título de la página (máximo 150 caracteres)
    title = models.CharField(max_length=150, verbose_name="Título")
    
    # Campo de texto enriquecido provisto por CKEditor para permitir formato avanzado (negritas, enlaces, imágenes, etc.)
    content = RichTextField(verbose_name="Contenido")
    
    # Campo para la URL amigable (slug). 'unique=True' garantiza que no se repitan URLs entre páginas
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    
    # Campo booleano (Verdadero/Falso) para indicar si la página está publicada y visible en el menú web
    visible = models.BooleanField(verbose_name="¿Visible?")
    
    # Campo numérico entero para controlar la posición en la que aparecerá la página (por defecto es 0)
    order = models.IntegerField(default=0, verbose_name="Orden") # <-- Agrega este campo
    
    # Fecha y hora de creación. 'auto_now_add=True' asigna automáticamente la fecha exacta al crear el registro por primera vez
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    
    # Fecha y hora de actualización. 'auto_now=True' actualiza la fecha automáticamente cada vez que se guarda el registro
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    # Clase interna Meta para configurar opciones de comportamiento y metadatos del modelo
    class Meta:
        # Nombre singular del modelo para mostrar amigablemente en el panel de administración
          verbose_name = "Página"
        # Nombre plural del modelo para el panel de administración
          verbose_name_plural = "Páginas"
        # Criterio de ordenamiento por defecto al consultar las páginas: primero por el campo 'order' y luego alfabéticamente por 'title'
          ordering = ['order', 'title'] # <-- Esto ordena por el campo orden por defecto

    # Método especial __str__ para definir cómo se representará el objeto como cadena de texto (ej. en el panel admin o consola)
    def __str__(self):
        # Retorna el título de la página como identificador visual del objeto
        return self.title