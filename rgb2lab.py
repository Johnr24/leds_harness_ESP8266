import colour
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from scipy import stats

# Function to convert a single RGB color to L* in LAB
def rgb_single_to_L_star(r, g, b):
    rgb = np.array([r, g, b]) / 255
    xyz = colour.sRGB_to_XYZ(rgb)
    lab = colour.XYZ_to_Lab(xyz)
    return lab[0]

# Generate a range of brightness values from 0 to 255
brightness_range = np.arange(0, 256)

# Initialize lists to hold L* values for each primary color
L_star_reds = []
L_star_greens = []
L_star_blues = []

# Calculate L* values across the brightness range for each primary color
for brightness in brightness_range:
    L_star_reds.append(rgb_single_to_L_star(brightness, 0, 0))
    L_star_greens.append(rgb_single_to_L_star(0, brightness, 0))
    L_star_blues.append(rgb_single_to_L_star(0, 0, brightness))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(brightness_range, L_star_reds, 'r', label='Red')
plt.plot(brightness_range, L_star_greens, 'g', label='Green')
plt.plot(brightness_range, L_star_blues, 'b', label='Blue')

plt.legend()
plt.title('Brightness (L*) of RGB Primaries across RGB Values')
plt.xlabel('RGB Value')
plt.ylabel('L* (Brightness)')
plt.grid(True)
plt.show()