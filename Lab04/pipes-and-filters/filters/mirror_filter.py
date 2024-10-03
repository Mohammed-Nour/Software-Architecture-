import cv2

def apply_mirror(frame):
    return cv2.flip(frame, 1)  # Flip horizontally
