
import numpy as np
import matplotlib.pyplot as plt

# Simplified steady-state temperature model for five interior grid points
# Diagonal dominance makes Jacobi and Gauss-Seidel converge

A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary influence: left boundary = 100 C, right boundary = 20 C
b = np.array([100., 0., 0., 0., 20.])


# Jacobi Method
def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        x_new = (b - R @ x) / D

        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)

        if error < tol:
            return x_new, errors

        x = x_new

    return x, errors


# Gauss-Seidel Method
def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        old = x.copy()

        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]

        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)

        if error < tol:
            return x, errors

    return x, errors


# Solve using Jacobi and Gauss-Seidel
x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)

# Direct solution using NumPy
x_exact = np.linalg.solve(A, b)


# Display the results
print("Jacobi temperatures:", x_j)
print("Gauss-Seidel temperatures:", x_gs)
print("Direct solution:", x_exact)

print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))


# Plot convergence comparison
plt.figure(figsize=(8, 5))

plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")

plt.xlabel("Iteration")
plt.ylabel("Error")
plt.title("Jacobi vs Gauss-Seidel Convergence")

plt.legend()
plt.grid(True)

plt.show()



#my example

 #Practice example: Room temperature distribution
# A building has five interior points where temperatures need to be calculated.
# The system is represented by Ax=b

import numpy as np

A = np.array([
    [2., -1., 0., 0., 0.],
    [-1., 2., -1., 0., 0.],
    [0., -1., 2., -1., 0.],
    [0., 0., -1., 2., -1.],
    [0., 0., 0., -1., 2.]
])

b = np.array([80., 0., 0., 0., 30.])

# Initial temperature guesses
x = np.zeros(5)

# Set tolerance and maximum iterations
tolerance = 0.000001
max_iterations = 1000

# Jacobi iteration
for iteration in range(max_iterations):

    x_new = np.zeros(5)

    for i in range(5):
        total = 0

        for j in range(5):
            if i != j:
                total += A[i, j] * x[j]

        x_new[i] = (b[i] - total) / A[i, i]

    # Check convergence
    if np.max(np.abs(x_new - x)) < tolerance:
        x = x_new
        break

    x = x_new

# Display results
print("Room temperature distribution")
print("Number of iterations:", iteration + 1)

for i in range(5):
    print(f"Point {i+1}: {x[i]:.4f} degrees")