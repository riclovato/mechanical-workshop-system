import pytest
from sqlalchemy.orm import Session
from app.models.mechanic import Mechanic
from app.crud.crud_mechanic import CRUDMechanic
from app.schemas.mechanic import MechanicCreate, MechanicUpdate