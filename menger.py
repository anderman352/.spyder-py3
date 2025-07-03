# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:21:21 2023

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the range of the cube to plot.
xmin = -1.0
xmax = 1.0
ymin = -1.0
ymax = 1.0
zmin = -1.0
zmax = 1.0

# Define the number of iterations to use.
max_iterations = 255

# Create a NumPy array to store the pixel values.
image = np.zeros((512, 512, 512), dtype=np.uint8)

# Iterate over all the pixels in the image.
for x in range(512):
    for y in range(512):
        for z in range(512):
            # Convert the pixel coordinates to a point in the cube.
            p = np.array([xmin + (x / 512.0) * (xmax - xmin), ymin + (y / 512.0) * (ymax - ymin), zmin + (z / 512.0) * (zmax - zmin)])

            # Iterate over the number of iterations.
            for i in range(max_iterations):
                # Check if the point is in the sponge.
                if is_in_menger_sponge(p):
                    break

            # Color the pixel based on the number of iterations.
            image[y, x, z] = int(255 - (i / max_iterations) * 255)

# Plot the image.
plt.imshow(image, cmap="gray")
plt.show()

# Function to check if a point is in the Menger sponge.
def is_in_menger_sponge(p):
    # Check if the point is outside the cube.
    if any(p < xmin) or any(p > xmax):
        return False

    # Check if the point is in the interior of the cube.
    if all(abs(p) < 1.0):
        return True

    # Check if the point is in one of the 27 smaller cubes.
    return any(is_in_menger_sponge(p / 3) for p in [[p[0] - 1, p[1] - 1, p[2] - 1], [p[0] - 1, p[1] - 1, p[2]], [p[0] - 1, p[1], p[2] - 1], [p[0] - 1, p[1], p[2]], [p[0] - 1, p[1] + 1, p[2] - 1], [p[0] - 1, p[1] + 1, p[2]], [p[0], p[1] - 1, p[2] - 1], [p[0], p[1] - 1, p[2]], [p[0], p[1], p[2] - 1], [p[0], p[1], p[2]], [p[0], p[1] + 1, p[2] - 1], [p[0], p[1] + 1, p[2]], [p[0] + 1, p[1] - 1, p[2] - 1], [p[0] + 1, p[1] - 1, p[2]], [p[0] + 1, p[1], p[2] - 1], [p[0] + 1, p[1], p[2]], [p[0] + 1, p[1] + 1, p[2] - 1], [p[0] + 1, p[1] + 1, p[2]]])
