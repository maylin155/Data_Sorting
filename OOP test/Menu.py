import os
from DB import *
import re

class Menu(DB):
    def __init__(self):
        super().__init__()
        self.exportDB = []

    def exit(self):
        os.system('cls')

    def convert_into_uppercase(self, a):
        return a.group(1) + a.group(2).upper()

    def get_search_menu(self):
        print("Search the title by:")
        print("1. Module")
        print("2. Lecturer")
        print("3. Zone Name")
        print("4. Exit the program")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            #Search by Module
            key_to_search = 'Module'
            value_to_find = input(f"Enter the Module you want to search for '{key_to_search}': ").upper()
            found_dicts = self.search_by_value(self.database, key_to_search, value_to_find)

            if found_dicts:
                df = pd.DataFrame(found_dicts)
                self.exportDB = found_dicts
                print(df)
            else:
                print(f"No dictionaries found with {key_to_search} = {value_to_find}")
                self.get_search_menu()
        elif choice == '2':
            # Search by Lecturer
            key_to_search = 'Allocated Staff Name'
            value_to_find = input(f"Enter the Lecturer you want to search for '{key_to_search}': ")
            value_to_find = re.sub("(^|\s)(\S)", self.convert_into_uppercase, value_to_find)
            found_dicts = self.search_by_value(self.database, key_to_search, value_to_find)

            if found_dicts:
                df = pd.DataFrame(found_dicts)
                self.exportDB = found_dicts
                print(df)
            else:
                print(f"No dictionaries found with {key_to_search} = {value_to_find}")
                self.get_search_menu()
        elif choice == '3':
            #Search by Location
            key_to_search = 'Zone Name'
            value_to_find = input(f"Enter the Zone Name you want to search for '{key_to_search}': ").capitalize()
            found_dicts = self.search_by_value(self.database, key_to_search, value_to_find)

            if found_dicts:
                df = pd.DataFrame(found_dicts)
                self.exportDB = found_dicts
                print(df)
            else:
                print(f"No dictionaries found with {key_to_search} = {value_to_find}")
                self.get_search_menu()
        elif choice == '4':
            self.exit()
        else:
            print("Invalid choice. Please try again.")
            self.get_search_menu()

    def get_sort_menu(self):
        print("Sort the timetable by")
        user_input = input("(M)odule or (D)ate? ").upper()
        #Sort by Module
        if user_input == "M":
            sort_by = input("(A)scending or (D)escending? ").upper()
            if sort_by == "A":
                sorted_data = self.merge_sort_by_module(self.database, ascending = True)
                df = pd.DataFrame.from_records(sorted_data)
                print(df)
            elif sort_by == "D":
                sorted_data = self.merge_sort_by_module(self.database, ascending = False)
                df = pd.DataFrame.from_records(sorted_data)
                print(df)
            else:
                print("Invalid option. Please try again.")
                return
            return sorted_data
        #Sort by Date
        elif user_input == "D":
            sort_by = input("(A)scending or (D)escending? ").upper()
            if sort_by == "A":
                sorted_data = self.merge_sort_by_date(self.database, ascending = True)
                df = pd.DataFrame.from_records(sorted_data)
                print(df)
            elif sort_by == "D":
                sorted_data = self.merge_sort_by_date(self.database, ascending = False)
                df = pd.DataFrame.from_records(sorted_data)
                print(df)
            else:
                print("Invalid option. Please try again.")
                return
            return sorted_data
        else:
            print("Invalid choice.Please try again")
            self.get_sort_menu()

    #Export the data frame to excel file.
    def get_export_menu(self):
        choice = input("Do you want to export the file : (Y) or (N)? ").upper()
        if choice == "Y":
            filename = input("Enter the filename to export: ")
            df = pd.DataFrame.from_records(self.exportDB)
            df.to_csv(rf"D:\Yona\BCS\Algorithms and Data Structures\casestudy\OOP test\exported_files\{filename}.csv")
            print("Exported")
        elif choice == "N":
            print("1. Go back to main menu")
            print("2. Exit the program.")
            user_input = input("Choose option: ")
            if user_input == '1':
                DB.importFile()
            if user_input == '2':
                self.exit()
            else:
                print("Invalid choice")
                self.get_export_menu()
        else:
            print("Invalid choice.Please try again.")
            self.get_export_menu()

    
    def export_to_csv(data, filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)