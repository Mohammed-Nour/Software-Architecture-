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

    # Input video
    cv2.namedWindow('Original Video', cv2.WND_PROP_FULLSCREEN)
    cv2.resizeWindow('Original Video', 600, 600)
    cv2.moveWindow('Original Video', 100, 100)

    # Preparation for output video
    cv2.namedWindow('Processed Video', cv2.WND_PROP_FULLSCREEN)
    cv2.resizeWindow('Processed Video', 600, 600)
    cv2.moveWindow('Processed Video', 800, 100)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Original Video', frame)

        # Apply filters sequentially
        grayscaled_frame = apply_grayscale(frame)
        mirrored_frame = apply_mirror(grayscaled_frame)
        resized_frame = apply_resize(mirrored_frame)
        result_frame = apply_edge_detection(resized_frame)

        # Display processed frame
        cv2.imshow('Processed Video', result_frame)

        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
