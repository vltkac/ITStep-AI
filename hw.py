import cv2


cap = cv2.VideoCapture('meter.mp4')

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

writer = cv2.VideoWriter('meter_binar.mp4', fourcc, fps, (width // 2, height // 2), isColor=False)

while True:
    success, frame = cap.read()

    if not success:
        break

    if cv2.waitKey(20) & 0xFF == 27:
        break

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 1)
    gray_frame = cv2.bilateralFilter(gray_frame, 9, 75, 75)

    gray_frame = cv2.adaptiveThreshold(gray_frame,
                                255,
                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY,
                                11,
                                2
                            )

    cv2.imshow('meter_binar.mp4', gray_frame)
    writer.write(gray_frame)


cap.release()
writer.release()