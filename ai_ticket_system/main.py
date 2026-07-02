from users import Users
from ticket import Ticket
from ticket_manager import TicketManager

# Priority scale: 1 (lowest) to 5 (highest)
PRIORITIES = {
    1: ("Low", "Minor issue, no urgency. Workaround exists; can wait."),
    2: ("Normal", "Standard request. Should be handled in normal queue."),
    3: ("Medium", "Affects work but system still usable. Fix within a few days."),
    4: ("High", "Major impact on user or business. Needs attention soon."),
    5: ("Critical", "System down or security/data risk. Fix immediately."),
}

# Status lifecycle: 1 to 5
STATUSES = {
    1: ("Open", "New ticket, not yet reviewed or assigned."),
    2: ("In Progress", "Team is actively working on it."),
    3: ("Pending", "Waiting on user info, approval, or another team."),
    4: ("Resolved", "Fix applied; waiting for user confirmation."),
    5: ("Closed", "Issue confirmed fixed; ticket is complete."),
}

user1 = Users(1, "Jay", "jay@gmail.com", "Customer", "Engineering")
user2 = Users(2, "John", "john@gmail.com", "Customer", "Sales")
user3 = Users(3, "Jane", "jane@gmail.com", "Customer", "Marketing")
user4 = Users(4, "Jim", "jim@gmail.com", "Customer", "Support")
user5 = Users(5, "Jill", "jill@gmail.com", "Customer", "Finance")

ticket1 = Ticket(1, user1.user_name, "Cannot log in to account", "Technical", PRIORITIES[5][0])
ticket2 = Ticket(2, user2.user_name, "Payment failed but money was deducted", "Payment", PRIORITIES[4][0])
ticket3 = Ticket(3, user3.user_name, "Want to update email address", "Account", PRIORITIES[2][0])
ticket4 = Ticket(4, user4.user_name, "App is slow on mobile", "Technical", PRIORITIES[3][0])
ticket5 = Ticket(5, user5.user_name, "Question about billing cycle", "Payment", PRIORITIES[1][0])

ticket1.update_status(STATUSES[2][0])  # In Progress
ticket2.update_status(STATUSES[1][0])  # Open
ticket3.update_status(STATUSES[3][0])  # Pending
ticket4.update_status(STATUSES[2][0])  # In Progress
ticket5.update_status(STATUSES[4][0])  # Resolved

for ticket in [ticket1, ticket2, ticket3, ticket4, ticket5]:
    ticket.assign_team()

manager = TicketManager()
for ticket in [ticket1, ticket2, ticket3, ticket4, ticket5]:
    manager.add_ticket(ticket)

print("=== All Tickets ===")
manager.show_all_tickets()
