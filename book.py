class Book:
    """This class stores and manages book details"""

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    #Display book details
    def display(self):
        print(f"{self.book_id}, {self.title}, {self.author}, {self.quantity}")

    #Update book quantity
    def update_quantity(self, quantity):
        self.quantity = quantity
        print("Book quantity updated successfully")

    #Borrow a book
    def borrow_book(self):
        if self.quantity > 0:
            self.quantity -= 1
            print("Book borrowed successfully")
            return True
        else:
            print("Book is not available")
            return False

    #Return a book
    def return_book(self):
        self.quantity += 1
        print("Book returned successfully")

    #Get book title
    def get_title(self):
        return self.title