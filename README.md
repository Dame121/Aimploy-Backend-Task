# AIMPLOY Backend - PDF Processing API

A FastAPI-based REST API for processing PDF files, extracting structured data including text, tables, and metadata with comprehensive error handling.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Sample Requests & Responses](#sample-requests--responses)
- [Error Handling](#error-handling)
- [Configuration](#configuration)

---

## Features

✅ **PDF File Upload** - Accept PDF files with validation
✅ **Text Extraction** - Extract all text content from PDF pages
✅ **Table Extraction** - Extract structured table data
✅ **Metadata Extraction** - Get PDF metadata (pages, author, title, creation date)
✅ **File Validation** - Extension and size checks (max 50MB)
✅ **Error Handling** - Comprehensive error responses
✅ **Automatic Cleanup** - Temporary files are automatically removed
✅ **Interactive API Docs** - Swagger UI at `/docs`

---

## Project Structure

```
AIMPLOY Backend/
├── main.py                 # Application entry point
├── models.py              # Pydantic response models
├── utils.py               # PDF extraction utilities
├── requirements.txt       # Project dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── routes/
    ├── __init__.py
    └── pdf.py             # PDF processing endpoints
```

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone/Download Project
```powershell
cd "d:\AIMPLOY Backend"
```

### Step 2: Create Virtual Environment
```powershell
python -m venv venv
```

### Step 3: Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 5: Run the Server
```powershell
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Step 6: Access the API
- **API Base URL:** `http://localhost:8000`
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## API Endpoints

### 1. Health Check
**Endpoint:** `GET /api/pdf/health`

**Description:** Check if the PDF processing service is running

**Response:**
```json
{
  "status": "healthy",
  "service": "PDF Processing API"
}
```

---

### 2. Upload and Process PDF
**Endpoint:** `POST /api/pdf/upload`

**Description:** Upload a PDF file to extract text, tables, and metadata

**Request:**
- **Method:** POST
- **Content-Type:** multipart/form-data
- **Parameter:** `file` (form-data, required) - PDF file to process
- **Max File Size:** 50 MB

**Response Model (Success - 200 OK):**
```json
{
  "success": true,
  "file_name": "document.pdf",
  "message": "PDF processed successfully",
  "data": {
    "text": "extracted text content...",
    "tables": [
      [
        ["Header 1", "Header 2"],
        ["Row 1 Col 1", "Row 1 Col 2"]
      ]
    ],
    "metadata": {
      "total_pages": 5,
      "author": "John Doe",
      "title": "Document Title",
      "created": "2024-01-15T10:30:00"
    }
  }
}
```

---

## Sample Requests & Responses

### Using Swagger UI (Recommended)
1. Open `http://localhost:8000/docs`
2. Find the `POST /api/pdf/upload` endpoint
3. Click "Try it out"
4. Select your PDF file
5. Click "Execute"

### Using cURL

**Command:**
```bash
curl -X POST -F "file=@path/to/document.pdf" http://localhost:8000/api/pdf/upload
```

### Using PowerShell

**Command:**
```powershell
$filePath = "C:\path\to\document.pdf"
$uri = "http://localhost:8000/api/pdf/upload"
$form = @{ file = Get-Item -Path $filePath }
$response = Invoke-WebRequest -Uri $uri -Method Post -Form $form
$response.Content | ConvertFrom-Json | ConvertTo-Json -Depth 10
```

### Using Python Requests

```python
import requests

url = "http://localhost:8000/api/pdf/upload"
files = {"file": open("document.pdf", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

### Using JavaScript/Fetch

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

fetch('http://localhost:8000/api/pdf/upload', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

---

## Error Handling

### 1. Invalid File Format
**Status Code:** 400 Bad Request

**Response:**
```json
{
  "detail": "Invalid file format. Only PDF files are accepted."
}
```

**Cause:** Uploaded file is not a PDF

---

### 2. File Size Exceeds Limit
**Status Code:** 413 Payload Too Large

**Response:**
```json
{
  "detail": "File size exceeds maximum limit of 50MB"
}
```

**Cause:** PDF file is larger than 50MB

---

### 3. PDF Processing Error
**Status Code:** 400 Bad Request

**Response:**
```json
{
  "detail": "Error processing PDF: No text content found in PDF"
}
```

**Cause:** PDF could not be processed or contains no extractable text

---

### 4. No File Provided
**Status Code:** 422 Unprocessable Entity

**Response:**
```json
{
  "detail": [
    {
      "loc": ["body", "file"],
      "msg": "Field required",
      "type": "missing"
    }
  ]
}
```

**Cause:** No file was provided in the request

---

## Configuration

### File Upload Settings

Edit `routes/pdf.py` to customize:

```python
UPLOAD_DIR = "uploads"  # Directory to temporarily store uploads
MAX_FILE_SIZE = 50 * 1024 * 1024  # Maximum file size (currently 50MB)
```

### API Settings

Edit `main.py` to customize:

```python
app = FastAPI(
    title="AIMPLOY Backend",
    description="PDF Processing API",
    version="1.0.0"
)
```

### Server Settings

Run with custom host/port:

```powershell
python main.py --host 0.0.0.0 --port 8080
```

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| fastapi | 0.104.1 | Web framework |
| uvicorn | 0.24.0 | ASGI server |
| pydantic | 2.5.0 | Data validation |
| pdfplumber | 0.10.3 | PDF extraction |
| python-multipart | 0.0.6 | File upload support |
| python-dotenv | 1.0.0 | Environment management |

---

## Troubleshooting

### Issue: "Module not found" errors
**Solution:** Ensure virtual environment is activated and run `pip install -r requirements.txt`

### Issue: Port 8000 already in use
**Solution:** Use a different port:
```powershell
python main.py
# Edit main.py and change port=8000 to another port like 8001
```

### Issue: PDF not extracting text
**Solution:** The PDF might be image-based (scanned). Consider using OCR tools for scanned PDFs.

### Issue: CORS errors in browser
**Solution:** CORS is already configured to accept all origins. Check browser console for specific errors.

---

## Development

### Running Tests (Future)
```powershell
pytest tests/
```

### Code Formatting
```powershell
black .
```

### Type Checking
```powershell
mypy .
```

---

## API Response Format

All successful responses follow this format:

```json
{
  "success": true,
  "file_name": "string",
  "message": "string",
  "data": {
    "text": "string",
    "tables": [],
    "metadata": {}
  }
}
```

All error responses follow this format:

```json
{
  "detail": "string"
}
```

---

## License

This project is part of AIMPLOY Backend services.

---

## Support

For issues or questions, please refer to the API documentation at `http://localhost:8000/docs`
