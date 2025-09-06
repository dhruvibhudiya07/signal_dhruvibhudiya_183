import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    y = np.where(n >= 0, 1, 0)
    plt.stem(n, y)
    plt.title("Unit Step Signal")
    plt.show()
    return y

def unit_impulse(n):
    y = np.where(n == 0, 1, 0)
    plt.stem(n, y)
    plt.title("Unit Impulse Signal")
    plt.show()
    return y

def ramp_signal(n):
    y = np.where(n >= 0, n, 0)
    plt.stem(n, y)
    plt.title("Ramp Signal")
    plt.show()
    return y