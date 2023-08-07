import rasterio
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

a=rasterio.open("Moro_Sindh HH.tif")
img = Image.open("Moro_Sindh HH.tif")
width= a.width
height=a.height
num_bands = a.count

print("Image(HH) Size  (Width x Height):", width, "x", height)

print("Number of Bands of HH:", num_bands)


# Open the image
img = Image.open("Moro_Sindh HH.tif")

# Convert the image to a NumPy array
img_array = np.array(img)

# Calculate image statistics
mean = np.mean(img_array)
std_dev = np.std(img_array)
min = np.min(img_array)
max = np.max(img_array)

# Print the results
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Min:", min)
print("Max:", max)

width, height = img.size

# Print the results
print("Width:", width)
print("Height:", height)

plt.imshow(img)
plt.show()