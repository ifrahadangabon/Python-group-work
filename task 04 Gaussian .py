import numpy as np
import matplotlib.pyplot as plt
# Simplified steady-state temperature model for five interior grid points.
# Diagonal dominance makes Jacobi and Gauss-Seidel converge.
import numpy as np
from scipy.linalg import lu_factor, lu_solve
# The same coefficient matrix is reused for several measurement vectors.
A = np.array([
[4, -1, 0],
[-1, 4, -1],
[0, -1, 3]
])
measurement_sets = [
np.array([15.0, 10.0, 10.0]),
np.array([16.0, 11.0, 9.0]),
np.array([14.0, 12.0, 11.0])
]
# Factor A only once
lu, piv = lu_factor(A)
for i, b in enumerate(measurement_sets, start=6):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x

    print(f"Measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()
# Direct solution for comparison
print("Direct solution for first set:",
np.linalg.solve(A, measurement_sets[0]))



#my own example

import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Electricity consumption model for three buildings

# Coefficient matrix
A = np.array([
    [5, -1, 0],
    [-1, 5, -1],
    [0, -1, 4]
], dtype=float)

# Three different measurement sets
measurement_sets = [
    np.array([20.0, 15.0, 12.0]),
    np.array([22.0, 14.0, 13.0]),
    np.array([18.0, 16.0, 11.0])
]

# Factor A only once
lu, piv = lu_factor(A)

# Solve each measurement set
for i, b in enumerate(measurement_sets, start=1):

    x = lu_solve((lu, piv), b)

    residual = b - A @ x

    print(f"Measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()

# Direct solution for comparison
print("Direct solution for first set:")
print(np.linalg.solve(A, measurement_sets[0]))























