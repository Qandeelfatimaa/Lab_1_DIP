import cv2
from matplotlib import pyplot as plt

try:
    # Read image from disk.
    img = cv2.imread("Moro_Sindh HV.tif")

    # Shape of image in terms of pixels.
    (rows, cols) = img.shape[:2]

    # getRotationMatrix2D creates a matrix needed for transformation.
    # We want matrix for rotation w.r.t center to 45 degree without scaling.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res1 = cv2.warpAffine(img, M, (cols, rows))

    # Write image back to disk.
    cv2.imwrite('result.tiff', res1)

    plt.imshow(res1)
    plt.show()

except IOError:
    print('Error while reading files !!!')

