
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, ArrowStyle
import numpy as np
import math
from gerrytools.plotting import latex

# Create a default set of arguments for point styles and ticks.
style = dict(
    s=8, c=latex["Amethyst"]
)

# Set font.
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "\sffamily"
})

# Create a plot of the geometric sequence 1/n.
fig, ax = plt.subplots(figsize=(7,3))
x = np.linspace(0, 25, 200)
y = [math.sin(math.pi*n/2)*math.exp((-1/10)*n) + math.pi/2 for n in x]

# Plotting!
ax.scatter(x, y, **style)

# Remove and reposition spines.
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# Set ticks.
ax.set_xticks(list(range(1, 26)))
ax.set_yticks([0, math.pi/2, math.pi], [0, r"$\frac{\pi}{2}$", "$\pi$"])
ax.set_ylim(-0.01, math.pi+0.5)
ax.set_xlim(0, 25.5)

plt.savefig("figures/sequence-cauchy-converges.pdf", dpi=300, bbox_inches="tight")
