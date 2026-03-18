from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Any


class ExtractedData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    text: str
    tables: List[Any] = []  # Flexible table structure
    metadata: dict = {}


class PDFProcessResponse(BaseModel):
    success: bool
    file_name: str
    message: str
    data: Optional[ExtractedData] = None


class ErrorResponse(BaseModel):
    success: bool
    message: str
    error_code: str
