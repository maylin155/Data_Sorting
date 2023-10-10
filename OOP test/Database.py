from datetime import datetime
import pandas as pd
from Dataset import *
from tabulate import tabulate
import textwrap
class Database(Dataset):

    def __init__(self):
        super().__init__()
        self.database = []

    #Store the data as a list after loading the file
    def store_data(self,data):
        self.database = data

    def get_database(self):
        return self.database
    
    def display_database(self):
        # df = pd.DataFrame.from_records(self.database)
        # data_list = df.to_dict(orient="records")
        # headers = df.columns.tolist()
        print(tabulate(self.database, headers="keys", showindex="always" ,tablefmt="psql"))

    def wrap_text(self, width=20):
        wrapped_data_list = []
        for data_dict in self.database:
            wrapped_data_dict = {}
            for key, value in data_dict.items():
                wrapped_value = "\n".join(textwrap.wrap(value, width=width))
                wrapped_data_dict[key] = wrapped_value
            wrapped_data_list.append(wrapped_data_dict)
        self.database = wrapped_data_list  # Replace the database with wrapped data


    #Using merge sort algorithm to sort the data by module
    def merge_sort_by_module(self,data, ascending=True):
        if len(data) <= 1:
            return data

        # Find the mid of the list
        mid = len(data) // 2
        #Dividing 
        L = data[:mid]
        R = data[mid:]

        # Recursively sort each half
        L = self.merge_sort_by_module(L)
        R = self.merge_sort_by_module(R)

        result = []
        i, j = 0, 0

        while i < len(L) and j < len(R):
            # Compare the module in the dictionaries
            left_module = L[i]['Module']
            right_module = R[j]['Module']

            if ascending:
                if left_module <= right_module:
                    result.append(L[i])
                    i += 1
                else:
                    result.append(R[j])
                    j += 1
            else:
                if left_module >= right_module:
                    result.append(L[i])
                    i += 1
                else:
                    result.append(R[j])
                    j += 1


        # Append the remaining elements from both lists
        result.extend(L[i:])
        result.extend(R[j:])
        return result

    #Using merge sort algorithm to sort the data by date
    def merge_sort_by_date(self,data, ascending=True):
        #Split date from dictionary to year,month and day
        def split_date(date_str):
            try:
                date= date_str.split('/')
                if len(date) == 3:
                    day,month,year = map(int, date)
                    return datetime(year, month, day)
                else:
                    return datetime(1900, 1, 1) #A default date for invalid format.
            except ValueError:
                return datetime(1900,1,1)
        def merge(L,R):
            result = []
            i,j = 0,0
            while i < len(L) and  j < len(R):
                left_date = split_date(L[i]['Activity Dates (Individual)'])
                right_date = split_date(R[j]['Activity Dates (Individual)'])

                #Ascending or Descending order
                if ascending:
                    if left_date <= right_date:
                        result.append(L[i])
                        i += 1
                    else:
                        result.append(R[j])
                        j += 1
                else:
                    if left_date >= right_date:
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
        
        #Find the mid of the list
        mid = len(data)//2

        #Divide the list into half
        left_half = data[:mid]
        right_half = data[mid:]

        #Recursively sort each half
        left_half = self.merge_sort_by_date(left_half)
        right_half = self.merge_sort_by_date(right_half)

        return merge(left_half, right_half)
    

    #Searching by key and value
    def search_by_value(self,data,key_to_search, value_to_find):
        result = [item for item in data if key_to_search in item and item[key_to_search] == value_to_find]
        return result
    
    #Searching by start time and end time
    def search_by_start_end_time(self, data, start_time, end_time):
        found_dicts = []
        for item in data:
            if "Scheduled Start Time" in item and "Scheduled End Time" in item:
                item_start_time = item["Scheduled Start Time"]
                item_end_time = item["Scheduled End Time"]
                if start_time <= item_start_time <= end_time or start_time <= item_end_time <= end_time:
                    found_dicts.append(item)
        return found_dicts
    
    #Search by Specific Time
    def search_by_specific_time(self, data, specific_time):
        key_to_search_start = "Scheduled Start Time"
        key_to_search_end = "Scheduled End Time"

        # Use the search_by_value function to find dictionaries with the specified time in both keys
        start_time_results = self.search_by_value(data, key_to_search_start, specific_time)
        end_time_results = self.search_by_value(data, key_to_search_end, specific_time)

        # Find dictionaries that match either start or end time
        found_dicts = start_time_results + end_time_results

        return found_dicts



    