from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.database import init_db
from app.routes import auth_routes, planner_routes, history_routes

app = FastAPI(title="PocketSmart AI")

init_db()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(auth_routes.router)
app.include_router(planner_routes.router)
app.include_router(history_routes.router)


@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.get("/{page_name}", response_class=HTMLResponse)
async def read_page(request: Request, page_name: str):
    valid_pages = [
        "login",
        "register",
        "dashboard",
        "home_planner",
        "party_planner",
        "jewelry_planner",
        "history",
        "testimonials"
    ]

    if page_name in valid_pages:
        return templates.TemplateResponse(
            request=request,
            name=f"{page_name}.html",
            context={"request": request}
        )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )