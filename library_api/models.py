from django.db import models

from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    biografia = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['apellido', 'nombre']

    def _str_(self):
        return f'{self.apellido}, {self.nombre}'


class Editorial(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        ordering = ['nombre']

    def _str_(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    isbn = models.CharField(max_length=20, unique=True)
    anio_publicacion = models.PositiveIntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='libros')
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT, related_name='libros')

    class Meta:
        ordering = ['-anio_publicacion', 'titulo']

    def _str_(self):
        return f'{self.titulo} ({self.anio_publicacion})'


class Miembro(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    fecha_membresia = models.DateField()

    class Meta:
        ordering = ['apellido', 'nombre']

    def _str_(self):
        return f'{self.apellido}, {self.nombre}'


class Prestamo(models.Model):
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='prestamos')

    class Meta:
        ordering = ['-fecha_prestamo']

    def _str_(self):
        return f'Préstamo #{self.id} - {self.libro} a {self.miembro}'