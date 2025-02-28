from pydantic import BaseModel
from typing import Optional

class MechanicBase(BaseModel):

    id: int
    name: str
    specialty: str
    phone: str
    available: bool

    class Config:
        from_attributes = True

class MechanicCreate(BaseModel):
    
    name: str
    specialty: str
    phone: str
    available: bool

class MechanicUpdate(BaseModel):

    name: Optional[str] = None
    specialty: Optional[str] = None
    phone: Optional[str] = None
    available: Optional[bool] = None


if __name__ == "__main__":
    # Dados para criação de um Mechanic
    mechanic_data = {
        "name": "João Silva",
        "specialty": "Motor",
        "phone": "(11) 99999-9999",
        "available": True
    }

    # Criando um objeto MechanicCreate
    mechanic_create = MechanicCreate(**mechanic_data)
    print("MechanicCreate:", mechanic_create)

    # Dados para atualização de um Mechanic
    update_data = {
        "specialty": "Suspensão",
        "available": False
    }

    # Criando um objeto MechanicUpdate
    mechanic_update = MechanicUpdate(**update_data)
    print("MechanicUpdate:", mechanic_update)