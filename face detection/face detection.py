import cv2
import face_recognition

def detect_faces_and_landmarks_from_camera():
    # Open the default camera (0) or specify the camera index if you have multiple cameras
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Find face locations in the frame
        face_locations = face_recognition.face_locations(frame)

        # Find facial landmarks for each detected face
        face_landmarks_list = face_recognition.face_landmarks(frame)

        for face_location, face_landmarks in zip(face_locations, face_landmarks_list):
            # Convert the face location from (top, right, bottom, left) to (top, left, width, height)
            top, right, bottom, left = face_location
            width = right - left
            height = bottom - top

            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw facial landmarks on the frame
            for landmark_type, landmark_points in face_landmarks.items():
                for x, y in landmark_points:
                    cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

        # Display the frame with detected faces and facial landmarks
        cv2.imshow("Face Detection and Landmark Detection", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_faces_and_landmarks_from_camera()