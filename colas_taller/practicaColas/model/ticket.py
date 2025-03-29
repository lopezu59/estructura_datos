from pydantic import BaseModel

class Ticket(BaseModel):
    name: str # name of the person
    type: str # type of consultation
    identity: int # identity card
    case_description: str # description of the case
    age: int # age of the person
    priority_attention: bool = None  # Will be calculated automatically


#lee todos los datos como si fuera un diccionario
def __init__(self, **data):
        # si priority_attention is not provided, es asignado en base su edad 
    if "priority_attention" not in data or data["priority_attention"] is None:
        data["priority_attention"] = data["age"] >= 60
    super().__init__(**data) #Pydantic valida y guarda correctamente todos los valores

