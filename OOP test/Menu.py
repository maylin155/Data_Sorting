import os
from datetime import datetime
from Database import *
from tabulate import tabulate
import re
import time

class Menu():
    def __init__(self, database):
        self.database = database
        self.exportDB =[]


    def exit(self):
        os.system('cls')

    def convert_into_uppercase(self, a):
        return a.group(1) + a.group(2).upper()

    def get_search_menu(self):
        print("Search the timetable by:")
        print("1. Module")
        print("2. Lecturer")
        print("3. Location/Room")
        print("4. Date")
        print("5. Date Range")
        print("6. Specific Time") 
        print("7. Time Range : Start Time - End Time")
        print("8. Day")
        print("9. Exit the program")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            #Search by Module
            key_to_search = 'Module'
            value_to_find = input(f"Enter the Module you want to search for '{key_to_search}': ").upper()
            found_dicts = self.database.search_by_value(self.database.database,key_to_search, value_to_find)

            if found_dicts:
                self.exportDB = found_dicts
                print(tabulate(found_dicts, headers="keys", tablefmt="grid"))
                #self.database.display_database(found_dicts)
            else:
                print(f"No Schedule found with {key_to_search} = {value_to_find}")
                self.get_search_menu()
        elif choice == '2':
            # Search by Lecturer
            key_to_search = 'Allocated Staff Name'
            value_to_find = input(f"Enter the Lecturer you want to search for '{key_to_search}': ")
            value_to_find = re.sub("(^|\s)(\S)", self.convert_into_uppercase, value_to_find)
            found_dicts = self.database.search_by_value(self.database.database, key_to_search, value_to_find)

            if found_dicts:
                self.exportDB = found_dicts
                print(tabulate(found_dicts, headers="keys", tablefmt="grid"))
                #self.database.display_database(found_dicts)
            else:
                print(f"No Schedule found with {key_to_search} = {value_to_find}")
                self.get_search_menu()

        elif choice == '3':
            #Search by Location
            key_to_search = 'Allocated Location Name'
            value_to_find = input(f"Enter the Zone Name you want to search for '{key_to_search}': ")
            value_to_find = re.sub("(^|\s)(\S)", self.convert_into_uppercase, value_to_find)
            found_dicts = self.database.search_by_value(self.database.database,key_to_search, value_to_find)

            if found_dicts:
                self.exportDB = found_dicts
                print(tabulate(found_dicts, headers="keys", tablefmt="grid"))
                #self.database.display_database(found_dicts)
            else:
                print(f"No Schedule found with {key_to_search} = {value_to_find}")
                self.get_search_menu()

        elif choice == '4':
            #Search by Date
            key_to_search = 'Activity Dates (Individual)'
            value_to_find = input(f"Enter the Date(DD/M/YYYY) you want to search for '{key_to_search}': ")
            found_dicts = self.database.search_by_value(self.database.database, key_to_search, value_to_find)

            if found_dicts:
                self.exportDB = found_dicts
                print(tabulate(found_dicts, headers="keys", tablefmt="grid"))
                #self.database.display_database(found_dicts)
            else:
                print(f"No Schedule found with {key_to_search} = {value_to_find}")
                self.get_search_menu()

        elif choice == '5':
            # Search by Date Range
            start_date = input("Enter the Start Date in (dd/mm/yyyy) : ")
            end_date = input("Enter the End Date in (dd/mm/yyyy): ")

            # Convert input dates to datetime objects for comparison
            start_date = datetime.strptime(start_date, '%d/%m/%Y')
            end_date = datetime.strptime(end_date, '%d/%m/%Y')

            found_dicts = []
            # Iterate through the database and find dictionaries within the date range
            for item in self.database.database:
                if "Activity Dates (Individual)" in item:
                    activity_dates = item["Activity Dates (Individual)"].split(", ")
                    for date_str in activity_dates:
                        date = datetime.strptime(date_str, '%d/%m/%Y')
                        if start_date <= date <= end_date:
                            found_dicts.append(item)

            if found_dicts:
                self.exportDB = found_dicts
                print(tabulate(found_dicts, headers="keys", tablefmt="grid"))
                #self.database.display_database(found_dicts)
            else:
                print(f"No schedules found between {start_date} and {end_date}")
                self.get_search_menu()  # Continue the search menu loop
        

        elif choice == '6':
            #Search by Specific Time
            time = input("Enter a specific time in (HH:MM:SS): ")
            found_dicts = self.database.search_by_specific_time(self.database.database,time)

            if found_dicts:
                self.exportDB = found_dicts
                print(tabulate(found_dicts, headers="keys", tablefmt="grid"))
                #self.database.display_database(found_dicts)
            else:
                print(f"No Schedule found with {key_to_search} = {value_to_find}")
                self.get_search_menu()

        elif choice == '7':
            # Search by Start and End Time
            start_time = input("Enter the Start Time in 24-hour-format (HH:MM:SS) : ")
            end_time = input("Enter the End Time in 24-hour-format (HH:MM:SS): ")

            # Convert the input times to a format suitable for searching
            start_time = pd.to_datetime(start_time).strftime('%H:%M:%S')
            end_time = pd.to_datetime(end_time).strftime('%H:%M:%S')

            found_dicts = self.database.search_by_start_end_time(self.database.database,start_time, end_time)

            if found_dicts:
                self.exportDB = found_dicts
                print(tabulate(found_dicts, headers="keys", tablefmt="grid"))
                #self.database.display_database(found_dicts)
            else:
                print(f"No schedules found between {start_time} and {end_time}")
                self.get_search_menu()  # Continue the search menu loop

        elif choice == '8':
            # Search by Day
            key_to_search = 'Scheduled Days'
            value_to_find = input(f"Enter the Day you want to search for '{key_to_search}': ").capitalize()
            found_dicts = self.database.search_by_value(self.database.database,key_to_search, value_to_find)

            if found_dicts:
                self.exportDB = found_dicts
                print(tabulate(found_dicts, headers="keys", tablefmt="grid"))
                #self.database.display_database(found_dicts)
            else:
                print(f"No Schedule found with {key_to_search} = {value_to_find}")
                self.get_search_menu()
        
        elif choice == '9':
            #Exit the search
            self.exit()
        else:
            print("Invalid choice. Please try again.")
            self.get_search_menu()

    def get_sort_menu(self):
        print("Sort the timetable by")
        user_input = input("(M)odule or (D)ate? ").upper()
        sorted_data = None
        #Sort by Module
        if user_input == "M":
            sort_by = input("(A)scending or (D)escending? ").upper()
            if sort_by == "A":
                sorted_data = self.database.merge_sort_by_module(data=self.database.database,ascending = True)
            elif sort_by == "D":
                sorted_data = self.database.merge_sort_by_module(data = self.database.database,ascending = False)
            else:
                print("Invalid option. Please try again.")
                return
        #Sort by Date
        elif user_input == "D":
            sort_by = input("(A)scending or (D)escending? ").upper()
            if sort_by == "A":
                sorted_data = self.database.merge_sort_by_date(data = self.database.database,ascending = True)
            elif sort_by == "D":
                sorted_data = self.database.merge_sort_by_date(data = self.database.database,ascending = False)
            else:
                print("Invalid option. Please try again.")
                return
        else:
            print("Invalid choice.Please try again")
            self.get_sort_menu()
            return
        
        if sorted_data:
            self.database.database = sorted_data
            self.database.display_sorted_data(sorted_data)
        else:
            print("Invalid data.")


    #Export the data frame to excel file.
    def get_export_menu(self):
        choice = input("Do you want to export the file : (Y) or (N)? ").upper()
        if choice == "Y":
            filename = input("Enter the filename to export: ")
            df = pd.DataFrame.from_records(self.exportDB)
            df.to_csv(rf"D:\Yona\BCS\Algorithms and Data Structures\casestudy\OOP test\exported_files\{filename}.csv")
            print("Exported")
        elif choice == "N":
                exit_message = "Exiting the program ..."
                for char in exit_message:
                    print(char, end='', flush=True)  # Print one character at a time without a newline
                    time.sleep(0.1)  # Delay of 0.1 seconds between each character
                print()  # Newline after the message
                self.exit()
        else:
                print("Invalid choice")
                self.get_export_menu()

