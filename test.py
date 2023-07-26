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

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        print("Detected object coordinates: x={}, y={}, width={}, height={}".format(x, y, w, h))
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Object Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()