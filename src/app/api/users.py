from fastapi import APIRouter, Depends
from app.api.deps import get_current_user, require_role
from app.schemas.role import Role
from app.schemas.user import UserInDB

router = APIRouter()

@router.get("/me", response_model=UserInDB)
async def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return current_user

@router.get("/admin-only")
async def admin_route(user: UserInDB = Depends(require_role(Role.ADMIN))):
    return {"message": "Admin access granted"}