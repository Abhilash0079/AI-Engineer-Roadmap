import pandas as pd

"""
A Series is a one-dimensional data structure containing values and an index. Think of it as a single column in a spreadsheet.
"""

scores = pd.Series([80, 90, 75, 95, 85])
print("Student Scores:")
print(scores)

print("\nSeries data type:")
print(type(scores))

print("\nValues:")
print(scores.values)

print("\nIndex:")
print(scores.index)

print("\nNumber of elements:")
print(scores.size)

print("\nAverage score:")
print(scores.mean())

print("\n--- Accessing Series Values ---")

print("First score:", scores.iloc[0])
print("Third score:", scores.iloc[2])
print("Last score:", scores.iloc[-1])

print("\n--- Slicing Series ---")

print("First three scores:")
print(scores.iloc[:3])

print("\nScores at positions 1 to 3:")
print(scores.iloc[1:4])

print("\n--- Boolean Filtering ---")

passing_scores = scores[scores >= 80]

print("Scores greater than or equal to 80:")
print(passing_scores)

print("\nNumber of passing scores:")
print(len(passing_scores))

print("\nScores below 80:")
print(scores[scores < 80])

