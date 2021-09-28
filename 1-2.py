import math
import matplotlib.pyplot as plt


class funcition:

    def cos(self, x, n, nega, numerator, denominator, y):
        m = 2 * n
        denominator = denominator * m * (m - 1)
        numerator = numerator * x * x
        a = numerator / denominator
        if (a <= 0.00000000001):
            return y
        else:
            return y + self.cos(x, n + 1, not nega, numerator,
                                denominator, a if nega else -a)

    def exp(self, x, n, numerator, denominator, y):
        denominator = denominator * n
        numerator = numerator * x
        a = numerator / denominator
        if (abs(a) <= 0.00000000001):
            return y
        else:
            return y + self.exp(x, n + 1, numerator, denominator, a)

    def log(self, x2, numerator, denominator, y):
        denominator = denominator + 2
        numerator = numerator * x2 * x2
        a = numerator / denominator
        if (abs(a) <= 0.00000000001):
            return y
        else:
            return y + self.log(x2, numerator, denominator, a)

    def plotCos(self):
        x = []
        y = []
        for i in range(0, 25):
            degree = i * 15
            if degree % 30 == 0 or degree % 45 == 0:
                radian = math.radians(degree)
                d1 = self.cos(radian, 1, False, 1.0, 1.0, 1.0)
                x.append(degree)
                y.append(d1)
        plt.plot(x, y)
        plt.title("cos")
        plt.show()

    def plotExp(self):
        x = []
        y = []
        for i in range(0, 21):
            x_ = (i - 10) / 4.0
            d2 = self.exp(x_, 1, 1.0, 1.0, 1.0)
            y.append(d2)
            x.append(x_)
        plt.plot(x, y)
        plt.title("exp")
        plt.show()

    def plotLog(self):
        x = []
        y = []
        for i in range(1, 21):
            x_ = i / 5.0
            x2 = (x_ - 1) / (x_ + 1)
            d2 = 2 * self.log(x2, x2, 1.0, x2)
            y.append(d2)
            x.append(x_)
        plt.plot(x, y)
        plt.title("log")
        plt.show()


if __name__ == '__main__':
    f = funcition()
    f.plotCos()
    f.plotExp()
    f.plotLog()
