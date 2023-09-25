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

folder_path = input("Enter the folder path where raw data is located: ")
if os.path.exists(folder_path):
    df = pd.read_csv(folder_path)

    # Initialize dictionaries to store module and session instances
    Module_variables = {}
    Session_variables = {}

    
    # Iterate over the DataFrame
    for i in range(len(df)):
        value = df.loc[i, 'Name']
        split_value = splitData(value, "_")

        # Create and store Module instances
        Module_variables["module{0}".format(i)] = Module(split_value[3])
        sessionList = splitData(split_value[4],"/")

        # Create and store Session instances
        Session_variables["session{0}".format(i)] = Session(sessionList[0])
    
    #print(Module_variables)
    #print(Session_variables)
    

    #df = df.drop(columns=['Name'])
    # Iterate over Module and Session dictionaries to access their attributes




    dict = df.to_dict(orient ='index')
    #print(dict)

    #Key to remove from each inner dictionary
    key = 'Name'

    #Iterate through outer dictionary
    for index, value in dict.items():
        #Remove the key if it exists in inner dictionary
        if key in value:
            value.pop(key)
    
    for x in Module_variables.values():
        #Get key, value pairs to add to inner dictionary.
        new_key = 'Module'  
        new_module = x.name

        #Iterate through outer dictionary
        for index, value in dict.items():
            #Adding the new key-value pair
            value[new_key] = new_module

    for y in Session_variables.values():
        #Get key, value pairs to add to inner dictionary. 
        new_key = 'Session'
        new_session = y.name

        #Iterate through outer dictionary
        for index, value in dict.items():
            #Adding the new key-value pair
            value[new_key] = new_module
    
    print(dict)
