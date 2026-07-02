from user import User
from ticket import Ticket
from ticket_manager import TicketManager


PRIORITIES = {
    1: ("Low", "Minor issue, no urgency."),
    2: ("Normal", "Standard request."),
    3: ("Medium", "Affects work but system still usable."),
    4: ("High", "Major impact. Needs attention soon."),
    5: ("Critical", "System down or security/data risk."),
}

STATUSES = {
    1: ("Open", "New ticket."),
    2: ("In Progress", "Team is working on it."),
    3: ("Pending", "Waiting for input."),
    4: ("Resolved", "Fix applied."),
    5: ("Closed", "Ticket complete."),
}


user1 = User(1, "Jay", "jay@gmail.com", "Customer", "Engineering")
user2 = User(2, "John", "john@gmail.com", "Customer", "Sales")
user3 = User(3, "Jane", "jane@gmail.com", "Customer", "Marketing")
user4 = User(4, "Jim", "jim@gmail.com", "Customer", "Support")
user5 = User(5, "Jill", "jill@gmail.com", "Customer", "Finance")


ticket1 = Ticket(1, user1.user_name, "Cannot log in to account", "Technical", PRIORITIES[5][0])
ticket2 = Ticket(2, user2.user_name, "Payment failed but money was deducted", "Payment", PRIORITIES[4][0])
ticket3 = Ticket(3, user3.user_name, "Want to update email address", "Account", PRIORITIES[2][0])
ticket4 = Ticket(4, user4.user_name, "App is slow on mobile", "Technical", PRIORITIES[3][0])
ticket5 = Ticket(5, user5.user_name, "Question about billing cycle", "Payment", PRIORITIES[1][0])


ticket1.update_status(STATUSES[2][0])
ticket2.update_status(STATUSES[1][0])
ticket3.update_status(STATUSES[3][0])
ticket4.update_status(STATUSES[2][0])
ticket5.update_status(STATUSES[4][0])


for ticket in [ticket1, ticket2, ticket3, ticket4, ticket5]:
    ticket.assign_team()


manager = TicketManager()

for ticket in [ticket1, ticket2, ticket3, ticket4, ticket5]:
    manager.add_ticket(ticket)


print("=== All Tickets ===")
manager.show_all_tickets()