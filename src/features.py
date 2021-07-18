from sklearn.base import BaseEstimator, TransformerMixin

class multiplyByValue(BaseEstimator, TransformerMixin):
    """ """
    def __init__(self, variables, multiply_value):
        self.variables = variables
        self.multiply_value = multiply_value


    def fit(self, X, y):
        return self

    def transform(self, X):
        for var in self.variables:
            X[var] = X[var] * self.multiply_value
        return X
