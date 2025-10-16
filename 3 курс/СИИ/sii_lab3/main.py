import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('Student_Performance.csv')

data = data.fillna(data.mean(numeric_only=True))
data['Extracurricular Activities'] = data['Extracurricular Activities'].fillna('No').map({'Yes': 1, 'No': 0})

for column in ['Hours Studied', 'Previous Scores', 'Sleep Hours', 'Sample Question Papers Practiced']:
    data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())

X = data.drop('Performance Index', axis=1)
y = data['Performance Index']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def fit_linear_regression(X, y):
    X = np.c_[np.ones(X.shape[0]), X]  # добавляем столбец единиц
    w = np.linalg.inv(X.T @ X) @ X.T @ y
    return w

X_train['Interaction'] = X_train['Hours Studied'] * X_train['Previous Scores']
X_test['Interaction'] = X_test['Hours Studied'] * X_test['Previous Scores']

feature_sets = [
    ['Hours Studied', 'Previous Scores'],
    ['Hours Studied', 'Sleep Hours', 'Sample Question Papers Practiced'],
    ['Previous Scores', 'Extracurricular Activities', 'Interaction']  # с синтетическим признаком
]

models = []
for features in feature_sets:
    X_train_subset = X_train[features]
    w = fit_linear_regression(X_train_subset.values, y_train.values)
    models.append((features, w))

def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / ss_tot

for features, w in models:
    X_test_subset = X_test[features].values
    X_test_subset = np.c_[np.ones(X_test_subset.shape[0]), X_test_subset]
    y_pred = X_test_subset @ w
    r2 = r2_score(y_test.values, y_pred)
    print(f"Модель с признаками {features}: R² = {r2:.4f}")

stats = data.describe()
print(stats)
