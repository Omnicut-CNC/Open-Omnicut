import cv2
from numpy import sqrt
import numpy as np

lower_yellow = np.array([20, 90, 100])
upper_yellow = np.array([40, 255, 255])

track = None
picture = None

def process_frame(frame, middle):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    kernel = np.ones((8, 8), np.uint8)
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            ellipse = cv2.fitEllipse(contour)
            cv2.ellipse(frame, ellipse, (0, 0, 255), 2)
            rect = cv2.boundingRect(contour)
            cv2.line(frame, (int(rect[0]+rect[2]/2), int(rect[1]+rect[3]/2)), (int(frame.shape[1]/2), int(frame.shape[0]/2)), (255, 0, 0), 2)
            cv2.line(frame, (int(rect[0]+rect[2]/2), int(frame.shape[0]/2)), (int(frame.shape[1]/2), int(frame.shape[0]/2)), (0, 255, 0), 2)
            cv2.line(frame, (int(frame.shape[1]/2), int(rect[1]+rect[3]/2)), (int(frame.shape[1]/2), int(frame.shape[0]/2)), (0, 255, 0), 2)
            Xoffset = abs(rect[0]+rect[2]/2-middle[0])
            Yoffset = abs(rect[1]+rect[3]/2-middle[1])
            if picture and sqrt(Xoffset**2 + Yoffset**2) < 30:
                cv2.putText(frame, "X centered!", (0, 50), fontFace=20, fontScale=1, color=(0, 0, 0))
                cv2.putText(frame, "Y centered!", (0, 100), fontFace=20, fontScale=1, color=(0, 0, 0))
                cv2.imwrite('centered wheel.png', frame)
            else:
                if Xoffset > 15:
                    cv2.putText(frame, f"X is off by {Xoffset}!", (0, 50), fontFace=20, fontScale=1, color=(0, 0, 0))
                else:
                    cv2.putText(frame, f"X is centered!", (0, 50), fontFace=20, fontScale=1, color=(0, 0, 0))

                if Yoffset > 15:
                    cv2.putText(frame, f"Y is off! by {Xoffset}!", (0, 100), fontFace=20, fontScale=1, color=(0, 0, 0))

                else:
                    cv2.putText(frame, f"Y is centered!", (0, 100), fontFace=20, fontScale=1, color=(0, 0, 0))

    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    cv2.circle(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)), 10, (0, 0, 255), 2)
    processed_frame = process_frame(frame, (frame.shape[1]/2, frame.shape[0]/2))
    cv2.imshow('Density Map with Ellipse', processed_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()