
from gerrytools.plotting import latex
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def term(x, n, rule, exponent, coefficient):
    return np.real(rule(x)**exponent(n) * coefficient(n))

def power(X, N, rule, exponent, coefficient):
    """
    Create a 2d array of values for the power series following the provided
    parameters.
    """
    sequences = []
    # Compute the terms of the series for each x.
    for x in X:
        sequences.append([np.power(rule(x), exponent(n))*coefficient(n) for n in N]) 

    return sequences

# Create rules.
rule = lambda x: x
exponent = lambda n: n
coefficient = lambda n: 1

# Set ranges of values.
X = np.linspace(-8, 8, 100)
N = np.linspace(1, 10, 100)
# S = power(X, N, rule, exponent, coefficient)

# Compute the ratios of really large terms, and create a "target."
ratios = [
    term(x, 101, rule, exponent, coefficient)/term(x, 100, rule, exponent, coefficient)
    for x in X
]

# Create the plot, and turn on tex.
fig, ax = plt.subplots()
plt.rcParams["text.usetex"] = True

# Plot the ratios.
ax.plot(X, ratios)

# Create the target.
ax.axhline(1, color="k", alpha=1/2)
ax.axhline(-1, color="k", alpha=1/2)
ax.axvline(1, color="k", alpha=1/2)
ax.axvline(-1, color="k", alpha=1/2)

# Create the target.
target = Rectangle((-1,-1), 2, 2, facecolor=latex["Amber"], alpha=1/2)
ax.add_patch(target)

# Set ticks.
xticks = list(range(-2, 3))
yticks = xticks
ax.set_xticks(xticks, [rf"${str(t)}$" for t in xticks])
ax.set_yticks(yticks, [rf"${str(t)}$" for t in yticks])

# Set limits.
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

plt.savefig("geometric-series-root-test.pdf", bbox_inches="tight", dpi=300)
