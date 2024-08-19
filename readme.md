# 🚀 FastAPI Authentication & Authorization System

Este proyecto es una API de autenticación y autorización construida con **FastAPI** y **MySQL**, utilizando **JWT (JSON Web Tokens)** para la autenticación. Los usuarios pueden registrarse, iniciar sesión, y se les pueden asignar roles específicos como `user` y `admin`. Este proyecto también incluye manejo de `created_at` y `updated_at` para rastrear la creación y actualización de registros.

## 📑 Tabla de Contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Rutas Disponibles](#rutas-disponibles)
- [Contribución](#contribución)
- [Licencia](#licencia)

## 🎯 Características

- **Autenticación JWT:** Maneja la autenticación utilizando tokens JWT.
- **Registro de Usuarios:** Permite a los usuarios registrarse con un nombre de usuario y contraseña.
- **Roles de Usuario:** Asignación de roles `user` y `admin` utilizando un `Enum`.
- **Timestamps Automáticos:** Campos `created_at` y `updated_at` manejados automáticamente por SQLAlchemy.
- **Configuración Centralizada:** Uso de archivos `.env` y configuración centralizada en `config.py`.

## 🛠 Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/) - Un framework web moderno y rápido.
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM usado para interactuar con la base de datos.
- [MySQL](https://www.mysql.com/) - Sistema de gestión de bases de datos relacional.
- [JWT (JSON Web Tokens)](https://jwt.io/) - Sistema de autenticación basado en tokens.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validación de datos y modelos.

## 📁 Estructura del Proyecto

    auth_system
    ├── app/
    │ ├── init.py
    │ ├── models.py
    │ ├── schemas.py
    │ ├── controllers/
    │ │ ├── init.py
    │ │ ├── user_controller.py
    │ ├── routers/
    │ │ ├── init.py
    │ │ ├── user_router.py
    │ ├── auth/
    │ │ ├── init.py
    │ │ ├── auth_handler.py
    │ │ ├── auth_bearer.py
    │ ├── database.py
    │ ├── config.py
    ├── .env
    ├── main.py
    ├── README.md
    └── requirements.txt

## 📦 Instalación

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/LuchoAGN/auth_system
   cd auth_system
   ```

2. **Crear un Entorno Virtual:**

   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Crear un Entorno Virtual:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la Base de Datos:**
   Asegúrate de tener MySQL instalado y funcionando. Crea una base de datos para la aplicación.

   ```bash
   CREATE DATABASE fastapi_auth_db;
   ```

5. **Configurar Variables de Entorno**

   Crea un archivo '.env' en la raíz del proyecto con el siguiente contenido:

   ```bash
   DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost/todo_db
   SECRET_KEY=tu_clave_secreta
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ALGORITHM=HS256
   ```

## ⚙️ Configuración

El proyecto utiliza un archivo .env para gestionar variables de entorno sensibles, como las credenciales de la base de datos y la clave secreta de JWT.

Ejemplo '.env':

    ```bash
    DATABASE_URL=mysql+pymysql://root:password@localhost:3306/fastapi_auth_db
    SECRET_KEY=tu_secreta_clave
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

'config.py': Este archivo centraliza la configuración, cargando las variables de entorno y haciéndolas disponibles en toda la aplicación.

## 🚀 Uso

Para iniciar el servidor FastAPI:

    ```bash
    fastapi dev
    ```

El servidor estará disponible en 'http://127.0.0.1:8000'.

## 🌐 Rutas Disponibles

- POST /users/: Crear un nuevo usuario.
- POST /token/: Obtener un token JWT para autenticación.
- GET /users/me/: Obtener detalles del usuario actual.

### Ejemplo de Solicitudes

- Registro de Usuario:

  ```bash
  curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{"username": "johndoe", "password": "secret"}'
  ```

- Login de Usuario:

  ```bash
  curl -X POST "http://127.0.0.1:8000/token/" -H "Content-Type: application/x-www-form-urlencoded" -d "username=johndoe&password=secret"
  ```

- Obtener Información del Usuario Actual:

  ```bash
  curl -X GET "http://127.0.0.1:8000/users/me/" -H "Authorization: Bearer <your_token>"
  ```

## 📝 Contribución

¡Las contribuciones son bienvenidas! Si tienes alguna mejora, abre un pull request o una issue para discutirla.
