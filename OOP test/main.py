from Database import *
from Menu import *
import os

def load_and_store_data(db_instance):
    """
    Loads data from a folder and stores it in the database.
    """
    try:
        data = db_instance.load_folder()
        db_instance.store_data(data)
    except Exception as e:  # You can catch a more specific exception if you know what to expect.
        print(f"Error loading or storing data: {e}")
        return False

    return True

def start():
    while True:
        db_instance = Database()
        menu = Menu(db_instance)

        if not load_and_store_data(db_instance):
            print("Failed to initialize the database.")
            return

        db_instance.display_database()

        try:
            menu.get_sort_menu()
            menu.get_search_menu()
            menu.get_export_menu()
            break  # If no errors occurred, break out of the loop.
        except KeyError:
            print("The data is not found in the list. Please try again.")
        except Exception as e:  # Catch any unexpected errors.
            print(f"An error occurred: {e}")

        # Ask the user if they want to restart the program.
        choice = input("Do you want to restart the program? (yes/no): ").lower().strip()
        if choice != "yes":
            print("Exiting program.")
            break

def main():
    start()
    
if __name__ == "__main__":
    main()