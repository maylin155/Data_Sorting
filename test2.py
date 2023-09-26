import pandas as pd
import os

class Module():
    def __init__(self,name):
        self.name = name
    
class Session():
    def __init__(self,name):
        self.name = name

def splitData(txt, splitstr):
    x = txt.split(splitstr)
    return x

#Function to create module variables
def create_module_instances(df):
    module_variables = {}
    for i, row in df.iterrows():
        name = row['Name']
        split_value = splitData(name, "_")
        module_name = split_value[3]
        module_variables[f"module{i}"] = Module(module_name)
    return module_variables

#Function to create session variables 
def create_session_instances(df):
    session_variables = {}
    for i, row in df.iterrows():
        name = row['Name']
        split_value = splitData(name, "_")
        session_list = splitData(split_value[4], "/")
        session_name = session_list[0]
        session_variables[f"session{i}"] = Session(session_name)
    return session_variables

#Function to drop "Name" column and add "Module" and "Session"
def process_df(df, module_variables, session_variables):
    # Remove the 'Name' column
    df.drop(columns=['Name'], inplace=True)

    # Add Module and Session information to the DataFrame
    df['Module'] = [module_variables[f"module{i}"].name for i in range(len(df))]
    df['Session'] = [session_variables[f"session{i}"].name for i in range(len(df))]

#Iterate through the folder and add the excel files into a list.
def list_files(folder_path):
    excel_dict_list= []
    excel_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    for excel_file in excel_files:
        file_path = os.path.join(folder_path, excel_file)
        df = pd.read_csv(file_path)
        module_variables = create_module_instances(df)
        session_variables = create_session_instances(df)
        process_df(df, module_variables, session_variables)
        dict = df.to_dict(orient= 'index')
        excel_dict_list.append((excel_file, dict))
    return excel_dict_list


def main():
    folder_path = input("Enter the folder path where raw data is located: ")
    if os.path.exists(folder_path):
        excel_dict_list = list_files(folder_path)
        print(excel_dict_list[0][1][0]['Description'])

        #excel_dict_list contains dictionaries from excel files in the folder.
        #for excel_file, data in excel_dict_list:
            #print(f"Data from Excel file: {excel_file}")
            #for i, record in enumerate(data, start=1):
                #print(f"Record {i}: {record}")
            #print()

    else:
        print(f"The folder path '{folder_path}' does not exist.")

if __name__ == "__main__":
    main()

