from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Actual labels: 0 - legitimate, 1 - spam
y_true = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

# Predicted labels by classifier
y_pred = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]

# Calculate classification metrices
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1_score = f1_score(y_true, y_pred)

# Confusion matrix: rows = actual, columns = predicted
matrix = confusion_matrix(y_true, y_pred)

print("Classification Evaluation")
print("-" * 30)
print("Confusion Matrix:")
print(matrix)
print(f"Accuracy:  {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall:    {recall:.2%}")
print(f"F1-score:  {f1_score:.2%}")