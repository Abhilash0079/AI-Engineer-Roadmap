# Day 22: Tensors and Neural Networks

## Objective
Learn PyTorch tensor fundamentals, build a simple neural network, and understand the basic model training process.

## Environment
- Python: 3.14.3
- PyTorch: installed in the shared project virtual environment
- Device: CPU
- Project environment: `D:\AI-Engineer-Roadmap\venv`

## Topics Covered
- Tensor types: scalar, vector, matrix, and 3D tensor
- Tensor shape, rank, and data type
- Element-wise tensor arithmetic
- Sum and mean operations
- Matrix multiplication
- Neural network layers using `torch.nn.Linear`
- ReLU activation
- Forward pass and predictions
- Mean squared error (MSE) loss
- Backpropagation and gradients
- Stochastic gradient descent (SGD)
- Training and evaluation modes

## Files
- `tensor_basics.py` — Creates and inspects tensors of different dimensions.
- `tensor_operations.py` — Demonstrates arithmetic, aggregation, and matrix multiplication.
- `first_neural_network.py` — Builds a basic neural network and generates predictions.
- `train_neural_network.py` — Trains a network using MSE loss and SGD.

## How to Run

Activate the shared virtual environment from the project root:

```powershell
.\venv\Scripts\Activate.ps1
```

Navigate to the Day 22 folder:

```powershell
cd .\04_Deep_Learning_NLP\day22
```

Run the scripts:

```powershell
python tensor_basics.py
python tensor_operations.py
python first_neural_network.py
python train_neural_network.py
```

## Training Experiment

The training example uses four samples with two input features and a target relationship:

`y = 2*x1 + 3*x2`

The model is trained for 500 epochs using mean squared error and SGD with a learning rate of 0.01.

Observed results from one run:
- Loss at epoch 100: 0.2235
- Loss at epoch 200: 0.1003
- Loss at epoch 300: 0.0500
- Loss at epoch 400: 0.0246
- Loss at epoch 500: 0.0119
- Prediction for `[3.0, 2.0]`: 11.7173
- Expected value: 12.0

The exact results can vary because the model parameters are initialized automatically.

## Key Learning
A neural network learns by repeatedly generating predictions, calculating a loss, computing gradients through backpropagation, and updating its parameters with an optimizer.

## Limitations
This is a small educational example with only four training samples. It demonstrates the training workflow but is not evidence of generalization to a real-world dataset.
