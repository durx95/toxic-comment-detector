import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split


class DataPreprocessing:
    def __init__(self, input_path: str):
        self.input_path = input_path

    def load_data(self):
        return pd.read_csv(self.input_path)

    def clean_text(self, text: str) -> str:
        # Lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r"http\S+|www\S+", "", text)

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Remove numbers
        text = re.sub(r"\d+", "", text)

        # Remove extra spaces
        text = text.strip()

        return text

    def apply_cleaning(self, df: pd.DataFrame):
        df["cleaned_text"] = df["comment_text"].apply(self.clean_text)
        return df

    def split_data(self, df: pd.DataFrame):
        X = df["cleaned_text"]
        y = df["label"]

        return train_test_split(
            X, y, test_size=0.2, random_state=42
        )

    def run(self):
        df = self.load_data()
        df = self.apply_cleaning(df)
        X_train, X_test, y_train, y_test = self.split_data(df)

        return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    processor = DataPreprocessing("data/processed/cleaned_data.csv")
    X_train, X_test, y_train, y_test = processor.run()

    print("Preprocessing Done")
    print(f"Train size: {len(X_train)}")
    print(f"Test size: {len(X_test)}")