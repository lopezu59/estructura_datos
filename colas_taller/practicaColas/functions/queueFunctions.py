
from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    opciones = { 
        "duda",
        "caja",
        "asesor",
        "otros"
    }

    if ticket.type not in opciones:
        return f"Error: Tipo de atención inválido ({ticket.type})"

    if ticket.type not in ticketTypes:
        ticketTypes[ticket.type] = TicketController()

    ticketTypes[ticket.type].enqueue(ticket)
    return f"Ticket de tipo '{ticket.type}' añadido a la cola"





