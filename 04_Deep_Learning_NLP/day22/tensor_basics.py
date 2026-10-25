import torch


# 0D tensor: scalar
scalar = torch.tensor(5)

# 1D tensor: vector
vector = torch.tensor([1, 2, 3])

# 2D tensor: matrix
matrix = torch.tensor([
    [1, 2],
    [3, 4],
])

# 3D tensor: stack of matrices
tensor_3d = torch.tensor([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
])


def inspect_tensor(name, tensor):
    print(f"\n{name}:")
    print(tensor)
    print("Shape:", tensor.shape)
    print("Dimensions (rank):", tensor.ndim)
    print("Data type:", tensor.dtype)


inspect_tensor("Scalar", scalar)
inspect_tensor("Vector", vector)
inspect_tensor("Matrix", matrix)
inspect_tensor("3D Tensor", tensor_3d)