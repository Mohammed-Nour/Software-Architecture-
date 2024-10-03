import cv2

def apply_edge_detection(frame):
    return cv2.Canny(frame, 100, 200)
