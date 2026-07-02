class User:

    def __init__(self, user_id, name, email, role, department):
        self.user_id = user_id
        self.user_name = name
        self.user_email = email
        self.role = role
        self.department = department

    def display_user(self):
        print(f"User ID    : {self.user_id}")
        print(f"User Name  : {self.user_name}")
        print(f"Email      : {self.user_email}")
        print(f"Role       : {self.role}")
        print(f"Department : {self.department}")

    def update_department(self, department):
        self.department = department

    def update_role(self, new_role):
        self.role = new_role

    def update_email(self, new_email):
        self.user_email = new_email