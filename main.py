from fastapi import FastAPI, Form
from src.store import store_text

app = FastAPI()


@app.post("/")
async def summarize(text: str = Form(...)):
    document_id = store_text(text)
    
    return {"document_id": document_id}
