from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import json
from utils.detection import ObjectDetector
import uuid

app = FastAPI(title="AI Object Detection Service")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize detector
try:
    detector = ObjectDetector()
    print("✅ Object detector initialized successfully")
except Exception as e:
    print(f"❌ Failed to initialize object detector: {e}")
    detector = None

# Create output directories
os.makedirs("/tmp/uploads", exist_ok=True)
os.makedirs("/tmp/outputs", exist_ok=True)

@app.get("/")
async def root():
    return {"message": "AI Object Detection Service", "status": "healthy"}

@app.get("/health")
async def health():
    return {"status": "healthy", "detector_ready": detector is not None}

@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    if detector is None:
        raise HTTPException(status_code=500, detail="Object detector not initialized")
    
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Generate unique filename
        file_id = str(uuid.uuid4())
        upload_path = f"/tmp/uploads/{file_id}_{file.filename}"
        output_image_path = f"/tmp/outputs/{file_id}_detected_{file.filename}"
        
        # Save uploaded file
        with open(upload_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        print(f"🔍 Processing image: {file.filename}")
        
        # Perform object detection
        detections = detector.detect_objects(upload_path)
        
        # Draw bounding boxes
        detector.draw_bounding_boxes(upload_path, detections, output_image_path)
        
        # Return just the filename (not full path) for UI service
        output_filename = f"{file_id}_detected_{file.filename}"
        
        # Prepare response
        response = {
            "filename": file.filename,
            "detections": detections,
            "detection_count": len(detections),
            "image_with_boxes": output_filename  # Just the filename, not full path
        }
        
        print(f"✅ Detection complete: {len(detections)} objects found")
        print(f"📁 Output file: {output_filename}")
        
        return response
        
    except Exception as e:
        print(f"❌ Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting AI Object Detection Service...")
    uvicorn.run(app, host="0.0.0.0", port=8000)