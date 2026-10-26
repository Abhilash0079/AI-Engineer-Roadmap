import copy
import torch
from torch import nn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset

def prepare_data():
    """Load, split, scale, and batch the real dataset."""
    dataset = load_diabetes()
    X = dataset.data
    y = dataset.target.reshape(-1, 1)

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.30, random_state=42
    )

    X_validation, X_test, y_validation, y_test = train_test_split(
        X_temp, y_temp, test_size=0.50, random_state=42
    )

    # Fit preprocessing only on training data.
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_validation = scaler.transform(X_validation)
    X_test = scaler.transform(X_test)

    X_train = torch.tensor(X_train, dtype=torch.float32)
    X_validation = torch.tensor(X_validation, dtype=torch.float32)
    X_test = torch.tensor(X_test, dtype=torch.float32)

    y_train = torch.tensor(y_train, dtype=torch.float32)
    y_validation = torch.tensor(y_validation, dtype=torch.float32)
    y_test = torch.tensor(y_test, dtype=torch.float32)

    train_loader = DataLoader(
        TensorDataset(X_train, y_train),
        batch_size=32,
        shuffle=True,
    )
    validation_loader = DataLoader(
        TensorDataset(X_validation, y_validation),
        batch_size=32,
        shuffle=False,
    )
    test_loader = DataLoader(
        TensorDataset(X_test, y_test),
        batch_size=32,
        shuffle=False,
    )

    return train_loader, validation_loader, test_loader


def evaluate_model(model, data_loader, loss_function):
    """Return sample-weighted loss and regression MAE."""
    model.eval()
    total_squared_error = 0.0
    total_absolute_error = 0.0
    total_samples = 0

    with torch.no_grad():
        for features, targets in data_loader:
            predictions = model(features)
            loss = loss_function(predictions, targets)
            batch_size = targets.size(0)

            total_squared_error += loss.item() * batch_size
            total_absolute_error += (
                torch.abs(predictions - targets).sum().item()
            )
            total_samples += batch_size

    average_mse = total_squared_error / total_samples
    average_mae = total_absolute_error / total_samples

    return average_mse, average_mae


def main():
    torch.manual_seed(42)

    train_loader, validation_loader, test_loader = prepare_data()

    model = nn.Sequential(
        nn.Linear(10, 32),
        nn.ReLU(),
        nn.Linear(32, 16),
        nn.ReLU(),
        nn.Linear(16, 1),
    )

    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    best_validation_loss = float("inf")
    best_model_state = None
    patience = 10
    epochs_without_improvement = 0
    max_epochs = 100

    for epoch in range(max_epochs):
        model.train()
        total_training_loss = 0.0
        training_samples = 0

        for features, targets in train_loader:
            predictions = model(features)
            loss = loss_function(predictions, targets)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            batch_size = targets.size(0)
            total_training_loss += loss.item() * batch_size
            training_samples += batch_size

        training_loss = total_training_loss / training_samples
        validation_loss, validation_mae = evaluate_model(
            model, validation_loader, loss_function
        )

        print(
            f"Epoch {epoch + 1:03d} | "
            f"Train MSE: {training_loss:.2f} | "
            f"Validation MSE: {validation_loss:.2f} | "
            f"Validation MAE: {validation_mae:.2f}"
        )

        if validation_loss < best_validation_loss:
            best_validation_loss = validation_loss
            best_model_state = copy.deepcopy(model.state_dict())
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1

        if epochs_without_improvement >= patience:
            print("Early stopping triggered.")
            break

    model.load_state_dict(best_model_state)

    test_mse, test_mae = evaluate_model(
        model, test_loader, loss_function
    )

    print("\nFinal test results")
    print(f"Test MSE: {test_mse:.2f}")
    print(f"Test RMSE: {test_mse ** 0.5:.2f}")
    print(f"Test MAE: {test_mae:.2f}")


if __name__ == "__main__":
    main()
