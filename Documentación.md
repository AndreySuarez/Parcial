# Parcial - API Biblioteca  

**Desarrollado por:**  
- Luis Francisco Torres  
- Andrey Felipe Suárez Cano  

---

## Descripción del Proyecto
Este proyecto consiste en el desarrollo de una **API RESTful** con **Django REST Framework** para gestionar una biblioteca.  

El sistema permite administrar:  
- Autores  
- Editoriales  
- Libros  
- Miembros  
- Préstamos  

Incluyendo sus relaciones, operaciones **CRUD** y consultas filtradas.  

La API está diseñada para ser consumida por aplicaciones web, móviles o clientes externos (Postman, cURL, etc.).  

---

## Tecnologías Utilizadas
- **Python**  
- **Django**  
- **Django REST Framework**  
- **django-filter**  
- **PostgreSQL**  

---

## Entidades y Relaciones

### Autor
- **Atributos:** `id`, `nombre`, `apellido`, `biografía (opcional)`.  
- **Relación:** 1 autor → N libros.  

### Editorial
- **Atributos:** `id`, `nombre`, `dirección`, `teléfono (opcional)`.  
- **Relación:** 1 editorial → N libros.  

### Libro
- **Atributos:** `id`, `título`, `resumen`, `ISBN`, `año_publicación`.  
- **Relaciones:**  
  - FK → Autor  
  - FK → Editorial  
- **Relación:** 1 libro → N préstamos.  

### Miembro
- **Atributos:** `id`, `nombre`, `apellido`, `email`, `fecha_membresía`.  
- **Relación:** 1 miembro → N préstamos.  

### Préstamo
- **Atributos:** `id`, `fecha_prestamo`, `fecha_devolucion (opcional)`.  
- **Relaciones:**  
  - FK → Libro  
  - FK → Miembro  

---

##  Funcionalidades Implementadas
-  **CRUD completo** para todas las entidades: Crear, listar, consultar detalle, actualizar y eliminar.  
-  **Filtros básicos**:  
  - Buscar libros por autor, editorial, año o título.  
  - Consultar préstamos por miembro, libro, rango de fechas o préstamos activos.  
-  **Serialización a JSON** con `ModelSerializer`.  
-  **Rutas con Router DRF** en `/api/`.  
-  **Paginación y búsqueda** configuradas.  

---

##  Ejemplo de Endpoints

- `GET /api/libros/?autor=1` → Lista libros de un autor.  
- `GET /api/prestamos/?miembro=2` → Lista préstamos de un miembro.  
- `GET /api/prestamos/?fecha_devolucion__isnull=true` → Lista préstamos activos.  

---

 **Nota:** Este documento se puede ampliar con instrucciones de instalación y pruebas (Postman, Swagger, etc.), según se requiera.
