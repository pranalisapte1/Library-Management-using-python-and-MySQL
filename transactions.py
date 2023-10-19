from database import Database

class Transactions:
    def __init__(self):
        self.db = Database()

    def issue_book(self, books, members):
        books.display_books()
        book_id = int(input("Enter the ID of the book to be issued: "))

        members.display_members()
        member_id = int(input("Enter the ID of the member: "))

        query = "INSERT INTO transactions (book_id, member_id) VALUES (%s, %s)"
        data = (book_id, member_id)

        if self.db.execute_query(query, data):
            print("Book issued successfully!")
            books.update_copies(book_id, -1)
        else:
            print("Error issuing book.")

    def return_book(self):
        transaction_id = int(input("Enter the ID of the transaction to be returned: "))

        query = "DELETE FROM transactions WHERE id = %s"
        data = (transaction_id,)

        if self.db.execute_query(query, data):
            print("Book returned successfully!")
        else:
            print("Error returning book.")

    def display_transactions(self):
        query = """
            SELECT transactions.id, books.title, members.name
            FROM transactions
            JOIN books ON transactions.book_id = books.id
            JOIN members ON transactions.member_id = members.id
        """
        transactions = self.db.fetch_query(query)

        print("\nTransaction History:")
        print("ID  | Book Title        | Member Name")
        print("-" * 45)

        for transaction in transactions:
            print(f"{transaction[0]:<4} | {transaction[1]:<18} | {transaction[2]:<18}")

