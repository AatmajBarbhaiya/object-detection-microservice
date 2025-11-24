from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import requests
import os
import json
import uuid

app = FastAPI(title="UI Object Detection Service")

# Templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# AI service URL (will be overridden by Docker)
AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://localhost:8000")

# Create output directory
os.makedirs("output", exist_ok=True)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            return JSONResponse(
                status_code=400,
                content={"error": "File must be an image"}
            )
        
        # Send image to AI service
        files = {"file": (file.filename, await file.read(), file.content_type)}
        
        response = requests.post(
            f"{AI_SERVICE_URL}/detect",
            files=files
        )
        
        if response.status_code != 200:
            return JSONResponse(
                status_code=response.status_code,
                content={"error": "AI service error", "details": response.text}
            )
        
        result = response.json()
        
        # Save results to output directory
        output_id = str(uuid.uuid4())
        json_filename = f"output/{output_id}_detections.json"
        image_filename = f"output/{output_id}_detected_image.jpg"
        
        # Save JSON results
        with open(json_filename, "w") as f:
            json.dump(result, f, indent=2)
        
        # Copy image with bounding boxes
        if os.path.exists(result["image_with_boxes"]):
            import shutil
            shutil.copy2(result["image_with_boxes"], image_filename)
        
        return JSONResponse(content={
            "success": True,
            "detections": result["detections"],
            "json_file": json_filename,
            "image_file": image_filename
        })
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal server error: {str(e)}"}
        )

@app.get("/download/{filename:path}")
async def download_file(filename: str):
    return FileResponse(filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)