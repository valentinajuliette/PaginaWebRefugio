# Se crea un modelo que represente los perritos del refugio.
# Este modelo utilizará el ORM de Django para interactuar con la base de datos.

from django.db import models

class Perrito(models.Model):
    nombre = models.CharField(max_length=255) # Nombre del perrito.
    descripcion = models.TextField() # Breve descripción del perrito.
    años = models.IntegerField() # edad del perrito con dos decimales.
    tamaño = models.CharField(max_length=100) # tamaño del perrito.
    imagen = models.ImageField(upload_to='img/perritos/', null=True, blank=True) # Campo para cargar la imagen del perrito.

    def __str__(self):
        return self.nombre
