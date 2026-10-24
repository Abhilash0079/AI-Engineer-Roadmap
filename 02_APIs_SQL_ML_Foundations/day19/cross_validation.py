from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import StratifiedKFold,cross_val_score, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def main():
    # Load a built-in binary classification dataset.
    dataset = load_breast_cancer()
    X = dataset.data
    y = dataset.target

    # Keep the class proportions similar across folds.
    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42,
    )

    # Fit preprocessing separately inside each training fold.
    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=5000)),
        ]
    )

    # scores = cross_val_score(
    #     model,
    #     X,
    #     y,
    #     cv=cv,
    #     scoring="accuracy",
    # )

    # print("Dataset shape:", X.shape)
    # print("Number of folds:", cv.get_n_splits())
    # print("Fold accuracy scores:", scores)
    # print("Mean accuracy:", round(scores.mean(), 4))
    # print("Standard deviation:", round(scores.std(), 4))

    scoring = {
        "accuracy": "accuracy",
        "precision": "precision",
        "recall": "recall",
        "f1": "f1",
    }
    
    results = cross_validate(
        model,
        X,
        y,
        cv=cv,
        scoring=scoring,
    )
    
    for metric in scoring:
        fold_scores = results[f"test_{metric}"]
        print(f"{metric.capitalize()} fold scores:", fold_scores)
        print(f"Mean {metric}:", round(fold_scores.mean(), 4))

if __name__ == "__main__":
    main()