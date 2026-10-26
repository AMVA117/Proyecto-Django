from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# ---------------------------------------------------------
# 1. MODELO CATEGORY (Categorías para clasificar los artículos)
# ---------------------------------------------------------
class Category(models.Model):
    # Campo de texto corto para el nombre de la categoría (máximo 100 caracteres)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    
    # Campo de texto para una breve descripción (máximo 225 caracteres)
    description = models.CharField(max_length=225, verbose_name='Descripción')
    
    # Fecha y hora de creación automática (auto_now_add registra la fecha exacta solo al crearlo por primera vez)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:  # Metadatos para configurar el comportamiento y nombres en el panel de administración
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    # Método __str__: Define cómo se va a mostrar el objeto visualmente en texto (ej. en los desplegables del admin)
    def __str__(self):
        return self.name

# ---------------------------------------------------------
# 2. MODELO ARTICLE (Artículos o entradas del blog)
# ---------------------------------------------------------
class Article(models.Model):
    # Título principal del artículo (hasta 150 caracteres)
    title = models.CharField(max_length=150, verbose_name='Título')
    
    # Contenido enriquecido: Utiliza el paquete CKEditor para permitir formato de texto avanzado (negritas, enlaces, tablas, etc.)
    content = RichTextField(verbose_name='Contenido')
    
    # Campo de imagen: Guarda la ruta de la imagen, con valor por defecto 'null' y se sube automáticamente a la carpeta 'articles/' dentro de media
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="articles")
    
    # Campo booleano (Verdadero/Falso) para indicar si el artículo está público o en borrador
    public = models.BooleanField(verbose_name='¿Publicado?')
    
    # Relación de Muchos a Uno (ForeignKey) con el modelo User por defecto de Django.
    # on_delete=models.CASCADE significa que si se borra el usuario, se borran sus artículos. null=True y blank=True permiten que sea opcional.
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE, null=True, blank=True)
    
    # Relación de Muchos a Muchos (ManyToManyField) con el modelo Category. Un artículo puede pertenecer a varias categorías y viceversa. blank=True permite guardarlo sin categorías.
    categories = models.ManyToManyField(Category, verbose_name='Categorías', blank=True)
    
    # Fechas de control de auditoría (creado y última actualización automática)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        # Orden por defecto: El signo menos (-) indica orden descendente, mostrando los artículos más nuevos primero
        ordering = ['-created_at']

    # Método __str__: Devuelve el título del artículo para identificarlo fácilmente en consultas y en el panel de administración
    def __str__(self):
        return self.title