from books import Books
from members import Members
from transactions import Transactions

def main():
    books = Books()
    members = Members()
    transactions = Transactions()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Display Transactions")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            books.add_book()
        elif choice == '2':
            members.add_member()
        elif choice == '3':
            transactions.issue_book(books, members)
        elif choice == '4':
            transactions.return_book()
        elif choice == '5':
            books.display_books()
        elif choice == '6':
            members.display_members()
        elif choice == '7':
            transactions.display_transactions()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
