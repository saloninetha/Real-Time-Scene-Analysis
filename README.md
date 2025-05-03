

## Project Overview
This is an AI-powered Webcam Image Analyzer that uses multimodal capabilities to analyze real-time images captured from your webcam. It allows users to ask natural language questions about the image, and provides smart, context-aware responses using Gemini 2.0 Flash and external web search tools.


## Features
- Real-time webcam image capture
- AI-powered image content analysis
- Natural language question support
- Context-aware responses using web search
- Clean and user-friendly interface


## Prerequisites
- Python 3.8+
- pip (Python package manager)
- A webcam-enabled device
- Google API key (for Gemini integration)
- .env file to store your API key securely



## Installation

1. Clone the repository:
```bash
git clone https://github.com/saloninetha/real-time-scene-detection.git
cd real-time-scene-detection
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate    # For Windows
# Or: source venv/bin/activate    # For macOS/Linux

```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
```bash
streamlit run app.py

```

## Technologies Used
- Streamlit
- Google Gemini API (via google-generativeai)
- phidata
- DuckDuckGo Search API
- Python packages: dotenv, Pillow, opencv-python, tempfile, pathlib

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

