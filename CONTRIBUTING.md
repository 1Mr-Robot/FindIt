# Guia de Contribución

## Requisitos Previos

- Python 3.11 o superior
- Git

## Clonar el Repositorio

```bash
git clone https://github.com/DarkGhost74/ProyectoAPS.git
cd ProyectoAPS
```

## Crear el Entorno Virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python -m venv venv
source venv/bin/activate
```

## Instalar las Dependencias

```bash
pip install -r requirements.txt
```

Para instalar dependencias de desarrollo:

```bash
pip install -r requirements-dev.txt
```

## Configurar el Archivo .env

Copia el archivo `.env.example` y renómbralo a `.env`:

### Windows

```bash
copy .env.example .env
```

### Linux/Mac

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus configuraciones. Un ejemplo:

```env
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Generar una SECRET_KEY

Puedes generar una nueva clave secreta ejecutando:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Ejecutar las Migraciones

```bash
python manage.py migrate
```

## Crear un Superusuario

```bash
python manage.py createsuperuser
```

## Correr el Servidor Local

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`

## Comandos Utiles

### Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### Recolectar archivos estáticos
```bash
python manage.py collectstatic
```

### Crear app
```bash
python manage.py startapp <nombre_app>
```

## Estructura del Proyecto

```
FindIt/
├── manage.py                 # Script de administración Django
├── requirements.txt          # Dependencias de producción
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
│   ├── models.py            # Modelos: Item, Claim, CampusZone
│   ├── views.py             # Vistas: home, reportar objetos
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
│   ├── models.py            # Modelo User personalizado
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
├── venv/                    # Entorno virtual Python (no incluir en git)
└── .vscode/                 # Configuración de VS Code
```