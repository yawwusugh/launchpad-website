
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
x = np.linspace(0, 10, 100)
y = [1/2*math.sin(2*n) + 1 for n in x]

# Plotting!
ax.scatter(x, y, **style)

# Remove and reposition spines.
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# Set ticks.
ax.set_xticks(list(range(0, 11)))
ax.set_yticks([1, 2])
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 2)

ax.axvspan(xmin=1, xmax=11, ymin=1/3, ymax=2/3, color=latex["Apple green"], alpha=1/2, zorder=-1000)
ax.hlines(y=2/3, xmin=1, xmax=11, color=latex["Amber"], zorder=-1000)
ax.hlines(y=4/3, xmin=1, xmax=11, color=latex["Amber"], zorder=-1000)

# Plot epsilon
distance = FancyArrowPatch((1, 2/3), (1, 4/3), arrowstyle=']-[', linewidth=1)
ax.add_patch(distance)
ax.text(0.8, 1, "$\epsilon$", ha="center", va="center")

plt.savefig("figures/sequence-cauchy-nothing.pdf", dpi=300, bbox_inches="tight")
