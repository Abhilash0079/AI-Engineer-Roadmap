import torch

# Create two tensors
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# Element-wise operations
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# Sum and mean
print("Sum of a:", torch.sum(a))
print("Mean of a:", torch.mean(a))

# Matrix Multiplication
x = torch.tensor([
    [1.0, 2.0],
    [3.0, 4.0]
])

y = torch.tensor([
    [5.0, 6.0],
    [7.0, 8.0]
])

print("Matrix Multiplication:")
print(torch.matmul(x, y))