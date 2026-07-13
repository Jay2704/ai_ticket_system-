from constants import STATUSES
from exceptions import TicketNotFoundError


class TicketManager:

    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_all_tickets(self):
        return self.tickets

    def remove_ticket(self, ticket_id):
        ticket = self.find_ticket(ticket_id)

        if ticket:
            self.tickets.remove(ticket)
        else:
            raise TicketNotFoundError(f"Ticket not found: {ticket_id}")

    def find_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def update_status(self, ticket_id, new_status):
        ticket = self.find_ticket(ticket_id)

        if ticket:
            ticket.update_status(new_status)
        else:
            raise TicketNotFoundError(f"Ticket not found: {ticket_id}")

    def update_priority(self, ticket_id, new_priority):
        ticket = self.find_ticket(ticket_id)

        if ticket:
            ticket.update_priority(new_priority)
        else:
            raise TicketNotFoundError(f"Ticket not found: {ticket_id}")

    def show_all_tickets(self):
        for ticket in self.tickets:
            ticket.get_ticket_summary()

    def show_open_tickets(self):
        for ticket in self.tickets:
            if ticket.get_status() == STATUSES[1][0]:
                ticket.get_ticket_summary()

    def show_tickets_by_priority(self, priority):
        for ticket in self.tickets:
            if ticket.get_priority() == priority:
                ticket.get_ticket_summary()

    def show_tickets_by_team(self, team):
        for ticket in self.tickets:
            if ticket.assigned_team == team:
                ticket.get_ticket_summary()
