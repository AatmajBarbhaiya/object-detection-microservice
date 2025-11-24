\documentclass[11pt]{article}

\usepackage[a4paper,margin=0.8in]{geometry}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{tcolorbox}
\usepackage{listings}
\usepackage{courier}
\usepackage{titlesec}

\renewcommand{\familydefault}{\sfdefault}
\setlist[itemize]{leftmargin=1.2em}
\lstset{
  basicstyle=\ttfamily\small,
  breaklines=true
}

\title{\LARGE 🚀 AI Object Detection Microservice}
\date{}

\begin{document}
\maketitle

A powerful and scalable microservice-based object detection system that leverages cutting-edge AI to identify objects in images with high accuracy. Built with FastAPI and PyTorch, this solution provides a seamless user experience through a modern web interface.

\begin{itemize}
\item \url{https://img.shields.io/badge/Architecture-Microservice-blue}
\item \url{https://img.shields.io/badge/Framework-FastAPI-green}
\item \url{https://img.shields.io/badge/AI-PyTorch-orange}
\item \url{https://img.shields.io/badge/Container-Docker-blue}
\end{itemize}

\section*{✨ Features}
\begin{itemize}
\item 🎯 High-Accuracy Detection using SSD300 with VGG16 backbone
\item ⚡ Real-time Processing with optimized inference
\item 🌐 Modern responsive web interface with drag-and-drop upload
\item 🔍 Bounding box visualization with class labels
\item 📊 JSON export for downstream processing
\item 🐳 Docker containerized deployment
\item 🔄 RESTful APIs for integration
\item 📱 Mobile friendly UI
\end{itemize}

\section*{🏗️ System Architecture}
\begin{tcolorbox}
\ttfamily
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐ \\
│   Client        │    │   UI Service     │    │   AI Service    │ \\
│   (Browser)     │◄──►│   (FastAPI)      │◄──►│   (FastAPI)     │ \\
│                 │    │   Port: 8081     │    │   Port: 8001    │ \\
└─────────────────┘    └──────────────────┘    └─────────────────┘ \\
          │                        │ \\
          └───── Shared Volume ────┘ \\
                 (/output)
\end{tcolorbox}

\section*{🛠️ Technology Stack}
\textbf{Backend:}
\begin{itemize}
\item FastAPI
\item PyTorch \& TorchVision
\item OpenCV
\item Uvicorn
\end{itemize}

\textbf{Frontend:}
\begin{itemize}
\item HTML5, CSS3, JavaScript
\item Jinja2 Templates
\item Responsive Web Design
\end{itemize}

\textbf{Infrastructure:}
\begin{itemize}
\item Docker \& Docker Compose
\item Microservices
\item CORS-enabled APIs
\end{itemize}

\section*{📦 Installation \& Setup}
\subsection*{Quick Start with Docker}
\begin{lstlisting}[language=bash]
git clone <repository-url>
cd object-detection-microservice
docker-compose up --build
\end{lstlisting}

Access:
\begin{itemize}
\item Web UI: http://localhost:8081
\item AI API: http://localhost:8001
\item Docs: http://localhost:8001/docs
\end{itemize}

\subsection*{Manual Development Setup}
\textbf{AI Service:}
\begin{lstlisting}[language=bash]
cd ai-service
pip install -r requirements.txt
python app_ai.py
\end{lstlisting}

\textbf{UI Service:}
\begin{lstlisting}[language=bash]
cd ui-service
pip install -r requirements.txt
python app_ui.py
\end{lstlisting}

\section*{🎮 Usage}
\subsection*{Web Interface}
Upload image → Detect → View bounding boxes → Download results

\subsection*{API Integration}
\begin{lstlisting}[language=bash]
curl -X POST "http://localhost:8001/detect" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_image.jpg"
\end{lstlisting}

\subsection*{Sample JSON Response}
\begin{lstlisting}[language=json]
{
  "filename": "image.jpg",
  "detections": [
    {
      "class": "person",
      "confidence": 0.95,
      "bbox": { "x1": 100.5, "y1": 150.2, "x2": 300.8, "y2": 450.6 }
    }
  ],
  "detection_count": 1,
  "image_with_boxes": "uuid_detected_image.jpg"
}
\end{lstlisting}

\section*{📁 Project Structure}
\begin{tcolorbox}
\ttfamily
object-detection-microservice/ \\
├── ai-service/ \\
│   ├── app_ai.py \\
│   ├── detection.py \\
│   ├── requirements.txt \\
│   └── Dockerfile \\
├── ui-service/ \\
│   ├── app_ui.py \\
│   ├── templates/ \\
│   ├── static/ \\
│   ├── requirements.txt \\
│   └── Dockerfile \\
├── output/ \\
├── docker-compose.yml \\
└── README.md
\end{tcolorbox}

\section*{⭐ Other Sections}
\begin{itemize}
\item 🎯 Detection Capabilities
\item ⚙️ Configuration
\item 🚀 Performance
\item 🔒 Error Handling
\item 🤝 Contributing
\item 📄 License (MIT)
\item 🙏 Acknowledgments
\end{itemize}

\end{document}
