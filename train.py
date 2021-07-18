from config.core import DATADIR, config
from sklearn.model_selection import train_test_split
#from data.download_data import get_data
from src.data_manager import load_data
from src.pipeline import pipe

#download_new_data = config.download_new_data
#train_data_file_name = config.train_file_name

# If this var is set True in config.yml file, download data
# Else, existing data file will be used for training
#if download_new_data:
#    get_data(DATADIR, train_data_file_name)

# load data from local file
data = load_data()#DATADIR, train_data_file_name)

X_train, X_test, y_train, y_test = train_test_split(data[config.features], data[config.target], 
        test_size=config.test_size,
        random_state = config.random_state)

print(y_test.values)
pipe.fit(X_train, y_train)
print(pipe.predict(X_test))
