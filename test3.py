import pandas as pd

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

def main():
    file_path = input("Enter file path: ")
    df = pd.read_csv(file_path)
    
    df['Module'] = df['Name'].apply(extract_module_data)
    df['Session'] = df['Name'].apply(extract_session_data)
    
    df = remove_column(df)

    print(df)

if __name__ == "__main__":
    main()