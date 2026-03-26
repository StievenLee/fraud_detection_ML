from sklearn.base import BaseEstimator, TransformerMixin

class BalanceDiffTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X["balanceDiffOrig"] = X["oldbalanceOrg"] - X["newbalanceOrig"]
        X["balanceDiffDest"] = X["newbalanceDest"] - X["oldbalanceDest"]
        return X