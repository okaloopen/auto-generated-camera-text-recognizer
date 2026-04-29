from pydantic import BaseModel

class OCRResponse(BaseModel):
    """Response model containing extracted text."""
    text: str
