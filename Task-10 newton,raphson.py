
from scipy.optimize import root_scalar

# Initial investment followed by annual cash inflows
cash_flows = [-10000, 3000, 3500, 4000, 2500]

# Define Net Present Value (NPV)
def npv(rate):
    return sum(
        cf / (1 + rate)**t
        for t, cf in enumerate(cash_flows)
    )

# Derivative of NPV
def d_npv(rate):
    return sum(
        -t * cf / (1 + rate)**(t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

# Newton-Raphson method
newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.10,
    method="newton",
    xtol=1e-12
)

# Secant method
secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant",
    xtol=1e-12
)

# Display results
print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")

#my own example
#A business invests KSh 15,000 initially and receives the following annual cash inflows:
# Year 1: KSh 4,000
# Year 2: KSh 5,000
# Year 3: KSh 6,000
# Year 4: KSh 4,000

from scipy.optimize import root_scalar

# Initial investment and annual cash inflows
cash_flows = [-15000, 4000, 5000, 6000, 4000]

# Define NPV function
def npv(rate):
    return sum(
        cf / (1 + rate)**t
        for t, cf in enumerate(cash_flows)
    )

# Define derivative of NPV
def d_npv(rate):
    return sum(
        -t * cf / (1 + rate)**(t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

# Newton-Raphson method
newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.10,
    method="newton",
    xtol=1e-12
)

# Secant method
secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant",
    xtol=1e-12
)

# Display results
print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")
