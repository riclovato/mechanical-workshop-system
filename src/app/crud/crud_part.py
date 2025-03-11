from sqlalchemy.orm import Session
from app.models.part import Part
from app.crud.crud_base import CRUDBase
from app.schemas.part import PartCreate, PartUpdate
from typing import Optional, List

class CRUDPart(CRUDBase[Part, PartCreate, PartUpdate]):
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