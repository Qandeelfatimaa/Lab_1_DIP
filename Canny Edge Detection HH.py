import cv2
from matplotlib import pyplot as plt
try:
    # Read image from disk.
    img = cv2.imread("Moro_Sindh HH.tif")
    # Canny edge detection.
    edges = cv2.Canny(img, 15, 10)
    # Write image back to disk.
    cv2.imwrite('result.tiff', edges)
    plt.imshow(edges)
    plt.show()
except IOError:
    print('Error while reading files !!!')

