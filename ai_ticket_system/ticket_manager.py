class TicketManager:
    def __init__(self) -> None:
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_all_tickets(self):
        return self.tickets

    