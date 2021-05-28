import numpy as np
import cv2

img = cv2.imread('pics/soccer_practice.jpg', 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
template = cv2.imread('pics/shoe.png', 0)
template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)
h, w = template.shape

# metody template matching SQMETHODS używaja min val, reszta max value
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    cv2.rectangle(img2, location, (location[0] + w, location[1] + h), (250, 0, 0))
    cv2.imshow("Image", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
