from src.data.preprocessing import DataPreprocessing
from src.features.vectorizer import TextVectorizer
from src.models.train_model import ModelTrainer

# Step 1: Preprocessing
processor = DataPreprocessing("data/processed/cleaned_data.csv")
X_train, X_test, y_train, y_test = processor.run()

# Step 2: Vectorization
vectorizer = TextVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
vectorizer.save_vectorizer()

# Step 3: Model Training
trainer = ModelTrainer()
trainer.train(X_train_vec, y_train)

accuracy, report = trainer.evaluate(X_test_vec, y_test)

print("Accuracy:", accuracy)
print(report)

trainer.save_model()