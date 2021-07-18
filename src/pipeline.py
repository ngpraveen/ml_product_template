from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from config.core import config
from src.features import multiplyByValue

pipe = Pipeline([
    ("multiply_variable", multiplyByValue(config.multiply_variables, config.multiply_value)),
    ('scaler', MinMaxScaler()),
    ('model', RandomForestClassifier(random_state=config.random_state))
    ])

