import torch
import torch.nn as nn
import torch.optim as optim


# Training data: 4 samples, 2 features each
X = torch.tensor([
    [1.0, 1.0],
    [2.0, 1.0],
    [1.0, 2.0],
    [2.0, 2.0],
])

# Target values
y = torch.tensor([
    [5.0],
    [7.0],
    [8.0],
    [10.0],
])


class SimpleNeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(2, 3)
        self.relu = nn.ReLU()
        self.output = nn.Linear(3, 1)

    def forward(self, x):
        x = self.hidden(x)
        x = self.relu(x)
        return self.output(x)


model = SimpleNeuralNetwork()

# Loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
epochs = 500

for epoch in range(epochs):
    # 1. Clear old gradients
    optimizer.zero_grad()

    # 2. Forward pass
    predictions = model(X)

    # 3. Calculate loss
    loss = criterion(predictions, y)

    # 4. Backpropagation
    loss.backward()

    # 5. Update parameters
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}")

# Test the trained model
model.eval()

with torch.no_grad():
    test_input = torch.tensor([[3.0, 2.0]])
    prediction = model(test_input)

print("\nTest input:", test_input)
print("Predicted value:", prediction.item())
print("Expected value:", 12.0)