class InvalidStatusError(Exception):
    def __init__(self, message="Invalid status"):
        self.message = message
        super().__init__(self.message)


class InvalidPriorityError(Exception):
    def __init__(self, message="Invalid priority"):
        self.message = message
        super().__init__(self.message)


class TicketNotFoundError(Exception):
    def __init__(self, message="Ticket not found"):
        self.message = message
        super().__init__(self.message)
