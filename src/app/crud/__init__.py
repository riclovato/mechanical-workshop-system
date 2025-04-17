from .crud_customer import CRUDCustomer
from .crud_vehicle import CRUDVehicle
from .crud_mechanic import CRUDMechanic
from .crud_part import CRUDPart
from .crud_service_order import CRUDServiceOrder
from .crud_service_item import CRUDServiceItem

__all__ = [
    'crud_user',
    'CRUDCustomer',
    'CRUDVehicle',
    'CRUDMechanic',
    'CRUDPart',
    'CRUDServiceOrder',
    'CRUDServiceItem'
]