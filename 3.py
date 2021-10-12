import numpy as np
import math as m
import matplotlib.pyplot as plt


def sin(x):
    a = x
    for i in range(2):
        a += ((-1)**i) * (x**(2 * i + 1)) / m.factorial(2 * i + 1)
    b = x
    for i in range(4):
        b += ((-1)**i) * (x**(2 * i + 1)) / m.factorial(2 * i + 1)
    c = x
    for i in range(6):
        c += ((-1)**i) * (x**(2 * i + 1)) / m.factorial(2 * i + 1)
    d = np.sin(x)
    return abs(a - d), abs(b - d), abs(c - d)


x = np.linspace(0.0, np.pi, 100)


y1, y2, y3 = [], [], []

for i in x:
    y1.append(sin(i)[0])
    y2.append(sin(i)[1])
    y3.append(sin(i)[2])

plt.plot(x, y1, 'r', label='$\\sin(x)$')
plt.plot(x, y2, 'r', label='$\\sin(x)$')
plt.plot(x, y3, 'r', label='$\\sin(x)$')
plt.show()
