import matplotlib.pyplot as plt
import math


exp = math.e
g = 9.8
p = 1000
n = 1.8e3
y_0 = 150
v_x0 = 20


def calc_m(r):
    return (4 / 3) * math.pi * r ** 3 * p


def x(t, r):
    m = calc_m(r)
    return (m * v_x0 / n) * (1 - exp - n / m * t)


def y(t, r):
    m = calc_m(r)
    return y_0 + (m ** 2 * g / n ** 2) * (1 - exp * (-n / m * t) + t)


def max_x(r):
    m = calc_m(r)
    return (m * v_x0) / n


def plot_prob1():
    x = list(map(lambda x: x / 1e6, range(1001)))
    y = list(map(lambda x: max_x(x / 2), x))
    plt.plot(x, y)
    plt.show()


def plot_prob2():
    x = list(map(lambda x: x / 1e6, range(1001)))


if __name__ == '__main__':
    plot_prob1()
    plot_prob2()
