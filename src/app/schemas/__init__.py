from .base import BaseSchema

# Import simple models first
from .customer import CustomerSimple
from .vehicle import VehicleSimple
from .service_order import ServiceOrderSimple
from .mechanic import MechanicSimple
from .part import PartSimple
from .service_item import ServiceItemSimple

# Then import full models
from .customer import CustomerBase, CustomerCreate, CustomerUpdate, CustomerResponse
from .vehicle import VehicleBase, VehicleCreate, VehicleUpdate, VehicleResponse
from .service_order import ServiceOrderBase, ServiceOrderCreate, ServiceOrderUpdate, ServiceOrderResponse
from .mechanic import MechanicBase, MechanicCreate, MechanicUpdate, MechanicResponse
from .part import PartBase, PartCreate, PartUpdate, PartResponse
from .service_item import ServiceItemBase, ServiceItemCreate, ServiceItemUpdate, ServiceItemResponse

# Rebuild the models with circular references in the correct order
ServiceItemSimple.model_rebuild()
PartSimple.model_rebuild()
MechanicSimple.model_rebuild()
CustomerSimple.model_rebuild()
VehicleSimple.model_rebuild()
ServiceOrderSimple.model_rebuild()

# Then rebuild the full models
PartResponse.model_rebuild()
ServiceItemResponse.model_rebuild()
MechanicResponse.model_rebuild()
CustomerResponse.model_rebuild()
VehicleResponse.model_rebuild()
ServiceOrderResponse.model_rebuild()