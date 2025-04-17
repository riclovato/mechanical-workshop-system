from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.core.security import create_access_token, verify_password_hash
from app.crud.crud_user import crud_user
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserInDB


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=Token, status_code=status.HTTP_200_OK)
async def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = crud_user.get_by_email(db, form_data.username)
    if not user or not verify_password_hash(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserInDB, status_code=status.HTTP_201_CREATED)
async def register(
    user_in: UserCreate,
    db: Session = Depends(get_db),
):
    if crud_user.get_by_email(db, user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered")
    return crud_user.create(db=db, obj_in=user_in)