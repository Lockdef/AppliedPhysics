import matplotlib.pyplot as plt
import numpy as np


def secondary_equation_euler_method(f, x_start, y_0, h, x_end):
    x = np.linspace(x_start, x_end, h)
    y = np.zeros(len(x))
    y[0] = y_0
    for i in range(1, len(x)):
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])
    return x, y
