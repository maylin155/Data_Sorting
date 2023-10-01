import pandas as pd
import os

def remove_column(df):
    return df.drop(['Name'], axis=1)

def splitData(txt, splitstr):
    x = txt.split(splitstr)
    return x

def extract_module_data(name):
        split_value = splitData(name,"_")
        if len(split_value) >= 4:
            return split_value[3]
        else:
             return None

def extract_session_data(name):
    split_value = splitData(name, "_")
    session_list = splitData(split_value[4], "/")
    if len(session_list) >= 1:
         return session_list[0]
    else:
         return None

def load_folder(folder_path):
    excel_dict_list = []

    # List all files in the folder
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            #Extract Module and Session data from name column and create new.
            df['Module'] = df['Name'].apply(extract_module_data)
            df['Session'] = df['Name'].apply(extract_session_data)

            #Remove name column
            df = remove_column(df)

            # Convert the DataFrame to a list of dictionaries
            dict_list = df.to_dict(orient='records')

            # Extend the excel_dict_list with data from the current file
            excel_dict_list.extend(dict_list)

        except Exception as e:
            print(f"Error processing file {file_name}: {str(e)}")

    return excel_dict_list

def main():
    folder_path = input("Enter folder path: ")
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
         excel_dict_list = load_folder(folder_path)
         print(excel_dict_list)
    

if __name__ == "__main__":
    main()