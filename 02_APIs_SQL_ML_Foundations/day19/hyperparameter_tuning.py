from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV, StratifiedKFold
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
        steps = [
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=5000)),
        ]
    )

    param_grid = {
        "classifier__C": [0.01, 0.1, 1, 10, 100]
    }

    search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        scoring="f1",
        cv=cv,
        n_jobs=-1,
        refit=True
    )

    search.fit(X,y)

    print("Best parameters:", search.best_params_)
    print("Best mean CV F1:", round(search.best_score_, 4))
    print("\nAll candidate results:")

    for mean_score, params in zip(
        search.cv_results_["mean_test_score"],
        search.cv_results_["params"],
    ):
        print(f"{params} -> F1: {mean_score:.4f}")


if __name__=="__main__":
    main()