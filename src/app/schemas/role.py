from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    MECHANIC = "mechanic"
    CUSTOMER = "customer"