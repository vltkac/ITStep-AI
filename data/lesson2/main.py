# Завдання 1
# Відкрийте зображення data/lesson2/marbles.png.
# Використайте кольорову сегментацію для отримання масок до
# кульок:
#  синього кольору


# import cv2


# marbles_orig = cv2.imread('marbles.png')
# cv2.imshow('original', marbles_orig)

# marbles_hsv = cv2.cvtColor(marbles_orig, cv2.COLOR_BGR2HSV)
# blue_mask = cv2.inRange(marbles_hsv, (90, 220, 10), (125, 255, 255))
# cv2.imshow('blue mask', blue_mask)
# h: 90-125, s: 220-255, v: 10-255

# blue_mask = blue_mask.astype(bool)

# marbles_orig[blue_mask] = 255

# cv2.imshow('white blue', marbles_orig)

#  зеленого і червоного
# green_mask = cv2.inRange(marbles_hsv, (50, 200, 10), (70, 255, 255))
# h: 50-70, s: 200-255, v: 10-255
# red_orange_mask = cv2.inRange(marbles_hsv, (0, 200, 30), (5, 255, 255))
# h: 0-5, s: 200-255, v: 20-255
# red_blue_mask = cv2.inRange(marbles_hsv, (175, 200, 30), (180, 255, 255))
# h: 175-180, s: 200-255, v: 20-255
# red_mask = cv2.bitwise_or(red_orange_mask, red_blue_mask)
# red_green_mask = cv2.bitwise_or(red_mask, green_mask)

# grey_marbles = cv2.cvtColor(marbles_orig, cv2.COLOR_BGR2GRAY)
# cv2.imshow('grey img', grey_marbles)

#  білого
# white_mask = cv2.inRange(grey_marbles, 210, 255)

#  чорного
# black_mask = cv2.inRange(grey_marbles, 0, 15)

# cv2.imshow('red org mask', red_orange_mask)
# cv2.imshow('red blue mask', red_blue_mask)
# cv2.imshow('red', red_mask)
# cv2.imshow('green mask', green_mask)
# cv2.imshow('red green mask', red_green_mask)
# cv2.imshow('black mask', black_mask)
# cv2.imshow('white mask', white_mask)
# cv2.waitKey(0)