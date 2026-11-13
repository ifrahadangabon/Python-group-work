#Original problem → understand the code → change the situation → create a working solution.

#The program must:

#Store the 24 temperatures in a NumPy array.
#Calculate the daily mean (average).
#Find the minimum temperature.
#Find the maximum temperature.
#Convert every temperature from Celsius (°C) to Fahrenheit (°F).

#The important formula is:

#F = 1.8 × C + 32

import numpy as np

# 24 hourly temperature readings in degrees Celsius
temperatures_c = np.array([
    20.5, 18.0, 12.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    30.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Celsius-to-Fahrenheit conversion
temperatures_f = 1.8 * temperatures_c + 32

print(f"Daily mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print("First eight Fahrenheit readings:", temperatures_f[:8])

#my own example
# Instruction B:
# Input values: 24 hourly temperature readings in degrees Celsius.
# Mathematical operations: mean, minimum, maximum, and Celsius-to-Fahrenheit conversion.

# Instruction C:
# I changed the first temperature from 18.5 C to 20.5 C.
# The daily mean increased from 23.12 C to 23.20 C.
# The minimum and maximum temperatures remained the same.
# The first Fahrenheit reading changed from 65.3 F to 68.9 F.

# Instruction D:
# The daily mean represents the average temperature recorded during the 24-hour period.
# The minimum represents the lowest recorded temperature.
# The maximum represents the highest recorded temperature.
# The original readings are in Celsius, and the program converts them to Fahrenheit
# using the formula F = 1.8C + 32.



#The programming concept stays the same, but the real-world situation and input data are different.
# Instruction E:
# New real-world case: Greenhouse temperature monitoring.
# Assumption: A greenhouse records its temperature every hour for 24 hours.
# The temperatures are recorded in degrees Celsius


greenhouse_c =np.array([20.5, 19.0, 19.5, 18.5, 18.8, 17.9,
                         20.2, 22.5, 20.5, 17.9, 17.8, 17.5,
                          20.2, 19.0, 20.0, 17.5, 22.0, 30.5, 
                          20.0, 23.0, 20.6, 20.5,22.9,30.0, ])


greenhouse_mean =np.mean(greenhouse_c)
greenhouse_max=np.max(greenhouse_c)
greenhouse_min=np.min(greenhouse_c)

greenhouse_f=1.8*greenhouse_c+32

print("\nGreenhouse Result")
print(f"mean temperature:{greenhouse_mean:.2f}C")
print(f"maximum temperature:{greenhouse_max:.2f}C")
print(f"minimum temperature:{greenhouse_min:.2f}C")
print("First ten farhenheit readings:",greenhouse_c[2:6])






