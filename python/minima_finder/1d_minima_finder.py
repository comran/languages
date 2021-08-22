import numpy as np
import matplotlib.pyplot as plt
from typing import Any


EPSILON = 1e-6


def equation(x_unclipped: Any):
    x = np.maximum(-4, np.minimum(3, x_unclipped))

    return np.power(x, 6) \
            + np.power(x, 5) \
            - 13 * np.power(x, 4) \
            - 0.9 * np.power(x, 3) \
            + 34 * np.power(x, 2) \
            - 14.5 * x \
            + 210


def gradient_descent(x):
    current_x = x
    max_epsilon = 0.5
    total_sims = 1000

    for i in range(1000):
        current_x = max(-6, min(6, current_x))
        epsilon = max_epsilon * (total_sims - i) / total_sims
        x_sides = np.array([
            current_x - epsilon / 2.,
            current_x + epsilon / 2.]
        )
        y_sides = equation(x_sides)

        current_x = x_sides[1] if y_sides[1] < y_sides[0] else \
            x_sides[0] if y_sides[0] < y_sides[1] else current_x

    return current_x


# def minima_finder():
#     pass


def plot_equation():
    x_minimas = []
    for x in np.linspace(-6, 6, 100):
        x_minima = gradient_descent(x)
        x_minimas.append(x_minima)

    x_minimas = np.array(x_minimas)
    y_minimas = equation(x_minimas)

    x = np.linspace(-6, 6, 10000)
    y = equation(x)
    plt.plot(x, y)
    plt.scatter(x_minimas, y_minimas, c="red")

    plt.show()


if __name__ == "__main__":
    plot_equation()
