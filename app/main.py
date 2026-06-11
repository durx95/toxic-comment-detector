from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import predict

app = FastAPI(title="Toxic Comment Detector API")

# 🔹 Static files (CSS, JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 🔹 Templates (HTML)
templates = Jinja2Templates(directory="app/templates")

# 🔹 Home Route (Frontend UI)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

# 🔹 API Routes
app.include_router(predict.router)