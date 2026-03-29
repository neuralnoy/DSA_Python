import math
import matplotlib.pyplot as plt

class Functions:
    @staticmethod
    def linear(constant, number):
        return constant * number

    @staticmethod
    def const_log_n(constant, number):
        return constant * number * math.log(number)

    @staticmethod
    def const_n_power(constant, number, power):
        return constant * (number ** power)

    @staticmethod
    def power_of_two(number):
        return 2 ** number

    @staticmethod
    def log_scale(number):
        if number <= 0:
            raise ValueError("Log scale requires positive numbers")
        return math.log(number)

# Data
data = range(1, 50)  # smaller range for 2^n to avoid overflow

# X-axis: log(n)
x = [Functions.log_scale(n) for n in data]

# Functions to plot
functions = [
    ("8n", lambda n: Functions.linear(8, n)),
    ("4n log n", lambda n: Functions.const_log_n(4, n)),
    ("2n^2", lambda n: Functions.const_n_power(2, n, 2)),
    ("n^3", lambda n: Functions.const_n_power(1, n, 3)),
    ("2^n", lambda n: Functions.power_of_two(n))
]

# Plot each function
for name, func in functions:
    y = []
    for n in data:
        val = func(n)
        # only take positive numbers for log scale
        if val > 0:
            y.append(Functions.log_scale(val))
        else:
            y.append(float('nan'))
    plt.plot(x, y, label=name, marker='o', linestyle='-')

plt.xlabel("log(n)")
plt.ylabel("log(f(n))")
plt.title("Log-Log Plot of Functions")
plt.legend()
plt.show()
