
grid_f1 = 0.9795
randomized_f1 = 0.9794

difference = abs(grid_f1 - randomized_f1)

print("GridSearchCV mean F1:", grid_f1)
print("RandomizedSearchCV mean F1:", randomized_f1)
print("Absolute difference:", round(difference, 4))

if difference < 0.001:
    print("Conclusion: Both methods performed similarly in this experiment.")
else:
    print("Conclusion: The scores show a larger difference in this experiment.")
