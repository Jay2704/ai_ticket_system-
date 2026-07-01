
class Users:

    def __init__(self, id, name, email, role, dept) -> None:
        self.user_id = id
        self.user_name = name
        self.user_email = email
        self.role = role
        self.department = dept

    def display_user(self):
        print(f"User ID         : {self.user_id}")
        print(f"User Name       : {self.user_name}")
        print(f"Email           : {self.user_email}")
        print(f"Role            : {self.role}")
        print(f"Department      : {self.department}")

    def update_department(self, dept):
        self.department = dept

    def update_role(self, new_role):
        self.role = new_role

    def update_email(self, new_email):
        self.email = new_email
    