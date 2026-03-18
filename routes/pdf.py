from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from models import PDFProcessResponse, ExtractedData, ErrorResponse
from utils import extract_text_from_pdf, extract_tables_from_pdf, get_pdf_metadata

router = APIRouter(prefix="/api/pdf", tags=["PDF Processing"])

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB


@router.post("/upload", response_model=PDFProcessResponse)
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload and process a PDF file
    - Accepts PDF file upload
    - Extracts text, tables, and metadata
    - Returns structured JSON response
    """
    
    # Validate file extension
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Only PDF files are accepted."
        )
    
    # Validate file size
    file_content = await file.read()
    if len(file_content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File size exceeds maximum limit of {MAX_FILE_SIZE / (1024*1024):.0f}MB"
        )
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    try:
        # Save file
        with open(file_path, "wb") as f:
            f.write(file_content)
        
        # Extract data
        text = extract_text_from_pdf(file_path)
        tables = extract_tables_from_pdf(file_path)
        metadata = get_pdf_metadata(file_path)
        
        # Check if any text was extracted
        if not text.strip():
            raise Exception("No text content found in PDF")
        
        # Prepare response
        extracted_data = ExtractedData(
            text=text,
            tables=tables,
            metadata=metadata
        )
        
        return PDFProcessResponse(
            success=True,
            file_name=file.filename,
            message="PDF processed successfully",
            data=extracted_data
        )
    
    except Exception as e:
        # Clean up uploaded file on error
        if os.path.exists(file_path):
            os.remove(file_path)
        
        raise HTTPException(
            status_code=400,
            detail=f"Error processing PDF: {str(e)}"
        )
    
    finally:
        # Clean up uploaded file after processing
        if os.path.exists(file_path):
            os.remove(file_path)


@router.get("/health")
async def health_check():
    """Health check endpoint for PDF API"""
    return {
        "status": "healthy",
        "service": "PDF Processing API"
    }
