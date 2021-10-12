import numpy as np
import matplotlib.pyplot as plt


def sin(x):
    a = x
    for i in range(1, 2):
        a += ((-1)**i) * (x**(2 * i + 1)) / (2 * i + 1)
    b = x
    for i in range(1, 4):
        b += ((-1)**i) * (x**(2 * i + 1)) / (2 * i + 1)
    c = x
    for i in range(1, 6):
        c += ((-1)**i) * (x**(2 * i + 1)) / (2 * i + 1)
    d = np.sin(x)
    return abs(a - d), abs(b - d), abs(c - d)


x = np.linspace(0.0, 3.14, 100)


y1 = []
y2 = []
y3 = []

for i in x:
    y1.append(sin(i)[0])
    y2.append(sin(i)[1])
    y3.append(sin(i)[2])

plt.plot(x, y1, 'r', label='$\\sin(x)$')
plt.plot(x, y2, 'r', label='$\\sin(x)$')
plt.plot(x, y3, 'r', label='$\\sin(x)$')
plt.show()
