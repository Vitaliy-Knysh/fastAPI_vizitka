from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def get_root(request: Request):
    context = {
        "title": "Мой замечательный сайт-визитка",
        "some_content": "КОНТЕНТ",
        "request": request
    }
    return templates.TemplateResponse("index.html", context)
