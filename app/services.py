import cv2
import logging
import pytesseract
import numpy as np

class CameraService:
    """Service for capturing frames from a camera and performing OCR."""

    def __init__(self, camera_index: int = 0) -> None:
        self.camera_index = camera_index
        self.logger = logging.getLogger(self.__class__.__name__)
        # Initialize video capture
        self.cap = cv2.VideoCapture(camera_index)

    def capture_frame(self) -> np.ndarray:
        """Capture a single frame from the camera."""
        if not self.cap.isOpened():
            self.logger.error("Camera could not be opened")
            raise RuntimeError("Camera could not be opened")
        ret, frame = self.cap.read()
        if not ret:
            self.logger.error("Failed to capture frame")
            raise RuntimeError("Failed to capture frame")
        return frame

    def extract_text(self, frame: np.ndarray) -> str:
        """Run OCR on a frame and return the extracted text."""
        # Convert the image to grayscale for better OCR performance
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        return text

    def capture_and_recognize(self) -> str:
        """Capture a frame and return extracted text."""
        frame = self.capture_frame()
        return self.extract_text(frame)

    def release(self) -> None:
        """Release the camera resource."""
        if self.cap.isOpened():
            self.cap.release()
