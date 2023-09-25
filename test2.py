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
    for i in range(len(df)):
        value = df.loc[i, 'Name']
        split_value = splitData(value, "_")
        module = Module(split_value[3])
        sessionList = splitData(split_value[4],"/")
        session = Session(sessionList[0])
        print(module.name)
        print(session.name)
        i += 1
