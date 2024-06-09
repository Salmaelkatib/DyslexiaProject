import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the dataset
data_path = 'D:/Grad Projroj/Eye_Tracking_Dataset.csv'
data = pd.read_csv(data_path)

# Separate features and target
X = data.drop(columns=['Dyslexic'])
y = data['Dyslexic']

# Identify categorical columns (example: 'Gender') and numerical columns
categorical_cols = X.select_dtypes(include=['object', 'category']).columns
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns

# Define the column transformer to handle both numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ]
)

# Define the SVM classifier
svm = SVC(kernel="linear")

# Define RFE with SVM
rfe = RFE(estimator=svm, n_features_to_select=10)  # Adjust n_features_to_select as needed

# Create a pipeline that preprocesses the data, applies RFE, and then fits the SVM
pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('feature_selection', rfe),
    ('classification', svm)
])

# Define 10-fold cross-validation
cv = StratifiedKFold(n_splits=10)

# Perform cross-validation and compute accuracy
scores = cross_val_score(pipeline, X, y, cv=cv, scoring='accuracy')

# Print the accuracy for each fold and the mean accuracy
print(f'Accuracy for each fold: {scores}')
print(f'Mean accuracy: {np.mean(scores)}')
