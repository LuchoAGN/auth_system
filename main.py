from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routers import user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)