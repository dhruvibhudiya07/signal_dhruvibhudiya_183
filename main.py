import numpy as np
from signal_DhruviBhudiya_183 import unitary_signals, trigonomatric_signals, operations

# 1. Generate unit step, impulse and ramp signals
n = np.arange(-10, 10)
step = unitary_signals.unit_step(n)
impulse = unitary_signals.unit_impulse(n)
ramp = unitary_signals.ramp_signal(n)

# 2. Generate sine,cosine and exponential wave
t = np.linspace(0, 1, 500)
sine = trigonomatric_signals.sine_wave(2, 5, 0, t)
cosine = trigonomatric_signals.cosine_wave(2, 5, 0, t)
exp_signal = trigonomatric_signals.exponential_signal(1, 2, t)  # A=1, a=2

# 3. Time shift, scale, add and multiplication wave
shifted_sine = operations.time_shift(sine, 5)  # Use 50 because 500 samples in 1s, so +5 units = 50 indices
scaled_sine = operations.time_scale(sine, 2)
added = operations.signal_addition(step, ramp)
product = operations.signal_multiplication(sine,cosine)