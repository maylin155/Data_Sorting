import pandas as pd
import os

class Dataset:
    
    #Function to extra module data from "Name" session
    def extract_module_data(self,name):
            split_value = name.split("_")
            if len(split_value) >= 4:
                return split_value[3]
            else:
                return None
            
    #Function to extract session data from "Name" session
    def extract_session_data(self,name):
        split_value = name.split("_")
        session_list = split_value[4].split("/")
        if len(session_list) >= 1:
            return session_list[0]
        else:
            return None

    #Loading all the files in raw dataset.
    def load_folder(self) -> list:
        self.folder_path = input("Enter folder path: ")
        excel_dict_list = []

        # List all files in the folder
        file_list = [f for f in os.listdir(self.folder_path) if f.endswith('.csv')]

        for file_name in file_list:
            file_path = os.path.join(self.folder_path, file_name)

            try:
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)

                #Extract Module and Session data from name column and create new.
                df['Module'] = df['Name'].apply(self.extract_module_data)
                df['Session'] = df['Name'].apply(self.extract_session_data)

                
                #Remove columns "Planned Size"
                df = df.drop(columns=['Planned Size'])
                df = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)

                # Convert the DataFrame to a list of dictionaries
                dict_list = df.to_dict(orient='records')


                # Extend the excel_dict_list with data from the current file
                excel_dict_list.extend(dict_list)

            except Exception as e:
                print(f"Error processing file {file_name}: {str(e)}")

        return excel_dict_list
    
    def displayDF(self,list):
        df = pd.DataFrame.from_records(list)
        print(df)

