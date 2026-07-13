from ticket import Ticket, TechnicalTicket, PaymentTicket, AccountTicket
from ticket_manager import TicketManager
from constants import PRIORITIES, STATUSES


def test_assign_team_override():
    technical = TechnicalTicket(
        1, "Jay", "Cannot log in to account", PRIORITIES[5][0],
        "AuthService", "ERR_AUTH_401"
    )
    payment = PaymentTicket(
        2, "John", "Payment failed but money was deducted", PRIORITIES[4][0],
        "TXN-10021", 49.99
    )
    account = AccountTicket(
        3, "Jane", "Want to update email address", PRIORITIES[2][0],
        "Personal", "Change email"
    )

    technical.assign_team()
    payment.assign_team()
    account.assign_team()

    print("=== Verify Method Overriding ===")
    print("Ticket.assign_team() is abstract — each child must implement it")
    print("TechnicalTicket.assign_team() should set -> 'Technical Team'")
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
        10, "Jay", "App crashes on launch", PRIORITIES[4][0],
        "MobileApp", "ERR_CRASH_500"
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
        11, "John", "Refund not received", PRIORITIES[3][0],
        "TXN-20011", 25.00
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
        1, "Jay", "Cannot log in to account", PRIORITIES[5][0],
        "AuthService", "ERR_AUTH_401"
    )
    payment = PaymentTicket(
        2, "John", "Payment failed but money was deducted", PRIORITIES[4][0],
        "TXN-10021", 49.99
    )
    account = AccountTicket(
        3, "Jane", "Want to update email address", PRIORITIES[2][0],
        "Personal", "Change email"
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
        TechnicalTicket(1, "Jay", "Cannot log in", PRIORITIES[5][0], "AuthService", "ERR_AUTH_401"),
        PaymentTicket(2, "John", "Payment failed", PRIORITIES[4][0], "TXN-10021", 49.99),
        AccountTicket(3, "Jane", "Update email", PRIORITIES[2][0], "Personal", "Change email"),
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


def test_child_specific_attributes():
    print("=== Test Child-Specific Attributes (super) ===")

    technical = TechnicalTicket(
        1, "Jay", "Cannot log in", PRIORITIES[5][0], "AuthService", "ERR_AUTH_401"
    )
    payment = PaymentTicket(
        2, "John", "Payment failed", PRIORITIES[4][0], "TXN-10021", 49.99
    )
    account = AccountTicket(
        3, "Jane", "Update email", PRIORITIES[2][0], "Personal", "Change email"
    )

    parent_ok = (
        technical.issue_category == "Technical"
        and payment.issue_category == "Payment"
        and account.issue_category == "Account"
    )
    child_ok = (
        technical.system_name == "AuthService"
        and technical.error_code == "ERR_AUTH_401"
        and payment.transaction_id == "TXN-10021"
        and payment.payment_amount == 49.99
        and account.account_type == "Personal"
        and account.requested_change == "Change email"
    )
    passed = parent_ok and child_ok

    print(f"Technical -> system_name={technical.system_name}, error_code={technical.error_code}")
    print(f"Payment   -> transaction_id={payment.transaction_id}, amount={payment.payment_amount}")
    print(f"Account   -> account_type={account.account_type}, requested={account.requested_change}")
    print("Parent attrs set via super(); child attrs set in child __init__")
    print(f"Child attributes work : {passed}")
    print("-" * 40)

    return passed


def test_summary_override_with_super():
    print("=== Test get_ticket_summary() Override with super() ===")

    technical = TechnicalTicket(
        1, "Jay", "Cannot log in", PRIORITIES[5][0], "AuthService", "ERR_AUTH_401"
    )
    technical.assign_team()

    method_owner = type(technical).get_ticket_summary.__qualname__
    passed = method_owner.startswith("TechnicalTicket")

    print("Child get_ticket_summary() calls super().get_ticket_summary()")
    print("then adds child-specific fields:")
    technical.get_ticket_summary()
    print(f"Method used            : {method_owner}")
    print(f"Summary override works : {passed}")
    print("-" * 40)

    return passed


def test_isinstance():
    print("=== Learn isinstance() ===")

    technical = TechnicalTicket(
        1, "Jay", "Cannot log in", PRIORITIES[5][0], "AuthService", "ERR_AUTH_401"
    )
    payment = PaymentTicket(
        2, "John", "Payment failed", PRIORITIES[4][0], "TXN-10021", 49.99
    )
    account = AccountTicket(
        3, "Jane", "Update email", PRIORITIES[2][0], "Personal", "Change email"
    )

    checks = [
        (isinstance(technical, Ticket), True, "technical is a Ticket"),
        (isinstance(technical, TechnicalTicket), True, "technical is a TechnicalTicket"),
        (isinstance(technical, PaymentTicket), False, "technical is NOT a PaymentTicket"),
        (isinstance(payment, Ticket), True, "payment is a Ticket"),
        (isinstance(payment, PaymentTicket), True, "payment is a PaymentTicket"),
        (isinstance(account, Ticket), True, "account is a Ticket"),
        (isinstance(account, AccountTicket), True, "account is an AccountTicket"),
        (isinstance(account, TechnicalTicket), False, "account is NOT a TechnicalTicket"),
    ]

    all_passed = True
    for result, expected, label in checks:
        passed = result == expected
        all_passed = all_passed and passed
        print(f"{label}: {result} (expected {expected}) -> {passed}")

    print(f"isinstance checks work : {all_passed}")
    print("-" * 40)

    return all_passed


def test_mro():
    print("=== Learn MRO (Method Resolution Order) ===")

    technical_mro = [cls.__name__ for cls in TechnicalTicket.__mro__]
    payment_mro = [cls.__name__ for cls in PaymentTicket.__mro__]
    account_mro = [cls.__name__ for cls in AccountTicket.__mro__]

    print(f"TechnicalTicket MRO: {technical_mro}")
    print(f"PaymentTicket MRO  : {payment_mro}")
    print(f"AccountTicket MRO  : {account_mro}")

    expected_tail = ["Ticket", "ABC", "object"]
    passed = (
        technical_mro == ["TechnicalTicket", *expected_tail]
        and payment_mro == ["PaymentTicket", *expected_tail]
        and account_mro == ["AccountTicket", *expected_tail]
    )

    print("Python looks up methods in this order (child -> parent -> ABC -> object)")
    print(f"MRO checks work : {passed}")
    print("-" * 40)

    return passed


def test_abstract_assign_team():
    print("=== Abstract Base Class: require assign_team() ===")

    # Child classes that implement assign_team can be created
    technical = TechnicalTicket(
        1, "Jay", "Cannot log in", PRIORITIES[5][0], "AuthService", "ERR_AUTH_401"
    )
    technical.assign_team()
    children_ok = technical.assigned_team == "Technical Team"

    # Ticket itself is abstract — cannot be instantiated directly
    cannot_create_base = False
    try:
        Ticket(1, "Jay", "Generic issue", "Technical", PRIORITIES[2][0])
    except TypeError as e:
        cannot_create_base = True
        print(f"Cannot create Ticket() directly: {e}")

    # A subclass that forgets assign_team() also cannot be created
    class BrokenTicket(Ticket):
        pass

    cannot_create_broken = False
    try:
        BrokenTicket(99, "Sam", "Broken", "Technical", PRIORITIES[2][0])
    except TypeError as e:
        cannot_create_broken = True
        print(f"Cannot create subclass without assign_team(): {e}")

    passed = children_ok and cannot_create_base and cannot_create_broken
    print(f"Abstract assign_team works : {passed}")
    print("-" * 40)

    return passed


if __name__ == "__main__":
    override_ok = test_assign_team_override()
    methods_ok = test_inherited_methods()
    private_ok = test_inherited_private_data()
    manager_ok = test_child_objects_in_manager()
    poly_ok = test_polymorphism()
    attrs_ok = test_child_specific_attributes()
    summary_ok = test_summary_override_with_super()
    isinstance_ok = test_isinstance()
    mro_ok = test_mro()
    abc_ok = test_abstract_assign_team()

    print("=== Summary ===")
    print(f"Override         : {override_ok}")
    print(f"Inherited methods: {methods_ok}")
    print(f"Private data     : {private_ok}")
    print(f"Manager storage  : {manager_ok}")
    print(f"Polymorphism     : {poly_ok}")
    print(f"Child attributes : {attrs_ok}")
    print(f"Summary override : {summary_ok}")
    print(f"isinstance       : {isinstance_ok}")
    print(f"MRO              : {mro_ok}")
    print(f"Abstract ABC     : {abc_ok}")
