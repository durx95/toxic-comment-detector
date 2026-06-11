import pandas as pd
import os


class DataIngestion:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def load_data(self) -> pd.DataFrame:
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        try:
            df = pd.read_csv(self.input_path)
            return df
        except Exception as e:
            raise RuntimeError(f"Error loading data: {e}")

    def basic_cleaning(self, df: pd.DataFrame) -> pd.DataFrame:
        # Null comments हटाओ
        if "comment_text" not in df.columns:
            raise KeyError("Column 'comment_text' not found in dataset")

        df = df.dropna(subset=["comment_text"])

        # Toxicity columns को combine करो
        toxicity_cols = [
            "toxic", "severe_toxic", "obscene",
            "threat", "insult", "identity_hate"
        ]

        missing_cols = [col for col in toxicity_cols if col not in df.columns]
        if missing_cols:
            raise KeyError(f"Missing toxicity columns: {missing_cols}")

        df["label"] = df[toxicity_cols].max(axis=1)

        return df[["comment_text", "label"]]

    def save_data(self, df: pd.DataFrame):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        try:
            df.to_csv(self.output_path, index=False)
            print(f"Data saved successfully at {self.output_path}")
        except Exception as e:
            raise RuntimeError(f"Error saving data: {e}")

    def run(self):
        df = self.load_data()
        df = self.basic_cleaning(df)
        self.save_data(df)


if __name__ == "__main__":
    ingestion = DataIngestion(
        input_path="data/raw/train.csv",
        output_path="data/processed/cleaned_data.csv"
    )
    ingestion.run()
