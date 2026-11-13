
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Heat-balance model:
# f(T) = 0 means heat gain equals heat loss.

def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)

# Bisection method
solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

# Fixed-point form:
# T = 25 + 10 * exp(-T/20)

def g(T):
    return 25 + 10 * np.exp(-T / 20)

T = 30.0
history = [T]

for _ in range(100):
    T_new = g(T)
    history.append(T_new)

    if abs(T_new - T) < 1e-10:
        break

    T = T_new

# Display results
print(f"Bisection equilibrium temperature: {solution.root:.6f} C")

print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} C")

print("Fixed-point iterations:", len(history) - 1)

# Plot graph
temps = np.linspace(20, 40, 300)

plt.plot(temps, heat_balance(temps))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")

plt.xlabel("Temperature (C)")
plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature")
plt.grid(True)

plt.show()


#Water-tank equilibrium
#A water tank has an equilibrium level represented by:
#f(h)=h-15-8e^{-h/10}

import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Water-tank equilibrium model

def water_level(h):
    return h - 15 - 8 * np.exp(-h / 10)

# Bisection method

solution = root_scalar(
    water_level,
    bracket=[15, 30],
    method="bisect",
    xtol=1e-10
)

# Fixed-point function

def g(h):
    return 15 + 8 * np.exp(-h / 10)

# Initial water level

h = 20.0
history = [h]

# Fixed-point iteration

for _ in range(100):
    h_new = g(h)
    history.append(h_new)

    if abs(h_new - h) < 1e-10:
        break

    h = h_new

# Display results

print(f"Bisection equilibrium level: {solution.root:.6f} m")

print(f"Fixed-point equilibrium level: {history[-1]:.6f} m")

print("Fixed-point iterations:", len(history) - 1)

# Draw graph

levels = np.linspace(15, 30, 300)

plt.plot(levels, water_level(levels))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")

plt.xlabel("Water level (m)")
plt.ylabel("Water-level function")
plt.title("Water Tank Equilibrium")
plt.grid(True)

plt.show()
