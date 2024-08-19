from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app.schemas import UserCreate, UserOut
from app.auth import auth_handler as auth
from app.controllers import user_controller

router = APIRouter()

@router.post("/token", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return user_controller.login_user(form_data, db)

@router.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(user, db)

@router.get("/users/me", response_model=UserOut)
def read_users_me(current_user: UserOut = Depends(auth.get_current_active_user)):
    return user_controller.get_current_user(current_user)

@router.get("/admin", response_model=UserOut)
def read_admin(current_user: UserOut = Depends(auth.get_current_admin_user)):
    return user_controller.get_current_admin_user(current_user)