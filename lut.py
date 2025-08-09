import colour
import matplotlib.pyplot as plt
import numpy as np

# Function to convert RGB to L* in LAB
def rgb_to_L_star(rgb):
    rgb = np.array(rgb) / 255
    xyz = colour.sRGB_to_XYZ(rgb)
    lab = colour.XYZ_to_Lab(xyz)
    return lab[0]

# Generate L* values for the blue channel
blue_values = np.arange(256)
blue_L_star = [rgb_to_L_star([0, 0, b]) for b in blue_values]

# Initialize the LUT for red and green channels
lut_red = np.zeros_like(blue_values)
lut_green = np.zeros_like(blue_values)

# Function to find RGB value for red/green channel matching L* value
def find_matching_rgb(target_L_star, channel):
    for value in range(256):
        rgb = [0, 0, 0]
        rgb[channel] = value
        if np.isclose(rgb_to_L_star(rgb), target_L_star, atol=1):
            return value
    return 0

# Populate the LUT for red and green channels
for i, L_star in enumerate(blue_L_star):
    lut_red[i] = find_matching_rgb(L_star, 0)  # Red channel index is 0
    lut_green[i] = find_matching_rgb(L_star, 1)  # Green channel index is 1

# The LUTs lut_red and lut_green now map blue channel values to the red and green values with matching L* in LAB

import matplotlib.pyplot as plt

# Assuming lut_red and lut_green are already generated
blue_values = range(256)  # Blue channel values from 0 to 255

plt.figure(figsize=(10, 6))

# Plotting the LUT for the red channel
plt.plot(blue_values, lut_red, label='Red Channel LUT', color='red')

# Plotting the LUT for the green channel
plt.plot(blue_values, lut_green, label='Green Channel LUT', color='green')

# Convert adjusted RGB values back to LAB and extract L* values
adjusted_L_star_red = [rgb_to_L_star([lut_red[i], 0, i]) for i in blue_values]
adjusted_L_star_green = [rgb_to_L_star([0, lut_green[i], i]) for i in blue_values]
original_L_star_blue = [rgb_to_L_star([0, 0, i]) for i in blue_values]

# Plotting
plt.figure(figsize=(10, 6))

# Plotting the original L* values for the blue channel
plt.plot(blue_values, original_L_star_blue, label='Original Blue Channel L*', color='blue', linestyle='--')

# Plotting the adjusted L* values for the red and green channels
plt.plot(blue_values, adjusted_L_star_red, label='Adjusted Red Channel L*', color='red')
plt.plot(blue_values, adjusted_L_star_green, label='Adjusted Green Channel L*', color='green')

plt.title('L* Values in LAB Space for Adjusted RGB Channels')
plt.xlabel('Blue Channel Intensity')
plt.ylabel('L* Value')
plt.legend()
plt.grid(True)
plt.show()