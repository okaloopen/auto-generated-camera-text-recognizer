import asyncio
import logging
from fastapi import FastAPI, HTTPException
from .services import CameraService
from .models import OCRResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Camera Text Recognizer")

# Instantiate the camera service
camera_service = CameraService()

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

@app.post("/capture", response_model=OCRResponse)
async def capture_text():
    """
    Capture a frame from the camera and return recognized text.
    """
    try:
        # Offload blocking camera capture to a thread
        text = await asyncio.to_thread(camera_service.capture_and_recognize)
        return OCRResponse(text=text)
    except Exception as e:
        logger.exception("Error capturing and recognizing text: %s", e)
        raise HTTPException(status_code=500, detail="Failed to capture and recognize text")

@app.on_event("shutdown")
async def shutdown_event():
    """Release resources on shutdown."""
    camera_service.release()
