import cv2
import numpy as np
from matplotlib import pyplot as plt

M = np.float32([[1, 0, 100], [0, 1, 50]])
try:
    # Read image from disk.
    img = cv2.imread("Moro_Sindh HH.tif")

    # warpAffine does appropriate shifting given the
    # translation matrix.
    res2 = cv2.warpAffine(img, M, (50, 75))

    # Write image back to disk.
    cv2.imwrite('result.tiff', res2)

    plt.imshow(res2)
    plt.show()

except IOError:
    print('Error while reading files !!!')
