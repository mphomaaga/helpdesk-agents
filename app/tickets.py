from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/tickets", tags=["tickets"])


class TicketCreate(BaseModel):
    title: str


class Ticket(BaseModel):
    id: int
    title: str
    status: str = "open"


_tickets: dict[int, Ticket] = {}
_next_id = 1


@router.post("", response_model=Ticket, status_code=201)
def create_ticket(body: TicketCreate) -> Ticket:
    global _next_id
    ticket = Ticket(id=_next_id, title=body.title)
    _tickets[ticket.id] = ticket
    _next_id += 1
    return ticket


@router.get("", response_model=list[Ticket])
def list_tickets() -> list[Ticket]:
    return list(_tickets.values())


@router.get("/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int) -> Ticket:
    ticket = _tickets.get(ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.patch("/{ticket_id}", response_model=Ticket)
def close_ticket(ticket_id: int) -> Ticket:
    ticket = _tickets.get(ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    ticket.status = "closed"
    return ticket
