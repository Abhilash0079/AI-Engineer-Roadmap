import torch
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset

def main():
    # 1. Load the dataset
    dataset = load_diabetes()
    X = dataset.data
    y = dataset.target.reshape(-1,1)

    print("Original dataset")
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)

    # 2. Split into training, validation and test sets.
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    X_validation, X_test, y_validation, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42
    )

    # 3. Fit the scaler on the training features only.
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_validation = scaler.transform(X_validation)
    X_test = scaler.transform(X_test)

    # 4. Convert features and targets into PyTorch tensors.
    X_train = torch.tensor(X_train, dtype=torch.float32)
    X_validation = torch.tensor(X_validation, dtype=torch.float32)
    X_test = torch.tensor(X_test, dtype=torch.float32)

    y_train = torch.tensor(y_train, dtype=torch.float32)
    y_validation = torch.tensor(y_validation, dtype=torch.float32)
    y_test = torch.tensor(y_test, dtype=torch.float32)

    # 5. Create datasets.
    train_dataset = TensorDataset(X_train, y_train)
    validation_dataset = TensorDataset(X_validation, y_validation)
    test_dataset = TensorDataset(X_test, y_test)

    # 6. Create data loaders.
    train_loader = DataLoader(
        train_dataset, batch_size=32, shuffle=True
    )

    validation_loader = DataLoader(
        validation_dataset, batch_size=32, shuffle=False
    )

    test_loader = DataLoader(
        test_dataset, batch_size=32, shuffle=False
    )


    # 7. Inspect the resulting pipeline.
    print("\nSplit sizes")
    print("Training:", len(train_dataset))
    print("Validation:", len(validation_dataset))
    print("Test:", len(test_dataset))

    print("\nTensor shapes")
    print("X_train:", X_train.shape)
    print("y_train:", y_train.shape)
    print("X_validation:", X_validation.shape)
    print("y_validation:", y_validation.shape)
    print("X_test:", X_test.shape)
    print("y_test:", y_test.shape)

    print("\nBatch verification")
    batch_features, batch_targets = next(iter(train_loader))
    print("Batch features:", batch_features.shape)
    print("Batch targets:", batch_targets.shape)
    print("Number of training batches:", len(train_loader))

    print("\nData pipeline completed successfully.")

if __name__=="__main__":
    main()

