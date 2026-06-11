import pickle

class PredictionService:
    def __init__(self):
        with open("artifacts/vectorizer.pkl", "rb") as f:
            self.vectorizer = pickle.load(f)

        with open("artifacts/model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, text: str):
        text_vec = self.vectorizer.transform([text])
        prediction = self.model.predict(text_vec)[0]
        return int(prediction)