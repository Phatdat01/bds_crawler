import os
import pandas as pd


def store_data(data: pd.DataFrame, link: str, file_name: str):
    if os.path.exists(f"{link}/{file_name}.csv"):
        data.to_csv(f"{link}/{file_name}.csv", mode='a', header=False, index=False, encoding='utf-16')        
    else:
        data.to_csv(f"{link}/{file_name}.csv", mode='a', header=True, index=False, encoding='utf-16')