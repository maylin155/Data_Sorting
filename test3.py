import pandas as pd
import os
from datetime import datetime


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

def merge_sort_by_module(data):
    if len(data) <= 1:
        return data

    # Find the mid of the list
    mid = len(data) // 2
    #Dividing 
    L = data[:mid]
    R = data[mid:]

    # Recursively sort each half
    L = merge_sort_by_module(L)
    R = merge_sort_by_module(R)

    result = []
    i, j = 0, 0

    while i < len(L) and j < len(R):
        # Compare the module in the dictionaries
        left_module = L[i]['Module']
        right_module = R[j]['Module']

        if left_module < right_module:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    # Append the remaining elements from both lists
    result.extend(L[i:])
    result.extend(R[j:])
    return result

def merge_sort_by_date(data):
    def split_date(date_str):
        try:
            date= date_str.split('/')
            if len(date) == 3:
                day,month,year = map(int, date)
                return datetime(year, month, day)
            else:
                return datetime(1900, 1, 1)
        except ValueError:
            return datetime(1900,1,1)
    def merge(L,R):
        result = []
        i,j = 0,0
        while i < len(L) and  j < len(R):
            left_date = split_date(L[i]['Activity Dates (Individual)'])
            right_date = split_date(R[j]['Activity Dates (Individual)'])

            if left_date < right_date:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        result.extend(L[i:])
        result.extend(R[j:])
        return result
    
    if len(data) <= 1:
        return data
    
    mid = len(data)//2
    left_half = data[:mid]
    right_half = data[mid:]

    left_half = merge_sort_by_date(left_half)
    right_half = merge_sort_by_date(right_half)

    return merge(left_half, right_half)

def main():
    folder_path = input("Enter folder path: ")
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
         excel_dict_list = load_folder(folder_path)
         #print(excel_dict_list)
         sorted = merge_sort_by_date(excel_dict_list)
         for item in sorted:
             print(item)

         
    

if __name__ == "__main__":
    main()