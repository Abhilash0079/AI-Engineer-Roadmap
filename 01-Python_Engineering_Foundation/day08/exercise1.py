"""
Exercise 1: Filter passing scores
Using your existing scores array, add code that:
1. Prints scores greater than or equal to 85.
2. Prints the number of scores greater than or equal to 85.
3. Calculates the average of those passing scores.
"""
import numpy as np

scores = np.array([80, 90, 75, 95, 85])

# 1. Prints scores greater than or equal to 85.
print("\n--- Passing Scores Practice ---")

passing_scores = scores[scores>=85]
print("Passing scores", passing_scores)
print("Number of passing scores:",len(passing_scores))
print("Average passing score:", np.mean(passing_scores))