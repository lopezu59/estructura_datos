from typing import Union
from fastapi import FastAPI
from model.ticket import Ticket
from controller.ticketController import TicketController
from functions.queueFunctions import add_queue
from typing import List

app = FastAPI()

ticketTypes = {
    "duda": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}


# Endpoint para crear un turno
@app.post("/ticketCreateBatch")
def create_shifts_batch(turnos: List[Ticket]):
    aggregates = []
    declined = []

    for shift in turnos:
        if shift.type in ticketTypes:
            add_queue(shift, ticketTypes)
            aggregates.append(shift.model_dump())
        else:
            declined.append({"name": shift.name, "type": shift.type})

    return {
        "mensaje": f"Tickets procesados. Agregados: {len(aggregates)}, Rechazados: {len(declined)}",
        "tickets_agregados": aggregates if aggregates else "Ninguno",
        "rechazados": declined if declined else "Ninguno"
    }

# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def get_next_shift():
    highest_priority_ticket = None
    highest_priority_type = None

    for type, queue in ticketTypes.items():
        if not queue.is_empty():
            candidate_ticket = queue.peek()
            if highest_priority_ticket is None or candidate_ticket.priority_attention:
                highest_priority_ticket = candidate_ticket
                highest_priority_type = type

    if highest_priority_ticket is None:
        return {"mensaje": "No hay tickets en ninguna cola."}
    
    ticketTypes[highest_priority_type].dequeue()

    
    return {
        "mensaje": "El siguiente turno es",
        "datos_turno": {
            "name": highest_priority_ticket.name, 
            "identity": highest_priority_ticket.identity,  
            "age": highest_priority_ticket.age,  
            "priority_attention": highest_priority_ticket.priority_attention
        }
    }
    
# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def list_tail_shifts():

    queue = []

    for type, queue_controller in ticketTypes.items():
        current = queue_controller.head
        while current:
            queue.append({
                "name": current.data.name,
                "identity": current.data.identity,
                "age": current.data.age,
                "priority_attention": current.priority,
                "tipo": type 
            })
            current = current.next

    # Ordenamos la lista por prioridad (True primero)
    queue.sort(key=lambda x: x["priority_attention"], reverse=True)

    return {"mensaje": "Lista de todos los turnos en cola ordenados por prioridad", "datos_turnos": queue if queue else "No hay turnos en cola"}
# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
