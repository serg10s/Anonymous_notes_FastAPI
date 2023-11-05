from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

app = FastAPI()

# Создайте экземпляр Jinja2Templates и укажите путь к вашей директории с шаблонами.
templates = Jinja2Templates(directory="templates")


class InfoData(BaseModel):
    password: str
    data: str | None = None


@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def process_form(data: str = Form(...), password: str = Form(...)):
    result = InfoData(password=password, data=data)
    JSONResponse(content=result.dict())


@app.get("/show_text", response_class=HTMLResponse)
async def show_text(request: Request):
    return templates.TemplateResponse("show_text.html", {"request": request})
