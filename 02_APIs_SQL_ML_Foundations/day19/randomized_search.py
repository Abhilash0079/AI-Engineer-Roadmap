from scipy.stats import loguniform
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def main():
    dataset = load_breast_cancer()
    X = dataset.data
    y = dataset.target

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42,
    )

    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=5000)),
        ]
    )

    param_distributions = {
        "classifier__C": loguniform(0.001, 100)
    }

    search = RandomizedSearchCV(
        estimator=pipeline,
        param_distributions=param_distributions,
        n_iter=10,
        scoring="f1",
        cv=cv,
        random_state=42,
        n_jobs=-1,
        refit=True,
    )

    search.fit(X, y)

    print("Number of candidates:", len(search.cv_results_["params"]))
    print("Best parameters:", search.best_params_)
    print("Best mean CV F1:", round(search.best_score_, 4))

    print("\nTop candidate results:")
    results = sorted(
        zip(
            search.cv_results_["mean_test_score"],
            search.cv_results_["params"],
        ),
        key=lambda item: item[0],
        reverse=True,
    )

    for score, params in results[:5]:
        print(f"{params} -> F1: {score:.4f}")


if __name__ == "__main__":
    main()
