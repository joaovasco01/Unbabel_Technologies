FastAPI Language Detection Service

Overview

This project is a language detection service built with FastAPI, integrated with Google Cloud Translation API, and backed by a PostgreSQL database. It demonstrates best practices in developing and deploying web applications using FastAPI, Google Cloud services, and relational database management systems.

Features

FastAPI Framework: Utilizes FastAPI for building high-performance APIs with Python 3.7+, leveraging standard Python type hints.
Asynchronous Handling: Capable of handling asynchronous requests, enhancing performance in demanding scenarios.
Google Cloud Translation API Integration: Seamlessly integrates with Google Cloud Translation API for accurate language detection.
PostgreSQL Database Integration: Incorporates a PostgreSQL database to store and manage detected language data.
Automatic API Documentation: Features automatically generated interactive API documentation using Swagger UI.
Getting Started

Prerequisites
Python 3.7+
FastAPI
Uvicorn (ASGI server)
Google Cloud Account with Translation API access
PostgreSQL database
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repository-name.git
Navigate to the project directory:
bash
Copy code
cd your-repository-name
Create a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate # Unix/macOS
venv\Scripts\activate # Windows
Configuration
Set up the Google Cloud service account and download the JSON key file.
Place the key file in a secure location and update GOOGLE_CREDENTIALS in main.py with its path.
Ensure PostgreSQL is installed and running. Update SQLALCHEMY_DATABASE_URL in main.py with your database credentials.
Running the Application
Start the FastAPI server:
css
Copy code
uvicorn main:app --reload
The service will be available at http://127.0.0.1:8000.
Access the interactive API documentation at http://127.0.0.1:8000/docs.
Usage

To detect the language of a text, send a POST request to the /detect-language/ endpoint with a JSON payload containing the text:

bash
Copy code
curl -X 'POST' \
  'http://127.0.0.1:8000/detect-language/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"content": "Hello, world"}'
The detected language will be returned in the response and stored in the PostgreSQL database for record-keeping and further analysis.
