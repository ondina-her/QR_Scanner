# QR Code Scanner - QA Testing Portfolio Project

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![Tests](https://img.shields.io/badge/tests-pytest-green.svg)]()

## 📋 Project Overview

This project is part of my software testing portfolio and demonstrates my approach to quality assurance on a real web application. The application combines a FastAPI backend with a camera-based QR code scanner interface, and I used it to practice functional testing, UI testing, API testing, and basic performance testing.

## 🎯 Project Goals

- Validate the core functionality of QR code scanning
- Verify the user interface and error handling behavior
- Test API endpoints through positive and negative scenarios
- Document and present testing work in a professional portfolio format

## 🚀 Key Features

- FastAPI backend for handling web requests
- Camera-based QR code scanning interface
- SQLite database integration for demo purposes
- Automated UI testing with Selenium and pytest
- API testing using Postman
- Performance testing using Apache JMeter

## 🗂️ Database Design

The backend uses two main database tables:

- Item → represents the decoded QR content such as a link or text
- Scan → represents each scanning event, including the source and related QR content

Each scan is linked to an item through the item_id relationship.

## 🧪 Testing Approach

This project highlights several important QA activities:

- Functional Testing: verifying that valid and invalid QR codes are handled correctly
- UI Testing: checking that the interface behaves as expected and that key elements are visible and functional
- API Testing: validating CRUD operations, error handling, and negative scenarios
- Performance Testing: evaluating the system under load and reviewing response behavior

These activities demonstrate my understanding of both manual and automated testing techniques.

## 🧪 Test Coverage

The project includes both manual and automated testing coverage:

- Manual and API testing using Postman for item and scan endpoints
- Automated UI testing using Selenium and pytest
- Test cases aligned with QA scenarios such as environment setup, valid QR scan, invalid QR scan, empty input, and UI validation

## 📋 Project Scope and Objectives

The main objective of this project was to validate that the QR scanner application functions correctly under different testing scenarios. The focus includes functional correctness, UI reliability, API behavior, and overall user experience.

Detailed test cases and QA documentation are available in [docs/test_cases.md](docs/test_cases.md).

## 🧪 Test Cases Documentation

A detailed test case document covering STQC-5 to STQC-9 is included in this repository. It covers:

- Functional tests with Selenium for valid QR, invalid QR, empty QR, and UI validation
- API tests with Postman for item and scan endpoints
- Negative cases such as empty fields and invalid IDs

## 📊 Performance Testing with JMeter

As part of my QA portfolio, I also created a JMeter test plan to evaluate the API under different load conditions. The report includes metrics such as response time, throughput, and error rate, which helps demonstrate my understanding of performance testing concepts.

🔗 [View the full JMeter Performance Report](https://ondina-her.github.io/jmeter-performance-report/)

## 📂 Project Structure

- app/ → FastAPI backend
- static/ → CSS, JavaScript, and images
- templates/ → HTML pages
- Test/ → Selenium tests, pytest tests, and Postman collection
- docs/ → test case documentation and QA templates

## 📦 Requirements

All dependencies are listed in requirements.txt. Install them with:

```bash
pip install -r requirements.txt
```

## ⚙️ Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install the required dependencies

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

## ▶️ Running the Application

Run the app with:

```bash
uvicorn app.app:app --reload
```

Then open:

```text
http://localhost:8000
```

## ▶️ Running Tests

```bash
pytest Test/ -v
```

## 🧪 API Testing with Postman

This project also includes a Postman collection for testing the API endpoints related to items and scans. The collection covers happy-path requests, error handling, and negative test cases.

To use it:

1. Open Postman
2. Import the collection from the Test/postman folder
3. Run the requests to validate API behavior

## 🐞 Bug Report Template

A reusable bug report template is available in [docs/bug_report_template.md](docs/bug_report_template.md).

## 📜 License

This project is licensed under the MIT License.

## Author

Made by Ondina Hernandez
Software Tester Portfolio Project