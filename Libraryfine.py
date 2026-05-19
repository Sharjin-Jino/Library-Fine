# ===== LIBRARY FINE SYSTEM =====

class Library:
    def __init__(self):
        self.books = {}

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        self.books[book_id] = {
            "name": name,
            "issued": False
        }
        print("Book Added Successfully!\n")

    # View Books
    def view_books(self):
        if not self.books:
            print("No Books Available\n")
            return

        print("\n--- BOOK LIST ---")
        for bid, data in self.books.items():
            status = "Issued" if data["issued"] else "Available"
            print(f"ID: {bid} | Name: {data['name']} | Status: {status}")
        print()

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID to Issue: ")

        if book_id in self.books:
            if not self.books[book_id]["issued"]:
                self.books[book_id]["issued"] = True
                print("Book Issued Successfully!\n")
            else:
                print("Book Already Issued!\n")
        else:
            print("Book Not Found!\n")

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID to Return: ")

        if book_id in self.books:
            if self.books[book_id]["issued"]:
                self.books[book_id]["issued"] = False

                days = int(input("Enter Late Days: "))

                if days <= 5:
                    fine = days * 2
                elif days <= 10:
                    fine = days * 5
                else:
                    fine = days * 10

                print("Book Returned Successfully!")
                print("Fine Amount =", fine, "\n")
            else:
                print("Book Was Not Issued!\n")
        else:
            print("Book Not Found!\n")


# Main Program
lib = Library()

while True:
    print("===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        lib.add_book()

    elif choice == "2":
        lib.view_books()

    elif choice == "3":
        lib.issue_book()

    elif choice == "4":
        lib.return_book()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")
