import matplotlib.pyplot as plt
import numpy as np

n1 = eval(input("Enter the first list of numbers: "))
n2 = eval(input("Enter the second list of numbers: "))


def f(x1):
    return 1 / (0.185 - 1.5325 / x1)


x = np.arange(9, 100, 1)
x2 = n1
y2 = n2
plt.plot(x, f(x), 'r-', x2, y2, 'g-')
plt.axis([0, 50, 0, 50])

plt.grid(True)
plt.title("Imaging law of single spherical surface")
plt.xlabel("object distance/cm")
plt.ylabel("image distance/cm")
plt.show()
