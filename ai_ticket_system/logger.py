def log_ticket(ticket):
    print(f"Ticket {ticket.id} created by {ticket.user_name} with priority {ticket.priority} and status {ticket.status}")

def log_user(user):
    print(f"User {user.id} created with name {user.name} and email {user.email}")

def log_ticket_assigned(ticket):
    print(f"Ticket {ticket.id} assigned to {ticket.assigned_to}")

def log_ticket_resolved(ticket):
    print(f"Ticket {ticket.id} resolved by {ticket.resolved_by}")

def log_ticket_closed(ticket):
    print(f"Ticket {ticket.id} closed by {ticket.closed_by}")