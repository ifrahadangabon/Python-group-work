import numpy as np
from scipy.optimize import root

# Find intersections of:
# Circle: x^2 + y^2 = 4
# Parabola: y = x^2 - 1
def equations(z):
    x, y = z
    return [
        x*2 + y*2 - 4,
        y - (x**2 - 1)
    ]

# Define your initial guess and solve (hidden under the tooltip)
guess = [1, 1] 
solution = root(equations, guess)

print("Initial guess:", guess)
print("Intersection:", solution.x)
print("Residuals:", equations(solution.x))
print("Converged:", solution.success)
print()


#my own example
import numpy as np
from scipy.optimize import root

# Satellite coordinates (X, Y, Z) in km
sat1 = np.array([0, 0, 6371])
sat2 = np.array([10000, 0, 0])
sat3 = np.array([0, 10000, 0])

# Measured distances to each satellite in km
d1 = 20000
d2 = 15000
d3 = 18000

# Define GPS equations
def gps_equations(p):
    x, y, z = p

    return [
        (x - sat1[0])**2 + (y - sat1[1])**2 + (z - sat1[2])**2 - d1**2,

        (x - sat2[0])**2 + (y - sat2[1])**2 + (z - sat2[2])**2 - d2**2,

        (x - sat3[0])**2 + (y - sat3[1])**2 + (z - sat3[2])**2 - d3**2
    ]

# Initial guess near the Earth's surface
initial_guess = [1000, 1000, 1000]

# Solve nonlinear equations
solution = root(gps_equations, initial_guess)

# Display results
print("Success:", solution.success)
print("Estimated Coordinates (x, y, z):", solution.x)
print("Residual errors:", gps_equations(solution.x))
