# Load data and train/test a Naïve Bayes Classifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Encode 'Gender' to numeric
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Select features and target
X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
y = df['Gender']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=45)

# Train Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc * 100:.2f}%")
