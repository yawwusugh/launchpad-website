
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

# Add lines.
ax.hlines(math.pi/4, xmin=2, xmax=26, color=latex["Amber"], zorder=-1000)
ax.hlines(3*math.pi/4, xmin=2, xmax=26, color=latex["Amber"], zorder=-1000)
ax.axvspan(xmin=2, xmax=26, ymin=1/4, ymax=3/4, color=latex["Apple green"], zorder=-10000, alpha=1/2)

# Remove and reposition spines.
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# Set ticks.
ax.set_xticks(list(range(1, 26)))
ax.set_yticks([0, math.pi/2, math.pi], [0, r"$\frac{\pi}{2}$", "$\pi$"])
ax.set_ylim(-0.01, math.pi)
ax.set_xlim(0, 25.5)

# Remove and reposition spines.
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# Annotate a_N.
ax.text(3, 7/4, "$a_N$")
style = ArrowStyle("Fancy", head_width=4, head_length=4)
pointer = FancyArrowPatch((3, 7/4), (2, math.pi/2), facecolor=None, arrowstyle=style)
ax.add_patch(pointer)

# Plot epsilon
distance = FancyArrowPatch((1.8, math.pi/4), (1.8, 3*math.pi/4), arrowstyle=']-[', linewidth=1)
ax.add_patch(distance)
ax.text(1.5, 1/2*math.pi, "$\epsilon$", ha="center", va="center")

# Annotate a_N.
ax.text(5, 2.75, "$a_5$")
style = ArrowStyle("Fancy", head_width=4, head_length=4)
pointer = FancyArrowPatch((5, 2.75), (5, 2.177), facecolor=None, arrowstyle=style)
ax.add_patch(pointer)

# Annotate a_N.
ax.text(7.2, 1/2, "$a_7$")
style = ArrowStyle("Fancy", head_width=4, head_length=4)
pointer = FancyArrowPatch((7, 1/2), (7, 1.074), facecolor=None, arrowstyle=style)
ax.add_patch(pointer)


plt.savefig("figures/sequence-cauchy-converges-annotated.pdf", dpi=300, bbox_inches="tight")
