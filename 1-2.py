import math
import matplotlib.pyplot as plt


def cos(x, n, nega, numerator, denominator, y):
    m = 2 * n
    denominator = denominator * m * (m - 1)
    numerator = numerator * x * x
    a = numerator / denominator
    if (a <= 0.00000000001):
        return y
    else:
        return y + cos(x, n + 1, not nega, numerator,
                       denominator, a if nega else -a)


x = []
y = []

for i in range(0, 25):
    degree = i * 15
    if degree % 30 == 0 or degree % 45 == 0:
        radian = math.radians(degree)
        d1 = cos(radian, 1, False, 1.0, 1.0, 1.0)
        x.append(degree)
        y.append(d1)

plt.plot(x, y)

plt.show()
