from database import Database

class Members:
    def __init__(self):
        self.db = Database()

    def add_member(self):
        name = input("Enter member name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")

        query = "INSERT INTO members (name, address, phone) VALUES (%s, %s, %s)"
        data = (name, address, phone)

        if self.db.execute_query(query, data):
            print("Member added successfully!")
        else:
            print("Error adding member.")

    def display_members(self):
        query = "SELECT * FROM members"
        members = self.db.fetch_query(query)

        print("\nMembers in Library:")
        print("ID  | Name             | Address          | Phone")
        print("-" * 50)

        for member in members:
            print(f"{member[0]:<4} | {member[1]:<18} | {member[2]:<18} | {member[3]:<10}")
