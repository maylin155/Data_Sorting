import pandas as pd

def remove_column(df):
    return df.drop(['Name'], axis=1)

def splitData(txt, splitstr):
    x = txt.split(splitstr)
    return x

def create_module_row(df):
    pass

def create_session_row(df):
    pass

def main():
    file_path = input("Enter file path: ")
    df = pd.read_csv(file_path)
    df = remove_column(df)
    print(df)

if __name__ == "__main__":
    main()