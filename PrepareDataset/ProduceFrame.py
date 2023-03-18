import cv2

# Initialize camera capture
cap = cv2.VideoCapture(0)

# Set frame dimensions and format
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define output file name and format
output_filename = 'output'
output_format = '.jpg'

# Initialize frame count
frame_count = 0

# Loop through frames
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame was successfully captured
    if not ret:
        break

    # Save frame as image
    cv2.imwrite(output_filename + str(frame_count) + output_format, frame)

    # Increase frame count
    frame_count += 1

    # Display the resulting frame
    cv2.imshow('frame',frame)

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
