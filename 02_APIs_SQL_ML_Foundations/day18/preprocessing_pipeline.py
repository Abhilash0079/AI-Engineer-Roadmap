import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Sample dataset with numerical and categorical features
data = {
    "Age": [25, 35, None, 45, 30, 40, 28, 50],
    "Salary": [30000, None, 60000, 50000, 45000, 70000, 35000, 80000],
    "City": ["Delhi", "Mumbai", "Delhi", None, "Mumbai", "Delhi", "Kolkata", "Mumbai"],
    "Purchased": [0, 1, 1, 0, 1, 1, 0, 1],
}

df = pd.DataFrame(data)

X = df.drop(columns=['Purchased'])
y = df['Purchased']

numerical_features = ["Age", "Salary"]
categorical_features = ["City"]

# Numerical preprocessing: fill missing values, then scale
numeric_pipeline = Pipeline(
    steps= [
        ("imputer", SimpleImputer(strategy='median')),
        ("scaler", StandardScaler()),
    ]
)

# Categorical preprocessing: fill missing values, then encode
categorical_pipeline = Pipeline(
    steps= [
        ("imputer", SimpleImputer(strategy='most_frequent')),
        ("encode", OneHotEncoder(handle_unknown='ignore')),
    ]
)

# Apply the appropriate pipeline to each column group
preprocessor = ColumnTransformer(
    transformers= [
        ("numeric", numeric_pipeline, numerical_features),
        ("categorical", categorical_pipeline, categorical_features),
    ]
)

# Fit and transform the sample data for this first demonstration
X_processed = preprocessor.fit_transform(X)

print("Original dataset shape:", X.shape)
print("Processed dataset shape:", X_processed.shape)
print("\nOriginal data:")
print(X)
print("\nProcessed data:")
print(X_processed)
print("\nTarget values:")
print(y.tolist())