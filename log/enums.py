from enum import Enum

class AdminPermissionEnum(Enum):
    AD = "Admin"
    CA = "Confirm all company"
    CS = "Confirm specific company"
    
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
