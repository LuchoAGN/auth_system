from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routers import user_router

description = """
Este proyecto es una API de autenticación y autorización construida con FastAPI y MySQL, utilizando JWT (JSON Web Tokens) 
para la autenticación. Los usuarios pueden registrarse, iniciar sesión, y se les pueden asignar roles específicos como user 
y admin. Este proyecto también incluye manejo de created_at y updated_at para rastrear la creación 
y actualización de registros.
"""

app = FastAPI( title="Auth System",
    description=description,
    summary="Base Authentication & Authorization System",
    version="0.0.1",
    terms_of_service="https://github.com/LuchoAGN/auth_system?tab=MIT-1-ov-file",
    contact={
        "name": "Lucho AGN",
        "url": "https://luchoagn.dev/",
        "email": "contact@luchoagn.dev",
    },
    license_info={
        "name": "MIT license",
        "url": "https://opensource.org/license/mit",
    },)

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)