from constants import PRIORITIES, STATUSES
from exceptions import InvalidPriorityError, InvalidStatusError


class Ticket:

    def __init__(self, ticket_id, user_name, issue_description, issue_category, priority):
        self.ticket_id = ticket_id
        self.user_name = user_name
        self.issue_description = issue_description
        self.issue_category = issue_category
        self.assigned_team = "Unassigned"
        self.created_at = "Today"
        self.__status = "Open"
        self.__priority = PRIORITIES[2][0]

        if self._is_valid_priority(priority):
            self.__priority = priority
        else:
            raise InvalidPriorityError(f"Invalid priority: {priority}")

    def get_status(self):
        return self.__status

    def get_priority(self):
        return self.__priority

    def _is_valid_status(self, new_status):
        return any(status[0] == new_status for status in STATUSES.values())

    def _is_valid_priority(self, new_priority):
        return any(priority[0] == new_priority for priority in PRIORITIES.values())

    def update_status(self, new_status):
        if self._is_valid_status(new_status):
            self.__status = new_status
        else:
            raise InvalidStatusError(f"Invalid status: {new_status}")

    def update_priority(self, new_priority):
        if self._is_valid_priority(new_priority):
            self.__priority = new_priority
        else:
            raise InvalidPriorityError(f"Invalid priority: {new_priority}")

    def assign_team(self):
        if self.issue_category == "Technical":
            self.assigned_team = "IT Team"
        elif self.issue_category == "Payment":
            self.assigned_team = "Finance Team"
        elif self.issue_category == "Account":
            self.assigned_team = "Support Team"
        else:
            self.assigned_team = "General Support"

    def get_ticket_summary(self):
        print(f"Ticket ID     : {self.ticket_id}")
        print(f"User Name     : {self.user_name}")
        print(f"Issue         : {self.issue_description}")
        print(f"Category      : {self.issue_category}")
        print(f"Priority      : {self.__priority}")
        print(f"Status        : {self.__status}")
        print(f"Assigned Team : {self.assigned_team}")
        print(f"Created At    : {self.created_at}")
        # Separator only for base Ticket; children add extras then print their own
        if type(self) is Ticket:
            print("-" * 40)



# Inheritance - TechnicalTicket is a subclass of Ticket
class TechnicalTicket(Ticket):
    def __init__(self, ticket_id, user_name, issue_description, priority, system_name, error_code):
        # Common attributes initialized through the parent
        super().__init__(ticket_id, user_name, issue_description, "Technical", priority)
        # Child-specific attributes
        self.system_name = system_name
        self.error_code = error_code

    def assign_team(self):
        self.assigned_team = "Technical Team"

    def get_ticket_summary(self):
        super().get_ticket_summary()
        print(f"System Name   : {self.system_name}")
        print(f"Error Code    : {self.error_code}")
        print("-" * 40)


# Inheritance - PaymentTicket is a subclass of Ticket
class PaymentTicket(Ticket):
    def __init__(self, ticket_id, user_name, issue_description, priority, transaction_id, payment_amount):
        # Common attributes initialized through the parent
        super().__init__(ticket_id, user_name, issue_description, "Payment", priority)
        # Child-specific attributes
        self.transaction_id = transaction_id
        self.payment_amount = payment_amount

    def assign_team(self):
        self.assigned_team = "Finance Team"

    def get_ticket_summary(self):
        super().get_ticket_summary()
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Payment Amount: {self.payment_amount}")
        print("-" * 40)


# Inheritance - AccountTicket is a subclass of Ticket
class AccountTicket(Ticket):
    def __init__(self, ticket_id, user_name, issue_description, priority, account_type, requested_change):
        # Common attributes initialized through the parent
        super().__init__(ticket_id, user_name, issue_description, "Account", priority)
        # Child-specific attributes
        self.account_type = account_type
        self.requested_change = requested_change

    def assign_team(self):
        self.assigned_team = "Support Team"

    def get_ticket_summary(self):
        super().get_ticket_summary()
        print(f"Account Type  : {self.account_type}")
        print(f"Requested     : {self.requested_change}")
        print("-" * 40)