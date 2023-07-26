import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break
    lower_yellow = (20, 100, 100)
    upper_yellow = (40, 255, 255)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    x1 = 10000000
    y1 = 10000000
    x2 = -1
    y2 = -1
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if x < x1:
            x1 = x

        if y < y1:
            y1 = y

        if x+w > x2:
            x2 = x+w

        if y+h > y2:
            y2 = y+h

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('Object Detection', cv2.flip(frame, 1))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()