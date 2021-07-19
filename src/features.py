from sklearn.base import BaseEstimator, TransformerMixin


class multiplyByValue(BaseEstimator, TransformerMixin):
    """ A custom transformer usable within pipeline. \
        This particular one is for demo purpose only - \
        it doesn't have any consequence. In this case \
        this transformer only multiplies features \
        (listed in yml file) by a constant (also specified \
        in yml file). More similar transformer classes can \
        be added."""

    def __init__(self, variables, multiply_value):
        self.variables = variables
        self.multiply_value = multiply_value

    def fit(self, X, y):
        return self

    def transform(self, X):
        for var in self.variables:
            X[var] = X[var] * self.multiply_value
        return X
