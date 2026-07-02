class TicketManager:

    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_all_tickets(self):
        return self.tickets

    def remove_ticket(self, ticket):
        self.tickets.remove(ticket)

    def find_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def update_status(self, ticket_id, new_status):
        ticket = self.find_ticket(ticket_id)

        if ticket:
            ticket.update_status(new_status)

    def update_priority(self, ticket_id, new_priority):
        ticket = self.find_ticket(ticket_id)

        if ticket:
            ticket.update_priority(new_priority)

    def show_all_tickets(self):
        for ticket in self.tickets:
            ticket.get_ticket_summary()