from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import timedelta
from app import crud, schemas, config
from app.auth import auth_handler

def create_user(user: schemas.UserCreate, db: Session):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

def login_user(form_data: schemas.UserCreate, db: Session):
    user = auth_handler.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.settings.access_token_expire_minutes)
    access_token = auth_handler.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(current_user: schemas.UserOut):
    return current_user

def get_current_admin_user(current_user: schemas.UserOut):
    return current_user