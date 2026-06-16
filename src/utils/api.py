from fastapi import FastAPI
import ollama

app = FastAPI()

@app.post("/generate")
def generate(prompt: str,model:str):
    response = ollama.chat(model=model,messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}
    
