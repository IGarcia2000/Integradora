from django.db import models

# Create your models here.
class Producto(models.Model):
    image = models.ImageField(upload_to = 'static/imgp')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.BooleanField()

    def str(self):
        texto = "{0} {1} {2} {3} {4}"
        return texto.format(self.id, self.image, self.nombre, self.descripcion, self.precio)
