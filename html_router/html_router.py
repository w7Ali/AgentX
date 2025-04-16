

# from fastapi import APIRouter, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

# html_app = APIRouter()
# templates = Jinja2Templates(directory="templates")

# @html_app.get("/", response_class=HTMLResponse)
# async def welcome(request: Request):
#     return templates.TemplateResponse("index.html", {
#         "request": request,
#         "active_page": "home"
#     })

# @html_app.get("/index/insert_data_to_index", response_class=HTMLResponse)
# async def show_upload_form(request: Request):
#     return templates.TemplateResponse("insert_data_to_index.html", {
#         "request": request,
#         "active_page": "upload"
#     })

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

html_app = APIRouter()
templates = Jinja2Templates(directory="templates")

@html_app.get("/", response_class=HTMLResponse)
async def welcome(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "active_page": "home"
    })

@html_app.get("/html/insert_data_to_index", response_class=HTMLResponse)
async def show_upload_form(request: Request):
    return templates.TemplateResponse("insert_data_to_index.html", {
        "request": request,
        "active_page": "upload"
    })

@html_app.get("/html/create_agent", response_class=HTMLResponse)
async def create_agent(request: Request):
    return templates.TemplateResponse("create_agent.html", {
        "request": request,
        "active_page": "create_agent"
    })

@html_app.get("/html/list_agents", response_class=HTMLResponse)
async def list_agents(request: Request):
    return templates.TemplateResponse("list_agents.html", {
        "request": request,
        "active_page": "list_agent"
    })

@html_app.get("/html/delete_agent", response_class=HTMLResponse)
async def delete_agent(request: Request):
    return templates.TemplateResponse("delete_agent.html", {
        "request": request,
        "active_page": "delete_agent"
    })

@html_app.get("/html/ask_agent", response_class=HTMLResponse)
async def ask_agent(request: Request):
    return templates.TemplateResponse("ask_agent.html", {
        "request": request,
        "active_page": "ask_agent"
    })
