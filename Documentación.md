Parcial desarrollado por: Luis Francisco Torres y Andrey Felipe Suarez Cano 
Este proyecto consiste en el desarrollo de una API RESTful con Django REST Framework para gestionar una biblioteca.
El sistema permite administrar Autores, Editoriales, Libros, Miembros y Préstamos, incluyendo sus relaciones, operaciones CRUD y consultas filtradas.

La API está diseñada para ser consumida por aplicaciones web, móviles o clientes externos (Postman, cURL, etc.).
-Tecnologías utilizadas
Python 
Django 
Django REST Framework
django-filter
PostgreSQL
Entidades y Relaciones
Autor
Atributos: id, nombre, apellido, biografía (opcional).
Relación: 1 autor → N libros.
Editorial
Atributos: id, nombre, dirección, teléfono (opcional).
Relación: 1 editorial → N libros.
Libro
Atributos: id, título, resumen, ISBN, año_publicación.
Relaciones:
FK → Autor
FK → Editorial
Relación: 1 libro → N préstamos.
Miembro
Atributos: id, nombre, apellido, email, fecha_membresía.
Relación: 1 miembro → N préstamos.
Préstamo
Atributos: id, fecha_prestamo, fecha_devolucion (opcional).
Relaciones:
FK → Libro
FK → Miembro
Funcionalidades Implementadas
CRUD completo para todas las entidades:
Crear, listar, consultar detalle, actualizar y eliminar.
Filtros básicos:
Buscar libros por autor, editorial, año o título.
Consultar préstamos por miembro, libro, rango de fechas o préstamos activos.
Serialización a JSON con ModelSerializer.
Rutas con Router DRF en /api/.
Paginación y búsqueda configuradas.