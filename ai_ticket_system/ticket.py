from constants import PRIORITIES, STATUSES


class Ticket:

    def __init__(self, ticket_id, user_name, issue_description, issue_category, priority):
        self.ticket_id = ticket_id
        self.user_name = user_name
        self.issue_description = issue_description
        self.issue_category = issue_category
        self.assigned_team = "Unassigned"
        self.created_at = "Today"
        self.status = "Open"
        self.priority = PRIORITIES[2][0]

        if self._is_valid_priority(priority):
            self.priority = priority
        else:
            print("Invalid priority")

    def _is_valid_status(self, new_status):
        return any(status[0] == new_status for status in STATUSES.values())

    def _is_valid_priority(self, new_priority):
        return any(priority[0] == new_priority for priority in PRIORITIES.values())

    def update_status(self, new_status):
        if self._is_valid_status(new_status):
            self.status = new_status
        else:
            print("Invalid status")

    def update_priority(self, new_priority):
        if self._is_valid_priority(new_priority):
            self.priority = new_priority
        else:
            print("Invalid priority")

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
        print(f"Priority      : {self.priority}")
        print(f"Status        : {self.status}")
        print(f"Assigned Team : {self.assigned_team}")
        print(f"Created At    : {self.created_at}")
        print("-" * 40)