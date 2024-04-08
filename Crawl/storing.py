import os
import re
import pandas as pd

def create_folder(path: str) -> bool:
    try:
        lst_of_path = re.split(r'[\\/]', path)
        path=""
        for folder in lst_of_path:
            if folder == "":
                path += "//"
            else:
                path+=f"{folder}/"
            if not os.path.exists(path):
                os.makedirs(path)
        return True
    except:
        return False

def store_data(data: pd.DataFrame, path: str, file_name: str):
    if create_folder(path=path):
        if os.path.exists(f"{path}/{file_name}.csv"):
            data.to_csv(f"{path}/{file_name}.csv", mode='a', header=False, index=False, encoding='utf-16')        
        else:
            data.to_csv(f"{path}/{file_name}.csv", mode='a', header=True, index=False, encoding='utf-16')          