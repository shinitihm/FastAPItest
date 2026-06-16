from fastapi import FastAPI,Depends,HTTPException,Header
from dotenv import load_dotenv
import os
import ollama

app = FastAPI()

load_dotenv()
ENDPOINT = 'generate'
x_api_key = os.getenv("API_KEY")

API_KEYS = {x_api_key:  5}

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    
    credits = API_KEYS.get(x_api_key)
    
    if credits <= 0:
        raise HTTPException(status_code=403, detail="Insufficient credits")
    
    return x_api_key

@app.post(f"/{ENDPOINT}")
def generate(prompt: str,api_key: str = Depends(verify_api_key)):
    API_KEYS[api_key] -= 1
    response = ollama.chat(model='mistral', messages=[#system prompt 
        {"role": "system", "content": "Você é um assistente virtual muito útil. Você DEVE sempre responder em português do Brasil, independente do idioma da pergunta"},
        {"role": "user", "content": prompt}
    ])
    return {"response": response["message"]["content"]}
    
