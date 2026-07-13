from ticket import TechnicalTicket, PaymentTicket, AccountTicket
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


if __name__ == "__main__":
    override_ok = test_assign_team_override()
    methods_ok = test_inherited_methods()
    private_ok = test_inherited_private_data()

    print("=== Summary ===")
    print(f"Override         : {override_ok}")
    print(f"Inherited methods: {methods_ok}")
    print(f"Private data     : {private_ok}")
