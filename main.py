from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import markdown

app = FastAPI()
templates = Jinja2Templates(directory="htmls")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/data", StaticFiles(directory="data"), name="data")
app.mount("/htmls", StaticFiles(directory="htmls"), name="htmls")
app.mount("/projects", StaticFiles(directory="projects"), name="projects")

@app.get("/")
def read_root(request: Request):
    with open('data/home.json') as f:
        data = json.load(f)
    return templates.TemplateResponse("home.html", {"request": request, "data": data})

@app.get("/project/{name}")
def project(name: str, request: Request):
    try:
        with open(f'projects/{name}.md', 'r', encoding='utf-8') as f:
            md_content = f.read()
        html_content = markdown.markdown(md_content)
        return templates.TemplateResponse("project.html", {"request": request, "content": html_content, "title": name.replace('_', ' ').title()})
    except FileNotFoundError:
        return templates.TemplateResponse("404.html", {"request": request, "error": "Project not found"}, status_code=status.HTTP_404_NOT_FOUND)

@app.get("/projects")
def projects_list(request: Request):
    try:
        with open('data/projects.json') as f:
            projects = json.load(f)
    except FileNotFoundError:
        projects = []
    
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects})

@app.get('/favicon.ico')
def favicon():
    return FileResponse('static/favicon.ico')

@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request, "error": "Page not found"}, status_code=status.HTTP_404_NOT_FOUND)
