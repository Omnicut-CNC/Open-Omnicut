import cv2

cap = cv2.VideoCapture(0)

object_detector = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    mask = object_detector.apply(frame)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 100:
            cv2.drawContours(frame, [cnt],-1, (0, 255, 0), 2)


    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()