import numpy as np
from scipy.integrate import simpson
# Smart-meter readings taken every two hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)
print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference between estimates: {abs(energy_simpson-energy_trapezoid):.3f} kWh")


#A water-flow monitoring system records the flow rate every 2 hours.
#Time: 0, 2, 4, 6, 8, 10, 12 hours.
#Flow rate: 2.0, 2.5, 3.0, 3.8, 3.5, 2.8, 2.2 litres/second.



import numpy as np
from scipy.integrate import simpson

# Water flow readings
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)

flow_rate = np.array([2.0, 2.5, 3.0, 3.8, 3.5, 2.8, 2.2])

# Convert hours to seconds
time_seconds = time_hours * 3600

# Trapezoidal rule
volume_trapezoid = np.trapezoid(flow_rate, time_seconds)

# Simpson's rule
volume_simpson = simpson(flow_rate, x=time_seconds)

# Calculate difference
difference = abs(volume_simpson - volume_trapezoid)

# Display results
print(f"Volume using trapezoidal rule: {volume_trapezoid:.3f} litres")
print(f"Volume using Simpson's rule: {volume_simpson:.3f} litres")
print(f"Difference between estimates: {difference:.3f} litres")


