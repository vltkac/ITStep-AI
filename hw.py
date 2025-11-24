import cv2
import numpy as np


orig = cv2.imread('sonet.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('orig', orig)

# розмиття або наведення різкості

kernel_sharp = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

orig_sharp = cv2.filter2D(orig,
                       -5,
                       kernel_sharp
                       )

cv2.imshow("orig_sharp", orig_sharp)


blurred_orig = cv2.GaussianBlur(orig_sharp,
                                ksize=(3, 3),
                                sigmaX=5)

cv2.imshow('blurred_orig', blurred_orig)
#
# # адаптивна бінарізація
#
adapted = cv2.adaptiveThreshold(blurred_orig,
                                255,
                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY,
                                11,
                                2.1,
                                )

cv2.imshow('adapted', adapted)
#
# # очищеня шумів
#
adapt_bilateral = cv2.bilateralFilter(adapted,
                              d=11,
                              sigmaColor=75,
                              sigmaSpace=75,
                              )

cv2.imshow("adapt_bilateral", adapt_bilateral)

cv2.waitKey(0)