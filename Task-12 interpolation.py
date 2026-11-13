
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

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

print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(target_time)):.2f} C")

# Draw graph
plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")

plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation")
plt.legend()
plt.grid(True)
plt.show()



#my own example
#Temperature interpolation
#A weather station records the following temperatures at different hours:
#Hour	Temperature (°C)
#7    	16.0
#8	    18.5
#9	     21.0
#10	     23.0
#11	     24.5
#12	      25.0
#13     	24.0

import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Hourly measurements
hours = np.array([7, 8, 9, 10, 11, 12, 13], dtype=float)

temperature = np.array(
    [16.0, 18.5, 21.0, 23.0, 24.5, 25.0, 24.0]
)

# Create interpolation methods
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Estimate every 15 minutes
times = np.arange(7, 13 + 0.25, 0.25)

# Calculate estimates
linear_estimates = linear(times)
cubic_estimates = cubic(times)

# Estimate temperature at 9:30 AM
target_time = 9.5

print("Linear estimate:", float(linear(target_time)))
print("Cubic estimate:", float(cubic(target_time)))

# Draw graph
plt.scatter(hours, temperature, label="Measurements")
plt.plot(times, linear_estimates, label="Linear")
plt.plot(times, cubic_estimates, label="Cubic spline")

plt.xlabel("Hour")
plt.ylabel("Temperature")
plt.title("Temperature interpolation")
plt.legend()
plt.grid(True)
plt.show()
