
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, ArrowStyle
import numpy as np
import math
from gerrytools.plotting import latex

# Create a default set of arguments for point styles and ticks.
style = dict(
    s=16, c=latex["Amethyst"]
)

# Set font.
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "\sffamily"
})

# Create a plot of the geometric sequence 1/n.
fig, ax = plt.subplots(figsize=(7,3))
x = list(range(1,21))
y = [1/n for n in x]

# Plotting!
ax.scatter(x, y, **style)

# Remove and reposition spines.
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# Plot epsilon
ax.hlines(1/10, -10, 25, color=latex["Amber"], zorder=-1000)
distance = FancyArrowPatch((9.8, 0), (9.8, 1/10), arrowstyle=']-[', linewidth=1/2)
ax.add_patch(distance)
ax.text(9.6, 1/20, "$\epsilon$", ha="center", va="center")

# Annotate a_10.
ax.text(12, 1/5, "$a_N$")
style = ArrowStyle("Fancy", head_width=4, head_length=4)
pointer = FancyArrowPatch((12, 1/5), (10.15, 1/10), facecolor=None, arrowstyle=style)
ax.add_patch(pointer)
plt.axvspan(xmin=10, xmax=25, ymin=1/25, ymax=1/8, color=latex["Apple green"], alpha=1/4, zorder=-1000)

# Set ticks.
ax.set_xticks(x)
ax.set_yticks([1])
ax.set_xlim(0, 21)

plt.savefig("figures/1n-epsilon.pdf", dpi=300, bbox_inches="tight")
