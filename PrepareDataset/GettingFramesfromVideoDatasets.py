import cv2

# Load the video from your computer
cap = cv2.VideoCapture('video.mp4')

# Loop through the video and extract each frame
while cap.isOpened():
    # Read the current frame
    ret, frame = cap.read()

    # Check if the video has ended
    if not ret:
        break

    # Display the current frame
    cv2.imshow('Frame', frame)

    # Wait for a key press and exit if the user presses 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
