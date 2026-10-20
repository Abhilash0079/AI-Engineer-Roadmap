"""
A Series represents one-dimensional data. A DataFrame represents tabular data with rows and columns, similar to an Excel spreadsheet.
"""
import pandas as pd

print("\n--- Creating a DataFrame ---")

students = {
    "Name": ["Amit", "Priya", "Rahul", "Neha"],
    "Age": [20, 21, 19, 20],
    "Score": [85, 92, 78, 88]
}

df = pd.DataFrame(students)

print("Student records:")
print(df)

print("\nDataFrame type:")
print(type(df))

print("\nDataFrame shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nNumber of rows:")
print(len(df))

print("\n--- Selecting Columns ---")

print("Student names:")
print(df["Name"])

print("\nStudent scores:")
print(df["Score"])

print("\nNames and scores:")
print(df[["Name", "Score"]])

print("\n--- Selecting Rows ---")

print("First student:")
print(df.iloc[0])

print("\nFirst two students:")
print(df.iloc[:2])

print("\nSecond student's name:")
print(df.iloc[1]["Name"])

print("\n---- Filtering  DataFrame Records ------")
high_scores = df[df['Score']>=85]

print("Student scoring 85 or above:")
print(high_scores)

print("\nStudents aged 20 or above")
print(df[df['Age']>=20])

print("\nStudents scoring 85 or above and aged 20 or above:")
print(df[(df['Score']>=85) & (df['Age']>=20)])