import numpy as np

scores = np.array([80, 90, 75, 95, 85])

print("Scores:", scores)
print("Array type:", type(scores))
print("Data type:", scores.dtype)
print("Number of dimensions:", scores.ndim)
print("Array shape:", scores.shape)
print("Number of elements:", scores.size)

print("\n--------- Array Operations ------------")
print("Scores + 5", scores + 5)
print("Scores - 5", scores - 5)
print("Scores * 2", scores * 2)
print("Scores / 10", scores / 10)

print("Total score:", np.sum(scores))
print("Average score:", np.mean(scores))
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))

print("\n--- Indexing and Slicing ---")
print("First score:", scores[0])
print("Third score:", scores[2])
print("Last score:", scores[-1])
print("First three scores:", scores[:3])
print("Scores from index 1 to 3:", scores[1:4])

print("\n--- Boolean Filtering ---")
print("Scores above 80:", scores[scores > 80])
print("Scores below 85:", scores[scores < 85])
print("Scores of at least 90:", scores[scores >= 90])

print("\n--- Two-Dimensional Arrays ---")

marks = np.array([
    [80, 90, 85],
    [70, 75, 95],
    [88, 92, 90]
])

print("Marks:")
print(marks)

print("Shape:", marks.shape)
print("Dimensions:", marks.ndim)
print("First student's marks:", marks[0])
print("Second subject marks:", marks[:, 1])

print("\n--- Student Averages ---")

student_averages = np.mean(marks, axis=1)
print("Student averages:", student_averages)
print("Highest student average:", np.max(student_averages))
print("Lowest student average:", np.min(student_averages))