from django.shortcuts import render

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import (
    AutorSerializer, EditorialSerializer, LibroSerializer,
    MiembroSerializer, PrestamoSerializer
)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.model.objects.all() if hasattr(Autor, 'model') else Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'apellido']
    ordering_fields = ['nombre', 'apellido']


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre']


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.select_related('autor', 'editorial').all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Filtros básicos solicitados:
    filterset_fields = {
        # por id o por igualdad exacta
        'autor': ['exact'],
        'editorial': ['exact'],
        'anio_publicacion': ['exact', 'gte', 'lte'],
    }
    # Búsqueda de texto (título/isbn) adicional
    search_fields = ['titulo', 'isbn', 'resumen']
    ordering_fields = ['anio_publicacion', 'titulo']


class MiembroViewSet(viewsets.ModelViewSet):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'apellido', 'email']
    ordering_fields = ['apellido', 'nombre', 'fecha_membresia']


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.select_related('libro', 'miembro').all()
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # Filtros básicos solicitados:
    filterset_fields = {
        'miembro': ['exact'],            # /prestamos/?miembro=3
        'libro': ['exact'],              # /prestamos/?libro=10
        'fecha_prestamo': ['exact', 'gte', 'lte'],   # rango
        'fecha_devolucion': ['isnull'],  # /prestamos/?fecha_devolucion__isnull=true (préstamos activos)
    }
    ordering_fields = ['fecha_prestamo']
