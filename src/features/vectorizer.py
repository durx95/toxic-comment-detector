import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


class TextVectorizer:
    def __init__(self, max_features=5000, ngram_range=(1, 2)):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=ngram_range
        )

    def fit_transform(self, X_train):
        X_train_vec = self.vectorizer.fit_transform(X_train)
        return X_train_vec

    def transform(self, X_test):
        X_test_vec = self.vectorizer.transform(X_test)
        return X_test_vec

    def save_vectorizer(self, path="artifacts/vectorizer.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self.vectorizer, f)