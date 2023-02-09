
import matplotlib.pyplot as plt
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

# Set ticks.
ax.set_xticks(x)
ax.set_yticks([1])
ax.set_xlim(0, 21)

# Remove and reposition spines.
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# Set aspect ratio.
# ax.set_aspect(16/9)

plt.savefig("figures/1n.pdf", dpi=300, bbox_inches="tight")
