
# FastAPI Language Detection Service

## Overview

This project is a language detection service built with FastAPI, integrated with Google Cloud Translation API, and backed by a PostgreSQL database. It demonstrates best practices in developing and deploying web applications using FastAPI, Google Cloud services, and relational database management systems. It saves the words and the corresponding language they were written in, in the Database.

## Features

- **FastAPI Framework**: Utilizes FastAPI for building high-performance APIs with Python 3.7+, leveraging standard Python type hints.
- **Asynchronous Handling**: Capable of handling asynchronous requests, enhancing performance in demanding scenarios.
- **Google Cloud Translation API Integration**: Seamlessly integrates with Google Cloud Translation API for accurate language detection.
- **PostgreSQL Database Integration**: Incorporates a PostgreSQL database to store and manage detected language data.
- **Automatic API Documentation**: Features automatically generated interactive API documentation using Swagger UI.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- Google Cloud Account with Translation API access
- PostgreSQL database

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repository-name.git
   ```
2. Navigate to the project directory:
   ```
   cd your-repository-name
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate # Unix/macOS
   venv\Scripts\activate # Windows
   ```

### Configuration

1. Set up the Google Cloud service account and download the JSON key file. 
2. Place the key file in a secure location and update `GOOGLE_CREDENTIALS` in `main.py` with its path.
3. Ensure PostgreSQL is installed and running. Update `SQLALCHEMY_DATABASE_URL` in `main.py` with your database credentials.

### Running the Application

1. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```
2. The service will be available at `http://127.0.0.1:8000`.
3. Access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Usage

To detect the language of a text, send a POST request to the `/detect-language/` endpoint with a JSON payload containing the text:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/detect-language/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"content": "Hello, world"}'
```

The detected language will be returned in the response and stored in the PostgreSQL database for record-keeping and further analysis.

## Database Results

<img width="536" alt="Screenshot 2024-01-26 at 1 38 38 AM" src="https://github.com/joaovasco01/Unbabel_Technologies/assets/61276111/4bd2f772-14b1-4372-b61d-a372b278834b">

