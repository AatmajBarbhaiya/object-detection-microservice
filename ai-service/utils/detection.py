import cv2
import numpy as np
import torch
import torchvision
from PIL import Image
import json
import os

class ObjectDetector:
    def __init__(self):
        self.model = self.load_model()
        self.classes = self.load_classes()
        self.transform = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
        ])
    
    def load_model(self):
        """Load a lightweight pre-trained model"""
        # Use a smaller, faster model for CPU
        model = torchvision.models.detection.ssd300_vgg16(pretrained=True)
        model.eval()  # Set to evaluation mode
        return model
    
    def load_classes(self):
        """Load COCO class names"""
        return [
            '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
            'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
            'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
            'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
            'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
            'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
            'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
            'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
            'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
            'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard',
            'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A',
            'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
        ]
    
    def detect_objects(self, image_path):
        """Perform object detection on image"""
        # Load and preprocess image
        image = Image.open(image_path).convert('RGB')
        image_tensor = self.transform(image).unsqueeze(0)
        
        # Perform detection
        with torch.no_grad():
            predictions = self.model(image_tensor)
        
        # Process results
        detections = []
        for i in range(len(predictions[0]['boxes'])):
            score = predictions[0]['scores'][i].item()
            
            # Filter by confidence threshold
            if score > 0.5:
                bbox = predictions[0]['boxes'][i].tolist()
                class_id = predictions[0]['labels'][i].item()
                
                detection = {
                    "class": self.classes[class_id],
                    "confidence": score,
                    "bbox": {
                        "x1": bbox[0],
                        "y1": bbox[1],
                        "x2": bbox[2],
                        "y2": bbox[3]
                    }
                }
                detections.append(detection)
        
        return detections
    
    def draw_bounding_boxes(self, image_path, detections, output_path):
        """Draw bounding boxes on image and save"""
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        for detection in detections:
            bbox = detection['bbox']
            class_name = detection['class']
            confidence = detection['confidence']
            
            # Draw rectangle
            start_point = (int(bbox['x1']), int(bbox['y1']))
            end_point = (int(bbox['x2']), int(bbox['y2']))
            color = (0, 255, 0)  # Green
            thickness = 2
            image = cv2.rectangle(image, start_point, end_point, color, thickness)
            
            # Draw label
            label = f"{class_name}: {confidence:.2f}"
            label_position = (int(bbox['x1']), int(bbox['y1']) - 10)
            image = cv2.putText(image, label, label_position, 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)
        
        # Convert back to BGR for saving
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(output_path, image)
        return output_path