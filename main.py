from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

app = FastAPI()

class Text(BaseModel):
    content: str

def detect_language(text: str) -> str:
    try:
        # Path to your service account key file
        key_path = "/Users/joaovasco/Desktop/unbabel/extra/my_fastapi_project/alien-aileron-412301-6a984fd02879.json"
        
        # Create credentials using the key file
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])

        # Pass the credentials to the client
        client = translate.Client(credentials=credentials)
        result = client.detect_language(text)
        return result['language']
    except Exception as e:
        print(f"An error occurred: {e}")
        # Return the exception message for debugging purposes
        return str(e)

        return "Error"

@app.post("/detect-language/")
def detect_language_endpoint(text: Text):
    if not text.content:
        raise HTTPException(status_code=400, detail="No content provided")
    language = detect_language(text.content)
    return {"language": language}

