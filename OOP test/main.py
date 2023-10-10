from Database import *
from Dataset import *
from Menu import *

def start():
    menu = Menu()
    data = menu.load_folder()
    menu.store_data(data)
    menu.wrap_text()
    menu.display_database()
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