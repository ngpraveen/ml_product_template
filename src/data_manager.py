import pandas as pd
from pathlib import Path
from config.core import DATADIR, config
from data.download_data import get_data

download_new_data = config.download_new_data
train_data_file_name = config.train_file_name

def load_data():#DATADIR, train_data_file_name):
    file_full_path = Path.joinpath(DATADIR, train_data_file_name)


    if download_new_data:
        get_data(DATADIR, train_data_file_name)


    df = pd.read_csv(file_full_path)
    return df

