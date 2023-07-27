import cv2

def detect_head_from_camera():
    # Load the Haar cascade model for head detection
    head_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"/haarcascade_frontalface_default.xml")

    cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or change to the camera index if multiple cameras are connected
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from the camera.")
            break

        # Convert the frame to grayscale for head detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect heads in the frame using the head cascade model
        heads = head_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        # Draw bounding boxes around the detected heads
        for (x, y, w, h) in heads:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with bounding boxes
        cv2.imshow("Head Detection", frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

# Usage example:
detect_head_from_camera()