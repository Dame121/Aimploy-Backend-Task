# 🚀 AIMPLOY Backend - PDF Processing API

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

A production-ready **FastAPI-based REST API** for intelligent PDF processing and data extraction. Seamlessly extract text, tables, and metadata from PDF documents with robust error handling, comprehensive validation, and an intuitive testing interface.

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [API Endpoints](#-api-endpoints)
- [Usage Examples](#-usage-examples)
- [Testing](#-testing)
- [Error Handling](#-error-handling)
- [Future Enhancements](#-future-enhancements)

---

## 🎯 Overview

AIMPLOY Backend is a robust PDF processing service designed for enterprise-level document handling. It provides a clean REST API interface for extracting valuable information from PDF files, including:

- 📝 **Full Text Extraction** - Extract all textual content while preserving structure
- 📊 **Table Recognition** - Automatically detect and extract complex tables
- 📋 **Metadata Retrieval** - Extract document properties and information
- 🔍 **Intelligent Validation** - Comprehensive file type and size validation
- 🎨 **Interactive UI** - Built-in web interface for API testing and exploration

---

## ✨ Key Features

✅ **Reliable PDF Processing** - Handle PDF uploads up to 50MB with validation  
✅ **Structured Data Extraction** - Extract text, tables, and metadata in JSON format  
✅ **Smart Error Handling** - Comprehensive error messages and HTTP status codes  
✅ **Automatic Cleanup** - Temporary files are securely removed after processing  
✅ **CORS Enabled** - Ready for cross-origin requests and web integrations  
✅ **Interactive API Documentation** - Swagger UI for easy endpoint exploration  
✅ **Web Testing UI** - Professional interface for testing all API endpoints  
✅ **Production Ready** - Health checks and service monitoring endpoints  

---

## 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Framework | FastAPI | 0.104.1 |
| Server | Uvicorn | 0.24.0 |
| PDF Processing | PDFPlumber | 0.10.3 |
| Data Validation | Pydantic | 2.5.0 |
| Python | Python | 3.12.5 |
| Environment | python-dotenv | 1.0.0 |

---

## 📁 Project Structure

```
AIMPLOY Backend/
│
├── 📄 main.py                     # FastAPI application entry point
├── 📊 models.py                   # Pydantic response models & schemas
├── 🛠️  utils.py                    # PDF extraction utility functions
├── 📋 requirements.txt             # Python dependencies
├── 📖 README.md                    # Project documentation
├── 🌐 index.html                   # Interactive testing UI
├── 🔧 create_sample_pdf.py        # Sample PDF generator for testing
│
└── 📁 routes/
    ├── __init__.py
    └── pdf.py                      # PDF processing endpoints & logic
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (Tested on Python 3.12.5)
- **pip** or **conda** for package management
- **Git** for version control

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "AIMPLOY Backend"
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

   Server will start at: `http://localhost:8000`

---

## 🔌 API Endpoints

### 1. Health Check Endpoint

**Description:** Verify API service is running and healthy

```http
GET /api/pdf/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "PDF Processing API"
}
```

**Status Code:** `200 OK`

---

### 2. PDF Upload & Processing Endpoint

**Description:** Upload and process a PDF file to extract text, tables, and metadata

```http
POST /api/pdf/upload
Content-Type: multipart/form-data

Parameters:
  - file: <PDF file> (required, max 50MB)
```

**Success Response (200):**
```json
{
  "success": true,
  "file_name": "document.pdf",
  "message": "PDF processed successfully",
  "data": {
    "text": "Extracted text content...",
    "tables": [
      [["Header1", "Header2"], ["Row1", "Data1"]],
      [["Header3", "Header4"], ["Row2", "Data2"]]
    ],
    "metadata": {
      "pages": 5,
      "title": "Document Title",
      "author": "Author Name",
      "created": "2024-01-15",
      "modified": "2024-01-16",
      "producer": "ReportLab PDF Producer"
    }
  }
}
```

**Error Response (400/413):**
```json
{
  "detail": "Error message describing what went wrong"
}
```

---

## 📚 Usage Examples

### Using cURL

**Test Health Endpoint:**
```bash
curl -X GET http://localhost:8000/api/pdf/health
```

**Upload and Process PDF:**
```bash
curl -X POST -F "file=@document.pdf" http://localhost:8000/api/pdf/upload
```

### Using Python Requests

```python
import requests

# Health check
response = requests.get("http://localhost:8000/api/pdf/health")
print(response.json())

# Upload PDF
with open("document.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post(
        "http://localhost:8000/api/pdf/upload",
        files=files
    )
    print(response.json())
```

### Using the Web Interface

1. Open browser: `http://localhost:8000/index.html`
2. Click "Check Health" to verify API status
3. Upload a PDF file using the drag-and-drop interface
4. View structured results with formatted tables and metadata
5. Switch between "Structured View" and "Raw JSON" tabs

---

## 🧪 Testing

### Generate Sample PDF

Create a test PDF file:
```bash
python create_sample_pdf.py
```

This generates `sample_document.pdf` with sample content for testing.

### API Documentation

- **Interactive Swagger UI:** `http://localhost:8000/docs`
- **ReDoc Documentation:** `http://localhost:8000/redoc`

---

## ⚠️ Error Handling

The API provides clear, actionable error messages:

| Error | Status | Message |
|-------|--------|---------|
| Invalid file format | 400 | `Invalid file format. Only PDF files are accepted.` |
| File too large | 413 | `File size exceeds maximum limit of 50MB` |
| Processing error | 400 | `Error processing PDF: [details]` |
| No text found | 400 | `No text content found in PDF` |

All errors include HTTP status codes and detailed descriptions for easy debugging.

---

## 🔮 Future Enhancements

- [ ] Add image extraction from PDFs
- [ ] Implement OCR for scanned documents
- [ ] Support for multiple file formats (DOCX, XLSX, PPTX)
- [ ] Batch file processing
- [ ] User authentication and API keys
- [ ] Rate limiting and quota management
- [ ] Advanced text analysis (NLP, sentiment analysis)
- [ ] Database integration for result storage
- [ ] Admin dashboard for monitoring
- [ ] Docker containerization

---

## 📝 License

This project is licensed under the MIT License.

---

## 👤 Author

**AIMPLOY Team**

*Building intelligent document processing solutions for the modern enterprise.*

---

## 📧 Support & Questions

For questions, issues, or feature requests, please open an issue in the repository.

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
