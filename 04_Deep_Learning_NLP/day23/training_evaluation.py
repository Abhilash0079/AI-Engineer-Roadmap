import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset, random_split

def create_dataset():
    """Create a small synthetic binary-classification dataset."""
    torch.manual_seed(42)

    negative_class = torch.randn(100,2) - 2
    positive_class = torch.randn(100,2) + 2

    features = torch.cat([negative_class, positive_class])
    labels = torch.cat([
        torch.zeros(100, 1),
        torch.ones(100, 1)
    ])

    return TensorDataset(features, labels)

def create_data_loader(dataset):
    """Split into training, validation and test sets."""
    train_size = 140
    validation_size = 30
    test_size = 30

    generator = torch.Generator().manual_seed(42)

    train_data, validation_data, test_data = random_split(
        dataset,
        [train_size, validation_size, test_size],
        generator=generator
    )

    train_loader = DataLoader(train_data, batch_size=16, shuffle=True)
    validation_loader = DataLoader(validation_data, batch_size=16, shuffle=False)
    test_loader = DataLoader(test_data, batch_size=16, shuffle=False)

    return train_loader, validation_loader, test_loader

def evaluate_model(model, data_loader, loss_function):
    """Calcualte average loss and classification accuracy."""
    model.eval()

    total_loss = 0.0
    correct_predictions = 0
    total_samples = 0

    with torch.no_grad():
        for features, labels in data_loader:
            predictions = model(features)
            loss = loss_function(predictions, labels)

            batch_size = labels.size(0)
            total_loss += loss.item() * batch_size

            predicted_class = (predictions >= 0.5).float()
            correct_predictions += (predicted_class == labels).sum().item()
            total_samples += batch_size

    average_loss = total_loss / total_samples
    accuracy = correct_predictions / total_samples
    
    return average_loss, accuracy

def main():
    dataset = create_dataset()
    train_loader, validation_loader, test_loader = create_data_loader(dataset)

    model = nn.Sequential(
        nn.Linear(2, 8),
        nn.ReLU(),
        nn.Linear(8, 1),
        nn.Sigmoid(),
    )

    loss_function = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    best_validation_loss = float("inf")
    best_model_state = None
    patience = 5
    epochs_without_improvement = 0
    max_epochs = 50

    for epoch in range(max_epochs):
        model.train()
        training_loss_total = 0.0
        training_samples = 0

        for features, labels in train_loader:
            predictions = model(features)
            loss = loss_function(predictions, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            batch_size = labels.size(0)
            training_loss_total += loss.item() * batch_size
            training_samples += batch_size

        training_loss = training_loss_total / training_samples
        validation_loss, validation_accuracy = evaluate_model(
            model, validation_loader, loss_function
        )

        print(
            f"Epoch {epoch + 1:02d} | "
            f"Train loss: {training_loss:.4f} | "
            f"Validation loss: {validation_loss:.4f} | "
            f"Validation accuracy: {validation_accuracy:.2%}"
        )

        if validation_loss < best_validation_loss:
            best_validation_loss = validation_loss
            best_model_state = {
                key: value.detach().clone()
                for key, value in model.state_dict().items()
            }
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1


        if epochs_without_improvement >= patience:
            print("Early stopping: validation loss stopped improving.")
            break

    model.load_state_dict(best_model_state)

    test_loss, test_accuracy = evaluate_model(
        model, test_loader, loss_function
    )

    print("\nFinal test results")
    print(f"Test loss: {test_loss:.4f}")
    print(f"Test accuracy: {test_accuracy:.2%}")

if __name__=="__main__":
    main()


"""
What this code demonstrates
- model.train() enables training behavior.
- model.eval() switches to evaluation behavior.
- torch.no_grad() avoids tracking gradients during evaluation.
- Validation loss tracks how well the model generalizes during training.
- Early stopping halts training after five consecutive epochs without validation-loss improvement.
- The best validation checkpoint is restored before evaluating the held-out test set.
The data is synthetic, so this is a learning exercise rather than a real-world model.
"""