import cv2
import numpy as np


valley_orig = cv2.imread('darken.png')

#  застосуйте вирівнювання гістограм

valley_hsv_pre_eq = cv2.cvtColor(valley_orig, cv2.COLOR_BGR2HSV)
img_value_pre_eq = valley_hsv_pre_eq[:, :, 2]
v_equalized = cv2.equalizeHist(img_value_pre_eq)
valley_hsv_pre_eq[:, :, 2] = v_equalized

valley_brg_equalized = cv2.cvtColor(valley_hsv_pre_eq, cv2.COLOR_HSV2BGR)

# збільшіть значення десь на 20-50%, оскільки тут
# результат буде типу float32 та явно вийде за межі [0-255]
# застосуйте np.clip(value, 0, 255) та value.astype(np.uint8)

valley_hsv = cv2.cvtColor(valley_orig, cv2.COLOR_BGR2HSV)
img_value = valley_hsv[:, :, 2]

value_new = np.clip(img_value * 1.5, 0, 255).astype(np.uint8)
valley_hsv[:, :, 2] = value_new
valley_brg_new = cv2.cvtColor(valley_hsv, cv2.COLOR_HSV2BGR)

# Виведіть результати обох обробок на екран

cv2.imshow('equalized image', valley_brg_equalized)
cv2.imshow('50% brightened image', valley_brg_new)
cv2.waitKey(0)