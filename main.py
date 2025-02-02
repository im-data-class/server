from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()


####################
# String responses
####################
@app.get("/")
def homepage_str(request: Request):
    return "Hello World!"


####################
# HTML responses
####################
# @app.get("/")
# async def homepage_html():
#     html_content = """
#     <html>
#         <head>
#             <title>My App</title>
#         </head>
#         <body>
#             <h1>Hello World</h1>
#         </body>
#     </html>
#     """
#     return HTMLResponse(content=html_content, status_code=200)

####################
# Template responses
####################
# templates = Jinja2Templates(directory="templates")


# @app.get("/")
# async def homepage_template(request: Request):
#     return templates.TemplateResponse(request=request, name="page_min.html")
