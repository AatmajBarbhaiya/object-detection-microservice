# 🚀 AI Object Detection Microservice

A powerful and scalable microservice-based object detection system that leverages cutting-edge AI to identify objects in images with high accuracy. Built with FastAPI and PyTorch, this solution provides a seamless user experience through a modern web interface.

![Architecture](https://img.shields.io/badge/Architecture-Microservice-blue)
![Framework](https://img.shields.io/badge/Framework-FastAPI-green)
![AI](https://img.shields.io/badge/AI-PyTorch-orange)
![Container](https://img.shields.io/badge/Container-Docker-blue)

---

## ✨ Features

🎯 **High-Accuracy Detection:** Utilizes SSD300 with VGG16 backbone trained on COCO dataset  
⚡ **Real-time Processing:** Optimized for fast inference with confidence scoring  
🌐 **Modern Web Interface:** Responsive UI with drag-and-drop upload functionality  
🔍 **Detailed Analytics:** Bounding box visualization with class labels and confidence scores  
📊 **JSON Export:** Structured data output for further analysis  
🐳 **Docker Containerized:** Easy deployment with Docker Compose  
🔄 **RESTful APIs:** Well-documented endpoints for integration  
📱 **Mobile-Friendly:** Responsive design that works on all devices  

---

---

## 🛠️ Technology Stack

### **Backend Services**
- FastAPI (Modern Python web framework)
- PyTorch & TorchVision (Deep learning)
- OpenCV (Computer vision)
- Uvicorn (ASGI server)

### **Frontend**
- HTML5, CSS3, JavaScript
- Jinja2 Templates
- Responsive Web Design

### **Infrastructure**
- Docker & Docker Compose
- Microservice Architecture
- CORS-enabled APIs

---

## 📦 Installation & Setup

### ✅ Prerequisites
- Docker & Docker Compose
- Python 3.8+ (for local development)

---

### 🚀 Quick Start with Docker

```bash
git clone <repository-url>
cd object-detection-microservice
docker-compose up --build
```

# 🚀 AI Object Detection Microservice

A powerful and scalable microservice-based object detection system that leverages cutting-edge AI to identify objects in images with high accuracy. Built with FastAPI and PyTorch, this solution provides a seamless user experience through a modern web interface.

---

## 🔗 Access the Application

### Web Interface  
http://localhost:8081  

### AI Service API  
http://localhost:8001  

### API Documentation  
http://localhost:8001/docs  

---

## 🧪 Manual Installation (Development)

### ✅ Set up AI Service
```bash
cd ai-service
pip install -r requirements.txt
python app_ai.py
```
## Set up UI Service
```bash
cd ui-service
pip install -r requirements.txt
python app_ui.py
```
## 🎮 Usage

✅ Web Interface

Open http://localhost:8081

- Click Choose File to upload an image

- Click Detect Objects

- View bounding boxes and detection metadata

- Download processed image or JSON results

## ✅ API Integration

### Detect Objects Endpoint

```bash
curl -X POST "http://localhost:8001/detect" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_image.jpg"
```
### Response Format
```bash
{
  "filename": "image.jpg",
  "detections": [
    {
      "class": "person",
      "confidence": 0.95,
      "bbox": {
        "x1": 100.5,
        "y1": 150.2,
        "x2": 300.8,
        "y2": 450.6
      }
    }
  ],
  "detection_count": 1,
  "image_with_boxes": "uuid_detected_image.jpg"
}
```
## 🔧 API Endpoints

### AI Service (Port 8001)
GET / — Service health check
GET /health — Detailed health status
POST /detect — Main object detection endpoint

### UI Service (Port 8081)
GET / — Web interface
POST /upload — Image upload endpoint
GET /download/{filename} — File download

## 🎯 Detection Capabilities

The system can detect 80+ common objects, including:
🚗 Vehicles (cars, trucks, buses, bicycles)
🏠 Indoor objects (chairs, tables, TV, laptop)
🍕 Food items (pizza, banana, apple, bottle)
🐶 Animals (cat, dog, bird, horse)
👥 People and accessories

## 🚀 Performance

Model: SSD300 with VGG16 backbone
Classes: 80 COCO dataset categories
Inference Time: ~2–3 seconds on CPU
Accuracy: State-of-the-art object detection
Scalability: Containerized microservices

## 🔒 Error Handling

✅ Comprehensive input validation
✅ Graceful error recovery
✅ Detailed logging for debugging
✅ User-friendly error messages

## 🙏 Acknowledgments

COCO Dataset for training data
PyTorch team
FastAPI framework
Docker containerization solutions


## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request


## 📞 Contact

**Developer:** Aatmaj  
**Contact:** aatmaj017@gamil.com  
**Year:** 2025
