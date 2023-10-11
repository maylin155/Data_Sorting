from Database import *
from Menu import *

def start():
    db_instance = Database()  # Instantiate the Database
    menu = Menu(db_instance)  # Pass the Database instance to Menu

    data = db_instance.load_folder()  # Use Database instance to call load_folder()
    db_instance.store_data(data)      # Use Database instance to call store_data()
    db_instance.display_database()    # Use Database instance to call display_database()

    while True:
        try:
            menu.get_sort_menu()
            menu.get_search_menu()
            menu.get_export_menu()
            break
        except KeyError:
            print("The data is not found in the list. Please try again.")

def main():
    start()
    
if __name__ == "__main__":
    main()