from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.pdf import router as pdf_router

app = FastAPI(
    title="AIMPLOY Backend",
    description="PDF Processing API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(pdf_router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to AIMPLOY Backend",
        "version": "1.0.0",
        "api_docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
