import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

data = {
    'amount': [100, 200, 300, 150, 120, 350, 400, 110, 90, 250],
    'currency': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  
    'card_number': [1234567890123456, 2345678901234567, 3456789012345678, 4567890123456789, 5678901234567890,
                    6789012345678901, 7890123456789012, 8901234567890123, 9012345678901234, 1234567890123456],
    'fraud': [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[['amount', 'currency', 'card_number']]
y = df['fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

with open("models/fraud_detection_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)