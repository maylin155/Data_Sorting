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
    print(splitData((df['Name']),"_"))

    #if __name__== "__main__":
    txt = df['Name']
    moduleList = splitData(txt, "_")
    module = Module(moduleList[3])
    print(module.name)
    sessionList = splitData(moduleList[4],"/")
    session = Session(sessionList[0])
    print(session.name)
