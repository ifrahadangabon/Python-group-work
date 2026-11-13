
import numpy as np
from scipy.optimize import minimize

# x = number of Type A servers
# y = number of Type B servers

# Cost per server
# Type A = 15
# Type B = 20

# Capacity per server
# Type A = 120
# Type B = 200

# Required capacity = at least 1200

def cost(z):
    x, y = z
    return 15*x + 20*y

# Capacity constraint
def capacity_constraint(z):
    x, y = z
    return 120*x + 200*y - 1200

constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

# Servers cannot be negative
bounds = [(0, None), (0, None)]

# Perform optimization
solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization success:", solution.success)
print(f"Type A servers: {x:.3f}")
print(f"Type B servers: {y:.3f}")
print(f"Total capacity: {120*x + 200*y:.2f}")
print(f"Minimum cost: Ksh {solution.fun:.2f}")

# Check nearby whole-number combinations
best_integer = None

for a in range(0, 20):
    for b in range(0, 20):
        capacity = 120*a + 200*b

        if capacity >= 1200:
            total_cost = 15*a + 20*b

            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity)

print("Best integer solution:", best_integer)


#my example
#Production cost optimization
#A factory produces two products, Product A and Product B.
#- Product A costs Ksh 25 per unit and uses 4 machine hours.
#- Product B costs Ksh 35 per unit and uses 6 machine hours.
#- The factory must produce at least 100 units of machine-hour capacity.
#- The factory wants to minimize production costs.


import numpy as np
from scipy.optimize import minimize

# x = number of Product A units
# y = number of Product B units

# Cost per unit
# Product A = 25
# Product B = 35

# Machine hours per unit
# Product A = 4
# Product B = 6

# Required machine hours = at least 100

def cost(z):
    x, y = z
    return 25*x + 35*y

# Machine hour constraint
def machine_constraint(z):
    x, y = z
    return 4*x + 6*y - 100

constraints = {
    "type": "ineq",
    "fun": machine_constraint
}

# Non-negative production quantities
bounds = [(0, None), (0, None)]

# Perform optimization
solution = minimize(
    cost,
    x0=[10, 10],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization success:", solution.success)
print(f"Product A units: {x:.3f}")
print(f"Product B units: {y:.3f}")
print(f"Total machine hours: {4*x + 6*y:.2f}")
print(f"Minimum production cost: Ksh {solution.fun:.2f}")

# Check whole-number solutions
best_integer = None

for a in range(0, 30):
    for b in range(0, 30):
        hours = 4*a + 6*b

        if hours >= 100:
            total_cost = 25*a + 35*b

            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, hours)

print("Best integer solution:", best_integer)
