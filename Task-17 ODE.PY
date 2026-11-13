import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# RC charging circuit
Vs = 5.0
R = 1000.0
C = 0.001
V0 = 0.0

# Differential equation
def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]

# Time points
t_eval = np.linspace(0, 5, 200)

# Solve the differential equation
solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Exact solution
exact = Vs * (1 - np.exp(-solution.t / (R * C)))

print("Solver success:", solution.success)
print(f"Capacitor voltage at 5 s: {solution.y[0, -1]:.4f} V")

# Calculate error
error = np.max(np.abs(solution.y[0] - exact))
print(f"Maximum error: {error:.3e} V")

# Plot graph
plt.plot(solution.t, solution.y[0], label="Numerical solution")
plt.plot(solution.t, exact, "--", label="Exact solution")

plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.title("RC Circuit Charging")
plt.legend()
plt.grid(True)
plt.show()


#RC Circuit Charging

#A capacitor is connected to a 12 V battery through a resistor of 2000 Ω 
#and a capacitor of 0.002 F.

#Initially, the capacitor has 0 V.

#Write a Python program using solve_ivp to:
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# RC charging circuit
Vs = 12.0
R = 2000.0
C = 0.002
V0 = 0.0

# Differential equation
def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]

# Time points
t_eval = np.linspace(0, 5, 200)

# Solve differential equation
solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Exact solution
exact = Vs * (1 - np.exp(-solution.t / (R * C)))

# Display results
print("Solver success:", solution.success)
print(f"Capacitor voltage at 5 s: {solution.y[0, -1]:.4f} V")

# Calculate error
error = np.max(np.abs(solution.y[0] - exact))
print(f"Maximum error: {error:.3e} V")

# Plot graph
plt.plot(solution.t, solution.y[0], label="Numerical solution")
plt.plot(solution.t, exact, "--", label="Exact solution")

plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.title("RC Circuit Charging")
plt.legend()
plt.grid(True)
plt.show()
