from typing import Annotated

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


app = FastAPI()


@app.get("/")
def homepage_get(request: Request):
    name = "Hello World"
    return templates.TemplateResponse(
        request=request, name="page.html", context={"name": name}
    )


@app.post("/")
def homepage_post(name: Annotated[str, Form()], request: Request):
    print(name)
    return templates.TemplateResponse(
        request=request, name="page.html", context={"name": name}
    )
