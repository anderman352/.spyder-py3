# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:12:35 2023

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the range of the complex plane to plot.
xmin = -2.0
xmax = 1.0
ymin = -1.5
ymax = 1.5

# Define the number of iterations to use.
max_iterations = 255

# Create a NumPy array to store the pixel values.
image = np.zeros((512, 512), dtype=np.uint8)

# Iterate over all the pixels in the image.
for x in range(512):
    for y in range(512):
        # Convert the pixel coordinates to a complex number.
        c = complex(xmin + (x / 512.0) * (xmax - xmin), ymin + (y / 512.0) * (ymax - ymin))

        # Iterate over the number of iterations.
        for i in range(max_iterations):
            # Calculate the next value in the sequence.
            z = c ** 2 + c

            # If the sequence diverges, break.
            if abs(z) > 2.0:
                break

        # Color the pixel based on the number of iterations.
        image[y, x] = int(255 - (i / max_iterations) * 255)

# Plot the image.
plt.imshow(image, cmap="Blues")
plt.show()
