import cv2
from filters.grayscale_filter import apply_grayscale
from filters.mirror_filter import apply_mirror
from filters.resize_filter import apply_resize
from filters.edge_detection_filter import apply_edge_detection

def main():
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply filters sequentially
        frame = apply_grayscale(frame)
        frame = apply_mirror(frame)
        frame = apply_resize(frame)
        frame = apply_edge_detection(frame)

        # Display processed frame
        cv2.imshow('Processed Video', frame)

        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
