
# FastAPI Language Detection Service

## Overview

This project is a language detection service built with FastAPI, integrated with Google Cloud Translation API, and backed by a PostgreSQL database. It demonstrates best practices in developing and deploying web applications using FastAPI, Google Cloud services, and relational database management systems. It saves the words and the corresponding language they were written in, in the Database. Additionally, it features a sentiment analysis component, utilizing a Go-based sentiment analysis tool to evaluate the sentiment of the input text.

## Features

- **FastAPI Framework**: Utilizes FastAPI for building high-performance APIs with Python 3.7+, leveraging standard Python type hints.
- **Asynchronous Handling**: Capable of handling asynchronous requests, enhancing performance in demanding scenarios.
- **Google Cloud Translation API Integration**: Seamlessly integrates with Google Cloud Translation API for accurate language detection.
- **PostgreSQL Database Integration**: Incorporates a PostgreSQL database to store and manage detected language data.
- **Automatic API Documentation**: Features automatically generated interactive API documentation using Swagger UI.
- **Sentiment Analysis**: Offers sentiment analysis through a Go-based tool, providing insights into the emotional tone behind texts.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- Google Cloud Account with Translation API access
- PostgreSQL database
- Go 1.21.6 (for sentiment analysis component)

### Installation

Clone the repository:
```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/joaovasco01/Unbabel_Technologies.git)
```
Navigate to the project directory:
```bash
cd Unbabel_Technologies
```
Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # Unix/macOS
venv\Scripts\activate # Windows
```
Install Python dependencies:
```
pip install -r requirements.txt
```
Ensure Go is installed and set up the Go environment for the sentiment analysis tool:
- Install Go from the [official website](https://golang.org/dl/).
- Navigate to the `sentiment_analysis` directory and run `go build` to compile the Go program.

### Configuration

- Set up the Google Cloud service account and download the JSON key file.
- Place the key file in a secure location and update `GOOGLE_CREDENTIALS` in `main.py` with its path.
- Ensure PostgreSQL is installed and running. Update `SQLALCHEMY_DATABASE_URL` in `main.py` with your database credentials.
- For sentiment analysis, ensure the compiled Go executable is accessible to `main.py`, adjusting the path in the `analyze_sentiment_with_go` function as necessary.

### Running the Application

Start the FastAPI server:
```css
uvicorn main:app --reload
```
The service will be available at `http://127.0.0.1:8000`.
Access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Usage

### Detecting Language

To detect the language of a text, send a POST request to the `/detect-language/` endpoint with a JSON payload containing the text:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/detect-language/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"content": "Hello, world"}'
```

### Analyzing Sentiment

To analyze the sentiment of a text, send a POST request to the `/analyze-sentiment/` endpoint with a JSON payload containing the text:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/analyze-sentiment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"content": "I love sunny days!"}'
```

The detected language and sentiment analysis results will be returned in the response and stored in the PostgreSQL database for record-keeping and further analysis.


## Database Results

<img width="536" alt="Screenshot 2024-01-26 at 1 38 38 AM" src="https://github.com/joaovasco01/Unbabel_Technologies/assets/61276111/4bd2f772-14b1-4372-b61d-a372b278834b">

