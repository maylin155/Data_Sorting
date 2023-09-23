import os
import pandas as pd

# Define a function to load data from CSV files in a folder
def load_data(folder_path):
    if os.path.exists(folder_path):
        df=pd.read_csv(folder_path)
        print(df)
    else:1
        raise FileNotFoundError('No such file or directory')




# Define a function to view the schedule
def view_schedule(df):
    print("Schedule:")
    print(df)

# Define a function to generate a timetable (You can implement this based on your requirements)

# Define the main program
def main():
    while True:
        print("Options:")
        print("1. Load data")
        print("2. View Schedule")
        print("3. Generate Timetable")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            folder_path = input("Enter the folder path where raw data is located: ")
            data = load_data(folder_path)

            #data = preprocess_data(data)
            print("Data loaded and preprocessed.")
        elif choice == '2':
            if 'data' in locals():
                view_schedule(data)
            else:
                print("Please load data first.")
        elif choice == '3':
            if 'data' in locals():
                # Generate timetable
                pass
            else:
                print("Please load data first.")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

