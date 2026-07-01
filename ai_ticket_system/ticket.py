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

    def create_ticket(self):
        pass

    def update_status(self):
        pass

    def update_priority(self):
        pass

    def assign_team(self):
        pass

    def get_ticket_summary(self):
        # display the info aboutthe ticket
        pass 
