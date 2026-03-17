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
ProyectoAPS/
├── manage.py
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── .env
├── db.sqlite3
├── ProyectoAPS/          # Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── venv/                # Entorno virtual (no incluir en git)
```