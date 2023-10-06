from datetime import datetime
import pandas as pd
from Dataset import *

class DB(Dataset):

    def __init__(self):
        super().__init__()
        self.database = []

    #Store the data as a list after loading the file
    def store_data(self,data):
        self.database = data

    def get_database(self):
        return self.database
    
    def display_database(self):
        # for item in self.database:
        #     print(item)
        df = pd.DataFrame.from_records(self.database)
        print(df)

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
    