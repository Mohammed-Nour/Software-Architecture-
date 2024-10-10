import cv2
from filters.grayscale_filter import apply_grayscale
from filters.mirror_filter import apply_mirror
from filters.resize_filter import apply_resize
from filters.edge_detection_filter import apply_edge_detection


def test_filters():
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    cv2.namedWindow('Grayscale Filter', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Grayscale Filter', 300, 300)
    cv2.moveWindow('Grayscale Filter', 0, 0)

    cv2.namedWindow('Mirror Filter', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Mirror Filter', 300, 300)
    cv2.moveWindow('Mirror Filter', 400, 0)

    cv2.namedWindow('Resize Filter', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Resize Filter', 300, 300)
    cv2.moveWindow('Resize Filter', 400, 500)

    cv2.namedWindow('Edge Detection Filter', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Edge Detection Filter', 300, 300)
    cv2.moveWindow('Edge Detection Filter', 0, 500)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply Grayscale filter and display
        grayscaled_frame = apply_grayscale(frame)
        cv2.imshow('Grayscale Filter', grayscaled_frame)

        # Apply Mirror filter and display
        mirrored_frame = apply_mirror(frame)
        cv2.imshow('Mirror Filter', mirrored_frame)

        # Apply Resize filter and display
        resized_frame = apply_resize(frame)
        cv2.imshow('Resize Filter', resized_frame)

        # Apply Edge Detection filter and display
        result_frame = apply_edge_detection(frame)
        cv2.imshow('Edge Detection Filter', result_frame)

        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    test_filters()
