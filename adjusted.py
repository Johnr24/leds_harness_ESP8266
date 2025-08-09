import colour
import matplotlib.pyplot as plt
import numpy as np

# Function to convert a single RGB color to L* in LAB
def rgb_single_to_L_star(r, g, b):
    rgb = np.array([r, g, b]) / 255
    xyz = colour.sRGB_to_XYZ(rgb)
    lab = colour.XYZ_to_Lab(xyz)
    return lab[0]

# Generate a range of brightness values from 0 to 255
brightness_range = np.arange(0, 255)

# Initialize lists to hold L* values for each primary color
L_star_reds = []
L_star_greens = []
L_star_blues = []

# Initialize lists to hold adjusted L* values for each primary color
L_star_reds_adjusted = []
L_star_greens_adjusted = []
L_star_blues_adjusted = []

# Adjusters for each RGB axis
red_adjuster = 0.71875
green_adjuster = 0.359375
blue_adjuster = 1.0

# Calculate L* values across the brightness range for each primary color
for brightness in brightness_range:
    L_star_reds.append(rgb_single_to_L_star(brightness, 0, 0))
    L_star_greens.append(rgb_single_to_L_star(0, brightness, 0))
    L_star_blues.append(rgb_single_to_L_star(0, 0, brightness))
    
    # Calculate adjusted L* values
    L_star_reds_adjusted.append(rgb_single_to_L_star(brightness * red_adjuster, 0, 0))
    L_star_greens_adjusted.append(rgb_single_to_L_star(0, brightness * green_adjuster, 0))
    L_star_blues_adjusted.append(rgb_single_to_L_star(0, 0, brightness * blue_adjuster))

# Function to calculate Delta E using CIE76 formula
def delta_E_CIE76(L1, a1, b1, L2, a2, b2):
    return np.sqrt((L1 - L2) ** 2 + (a1 - a2) ** 2 + (b1 - b2) ** 2)

# Initialize lists to hold Delta L* values
delta_L_star_reds = []
delta_L_star_greens = []

# Calculate Delta L* for each brightness value
for brightness in brightness_range:
    # Convert RGB to LAB for original and adjusted colors
    lab_red = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(np.array([brightness * red_adjuster, 0, 0]) / 255))
    lab_green = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(np.array([0, brightness * green_adjuster, 0]) / 255))
    lab_blue = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(np.array([0, 0, brightness * blue_adjuster]) / 255))
    
    # Calculate Delta L* for red and blue
    delta_L_star_reds.append(abs(lab_red[0] - lab_blue[0]))
    
    # Calculate Delta L* for green and blue
    delta_L_star_greens.append(abs(lab_green[0] - lab_blue[0]))

# Plotting Delta L* values
plt.figure(figsize=(12, 8))

plt.plot(brightness_range, delta_L_star_reds, 'r', label='Delta L* Red vs. Blue')
plt.plot(brightness_range, delta_L_star_greens, 'g', label='Delta L* Green vs. Blue')

plt.legend()
plt.title('Delta L* of Adjusted Red and Green vs. Blue')
plt.xlabel('RGB Value')
plt.ylabel('Delta L*')
plt.grid(True)
plt.show()



# Initialize lists to hold Delta L* values for original RGB
delta_L_star_reds_original = []
delta_L_star_greens_original = []

# Calculate Delta L* for each brightness value for original RGB
for brightness in range(256):  # Assuming 8-bit color depth
    # Convert original RGB to LAB
    lab_red_original = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(np.array([brightness, 0, 0]) / 255))
    lab_green_original = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(np.array([0, brightness, 0]) / 255))
    lab_blue_original = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(np.array([0, 0, brightness]) / 255))
    
    # Calculate Delta L* for red and blue original
    delta_L_star_reds_original.append(abs(lab_red_original[0] - lab_blue_original[0]))
    
    # Calculate Delta L* for green and blue original
    delta_L_star_greens_original.append(abs(lab_green_original[0] - lab_blue_original[0]))

# Plotting Delta L* values for original RGB
plt.figure(figsize=(12, 8))

plt.plot(range(256), delta_L_star_reds_original, 'r--', label='Delta L* Original Red vs. Blue')
plt.plot(range(256), delta_L_star_greens_original, 'g--', label='Delta L* Original Green vs. Blue')

plt.legend()
plt.title('Delta L* of Original RGB')
plt.xlabel('RGB Value')
plt.ylabel('Delta L*')
plt.grid(True)
plt.show()