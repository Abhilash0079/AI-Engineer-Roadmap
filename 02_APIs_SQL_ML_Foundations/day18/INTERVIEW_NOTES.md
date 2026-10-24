# Day 18 — Data Preprocessing Pipelines: Interview Notes

## 1. What is data preprocessing?
Data preprocessing transforms raw data into a suitable format for machine learning. Common tasks include handling missing values, scaling numerical features, and encoding categorical features.

## 2. What is imputation?
Imputation replaces missing values using a selected strategy.

- `SimpleImputer(strategy="mean")`: fills missing numerical values with the mean.
- `SimpleImputer(strategy="median")`: fills missing numerical values with the median.
- `SimpleImputer(strategy="most_frequent")`: fills missing values with the most frequent value.

The median is often useful when numerical data contains outliers.

## 3. What is feature scaling?
Feature scaling adjusts numerical features to comparable scales.

`StandardScaler` standardizes values using the mean and standard deviation learned from training data.

Scaling is especially useful for models such as Logistic Regression, KNN, and SVM. Tree-based models generally do not require standard scaling.

## 4. What is categorical encoding?
Categorical encoding converts categories into numerical representations.

`OneHotEncoder` creates indicator columns for categories. With `handle_unknown="ignore"`, unseen categories do not cause an encoding error; their encoded values are all zero across the categories learned by that encoder.

## 5. What is ColumnTransformer?
`ColumnTransformer` applies different transformations to selected column groups.

Example:
- Numerical columns: median imputation followed by scaling.
- Categorical columns: most-frequent imputation followed by one-hot encoding.

## 6. What is Pipeline?
`Pipeline` connects sequential steps into one workflow. For example, a preprocessing step can be followed by a Logistic Regression classifier.

When the pipeline is fitted, each step learns from the training data. During prediction, the fitted transformations are applied before the classifier generates predictions.

## 7. What is data leakage?
Data leakage occurs when information that should be unavailable during training influences the training process or evaluation.

To avoid preprocessing leakage:
1. Split the dataset into training and test sets.
2. Fit preprocessing and the model using training data only.
3. Use the fitted pipeline to predict on test data.

A scikit-learn pipeline helps enforce this workflow when used correctly.

## 8. What is the difference between fit, transform, and fit_transform?
- `fit()`: learns parameters from data.
- `transform()`: applies previously learned parameters.
- `fit_transform()`: learns parameters and transforms the supplied data.

For example, fit a scaler on training data and transform test data with that fitted scaler.

## 9. Why should we not fit StandardScaler on test data?
The test set is reserved for evaluation. Fitting the scaler on it uses information from the test distribution and can make evaluation less representative of a truly unseen dataset.

## 10. What happens when an unseen category appears?
With `OneHotEncoder(handle_unknown="ignore")`, an unseen category is encoded as zeros across the learned category indicators for that feature. The prediction pipeline can continue without an unknown-category encoding error, but the model has not learned the meaning of the new category.

## 11. Pipeline vs. ColumnTransformer

| Component | Responsibility |
|---|---|
| `Pipeline` | Connects sequential preprocessing and model steps |
| `ColumnTransformer` | Applies different transformations to selected column groups |

They are commonly combined.

## 12. Why was the example accuracy 50%?
The test set contains only two records, and one was predicted correctly. The score is therefore 1 out of 2, or 50%. Two test examples are far too few to estimate real-world performance reliably.

## 13. Interview questions and short answers

**Q: Why use a pipeline?**  
A: It makes preprocessing and model training reusable, consistent, and easier to maintain.

**Q: Why use ColumnTransformer?**  
A: It applies different preprocessing operations to different column groups.

**Q: Why use OneHotEncoder?**  
A: It converts categorical features into numerical indicator columns.

**Q: Why split before fitting preprocessing?**  
A: To prevent information from the test set from influencing preprocessing learned during training.

**Q: Does a pipeline automatically prevent every kind of data leakage?**  
A: No. It helps prevent leakage from preprocessing when correctly fitted, but the overall data preparation and feature selection process must also be designed carefully.

**Q: Must every ML model use StandardScaler?**  
A: No. Scaling is important for many distance-based and gradient-based models, but usually unnecessary for decision trees and random forests.

## Day 18 Summary
I implemented preprocessing for numerical and categorical features, combined the transformations with Logistic Regression in a scikit-learn pipeline, used a train/test split, and reviewed how to avoid data leakage.