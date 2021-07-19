from src.data_manager import load_pipeline, load_data
from config.core import config
TARGET = config.target

pipe = load_pipeline()
data = load_data()
print(pipe.predict(data.drop(TARGET, axis=1).sample(2)))
