from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import Base, engine
from application.views.sync_data import sync_data_router, sync_all_data

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(sync_data_router)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_item(request: Request):
    if request.headers.get('Content-Type') == 'application/json':
        return sync_all_data()
    else:
        context = {"request": request}
        return templates.TemplateResponse("home.html", context)
