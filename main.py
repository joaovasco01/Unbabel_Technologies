from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
import os
import subprocess

# Initialize the FastAPI app
app = FastAPI()

# Base class for SQLAlchemy models
Base = declarative_base()

# Google Cloud credentials for Translation API
GOOGLE_CREDENTIALS = '/Users/joaovasco/Desktop/unbabel/extra/my_fastapi_project/alien-aileron-412301-6a984fd02879.json'

# Database connection URL
SQLALCHEMY_DATABASE_URL = "postgresql://myuser:vaskinho@localhost/mydatabase"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Configure sessionmaker for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class LanguageDetection(Base):
    """
    SQLAlchemy ORM model for the language_detection table.
    Stores detected language information for texts.

    Attributes:
        id (Integer): The primary key.
        content (Text): The original text whose language was detected.
        detected_language (String): The ISO code of the detected language.
    """
    __tablename__ = "language_detection"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    detected_language = Column(String, nullable=False)

class SentimentAnalysisRequest(BaseModel):
    content: str


def get_db():
    """
    Generator that provides a database session for each request.
    Yields a session and ensures its closure after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Text(BaseModel):
    """
    Pydantic model for the request body.
    Used for validating the data received in the request.

    Attributes:
        content (str): The text content to be analyzed for language detection.
    """
    content: str


def detect_language(text: str) -> str:
    """
    Detects the language of the given text using Google Cloud Translation API.

    Args:
        text (str): Text whose language needs to be detected.

    Returns:
        Detected language code (e.g., 'en' for English).

    Raises:
        Exception: Any exceptions that occur during the API call.
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(
            GOOGLE_CREDENTIALS, scopes=["https://www.googleapis.com/auth/cloud-platform"])
        client = translate.Client(credentials=credentials)
        result = client.detect_language(text)
        return result['language']
    except Exception as e:
        # Consider replacing print with logging for production use
        print(f"An error occurred in detect_language: {e}")
        raise

@app.post("/detect-language/")
def detect_language_endpoint(text: Text, db: Session = Depends(get_db)):
    """
    FastAPI endpoint to detect the language of provided text and store in database.

    Args:
        text (Text): Instance of Text model containing content to be analyzed.
        db (Session): Database session dependency injected by FastAPI.

    Returns:
        JSON response with the detected language.
    """
    if not text.content:
        raise HTTPException(status_code=400, detail="No content provided")
    
    detected_language = detect_language(text.content)

    # Create and add new record to the database
    language_record = LanguageDetection(content=text.content, detected_language=detected_language)
    db.add(language_record)
    db.commit()

    return {"language": detected_language}

def analyze_sentiment_with_go(text: str) -> str:
    try:
        # Adjust the path to your Go executable as necessary
        result = subprocess.run(["./sentiment_analysis", text], capture_output=True, text=True, check=True)
        sentiment_score = result.stdout.strip()
        return sentiment_score
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while analyzing sentiment: {e}")
        raise HTTPException(status_code=500, detail="Sentiment analysis failed")
        
@app.post("/analyze-sentiment/")
def analyze_sentiment(request: SentimentAnalysisRequest):
    sentiment_score = analyze_sentiment_with_go(request.content)
    return {"text": request.content, "sentiment_score": sentiment_score}


# Auto-create all tables based on Base metadata
Base.metadata.create_all(bind=engine)
