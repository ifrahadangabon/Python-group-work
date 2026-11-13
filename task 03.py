# Numerical stability and floating point precision .

#Floating-point error: Computers cannot represent some decimal numbers exactly in binary.
#Exact comparison: 0.1 + 0.2 == 0.3 returns False because the calculated value is slightly
#  different from the expected value .
#np.isclose(): Checks whether two numbers are sufficiently close within a tolerance.
#Absolute error: The difference between the true value and the approximate value.
# elative error: The absolute error divided by the magnitude of the true value.
#Direct and stable formulas: Two mathematically equivalent expressions can produce different
#  numerical accuracy because of how the computer performs calculation.

import numpy as np

# Example 1: Floating-point comparison
calculated = 0.1 + 0.2
expected = 0.3

print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance comparison:", np.isclose(calculated, expected))

# Example 2: Absolute and relative error
true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nAbsolute error:", round(absolute_error, 8))
print("Relative error:", f"{relative_error:.4%}")

# Example 3: Direct and stable formulas
for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)

    print(f"\nx = {x}")
    print("Direct result:", direct)
    print("Stable result:", stable)





#my own example

import numpy as np

# Example 1: Floating-point comparison
calculated = 0.5 + 0.3
expected = 0.8

print("0.5 + 0.3 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance comparison:", np.isclose(calculated, expected))


# Example 2: Absolute and relative error
true_value = np.sqrt(5)
approx_value = 2.236

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nAbsolute error:", round(absolute_error, 8))
print("Relative error:", f"{relative_error:.4%}")


# Example 3: Direct and stable formulas
for x in [1e-3, 1e-6, 1e-9]:

    direct = (np.sqrt(1 + x) - 1) / x

    stable = 1 / (np.sqrt(1 + x) + 1)

    print(f"\nx = {x}")
    print("Direct result:", direct)
    print("Stable result:", stable)

