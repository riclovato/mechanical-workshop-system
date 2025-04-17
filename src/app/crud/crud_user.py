from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash
from app.crud.crud_base import CRUDBase


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def __init__(self):
        super().__init__(model=User)

    def get_by_email(self, db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, obj_in: UserCreate) -> User:

        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            role=obj_in.role.value, 
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

crud_user = CRUDUser()