from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from analyzer import analyze_text
import os

app = FastAPI()

# Šablóny (HTML)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

class MessageRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_message(request: MessageRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text is empty")
    result = analyze_text(request.text)
    return result

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
