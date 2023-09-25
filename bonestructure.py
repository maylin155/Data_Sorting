import os
import pandas as pd

def export():
    print("Do you want to export the file?")
    answer = input("Enter yes or no: ")
    if answer == 'yes':
        print("File exported")
    elif answer == 'no':
        main()
    
def main():
    folder_path = input("Enter the folder path where raw data is located: ")
    if os.path.exists(folder_path):
        df = pd.read_csv(folder_path)
        print(df)
    else:
        raise FileNotFoundError('No such file or directory')
    # Perform data preprocessing
    
    while True:
        print("Search the title by:")
        print("1. Module")
        print("2. Lecturer")
        print("3. Location")
        print("4. Exit the program")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Search by Module
            export()
        elif choice == '2':
            # Search by Lecturer
            export()
        elif choice == '3':
            #Search by Location
            export()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# Convert the DataFrame to a list of dictionaries
#data_list = df.to_dict(orient='records')
