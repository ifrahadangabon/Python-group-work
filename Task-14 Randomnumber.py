
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0

N = 100_000

# Generate random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)

# Check overloaded cases
overloaded = demand > capacity

# Calculate overload probability
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Running probability
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

# Plot convergence graph
plt.semilogx(
    indices + 1,
    running_probability[indices]
)

plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.grid(True)

plt.show()






#Practice example: Estimating water shortage risk

#A water storage tank has a maximum capacity of 2,000 litres. The average daily water demand is 1,700 litres, with a standard deviation of 250 litres.

#Write a Python program using Monte Carlo Simulation to:
1.# Generate 100,000 random water-demand scenarios.
2. #Check how many scenarios exceed the tank capacity.
3. #Calculate the probability of water shortage.
4. #Print the estimated probability and number of shortage cases.
5. #Plot a graph showing how the estimated probability changes as simulations increase.



import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

capacity = 2000.0
mean_demand = 1700.0
std_demand = 250.0

N = 100_000

# Generate random demand
demand = rng.normal(mean_demand, std_demand, N)

# Check shortage cases
shortage = demand > capacity

# Calculate probability
shortage_probability = shortage.mean()

print(f"Estimated shortage probability: {shortage_probability:.4%}")
print(f"Number of shortage cases: {shortage.sum()} out of {N}")

# Running probability
running_probability = np.cumsum(shortage) / np.arange(1, N + 1)

# Plot graph
plt.plot(running_probability)
plt.xlabel("Number of simulations")
plt.ylabel("Estimated shortage probability")
plt.title("Monte Carlo estimate of water shortage risk")
plt.grid(True)
plt.show()
