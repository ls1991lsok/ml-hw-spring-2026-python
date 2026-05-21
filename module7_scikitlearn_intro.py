import sys
import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def read_positive_int(prompt: str) -> int:
    raw = input(prompt)
    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"Expected a positive integer, got: {raw!r}")
    if value <= 0:
        raise ValueError(f"Expected a positive integer (> 0), got: {value}")
    return value


def read_float(prompt: str) -> float:
    raw = input(prompt)
    try:
        return float(raw)
    except ValueError:
        raise ValueError(f"Expected a real number, got: {raw!r}")


def main() -> int:
    try:
        N = read_positive_int("Enter N (positive integer, number of points): ")
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    try:
        k = read_positive_int("Enter k (positive integer, number of neighbors): ")
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    X_train = np.empty((N, 1), dtype=float)
    y_train = np.empty(N, dtype=float)

    print(f"\nNow enter {N} (x, y) points, one value per line:")
    for i in range(N):
        try:
            xi = read_float(f"  Point {i + 1} - x: ")
            yi = read_float(f"  Point {i + 1} - y: ")
        except ValueError as e:
            print(f"Error: {e}")
            return 1
        X_train[i, 0] = xi
        y_train[i] = yi

    try:
        X_query = read_float("\nEnter X (query point): ")
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    if k > N:
        print(f"Error: k ({k}) must be <= N ({N}). Cannot perform k-NN regression.")
        variance = float(np.var(y_train))
        print(f"Variance of labels in the training dataset: {variance}")
        return 1

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    Y_pred = model.predict(np.array([[X_query]], dtype=float))[0]

    print(f"\nk-NN Regression result Y for X = {X_query}: {Y_pred}")

    variance = float(np.var(y_train))
    print(f"Variance of labels in the training dataset: {variance}")

    return 0


if __name__ == "__main__":
    sys.exit(main())