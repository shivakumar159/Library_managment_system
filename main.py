from book import Book
from member import Member
from borrow import Borrow
from file_manager import FileManager

# Initial sample data for books, members, and records
books = [
    Book(101, "Atomic Bomb", "James Robart", 5),
    Book(102, "Naa Book Naa Ishtam", "Prsiddhi", 4),
    Book(103, "The Rular", "Paulo Raj", 3),
    Book(104, "Think Big", "Ben Robu", 2)
]

members = [
    Member(1, "Shiva Kumar", "shiva@gmail.com"),
    Member(2, "Aarav Singh", "aarav@gmail.com"),
    Member(3, "Meera Patel", "meera@yahoo.com")
]

borrow_records = []
borrow_id = 1
file_manager = FileManager()

# Main menu loop  runs until user chooses Exit
while True:
    print("\n LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Member")
    print("4. View Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. View Borrow Records")
    print("8. Save Books")
    print("9. Read Books File")
    print("10. Clear File")
    print("11. Exit")

    # Add a new book
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            book_id = int(input("Book ID: "))
            title = input("Book Title: ")
            author = input("Author: ")
            quantity = int(input("Quantity: "))

            book = Book(book_id, title, author, quantity)  #Create a new Book object and add to list
            books.append(book)

            print("Book added successfully")

        except ValueError:
            print("Invalid input, Please enter numbers correctly")

    #View all books
    elif choice == "2":
        print("\n Available Books")
        for book in books:
            book.display()

    #Add a new member
    elif choice == "3":
        try:
            member_id = int(input("Member ID: "))
            name = input("Member Name: ")
            email = input("Email: ")

            member = Member(member_id, name, email) #Create a new Member object and add to list
            members.append(member)

            print("Member added successfully")

        except ValueError:
            print("Invalid member ID")

    #View all members
    elif choice == "4":
        print("\n Library Members")
        for member in members:
            member.display()

    #Borrow a book
    elif choice == "5":
        member_name = input("Member Name: ")
        book_title = input("Book Title: ")

        found = False

        for book in books:
            if book.title.lower() == book_title.lower():  #Check if book title matches
                found = True

                # Try to borrow the book
                if book.borrow_book():
                    record = Borrow(borrow_id, member_name, book_title)
                    borrow_records.append(record)
                    borrow_id += 1

                break

        if not found:
            print("Book not found")

    # Return a book
    elif choice == "6":
        book_title = input("Enter returned book title: ")

        found = False

        for book in books:
            if book.title.lower() == book_title.lower():  #Check if book exists
                book.return_book()
                found = True
                break

        if not found:
            print("Book not found")

    #View all borrow records
    elif choice == "7":
        print("\n Borrow Records")

        if not borrow_records:
            print("No borrow records found")
        else:
            for record in borrow_records:
                record.display()

    #Save books to CSV file
    elif choice == "8":
        file_manager.save_books(books)

    #Read books from CSV file
    elif choice == "9":
        file_manager.read_books()

    #Clear the CSV file
    elif choice == "10":
        file_manager.clear_file()

    #Exit the program
    elif choice == "11":
        print("Thank you for using Library Management System")
        break
    
    #Invalid menu choice
    else:
        print("Invalid choice. Try again")