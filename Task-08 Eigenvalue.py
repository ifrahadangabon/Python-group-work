
import numpy as np

# Adjacency matrix for a small undirected network
# Node order: A, B, C, D

A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the dominant eigenvalue and eigenvector
index = np.argmax(np.real(eigenvalues))

dominant_value = np.real(eigenvalues[index])

dominant_vector = np.abs(np.real(eigenvectors[:, index]))

# Calculate centrality
centrality = dominant_vector / dominant_vector.sum()

# Name the nodes
nodes = ["A", "B", "C", "D"]

# Display results
print("Dominant eigenvalue:", dominant_value)

print("Eigenvector-based importance:")

for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify Av = lambda * v
v = np.real(eigenvectors[:, index])

print("Verification error:",
      np.linalg.norm(A @ v - dominant_value * v))




import numpy as np

# Adjacency matrix for an undirected network
# Node order: A, B, C, D, E

A = np.array([
    [0., 1., 1., 0., 0.],
    [1., 0., 1., 1., 0.],
    [1., 1., 0., 1., 1.],
    [0., 1., 1., 0., 1.],
    [0., 0., 1., 1., 0.]
])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find dominant eigenvalue
index = np.argmax(np.real(eigenvalues))

dominant_value = np.real(eigenvalues[index])

# Find dominant eigenvector
dominant_vector = np.abs(
    np.real(eigenvectors[:, index])
)

# Calculate centrality
centrality = dominant_vector / dominant_vector.sum()

# Name the nodes
nodes = ["A", "B", "C", "D", "E"]

# Display results
print("Dominant eigenvalue:", dominant_value)

print("Eigenvector-based importance:")

for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify Av = lambda * v
v = np.real(eigenvectors[:, index])

print("Verification error:",
      np.linalg.norm(A @ v - dominant_value * v))
