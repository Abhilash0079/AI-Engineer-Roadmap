# Day 22: Tensors and Neural Networks — Interview Notes

## 1. What is a tensor?
A tensor is a data structure used to store numerical values in PyTorch. It can represent a scalar, vector, matrix, or higher-dimensional array.

## 2. What are tensor shape and rank?
- **Shape:** The size along each dimension.
- **Rank (`ndim`):** The number of dimensions.

For example, a tensor with shape `(2, 3)` has rank 2.

## 3. What is the difference between element-wise multiplication and matrix multiplication?
- Element-wise multiplication multiplies corresponding elements of two compatible tensors.
- Matrix multiplication combines rows of the first matrix with columns of the second matrix.

## 4. What is a neural network?
A neural network is a model made of connected computational units arranged in layers. It learns patterns by adjusting trainable parameters.

## 5. What are weights and biases?
Weights control how input values contribute to a layer's output. Biases provide an additional trainable term.

## 6. What is an activation function?
An activation function transforms a neuron's output. Nonlinear activation functions, such as ReLU, allow neural networks to learn nonlinear relationships.

## 7. What is ReLU?
ReLU, or Rectified Linear Unit, returns zero for negative inputs and returns the input unchanged for positive inputs.

## 8. What is a forward pass?
A forward pass sends input data through the network to generate predictions.

## 9. What is a loss function?
A loss function measures how different model predictions are from the target values.

## 10. What is mean squared error (MSE)?
MSE calculates the average of the squared differences between predicted and target values. It is commonly used for regression tasks.

## 11. What is backpropagation?
Backpropagation calculates gradients of the loss with respect to trainable parameters using the chain rule.

## 12. What does `loss.backward()` do?
It calculates gradients for parameters involved in the computation graph. Gradients accumulate until they are cleared.

## 13. What does `optimizer.zero_grad()` do?
It clears existing gradients so that gradients from a previous training iteration do not unintentionally accumulate.

## 14. What does `optimizer.step()` do?
It updates the optimizer-managed model parameters using the calculated gradients.

## 15. What is an epoch?
An epoch is one complete pass through the training dataset.

## 16. What is a learning rate?
The learning rate controls the size of parameter updates during optimization. If it is too high, training may become unstable; if too low, learning may be slow.

## 17. What is the purpose of `model.eval()`?
It switches the model into evaluation mode, changing the behavior of layers such as dropout and batch normalization.

## 18. What does `torch.no_grad()` do?
It disables gradient tracking within its context, which can reduce memory usage during inference.

## 19. Why use `nn.Linear(2, 3)`?
It creates a fully connected layer that accepts two input features and produces three output features.

## 20. Why can neural network predictions vary between runs?
Parameters are often initialized randomly, and results can depend on initialization, training settings, and other sources of nondeterminism.

## Practical Summary
A basic PyTorch training loop typically:
1. Clears old gradients.
2. Runs a forward pass.
3. Calculates loss.
4. Calls `loss.backward()`.
5. Calls `optimizer.step()`.

During inference, evaluation mode and disabled gradient tracking serve different purposes and are often used together.
