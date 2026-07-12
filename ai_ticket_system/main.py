from users import User
from ticket import TechnicalTicket, PaymentTicket, AccountTicket
from ticket_manager import TicketManager
from constants import PRIORITIES, STATUSES
from exceptions import InvalidStatusError, InvalidPriorityError, TicketNotFoundError


manager = TicketManager()

user1 = User(1, "Jay", "jay@gmail.com", "Customer", "Engineering")
user2 = User(2, "John", "john@gmail.com", "Customer", "Sales")
user3 = User(3, "Jane", "jane@gmail.com", "Customer", "Marketing")
user4 = User(4, "Jim", "jim@gmail.com", "Customer", "Support")
user5 = User(5, "Jill", "jill@gmail.com", "Customer", "Finance")


# Test each child class
ticket1 = TechnicalTicket(1, user1.user_name, "Cannot log in to account", "Technical", PRIORITIES[5][0])
ticket2 = PaymentTicket(2, user2.user_name, "Payment failed but money was deducted", "Payment", PRIORITIES[4][0])
ticket3 = AccountTicket(3, user3.user_name, "Want to update email address", "Account", PRIORITIES[2][0])
ticket4 = TechnicalTicket(4, user4.user_name, "App is slow on mobile", "Technical", PRIORITIES[3][0])
ticket5 = PaymentTicket(5, user5.user_name, "Question about billing cycle", "Payment", PRIORITIES[1][0])

ticket1.assign_team()
ticket2.assign_team()
ticket3.assign_team()
ticket4.assign_team()
ticket5.assign_team()

print("=== Verify Method Overriding ===")
print("Parent Ticket.assign_team() would set Technical -> 'IT Team'")
print("Child TechnicalTicket.assign_team() should set -> 'Technical Team'")
print()

checks = [
    (ticket1, "TechnicalTicket", "Technical Team"),
    (ticket2, "PaymentTicket", "Finance Team"),
    (ticket3, "AccountTicket", "Support Team"),
]

for ticket, expected_class, expected_team in checks:
    method_owner = type(ticket).assign_team.__qualname__
    class_name = type(ticket).__name__
    passed = (
        class_name == expected_class
        and ticket.assigned_team == expected_team
        and method_owner.startswith(expected_class)
    )
    print(f"Object class     : {class_name}")
    print(f"Method used      : {method_owner}")
    print(f"Assigned team    : {ticket.assigned_team}")
    print(f"Override works   : {passed}")
    print("-" * 40)

print("=== Child Class Team Assignment ===")
print(f"TechnicalTicket -> {ticket1.assigned_team}")
print(f"PaymentTicket   -> {ticket2.assigned_team}")
print(f"AccountTicket   -> {ticket3.assigned_team}")
print("-" * 40)

for ticket in [ticket1, ticket2, ticket3, ticket4, ticket5]:
    manager.add_ticket(ticket)
    ticket.assign_team()

manager.update_status(ticket1.ticket_id, STATUSES[2][0])
manager.update_status(ticket2.ticket_id, STATUSES[1][0])
manager.update_status(ticket3.ticket_id, STATUSES[3][0])
manager.update_status(ticket4.ticket_id, STATUSES[2][0])
manager.update_status(ticket5.ticket_id, STATUSES[4][0])


print("=== Exception Handling ===")

try:
    manager.update_status(99, STATUSES[5][0])
except TicketNotFoundError as e:
    print(e)

try:
    manager.update_status(ticket1.ticket_id, "Sleeping")
except InvalidStatusError as e:
    print(e)

try:
    manager.update_priority(ticket1.ticket_id, "Urgent")
except InvalidPriorityError as e:
    print(e)


print("=== All Tickets ===")
manager.show_all_tickets()

print("=== Open Tickets ===")
manager.show_open_tickets()

print("=== Critical Priority Tickets ===")
manager.show_tickets_by_priority(PRIORITIES[5][0])

print("=== Technical Team Tickets ===")
manager.show_tickets_by_team("Technical Team")