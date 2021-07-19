from config.core import DATADIR, config
from sklearn.model_selection import train_test_split
from src.data_manager import load_data, save_pipeline
from src.pipeline import pipe


# load data from local file
data = load_data()


X_train, X_test, y_train, y_test = train_test_split(data[config.features], data[config.target], 
        test_size=config.test_size,
        random_state = config.random_state)

print(y_test.values)
pipe.fit(X_train, y_train)
print(pipe.predict(X_test))
save_pipeline(pipe)
