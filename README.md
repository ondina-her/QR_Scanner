# QR Code Scanner - Software Tester Portfolio

## 📋 Project Overview
This project demonstrates a **FastAPI** backend with a **QR code scanner** frontend.  
It includes **Selenium + pytest** automated tests aligned with JIRA Sprint tasks (STQC-5 to STQC-9).

## 🚀 Features
- FastAPI server with QR scanner page
- Camera-based QR code scanning
- SQLAlchemy database integration (SQLite for demo)
- Automated UI tests with Selenium + pytest

## 🧪 Test Coverage
- STQC-5 Environment setup
- STQC-6 Valid QR test
- STQC-7 Invalid QR test
- STQC-8 Empty request test
- STQC-9 UI validation


## 📂 Project Structure
app/           # FastAPI backend
static/        # CSS, JS, images
templates/     # HTML templates
Test/          # Selenium + pytest tests

## 📦 Requirements
All dependencies are listed in `requirements.txt`.  
Install them with:
```bash
pip install -r requirements.txt
```

## ⚙️ Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/qr-scanner-portfolio.git

##Virtual Enviroment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows



## ▶️ Usage
#Run the app
uvicorn app.app:app --reload

#Run test
pytest Test/ -v
- Open http://localhost:8000 in your browser.

- Click Start Scanner and show a QR code to your camera.

- Decoded text will appear in the result box.

## 📜 License
This project is licensed under the MIT License.

##Author
Made by Ondina Hernandez— Software Tester Portfolio Project