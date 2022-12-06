import numpy
import cv2
import matplotlib.pyplot as plp

img = cv2.imread("test_5bb_blancs.png")

cv2.imshow("Image originale", img)
cv2.waitKey(0)


def rgb_to_bw(img):
    nl = img.shape[0]
    nc = img.shape[1]
    IM = img[:, :, 0]
    for i in range(nl):
        for j in range(nc):
            IM[i, j] = (int(img[i, j, 0]) + int(img[i, j, 1]) + int(img[i, j, 2])) / 3

    return IM

IM = rgb_to_bw(img)


cv2.imshow("En noir et blanc", IM)
cv2.waitKey(0)

def histogramme(img):
    nl = img.shape[0]
    nc = img.shape[1]
    h = numpy.zeros(256)
    for i in range(nl):
        for j in range(nc):
            val = img[i, j]
            h[val] = h[val] + 1
    return h

h = histogramme(IM)
plp.stem(h)
plp.show()
plp.close("all")


def binarisation(img, seuil):
    nl = img.shape[0]
    nc = img.shape[1]
    for i in range(nl):
        for j in range(nc):
            if (img[i, j] > seuil):
                IM[i, j] = 255
            else:
                IM[i, j] = 0
    return IM

IM_bin = binarisation(IM, 100)

cv2.imshow("Image binarisee", IM_bin)
cv2.waitKey(0)
h_bin = histogramme(IM_bin)

plp.stem(h_bin)
plp.show()
plp.close("all")

nombre_pixels_blancs = 3994 

""" 
pour 3 bonbons, 3994 pixels/bonbon
"""

nombre_bonbons = h_bin[255]/(nombre_pixels_blancs-100)
print(nombre_bonbons)

"""
pour 1, +390
pour 3
pour 5, -100
pour 7 bonbons, on a environ 6.6 de determines, donc on diminue le nombre pixels bonbons -250
pour 9, 8.8 avec -250, donc -310
pour 11, -390
"""
def calibration():
    x1 = 1
    y1 = 390
    x2 = 11
    y2 = -390
    alpha = (y2 - y1)/(x2 - x1)
    beta = 3
    t = numpy.array(500)
    y = alpha*t - beta