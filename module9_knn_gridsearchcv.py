# module9_knn_gridsearchcv.py

import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from sklearn.neighbors import KNeighborsClassifier


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Error: please enter a positive integer.")
        except ValueError:
            print("Error: please enter an integer.")


def read_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Error: please enter a non-negative integer.")
        except ValueError:
            print("Error: please enter an integer.")


def read_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: please enter a real number.")


def read_dataset(number_of_pairs, dataset_name):
    x_values = np.zeros((number_of_pairs, 1), dtype=float)
    y_values = np.zeros(number_of_pairs, dtype=int)

    for i in range(number_of_pairs):
        print(f"{dataset_name} pair #{i + 1}")
        x_values[i, 0] = read_real_number("Enter x value: ")
        y_values[i] = read_non_negative_integer("Enter y value: ")

    return x_values, y_values


def find_best_knn_model(x_train, y_train):
    number_of_training_samples = len(x_train)

    if number_of_training_samples == 1:
        model = KNeighborsClassifier(n_neighbors=1)
        model.fit(x_train, y_train)
        return 1, model

    cv = LeaveOneOut()

    max_k = min(10, number_of_training_samples - 1)

    param_grid = {
        "n_neighbors": np.arange(1, max_k + 1)
    }

    knn = KNeighborsClassifier()

    grid_search = GridSearchCV(
        estimator=knn,
        param_grid=param_grid,
        scoring="accuracy",
        cv=cv
    )

    grid_search.fit(x_train, y_train)

    best_k = grid_search.best_params_["n_neighbors"]
    best_model = grid_search.best_estimator_

    return best_k, best_model


def main():
    print("Mini kNN Classifier with GridSearchCV")

    n = read_positive_integer("Enter N, the number of training pairs: ")
    x_train, y_train = read_dataset(n, "Training")

    m = read_positive_integer("Enter M, the number of test pairs: ")
    x_test, y_test = read_dataset(m, "Test")

    best_k, best_model = find_best_knn_model(x_train, y_train)

    y_pred = best_model.predict(x_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    print("Best k:", best_k)
    print("Test accuracy:", test_accuracy)


if __name__ == "__main__":
    main()
