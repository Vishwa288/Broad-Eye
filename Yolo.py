import cv2
import time
from ultralytics import YOLO

# Load YOLO model (make sure best.pt is in same folder)
model = YOLO("best_ncnn_model")

# Initialize the USB webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Set webcam resolution for better clarity
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Start the video stream
prev_time = 0
print("Starting real-time detection... Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Run YOLO model on the captured frame
    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    # Calculate FPS (Frames Per Second)
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    # Display FPS on the frame
    cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the annotated frame
    cv2.imshow("Component Detection - YOLO", annotated_frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Detection stopped.")
