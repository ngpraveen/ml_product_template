from pathlib import Path
from typing import List
from pydantic import BaseModel
from strictyaml import load
import src

ROOT = Path(src.__file__).parent.parent
DATADIR = ROOT / "data"
CONFIG_FILE = ROOT / "config/config.yml"

class Config(BaseModel):
    download_new_data : bool
    train_file_name : str
    features: List[str]
    target: str
    random_state: int
    test_size: float


def read_config():
    """Reads config file (yml) and returns it as text (str)"""

    if CONFIG_FILE.is_file():
        with open(CONFIG_FILE, "r") as f:
            config_txt = f.read()
        return config_txt
    else:
        raise Exception(f"yml file is not found at {CONFIG_FILE}!")


def create_config():
    """Creates and validates Config object based on config file"""
    config_txt = read_config()
    config_yml = load(config_txt)
    config_ = Config(**config_yml.data)
    return config_

config = create_config()

