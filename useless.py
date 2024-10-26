import cv2
import mediapipe as mp
import os

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Function to write coordinates to a text file
def save_landmarks_to_file(landmarks, file_path):
    try:
        with open(file_path, 'a') as f:
            # Create a single line of coordinates
            line = ','.join(f'{int(landmark.x * 1000)},{int(landmark.y * 1000)},{int(landmark.z * 1000)}' for landmark in landmarks)
            f.write(line + '\n')  # Write the line and add a newline at the end
        print(f"Saved landmarks to {file_path}.")
    except Exception as e:
        print(f"Error saving landmarks: {e}")

# Define the video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Path to save the coordinates
output_file_path = r'C:\Users\hp\Desktop\OpenCV\BodyDetection\pose_coordinates.txt'

# Create directory if it doesn't exist
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Delete existing file if it exists
if os.path.exists(output_file_path):
    os.remove(output_file_path)

# Loop through the frames of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect pose
    result = pose.process(rgb_frame)

    # If landmarks are detected
    if result.pose_landmarks:
        # Draw landmarks on the frame
        mp_drawing.draw_landmarks(
            frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Extract and save landmarks
        landmarks = result.pose_landmarks.landmark
        save_landmarks_to_file(landmarks, output_file_path)

        print(f"Detected {len(landmarks)} landmarks.")

    # Show the frame with landmarks
    cv2.imshow('Pose Tracking', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
