from pydantic import BaseModel, EmailStr
from app.schemas.role import Role


class UserBase(BaseModel):
    email: EmailStr
    role: Role


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
    role: Role | None = None


class UserInDB(UserBase):
    id: int
    is_active: bool
    role: Role

    class Config:
        orm_mode = True


