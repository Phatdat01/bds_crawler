import os
import pandas as pd


def store_data(data: pd.DataFrame, link: str, name: str):
    data.to_csv(f"{link}/{name}.csv", mode='a', header=True, index=False, encoding='utf-16')