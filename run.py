#!/usr/bin/env python3
"""
Barangay Survey Generator - Startup Script
Run this script to start the FastAPI application
"""

import uvicorn
from app import app

if __name__ == "__main__":
    print("🚀 Starting Barangay Survey Generator...")
    print("📊 A simple survey tool for barangay communities")
    print("🌐 Access the application at: http://localhost:8000")
    print("📖 Documentation available at: http://localhost:8000/docs")
    print("=" * 50)
    
    uvicorn.run(
        "app:app",  # Use import string for reload to work
        host="0.0.0.0", 
        port=8000, 
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )
