# FindIt Campus

**FindIt Campus** es una plataforma web diseñada para ayudar a los estudiantes de la Universidad Autónoma de Nuevo León (UANL) a reportar y encontrar objetos perdidos dentro del campus universitario.

## Descripción del Proyecto

El sistema permite a los usuarios:
- Reportar objetos encontrados mediante una formulario que incluye imagen, título, descripción y medio de contacto
- Buscar objetos perdidos que coincidan con sus pertenencias
- Contactar directamente con la persona que reportó el objeto encontrado
- Autenticarse únicamente con correos institucionales (@uanl.edu.mx) para garantizar que solo estudiantes de la UANL puedan acceder

## Características Principales

### Para usuarios que encuentran objetos:
- Subir imagen del objeto encontrado
- Proporcionar título descriptivo y detallada descripción
- Especificar categoría, color y zona del campus donde fue encontrado
- Incluir información de contacto para que el dueño pueda comunicarse
- Seleccionar automáticamente la fecha actual como fecha de pérdida

### Para usuarios que buscan objetos perdidos:
- Navegar por lista de objetos reportados recientemente
- Filtrar objetos por categoría, color y zona del campus
- Ver detalles completos de cada objeto incluyendo imagen
- Contactar al reportante mediante la información proporcionada

### Seguridad y Autenticación:
- Registro exclusivo para correos @uanl.edu.mx
- Sistema de autenticación robusto con Django
- Protección contra accesos no autorizados
- Perfil de usuario con información institucional

## Tecnologías Utilizadas

### Backend:
- **Django 5.2**: Framework web fullstack para desarrollo rápido y seguro
- **MySQL 8**: Sistema de gestión de bases de datos relacional
- **Python 3.11**: Lenguaje de programación principal

### Frontend:
- **HTML5/CSS3**: Estructura y presentación de interfaces
- **JavaScript**: Interactividad y dinámicas en el cliente
- **Bootstrap**: Framework CSS para diseño responsivo

### Infraestructura y DevOps:
- **Docker**: Contenerización de la aplicación para despliegue consistente
- **Docker Compose**: Orquestación de múltiples servicios (web, base de datos, nginx)
- **Nginx**: Servidor proxy inverso para servir archivos estáticos y balancear carga
- **Gunicorn**: Servidor WSGI para producción
- **Waitress**: Servidor alternativo para desarrollo en Windows

### Despliegue:
- **Dokploy**: Plataforma de despliegue utilizada en el servidor personal del equipo
- **Cloudflare Tunnels**: Exposición segura de la aplicación al público mediante el dominio personalizado
- **Dominio personalizado**: Acceso público en https://findit.uziel.app

## Estructura del Proyecto

```
FindIt/
├── manage.py                # Script de administración Django
├── requirements.txt         # Dependencias de producción
├── requirements-dev.txt     # Dependencias de desarrollo
├── .env.example             # Plantilla de variables de entorno
├── .env                     # Variables de entorno (no incluir en git)
├── .gitignore               # Archivos ignorados por Git
├── Dockerfile               # Imagen Docker para producción
├── docker-compose.yml       # Orquestación de servicios Docker
├── nginx.conf               # Configuración del servidor Nginx
├── entrypoint.sh            # Script de inicio para Docker
├── LICENSE                  # Licencia del proyecto
├── README.md                # Documentación principal
├── .dockerignore            # Archivos ignorados en Docker
├── FindIt/                  # Paquete de configuración del proyecto
│   ├── __init__.py
│   ├── settings.py          # Configuración principal de Django
│   ├── urls.py              # Rutas principales del proyecto
│   ├── wsgi.py              # Entry point para servidores WSGI
│   └── asgi.py              # Entry point para servidores ASGI
├── core/                    # App Django: gestión de objetos perdidos
│   ├── __init__.py
│   ├── models.py            # Modelos: Item, ItemCategory, ItemColor, CampusZone
│   ├── views.py             # Vistas: home, reportar objetos, buscar objetos
│   ├── forms.py             # Formularios: ReportItemForm
│   ├── admin.py             # Configuración del admin de Django
│   ├── urls.py              # Rutas de la app core
│   ├── apps.py              # Configuración de la app
│   ├── tests.py             # Pruebas unitarias
│   ├── migrations/          # Migraciones de base de datos
│   ├── static/core/         # CSS y JS estático
│   └── templates/core/      # Plantillas HTML
├── users/                   # App Django: gestión de usuarios
│   ├── __init__.py
│   ├── models.py            # Modelo User personalizado con validación institucional
│   ├── views.py             # Vistas: login, register, profile
│   ├── forms.py             # Formularios de autenticación
│   ├── admin.py             # Configuración del admin
│   ├── urls.py              # Rutas de la app users
│   ├── apps.py              # Configuración de la app
│   ├── tests.py             # Pruebas unitarias
│   ├── migrations/          # Migraciones de base de datos
│   ├── static/users/        # CSS, JS e imágenes estáticas
│   └── templates/users/     # Plantillas HTML
├── media/                   # Archivos subidos por usuarios (imágenes)
│   ├── items/               # Imágenes de objetos perdidos
│   └── avatars/             # Avatares de usuarios
└── .vscode/                 # Configuración de VS Code
```

## Modelos de Datos Principales

### Core App Models:
- **ItemCategory**: Categorías de objetos (libro, teléfono, cartera, etc.)
- **ItemColor**: Colores de objetos para facilitar búsqueda
- **CampusZone**: Zonas específicas del campus UANL (facultades, edificios, áreas comunes)
- **Item**: Modelo principal que representa un objeto perdido/encontrado con campos para:
  - Información básica (nombre, descripción)
  - Relaciones con categoría, color y zona
  - Imagen del objeto
  - Fecha de pérdida
  - Información de contacto
  - Estado (perdido/encontrado)
  - Usuario que reportó

### Users App Models:
- **UserPersonalizado**: Extensión del modelo User de Django que incluye:
  - Validación de correo institucional (@uanl.edu.mx)
  - Número de matrícula
  - Campos de perfil adicionales

## Flujo de Trabajo

### Reportar un Objeto Encontrado:
1. Usuario autenticado accede a la sección "Reportar Objeto"
2. Completa el formulario con:
   - Imagen del objeto (obligatorio)
   - Nombre descriptivo
   - Detallada descripción
   - Selección de categoría y color
   - Selección de zona del campus donde fue encontrado
   - Información de contacto (teléfono, correo, etc.)
3. Al enviar, se crea un registro en la base de datos con estado "Encontrado"
4. El objeto aparece en la lista pública para que otros usuarios lo puedan ver

### Buscar un Objeto Perdido:
1. Usuario accede a la página principal o sección "Buscar Objetos"
2. Opcionalmente aplica filtros por categoría, color y/o zona
3. Revisa la lista de objetos reportados recientemente
4. Al encontrar un objeto que coincidir con su pérdida:
   - Ve los detalles completos incluyendo imagen
   - Usa la información de contacto proporcionada para comunicarse con el reportante
   - Opcionalmente marca el objeto como reclamado (funcionalidad futura)

## Requisitos para Desarrollo Local

### Prerrequisitos:
- Python 3.11 o superior
- Git
- Sistema operativo compatible (Windows/Linux/Mac)

### Pasos de Instalación:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/1Mr-Robot/FindIt.git
   cd ProyectoAPS
   ```

2. **Crear entorno virtual:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   # Para desarrollo:
   pip install -r requirements-dev.txt
   ```

4. **Configurar variables de entorno:**
   ```bash
   # Windows
   copy .env.example .env
   
   # Linux/Mac
   cp .env.example .env
   ```
   Editar `.env` con configuraciones apropiadas

5. **Generar clave secreta (opcional pero recomendado):**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

6. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   ```

7. **Crear superusuario (para acceso admin):**
   ```bash
   python manage.py createsuperuser
   ```

8. **Iniciar servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   La aplicación estará disponible en http://127.0.0.1:8000/

## Despliegue con Docker

### Construir y ejecutar:
```bash
docker-compose up --build
```

Los servicios se ejecutarán en:
- Aplicación web: http://localhost:{PUERTO_DE_NGINX}
- Base de datos MySQL: Puerto 3306 (interno)
- Nginx: Puerto configurado en variable de entorno PORT

### Detener y eliminar contenedores:
```bash
docker-compose down
```

Para eliminar también los volúmenes (datos persistentes):
```bash
docker-compose down -v
```

## Seguridad y Privacidad

- **Autenticación institucional**: Solo se permiten registros con correos @uanl.edu.mx
- **Validación de correos**: Sistema que verifica el dominio institucional durante el registro
- **Protección de datos**: Las imágenes y información de contacto solo son accesibles mediante la interfaz web
- **Control de acceso**: Los usuarios deben autenticarse para reportar objetos, pero cualquiera puede ver los objetos reportados (sin información de contacto hasta que se autentique)
- **CSRF Protection**: Protección incorporada de Django contra ataques CSRF
- **Sanitización de entradas**: Validación y escape adecuado de todos los inputs de usuario

## Personalización

### Modificando la Zona Horaria:
El proyecto está configurado para usar la zona horaria de Monterrey (America/Monterrey). Para cambiarlo:
1. Modificar `TIME_ZONE` en `.env`
2. Actualizar `TIME_ZONE` en `FindIt/settings.py`

### Agregando Nuevas Categorías/Colores/Zonas:
Los administradores pueden agregar nuevas opciones mediante:
1. Accediendo al panel de administración de Django (/admin/)
2. Navegando a las secciones correspondientes (Categorías, Colores, Zonas del campus)
3. Agregando nuevos registros según sea necesario

## Contribución

Consulte el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para obtener directrices detalladas sobre cómo contribuir al proyecto, incluyendo:
- Estructura de ramas y flujo de trabajo Git
- Estándares de codificación
- Proceso de revisión de código
- Guías para escribir pruebas

## Licencia

Este proyecto está licenciado bajo los términos especificados en el archivo [LICENSE](LICENSE).

## Equipo de Desarrollo

FindIt Campus fue desarrollado por el Equipo 2 de la materia Administración de Proyectos de Software, Grupo 005, como proyecto final del curso.

## Contacto y Soporte

Para reportar problemas, sugerir características o obtener soporte técnico, por favor utilice el sistema de Issues del repositorio GitHub.

**Sitio de producción**: https://findit.uziel.app
**Repositorio**: https://github.com/1Mr-Robot/FindIt