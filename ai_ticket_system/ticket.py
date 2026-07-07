class Ticket:

    def __init__(self, ticket_id, user_name, issue_description, issue_category, priority):
        self.ticket_id = ticket_id
        self.user_name = user_name
        self.issue_description = issue_description
        self.issue_category = issue_category
        self.priority = priority
        self.status = "Open"
        self.assigned_team = "Unassigned"
        self.created_at = "Today"

    def update_status(self, new_status):
        # self.status = new_status
        pass

    def update_priority(self, new_priority):
        self.priority = new_priority

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