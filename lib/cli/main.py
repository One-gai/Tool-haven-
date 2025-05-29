
from lib.db.setup import session
from lib.db.setup import create_tables

from lib.db.setup import session, create_tables

from lib.models.user import User
from lib.models.tool import Tool
from lib.models.part import Part
from lib.models.checkout import Checkout

def main_menu():
    while True:
        print("\n===== Workshop Inventory CLI ======")
        print("\nUsers Prompt")
        print("1. Create user | 2. View all users | 3. Delete user")

        print("\nTools Prompt")
        print("4. Create Tool | 5. View all tools | 6. Delete Tool")
        

        print("\nPart Prompt")
        print("7. Create part | 8. View all parts | 9. Delete part")
    
        print("\nCheckout Prompt")
        print("10. Create a checkout | 11. View all checkouts | 12. Delete a checkout")
        
        print("\n0. Exit")
        
        choice = input("Enter choice: ")
        #This is Users
        if choice == "1":
            name = input("Enter user name: ")
            role = input("Enter role: ")
            User.create(session, name, role)
        elif choice == "2":
            for user in User.get_all(session):
                print(f"\n{user.id}: {user.name} ({user.role})")
        elif choice == "3":
            user_id = int(input("\nEnter user ID to delete: "))
            if User.delete(session, user_id):
                print("\n~~~~~ User Deleted ~~~~~")
            else:
                print("\n~~~~~ User not found ~~~~~")

        #This is Tools        
        elif choice == "4":
            name = input("\nEnter tool name: ")
            description = input("\nEnter tool description: ")
            Tool.create(session, name, description)
        elif choice == "5":
            tools = Tool.get_all(session)
            for tool in tools:
                print(f"\nID: {tool.id}| Name: {tool.name} | Description: {tool.description}")
        elif choice == "6":

            tool_id = int(input("\nEnter tool ID to Delete: "))

            tool_id = int(input("\nEnter tool ID to Delete"))

            if Tool.delete(session, tool_id):
                print("\n~~~~~ Tool deleted. ~~~~~")
            else:
                print("\n~~~~~ Tool not found. ~~~~~")

        #This is the Exit option        
        elif choice == "0":
            print("\n~~~~~ Goodbye! ~~~~~")
            break

        #This is Parts
        elif choice == "7":
            name = input("\n Enter part name: ")
            description = input("\n Enter part description: ")
            quantity = input("\n Enter quantity of part: ")
            Part.create(session, name, description, quantity)
        elif choice == "8":
            parts = Part.get_all(session)
            for part in parts:
                print(f"\nID : {part.id} | Name: {part.name} | Description: {part.description} | Quantity: {part.quantity}")
        elif choice == "9":
            part_id = int(input("\nEnter part ID to Delete: "))
            if Part.delete(session, part_id):
                print("\n~~~~~ Part deleted. ~~~~~")
            else:
                print("\n~~~~~ Part not found ~~~~~")

        #This is Checkouts        
        elif choice == "10":
            user_id = int(input("\nEnter User ID: "))
            tool_id = int(input("\nEnter Tool ID: "))


            user = User.find_by_id(session, user_id)
            tool = Tool.find_by_id(session, tool_id)
        
            if not user and not tool:
                print("\n~~~~~ Error: Both User ID and Tool ID are invalid. ~~~~~")
            elif not user:
                print("\n~~~~~ Error: User ID is invalid. ~~~~~")
            elif not tool:
                print("\n~~~~~ Error: Tool ID is invalid. ~~~~~")
            else:
                Checkout.create(session, user_id, tool_id)
                print("\n~~~~~ Checkout created. ~~~~~.")

            

        elif choice == "11":
            checkouts = Checkout.get_all(session)
            for checkout in checkouts:
                print(f"\nCheckout ID: {checkout.id} | User ID: {checkout.user_id} | Tool ID: {checkout.tool_id} | Timestamp: {checkout.timestamp}")

        elif choice == "12":
            checkout_id = int(input("\nEnter Checkout ID to Delete: "))
            if Checkout.delete(session, checkout_id):
                print("\n~~~~~ Checkout deleted. ~~~~~")
            else:
                print("\n~~~~~ Tool not found. ~~~~~") 

        #This is for anything else
        else:
            print("\n~~~~~ Invalid choice. ~~~~~")

if __name__ == "__main__":
    create_tables()
    main_menu()
