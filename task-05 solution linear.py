
import numpy as np

# x = number of Type A servers
# y = number of Type B servers
#
# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total observed usage: 20 CPU units and 72 GB memory

# Create the coefficient matrix
A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

# Create the values array
b = np.array([20.0, 72.0])

# Solve the simultaneous linear equations
solution = np.linalg.solve(A, b)

# Calculate residual
residual = b - A @ solution

# Display the results
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")

# Verify the solution
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

#my own example
#A university uses two types of network servers:
#Type A uses 6 CPU units and 5 GB of memory.
#Type B uses 2 CPU units and 10 GB of memory.
# Total CPU usage is 22 units.
#Total memory usage is 35 GB.
import numpy as np
# Create coefficient matrix
A = np.array([
    [6.0, 2.0],
    [5.0, 10.0]
])

# Create values array
b = np.array([22.0, 35.0])

# Solve simultaneous equations
solution = np.linalg.solve(A, b)

# Calculate residual
residual = b - A @ solution

# Display results
print("Type A servers:", solution[0])
print("Type B servers:", solution[1])

# Verify solution
print("Verification:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

