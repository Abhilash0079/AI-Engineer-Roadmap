import pandas as pd

students_with_missing = {
    "Name": ["Amit", "Priya", "Rahul", "Neha"],
    "Age": [20, 21, None, 20],
    "Score": [85, None, 78, 88]
}

df_missing = pd.DataFrame(students_with_missing)

print("\n--- Handling Missing Values ---")

print("DataFrame with missing values:")
print(df_missing)

print("\nMissing values in each column:")
print(df_missing.isnull().sum())

print("\nTotal missing values:")
print(df_missing.isnull().sum().sum())

print("\n--- Removing Rows with Missing Values ---")

df_dropped = df_missing.dropna()
print(df_dropped)

print("\nRows remaining after dropna():")
print(len(df_dropped))

print("\n--- Filling Missing Values ---")

df_filled = df_missing.copy()

df_filled["Age"] = df_filled["Age"].fillna(
    df_filled["Age"].mean().round(2)
)

df_filled["Score"] = df_filled["Score"].fillna(
    df_filled["Score"].mean().round(2)
)

print(df_filled)

print("\nMissing values after filling:")
print(df_filled.isnull().sum())

print("\n--- Inspecting a DataFrame ---")

print("\nFirst two rows:")
print(df_missing.head(2))

print("\nDataFrame information:")
df_missing.info()

print("\nStatistical summary:")
print(df_missing.describe())

print("\nColumn data types:")
print(df_missing.dtypes)