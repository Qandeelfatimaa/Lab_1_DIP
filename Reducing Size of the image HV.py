import matplotlib.pyplot as plt
import cv2

try:
    # Read image from disk.
    img = cv2.imread("Moro_Sindh HV.tif")

    # Get number of pixel horizontally and vertically.
    (height, width) = img.shape[:2]

    # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
    # is used for zooming.
    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

    # Write image back to disk.
    cv2.imwrite('result.tiff', res)

    plt.imshow(res)
    plt.show()

except IOError:
    print('Error while reading files !!!')
