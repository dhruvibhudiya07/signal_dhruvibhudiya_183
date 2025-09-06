import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, k):
    shifted = np.roll(signal, k)
    plt.plot(shifted)
    plt.title(f"Time Shifted Signal by {k}")
    plt.show()
    return shifted

def time_scale(signal, k):
    scaled = signal[::k]
    plt.plot(scaled)
    plt.title(f"Time Scaled Signal by {k}")
    plt.show()
    return scaled

def signal_addition(signal1, signal2):
    added = signal1 + signal2
    plt.plot(added)
    plt.title("Signal Addition")
    plt.show()
    return added

def signal_multiplication(signal1, signal2):
    multiplied = signal1 * signal2
    plt.plot(multiplied)
    plt.title("Signal Multiplication")
    plt.show()
    return multiplied