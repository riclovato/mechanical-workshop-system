
from .base import BaseSchema

from .customer import CustomerSimple
from .vehicle import VehicleSimple
from .service_order import ServiceOrderSimple
from .mechanic import MechanicSimple


from .customer import CustomerBase, CustomerCreate, CustomerUpdate, CustomerResponse
from .vehicle import VehicleBase, VehicleCreate, VehicleUpdate, VehicleResponse
from .service_order import ServiceOrderBase, ServiceOrderCreate, ServiceOrderUpdate, ServiceOrderResponse
from .mechanic import MechanicBase, MechanicCreate, MechanicUpdate, MechanicResponse

# rebuild the models with circular references
CustomerResponse.model_rebuild()
VehicleResponse.model_rebuild()
ServiceOrderResponse.model_rebuild()


if hasattr(MechanicResponse, 'model_rebuild'):
    MechanicResponse.model_rebuild()