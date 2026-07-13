from ticket import TechnicalTicket, PaymentTicket, AccountTicket
from ticket_manager import TicketManager
from constants import PRIORITIES, STATUSES


def test_assign_team_override():
    technical = TechnicalTicket(
        1, "Jay", "Cannot log in to account", "Technical", PRIORITIES[5][0]
    )
    payment = PaymentTicket(
        2, "John", "Payment failed but money was deducted", "Payment", PRIORITIES[4][0]
    )
    account = AccountTicket(
        3, "Jane", "Want to update email address", "Account", PRIORITIES[2][0]
    )

    technical.assign_team()
    payment.assign_team()
    account.assign_team()

    print("=== Verify Method Overriding ===")
    print("Parent Ticket.assign_team() would set Technical -> 'IT Team'")
    print("Child TechnicalTicket.assign_team() should set -> 'Technical Team'")
    print()

    checks = [
        (technical, "TechnicalTicket", "Technical Team"),
        (payment, "PaymentTicket", "Finance Team"),
        (account, "AccountTicket", "Support Team"),
    ]

    all_passed = True
    for ticket, expected_class, expected_team in checks:
        method_owner = type(ticket).assign_team.__qualname__
        class_name = type(ticket).__name__
        passed = (
            class_name == expected_class
            and ticket.assigned_team == expected_team
            and method_owner.startswith(expected_class)
        )
        all_passed = all_passed and passed

        print(f"Object class     : {class_name}")
        print(f"Method used      : {method_owner}")
        print(f"Assigned team    : {ticket.assigned_team}")
        print(f"Override works   : {passed}")
        print("-" * 40)

    print("=== Child Class Team Assignment ===")
    print(f"TechnicalTicket -> {technical.assigned_team}")
    print(f"PaymentTicket   -> {payment.assigned_team}")
    print(f"AccountTicket   -> {account.assigned_team}")
    print("-" * 40)

    if all_passed:
        print("All override checks passed.")
    else:
        print("Some override checks failed.")

    return all_passed


def test_inherited_methods():
    print("=== Test Inherited Methods ===")

    child = TechnicalTicket(
        10, "Jay", "App crashes on launch", "Technical", PRIORITIES[4][0]
    )

    child.update_status(STATUSES[2][0])
    child.update_priority(PRIORITIES[5][0])

    status_ok = child.get_status() == STATUSES[2][0]
    priority_ok = child.get_priority() == PRIORITIES[5][0]
    passed = status_ok and priority_ok

    print(f"Called update_status()   -> {child.get_status()} (expected In Progress)")
    print(f"Called update_priority() -> {child.get_priority()} (expected Critical)")
    print("Called get_ticket_summary() on child:")
    child.get_ticket_summary()
    print(f"Inherited methods work   : {passed}")
    print("-" * 40)

    return passed


def test_inherited_private_data():
    print("=== Test Inherited Private Data ===")

    child = PaymentTicket(
        11, "John", "Refund not received", "Payment", PRIORITIES[3][0]
    )

    status = child.get_status()
    priority = child.get_priority()

    # Access only through getters — never child.__status or child.__priority
    status_ok = status == STATUSES[1][0]
    priority_ok = priority == PRIORITIES[3][0]
    passed = status_ok and priority_ok

    print(f"get_status()   -> {status} (expected Open)")
    print(f"get_priority() -> {priority} (expected Medium)")
    print("Accessed private data via getters only (not __status / __priority)")
    print(f"Private data access works : {passed}")
    print("-" * 40)

    return passed


def test_child_objects_in_manager():
    print("=== Add Child Objects to TicketManager ===")

    manager = TicketManager()

    technical = TechnicalTicket(
        1, "Jay", "Cannot log in to account", "Technical", PRIORITIES[5][0]
    )
    payment = PaymentTicket(
        2, "John", "Payment failed but money was deducted", "Payment", PRIORITIES[4][0]
    )
    account = AccountTicket(
        3, "Jane", "Want to update email address", "Account", PRIORITIES[2][0]
    )

    for ticket in [technical, payment, account]:
        ticket.assign_team()
        manager.add_ticket(ticket)

    stored = manager.get_all_tickets()
    class_names = [type(ticket).__name__ for ticket in stored]

    count_ok = len(stored) == 3
    types_ok = class_names == ["TechnicalTicket", "PaymentTicket", "AccountTicket"]
    same_list = stored is manager.tickets
    passed = count_ok and types_ok and same_list

    print(f"Tickets in manager list : {len(stored)}")
    print(f"Classes stored          : {class_names}")
    print("All subclasses share one tickets list in TicketManager")
    print(f"Mixed subclasses stored : {passed}")
    print("-" * 40)

    print("Managers can still show mixed tickets:")
    manager.show_all_tickets()

    return passed


def test_polymorphism():
    print("=== Test Polymorphism ===")

    tickets = [
        TechnicalTicket(1, "Jay", "Cannot log in", "Technical", PRIORITIES[5][0]),
        PaymentTicket(2, "John", "Payment failed", "Payment", PRIORITIES[4][0]),
        AccountTicket(3, "Jane", "Update email", "Account", PRIORITIES[2][0]),
    ]

    expected = {
        "TechnicalTicket": "Technical Team",
        "PaymentTicket": "Finance Team",
        "AccountTicket": "Support Team",
    }

    print("Same call in a loop: ticket.assign_team()")
    print("Different child implementations run automatically:")
    print()

    all_passed = True
    for ticket in tickets:
        ticket.assign_team()

        class_name = type(ticket).__name__
        method_used = type(ticket).assign_team.__qualname__
        team = ticket.assigned_team
        passed = team == expected[class_name] and method_used.startswith(class_name)
        all_passed = all_passed and passed

        print(f"Class        : {class_name}")
        print(f"Method used  : {method_used}")
        print(f"Assigned team: {team}")
        print(f"Correct      : {passed}")
        print("-" * 40)

    print(f"Polymorphism works : {all_passed}")
    print("-" * 40)

    return all_passed


if __name__ == "__main__":
    override_ok = test_assign_team_override()
    methods_ok = test_inherited_methods()
    private_ok = test_inherited_private_data()
    manager_ok = test_child_objects_in_manager()
    poly_ok = test_polymorphism()

    print("=== Summary ===")
    print(f"Override         : {override_ok}")
    print(f"Inherited methods: {methods_ok}")
    print(f"Private data     : {private_ok}")
    print(f"Manager storage  : {manager_ok}")
    print(f"Polymorphism     : {poly_ok}")
