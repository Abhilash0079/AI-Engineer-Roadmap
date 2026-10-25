import torch
import torch.nn as nn

class SimpleNeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(2,3)
        self.relu = nn.ReLU()
        self.output = nn.Linear(3,1)

    def forward(self, x):
        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x)

        return x

model = SimpleNeuralNetwork()

# Twp samples, each with two input features
inputs = torch.tensor([
    [1.0, 2.0],
    [3.0, 4.0]
])

predictions = model(inputs)

print("Model:")
print(model)

print("\nInput shape:", inputs.shape)
print("Prediction shape:", predictions.shape)
print("Predictions:")
print(predictions)