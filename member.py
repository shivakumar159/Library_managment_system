class Member:
    """This class stores and manages member details"""

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    #Display member details
    def display(self):
        print(f"{self.member_id}, {self.name}, {self.email}")

    #Update member name
    def update_name(self, name):
        self.name = name
        print("Member name updated successfully")

    #Update member email
    def update_email(self, email):
        self.email = email
        print("Member email updated successfully")

    #Return member name
    def get_name(self):
        return self.name

    #Return member email
    def get_email(self):
        return self.email
    

    