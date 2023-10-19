from database import Database

class Books:
    def __init__(self):
        self.db = Database()

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        copies = int(input("Enter number of copies: "))

        query = "INSERT INTO books (title, author, genre, copies) VALUES (%s, %s, %s, %s)"
        data = (title, author, genre, copies)

        if self.db.execute_query(query, data):
            print("Book added successfully!")
        else:
            print("Error adding book.")

    def display_books(self):
        query = "SELECT * FROM books"
        books = self.db.fetch_query(query)

        print("\nBooks in Library:")
        print("ID  | Title             | Author           | Genre      | Copies")
        print("-" * 60)

        for book in books:
            print(f"{book[0]:<4} | {book[1]:<18} | {book[2]:<18} | {book[3]:<10} | {book[4]:<6}")

