from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import Base, engine
from application.views.rest.sync_data import sync_all_data
from application.routes.rest_api_routes import rest_api_routes
from application.routes.graphql_routes import graphql_routes
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Routes ===
rest_api_routes(app)
graphql_routes(app)
# ===============

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_item(request: Request):
    if request.headers.get('Content-Type') == 'application/json':
        return sync_all_data()
    else:
        context = {"request": request}
        return templates.TemplateResponse("home.html", context)
