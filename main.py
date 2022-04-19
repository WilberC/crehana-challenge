from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import Base, engine
from application.views.sync_data import sync_data_router, sync_all_data
from application.views.user_view import user_router
from application.views.post_view import post_router
from application.views.comment_view import comment_router
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
app.include_router(sync_data_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
# ===============

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_item(request: Request):
    if request.headers.get('Content-Type') == 'application/json':
        return sync_all_data()
    else:
        context = {"request": request}
        return templates.TemplateResponse("home.html", context)
