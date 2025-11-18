import cv2

# Завдання 1
# Відкрийте зображення data/Lenna.png. Прочитайте маски
# data/mask1.png та data/mask2.png

image_lenna = cv2.imread('Lenna.png')
mask1 = cv2.imread('mask1.png', cv2.IMREAD_GRAYSCALE)
mask2 = cv2.imread('mask2.png', cv2.IMREAD_GRAYSCALE)

# Виведіть ту частину зображення, яка відповідає:
# mask1
# mask2
# mask1 і mask2

result1 = cv2.bitwise_and(image_lenna, image_lenna, mask=mask1)
result2 = cv2.bitwise_and(image_lenna, image_lenna, mask=mask2)
cv2.imshow('Result Mask 1', result1)
cv2.imshow('Result Mask 2', result2)

combined_mask = cv2.bitwise_or(mask1, mask2)
result_combined = cv2.bitwise_and(image_lenna, image_lenna, mask=combined_mask)
cv2.imshow('Result Combined Mask', result_combined)

cv2.waitKey(0)

# Завдання 2
# Виведіть зображення. Підберіть самостійно межі

baboo_img = cv2.imread('baboo.jpg', cv2.IMREAD_GRAYSCALE)
eyes_img = baboo_img[10:45, 55:210]
cv2.imshow('Baboo Eyes', eyes_img)
cv2.waitKey(0)