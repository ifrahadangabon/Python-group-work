import numpy as np
# Four corners of a square:c each row is [x, y]
points = np.array([
[0.0, 0.0],
[1.0, 0.0],
[1.0, 1.0],
[0.0, 1.0]
])
print("Original points:\n", points) 
angle = np.deg2rad(45)
rotation = np.array([
[np.cos(angle), -np.sin(angle)],
[np.sin(angle), np.cos(angle)]
])
print("rotation:\n", rotation)
scale = np.array([
[2.0, 0.0],
   [0.0, 1.5] ]) 
print("scale:\n",scale)
transformation = rotation @ scale 
print("Transformation matrix:\n", transformation) 
transformed_points = points @ transformation
print("Transformed points:\n", transformed_points)




#Rotating and scaling a rectangle

#A rectangle has four points:

import numpy as np

# Four corners of a rectangle
points = np.array([
    [0.0, 0.0],
    [2.0, 0.0],
    [2.0, 1.0],
    [0.0, 1.0]
])

print("Original points:\n", points)

# Rotation angle
angle = np.deg2rad(30)

# Rotation matrix
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

print("Rotation:\n", rotation)

# Scaling matrix
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

print("Scale:\n", scale)

# Combine transformations
transformation = rotation @ scale

print("Transformation matrix:\n", transformation)

# Transform points
transformed_points = points @ transformation

print("Transformed points:\n", transformed_points)

