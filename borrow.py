class Borrow:
    """This class stores and manages borrowing records"""

    def __init__(self, borrow_id, member_name, book_title):
        self.borrow_id = borrow_id
        self.member_name = member_name
        self.book_title = book_title

    #Display borrow record
    def display(self):
        print(f"{self.borrow_id}, {self.member_name}, {self.book_title}")

    #Update book title in borrow record
    def update_book(self, book_title):
        self.book_title = book_title
        print("Borrow book title updated successfully")

    #Update member name in borrow record
    def update_member(self, member_name):
        self.member_name = member_name
        print("Borrow member name updated successfully")

    #Return book title from record
    def get_record(self):
        return self.book_title

    #Return member name
    def get_member_name(self):
        return self.member_name