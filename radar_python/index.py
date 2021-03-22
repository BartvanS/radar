import cv2 as cv
import numpy as np
W = 400
def my_line(img, start, end):
    thickness = 2
    line_type = 8
    cv.line(img,
            start,
            end,
            (0, 0, 0),
            thickness,
            line_type)
rook_window = "Drawing 2: Rook"
# Create black empty images
size = W, W, 3
rook_image = np.zeros(size, dtype=np.uint8)
# cv.rectangle(rook_image,
#               (0, 7 * W // 8),
#               (W, W),
#               (0, 255, 255),
#               -1,
#               8)
# #  2.c. Create a few lines
my_line(rook_image, (0, 15 * W // 16), (W, 15 * W // 16))
# my_line(rook_image, (W // 4, 7 * W // 8), (W // 4, W))
# my_line(rook_image, (W // 2, 7 * W // 8), (W // 2, W))
# my_line(rook_image, (3 * W // 4, 7 * W // 8), (3 * W // 4, W))
cv.imshow(rook_window, rook_image)
cv.moveWindow(rook_window, W, 200)
cv.waitKey(0)
cv.destroyAllWindows()