import pdfplumber
from typing import Dict, List, Any
import os
import json


def _convert_to_serializable(obj: Any) -> Any:
    """Recursively convert any object to JSON serializable format"""
    if obj is None:
        return None
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, (int, float, bool)):
        return obj
    elif isinstance(obj, (list, tuple)):
        return [_convert_to_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: _convert_to_serializable(value) for key, value in obj.items()}
    else:
        # For any other type, convert to string
        return str(obj)


def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from PDF file"""
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        raise Exception(f"Error extracting text: {str(e)}")
    return text.strip()


def extract_tables_from_pdf(file_path: str) -> List[Any]:
    """Extract tables from PDF file, converting all values to JSON serializable format"""
    tables = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_tables = page.extract_tables()
                if page_tables:
                    for table in page_tables:
                        # Convert all values in the table to be JSON serializable
                        serializable_table = _convert_to_serializable(table)
                        tables.append(serializable_table)
    except Exception as e:
        raise Exception(f"Error extracting tables: {str(e)}")
    return tables


def get_pdf_metadata(file_path: str) -> Dict:
    """Extract metadata from PDF file"""
    metadata = {}
    try:
        with pdfplumber.open(file_path) as pdf:
            metadata = {
                "total_pages": len(pdf.pages),
                "author": pdf.metadata.get("Author") if pdf.metadata and pdf.metadata.get("Author") else None,
                "title": pdf.metadata.get("Title") if pdf.metadata and pdf.metadata.get("Title") else None,
                "created": pdf.metadata.get("CreationDate") if pdf.metadata and pdf.metadata.get("CreationDate") else None,
            }
    except Exception as e:
        raise Exception(f"Error extracting metadata: {str(e)}")
    
    # Ensure metadata is JSON serializable
    return _convert_to_serializable(metadata)
