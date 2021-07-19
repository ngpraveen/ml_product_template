import pandas as pd
from pathlib import Path
from config.core import DATADIR, ROOT, config
from data.download_data import get_data
import joblib

download_new_data = config.download_new_data
train_data_file_name = config.train_file_name

file_full_dir = ROOT / config.pipeline_save_dir
file_full_path = file_full_dir / config.pipeline_save_file


def load_data():
    file_full_path = Path.joinpath(DATADIR, train_data_file_name)

    if download_new_data:
        get_data(DATADIR, train_data_file_name)

    df = pd.read_csv(file_full_path)
    return df


def save_pipeline(pipe_name):
    if not file_full_dir.is_dir():
        print(f"The output directory {file_full_dir} \
                does not exist. Creating it.")
        file_full_dir.mkdir(exist_ok=True)
    joblib.dump(pipe_name, file_full_path)


def load_pipeline():
    pipe = joblib.load(file_full_path)
    return pipe
