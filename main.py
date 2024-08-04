class Property:
    def __init__(self, property_id, title, description, price, location):
        self.property_id = property_id
        self.title = title
        self.description = description
        self.price = price
        self.location = location

    def __str__(self):
        return f"ID: {self.property_id}, Title: {self.title}, Price: {self.price}, Location: {self.location}\nDescription: {self.description}\n"

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

class RealEstateManagementSystem:
    def __init__(self):
        self.properties = []
        self.users = []
        self.next_property_id = 1
        self.next_user_id = 1

    def add_property(self, title, description, price, location):
        property = Property(self.next_property_id, title, description, price, location)
        self.properties.append(property)
        self.next_property_id += 1
        print(f"Property '{title}' added successfully.")
    
    def view_properties(self):
        if not self.properties:
            print("No properties available.")
        else:
            for property in self.properties:
                print(property)

    def add_user(self, username, email):
        user = User(self.next_user_id, username, email)
        self.users.append(user)
        self.next_user_id += 1
        print(f"User '{username}' added successfully.")

    def send_promotional_message(self, message):
        if not self.users:
            print("No users to send messages to.")
        else:
            for user in self.users:
                print(f"Sending message to {user.email}: {message}")
            print("Promotional message sent successfully.")

def main():
    system = RealEstateManagementSystem()
    while True:
        print("\nReal Estate Management System")
        print("1. Add Property")
        print("2. View Properties")
        print("3. Register User")
        print("4. Send Promotional Message")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            title = input("Enter property title: ")
            description = input("Enter property description: ")
            price = float(input("Enter property price: "))
            location = input("Enter property location: ")
            system.add_property(title, description, price, location)
        elif choice == 2:
            system.view_properties()
        elif choice == 3:
            username = input("Enter username: ")
            email = input("Enter email: ")
            system.add_user(username, email)
        elif choice == 4:
            message = input("Enter promotional message: ")
            system.send_promotional_message(message)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

            
            
                           
        