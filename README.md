# fastapi-project

## Descripción
Proyecto de API desarrollada con FastAPI.

## Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener lo siguiente instalado:
- **Python 3.7+**
- **pip** (gestor de paquetes de Python)


## Instalación

### 1. Crear un entorno virtual

En el directorio del proyecto, ejecuta:

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual

**En Windows:**
```bash
.venv\Scripts\Activate.ps1
```

**En macOS o Linux:**
```bash
source .venv/bin/activate
```

### 3. Instalar las dependencias

Una vez activado el entorno virtual, instala FastAPI y Uvicorn (servidor ASGI):

```bash
pip install "fastapi[standard]"
```

## Ejecución de la Aplicación

### Iniciar el servidor de desarrollo

Para ejecutar la aplicación, usa el siguiente comando:

```bash
fastapi dev main.py
```

### Acceder a la API

Una vez que el servidor esté corriendo, la API estará disponible en:

- **URL base:** `http://localhost:8000`
- **Documentación interactiva (Swagger UI):** `http://localhost:8000/docs`
- **Documentación alternativa (ReDoc):** `http://localhost:8000/redoc`

## Endpoints Disponibles

### 1. GET `/`

Accede al root de la API.

**Respuesta:**
```json
{
  "mensaje": "Haz accedido al root de la API, bienvenido!",
  "razon de ser": "Es una buena practica definir un root en una API y que este devuelva algo útil",
  "estado": "Si puedes ver toda esta información, es porque la API está corriendo correctamente",
  "hotel?": "trivago"
}
```

### 2. GET `/saludo/{nombre}`

Saluda al usuario con un nombre específico.

**Parámetro:**
- `nombre` (string): El nombre de la persona a saludar

**Ejemplo:** `GET /saludo/Ana`

**Respuesta:**
```json
{
  "mensaje": "Hola, Ana. ¡Bienvenido a nuestra API!"
}
```

## Detener la Aplicación

Para detener el servidor, presiona `Ctrl + C` en la terminal donde se está ejecutando.