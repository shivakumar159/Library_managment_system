import csv


class FileManager:
    """Handles all file operations for the library system"""

    def __init__(self, filename="books.csv"):
        self.filename = filename

    #Save books to CSV file
    def save_books(self, books):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Book ID", "Title", "Author", "Quantity"])

            for book in books:
                writer.writerow([
                    book.book_id,
                    book.title,
                    book.author,
                    book.quantity
                ])

        print("Books saved successfully")

    #Read books from CSV file
    def read_books(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    print(row)

        except FileNotFoundError:
            print("No file found")

    #Clear file contents
    def clear_file(self):
        open(self.filename, "w").close()
        print("File cleared successfully")

    # Append one book to file
    def append_book(self, book):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                book.book_id,
                book.title,
                book.author,
                book.quantity
            ])

        print("Book added to file")

    #Return file name
    def get_filename(self):
        return self.filename