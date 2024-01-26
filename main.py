from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account



app = FastAPI()
Base = declarative_base()

# Database Configuration
SQLALCHEMY_DATABASE_URL = "postgresql://myuser:vaskinho@localhost/mydatabase"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database Model
class LanguageDetection(Base):
    __tablename__ = "language_detection"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    detected_language = Column(String, nullable=False)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Text(BaseModel):
    """
    Model representing text input for language detection.
    Attributes:
        content (str): The text content to be analyzed for language detection.
    """
    content: str

def detect_language(text: str) -> str:
    """
    Detect the language of a given text using Google Cloud Translation API.
    
    Args:
        text (str): The text for which the language needs to be detected.

    Returns:
        str: Detected language code (e.g., 'en' for English).

    Raises:
        Exception: If an error occurs during language detection.
    """
    try:
        key_path = "/Users/joaovasco/Desktop/unbabel/extra/my_fastapi_project/alien-aileron-412301-6a984fd02879.json"
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])

        client = translate.Client(credentials=credentials)
        result = client.detect_language(text)
        return result['language']
    except Exception as e:
        # Log the exception for debugging purposes
        # In a production environment, consider using a logging framework
        print(f"An error occurred in detect_language: {e}")
        # Re-raise the exception to be handled by the caller
        raise


@app.post("/detect-language/")
def detect_language_endpoint(text: Text, db: Session = Depends(get_db)):
    if not text.content:
        raise HTTPException(status_code=400, detail="No content provided")
    
    language = detect_language(text.content)

    # Insert into database
    language_record = LanguageDetection(content=text.content, detected_language=language)
    db.add(language_record)
    db.commit()

    return {"language": language}

# Create the database tables
Base.metadata.create_all(bind=engine)


