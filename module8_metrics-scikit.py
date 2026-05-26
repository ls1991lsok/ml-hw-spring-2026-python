import sys
import numpy as np
from sklearn.metrics import precision_score, recall_score


def read_positive_int(prompt: str) -> int:
    raw = input(prompt)
    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"Expected a positive integer, got: {raw!r}")

    if value <= 0:
        raise ValueError(f"Expected a positive integer (> 0), got: {value}")

    return value


def read_binary_label(prompt: str) -> int:
    raw = input(prompt)
    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"Expected a binary label 0 or 1, got: {raw!r}")

    if value not in (0, 1):
        raise ValueError(f"Expected a binary label 0 or 1, got: {value}")

    return value


def main() -> int:
    try:
        N = read_positive_int("Enter N (positive integer, number of points): ")
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    data = np.empty((N, 2), dtype=int)

    print(f"\nNow enter {N} (x, y) points, one value per line:")
    print("x = ground truth label, y = predicted label")
    print("Both x and y must be either 0 or 1.\n")

    for i in range(N):
        try:
            x_value = read_binary_label(f"  Point {i + 1} - x: ")
            y_value = read_binary_label(f"  Point {i + 1} - y: ")
        except ValueError as e:
            print(f"Error: {e}")
            return 1

        data[i, 0] = x_value
        data[i, 1] = y_value

    y_true = data[:, 0]
    y_pred = data[:, 1]

    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    print("\nClassification metrics:")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())