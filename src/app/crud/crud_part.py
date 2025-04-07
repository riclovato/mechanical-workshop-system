from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import Part, ServiceItem
from app.crud.crud_base import CRUDBase
from app.schemas.part import PartCreate, PartUpdate
from typing import Optional, List
from fastapi import HTTPException, status

class CRUDPart(CRUDBase[Part, PartCreate, PartUpdate]):
    
    def __init__(self):  
        super().__init__(model=Part) 
    
    def update_stock(self, db: Session, part_id: int, delta : int) -> Optional[Part]:
        """
        Atualiza o estoque de uma peça
        Args: 
        db: Sessão do banco de dados
        part_id: ID da peça
        delta: Valor a ser adicionado ou subtraído

        Returns:
            Part atualizada ou None se não encontrar
        """

        part = self.get(db, part_id)

        if part:
            part.stock_quantity += delta
            db.commit()
            db.refresh(part) #Atualiza o banco de dados do obj

        return part
    
    def remove(self, db:Session, id: int) -> None:
        "Sobrescreve o método remove para verificar ordens de serviço vinculadas"
        part = self.get(db,id)
        if not part:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail = "Peça não encontrada"
            )
        if db.query(ServiceItem).filter(ServiceItem.part_id == id).first():
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail="Não é possível deletar: peça vinculada a ordem de serviço"
            )
        
        try: 
            db.delete(part)
            db.commit()
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Erro ao deletar peça: {str(e)}"
            ) 