FastAPI Language Detection Service

Overview

This project is a language detection service built with FastAPI and integrated with Google Cloud Translation API. It provides an endpoint that accepts text input and returns the detected language. The project is structured to demonstrate best practices in developing and deploying modern web applications with FastAPI and Google Cloud services.

Features

FastAPI Framework: Utilizes the modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
Asynchronous Handling: Capable of handling asynchronous requests, making it suitable for high-performance scenarios.
Google Cloud Translation API Integration: Seamlessly integrates with Google Cloud Translation API for efficient and accurate language detection.
Automatic API Documentation: Includes automatically generated interactive API documentation (Swagger UI).
Getting Started

Prerequisites
Python 3.7+
FastAPI
Uvicorn (ASGI server)
Google Cloud Account and Translation API access

Installation
Clone the repository:
git clone https://github.com/your-username/your-repository-name.git

Navigate to the project directory:
cd your-repository-name

Create a virtual environment 
python -m venv venv
source venv/bin/activate  # On Unix/macOS
venv\Scripts\activate  # On Windows

Configuration
Set up the Google Cloud service account and download the JSON key file.
Update the key_path in main.py with the path to your Google Cloud service account JSON key file.
Running the Application

Start the FastAPI server:
bash
Copy code
uvicorn main:app --reload
The service will be available at http://127.0.0.1:8000.
Access the interactive API documentation at http://127.0.0.1:8000/docs.


Usage
To detect the language of a text, send a POST request to /detect-language/ endpoint with a JSON payload containing the text:

bash
Copy code
curl -X 'POST' \
  'http://127.0.0.1:8000/detect-language/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"content": "Hello, world"}'
