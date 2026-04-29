# Auto-Generated Camera Text Recognizer

## Overview
This project implements a real-time camera-based text recognition API using **FastAPI**, **OpenCV**, and **Tesseract**. It is designed to capture an image frame from a connected camera, perform optical character recognition (OCR), and expose the result via an HTTP API. The service is asynchronous and uses a modular architecture with clear separation of concerns.

## Features
- **Real-time OCR**: Captures a frame from the default camera device and extracts text using Tesseract.
- **Asynchronous API**: Built on FastAPI with async endpoints for high performance.
- **Modular Design**: Core functionality is encapsulated in a `CameraService` class, and data schemas are defined with Pydantic models.
- **Logging**: Provides structured logging to facilitate debugging and monitoring.
- **Extensible**: The service can be extended to support different camera devices or alternative OCR engines.

## Architecture Overview
The project is organized into modules under the `app` package to promote maintainability and testability:

```
app/
├── __init__.py          # Package marker
├── main.py              # FastAPI application and API routes
├── models.py            # Pydantic models for request/response data
└── services.py          # CameraService class for capturing and processing frames
requirements.txt         # Python dependencies
README.md
```

### Modules

- **main.py**: Creates the FastAPI app, configures logging, and defines the `/health` and `/capture` endpoints.
- **models.py**: Defines the `OCRResponse` model used to serialize the response body containing recognized text.
- **services.py**: Implements `CameraService` which opens the default camera, captures a single frame, converts it to grayscale, runs Tesseract OCR, and returns the extracted text.

## Installation
1. Clone the repository or download the source code.
2. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure that [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is installed on your system and available in your system PATH.

## Usage
Run the application with Uvicorn:

```bash
uvicorn app.main:app --reload
```

Once the server is running you can access the following endpoints:

### GET /health
Returns a simple JSON object to indicate that the service is running.

```bash
curl http://localhost:8000/health
```

### POST /capture
Captures a frame from the camera and returns the extracted text. This endpoint does not require a request body.

```bash
curl -X POST http://localhost:8000/capture
```

Response example:
```json
{
  "text": "Recognized text from the camera frame"
}
```

## API Documentation
The API is documented automatically by FastAPI. Once the server is running, navigate to `/docs` in your browser to view an interactive Swagger UI or `/redoc` for alternative documentation.

| Method | Endpoint   | Description                                       |
|-------:|:-----------|:--------------------------------------------------|
| GET    | `/health`  | Health check endpoint                             |
| POST   | `/capture` | Capture a frame and return recognized text        |

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/okaloopen/auto-generated-camera-text-recognizer/issues) if you want to contribute.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
