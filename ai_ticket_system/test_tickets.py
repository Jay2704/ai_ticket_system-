from ticket import TechnicalTicket, PaymentTicket, AccountTicket
from constants import PRIORITIES


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


if __name__ == "__main__":
    test_assign_team_override()
