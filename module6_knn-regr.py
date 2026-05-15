import numpy as np


class KNNRegressor:
    def __init__(self):
        self.points = np.empty((0, 2), dtype=float)

    def insert_point(self, x, y):
        new_point = np.array([[x, y]], dtype=float)
        self.points = np.vstack((self.points, new_point))

    def predict(self, k, query_x):
        x_values = self.points[:, 0]
        y_values = self.points[:, 1]

        distances = np.abs(x_values - query_x)
        nearest_indices = np.argsort(distances)[:k]

        predicted_y = np.mean(y_values[nearest_indices])
        return predicted_y


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Error: please enter a positive integer.")
        except ValueError:
            print("Error: please enter a valid integer.")


def read_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: please enter a valid real number.")


def main():
    N = read_positive_integer("Enter N: ")
    k = read_positive_integer("Enter k: ")

    model = KNNRegressor()

    for i in range(N):
        print(f"Enter point {i + 1}:")
        x = read_real_number("Enter x value: ")
        y = read_real_number("Enter y value: ")
        model.insert_point(x, y)

    query_x = read_real_number("Enter X: ")

    if k <= N:
        result = model.predict(k, query_x)
        print("Predicted Y:", result)
    else:
        print("Error: k must be less than or equal to N.")


if __name__ == "__main__":
    main()