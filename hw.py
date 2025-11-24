# Завдання 2
# Відкрийте відео з файлу data\lesson7\text.mp4. Проведіть
# бінарізацію кадрів та збережіть в новий файл.


import cv2


cap = cv2.VideoCapture('text.mp4')

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(width * 0.5))
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height * 0.5))

writer = cv2.VideoWriter(
    'new_text.mp4',  # шлях до файлу
    fourcc,        # кодек
    fps,
    (width // 2, height // 2),
    isColor=False   # чи кадри кольорові
)


while True:
    success, img = cap.read()

    if not success:
        break

    img = cv2.resize(img, None, fx=0.5, fy=0.5)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.GaussianBlur(img, (9, 9), 1)
    img = cv2.bilateralFilter(img, 7, 75, 75)

    img = cv2.adaptiveThreshold(img,
                                255,
                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY,
                                11,
                                4
                            )


    cv2.imshow('orig', img)

    writer.write(img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
writer.release()