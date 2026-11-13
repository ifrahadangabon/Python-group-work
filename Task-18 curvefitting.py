
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# PART 1: INTERPOLATION

# Hourly temperature measurements
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)

temperature = np.array(
    [18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0]
)

# Create interpolation methods
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Estimate every 10 minutes
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)

linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

# Estimate temperature at 10:30 AM
target_time = 10.5

print("INTERPOLATION RESULTS ")

print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")

print(f"Cubic estimate at 10:30: {float(cubic(target_time)):.2f} C")

# PART 2: CURVE FITTING
# Concurrent users and server response time
users = np.array(
    [50, 100, 150, 200, 250, 300, 350],
    dtype=float
)

response_ms = np.array(
    [82, 95, 115, 145, 185, 238, 305],
    dtype=float
)

# Quadratic mathematical model
def model(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the curve
parameters, covariance = curve_fit(
    model, users, response_ms
)

a, b, c = parameters

# Calculate predicted values
predicted = model(users, a, b, c)

# Calculate RMSE
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

print("\n CURVE FITTING RESULTS")

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")

print(f"RMSE: {rmse:.2f} ms")

print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")



# PART 3: DRAW BOTH GRAPHS

plt.figure(figsize=(12, 5))

# First graph: Interpolation
plt.subplot(1, 2, 1)

plt.scatter(hours, temperature, label="Hourly measurements")

plt.plot(ten_minute_times, linear_estimates, label="Linear")

plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")

plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation")
plt.legend()
plt.grid(True)


# Second graph: Curve fitting
plt.subplot(1, 2, 2)

x_plot = np.linspace(users.min(), 400, 300)

plt.scatter(users, response_ms, label="Measurements")

plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")

plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend()
plt.grid(True)


# Display both graphs
plt.tight_layout()
plt.show()







