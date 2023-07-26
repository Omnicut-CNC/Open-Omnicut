import cv2
from numpy import sqrt
import numpy as np

def process_frame(frame, middle):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 90, 100])
    upper_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    kernel = np.ones((8, 8), np.uint8)
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            ellipse = cv2.fitEllipse(contour)
            cv2.ellipse(frame, ellipse, (0, 0, 255), 2)
            rect = cv2.boundingRect(contour)
            if sqrt((rect[0]+rect[2]/2-middle[0])**2 + (rect[1]+rect[3]/2-middle[1])**2) < 30:
                cv2.imwrite('centered wheel.png', frame)

    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = process_frame(frame, (frame.shape[1]/2, frame.shape[0]/2))
    cv2.imshow('Density Map with Ellipse', cv2.flip(processed_frame, 1))

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()